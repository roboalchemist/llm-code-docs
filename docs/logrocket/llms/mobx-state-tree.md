# Source: https://docs.logrocket.com/reference/mobx-state-tree.md

# MobX State Tree

The LogRocket MobX-state-tree plugin allows you to log state changes to a single mobx-state-tree store. This plugin may be used in conjunction with the LogRocket MobX plugin.

## Installation

Install the plugin via NPM

```text
npm i logrocket-mobx-state-tree --save
```

Initialize the plugin after you initialize LogRocket

```javascript
import LogRocket from 'logrocket';
import logStore from 'logrocket-mobx-state-tree';

import someStore from './store'; // import your mobx-state-tree store

// initialize logrocket
LogRocket.init('your app here');

// attach logrocket to the store to watch for state changes
logStore(LogRocket, someStore);
```

> 📘 Note
>
> You may use the plugin multiple times to log changes to multiple stores.

State changes will be reported in LogRocket as if they came from Redux. You can filter over log entries by using the "redux" log filter category. In the action dropdown view you will see the action as reported from mobx-state-tree as well as the previous and next state and a view of the difference between the two.

## Sanitizing state

Just like Redux, you can sanitize the actions and state passed to LogRocket. The third parameter to the plugin accepts the same options as our [reduxMiddleware plugin](https://docs.logrocket.com/reference#redux-logging).

```javascript
logStore(LogRocket, someStore, {
  // example of sanitizing a part of the state tree
  stateSanitizer: function (state) {
    return {
      ...state,
      removeThisKey: undefined,
    };
  },

  // example of sanitizing 
  actionSanitizer: function (action) {
    if (action.type === 'ignoreThis') {
      return null;
    }
    return action;
  },
});
```

> 📘 Session Filtering
>
> This plugin is implemented by wrapping our Redux middleware. Therefore you can filter over sessions containing mobx-state-tree state changes using the  **redux action type** filter. In the log entry pane in the session view they will appear under the **redux** label.