# Source: https://firebase.google.com/docs/reference/functions/test/test.analytics.md.txt

# Namespace: analytics

# [test](https://firebase.google.com/docs/reference/functions/test/test).analytics

namespace static

Namespace for testing Analytics functions using the Cloud Functions for Firebase Test SDK.

## Methods

### exampleAnalyticsEvent

static

exampleAnalyticsEvent() returns functions.analytics.AnalyticsEvent

Fetch an example AnalyticsEvent already populated with data.

Returns

:   `non-null functions.analytics.AnalyticsEvent`

### makeAnalyticsEvent

static

makeAnalyticsEvent(fields) returns functions.analytics.AnalyticsEvent

Function to create an Analytics event.

|                                                                                                                 #### Parameter                                                                                                                  ||
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fields | Object Fields of `AnalyticsEvent` to specify. Can be any subset of the fields in [functions.analytics.analyticsEvent](https://firebase.google.com/docs/reference/functions/functions.analytics.AnalyticsEvent). Value must not be null. |

Returns

:   `non-null functions.analytics.AnalyticsEvent`