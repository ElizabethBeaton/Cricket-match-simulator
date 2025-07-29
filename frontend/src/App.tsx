import { useState } from "react";
import GameSelector from "./components/GameSelector";
import MatchupDisplay from "./components/MatchupDisplay";
import { useMatchupInsight } from "./hooks/useMatchupInsight";
import { useTeams } from "./hooks/useTeams";

function App() {
  //hook to get unique team names
  const teamOptions = useTeams();

  // State for selected teams and trigger to fetch insight
  const [homeTeam, setHomeTeam] = useState<string>("");
  const [awayTeam, setAwayTeam] = useState<string>("");
  const [triggerFetch, setTriggerFetch] = useState(false);

  // Custom hook to fetch matchup insight
  const { insight, errorMessage } = useMatchupInsight(
    homeTeam,
    awayTeam,
    triggerFetch
  );

  // Trigger data fetch when user clicks search
  const handleSearch = () => {
    setTriggerFetch((prev) => !prev);
  };

  return (
    <div className="app">
      <h1 className="heading">Match Simulator</h1>

      <GameSelector
        teamOptions={teamOptions}
        homeTeam={homeTeam}
        awayTeam={awayTeam}
        onHomeTeamChange={setHomeTeam}
        onAwayTeamChange={setAwayTeam}
      />

      <button
        className="searchButton"
        disabled={!homeTeam || !awayTeam || homeTeam === awayTeam}
        onClick={handleSearch}
      >
        Search
      </button>

      {errorMessage && <p className="error-message">{errorMessage}</p>}

      {insight && <MatchupDisplay insight={insight} />}
    </div>
  );
}

export default App;
