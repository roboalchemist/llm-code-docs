# Source: https://docs.logrocket.com/reference/shoulddebuglog.md

# Show LogRocket SDK Messages In Console

Control whether LogRocket SDK messages are presented on the client-side browser

## Disable LogRocket SDK from logging to browser console

#### `shouldDebugLog` - Boolean

##### optional (default - `true`)

LogRocket will log debug information to the console when there are issues with the SDK. These can be useful for fixing your SDK configuration but you may want to hide them on the client side.

If you want to hide these messages, add this option to your configuration:

```javascript
LogRocket.init(YOUR_APP_ID, {
  shouldDebugLog: false,
});
```

LogRocket will still attempt to log these messages to the dashboard, but depending on the issue encountered this may not be possible.