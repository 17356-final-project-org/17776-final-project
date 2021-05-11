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
        sendResponse(document.getElementById("productTitle").childNodes[0].nodeValue);

        //store in chrome storage so that React can access it
        var product_title = document.getElementById("productTitle").childNodes[0].nodeValue
        console.log(product_title)
        chrome.storage.local.set({'product_title': product_title}, function(result) {
            console.log("Data saved in chrome storage from content.js")
        }
        );

    }

});