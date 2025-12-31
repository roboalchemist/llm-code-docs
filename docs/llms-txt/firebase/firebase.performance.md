# Source: https://firebase.google.com/docs/reference/js/v8/firebase.performance.md.txt

# performance | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- performance

The Performance SDK does not work in a Node.js environment.

### Callable

- performance ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [Performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance)
- Gets the [`Performance`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance) service.

  `firebase.performance()` can be called with no arguments to access the default
  app's [`Performance`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance) service.
  The [`Performance`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance) service does not work with
  any other app.

  The Performance SDK does not work in a Node.js environment.

  example
  :

          // Get the Performance service for the default app
          const defaultPerformance = firebase.performance();


  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

    The app to create a performance service for. Performance Monitoring only works with
    the default app.
    If not passed, uses the default app.

  #### Returns [Performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance)

## Index

### Interfaces

- [Performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance)
- [Trace](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace)