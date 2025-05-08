import React from 'react';
import possibilities from '../../api/predictions.json';
import './App.css';

function App() {
  return (
    <>
      <div className="app-container">
        <div className="card">
          <div className="card-title">Prediction Possibilities</div>


          {/* Display Android/Apple possibilities */}
          <div className="card-item">
            <span className="item-key">Android:</span>
            <span className="item-value">{possibilities.an}%</span>
          </div>
           <div className="card-item">
            <span className="item-key">Apple:</span>
            <span className="item-value">{possibilities.ap}%</span>
          </div>

          {/* Display Age possibilities */}
          <div className="card-item">
            <span className="item-key">Young:</span>
            <span className="item-value">{possibilities.y}%</span>
          </div>
          <div className="card-item">
            <span className="item-key">Old:</span>
            <span className="item-value">{possibilities.o}%</span>
          </div>

          {/* Display Wealth possibilities */}
           <div className="card-item">
            <span className="item-key">Rich:</span>
            <span className="item-value">{possibilities.r}%</span>
          </div>
          <div className="card-item">
            <span className="item-key">Poor:</span>
            <span className="item-value">{possibilities.p}%</span>
          </div>

        </div>
      </div>
    </>
  );
}

export default App;