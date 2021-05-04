chrome.tabs.onActivated.addListener((activeInfo) => {  
    sendCurrentUrl()
})

chrome.tabs.onSelectionChanged.addListener(() => {
sendCurrentUrl()
})