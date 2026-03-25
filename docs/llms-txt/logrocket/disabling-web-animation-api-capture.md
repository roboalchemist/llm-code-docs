# Source: https://docs.logrocket.com/reference/disabling-web-animation-api-capture.md

# Disabling Web Animation API Capture

If you start to notice issues with sessions containing Web Animations, notably elements persisting during the replay unexpectedly, you have the option of disabling capture of web animations of future sessions. You can disable capture by adding `dom: { disableWebAnimations: true }` to your init call, so for example:

```javascript
LogRocket.init(YOUR_APP_ID, {  
  dom: {  
    disableWebAnimations: true  
  },  
});
```