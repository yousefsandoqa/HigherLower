import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [currentNumber, setCurrentNumber] = useState(Math.floor(Math.random() * 15)+1);
  const[newNumber, setNewNumber] = useState(0);
  const [score, setScore] = useState(0);
  const [gameStatus, setGameStatus] = useState('');
  const [isGameOver, setIsGameOver] = useState(false);
  const [statCategory, setStatCategory] = useState('PPG'); // Default stat category
  const [selectedTeam, setSelectedTeam] = useState('All Teams'); // Default team selection
  const [selectedYear, setSelectedYear] = useState('All Time'); // Default year selection
  const [player, setPlayer] = useState({name: '', year: ''}); // Player object with name and year

  const teams = [
    'All Teams', 
    'ATL',
    'BOS',
    'BKN',
    'CHA',
    'CHI',
    'CLE',
    'DAL',
    'DEN',
    'DET',
    'GSW',
    'HOU',
    'IND',
    'LAC',
    'LAL',
    'MEM',
    'MIA',
    'MIL',
    'MIN',
    'NOP',
    'NYK',
    'OKC',
    'ORL',
    'PHI',
    'PHX',
    'POR',
    'SAC',
    'SAS',
    'TOR',
    'UTA',
    'WAS',
  ]

  // Generate years from 1980 to the current year in the format "1980-81"
  const currentYear = new Date().getFullYear()
  const years = ['All Time', ...Array.from({ length: currentYear - 1980 -3 }, (_, i) => {
    const startYear = 1980 + i
    const endYear = (startYear + 1).toString().slice(-2)
    return `${startYear}-${endYear}`
  }).reverse()] // Reverse the array to show the most recent year first

  function generateInput() {
    return Math.floor(Math.random() * 20) + 1
  }

  const fetchPlayerData = async () => {
    try {
      // Prepare payload based on selections
      let payload = {};
      let endpoint = 'http://127.0.0.1:8000/season/stat_team';
      
      if (selectedYear === 'All Time' && selectedTeam === 'All Teams') {
        payload = {
          stat: [statCategory],
          teams: teams
        };
      } else if (selectedYear === 'All Time') {
        payload = {
          stat: [statCategory],
          teams: [selectedTeam],
        };
        endpoint = 'http://127.0.0.1:8000/season/stat_team';
      } else {
        payload = {
          stat: [statCategory],
          teams: [selectedTeam],
          year: selectedYear,
        };
        endpoint = 'http://127.0.0.1:8000/season/stat_team_year';
      }
      
      // Replace with your actual API endpoint
      const response = await axios.post(endpoint, payload);
      console.log('Using player data:', response.data);
      console.log('currentNumber:', currentNumber);
      console.log('NewNumber:', newNumber);
      return response.data;
    } catch (error) {
      console.error('Error fetching player data:', error);
      let defaultReturn = {}
      defaultReturn.name = "Default Player "+generateInput();
      defaultReturn.stat = generateInput();
      defaultReturn.year = '1725-26';
      console.log('Using default player data:', defaultReturn);
      console.log('currentNumber:', currentNumber);
      console.log('NewNumber:', newNumber);
      return defaultReturn;
    }
  };

  const handleGuess = async (guess) => {
    console.log('Current Number:', currentNumber);
    console.log('New Number:', newNumber);
    const correct =
      (guess === 'higher' && newNumber > currentNumber) ||
      (guess === 'lower' && newNumber < currentNumber);

    if (correct) {
      setScore(score + 1);
      setGameStatus(`Correct! It was ${newNumber}. Keep going!`);
      

      // Get API data with payload of selectedTeam, selectedYear, and statCategory
      const playerData = await fetchPlayerData();
      setCurrentNumber(newNumber);
      setNewNumber(playerData.stat);
      if (playerData) {
        setPlayer({
          name: playerData.name,
          year: playerData.year
        });
        setNewNumber(playerData.stat);
        setGameStatus(`Your new player is: ${playerData.name} (${playerData.year || 'All Time'})!`);
      }
    } else {
      setGameStatus(`Wrong! It was ${newNumber}. Game over.`);
      setIsGameOver(true);
    }
  };

  const restartGame = async () => {
    setScore(0);
    setIsGameOver(false);
    
    // Get API data with payload of selectedTeam, selectedYear, and statCategory
    const playerData = await fetchPlayerData();
    
    if (playerData) {
      setPlayer({
        name: playerData.name,
        year: playerData.year
      });
      setCurrentNumber(playerData.stat+(Math.floor(Math.random() * 5)));
      setNewNumber(playerData.stat);
      console.log('Player data:', playerData);
      console.log('currentNumber:', currentNumber);
      console.log('NewNumber:', newNumber);
      // Use playerData.name directly instead of player.name from state
      setGameStatus(`Your starting player is: ${playerData.name} (${playerData.year || 'All Time'})!`);
    } else {
      // setCurrentNumber(generateInput());
      setGameStatus('Failed to load player data. Using random number.');
    }
  };

  const handleStatChange = (e) => {
    setStatCategory(e.target.value)
  }

  const handleTeamChange = (e) => {
    setSelectedTeam(e.target.value)
  }

  const handleYearChange = (e) => {
    setSelectedYear(e.target.value)
  }

  return (
    <>
      <div className="emoji-background" aria-hidden="true">
        {Array.from({ length: 300 }).map((_, i) => (
          <span key={i}>{Math.random() > 0.5 ? '⬆️' : '⬇️'}</span>
        ))}
      </div>
      <div className="game-wrapper">
        <div className="game-container">
          <h1>🎮 Higher or Lower</h1>

          <div className="category-selections">
            <div className="stat-selection">
              <label htmlFor="stat-category">Choose a stat category: </label>
              <select 
                id="stat-category" 
                value={statCategory} 
                onChange={handleStatChange}
                disabled={!isGameOver && score > 0}
              >
                <option value="PPG">Points Per Game (PPG)</option>
                <option value="APG">Points Per Game (PPG)</option>
                <option value="RPG">Rebounds Per Game (RPG)</option>
                <option value="BPG">Blocks Per Game (BPG)</option>
                <option value="SPG">Steals Per Game (SPG)</option>
              </select>
            </div>

            <div className="team-selection">
              <label htmlFor="team-selection">Choose a team: </label>
              <select 
                id="team-selection" 
                value={selectedTeam} 
                onChange={handleTeamChange}
              >
                {teams.map((team, index) => (
                  <option key={index} value={team}>{team}</option>
                ))}
              </select>
            </div>

            <div className="year-selection">
              <label htmlFor="year-selection">Choose a season: </label>
              <select 
                id="year-selection" 
                value={selectedYear} 
                onChange={handleYearChange}
              >
                {years.map((year, index) => (
                  <option key={index} value={year}>{year}</option>
                ))}
              </select>
            </div>
          </div>

          <div className="restart-section">
            <button className="start-button" onClick={restartGame}>
              {score > 0 ? 'Restart' : 'Start Game'}
            </button>
          </div>

          <p className="status">{gameStatus}</p>
          <div className="number-display">{currentNumber}</div>
          <div className="stat-category">Current Stat: {statCategory}</div>
          <div className="team-category">Selected Team: {selectedTeam}</div>
          <div className="year-category">Selected Year: {selectedYear}</div>
          <div className="buttons">
            <button onClick={() => handleGuess('higher')} disabled={isGameOver}>Higher</button>
            <button onClick={() => handleGuess('lower')} disabled={isGameOver}>Lower</button>
          </div>
          <div className="score">Score: {score}</div>
          {isGameOver && (
            <button className="restart-button" onClick={restartGame}>Restart Game</button>
          )}
          <div className="history-section">
            <h2>High Scores (connect?)</h2>
            <p>Connect the DB to load this area.</p>
          </div>
        </div>
      </div>
    </>
  )
}  

export default App
