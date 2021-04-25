import axios from "axios";
const api = "https://covid19.mathdro.id/api/countries";
const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const cases = document.querySelector(".cases");
const recovered = document.querySelector(".recovered");
const deaths = document.querySelector(".deaths");
const results = document.querySelector(".result-container");

const currenturl = document.querySelector(".currenturl")


results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";
// grab the form
const form = document.querySelector(".form-data");
// grab the country name
const country = document.querySelector(".country-name");

//get current url
function sendCurrentUrl() {
  chrome.tabs.getSelected(null, function(tab) {
    currenturl.textContent = tab.url
  })
}

// declare a method to search by country name
const searchForCountry = async countryName => {
  loading.style.display = "block";
  errors.textContent = "";
  try {
    const response = await axios.get(`${api}/${countryName}`);
    loading.style.display = "none";
    cases.textContent = response.data.confirmed.value;
    recovered.textContent = response.data.recovered.value;
    deaths.textContent = response.data.deaths.value;

    sendCurrentUrl()

    results.style.display = "block";
  } catch (error) {
    loading.style.display = "none";
    results.style.display = "none";
    errors.textContent = "We have no data for the country you have requested.";
  }
};

// declare a function to handle form submission
const handleSubmit = async e => {
  e.preventDefault();
  searchForCountry(country.value);
  console.log(country.value);
};

form.addEventListener("submit", e => handleSubmit(e));
