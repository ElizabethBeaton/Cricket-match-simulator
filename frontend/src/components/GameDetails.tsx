import React from "react";

interface GameDetailsProps {
  homeTeam: string;
  awayTeam: string;
  matchingVenuesWithDates: { venue: string; date: string }[];
}

const GameDetails: React.FC<GameDetailsProps> = ({
  homeTeam,
  awayTeam,
  matchingVenuesWithDates,
}) => {
  return (
    <div className="game-details">
      <h3 className="team">
        {homeTeam} vs {awayTeam} 🏏
      </h3>

      {matchingVenuesWithDates.length > 0 && (
        <div style={{ marginTop: "0.5rem" }}>
          <h4>Venue History:</h4>
          <ul>
            {matchingVenuesWithDates.map((entry, idx) => (
              <li className="list-details" key={idx}>
                <span className="list-venue-name">{entry.venue}</span>
                <span className="list-venue-date">
                  {new Date(entry.date).toLocaleDateString("en-GB")}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default GameDetails;
