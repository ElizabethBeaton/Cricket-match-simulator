from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import routes  
from database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  #without this, browser security would block frontend-backend communication
    allow_origins=["http://localhost:5173"],  #  allow requests from React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

init_db() 
app.include_router(routes.router) 



#this is my backend entry point. i initiiase the fastapi app, enable cors so my front end can talk to it, load all my csvs into a relational sqllite database using init_db(), and register all the route logic using fastapis router system