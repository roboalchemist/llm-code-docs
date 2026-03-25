# Source: https://docs.logrocket.com/reference/console.md

# Capture Console Logs

Control how LogRocket treats different methods of the console API

By default, LogRocket logs the following methods of the `console` API:

* `console.log()`
* `console.info()`
* `console.debug()`
* `console.warn()`
* `console.error()`

If you'd like to log data but not have it appear in the browser console while developing, you can call any of these methods:

```javascript
LogRocket.log('foo', { bar: 'baz' });
```

LogRocket's console capture can be modified with the options below.

## Disable Console Logging

#### **`isEnabled`** - Boolean

##### optional (default - `true`)

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