# Source: https://docs.logrocket.com/reference/capture-exceptions.md

# Capture Exceptions

Capture exceptions for React Native

Use `captureException()` to manually report an [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) caught by your code.

```javascript Calling captureException()
try {
  doSomethingBroken();
} catch (err) {
  LogRocket.captureException(err, {
    tags: {
      // additional data to be grouped as "tags"
      subscription: 'Pro',
    },
    extra: {
      // additional arbitrary data associated with the event
      pageName: 'ProfileView',
    },
  });
}
```

Use `tags` and `extra` to send additional metadata with the error. The values contained in the `tags` and `extra` objects must be scalar values (e.g., booleans, numbers, or strings). Tags and extra data will appear with the error in the Issues view of the LogRocket dashboard, in the `Custom Tags` and `Additional Data` sections respectively.