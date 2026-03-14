# Source: https://docs.logrocket.com/reference/react-native-capturing-logs.md

# Capture Application Logs

Surface application logs in LogRocket sessions

By default, LogRocket logs the following methods of the `console` API:

* `console.log()`
* `console.info()`
* `console.debug()`
* `console.warn()`
* `console.error()`

### Disable Console Logging

##### **`isEnabled`** - Boolean

###### optional (default - `true`)

Disable this boolean to prevent logging of console data to LogRocket.

```javascript Disable console logging
LogRocket.init(YOUR_APP_ID, {
  console: {
    isEnabled: false,
  },
});
```

You can also disable specific console methods by setting the method name to be *false*. By default, all methods will be logged unless explicitly set to *false*.

```javascript Disabling specific console logging methods
// This will log all console.info, console.warn, and console.error calls.
LogRocket.init(YOUR_APP_ID, {
  console: {
    isEnabled: {
      log: false,
      debug: false, 
    },
  },
});
```

### Manual Log Capture

If you'd like to add logs to your LogRocket sessions without emitting logs in your application itself, you can call any of these methods:

```javascript Javascript
LogRocket.log('a message');
LogRocket.info('some information');
LogRocket.debug('debug log');
LogRocket.warn('a warning');
LogRocket.error('an error');
```

The contents of these method calls will appear in your LogRocket sessions as if you had called the corresponding `console` methods.