// Initialize button with user's preferred color
let rivalButton = document.getElementById("rivalButton");
let rivalLink = document.getElementById("rivalLink");

// When the button is clicked, inject setPageBackgroundColor into current page
rivalButton.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: rivalCallback,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function rivalCallback() {
  console.log(document.getElementById("productTitle").innerHTML.trim());
  console.log(document.getElementById("priceblock_ourprice").innerHTML);
  alert("hey");
  // rivalLink.setAttribute("href", "https://www.Apple.com");
  // console.log(rivalLink.href);
}
