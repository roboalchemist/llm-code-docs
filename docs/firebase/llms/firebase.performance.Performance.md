# Source: https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance.md.txt

# Performance | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance).
- Performance

The Firebase Performance Monitoring service interface.

Do not call this constructor directly. Instead, use
[`firebase.performance()`](https://firebase.google.com/docs/reference/js/v8/firebase.performance).

## Index

### Properties

- [app](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance#app)
- [dataCollectionEnabled](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance#datacollectionenabled)
- [instrumentationEnabled](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance#instrumentationenabled)

### Methods

- [trace](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance#trace)

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Performance` service
instance.

example
:

        var app = analytics.app;


### dataCollectionEnabled

dataCollectionEnabled: boolean  
Controls the logging of custom traces.

### instrumentationEnabled

instrumentationEnabled: boolean  
Controls the logging of automatic traces and HTTP/S network monitoring.

## Methods

### trace

- trace ( traceName : string ) : [Trace](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace)
- Creates an uninitialized instance of [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) and returns
  it.

  #### Parameters

  -

    ##### traceName: string

    The name of the trace instance.

  #### Returns [Trace](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace)

The Trace instance.