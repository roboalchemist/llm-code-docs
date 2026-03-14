# Source: https://docs.logrocket.com/reference/get-session-url.md

# Access Session URL

Access the URL of the associated LogRocket session

Every user session is associated with a unique session URL. See [What defines a session?](https://docs.logrocket.com/docs/what-defines-a-session) for information on what determines a unique session.

Use `LogRocket.getSessionURL()` to register a callback that takes the URL as a parameter. That URL could then be attached to crash reports or support tickets. See [Integration](https://docs.logrocket.com/docs/integrations) for more details. When a new session starts, such as after 30 minutes of inactivity, that registered callback will again be triggered.

```javascript Get the URL for a LogRocket session
LogRocket.getSessionURL(sessionURL => {
  console.log(sessionURL);
});
```

> 📘 Using .sessionURL directly
>
> You can also use `LogRocket.sessionURL` directly, but this might return `null` in cases when the LogRocket script has not been fully loaded. Integrations that require synchronous execution can use this API. For example:
>
> ```javascript
> Sentry.configureScope(scope => {
>   scope.setExtra("sessionURL", LogRocket.sessionURL);
> });
> ```