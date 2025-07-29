# Pluto Cricket Match Simulator

A full stack application that allows users to simulate cricket matchups between local teams.

---

## Stack
- **Frontend**: React + TypeScript (Vite)
- **Backend**: FastAPI (Python), SQLite
- **Data**: Loaded from CSVs on startup

---

## How to Run

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## Local URLs

- **Frontend UI**: [http://localhost:5173](http://localhost:5173)
- **Backend API**: [http://localhost:8000](http://localhost:8000)

---

## API Endpoints
- `/games` – Get all games
- `/venues` – Get all venues
- `/simulations/{game_id}` – Get score simulations
- `/matchup-insight?home_team=X&away_team=Y` –  
  Returns win percentage, score distribution (histogram), and venue history for the selected teams

---

## Features
- Pick any home/away team
- See historical venues
- View score histograms
- Win % of home team
