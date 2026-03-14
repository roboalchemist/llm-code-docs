# Source: https://docs.logrocket.com/docs/drift.md

# Drift

Integrating LogRocket with [Drift](https://drift.com)

Add a LogRocket session URL to every Drift support request:

```javascript
LogRocket.getSessionURL(function (sessionURL) {
  drift.track('LogRocket', { sessionURL: sessionURL });
});
```

Alternatively see [Other Services](https://docs.logrocket.com/docs/other-services) as a way to add a link the a list of all the user's sessions to the customers' Drift profile.