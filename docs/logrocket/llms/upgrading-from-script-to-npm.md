# Source: https://docs.logrocket.com/docs/upgrading-from-script-to-npm.md

# Upgrading from <script> to NPM

Upgrading from the LogRocket script tag to the LogRocket NPM package

Some users may be using the synchronous script tag to load LogRocket:

```
<script src="https://cdn.logr-in.com/LogRocket.min.js"></script>
```

We highly recommend that you use LogRocket NPM package instead. This has a few advantages:

* Bundled with your app - allows the browser to optimize the JavaScript download.
* Smaller script - the majority of the LogRocket script is loaded asynchronously, which improves page load time.
* Version controlled - you are free to upgrade the API at your own convenience.

***

## Installation

Switching to the NPM package is simple:

1. Install the logrocket module via NPM: `npm i --save logrocket`
2. Import logrocket and then call init with your app id. Make sure to import logrocket **before anything else in your application**.

```javascript
import LogRocket from 'logrocket';

LogRocket.init('org/app');
```

3. (Optional) If your app uses Redux, add our store middleware to log state and actions.

```javascript
import LogRocket from 'logrocket';
import { applyMiddleware, createStore, compose } from 'redux';

const store = createStore(
  reducer, // your app reducer
  compose(
    applyMiddleware(middlewares, LogRocket.reduxMiddleware()), // LogRocket should be the last middleware
  )
);
```