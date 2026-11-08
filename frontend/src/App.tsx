import React, { useState } from 'react';
import TextGenerator from './components/TextGenerator';
import Pricing from './components/Pricing';

function App() {
  const [view, setView] = useState('home');

  return (
    <div className="App">
      <nav style={{ padding: '10px', background: '#333', color: '#fff', display: 'flex', gap: '20px' }}>
        <button onClick={() => setView('home')}>Home</button>
        <button onClick={() => setView('pricing')}>Pricing</button>
      </nav>
      <header className="App-header">
        <h1>ALPHA AI</h1>
        <p>Premium Content Generation</p>
      </header>
      <main>
        {view === 'home' ? <TextGenerator /> : <Pricing />}
      </main>
      <footer>
        <p>© 2026 ALPHA AI - Start Earning Today</p>
      </footer>
    </div>
  );
}

export default App;
