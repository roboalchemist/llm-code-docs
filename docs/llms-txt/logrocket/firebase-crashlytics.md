# Source: https://docs.logrocket.com/docs/firebase-crashlytics.md

# Firebase Crashlytics

Integrating LogRocket with [Firebase Crashlytics](https://firebase.google.com/products/crashlytics)

LogRocket's [getSessionUrl method](https://docs.logrocket.com/reference/get-session-url) allows you to register a callback that will receive the session URL as a parameter. That LogRocket session URL can then be attached to Crashlytics crash reports as a [custom key](https://firebase.google.com/docs/crashlytics/customize-crash-reports):

```swift Swift
SDK.getSessionURL { sessionURL in
  Crashlytics.crashlytics().setCustomValue(sessionURL, forKey: "LogRocket_session")                  
}
```

```objectivec Objective-C
void (^completion)(NSString*) = ^(NSString* sessionURL) {
  [[FIRCrashlytics crashlytics] setCustomValue:sessionURL forKey:@"LogRocket_session"];
}

[LROSDK getSessionURL:completion]
```

```java Java
SDK.getSessionURL(sessionUrl -> {
  FirebaseCrashlytics crashlytics = FirebaseCrashlytics.getInstance();
  crashlytics.setCustomKey("LogRocket_session", sessionUrl);
});
```