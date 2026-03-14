# Source: https://docs.logrocket.com/reference/android-start-new-session.md

# Manually Start a New Session

For Android - End the current session and immediately start a new clean session

# `startNewSession(...)`

By default, a mobile session will end, and new activity will automatically start a new session, after 5 minutes of inactivity. The StartNewSession call may be useful on a shared device with rapid turnover between users. Separating the sessions can make it easier to review individual user's activity, and create metrics based on session activity that assumes a single user journey.

This function will both end the current session, and initialize a new session. The new session will have no connection to the previous one. This is best used for shared devices with multiple users, where you want to understand separate user behavior across different sessions.

A typical use case would involve calling `startNewSession` after the event that should force end the session, such as logout or the end of a transaction. The next customer to use the device would have a separate session.

## Changing Settings During StartNewSession Call

By default, the next session will initialize using the same parameters from the most recent [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk)call. This means configurations such as privacy settings will remain the same.

If you do wish to change the behavior of initialization settings after StartNewSession is called, you can choose to pass in new initialization parameters that will used to initialize the new session (see the [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk)call for more details).

```java
Future<Boolean> startNewSession(
  Application application,
  Context context,
  OptionsConfiguration options
)
```

#### Example Usage

```java java
Future<Boolean> newSessionFuture = SDK.startNewSession(
  (Application) this.getContext().getApplicationContext(),
  this.getContext(),
  options -> {
    options.setAppID(appID.getText().toString());
    options.setServerURL(serverURL.getText().toString());
  }
);
```

## Completion Future

In either case `startNewSession` runs its internal steps asynchronously and returns a `Future<Boolean>` object. This future can optionally be used to wait for initializing the new session to complete. The returned boolean will be `true` if a new session was initialized successfully, and `false` otherwise.

```java
Future<Boolean> newSessionFuture = SDK.startNewSession();
try {
  Boolean wasSuccessful = newSessionFuture.get();
} catch (ExecutionException | InterruptedException e) {
  Logger.e(
    "SessionInfoFragment",
    String.format("Error while starting clean session, %s", e.getCause()));
}
```

> 🚧 Avoid waiting for the result of startNewSession in the main UI thread to prevent impacting user experience
>
> Due to the need for the shutdown process to wait on various actions to complete successfully before returning, please ensure that if you wait on the result of `startNewSession` you are doing so off of the main UI thread so that rendering is not blocked.