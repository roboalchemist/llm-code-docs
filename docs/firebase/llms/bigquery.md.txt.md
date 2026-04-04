# Source: https://firebase.google.com/docs/ab-testing/bigquery.md.txt

In addition to viewing A/B Testing experiment data in the
Firebase console, you can inspect and analyze experiment data in
BigQuery. While A/B Testing does not have a separate
BigQuery table, experiment and variant memberships are stored on every
Google Analytics event within the Analytics event tables.

The user properties that contain experiment information are of the form
`userProperty.key like "firebase_exp_%"` or `userProperty.key =
"firebase_exp_01"` where `01` is the experiment ID, and
`userProperty.value.string_value` contains the (zero-based) index of the
experiment variant.

You can use these experiment user properties to extract experiment data.
This gives you the power to slice your experiment results in many different
ways and independently verify the results of A/B Testing.

To get started, complete the following as described in this guide:

1. [Enable BigQuery export for Google Analytics in the Firebase
   console](https://firebase.google.com/docs/ab-testing/bigquery#enable-bigquery-export)
2. [Access A/B Testing data using BigQuery](https://firebase.google.com/docs/ab-testing/bigquery#access-abtesting-data)
3. [Explore example queries](https://firebase.google.com/docs/ab-testing/bigquery#explore-example-queries)

### Enable BigQuery export for Google Analytics in the Firebase console

If you're on the Spark plan, you can use the
[BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) to
access BigQuery at no cost, subject to
[Sandbox limits](https://cloud.google.com/bigquery/docs/sandbox#limitations).
See
[Pricing and the BigQuery sandbox](https://firebase.google.com/docs/projects/bigquery-export?product=analytics#pricing)
for more information.

First, make sure that you're exporting your Analytics data to
BigQuery:

1. Open the [Integrations](https://console.firebase.google.com/project/_/settings/integrations) tab, which you can access using **\>** **Project settings** in the [Firebase console](https://console.firebase.google.com/).
2. If you're already using BigQuery with other Firebase services, click **Manage** . Otherwise, click **Link**.
3. Review **About Linking Firebase to BigQuery** , then click **Next**.
4. In the **Configure integration** section, enable the **Google Analytics** toggle.
5. Select a region and choose export settings.

   > [!NOTE]
   > **Note:** For more information about Google Analytics for Firebase settings, see [Data collection](https://support.google.com/analytics/answer/11593727).

6. Click **Link to BigQuery**.

Depending on how you chose to export data, it may take up to a day for the
tables to become available. For more information about exporting project data to
BigQuery, see
[Export project data to BigQuery](https://firebase.google.com/docs/projects/bigquery-export?product=analytics).

### Access A/B Testing data in BigQuery

Before querying for data for a specific experiment, you'll want to obtain some
or all of the following to use in your query:

- **Experiment ID:** You can obtain this from the URL of the **Experiment overview** page. For example, if your URL looks like `https://console.firebase.google.com/project/my_firebase_project/config/experiment/results/25`, the experiment ID is **25**.
- **Google Analytics property ID** : This is your 9-digit Google Analytics property ID. You can find this within Google Analytics; it also appears in BigQuery when you expand your project name to show the name of your Google Analytics event table (`project_name.analytics_000000000.events`).
- **Experiment date:** To compose a faster and more efficient query, it's good practice to limit your queries to the Google Analytics daily event table partitions that contain your experiment data---tables identified with a `YYYYMMDD` suffix. So, if your experiment ran from February 2, 2024 through May 2, 2024, you'd specify a `_TABLE_SUFFIX between
  '20240202' AND '20240502'`. For an example, see [Select a specific experiment's values](https://firebase.google.com/docs/ab-testing/bigquery#select-a-specific-experiment).
- **Event names:** Typically, these correspond with your [goal metrics](https://firebase.google.com/docs/ab-testing/abtest-with-console#ab-testing-metrics) that you configured in the experiment. For example, `in_app_purchase` events, `ad_impression`, or `user_retention` events.

> [!TIP]
> **Tip:** If you're on the Blaze plan, Firebase can generate a sample query to extract the experiment name, variant, event name, and number of events for the experiment you select. Learn more at [Query experiment data using the Firebase console's auto-generated query](https://firebase.google.com/docs/ab-testing/bigquery#query-experiment-data-generated)

After you gather the information you need to generate your query:

1. Open [BigQuery](https://console.cloud.google.com/bigquery?project=_) in the Google Cloud console.
2. Select your project, then select **Create SQL query**.
3. Add your query. For example queries to run, see [Explore example queries](https://firebase.google.com/docs/ab-testing/bigquery#explore-example-queries).
4. Click **Run**.

> [!TIP]
> **Tip:** While these steps describe using the Google Cloud console, you can also use the CLI or client libraries to query BigQuery. Find out more in the [BigQuery documentation](https://cloud.google.com/bigquery/docs).

#### Query experiment data using the Firebase console's auto-generated query

If you're using the Blaze plan, the **Experiment overview** page provides a
sample query that returns the experiment name, variants, event names, and the
number of events for the experiment you're viewing.

To obtain and run the auto-generated query:

1. From the Firebase console, open [**A/B Testing**](https://console.firebase.google.com/project/_/experiments/list) and select the A/B Testing experiment you want to query to open the **Experiment overview**.
2. From the Options menu, beneath **BigQuery integration** , select **Query experiment data** . This opens your project in BigQuery within the Google Cloud console console and provides a basic query you can use to query your experiment data.

The following example shows a generated query for an experiment with
three variants (including the baseline) named "Winter welcome experiment."
It returns the active experiment name, variant name, unique event, and
event count for each event. Note that the query builder doesn't specify
your project name in the table name, as it opens directly within your project.

      /*
        This query is auto-generated by Firebase A/B Testing for your
        experiment "Winter welcome experiment".
        It demonstrates how you can get event counts for all Analytics
        events logged by each variant of this experiment's population.
      */
      SELECT
        'Winter welcome experiment' AS experimentName,
        CASE userProperty.value.string_value
          WHEN '0' THEN 'Baseline'
          WHEN '1' THEN 'Welcome message (1)'
          WHEN '2' THEN 'Welcome message (2)'
          END AS experimentVariant,
        event_name AS eventName,
        COUNT(*) AS count
      FROM
        `analytics_000000000.events_*`,
        UNNEST(user_properties) AS userProperty
      WHERE
        (_TABLE_SUFFIX BETWEEN '20240202' AND '20240502')
        AND userProperty.key = 'firebase_exp_25'
      GROUP BY
        experimentVariant, eventName

For additional query examples, proceed to
[Explore example queries](https://firebase.google.com/docs/ab-testing/bigquery#explore-example-queries).

### Explore example queries

The following sections provide examples of queries you can use to extract
A/B Testing experiment data from Google Analytics event tables.

#### Extract purchase and experiment standard deviation values from all experiments

You can use experiment results data to independently verify
Firebase A/B Testing results. The following BigQuery SQL statement
extracts experiment
variants, the number of unique users in each variant, and sums total revenue
from `in_app_purchase` and `ecommerce_purchase` events, and standard deviations
for all experiments within the time range specified as the `_TABLE_SUFFIX` begin
and end dates. You can use the data you obtain from this query with a
statistical significance generator for one-tailed t-tests to verify that the
results Firebase provides match your own analysis.

For more information about how A/B Testing calculates inference, see
[Interpret test results](https://firebase.google.com/docs/ab-testing/ab-concepts#interpreting-test-results).

      /*
        This query returns all experiment variants, number of unique users,
        the average USD spent per user, and the standard deviation for all
        experiments within the date range specified for _TABLE_SUFFIX.
      */
      SELECT
        experimentNumber,
        experimentVariant,
        COUNT(*) AS unique_users,
        AVG(usd_value) AS usd_value_per_user,
        STDDEV(usd_value) AS std_dev
      FROM
        (
          SELECT
            userProperty.key AS experimentNumber,
            userProperty.value.string_value AS experimentVariant,
            user_pseudo_id,
            SUM(
              CASE
                WHEN event_name IN ('in_app_purchase', 'ecommerce_purchase')
                  THEN event_value_in_usd
                ELSE 0
                END) AS usd_value
          FROM `PROJECT_NAME.analytics_ANALYTICS_ID.events_*`
          CROSS JOIN UNNEST(user_properties) AS userProperty
          WHERE
            userProperty.key LIKE 'firebase_exp_%'
            AND event_name IN ('in_app_purchase', 'ecommerce_purchase')
            AND (_TABLE_SUFFIX BETWEEN 'YYYYMMDD' AND 'YYYMMDD')
          GROUP BY 1, 2, 3
        )
      GROUP BY 1, 2
      ORDER BY 1, 2;

#### Select a specific experiment's values

The following example query illustrates how to obtain data for a specific
experiment in BigQuery. This sample query returns the experiment name,
variant names (including Baseline), event names, and event counts.

      SELECT
        'EXPERIMENT_NAME' AS experimentName,
        CASE userProperty.value.string_value
          WHEN '0' THEN 'Baseline'
          WHEN '1' THEN 'VARIANT_1_NAME'
          WHEN '2' THEN 'VARIANT_2_NAME'
          END AS experimentVariant,
        event_name AS eventName,
        COUNT(*) AS count
      FROM
        `analytics_ANALYTICS_PROPERTY.events_*`,
        UNNEST(user_properties) AS userProperty
      WHERE
        (_TABLE_SUFFIX BETWEEN 'YYYMMDD' AND 'YYYMMDD')
        AND userProperty.key = 'firebase_exp_EXPERIMENT_NUMBER'
      GROUP BY
        experimentVariant, eventName