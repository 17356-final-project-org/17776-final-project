/*global chrome*/
import React, { useState, useEffect } from 'react';

import axios from 'axios';

import logo from './logo.svg';
import './App.css';

function App() {

  const [name, setName] = useState("");
  const [curPrice, setCurPrice] = useState(0);
  const [newPrice, setNewPrice] = useState(0);
  const [oldPrice, setOldPrice] = useState(0);
  const [link, setLink] = useState("");

  // Get information about current product

  const fetchName = async () => {
    // get data from html...
    chrome.storage.local.get(['product_title'], function(result) {
      console.log('product_title retrieved from chrome storage is ' + result.product_title);
      setName(result.product_title);
    });
    
  }

  const fetchCurPrice = async () => {
    // get data from html... 
    setCurPrice(1);
  }

  const fetchPricesAndLink = async () => {
    fetchName();
    fetchCurPrice();
    const res = await axios.get("https://rival-app.azurewebsites.net/api/item/" + name);
    console.log(res);
    setNewPrice(res.data.lowest_price);
    setOldPrice(res.data.nominal_price);
    setLink(res.data.item_url);
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
        <button onClick={() => fetchPricesAndLink()}>
        Click me
        </button>

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
