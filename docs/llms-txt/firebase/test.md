# Source: https://firebase.google.com/docs/reference/functions/test.md.txt

# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects/test.md.txt

# Source: https://firebase.google.com/docs/reference/functions/test/test.md.txt

# Namespace: test

# test

namespace

`test` is a global namespace that serves as a testing companion to firebase-functions.

Use `test()` to initialize the SDK, optionally providing these parameters for online testing:

- `firebaseConfig` Firebase config values for initializing a Firebase app for your test code to interact with (e.g. making database writes). It is recommended that you use a project that is specifically for testing. If omitted, mock config values are used and your tests do not interact with a real Firebase app, and all Firebase methods need to be stubbed.
- `pathToServiceAccountKey` Path to a service account key file to be used when initializing the Firebase app.

For example:

`const test = require('firebase-functions-test')(); // Offline mode`

`const test = require('firebase-functions-test')(firebaseConfigValues,
path/to/key.json'); // Online mode`

## Interface

### [EventContextOptions](https://firebase.google.com/docs/reference/functions/test/test.EventContextOptions)

## Namespaces

### [analytics](https://firebase.google.com/docs/reference/functions/test/test.analytics)

### [auth](https://firebase.google.com/docs/reference/functions/test/test.auth)

### [crashlytics](https://firebase.google.com/docs/reference/functions/test/test.crashlytics)

### [database](https://firebase.google.com/docs/reference/functions/test/test.database)

### [firestore](https://firebase.google.com/docs/reference/functions/test/test.firestore)

### [pubsub](https://firebase.google.com/docs/reference/functions/test/test.pubsub)

### [storage](https://firebase.google.com/docs/reference/functions/test/test.storage)

## Methods

### cleanup

static

cleanup()

Complete clean up tasks.

### makeChange

static

makeChange(before, after) returns Object

Make a `Change` object to be used as test data for Firestore and Realtime Database `onWrite` and `onUpdate` functions.

|                               #### Parameter                                ||
|--------|---------------------------------------------------------------------|
| before | Object Snapshot before the write or update. Value must not be null. |
| after  | Object Snapshot after the write or update. Value must not be null.  |

Returns

:   `non-null Object` A `Change` object for testing.

### mockConfig

static

mockConfig(config)

Mock values returned by `functions.config()`.

|                                     #### Parameter                                      ||
|--------|---------------------------------------------------------------------------------|
| config | Object Key value pairs representing the config to mock. Value must not be null. |

### wrap

static

wrap(cloudFunction) returns [test.WrappedFunction](https://firebase.google.com/docs/reference/functions/test/test#.WrappedFunction)

Takes a function to be tested, and returns a `WrappedFunction` which can be called in test code.

|                                                                                                     #### Parameter                                                                                                     ||
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cloudFunction | Object A CloudFunction is both an object that exports its trigger definitions at __trigger and can be called as a function using the JavaScript API for Google Cloud Functions. Value must not be null. |

Returns

:   `non-null `[test.WrappedFunction](https://firebase.google.com/docs/reference/functions/test/test#.WrappedFunction)

### WrappedFunction

static

WrappedFunction(data, options)

A function type that can be called with test data and optional override values for the event context. It will subsequently invoke the function it wraps with the provided test data and a generated event context.

|                                              #### Parameter                                              ||
|---------|-------------------------------------------------------------------------------------------------|
| data    | any type The test data. Value must not be null.                                                 |
| options | Object Override values for event context as an `EventContextOptions` object. Value may be null. |