// console.log("hello world from content.js");

// Listen for messages
chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    console.log(msg);
    // If the received message has the expected format...
    if (msg.text === 'report_back') {
        // Call the specified callback, passing
        // the web-page's DOM content as argument

        // console.log(document);
        // console.log(document.getElementById("productTitle").childNodes[0].nodeValue)

        //returning response to background.js
        sendResponse(document.getElementById("productTitle").childNodes[0].nodeValue.trim());

        //store in chrome storage so that React can access it
        var product_title = document.getElementById("productTitle").childNodes[0].nodeValue.trim()

        console.log("over here")
        console.log(product_title)

        // var product_price = document.getElementById("priceblock_ourprice").childNodes[0].nodeValue.trim()

        // console.log(product_price)
        // chrome.storage.sync.set({'product_title': product_title, 'product_price': product_price}, function(result) {

        if (product_title === undefined)
        {
            chrome.storage.sync.set({'product_title': 'page is still loading please try again'}, function(result) {
                console.log("Data saved in chrome storage from content.js")
                console.log("data saved is" + product_title)
            }
            );
        }
        else
        {
            chrome.storage.sync.set({'product_title': product_title}, function(result) {
                console.log("Data saved in chrome storage from content.js")
                console.log("data saved is" + product_title)
            }
            );
        }
    }

});