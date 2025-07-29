from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Game, Venue, Simulation
from schemas import GameOut, VenueOut, SimulationOut, MatchupInsightOut, VenueHistoryItem
from typing import List
from collections import defaultdict

#create a fastAPI router to define all api endpoints
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get /games - returns all agmes from database
@router.get("/games", response_model=List[GameOut]) 
def get_games(db: Session = Depends(get_db)):
    return db.query(Game).all()

# get /venues - returns all venues from database
@router.get("/venues", response_model=List[VenueOut])
def get_venues(db: Session = Depends(get_db)):
    return db.query(Venue).all()

# get .simulation/{game_id} - returns simulations for both teams in the game
@router.get("/simulations/{game_id}", response_model=List[SimulationOut])
def get_simulations(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    home = db.query(Simulation).filter(Simulation.team == game.home_team).all()
    away = db.query(Simulation).filter(Simulation.team == game.away_team).all()
    return home + away

# get /matchup-insight - combines venue history, simulations, and win statts
@router.get("/matchup-insight", response_model=MatchupInsightOut) 
def get_matchup_insight(
    home_team: str = Query(...),
    away_team: str = Query(...),
    db: Session = Depends(get_db)
):
    # validation - teams but be different
    if home_team == away_team:
        raise HTTPException(status_code=400, detail="Teams must be different")

#get all games between these teams
    games = db.query(Game).filter(Game.home_team == home_team, Game.away_team == away_team).all()
    if not games:
        raise HTTPException(status_code=404, detail="No matching games found")

# build venue history from those games given
    venue_history = []
    venues = {v.venue_id: v.venue_name for v in db.query(Venue).all()}
    for game in games:
        venue_name = venues.get(game.venue_id, "Unknown")
        venue_history.append(VenueHistoryItem(venue=venue_name, date=game.date))

#get all simulation results for both teams
    home_sims = db.query(Simulation).filter(Simulation.team == home_team).all()
    away_sims = db.query(Simulation).filter(Simulation.team == away_team).all()

#ensure simulations are present and aligned
    if not home_sims or not away_sims or len(home_sims) != len(away_sims):
        raise HTTPException(status_code=400, detail="Simulation data is invalid or missing")

#calculate win percentae for home team
    wins = sum(1 for h, a in zip(home_sims, away_sims) if h.results > a.results)
    win_percentage = (wins / len(home_sims)) * 100

#build histogram bins
    BIN_SIZE = 10
    grouped = defaultdict(lambda: {home_team: 0, away_team: 0})
    for sim in home_sims:
        bin = (int(sim.results) // BIN_SIZE) * BIN_SIZE
        grouped[bin][home_team] += 1
    for sim in away_sims:
        bin = (int(sim.results) // BIN_SIZE) * BIN_SIZE
        grouped[bin][away_team] += 1

#convert grouped data into list format for charting
    histogram = [
        {
            "bin": k,
            home_team: v[home_team],
            away_team: v[away_team],
        }
        for k, v in sorted(grouped.items())
    ]

#return the complete matchup insight response
    return MatchupInsightOut(
        home_team=home_team,
        away_team=away_team,
        home_win_percentage=round(win_percentage, 2),
        histogram=histogram,
        venue_history=venue_history
    )



