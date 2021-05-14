// Regex-pattern to check URLs against. 
// It matches URLs like: http[s]://[...]amazon.com[...]
var urlRegex = /^https?:\/\/(?:[^./?#]+\.)?amazon\.com/;

// get current url for listener
var currenturl = "";
function sendCurrentUrl() {
    chrome.tabs.getSelected(null, function(tab) {
      currenturl = tab.url
    })
  }

chrome.tabs.onActivated.addListener((activeInfo) => {  
    sendCurrentUrl()
})

chrome.tabs.onSelectionChanged.addListener(() => {
    sendCurrentUrl()
})

// callback function for use in listener
function doInCurrentTab(tabCallback) {
    chrome.tabs.query(
        { currentWindow: true, active: true },
        function (tabArray) { tabCallback(tabArray[0]);}
    );
}

// listening for message from popup.js
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse){
    console.log(message);
    if(message.popupOpen) {
      console.log('popup is open');
      sendCurrentUrl();
      // ...check the URL of the active tab against our pattern and...
      if (urlRegex.test(currenturl)) {
        // ...if it matches, send a message specifying a callback too
        // alert('hello world');
        var activeTabId;

        activeTabId = doInCurrentTab(function(tab) 
            { 
              activeTabId = tab.id;
              // send message here for content.js
              // will receive dom content from content.js
              // but dom content is not actually in use here...
              chrome.tabs.sendMessage(tab.id, {text: 'report_back'}, 
                function(domContent){
                  console.log('I received the following DOM content:\n' + domContent);
                  if (domContent !== undefined)
                    chrome.runtime.sendMessage({isPinged: true});
                });
            });
      }
    }
  });