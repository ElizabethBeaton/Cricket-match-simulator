
interface GameSelectorProps {
  teamOptions: string[];
  homeTeam: string;
  awayTeam: string;
  onHomeTeamChange: (team: string) => void;
  onAwayTeamChange: (team: string) => void;
}

const GameSelector = ({
  teamOptions,
  homeTeam,
  awayTeam,
  onHomeTeamChange,
  onAwayTeamChange,
}: GameSelectorProps) => {
  return (
    <div>
      <div className="dropdown">
        <label>Home Team:</label>
        <select
          className="wide-select"
          value={homeTeam}
          onChange={(e) => onHomeTeamChange(e.target.value)}
        >
          <option value="">Select Home Team</option>
          {teamOptions.map((team) => (
            <option key={team} value={team}>
              {team}
            </option>
          ))}
        </select>
      </div>

      <div className="dropdown">
        <label>Away Team:</label>
        <select
          className="wide-select"
          value={awayTeam}
          onChange={(e) => onAwayTeamChange(e.target.value)}
        >
          <option value="">Select Away Team</option>
          {teamOptions.map((team) => (
            <option key={team} value={team}>
              {team}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};

export default GameSelector;
