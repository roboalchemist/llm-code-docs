# Source: https://firebase.google.com/docs/reference/functions/test/test.auth.md.txt

# Namespace: auth

# [test](https://firebase.google.com/docs/reference/functions/test/test).auth

namespace static

Namespace for testing Auth functions using the Cloud Functions for Firebase Test SDK.

## Methods

### exampleUserRecord

static

exampleUserRecord() returns functions.auth.UserRecord

Fetch an example `UserRecord` already populated with data.

Returns

:   `non-null functions.auth.UserRecord`

### makeUserRecord

static

makeUserRecord(fields) returns functions.auth.UserRecord

Function to create a `UserRecord`.

|                                                                                                      #### Parameter                                                                                                       ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fields | Object Fields of `UserRecord` to specify. Can be any subset of the fields in [functions.auth.UserRecord](https://firebase.google.com/docs/reference/functions/functions.auth.UserRecord). Value must not be null. |

Returns

:   `non-null functions.auth.UserRecord`