# Source: https://docs.logrocket.com/reference/startnewsession.md

# Split Web Sessions

Web SDK - End the current user session and start a new session.

Call `LogRocket.startNewSession()` to end the current user session and begin a new session. The new session will appear separately in the LogRocket dashboard.

> 📘 LogRocket sessions should be started using `.init()`
>
> Unless recommended otherwise by LogRocket Support, you should call `.init()`, not `.startNewSession()`, to start recording a session.

> 🚧 `.startNewSession()` is rarely necessary
>
> The `.startNewSession` method is recommended in rare cases where you have multiple users on the same computer, and would like to analyze their sessions separately.

By default, LogRocket will start a new session after 30 minutes of inactivity as described in "[What defines a session?](https://docs.logrocket.com/docs/what-defines-a-session)". The LogRocket SDK gracefully handles both starting and halting ongoing sessions, with built-in logic to ensure continuity of recordings and the initialization of new sessions at appropriate times.

Use of `startNewSession` typically results in sessions being consumed faster than intended, and may cause you to reach your quota unexpectedly early.

The session created when  `LogRocket.startNewSession()`is called will clear any previously identified user. To identify the session's active user, call `LogRocket.identify` after calling `LogRocket.startNewSession()`:

```javascript
// Start a new session associated with a different user.

LogRocket.startNewSession();
LogRocket.identify(newUserId, {
  email: userEmail,
  name: userName,
});

```