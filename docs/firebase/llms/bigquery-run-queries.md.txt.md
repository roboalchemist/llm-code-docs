# Source: https://firebase.google.com/docs/crashlytics/bigquery-run-queries.md.txt

<br />

After you export your Crashlytics and (optionally) Firebase sessions data
into BigQuery, you can start working with the data:

- **Analyze data using SQL queries**   

  You can run queries on your Crashlytics data to generate custom reports
  and summaries. Since these types of custom reports aren't available in the
  Crashlytics dashboard of the Firebase console, they can supplement your
  analysis and understanding of crash data. See the collection of
  [example queries](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-queries) later on this page.

- **Join data from different datasets**   

  For example, if you choose to export Firebase sessions data when you set up
  Crashlytics data export, then you can improve understanding of crash-free
  users and crash-free sessions
  (see [example query](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-crash-free-metrics-sessions-data)).
  Also, you can export data from various Firebase products (like Performance Monitoring) or
  from Google Analytics and then join and analyze that data in
  BigQuery with your Crashlytics data.

- **Create views**   

  Using the BigQuery UI, you can create a *view* , which is a virtual
  table defined by a SQL query. For detailed instructions about the different
  types of views and how to create them, see the
  [BigQuery documentation](https://cloud.google.com/bigquery/docs/views-intro).

For details about the dataset schema, see
[Dataset schema for exported data in BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema).

## Learn about BigQuery SQL

- Learn about the
  [types of queries you can run](https://docs.cloud.google.com/bigquery/docs/running-queries),
  including interactive query jobs, batch query jobs, and continuous query jobs.

- Learn about the
  [supported statements and SQL dialects in BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction-sql).

- Learn how to
  [write queries using AI-powered assistance (Gemini)](https://docs.cloud.google.com/bigquery/docs/write-sql-gemini).

## Example queries for Crashlytics data

This section provides some example situations and example queries that
demonstrate how you can use BigQuery SQL with your exported
Crashlytics data and Firebase sessions data.

- [Calculate crash-free metrics using Firebase sessions data](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-crash-free-metrics-sessions-data)
- [Crashes by day](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-crashes-by-day)
- [Find the most pervasive crashes](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-find-most-pervasive-crashes)
- [Top 10 crashing devices](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-top-10-crashing-devices)
- [Filter by custom key](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-filter-by-custom-key)
- [Extract user IDs](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-extract-user-ids)
- [Find all users facing a particular crash issue](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-find-all-users-facing-a-particular-crash-issue)
- [Number of users impacted by a crash issue, broken down by country](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-number-users-impacted-by-country)
- [Top 5 issues so far today](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-top-5-issues-today)
- [Top 5 issues since DATE, including today](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-top-5-issues-since-date)

#### Example 1: Calculate crash-free metrics using Firebase sessions data

In your latest version, you launched a major revamp of your app to address
crashes in a critical user journey. You've received stellar reviews from users,
but you'd like quantitative evidence that your app is more stable than before.

[Crash-free metrics](https://firebase.google.com/docs/crashlytics/crash-free-metrics) can help provide this
information. These metrics are important measurements that help you understand
the overall health of your app. With Firebase sessions data and
Crashlytics events, you can calculate these metrics with a basic query.

Here are example queries for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

**Crash-free *users* for a specific version:**

```
SELECT
  TIMESTAMP_TRUNC(crashlytics.event_timestamp,DAY) AS event_date,
  (1 - (COUNT (DISTINCT installation_uuid) / COUNT (DISTINCT instance_id))) AS CFU
FROM
  `PROJECT_ID.firebase_sessions.PACKAGE_NAME_ANDROID` AS sessions
LEFT JOIN
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID` AS crashlytics
ON
  TIMESTAMP_TRUNC(sessions.event_timestamp,DAY) = TIMESTAMP_TRUNC(crashlytics.event_timestamp,DAY)
WHERE
  crashlytics.error_type="FATAL"
  AND crashlytics.application.display_version="APP_VERSION"
  AND sessions.application.display_version = "APP_VERSION"
GROUP BY
  event_date
ORDER BY
  event_date
```

**Crash-free *sessions* over the past week (past 168 hours):**

```
SELECT
  TIMESTAMP_TRUNC(crashlytics.event_timestamp,DAY) AS event_date,
  (1 - (COUNT (DISTINCT crashlytics.firebase_session_id) / COUNT (DISTINCT sessions.session_id))) AS CFS
FROM
  `PROJECT_ID.firebase_sessions.PACKAGE_NAME_ANDROID` AS sessions
LEFT JOIN
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID` AS crashlytics
ON
  TIMESTAMP_TRUNC(sessions.event_timestamp,DAY) = TIMESTAMP_TRUNC(crashlytics.event_timestamp,DAY)
WHERE
  crashlytics.error_type="FATAL" AND _PARTITIONTIME >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 168 HOUR)
  AND _PARTITIONTIME < CURRENT_TIMESTAMP()
GROUP BY
  event_date
ORDER BY
  event_date
```

#### Example 2: Crashes by day

After working to fix as many bugs as possible, you think your team is finally
ready to launch your new photo-sharing app. Before you do, you want to check the
number of crashes per day for the past month, to be sure your bug-bash made the
app more stable over time.

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT
  COUNT(DISTINCT event_id) AS number_of_crashes,
  FORMAT_TIMESTAMP("%F", event_timestamp) AS date_of_crashes
FROM
 `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`
GROUP BY
  date_of_crashes
ORDER BY
  date_of_crashes DESC
LIMIT 30;
```

#### Example 3: Find the most pervasive crashes

To properly prioritize production plans, you want to find the top 10 most
pervasive crashes in your app. You produce a query that provides the pertinent
points of data.

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT
  DISTINCT issue_id,
  COUNT(DISTINCT event_id) AS number_of_crashes,
  COUNT(DISTINCT installation_uuid) AS number_of_impacted_user,
  blame_frame.file,
  blame_frame.line
FROM
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`
WHERE
  event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(),INTERVAL 168 HOUR)
  AND event_timestamp < CURRENT_TIMESTAMP()
GROUP BY
  issue_id,
  blame_frame.file,
  blame_frame.line
ORDER BY
  number_of_crashes DESC
LIMIT 10;
```

#### Example 4: Top 10 crashing devices

Fall is new phone season! Your company knows that this also means it's new
device-specific issues season --- especially for Android. To get ahead of the
looming compatibility concerns, you put together a query that identifies the
10 devices that experienced the most crashes in the past week (168 hours).

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT
  device.model,
COUNT(DISTINCT event_id) AS number_of_crashes
FROM
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`
WHERE
  event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 168 HOUR)
  AND event_timestamp < CURRENT_TIMESTAMP()
GROUP BY
  device.model
ORDER BY
  number_of_crashes DESC
LIMIT 10;
```

#### Example 5: Filter by custom key

You're a game developer who wants to know which level of your game experiences
the most crashes.

To help track that stat, you set a custom Crashlytics key
([iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#add-keys) \|
[Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-keys) \|
[Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-keys) \|
[Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#add-keys)
)
called `current_level`, and update it every time the user reaches a new level.

### Swift

    Crashlytics.sharedInstance().setIntValue(3, forKey: "current_level");

### Objective-C

    CrashlyticsKit setIntValue:3 forKey:@"current_level";

### Java

    Crashlytics.setInt("current_level", 3);

With that key in your export to BigQuery, you can then write a query to
report the distribution of `current_level` values associated with each crash
event.

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT
COUNT(DISTINCT event_id) AS num_of_crashes,
  value
FROM
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`
UNNEST(custom_keys)
WHERE
  key = "current_level"
GROUP BY
  key,
  value
ORDER BY
  num_of_crashes DESC
```

#### Example 6: Extract user IDs

You have an Android app in early access. Most of your users love it, but three
have experienced an unusual number of crashes. To get to the bottom of the
problem, you write a query that pulls all the crash events for those users,
using their user IDs.

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT *
FROM
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`
WHERE
  user.id IN ("USER_ID_1", "USER_ID_2", "USER_ID_3")
ORDER BY
  user.id
 
```

#### Example 7: Find all users facing a particular crash issue

Your team has accidentally released a critical bug to a group of beta testers.
Your team was able to use the query from the
["Find most pervasive crashes" example](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-find-most-pervasive-crashes)
above to identify the specific crash issue ID. Now your team would like to run a
query to extract the list of app users who were impacted by this crash.

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT user.id as user_id
FROM
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`
WHERE
  issue_id = "ISSUE_ID"
  AND application.display_version = "APP_VERSION"
  AND user.id != ""
ORDER BY
  user.id;
```

#### Example 8: Number of users impacted by a crash issue, broken down by country

Your team has detected a critical bug during the rollout of a new release. You
were able to use the query from the
["Find most pervasive crashes" example](https://firebase.google.com/docs/crashlytics/bigquery-run-queries#example-find-most-pervasive-crashes)
above to identify the specific crash issue ID. Your team would now like to see
if this crash has spread to users in different countries around the world.

To write this query, your team will need to do the following:

1. Enable export of Google Analytics data to BigQuery.
   See [Export project data to BigQuery](https://firebase.google.com/docs/projects/bigquery-export).

2. Update your app to pass a user ID into both the Google Analytics SDK
   and the Crashlytics SDK.

   ### Swift

       Crashlytics.sharedInstance().setUserIdentifier("123456789");
       Analytics.setUserID("123456789");

   ### Objective-C

       CrashlyticsKit setUserIdentifier:@"123456789";
       FIRAnalytics setUserID:@"12345678 9";

   ### Java

       Crashlytics.setUserIdentifier("123456789");
       mFirebaseAnalytics.setUserId("123456789");

3. Write a query that uses the user ID field to join events in the
   Google Analytics dataset with crashes in the Crashlytics dataset.

   Here's an example query for an Android app. For an iOS app, use its
   bundle ID and `IOS` (instead of package name and `ANDROID`).

   ```
   SELECT DISTINCT c.issue_id, a.geo.country, COUNT(DISTINCT c.user.id) as num_users_impacted
   FROM `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID` c
   INNER JOIN  `PROJECT_ID.analytics_TABLE_NAME.events_*` a on c.user.id = a.user_id
   WHERE
     c.issue_id = "ISSUE_ID"
     AND a._TABLE_SUFFIX BETWEEN '20190101'
     AND '20200101'
   GROUP BY
     c.issue_id,
     a.geo.country,
     c.user.id
   ```

#### Example 9: Top 5 issues so far today

> [!NOTE]
> **Note:** This example requires [enabling Crashlytics streaming export to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-streaming).

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT
  issue_id,
  COUNT(DISTINCT event_id) AS events
FROM
  `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID_REALTIME`
WHERE
  DATE(event_timestamp) = CURRENT_DATE()
GROUP BY
  issue_id
ORDER BY
  events DESC
LIMIT
  5;
```

#### Example 10: Top 5 issues since DATE, including today

> [!NOTE]
> **Note:** This example requires [enabling Crashlytics streaming export to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-streaming).

You can also combine the batch and realtime tables with a stitching query to add
realtime information to the reliable batch data. Since `event_id` is a primary
key, you can use `DISTINCT event_id` to dedupe any common events from the two
tables.

Here's an example query for an Android app. For an iOS app, use its bundle ID
and `IOS` (instead of package name and `ANDROID`).

```
SELECT
  issue_id,
  COUNT(DISTINCT event_id) AS events
FROM (
  SELECT
    issue_id,
    event_id,
    event_timestamp
  FROM
    `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID_REALTIME`
  UNION ALL
  SELECT
    issue_id,
    event_id,
    event_timestamp
  FROM
    `PROJECT_ID.firebase_crashlytics.PACKAGE_NAME_ANDROID`)
WHERE
  event_timestamp >= PARSE_TIMESTAMP("%Y_%m_%d", "YYYY_MM_DD")
GROUP BY
  issue_id
ORDER BY
  events DESC
LIMIT
  5;
```

## What's next?

- [Build custom dashboards](https://firebase.google.com/docs/crashlytics/bigquery-custom-dashboards) using
  exported data and various Google Cloud services, like Looker Studio.

- Learn about the
  [dataset schema for exported data](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema).