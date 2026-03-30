# Source: https://docs.logrocket.com/reference/disable-page-titles.md

# Disable Page Titles

LogRocket will capture and display the contents of `document.title`. Similar to your browser's tab bar, we use these to make it easier to differentiate between different tabs during replay. If your page titles contain sensitive information, we recommend disabling this capture by adding `dom: { disablePageTitles: true }` to your init call. For example:

```javascript
LogRocket.init(YOUR_APP_ID, {  
  dom: {  
    disablePageTitles: true  
  },  
});
```