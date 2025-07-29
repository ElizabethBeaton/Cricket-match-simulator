#sets up the sqllite database using sqlalchemy
#loads all the csvs files into the correct database tables

import csv # lets you read .csv files eaily, row by row
from sqlalchemy import create_engine # create_engine connects python to the sqlite database
from sqlalchemy.orm import sessionmaker 
from models import Base, Venue, Game, Simulation 

#defining the database connection url (using sqlite in the project root)
DATABASE_URL = "sqlite:///./cricket.db" 

#create the database engine (connects python to the database)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#this function sets up the database and loads all 3 csvs
def init_db():
    Base.metadata.drop_all(bind=engine) 
    Base.metadata.create_all(bind=engine) 

    session = SessionLocal()

# load venues.csv and add to database
    with open("data/venues.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            session.add(Venue(
                venue_id=int(row["venue_id"]),
                venue_name=row["venue_name"]
            ))

#load games.csv and add to db
    with open("data/games.csv", newline='') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            session.add(Game(
                game_id=idx, #assigns a unique is based on rw index
                home_team=row["home_team"],
                away_team=row["away_team"],
                venue_id=int(row["venue_id"]),
                date=row["date"]
            ))

#load simulations.csv and add to db
    with open("data/simulations.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            session.add(Simulation(
                team_id=int(row["team_id"]),
                team=row["team"],
                simulation_run=int(row["simulation_run"]),
                results=float(row["results"])
            ))

#commit all records to the db and close the session
    session.commit()
    session.close()

