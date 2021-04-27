import React, { useState, useEffect } from 'react';

import axios from 'axios';

import logo from './logo.svg';
import './App.css';

function App() {

  const [name, setName] = useState("Name");
  const [curPrice, setCurPrice] = useState(0);
  const [newPrice, setNewPrice] = useState(0);
  const [oldPrice, setOldPrice] = useState(0);
  const [link, setLink] = useState("");

  // Get information about current product

  const fetchName = async () => {
    const res = await axios(``); // TODO: call to Amazon with URL
    setName(res);
  }

  const fetchCurPrice = async () => {
    const res = await axios(``); // TODO: call to Amazon with URL
    setCurPrice(res);
  }

  const fetchPricesAndLink = async () => {
    const res = await axios(``); // TODO: call to back-end with parameter
    setNewPrice(res.newPrice);
    setOldPrice(res.oldPrice);
    setLink(res.link);
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Name: {name}
        </p>
        <p>
          oldPrice: {oldPrice}
        </p>
        <p>
          newPrice: {newPrice}
        </p>
        <a
          className="App-link"
          href={link}
          target="_blank"
          rel="noopener noreferrer"
        >
          Buy
        </a>
      </header>
    </div>
  );
}

export default App;
