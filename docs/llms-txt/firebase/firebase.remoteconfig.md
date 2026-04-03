# Source: https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.md.txt

# remoteConfig | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- remoteConfig

The Remote Config SDK does not work in a Node.js environment.

### Callable

- remoteConfig ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig)
- Gets the [`RemoteConfig`](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig) instance.

  The Remote Config SDK does not work in a Node.js environment.

  example
  :

          // Get the RemoteConfig instance for the default app
          const defaultRemoteConfig = firebase.remoteConfig();


  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

    The app to create a Remote Config service for. If not passed, uses the default app.

  #### Returns [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig)

## Index

### Interfaces

- [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig)
- [Settings](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Settings)
- [Value](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value)

### Type aliases

- [FetchStatus](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#fetchstatus)
- [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#loglevel)
- [ValueSource](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#valuesource)

### Functions

- [isSupported](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#issupported)

## Type aliases

### FetchStatus

FetchStatus: "no-fetch-yet" \| "success" \| "failure" \| "throttle"  
Summarizes the outcome of the last attempt to fetch config from the Firebase Remote Config server.

- "no-fetch-yet" indicates the [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig) instance has not yet attempted to fetch config, or that SDK initialization is incomplete.
- "success" indicates the last attempt succeeded.
- "failure" indicates the last attempt failed.
- "throttle" indicates the last attempt was rate-limited.

### LogLevel

LogLevel: "debug" \| "error" \| "silent"  
Defines levels of Remote Config logging.

### ValueSource

ValueSource: "static" \| "default" \| "remote"  
Indicates the source of a value.

- "static" indicates the value was defined by a static constant.
- "default" indicates the value was defined by default config.
- "remote" indicates the value was defined by fetched config.

## Functions

### isSupported

- isSupported ( ) : Promise \< boolean \>
- This method provides two different checks:
  1. Check if IndexedDB exists in the browser environment.
  2. Check if the current browser context allows IndexedDB `open()` calls.

  It returns a `Promise` which resolves to true if a [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig) instance
  can be initialized in this environment, or false if it cannot.

  #### Returns Promise\<boolean\>