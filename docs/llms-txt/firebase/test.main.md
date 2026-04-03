# Source: https://firebase.google.com/docs/reference/functions/test/test.main.md.txt

# Namespace: main

# [test](https://firebase.google.com/docs/reference/functions/test/test).main

namespace static

Utility functions and types for creating and managing tests within the Cloud Functions for Firebase Test SDK.

## Properties

### auth

static

object

Authentication information for the user that triggered the function. This object contains `uid` and `token` properties for authenticated users. For more detail including token keys, see the
[security rules reference](https://firebase.google.com/docs/firestore/reference/security#properties).

For an unauthenticated user, this field is null. For event types that do not provide user information (all except Realtime Database) or for Firebase admin users, this field will not exist.

Defaults to null.

### authType

static

(string or undefined)

The level of permissions for a user. Valid values are:

- `ADMIN` Developer user or user authenticated via a service account.
- `USER` Known user.
- `UNAUTHENTICATED` Unauthenticated action
- `null` For event types that do not provide user information (all except Realtime Database).

### eventId

(string or undefined)

The event's unique identifier. If omitted, a random ID will be generated.

### params

(non-null Object or undefined)

The values for the wildcards in the reference path that a database or Firestore function is listening to. If omitted, random values are generated.

### timestamp

(string or undefined)

Timestamp for the event as an
[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) string. If omitted, the current time is used.

## Methods

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

mockConfig(config) returns any type

Mock values returned by `functions.config()`.

|                                     #### Parameter                                      ||
|--------|---------------------------------------------------------------------------------|
| config | Object Key value pairs representing the config to mock. Value must not be null. |

Returns

:   `any type`

### wrap

static

wrap(cloudFunction)

Takes a function to be tested, and returns a `WrappedFunction` which can be called in test code.

|                                                                                                     #### Parameter                                                                                                     ||
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cloudFunction | Object A CloudFunction is both an object that exports its trigger definitions at __trigger and can be called as a function using the JavaScript API for Google Cloud Functions. Value must not be null. |

### WrappedFunction

static

WrappedFunction(data, options)

A function that can be called with test data and optional override values for the event context. It will subsequently invoke the function it wraps with the provided test data and a generated event context.

|                                              #### Parameter                                              ||
|---------|-------------------------------------------------------------------------------------------------|
| data    | any type The test data. Value must not be null.                                                 |
| options | Object Override values for event context as an `EventContextOptions` object. Value may be null. |