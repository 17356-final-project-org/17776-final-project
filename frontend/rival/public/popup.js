//sending message to background js that popup is open

var isPinged = false;

function ping() {
    chrome.runtime.sendMessage({popupOpen: true}, response => {
        console.log(chrome.runtime.lastError);
        if (!isPinged)
            setTimeout(ping, 1000);
        //chrome.runtime.sendMessage({popupOpen: true});
    });
  }

  chrome.runtime.onMessage.addListener(function(message, sender, sendResponse){
    console.log(message);
    if(message.isPinged) {
      isPinged = true;
    }
  });

  chrome.storage.sync.set({'product_title': 'page is still loading please try again'}, function(result) {
    console.log("first Data saved in chrome storage from content.js")
    }
    );
ping();
  