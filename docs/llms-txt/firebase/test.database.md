# Source: https://firebase.google.com/docs/reference/functions/test/test.database.md.txt

# Namespace: database

# [test](https://firebase.google.com/docs/reference/functions/test/test).database

namespace static

Namespace for testing Realtime Database functions using the Cloud Functions for Firebase Test SDK.

## Methods

### exampleDataSnapshot

static

exampleDataSnapshot() returns test.database.DataSnapshot

Fetch an example data snapshot already populated with data. Can be passed into a wrapped database `onCreate` or `onDelete` function.

Returns

:   `non-null test.database.DataSnapshot`

### exampleDataSnapshotChange

static

exampleDataSnapshotChange() returns test.database.DataSnapshot

Fetch an example `Change` object of data snapshots already populated with data. Can be passed into a wrapped database `onUpdate` or `onWrite` function.

Returns

:   `non-null test.database.DataSnapshot`

### makeDataSnapshot

static

makeDataSnapshot(val, refPath, app) returns test.database.DataSnapshot

Create a data snapshot for testing.

|                                                                                                                                              #### Parameter                                                                                                                                              ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| val     | (string, number, boolean, or non-null Object) Value of data for the snapshot.                                                                                                                                                                                                                   |
| refPath | string Full path of the reference (e.g. 'users/alovelace').                                                                                                                                                                                                                                     |
| app     | firebase.app.App The Firebase app that the database belongs to. The `databaseURL` supplied when initializing the app is used for creating this snapshot. You do not need to supply this parameter if you supplied config values when initializing `firebase-functions-test`. Value may be null. |

Returns

:   `non-null test.database.DataSnapshot`