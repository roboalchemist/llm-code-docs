# Source: https://firebase.google.com/docs/reference/functions/test/global.md.txt

# Globals

# Globals

## Methods

### cleanup

cleanup()

Complete clean up tasks.

### makeChange

makeChange(before, after) returns Object

Make a `Change` object to be used as test data for Firestore and Realtime Database `onWrite` and `onUpdate` functions.

|                               #### Parameter                                ||
|--------|---------------------------------------------------------------------|
| before | Object Snapshot before the write or update. Value must not be null. |
| after  | Object Snapshot after the write or update. Value must not be null.  |

Returns

:   `non-null Object` A `Change` object for testing.

### mockConfig

mockConfig(config) returns any type

Mock values returned by `functions.config()`.

|                                     #### Parameter                                      ||
|--------|---------------------------------------------------------------------------------|
| config | Object Key value pairs representing the config to mock. Value must not be null. |

Returns

:   `any type`

### test

test(firebaseConfig, pathToServiceAccountKey)

Initialize the SDK.

|                                                                                                                                                                                            #### Parameter                                                                                                                                                                                             ||
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebaseConfig          | Object Firebase config values for initializing a Firebase app for your test code to interact with (e.g. making database writes). It is recommended that you use a project that is specifically for testing. If omitted, mock config values are used and your tests do not interact with a real Firebase app, and all Firebase methods need to be stubbed. Value may be null. |
| pathToServiceAccountKey | string Path to a service account key file to be used when initializing the Firebase app. Value may be null.                                                                                                                                                                                                                                                                  |

#### Example

    const test = require('firebase-functions-test')(); // Offline mode
    const test = require('firebase-functions-test')(firebaseConfigValues,
      path/to/key.json'); // Online mode

### wrap

wrap(cloudFunction)

Takes a function to be tested, and returns a `WrappedFunction` which can be called in test code.

|                                                                                                     #### Parameter                                                                                                     ||
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cloudFunction | Object A CloudFunction is both an object that exports its trigger definitions at __trigger and can be called as a function using the JavaScript API for Google Cloud Functions. Value must not be null. |

### WrappedFunction

WrappedFunction(data, options)

A function that can be called with test data and optional override values for the event context. It will subsequently invoke the function it wraps with the provided test data and a generated event context.

|                                              #### Parameter                                              ||
|---------|-------------------------------------------------------------------------------------------------|
| data    | any type The test data. Value must not be null.                                                 |
| options | Object Override values for event context as an `EventContextOptions` object. Value may be null. |