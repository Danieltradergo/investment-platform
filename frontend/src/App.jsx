import { useState } from 'react';
import './App.css';

const API_BASE_URL = 'https://investment-platform-ny5x.onrender.com';

function App() {
  const [portfolios, setPortfolios] = useState([
    { id: 1, name: 'My Portfolio', balance: 10000, assets: [] }
  ]);

  return (
    <div className="app">
      <header className="header">
        <h1>Investment Platform</h1>
      </header>
      <main className="main">
        <section className="dashboard">
          <h2>Portfolios</h2>
          <div className="portfolio-list">
            {portfolios.map(portfolio => (
              <div key={portfolio.id} className="portfolio-card">
                <h3>{portfolio.name}</h3>
                <p>Balance: ${portfolio.balance.toLocaleString()}</p>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
