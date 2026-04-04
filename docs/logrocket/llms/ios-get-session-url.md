# Source: https://docs.logrocket.com/reference/ios-get-session-url.md

# Access the Session URL

Retrieve the LogRocket session URL for use in integrations

### Session URL

Integration with [third party services](https://docs.logrocket.com/docs/other-services) can be accomplished by retrieving the Session URL and adding it as context to the third party library. In the iOS SDK, the session URL can be accessed with the `SDK.getSessionURL` method. Session URLs are only made available when our backend has accepted the session, which can take 1-5 seconds from when the SDK is initialized.

As of SDK version 1.32.0, once a `getSessionURL` handler is registered, it will be called each time a new session is started. A `hardShutdown` clears all registered handlers.

```swift Swift
SDK.getSessionURL { sessionURL in
  // Use the accepted Session URL
}
```

```objectivec Objective-C
void (^completion)(NSString*) = ^(NSString* sessionURL) {
  // Use the accepted Session URL
}

[LROSDK getSessionURL:completion]
```

> 🚧 Main UI Thread Considerations
>
> The session URL handler may be run on a background thread. To prevent errors, avoid modifying UI elements within `getSessionURL `, or wrap any UI modifications with `if Thread.isMainThread`.

### Session URL Status

If you would like more updates on a particular session URL, such as when the session is rejected, you can make use of `getSessionURLStatus`. Like `getSessionURL`, this function takes a handler function, however this handler runs once immediately, whenever a new session URL is available, and whenever a session is rejected.

Each time the handler is called, it will be provided a String containing one of the following:

* A session URL
* Information on why the session URL is not yet available
* Information on why the session was rejected. There are a number of reasons that a session may be rejected, such as when session quota has been reached, or when a particular user has been blocked for GDPR/CCPA purposes.

```swift Swift
SDK.getSessionURLStatus { sessionUrlOrStatus in
  // Use the accepted Session URL or status update
}
```

```objectivec Objective-C
void (^completion)(NSString*) = ^(NSString* sessionUrlOrStatus) {
  // Use the accepted Session URL or status update
}

[LROSDK getSessionURLStatus:completion]
```