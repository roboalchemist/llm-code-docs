# Source: https://docs.logrocket.com/reference/redux-logging.md

# Log Redux Actions

Log Redux actions in your app and the associated state

To add Redux logs to a LogRocket report, you need to add a store middleware to your Redux store by calling `LogRocket.reduxMiddleware()`

```javascript Basic installation
import { createStore } from 'redux';

const store = createStore(
  reducer, // your app reducer
  applyMiddleware(LogRocket.reduxMiddleware())
);
```

If you use other middlewares, LogRocket should be the **final** middleware:

```javascript Redux with other middlewares
import { applyMiddleware, createStore } from 'redux';

const store = createStore(
  reducer, // your app reducer
  applyMiddleware(middlewares, LogRocket.reduxMiddleware())
);
```

> 📘 Where to put LogRocket.reduxMiddleware()
>
> Most apps separate their analytics calls (like LogRocket) from their Redux store initialization. It's perfectly fine to call reduxMiddleware() before calling init().

## Customizing reduxMiddleware()

An optional configuration object can be passed into `LogRocket.reduxMiddleware(config)`.\
This object can be used to sanitize the Redux state and/or Redux actions before they are logged.

### Sanitize redux state

#### `stateSanitizer` - Function

##### optional

A `stateSanitizer` function can be used to scrub the Redux state.

To scrub the state, return a modified copy of the state.

```javascript Scrub state
LogRocket.reduxMiddleware({
  stateSanitizer: function (state) {
    return {
      ...state,
      removeThisKey: undefined,
    };
  },
});
```

> 📘 Immutable.js
>
> If you are using Immutable.js, LogRocket automatically serializes the Immutable state via the `toJSON()` method.

### Sanitize redux actions

#### `actionSanitizer` - Function

##### optional

An `actionSanitizer` function can be used to scrub or ignore an action. Actions can either be scrubbed or ignored altogether

To scrub the action, return a modified copy of the action.

```javascript Scrub action
LogRocket.reduxMiddleware({
  actionSanitizer: function (action) {
    return {
      ...action,
      removeThisKey: undefined,
    };
  },
});
```

To ignore an action, return null.

```javascript Ignore action
LogRocket.reduxMiddleware({
  actionSanitizer: function (action) {
    if (action.type === 'ignoreThis') {
      return null;
    }
    return action;
  },
});
```

### Notes on Performance and Bandwidth Usage

We compress all actions and state objects to a binary format, and perform diffs on your Redux state to minimize the data over the network.