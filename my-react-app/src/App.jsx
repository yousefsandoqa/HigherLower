import { useState } from 'react'
import './App.css'

function App() {
  const [currentNumber, setCurrentNumber] = useState(generateInput())
  const [setNextNumber] = useState(null)
  const [score, setScore] = useState(0)
  const [gameStatus, setGameStatus] = useState('Start guessing!')
  const [isGameOver, setIsGameOver] = useState(false)

  function generateInput() {
    return Math.floor(Math.random() * 100) + 1
  }

  const handleGuess = (guess) => {
    const newNumber = generateInput()
    setNextNumber(newNumber)

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
    setGameStatus('Start guessing!')
    setIsGameOver(false)
    setNextNumber(null)
  }

  return (
    <>
      {/* Emoji background goes here */}
      <div className="emoji-background" aria-hidden="true">
        {Array.from({ length: 300 }).map((_, i) => (
          <span key={i}>{Math.random() > 0.5 ? '⬆️' : '⬇️'}</span>
        ))}
      </div>
  
      {/* Game UI is wrapped in a foreground container */}
      <div className="game-wrapper">
        <div className="game-container">
          <h1>🎮 Higher or Lower</h1>
          <p className="status">{gameStatus}</p>
          <div className="number-display">{currentNumber}</div>
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
