from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

#base class all models will inherit from
Base = declarative_base()

#venue model - represents the "venues" table in the database
class Venue(Base):
    __tablename__ = "venues" #table name in db
    venue_id = Column(Integer, primary_key=True, index=True) # unique id for each venue
    venue_name = Column(String) #name of venues

class Game(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True, index=True) #unique id for each game
    home_team = Column(String)
    away_team = Column(String)
    venue_id = Column(Integer, ForeignKey("venues.venue_id")) #foreign key to venue table
    date = Column(String)  # Could also use Date type

class Simulation(Base):
    __tablename__ = "simulations"
    id = Column(Integer, primary_key=True, index=True) #auto-incremented id
    team_id = Column(Integer) 
    team = Column(String)
    simulation_run = Column(Integer) #which sim run it was
    results = Column(Float)
