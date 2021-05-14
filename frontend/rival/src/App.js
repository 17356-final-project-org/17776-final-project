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
    chrome.storage.sync.get(['product_title'], function(result) {
      console.log('product_title retrieved from chrome storage is ' + result.product_title);
      populate(result.product_title);
    });

    // chrome.storage.sync.get(['product_title','product_price'], function(result) {
    //   console.log('product_title retrieved from chrome storage is ' + result.product_title);
    //   console.log('product_price retrieved from chrome storage is ' + result.product_price);

    //   test(result.product_title,result.product_price);
    // });

  }

  const fetchCurPrice = async () => {
    // get data from html... 
    setCurPrice(1);
  }

  // const test = async (productName,productPrice) => {
  const populate = async (productName) => {
    if (productName !== 'page is still loading please try again')
    {
      fetchCurPrice();    
      const res = await axios.get("https://rival-app.azurewebsites.net/api/item/" + (productName.replace(/[^a-zA-Z0-9 ]/g, "")));
      console.log(res);
      // console.log(productPrice)
      setName(productName);
      setNewPrice(res.data.lowest_price);
      setOldPrice(res.data.nominal_price);
      setLink(res.data.item_url);
    }
    else
    {
      setName(productName);
    }
    
  }


  const fetchPricesAndLink = async () => {
    fetchName();
    /*fetchCurPrice();
    const res = await axios.get("https://rival-app.azurewebsites.net/api/item/" + name);
    console.log(res);
    setNewPrice(res.data.lowest_price);
    setOldPrice(res.data.nominal_price);
    setLink(res.data.item_url);*/
    
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Name: {name}
        </p>
        <p>
          Sale Price: {newPrice}
        </p>


        <a
          className="App-link"
          href={link}
          target="_blank"
          rel="noopener noreferrer"
        >
          Buy
        </a>

        <button onClick={() => fetchPricesAndLink()}>
        Search Rival Deals
        </button>


      </header>
    </div>
  );
}

export default App;
