# Source: https://docs.logrocket.com/reference/starting-a-new-clean-session-react-native.md

# Manually Start a New Session

For React Native - End the current session and immediately start a new clean session

# `startNewSession(...)`

By default, a mobile session will end, and new activity will automatically start a new session, after 5 minutes of inactivity. The StartNewSession call may be useful on a shared device with rapid turnover between users. Separating the sessions can make it easier to review individual user's activity, and create metrics based on session activity that assumes a single user journey.

The startNewSession function will both end the current session, and initialize a new session. The new session will have no connection to the previous one. This is best used for shared devices with multiple users, where you want to understand separate user behavior across different sessions.

A typical use case would involve calling `startNewSession` after the event that should force end the session, such as logout or the end of a transaction. The next customer to use the device would have a separate session.

## Changing Settings During StartNewSession Call

To initialize using the same parameters from the most recent [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk)call, use the function `startNewSessionSameConfig` or `startNewSession()` without providing any parameters. This means configurations such as privacy settings will remain the same.

```swift TSX
// startNewSessionSameConfig(): Promise<boolean>

LogRocket.startNewSessionSameConfig();
```

If you do wish to change the behavior of initialization settings after StartNewSession is called, you can choose to pass in new initialization parameters that will used to initialize the new session (see the [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk)call for more details). For example:

```swift TSX
// startNewSession(appID: string, config?: IOptions): Promise<boolean>

LogRocket.startNewSession(appID, {
  serverURL,
  textSanitizer,
});
```

## Completion Promise

`startNewSession` runs its internal steps asynchronously and returns a `Promise<boolean>`when called. This Promise will resolve after the process to shut down the current session and initialize the new one completes. The boolean returned will be `true` if the new session was initialized successfully, or `false` otherwise.

> 🚧 Avoid waiting in the main UI thread for the startNewSession Promise to resolve
>
> Due to the need for the shutdown process to wait on various actions to complete successfully before returning, please ensure that if you wait for the `startNewSession` promise to resolve you are doing so off of the main UI thread so that rendering is not blocked and the user experience is not negatively impacted.