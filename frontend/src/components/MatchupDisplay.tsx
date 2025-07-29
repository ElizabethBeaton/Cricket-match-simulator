import React from "react";
import Histogram from "./Histogram";
import GameDetails from "./GameDetails";
import type { MatchupInsight } from "../hooks/useMatchupInsight";

interface Props {
  insight: MatchupInsight;
}

const MatchupDisplay: React.FC<Props> = ({ insight }) => {
  return (
    <>
      <GameDetails
        homeTeam={insight.home_team}
        awayTeam={insight.away_team}
        matchingVenuesWithDates={insight.venue_history}
      />

      <Histogram
        data={insight.histogram}
        homeTeam={insight.home_team}
        awayTeam={insight.away_team}
      />

      <div className="win-percentage">
        <strong>Home Win Percentage:</strong>{" "}
        {insight.home_win_percentage.toFixed(1)}%
      </div>
    </>
  );
};

export default MatchupDisplay;
