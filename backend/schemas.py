from pydantic import BaseModel 
from typing import List #

#schema for returning a venue object to the frontend from the /venues route
class VenueOut(BaseModel):
    venue_id: int
    venue_name: str
#allows conversion from sqlalchemy model to pydantic model
    model_config = {
        "from_attributes": True 
    }

# schema for returning a game object to the frontend from the /games route
class GameOut(BaseModel):
    game_id: int
    home_team: str
    away_team: str
    venue_id: int
    date: str

    model_config = {
        "from_attributes": True
    }

# sub-schema for returning a simulation object to the frontend
# this is the response for the /simulation/{game_id} route
# each record represents the simulated score for one team in one run
class SimulationOut(BaseModel):
    id: int
    team_id: int
    team: str
    simulation_run: int
    results: float

    model_config = {
        "from_attributes": True
    }

class VenueHistoryItem(BaseModel):
    venue: str #venue name
    date: str #date of the match


#main schema returned by /matchup-insight route
class MatchupInsightOut(BaseModel):
    home_team: str
    away_team: str
    home_win_percentage: float #calculate win percentage for home team
    histogram: List[dict] #histogram data for score (bin and score counts)
    venue_history: List[VenueHistoryItem] #list of past venues and dates
