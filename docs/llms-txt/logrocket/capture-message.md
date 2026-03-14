# Source: https://docs.logrocket.com/reference/capture-message.md

# Capture Error Messages

Add custom errors into the LogRocket dashboard

## Manually surface error messages in LogRocket

Use `captureMessage()` to manually report a message. This message will be treated as an error within LogRocket.

```javascript Calling captureMessage()
LogRocket.captureMessage('Something is wrong!', {
  tags: {
    // additional data to be grouped as "tags"
    subscription: 'Pro',
  },
  extra: {
    // additional arbitrary data associated with the event
    pageName: 'ProfileView',
  },
});
```

Add `tags` and `extra` fields to send extra metadata about the message. The values contained in the `tags` and `extra` objects must be scalar values (e.g., booleans, numbers, or strings). Tags and extra data will appear with the error in the Issues view of the LogRocket dashboard.

> 🚧
>
> Some tags are reserved. The following tag keys will be omitted from the `Custom Tags` section:
>
> * `browser`
> * `browser.name`
> * `level`
> * `logger`
> * `os`
> * `os.name`
> * `release`
> * `transaction`
> * `url`
> * `user`

## Automatically aggregate console errors in LogRocket

#### `shouldAggregateConsoleErrors` - Boolean

##### optional (default - `false`)

Use this option to control whether aggregated data about messages logged with `console.error()` or `LogRocket.error()` is surfaced as an error in LogRocket.

```javascript
LogRocket.init(YOUR_APP_ID, {
  console: {
    shouldAggregateConsoleErrors: true,
  },
});
```

> 🚧
>
> Aggregated console errors do not include stack traces. Use [`LogRocket.captureException()`](https://docs.logrocket.com/reference/capture-exception) for stack traces to be included when [source maps](https://docs.logrocket.com/docs/stacktraces) are in use.