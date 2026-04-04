# Source: https://docs.logrocket.com/reference/capture-error-messages-2.md

# Capture Error Messages

Add custom errors into the LogRocket dashboard in React Native

## Manually surface error messages in LogRocket

Use `captureMessage()` to manually report a message. This message will be treated as an error within LogRocket.

```javascript
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

Add `tags` and `extra` fields to send extra metadata about the message. The values contained in the `tags` and `extra` objects must be scalar values (e.g., booleans, numbers, or strings). Tags and extra data will appear within the error in the LogRocket dashboard.