import { useState } from 'react'
import './App.css'

function App() {
  const [currentNumber, setCurrentNumber] = useState(generateInput())
  const [score, setScore] = useState(0)
  const [gameStatus, setGameStatus] = useState('Select your stat categories!')
  const [isGameOver, setIsGameOver] = useState(false)
  const [statCategory, setStatCategory] = useState('PPG') // Default stat category
  const [selectedTeam, setSelectedTeam] = useState('All Teams') // Default team selection
  const [selectedYear, setSelectedYear] = useState('All Time') // Default year selection

  const teams = [
    'All Teams', 
    'ATL Atlanta Hawks',
    'BOS Boston Celtics',
    'BKN Brooklyn Nets',
    'CHA Charlotte Hornets',
    'CHI Chicago Bulls',
    'CLE Cleveland Cavaliers',
    'DAL Dallas Mavericks',
    'DEN Denver Nuggets',
    'DET Detroit Pistons',
    'GSW Golden State Warriors',
    'HOU Houston Rockets',
    'IND Indiana Pacers',
    'LAC Los Angeles Clippers',
    'LAL Los Angeles Lakers',
    'MEM Memphis Grizzlies',
    'MIA Miami Heat',
    'MIL Milwaukee Bucks',
    'MIN Minnesota Timberwolves',
    'NOP New Orleans Pelicans',
    'NYK New York Knicks',
    'OKC Oklahoma City Thunder',
    'ORL Orlando Magic',
    'PHI Philadelphia 76ers',
    'PHX Phoenix Suns',
    'POR Portland Trail Blazers',
    'SAC Sacramento Kings',
    'SAS San Antonio Spurs',
    'TOR Toronto Raptors',
    'UTA Utah Jazz',
    'WAS Washington Wizards'
  ]

  // Generate years from 1980 to the current year in the format "1980-81"
  const currentYear = new Date().getFullYear()
  const years = ['All Time', ...Array.from({ length: currentYear - 1980 -3 }, (_, i) => {
    const startYear = 1980 + i
    const endYear = (startYear + 1).toString().slice(-2)
    return `${startYear}-${endYear}`
  }).reverse()] // Reverse the array to show the most recent year first

  function generateInput() {
    return Math.floor(Math.random() * 100) + 1
  }

  const handleGuess = (guess) => {
    const newNumber = generateInput()
    const correct =
      (guess === 'higher' && newNumber > currentNumber) ||
      (guess === 'lower' && newNumber < currentNumber)

    if (correct) {
      setScore(score + 1)
      setGameStatus(`Correct! It was ${newNumber}. Keep going!`)
      setCurrentNumber(newNumber)
    } else {
      setGameStatus(`Wrong! It was ${newNumber}. Game over.`)
      setIsGameOver(true)
    }
  }

  const restartGame = () => {
    setCurrentNumber(generateInput())
    setScore(0)
    setGameStatus('Select your stat categories!')
    setIsGameOver(false)
  }

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
