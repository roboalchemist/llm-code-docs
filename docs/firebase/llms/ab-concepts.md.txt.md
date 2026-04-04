# Source: https://firebase.google.com/docs/ab-testing/ab-concepts.md.txt

To help you maximize the relevance and usefulness of your test results, this
page provides detailed information about how Firebase A/B Testing works.

## Sample size

Firebase A/B Testing inference does not require the identification of a
minimum sample size prior to starting an experiment. In general, you should pick
the largest experiment exposure level that you feel comfortable with. Larger
sample sizes increase the chances of finding a statistically significant result,
especially when performance differences between variants are small. You may also
find it useful to consult an online sample size calculator to find the
recommended sample size based on the characteristics of your experiment.

## Edit experiments

You can edit selected parameters of running experiments, including:

- Experiment name
- Description
- Targeting conditions
- Variant values

To edit an experiment:

1. Open the results page for the experiment you want to modify.
2. From the **More** menu, select **Edit running experiment**.
3. Make your changes, then click **Publish**.

Note that changing the app's behavior during a running experiment may impact
results.

## Remote Config variant assignment logic

Users who match all experiment targeting conditions (including the percentage
exposure condition) are assigned to experiment variants according to
[variant weights](https://firebase.google.com/docs/ab-testing/ab-concepts#variant-weights) and a hash of the experiment ID and the
user's Firebase installation ID.

[Google Analytics Audiences](https://support.google.com/analytics/answer/9267572)
are subject to latency and are not immediately available when a user initially
meets the audience criteria:

- When you create a new audience, it may take 24-48 hours to accumulate new users.
- New users are typically enrolled into qualifying audiences 24-48 hours after they become eligible.

For time-sensitive targeting, consider the use of Google Analytics user
properties or built-in targeting options such as country or region, language,
and app version.

Once a user has entered an experiment, they are persistently assigned to their
experiment variant and receive parameter values from the experiment as long as
the experiment remains active, even if their user properties change and they no
longer meet the experiment targeting criteria.

## Activation events

Experiment activation events limit experiment measurement to app users who
trigger the activation event. The experiment activation event does not have any
impact on the experiment parameters that are fetched by the app; all users who
meet the experiment targeting criteria will receive experiment parameters.
Consequently, it is important to choose an activation event that occurs after
the experiment parameters have been fetched and activated, but before the
experiment parameters have been used to modify the app's behavior.

## Variant weights

During experiment creation, it is possible to change the default variant weights
to place a larger percentage of experiment users into a variant.

## Interpret test results

[Video](https://www.youtube.com/watch?v=a0aVOlw5210)

Firebase A/B Testing uses *frequentist inference* to help you understand the
likelihood that your experiment results could have occurred solely due to random
chance. This likelihood is represented by a *probability value* , or
*p-value* . The p-value is the probability that a difference in performance this
large, or larger, between two variants could have occurred due to random chance
if there is actually no effect, measured by a
value between 0 and 1. A/B Testing uses a significance level of 0.05 so that:

- A p-value less than 0.05 indicates that if the true difference were zero, there is a less than 5% chance that an observed difference this extreme could occur randomly. Because 0.05 is the threshold, any p-value less than 0.05 indicates a statistically significant difference between variants.
- A p-value greater than 0.05 indicates that the difference between variants is not statistically significant.

Experiment data is refreshed once a day, and the last update time
appears at the top of the experiment results page.

The experiment results graph displays the cumulative average values of the
selected metric. For example, if you're tracking Ad revenue per user as a
metric, it displays observed revenue per user and if you're tracking Crash-free
users, it tracks the percentage of users who have not encountered a crash. This
data is cumulative from the beginning of the experiment.

Results are split into **Observed data** and **Inference data**.
Observed data is calculated directly from Google Analytics data, and inference
data provides p-values and confidence intervals to help you evaluate the
statistical significance of the observed data.

For each metric, the following statistics are displayed:

### Observed data

- Total value for the tracked metric (number of retained users, number of users who crashed, total revenue)
- Metric-specific rate (retention rate, conversion rate, revenue per user)
- Percent difference (lift) between the variant and baseline

### Inference data

- **95% CI (Difference in means)** displays an interval
  that contains the "true" value of the tracked metric with 95% confidence. For
  example, if your experiment results in a 95% CI for estimated total revenue
  between $5 and $10, there is a 95% chance that the true difference in means is
  between $5 and $10. If the CI range includes 0, a statistically significant
  difference between the variant and baseline was not detected.

  Confidence interval values appear in the format that matches the tracked
  metric. For example, Time (in `HH:MM:SS`) for user retention, USD for ad
  revenue per user, and percentage for conversion rate.
- **P-value** , which represents the probability of
  observing data as extreme as the results obtained in the experiment, given
  that there is no true difference between the variant and baseline. The lower
  the p-value, the higher the confidence that the observed performance remains
  true if we repeat the experiment. A value of 0.05 or lower indicates a
  significant difference and a low
  likelihood that results were due to chance. P-values are based on a
  *one-tailed test* , where the Variant value is greater than the Baseline value.
  Firebase uses an *unequal variance t-test* for continuous variables
  (numeric values, like revenue) and a *z-test of proportions* for conversion
  data (binary values, like user retention, crash-free users,
  users who trigger a Google Analytics event).

The experiment results provide important insights for each experiment variant,
including:

- How much higher or lower each experiment metric is compared to the baseline, as directly measured (that is, the actual observed data)
- The likelihood that the observed difference between the variant and the baseline could have occurred due to random chance (p-value)
- A range that is likely to contain the "true" performance difference between the variant and the baseline for each experiment metric---a way to understand the "best case" and "worst case" performance scenarios

### Interpret results for experiments powered by Google Optimize

Firebase A/B Testing results for experiments started before October 23, 2023
were powered by Google Optimize. Google Optimize used Bayesian inference to
generate insightful statistics from your experiment data.

Results are split into "observed data" and "modeled data." Observed data was
calculated directly from analytics data, and modeled data was derived from the
application of our Bayesian model to the observed data.

For each metric, the following statistics are displayed:

#### Observed Data

- Total value (sum of metric for all users in the variant)
- Average value (average value of metric for users in the variant)
- % difference from baseline

#### Modeled Data

- Probability to beat baseline: how likely that the metric is higher for this variant compared to the baseline
- Percent difference from baseline: based on the median model estimates of the metric for the variant and the baseline
- Metric ranges: the ranges where the value of the metric is most likely to be found, with 50% and 95% certainty

Overall, the experiment results give us three important insights for each
variant in the experiment:

1. How much higher or lower each experiment metric is compared to the baseline, as directly measured (i.e., the actual observed data)
2. How *likely* it is that each experiment metric is higher than the baseline / best overall, based on Bayesian inference (probability to be better / best respectively)
3. The plausible ranges for each experiment metric based on Bayesian inference--"best case" and "worst case" scenarios (credible intervals)

## Leader determination

For experiments using
[Frequentist inference](https://firebase.google.com/docs/ab-testing/ab-concepts#interpreting-test-results),
Firebase declares that a variant is leading if there is a statistically
significant performance difference between the variant and the baseline on the
goal metric. If multiple variants meet this criteria, the variant with the
lowest [p-value](https://firebase.google.com/docs/ab-testing/ab-concepts#p-value) is chosen.

For experiments that used
[Google Optimize](https://firebase.google.com/docs/ab-testing/ab-concepts#optimize-results),
Firebase declared that a variant is a "clear leader" if it had greater than 95%
chance of being better than the baseline variant on the primary metric. If
multiple variants met the "clear leader" criteria, only the best performing
variant overall was labeled as the "clear leader."

Since leader determination is based on the primary goal only, you should
consider all relevant factors and review the results of secondary metrics before
deciding whether or not to
roll out
a leading variant. You may want
to consider the expected upside of making the change, the downside risk (such as
the lower end of the confidence interval for improvement), and the impact to
metrics other than the primary goal.

For example, if your primary metric is Crash-free users, and Variant A is a
clear leader over the baseline, but Variant A user retention metrics trail
baseline user retention, you may want to investigate further before rolling out
Variant A more widely.

You can
roll out
any variant, not just a leading variant, based on
your overall evaluation of performance across both primary and secondary
metrics.

## Experiment duration

Firebase recommends that an experiment continue to run until the following
conditions are met:

1. The experiment has accrued enough data to provide a useful result. Experiments and result data are updated once daily. You may want to consult an online sample size calculator to evaluate the recommended sample size of your experiment.
2. The experiment has run long enough to ensure a representative sample of your users and measure longer-term performance. Two weeks is the recommended minimum runtime for a typical Remote Config experiment.

Experiment data is processed for a maximum of 90 days after
experiment start. After 90 days, the experiment is automatically stopped.
Experiment results are no longer updated in the Firebase console and the
experiment stops sending experiment-specific parameter values. At this
point, clients begin fetching parameter values based on the conditions set
in the Remote Config template. Historical experiment data is retained until
you delete the experiment.

## BigQuery schema

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
   console](https://firebase.google.com/docs/ab-testing/ab-concepts#enable-bigquery-export)
2. [Access A/B Testing data using BigQuery](https://firebase.google.com/docs/ab-testing/ab-concepts#access-abtesting-data)
3. [Explore example queries](https://firebase.google.com/docs/ab-testing/ab-concepts#explore-example-queries)

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
  '20240202' AND '20240502'`. For an example, see [Select a specific experiment's values](https://firebase.google.com/docs/ab-testing/ab-concepts#select-a-specific-experiment).
- **Event names:** Typically, these correspond with your [goal metrics](https://firebase.google.com/docs/ab-testing/abtest-with-console#ab-testing-metrics) that you configured in the experiment. For example, `in_app_purchase` events, `ad_impression`, or `user_retention` events.

> [!TIP]
> **Tip:** If you're on the Blaze plan, Firebase can generate a sample query to extract the experiment name, variant, event name, and number of events for the experiment you select. Learn more at [Query experiment data using the Firebase console's auto-generated query](https://firebase.google.com/docs/ab-testing/ab-concepts#query-experiment-data-generated)

After you gather the information you need to generate your query:

1. Open [BigQuery](https://console.cloud.google.com/bigquery?project=_) in the Google Cloud console.
2. Select your project, then select **Create SQL query**.
3. Add your query. For example queries to run, see [Explore example queries](https://firebase.google.com/docs/ab-testing/ab-concepts#explore-example-queries).
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
[Explore example queries](https://firebase.google.com/docs/ab-testing/ab-concepts#explore-example-queries).

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

## Limits

A/B Testing is limited to 300 total experiments, 24 running experiments,
and 24 draft experiments. These limits are shared with Remote Config rollouts.
For example, if you have two running rollouts, and three running experiments,
you can have up to 19 additional rollouts or experiments.

- If you reach the 300 total experiment limit or the 24 draft experiment limit,
  you must delete an existing experiment before creating a new one.

- If you reach the 24 running experiment and rollout limit, you must stop a
  running experiment or rollout before starting a new one.

An experiment can have a maximum of 8 variants (including the baseline) and up
to 25 parameters for each variant. An experiment can have a size up to around
200 KiB. This includes variant names, variant parameters, and other
configuration metadata.