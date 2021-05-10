let color = '#3aa757';
let url = 'https://www.amazon.com';

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log('Default background color set to %cgreen', `color: ${color}`);
});

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ url });
  console.log('URL set to', `url: ${url}`);
});
