import { useState, useEffect } from "react";
import axios from "axios";

export interface MatchupInsight {
  home_team: string;
  away_team: string;
  home_win_percentage: number;
  histogram: {
    bin: number;
    [team: string]: number;
  }[];
  venue_history: {
    venue: string;
    date: string;
  }[];
}

export const useMatchupInsight = (
  homeTeam: string,
  awayTeam: string,
  triggerFetch: boolean
) => {
  const [insight, setInsight] = useState<MatchupInsight | null>(null);
  const [errorMessage, setErrorMessage] = useState<string>("");

  useEffect(() => {
    if (!triggerFetch || !homeTeam || !awayTeam || homeTeam === awayTeam)
      return;

    axios
      .get("http://localhost:8000/matchup-insight", {
        params: { home_team: homeTeam, away_team: awayTeam },
      })
      .then((res) => {
        setInsight(res.data);
        setErrorMessage("");
      })
      .catch(() => {
        setInsight(null);
        setErrorMessage("Could not load matchup data.");
      });
  }, [homeTeam, awayTeam, triggerFetch]);

  return { insight, errorMessage };
};
