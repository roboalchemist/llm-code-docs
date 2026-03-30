# Source: https://docs.logrocket.com/reference/react-native-get-session-url.md

# Access the Session URL

Retrieve the LogRocket session URL for use in integrations

### Session URL

Integration with [third party services](https://docs.logrocket.com/docs/other-services) can be accomplished by retrieving the Session URL and adding it as context to the third party library. In the React Native SDK, the session URL can be accessed with the `LogRocket.getSessionURL` method. Session URLs are only made available when our backend has accepted the session, which can take 1-5 seconds from when the SDK is initialized.

As of LogRocket version 1.32.0, once a `getSessionURL` callback is registered, it will be called each time a new session is started. A `hardShutdown` clears all registered callbacks.

```javascript JavaScript
LogRocket.getSessionURL((url) => {
  // Use the accepted Session URL.
  // i.e. console.info(`LogRocket session URL: ${url}`)
});
```

### Session URL Status

If you would like more updates on a particular session URL, such as when the session is rejected, you can make use of `getSessionURLStatus`. Like `getSessionURL`, this function takes a callback function, however this callback runs once immediately, whenever a new session URL is available, and whenever a session is rejected.

Each time the callback is called, it will be provided a String containing one of the following:

* A session URL
* Information on why the session URL is not yet available
* Information on why the session was rejected. There are a number of reasons that a session may be rejected, such as when session quota has been reached, or when a particular user has been blocked for GDPR/CCPA purposes.

```javascript JavaScript
LogRocket.getSessionURLStatus((urlOrStatus) => {
  // Use the session URL status
});
```