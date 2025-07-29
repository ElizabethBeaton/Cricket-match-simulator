import { useState, useEffect } from "react";
import axios from "axios";

// Custom hook to fetch and return unique team names from the backend 
export const useTeams = () => {
  const [teams, setTeams] = useState<string[]>([]);

  useEffect(() => {
    axios.get("http://localhost:8000/games").then((res) => {
      const uniqueTeams = Array.from(
        new Set(res.data.flatMap((g: any) => [g.home_team, g.away_team]))
      ) as string[];
      setTeams(uniqueTeams);
    });
  }, []);

  return teams;
};
