# Source: https://firebase.google.com/docs/reference/functions/test/test.crashlytics.md.txt

# Namespace: crashlytics

# [test](https://firebase.google.com/docs/reference/functions/test/test).crashlytics

namespace static

Namespace for testing Crashlytics functions using the Cloud Functions for Firebase Test SDK.

## Methods

### exampleIssue

static

exampleIssue() returns functions.crashlytics.Issue

Fetch an example Issue already populated with data.

Returns

:   `non-null functions.crashlytics.Issue`

### makeIssue

static

makeIssue(fields) returns functions.crashlytics.Issue

Function to create a Crashlytics event.

|                                                                                                                #### Parameter                                                                                                                ||
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fields | Object Fields of `CrashlyticsIssue` to specify for a test Can be any subset of the fields in [functions.crashlytics.Issue](https://firebase.google.comdocs/reference/functions/functions.crashlytics.Issue). Value must not be null. |

Returns

:   `non-null functions.crashlytics.Issue`