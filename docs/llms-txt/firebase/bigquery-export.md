# Source: https://firebase.google.com/docs/projects/bigquery-export.md.txt

# Source: https://firebase.google.com/docs/perf-mon/bigquery-export.md.txt

# Source: https://firebase.google.com/docs/crashlytics/bigquery-export.md.txt

<br />

You can export yourFirebase Crashlyticsdata into[BigQuery](https://console.cloud.google.com/bigquery/)for further analysis.BigQuerylets you analyze the data usingBigQuerySQL, export it to another cloud provider, and use it for visualization and custom dashboards withLookerStudio.

## What can you do with the exported data?

Exports toBigQuerycontain raw crash data including device type, operating system, exceptions (Android apps) or errors (Apple apps), andCrashlyticslogs, as well as other data. You can review exactly whatCrashlyticsdata is exported and its table[schema](https://firebase.google.com/docs/crashlytics/bigquery-export#understand-schema)later in this page.

Here are some examples of what you can do with your exportedCrashlyticsdata:

- **Run queries**   
  You can run queries on yourCrashlyticsdata to generate reports that aggregate crash event data into more easily-understood summaries. Since these types of reports aren't available in theCrashlyticsdashboard of theFirebaseconsole, they can supplement your analysis and understanding of crash data. Later on this page, find a selection of[example queries](https://firebase.google.com/docs/crashlytics/bigquery-export#example-queries).

- **Use aLookerStudiotemplate**   
  Crashlyticsprovides a[pre-builtLookerStudiotemplate](https://firebase.google.com/docs/crashlytics/bigquery-export#visualize-exported)for visualizing your exported data.

- **Create views**   
  Using theBigQueryUI, you can create a*view* , which is a virtual table defined by a SQL query. For detailed instructions about the different types of views and how to create them, see the[BigQuerydocumentation](https://cloud.google.com/bigquery/docs/views-intro).

- **CombineCrashlytics-specific data with Firebase sessions data**   
  You can also export Firebase sessions data when you set upCrashlyticsdata export. Use this sessions data to improve understanding of crash-free users and crash-free sessions.

### Benefits of streaming export toBigQuery

By default, data is exported toBigQueryin a daily batch export. Additionally, you can stream yourCrashlyticsdata and Firebase sessions in realtime with[BigQuerystreaming](https://cloud.google.com/bigquery/streaming-data-into-bigquery). You can use it for any purpose that requires live data, such as presenting information in a live dashboard, watching a rollout live, or monitoring application problems that trigger alerts and custom workflows.
| **Note:** Streaming export isn't available if your project is on the Spark pricing plan or using[BigQuerysandbox](https://cloud.google.com/bigquery/docs/sandbox)(no-cost access toBigQuery).

When you enable streaming export toBigQuery, you'll also have realtime tables (in addition to batch tables). Both types of tables will have the same[dataset schema](https://firebase.google.com/docs/crashlytics/bigquery-export#understand-schema), but here some important differences between batch tables and realtime tables:

|                                                                                                            **Batch table**                                                                                                             |                       **Realtime table**                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| - Data is exported once daily. - Events are durably stored before batch writing toBigQuery. - Data can be[backfilled](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer)up to 30 days prior\*. | - Data is exported in realtime. - No backfilling is available. |

The batch table is ideal for long-term analysis and identifying trends over time because we durably store events before writing them, and they can be backfilled to the table for up to 30 days\*. When we write data to your realtime table, we immediately write it toBigQuery, and so it is ideal for live dashboards and custom alerts. These two tables can be[combined with a stitching query](https://firebase.google.com/docs/crashlytics/bigquery-export#example-top-5-issues-since-date)to get the benefits of both.

By default, the realtime table has a partition expiration time of 30 days. To learn how to modify this, see[Set the partition expiration](https://cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration)in theBigQuerydocumentation.

^**\*** *See details about backfill support in[Upgrade to the new export infrastructure](https://firebase.google.com/docs/crashlytics/bigquery-export#upgraded-infrastructure).*^

<br />

*** ** * ** ***

## Enable export toBigQuery

| **Note:** Make sure that you have the[required level of access](https://firebase.google.com/docs/projects/bigquery-export#permissions-and-roles)to view or manage settings for data export toBigQuery.

1. In theFirebaseconsole, go to the[**Integrations**page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the**BigQuery** card, click**Link**.

3. Follow the on-screen instructions to enable export toBigQuery, including the following options:

   - To improve understanding of crash-free users and crash-free sessions,[enable Firebase sessions data export](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-sessions-export).

   - To get near realtime access to yourCrashlyticsdata and Firebase sessions data inBigQuery,[enable streaming export](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-streaming).

<br />

#### Enable Firebase sessions data export

<br />

| **Note:** To export sessions data intoBigQuery, your app must use*at minimum* the following versions of theCrashlyticsSDK:  
| Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

This option can also be enabled during the initial setup of export toBigQuery.

1. In theFirebaseconsole, go to the[**Integrations**page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the**BigQuery** card, click**Manage**.

3. Select the**Include sessions**checkbox.

This action enables export of session data for all of your linked apps. If you have streaming export enabled, this will start exporting session data in realtime as well.

<br />

<br />

<br />

#### Enable streaming export

<br />

| **Note:** Streaming export isn't available if your project is on the Spark pricing plan or using[BigQuerysandbox](https://cloud.google.com/bigquery/docs/sandbox)(no-cost access toBigQuery).

This option can also be enabled during the initial setup of export toBigQuery.

1. In theFirebaseconsole, go to the[**Integrations**page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the**BigQuery** card, click**Manage**.

3. Select the**Include streaming**checkbox.

This action enables streaming for all of your linked apps. If you have Firebase sessions export enabled, this will enable streaming export for session data as well.

<br />

<br />

### What happens when you enable export?

- **Firebase exports data from the apps linked toBigQuery.**

  - During setup, by default, all apps in your project are linked toBigQuery, but you can select to*not*link specific apps during setup.

  - Any apps that you later add to your Firebase project are automatically linked toBigQuery.

  - At any time, you can[manage which apps export data](https://support.google.com/firebase/answer/6318765#manage).

- **Firebase exports data to the dataset location you selected during setup.**

  - This location applies to both theCrashlyticsdataset and the Firebase sessions dataset (if sessions data is enabled for export).

  - This location is only applicable for the data exported intoBigQuery, and it does not impact the location of data stored for use in theCrashlyticsdashboard of theFirebaseconsole or in Android Studio.

  - After a dataset is created, its location can't be changed, but you can copy the dataset to a different location or manually move (recreate) the dataset in a different location. To learn more, see[Change the location for existing exports](https://firebase.google.com/docs/projects/bigquery-export#change-dataset-location).

  | **Note:** The capability to select and change the location for data export is*only* available if you enabled export after mid-October 2024 or if you[upgrade to the new export infrastructure](https://firebase.google.com/docs/crashlytics/bigquery-export#upgraded-infrastructure).
- **Firebase sets up daily syncs of your batch data toBigQuery.**

  - After linking toBigQuery, it may take up to 48 hours for the*initial*batch data export.

  - The daily sync happens once per day, regardless of any scheduled export that you might have set up inBigQuery. Note that the timing and duration of the sync job can change, so we don't recommend scheduling downstream operations or jobs based on a specific timing of the export.

- **Firebase[exports a copy of your existing data](https://firebase.google.com/docs/crashlytics/bigquery-export#what-data-exported)toBigQuery.**

  - For each linked app, this export includes a batch table containing the data from the daily sync.

  - You can[manually schedule data backfills](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer)for the batch table up to the past 30 days*or* for the most recent date when you enabled export toBigQuery(whichever is most recent).

  Note that if you enabled export ofCrashlyticsdata*before*mid-October 2024, you can also backfill 30 days prior to the day you enabled export.
- **The following applies if you[enable streaming export toBigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#streaming-export).**

  - Each linked app will also have its own realtime table containing constantly updating data (in addition to the app's batch table for daily batch export).

  - After enabling streaming, it may take up to 1 hour for data to begin streaming.

  <br />

  Are you not seeing data in your realtime table?

  <br />

  1. Make sure that you've sent at least two events from your app toCrashlyticsand waited a couple minutes after sending them.

  2. Make sure your Firebase project is on the pay-as-you-go Blaze pricing plan.  
     You can check this by looking in the bottom-left corner of the[Firebaseconsole](https://console.firebase.google.com/).

  3. If there's still no data in your realtime table after sending two events and waiting a couple minutes:

     1. Go to the[**BigQuery**card](https://console.firebase.google.com/project/_/settings/integrations)in theFirebaseconsole.

     2. Disable and then re-enable streaming export.

     3. Make sure the service account`service-`<var translate="no">PROJECT_NUMBER</var>`@gcp-sa-crashlytics.iam.gserviceaccount.com`is in your Firebase project and has the*Firebase Crashlytics Service Agent* role.  
        You can check this in the*IAM* page of the[Google Cloudconsole](https://console.cloud.google.com/iam-admin/iam)(make sure to select the checkbox for**Include Google-provided role grants**).

     4. Send at least two events toCrashlyticsand wait a couple minutes.

  4. If you still don't see data in your realtime table,[reach out to Firebase Support](https://firebase.google.com/support/troubleshooter/contact).

  <br />

  <br />

| **Note:** To deactivate export toBigQuery,[unlink your project](https://support.google.com/firebase/answer/6318765#unlink)in theFirebaseconsole.

<br />

*** ** * ** ***

## Example queries

#### Example 1: Calculate crash-free metrics using Firebase sessions data

In your latest version, you launched a major revamp of your app to address crashes in a critical user journey. You've received stellar reviews from users, but you'd like quantitative evidence that your app is more stable than before.

[Crash-free metrics](https://firebase.google.com/docs/crashlytics/crash-free-metrics)can help provide this information. These metrics are important measurements that help you understand the overall health of your app. With Firebase sessions data andCrashlyticsevents, you can calculate these metrics with a basic query.

Here are example queries for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).

**Crash-free*users*for a specific version:**  

```carbon
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
  AND crashlytics.application.display_version="<var translate="no">APP_VERSION</var>"
  AND sessions.application.display_version = "<var translate="no">APP_VERSION</var>"
GROUP BY
  event_date
ORDER BY
  event_date
```

**Crash-free*sessions*over the past week (past 168 hours):**  

```carbon
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

After working to fix as many bugs as possible, you think your team is finally ready to launch your new photo-sharing app. Before you do, you want to check the number of crashes per day for the past month, to be sure your bug-bash made the app more stable over time.

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```googlesql
SELECT
  COUNT(DISTINCT event_id) AS number_of_crashes,
  FORMAT_TIMESTAMP("%F", event_timestamp) AS date_of_crashes
FROM
 `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`
GROUP BY
  date_of_crashes
ORDER BY
  date_of_crashes DESC
LIMIT 30;
```

#### Example 3: Find the most pervasive crashes

To properly prioritize production plans, you want to find the top 10 most pervasive crashes in your app. You produce a query that provides the pertinent points of data.

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```googlesql
SELECT
  DISTINCT issue_id,
  COUNT(DISTINCT event_id) AS number_of_crashes,
  COUNT(DISTINCT installation_uuid) AS number_of_impacted_user,
  blame_frame.file,
  blame_frame.line
FROM
  `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`
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

Fall is new phone season! Your company knows that this also means it's new device-specific issues season --- especially for Android. To get ahead of the looming compatibility concerns, you put together a query that identifies the 10 devices that experienced the most crashes in the past week (168 hours).

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```googlesql
SELECT
  device.model,
COUNT(DISTINCT event_id) AS number_of_crashes
FROM
  `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`
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

You're a game developer who wants to know which level of your game experiences the most crashes.

To help track that stat, you set a customCrashlyticskey ([iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#add-keys)\|[Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-keys)\|[Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-keys)\|[Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#add-keys)) called`current_level`, and update it every time the user reaches a new level.  

### Swift

    Crashlytics.sharedInstance().setIntValue(3, forKey: "current_level");

### Objective-C

    CrashlyticsKit setIntValue:3 forKey:@"current_level";

### Java

    Crashlytics.setInt("current_level", 3);

With that key in your export toBigQuery, you can then write a query to report the distribution of`current_level`values associated with each crash event.

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```scdoc
SELECT
COUNT(DISTINCT event_id) AS num_of_crashes,
  value
FROM
  `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`
UNNEST(custom_keys)
WHERE
  key = "current_level"
GROUP BY
  key,
  value
ORDER BY
  num_of_crashes DESC
```

#### Example 6: User ID extraction

You have an Android app in early access. Most of your users love it, but three have experienced an unusual number of crashes. To get to the bottom of the problem, you write a query that pulls all the crash events for those users, using their user IDs.

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```scdoc
SELECT *
FROM
  `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`
WHERE
  user.id IN ("USER_ID_1", "USER_ID_2", "USER_ID_3")
ORDER BY
  user.id
 
```

#### Example 7: Find all users facing a particular crash issue

Your team has accidentally released a critical bug to a group of beta testers. Your team was able to use the query from the["Find most pervasive crashes" example](https://firebase.google.com/docs/crashlytics/bigquery-export#example-find-most-pervasive-crashes)above to identify the specific crash issue ID. Now your team would like to run a query to extract the list of app users who were impacted by this crash.

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```scdoc
SELECT user.id as user_id
FROM
  `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`
WHERE
  issue_id = "ISSUE_ID"
  AND application.display_version = "APP_VERSION"
  AND user.id != ""
ORDER BY
  user.id;
```

#### Example 8: Number of users impacted by a crash issue, broken down by country

Your team has detected a critical bug during the rollout of a new release. You were able to use the query from the["Find most pervasive crashes" example](https://firebase.google.com/docs/crashlytics/bigquery-export#example-find-most-pervasive-crashes)above to identify the specific crash issue ID. Your team would now like to see if this crash has spread to users in different countries around the world.

To write this query, your team will need to do the following:

1. Enable export ofGoogle Analyticsdata toBigQuery. See[Export project data to BigQuery](https://firebase.google.com/docs/projects/bigquery-export).

2. Update your app to pass a user ID into both theGoogle AnalyticsSDK and theCrashlyticsSDK.

   ### Swift

       Crashlytics.sharedInstance().setUserIdentifier("123456789");
       Analytics.setUserID("123456789");

   ### Objective-C

       CrashlyticsKit setUserIdentifier:@"123456789";
       FIRAnalytics setUserID:@"12345678 9";

   ### Java

       Crashlytics.setUserIdentifier("123456789");
       mFirebaseAnalytics.setUserId("123456789");

3. Write a query that uses the user ID field to join events in theGoogle Analyticsdataset with crashes in theCrashlyticsdataset.

   Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

   ```scdoc
   SELECT DISTINCT c.issue_id, a.geo.country, COUNT(DISTINCT c.user.id) as num_users_impacted
   FROM `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID` c
   INNER JOIN  `<var translate="no">PROJECT_ID</var>.analytics_<var translate="no">TABLE_NAME</var>.events_*` a on c.user.id = a.user_id
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

| **Note:** This example requires[enablingCrashlyticsstreaming export toBigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-streaming).

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```googlesql
SELECT
  issue_id,
  COUNT(DISTINCT event_id) AS events
FROM
  `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID_REALTIME`
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

| **Note:** This example requires[enablingCrashlyticsstreaming export toBigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-streaming).

You can also combine the batch and realtime tables with a stitching query to add realtime information to the reliable batch data. Since`event_id`is a primary key, you can use`DISTINCT event_id`to dedupe any common events from the two tables.

Here's an example query for an Android app. For an iOS app, use its bundle ID and`IOS`(instead of package name and`ANDROID`).  

```googlesql
SELECT
  issue_id,
  COUNT(DISTINCT event_id) AS events
FROM (
  SELECT
    issue_id,
    event_id,
    event_timestamp
  FROM
    `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID_REALTIME`
  UNION ALL
  SELECT
    issue_id,
    event_id,
    event_timestamp
  FROM
    `<var translate="no">PROJECT_ID</var>.firebase_crashlytics.<var translate="no">PACKAGE_NAME</var>_ANDROID`)
WHERE
  event_timestamp >= PARSE_TIMESTAMP("%Y_%m_%d", "<var translate="no">YYYY_MM_DD</var>")
GROUP BY
  issue_id
ORDER BY
  events DESC
LIMIT
  5;
```

<br />

*** ** * ** ***

## Visualize exportedCrashlyticsdata withLookerStudio

[LookerStudio](https://cloud.google.com/looker-studio)turns yourCrashlyticsdatasets inBigQueryinto reports that are easier to read, easier to share, and fully customizable.

To learn more about usingLookerStudio, check out their[welcome guide](https://cloud.google.com/looker/docs/studio).

### Use aCrashlyticsreport template

LookerStudiohas a sample report forCrashlyticsthat includes a comprehensive set of dimensions and metrics from the exportedCrashlyticsBigQueryschema. If you've enabledCrashlyticsstreaming export toBigQuery, then you can view that data on the**Realtime trends** page of theLookerStudiotemplate.You can use the sample as a template to quickly create new reports and visualizations based on your own app's raw crash data:

1. Open the[CrashlyticsLookerStudioDashboard template](https://datastudio.google.com/c/reporting/10TMAKxL0ZxcNGTLDQy1LAF5V7uNDYxRC/page/1xZU/preview).

2. Click**Use Template**in the upper-right corner.

3. In the**New Data Source** drop down, select**Create New Data Source**.

4. Click**Select** on the**BigQuery**card.

5. Select a table containing exportedCrashlyticsdata by choosing**My Projects \><var translate="no">PROJECT_ID</var>\> firebase_crashlytics \><var translate="no">TABLE_NAME</var>**.

   Your batch table is always available to select. IfCrashlyticsstreaming export toBigQueryis enabled, then you can select your realtime table instead.
6. Under**Configuration** , set**CrashlyticsTemplate level** to**Default**.

7. Click**Connect**to create the new data source.

8. Click**Add to Report** to return to theCrashlyticstemplate.

9. Finally, click**Create Report** to create your copy of theCrashlyticsLookerStudioDashboard template.

| **Note:** If you linkedCrashlyticstoBigQuerybefore December 6, 2018, then your dataset is named**My Projects \><var translate="no">PROJECT_ID</var>\> crashlytics \><var translate="no">TABLE_NAME</var>**.

<br />

*** ** * ** ***

## Understand the schema inBigQuery

Firebase creates new datasets inBigQueryfor your exported data:

- [Crashlyticsdataset](https://firebase.google.com/docs/crashlytics/bigquery-export#dataset-schema-crashlytics)

- [Firebase sessions dataset](https://firebase.google.com/docs/crashlytics/bigquery-export#dataset-schema-sessions)(if sessions data is enabled for export)

### Crashlyticsdataset

Crashlyticsdata is exported into aBigQuerydataset named`firebase_crashlytics`. The dataset covers your entire project, even if it has multiple apps.

#### Tables

By default, Firebase creates individual tables inside theCrashlyticsdataset for each app in your project that's linked toBigQuery.

The tables are named based on the app's identifier (with periods converted to underscores) and appended with the app's platform (`_IOS`or`_ANDROID`). For example, data for an Android app with the package name`com.google.test`would be in a table named`com_google_test_ANDROID`.
| **Note:** You may also choose to opt out of exporting data intoBigQueryfor specific apps in your project from within theFirebaseconsole.

- If streaming export toBigQueryis enabled, then data will also be streamed in realtime to a table appended with`_REALTIME`(for example,`com_google_test_ANDROID_REALTIME`).

- Each row in a table represents an event that occurred in the app, including crashes, non-fatal errors, and ANRs.

- The tables contain a standard set ofCrashlyticsdata in addition to any customCrashlyticskeys defined by you in your app ([iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#add-keys)\|[Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-keys)\|[Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-keys)\|[Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#add-keys)).

#### Rows

Each row in a table represents an error the app encountered.

#### Columns

The columns in a table are identical for crashes, non-fatal errors, and ANRs.

- If streaming export toBigQueryis enabled, then the realtime table will have the same columns as the batch table.

- You might have columns in rows that represent events that don't have stack traces.

Here are the columns in the table for the exportedCrashlyticsdata:

|                   Field name                   |    Data type    |                                                                                                        Description                                                                                                         |
|------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app_orientation`                              | STRING          | For example,`PORTRAIT`,`LANDSCAPE`,`FACE_UP`,`FACE_DOWN`, etc.                                                                                                                                                             |
| `application`                                  | RECORD          | The app that generated the event                                                                                                                                                                                           |
| `application.build_version`                    | STRING          | The app's build version                                                                                                                                                                                                    |
| `application.display_version`                  | STRING          |                                                                                                                                                                                                                            |
| `blame_frame`                                  | RECORD          | The frame identified as the root cause of the crash or error                                                                                                                                                               |
| `blame_frame.address`                          | INT64           | The address in the binary image which contains the code Unset for Java frames                                                                                                                                              |
| `blame_frame.blamed`                           | BOOLEAN         | WhetherCrashlyticsdetermined that this frame is the cause of the crash or error                                                                                                                                            |
| `blame_frame.file`                             | STRING          | The name of the frame file                                                                                                                                                                                                 |
| `blame_frame.library`                          | STRING          | The display name of the library that includes the frame                                                                                                                                                                    |
| `blame_frame.line`                             | INT64           | The line number of the file of the frame                                                                                                                                                                                   |
| `blame_frame.offset`                           | INT64           | The byte offset into the binary image that contains the code Unset for Java exceptions                                                                                                                                     |
| `blame_frame.owner`                            | STRING          | For example,`DEVELOPER`,`VENDOR`,`RUNTIME`,`PLATFORM`, or`SYSTEM`                                                                                                                                                          |
| `blame_frame.symbol`                           | STRING          | The hydrated symbol, or raw symbol if it's unhydrateable                                                                                                                                                                   |
| `breadcrumbs`                                  | REPEATED RECORD | Timestamped[Google Analyticsbreadcrumbs](https://firebase.google.com/docs/crashlytics/customize-crash-reports#get-breadcrumb-logs), if enabled                                                                             |
| `breadcrumbs.name`                             | STRING          | The name associated with the breadcrumb                                                                                                                                                                                    |
| `breadcrumbs.params`                           | REPEATED RECORD | Parameters associated with the breadcrumb                                                                                                                                                                                  |
| `breadcrumbs.params.key`                       | STRING          | A parameter key associated with the breadcrumb                                                                                                                                                                             |
| `breadcrumbs.params.value`                     | STRING          | A parameter value associated with the breadcrumb                                                                                                                                                                           |
| `breadcrumbs.timestamp`                        | TIMESTAMP       | The timestamp associated with the breadcrumb                                                                                                                                                                               |
| `bundle_identifier`                            | STRING          | The unique identifier for the app as registered in the Firebase project (for example,`com.google.gmail`) For Apple platform apps, this is the bundle ID of the app. For Android apps, this is the package name of the app. |
| `crashlytics_sdk_versions`                     | STRING          | TheCrashlyticsSDK version that generated the event                                                                                                                                                                         |
| `custom_keys`                                  | REPEATED RECORD | Developer-defined key-value pairs                                                                                                                                                                                          |
| `custom_keys.key`                              | STRING          | A developer-defined key                                                                                                                                                                                                    |
| `custom_keys.value`                            | STRING          | A developer-defined value                                                                                                                                                                                                  |
| `device`                                       | RECORD          | The device the event occurred on                                                                                                                                                                                           |
| `device_orientation`                           | STRING          | For example,`PORTRAIT`,`LANDSCAPE`,`FACE_UP`,`FACE_DOWN`, etc.                                                                                                                                                             |
| `device.architecture`                          | STRING          | For example,`X86_32`,`X86_64`,`ARMV7`,`ARM64`,`ARMV7S`, or`ARMV7K`                                                                                                                                                         |
| `device.manufacturer`                          | STRING          | The device manufacturer                                                                                                                                                                                                    |
| `device.model`                                 | STRING          | The device model                                                                                                                                                                                                           |
| `error`                                        | REPEATED RECORD | *(Apple apps only)*non-fatal errors                                                                                                                                                                                        |
| `error_type`                                   | STRING          | The error type of the event (for example,`FATAL`,`NON_FATAL`,`ANR`, etc.)                                                                                                                                                  |
| `error.blamed`                                 | BOOLEAN         | WhetherCrashlyticsdetermined that this frame is the cause of the error                                                                                                                                                     |
| `error.code`                                   | INT64           | Error code associated with the app's custom logged NSError                                                                                                                                                                 |
| `error.frames`                                 | REPEATED RECORD | The frames of the stacktrace                                                                                                                                                                                               |
| `error.frames.address`                         | INT64           | The address in the binary image which contains the code                                                                                                                                                                    |
| `error.frames.blamed`                          | BOOLEAN         | WhetherCrashlyticsdetermined that this frame is the cause of the error                                                                                                                                                     |
| `error.frames.file`                            | STRING          | The name of the frame file                                                                                                                                                                                                 |
| `error.frames.library`                         | STRING          | The display name of the library that includes the frame                                                                                                                                                                    |
| `error.frames.line`                            | INT64           | The line number of the file of the frame                                                                                                                                                                                   |
| `error.frames.offset`                          | INT64           | The byte offset into the binary image that contains the code                                                                                                                                                               |
| `error.frames.owner`                           | STRING          | For example,`DEVELOPER`,`VENDOR`,`RUNTIME`,`PLATFORM`, or`SYSTEM`                                                                                                                                                          |
| `error.frames.symbol`                          | STRING          | The hydrated symbol, or raw symbol if it's unhydrateable                                                                                                                                                                   |
| `error.queue_name`                             | STRING          | The queue the thread was running on                                                                                                                                                                                        |
| `error.subtitle`                               | STRING          | The subtitle of the thread                                                                                                                                                                                                 |
| `error.title`                                  | STRING          | The title of the thread                                                                                                                                                                                                    |
| `event_id`                                     | STRING          | The unique ID for the event                                                                                                                                                                                                |
| `event_timestamp`                              | TIMESTAMP       | When the event occurred                                                                                                                                                                                                    |
| `exceptions`                                   | REPEATED RECORD | *(Android only)*Exceptions that occurred during this event. Nested exceptions are presented in reverse chronological order, which means that the last record is the first exception thrown                                 |
| `exceptions.blamed`                            | BOOLEAN         | True ifCrashlyticsdetermines the exception is responsible for the error or crash                                                                                                                                           |
| `exceptions.exception_message`                 | STRING          | A message associated with the exception                                                                                                                                                                                    |
| `exceptions.frames`                            | REPEATED RECORD | The frames associated with the exception                                                                                                                                                                                   |
| `exceptions.frames.address`                    | INT64           | The address in the binary image which contains the code Unset for Java frames                                                                                                                                              |
| `exceptions.frames.blamed`                     | BOOLEAN         | WhetherCrashlyticsdetermined that this frame is the cause of the crash or error                                                                                                                                            |
| `exceptions.frames.file`                       | STRING          | The name of the frame file                                                                                                                                                                                                 |
| `exceptions.frames.library`                    | STRING          | The display name of the library that includes the frame                                                                                                                                                                    |
| `exceptions.frames.line`                       | INT64           | The line number of the file of the frame                                                                                                                                                                                   |
| `exceptions.frames.offset`                     | INT64           | The byte offset into the binary image that contains the code Unset for Java exceptions                                                                                                                                     |
| `exceptions.frames.owner`                      | STRING          | For example,`DEVELOPER`,`VENDOR`,`RUNTIME`,`PLATFORM`, or`SYSTEM`                                                                                                                                                          |
| `exceptions.frames.symbol`                     | STRING          | The hydrated symbol, or raw symbol if it's unhydrateable                                                                                                                                                                   |
| `exceptions.nested`                            | BOOLEAN         | True for all but the last-thrown exception (meaning the first record)                                                                                                                                                      |
| `exceptions.subtitle`                          | STRING          | The subtitle of the thread                                                                                                                                                                                                 |
| `exceptions.title`                             | STRING          | The title of the thread                                                                                                                                                                                                    |
| `exceptions.type`                              | STRING          | The exception type (for example,`java.lang.IllegalStateException)`                                                                                                                                                         |
| `firebase_session_id`                          | STRING          | The automatically generated ID for the Firebase session mapped to the event fromCrashlytics                                                                                                                                |
| `installation_uuid`                            | STRING          | An ID that identifies a unique app and device installation                                                                                                                                                                 |
| `is_fatal`                                     | BOOLEAN         | | This field is deprecated. Use`error_type`instead. Whether the app crashed                                                                                                                                                |
| `issue_id`                                     | STRING          | The issue associated with the event                                                                                                                                                                                        |
| `logs`                                         | REPEATED RECORD | Timestamped log messages generated by theCrashlyticslogger, if enabled                                                                                                                                                     |
| `logs.message`                                 | STRING          | The logged message                                                                                                                                                                                                         |
| `logs.timestamp`                               | TIMESTAMP       | When the log was made                                                                                                                                                                                                      |
| `memory`                                       | RECORD          | The device's memory status                                                                                                                                                                                                 |
| `memory.free`                                  | INT64           | Bytes of memory remaining                                                                                                                                                                                                  |
| `memory.used`                                  | INT64           | Bytes of memory used                                                                                                                                                                                                       |
| `operating_system`                             | RECORD          | The details of the OS on the device                                                                                                                                                                                        |
| `operating_system.device_type`                 | STRING          | The type of device (for example,`MOBILE`,`TABLET`,`TV`, etc.); also known as "device category"                                                                                                                             |
| `operating_system.display_version`             | STRING          | The version of the OS on the device                                                                                                                                                                                        |
| `operating_system.modification_state`          | STRING          | Whether the device has been modified (for example, a jailbroken app is`MODIFIED`and a rooted app is`UNMODIFIED`)                                                                                                           |
| `operating_system.name`                        | STRING          | The name of the OS on the device                                                                                                                                                                                           |
| `operating_system.type`                        | STRING          | *(Apple apps only)* The type of OS running on the device (for example,`IOS`,`MACOS`, etc.)                                                                                                                                 |
| `platform`                                     | STRING          | The platform of the app as registered in the Firebase project (valid values:`IOS`or`ANDROID`)                                                                                                                              |
| `process_state`                                | STRING          | `BACKGROUND`or`FOREGROUND`                                                                                                                                                                                                 |
| `storage`                                      | RECORD          | The device's persistent storage                                                                                                                                                                                            |
| `storage.free`                                 | INT64           | Bytes of storage remaining                                                                                                                                                                                                 |
| `storage.used`                                 | INT64           | Bytes of storage used                                                                                                                                                                                                      |
| `threads`                                      | REPEATED RECORD | Threads present at the time of the event                                                                                                                                                                                   |
| `threads.blamed`                               | BOOLEAN         | WhetherCrashlyticsdetermined that this frame is the cause of the crash or error                                                                                                                                            |
| `threads.code`                                 | INT64           | *(Apple apps only)*Error code of the application's custom logged NSError                                                                                                                                                   |
| `threads.crash_address`                        | INT64           | The address of the signal that caused the application to crash; only present on crashed native threads                                                                                                                     |
| `threads.crashed`                              | BOOLEAN         | Whether the thread crashed                                                                                                                                                                                                 |
| `threads.frames`                               | REPEATED RECORD | The frames of the thread                                                                                                                                                                                                   |
| `threads.frames.address`                       | INT64           | The address in the binary image which contains the code                                                                                                                                                                    |
| `threads.frames.blamed`                        | BOOLEAN         | WhetherCrashlyticsdetermined that this frame is the cause of the error                                                                                                                                                     |
| `threads.frames.file`                          | STRING          | The name of the frame file                                                                                                                                                                                                 |
| `threads.frames.library`                       | STRING          | The display name of the library that includes the frame                                                                                                                                                                    |
| `threads.frames.line`                          | INT64           | The line number of the file of the frame                                                                                                                                                                                   |
| `threads.frames.offset`                        | INT64           | The byte offset into the binary image that contains the code                                                                                                                                                               |
| `threads.frames.owner`                         | STRING          | For example,`DEVELOPER`,`VENDOR`,`RUNTIME`,`PLATFORM`, or`SYSTEM`                                                                                                                                                          |
| `threads.frames.symbol`                        | STRING          | The hydrated symbol, or raw symbol if it's unhydreatable                                                                                                                                                                   |
| `threads.queue_name`                           | STRING          | *(Apple apps only)*The queue the thread was running on                                                                                                                                                                     |
| `threads.signal_code`                          | STRING          | The code of the signal that caused the app to crash; only present on crashed native threads                                                                                                                                |
| `threads.signal_name`                          | STRING          | The name of the signal that caused the app to crash, only present on crashed native threads                                                                                                                                |
| `threads.subtitle`                             | STRING          | The subtitle of the thread                                                                                                                                                                                                 |
| `threads.thread_name`                          | STRING          | The thread's name                                                                                                                                                                                                          |
| `threads.title`                                | STRING          | The title of the thread                                                                                                                                                                                                    |
| `unity_metadata.debug_build`                   | BOOLEAN         | If this is a debug build                                                                                                                                                                                                   |
| `unity_metadata.graphics_copy_texture_support` | STRING          | Support for copying graphics texture as defined in the[Unity API](https://docs.unity3d.com/ScriptReference/Rendering.CopyTextureSupport.html)                                                                              |
| `unity_metadata.graphics_device_id`            | INT64           | The identifier of the graphics device                                                                                                                                                                                      |
| `unity_metadata.graphics_device_name`          | STRING          | The name of the graphics device                                                                                                                                                                                            |
| `unity_metadata.graphics_device_type`          | STRING          | The type of the graphics device                                                                                                                                                                                            |
| `unity_metadata.graphics_device_vendor_id`     | INT64           | The identifier of the graphics processor's vendor                                                                                                                                                                          |
| `unity_metadata.graphics_device_vendor`        | STRING          | The vendor of the graphics device                                                                                                                                                                                          |
| `unity_metadata.graphics_device_version`       | STRING          | The version of the graphics device                                                                                                                                                                                         |
| `unity_metadata.graphics_max_texture_size`     | INT64           | The maximum size dedicated to rendering texture                                                                                                                                                                            |
| `unity_metadata.graphics_memory_size_mb`       | INT64           | The graphics memory in MB                                                                                                                                                                                                  |
| `unity_metadata.graphics_render_target_count`  | INT64           | The number of graphical rendering targets                                                                                                                                                                                  |
| `unity_metadata.graphics_shader_level`         | INT64           | The shader level of the graphics                                                                                                                                                                                           |
| `unity_metadata.processor_count`               | INT64           | The number of processors (cores)                                                                                                                                                                                           |
| `unity_metadata.processor_frequency_mhz`       | INT64           | The frequency of the processor(s) in MHz                                                                                                                                                                                   |
| `unity_metadata.processor_type`                | STRING          | The type of processor                                                                                                                                                                                                      |
| `unity_metadata.screen_refresh_rate_hz`        | INT64           | The refresh rate of the screen in Hz                                                                                                                                                                                       |
| `unity_metadata.screen_resolution_dpi`         | STRING          | The DPI of the screen as a floating point number                                                                                                                                                                           |
| `unity_metadata.screen_size_px`                | STRING          | The size of the screen in pixels, formatted as width x height                                                                                                                                                              |
| `unity_metadata.system_memory_size_mb`         | INT64           | The size of the system's memory in Mb                                                                                                                                                                                      |
| `unity_metadata.unity_version`                 | STRING          | The version of Unity running on this device                                                                                                                                                                                |
| `user`                                         | RECORD          | *(Optional)*Info collected about the app's user                                                                                                                                                                            |
| `user.email`                                   | STRING          | | This field is deprecated; do not use this field. *(Optional)*The user's email address                                                                                                                                    |
| `user.id`                                      | STRING          | *(Optional)*An app-specific ID associated with the user                                                                                                                                                                    |
| `user.name`                                    | STRING          | | This field is deprecated; do not use this field. *(Optional)*The user's name                                                                                                                                             |
| `variant_id`                                   | STRING          | The issue variant associated with this event Note that not all events have an associated issue variant.                                                                                                                    |

### Firebase sessions dataset

Firebase sessions data is exported into aBigQuerydataset named`firebase_sessions`. The dataset covers your entire project, even if it has multiple apps.

#### Tables

By default, Firebase creates individual tables inside the Firebase sessions dataset for each app in your project that's linked toBigQuery.

The tables are named based on the app's identifier (with periods converted to underscores) and appended with the app's platform (`_IOS`or`_ANDROID`). For example, data for an Android app with the package name`com.google.test`would be in a table named`com_google_test_ANDROID`.

#### Rows

Each row in a table represents a session event that happened.

#### Columns

If streaming export toBigQueryis enabled, then the realtime table will have the same columns as the batch table.

Here are the columns within the table for the exported Firebase sessions data:

|              Field name               | Data type |                                                                                                                             Description                                                                                                                              |
|---------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `instance_id`                         | STRING    | The Firebase installation ID (FID) from the device. Identifies a unique app + device installation                                                                                                                                                                    |
| `session_id`                          | STRING    | The unique ID of this session                                                                                                                                                                                                                                        |
| `first_session_id`                    | STRING    | The first ID of a series of sessions this session is in since the app was cold started. This can be used to group all sessions that have occurred since a cold start. If this session is the first session, this field will be the same as`session_id`.              |
| `session_index`                       | INTEGER   | The order this session came in after the app was cold started. For the first session after a cold start, this will be`0`. The index will be incremented every time a session is generated without a cold start occurring (for example, after 30 mins of inactivity). |
| `event_type`                          | STRING    | The type of event that happened in the session (for example,`SESSION_START`)                                                                                                                                                                                         |
| `event_timestamp`                     | TIMESTAMP | The time of the event's occurrence                                                                                                                                                                                                                                   |
| `received_timestamp`                  | TIMESTAMP | The time the event was received by the server from the device                                                                                                                                                                                                        |
| `performance_data_collection_enabled` | BOOLEAN   | Whether the Firebase Performance Monitoring SDK data collection was enabled at the time of the session                                                                                                                                                               |
| `crashlytics_data_collection_enabled` | BOOLEAN   | Whether the Firebase Crashlytics SDK data collection was enabled at the time of the session                                                                                                                                                                          |
| `application`                         | RECORD    | Describes the application                                                                                                                                                                                                                                            |
| `application.build_version`           | STRING    | The build version of the application (for example,`1523456`)                                                                                                                                                                                                         |
| `application.display_version`         | STRING    | The display version of the application (for example,`4.1.7`)                                                                                                                                                                                                         |
| `device`                              | RECORD    | The device on which the event occurred                                                                                                                                                                                                                               |
| `device.model`                        | STRING    | The model of the device                                                                                                                                                                                                                                              |
| `device.manufacturer`                 | STRING    | The manufacturer of the device. For Apple platform apps, this will be`NULL`.                                                                                                                                                                                         |
| `operating_system`                    | RECORD    | Describes the OS of the device                                                                                                                                                                                                                                       |
| `operating_system.display_version`    | STRING    | The display version of the operating system (for example,`10.2.1`)                                                                                                                                                                                                   |
| `operating_system.name`               | STRING    | The name of the operating system                                                                                                                                                                                                                                     |
| `operating_system.type`               | STRING    | The type of the operating system (for example,`IOS`). This field is only set for Apple devices.                                                                                                                                                                      |
| `operating_system.device_type`        | STRING    | The type of device (for example,`MOBILE`,`TABLET`,`TV`)                                                                                                                                                                                                              |

<br />

*** ** * ** ***

## Upgrade to the new export infrastructure forBigQuery

In mid-October 2024,Crashlyticslaunched a new infrastructure for*batch* export ofCrashlyticsdata intoBigQuery.

- If you enabled batch export***after**October 2024* , then your Firebase project is automatically using the new export infrastructure.**No action is needed.**

- If you enabled batch export***before or during**October 2024* , review the information in["How to upgrade to the new export infrastructure for BigQuery?"](https://firebase.google.com/docs/crashlytics/troubleshooting#bigquery-upgraded-export-infra)to determine if you need to take any action.