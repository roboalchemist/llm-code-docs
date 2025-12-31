# Source: https://firebase.google.com/docs/firestore/solutions/bigquery.md.txt

# Source: https://firebase.google.com/docs/ab-testing/bigquery.md.txt

# Source: https://firebase.google.com/docs/remote-config/personalization/bigquery.md.txt

# Source: https://firebase.google.com/docs/ab-testing/bigquery.md.txt

# Source: https://firebase.google.com/docs/remote-config/personalization/bigquery.md.txt

<br />

Remote Configpersonalization logs a`personalization_assignment`Analyticsevent when a personalization is assigned to a user, allowing you to use[BigQuery](https://cloud.google.com/bigquery)to inspect and analyze personalization events and associated events.
| **Tip:** You can also view`personalization_assignment`events on the[FirebaseAnalyticsEvents](https://console.firebase.google.com/project/_/analytics/events)page and view a detailed graph of results on the[Remote Configpersonalization results page](https://firebase.google.com/docs/remote-config/personalization/about#understand-personalization-results).

The following sections describe how to enableBigQueryexport forAnalyticsevents, how personalization events are stored, and provide some basic queries to get you started.

## EnableBigQueryexport forGoogle AnalyticsforFirebase

If you're on the Spark plan, you can use the[BigQuerysandbox to](https://cloud.google.com/bigquery/docs/sandbox)accessBigQueryat no cost, subject to[Sandbox limits](https://cloud.google.com/bigquery/docs/sandbox#limitations). See[Pricing and the BigQuery sandbox](https://firebase.google.com/docs/projects/bigquery-export?product=analytics#pricing)for more information.

First, make sure that you're exporting yourAnalyticsdata toBigQuery:

1. Open the[Integrations](https://console.firebase.google.com/project/_/settings/integrations)tab, which you can access usingsettings**\>** **Project settings** in the[Firebaseconsole](https://console.firebase.google.com/).
2. If you're already usingBigQuerywith other Firebase services, click**Manage** . Otherwise, click**Link**.
3. Review**About Linking Firebase toBigQuery** , then click**Next**.
4. In the**Configure integration** section, enable the**Google Analytics**toggle.
5. Select a region and choose export settings.

   | **Note:** For more information aboutGoogle AnalyticsforFirebasesettings, see[Data collection](https://support.google.com/analytics/answer/11593727).
6. Click**Link toBigQuery**.

Depending on how you chose to export data, it may take up to a day for the tables to become available. For more information about exporting project data toBigQuery, see[Export project data to BigQuery](https://firebase.google.com/docs/projects/bigquery-export?product=analytics).

Next, let's access and inspect our personalization events inBigQuery.

## AccessRemote Configpersonalization data usingBigQuery

To query analytics data for an experiment:

1. OpenBigQueryin the[Google Cloudconsole](https://console.cloud.google.com/bigquery). You can also open it directly from[AnalyticsEvents](https://console.firebase.google.com/project/_/analytics/events)using the**view your raw events inBigQuery**link at the bottom of the page.
2. Select yourFirebaseproject and expand it, then expand the`analytics_`<var translate="no">ANALYTICS_PROPERTY_ID</var>entry and click`events_`.

   ![Access personalization events in the Cloud console](https://firebase.google.com/static/docs/remote-config/personalization/images/bq-personalization-entry.png "Access personalization events in the Cloud console")
3. From the**Query** drop-down, select**In a new tab**.

   An auto-generated example query appears.
4. To view personalization events and associated data, update the query to select`personalization_assignment`events. The following example query will return a complete personalization assignment event for a specific date shard, limiting results to 10:

       # Select all personalization_assignment events
       SELECT *
       FROM `<var translate="no">PROJECT_NAME</var>.analytics_<var translate="no">ANALYTICS_PROPERTY_ID</var>.events_<var translate="no">DATE_SHARD</var>`
       WHERE event_name = 'personalization_assignment'
       LIMIT 10

   **Tip:** To search all event tables instead of the sharded table, you can replace the events table date with an asterisk (for example,<var translate="no">PROJECT_NAME</var>`.analytics_`<var translate="no">ANALYTICS_PROPERTY_ID</var>`.events_*`). This is not recommended in non-test scenarios or for large data sets.
5. In the query composer, select**Run query.**Results appear in the lower pane.

| **Note:** If you are not streamingAnalyticsdata,Firebasedata inBigQueryis updated only once daily. Therefore, the data available in the experiment page may be more up-to-date than the data available in theBigQueryconsole.

In the next section, we'll discuss what's included in a personalization assignment event in more detail.

## What personalization data is exported toBigQuery?

Personalization data is included inGoogle Analyticstables inBigQueryand stored in`personalization_assignment`events.

The basic fields provided in a personalization event are the same as anyAnalyticsevent as described in[\[GA4\]BigQueryExport schema](https://support.google.com/firebase/answer/7029846). You'll be mostly concerned with`user_pseudo_id`i(which can be used to differentiate distinct users), event timestamps, and other user properties.

Personalization-specific details are stored in the`event_params`field and are described in the following table:

|     **Parameter**     | **Data type** |                                                                                                           **Description**                                                                                                           |
|-----------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| personalization_id    | STRING        | Provides the assigned personalization's universally unique identifier (UUID).                                                                                                                                                       |
| group                 | STRING        | Indicates whether the user was assigned to the personalization group (P13N) or the baseline (BASELINE) group.                                                                                                                       |
| arm_index             | INTEGER       | Represents the alternative value assigned to the user, an integer between 0 and 4.                                                                                                                                                  |
| arm_key               | STRING        | Contains the parameter name used by the personalization.                                                                                                                                                                            |
| arm_value             | STRING        | Contains the alternative value string assigned by personalization.                                                                                                                                                                  |
| engaged_session_event | INTEGER       | Includes the number of sessions the user is engaged in. See[About sessions](https://support.google.com/analytics/answer/9191807)for more information.                                                                               |
| firebase_event_origin | STRING        | Indicates the origin of the event. This will always be`fp`for`personalization_assignment`events.                                                                                                                                    |
| firebase_screen_class | STRING        | Provides the class name of the screen on which the user was active when the personalization assignment occurred. See[Automatically collected events](https://support.google.com/analytics/answer/9234069)for more information.      |
| firebase_screen_id    | INTEGER       | Displays the ID of the screen the user was on when the personalization assignment occurred. See[Automatically collected events](https://support.google.com/analytics/answer/9234069)for more information.                           |
| first_open_time       | STRING        | Provides the timestamp, in UTC milliseconds, of the first time the user opened the app. See[Automatically collected events](https://support.google.com/analytics/answer/9234069)for more information.                               |
| ga_session_id         | INTEGER       | Provides theGoogle Analyticssession ID. See[About sessions](https://support.google.com/analytics/answer/9191807)for more information. You can use this to correlate the`personalization_assignment`event with otherAnalyticsevents. |
| ga_session_number     | INTEGER       | Provides theGoogle Analyticssession number. See[About sessions](https://support.google.com/analytics/answer/9191807)for more information.                                                                                           |

## Example queries

You can use a SQL statement like the following to extract the personalization-specific parameters from`personalization_assignment`events:  

        # Expand nested personalization parameters
        SELECT
         timestamp_micros(event_timestamp) AS event_time,
         user_pseudo_id,
         (
           SELECT event_params.value.string_value
           FROM UNNEST(event_params) event_params
           WHERE event_params.key = 'group'
         ) AS personalization_group,
         (
           SELECT event_params.value.string_value
           FROM UNNEST(event_params) event_params
           WHERE event_params.key = 'personalization_id'
         ) AS personalization_id,
         (
           SELECT event_params.value.string_value,
           FROM UNNEST(event_params) event_params
           WHERE event_params.key = 'arm_key'
         ) AS arm_key,
         (
           SELECT event_params.value.string_value
           FROM UNNEST(event_params) event_params
           WHERE event_params.key = 'arm_value'
         ) AS arm_value,
         (
           SELECT event_params.value.int_value
           FROM UNNEST(event_params) event_params
           WHERE event_params.key = 'ga_session_id'
         ) AS ga_session_id,
        FROM `<var translate="no">PROJECT_NAME</var>.analytics_<var translate="no">ANALYTICS_ACCOUNT_ID</var>.events_<var translate="no">DATE_SHARD</var>`
        WHERE event_name = 'personalization_assignment'
        LIMIT 10