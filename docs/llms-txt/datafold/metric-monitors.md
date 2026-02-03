# Source: https://docs.datafold.com/data-monitoring/monitors/metric-monitors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metric Monitors

> Metric monitors detect anomalies in your data using ML-based algorithms or manual thresholds, supporting standard and custom metrics for tables or columns.

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to enable this feature for your organization.
</Note>

Metric monitors allow you to perform anomaly detection—either automatically using our ML-based algorithm or by setting manual thresholds—on the following metric types:

1. Standard metrics (e.g. row count, freshness, and cardinality)
2. Custom metrics (e.g. sales volume per region)

## Create a Metric monitor

There are two ways to create a Metric Monitor:

1. Open the **Monitors** page, select **Create new monitor**, and then choose **Metric**.
2. Clone an existing Metric monitor by clicking **Actions** and then **Clone**. This will pre-fill the form with the existing monitor configuration.

## Set up your monitor

Select your data connection, then choose the type of metric you'd like: **Table**, **Column**, or **Custom**.

If you select table or column, you have the option to add a SQL filter to refine your dataset. For example, you could implement a 7-day rolling time window with the following: `timestamp >= dateadd(day, -7, current_timestamp)`. Please ensure the SQL is compatible with your selected data connection.

## Metric types

### Table metrics

| Metric    | Definition                        | Additional Notes                                                                                               |
| --------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Freshness | Time since table was last updated | Measured in minutes. Derived from INFORMATION\_SCHEMA. Only supported for Snowflake, BigQuery, and Databricks. |
| Row Count | Total number of rows              |                                                                                                                |

### Column metrics

| Metric             | Definition                     | Supported Column Types | Additional Notes           |
| ------------------ | ------------------------------ | ---------------------- | -------------------------- |
| Cardinality        | Number of distinct values      | All types              |                            |
| Uniqueness         | Proportion of distinct values  | All types              | Proportion between 0 and 1 |
| Minimum            | Lowest numeric value           | Numeric columns        |                            |
| Maximum            | Highest numeric value          | Numeric columns        |                            |
| Average            | Mean value                     | Numeric columns        |                            |
| Median             | Median value (50th percentile) | Numeric columns        |                            |
| Sum                | Sum of all values              | Numeric columns        |                            |
| Standard Deviation | Measure of data spread         | Numeric columns        |                            |
| Fill Rate          | Proportion of non-null values  | All types              | Proportion between 0 and 1 |

### Custom metrics

Our custom metric framework is extremely flexible and supports several approaches to defining metrics. Depending on the approach you choose, your query should return some combination of the following columns:

* **Metric value (required)**: a numeric column containing your *metric values*
* **Timestamp (optional)**: a date/time column containing *timestamps* corresponding to your metric values
* **Group (optional)**: a string column containing *groups/dimensions* for your metric

<Note>
  **INFO**

  The names and order of your columns don't matter. Datafold will automatically infer their meaning based on data type.
</Note>

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=538ed4183ea523c46e2a3fa093697e1f" data-og-width="4768" width="4768" data-og-height="3200" height="3200" data-path="images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=fc94579a5279f3ba6036ff574f9eb30b 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=add70a4caf25b88e6de28371f8533ae3 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e34f719fcf3fdaecf30f0aa11845ea80 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=95e0a279fc8cea4d3940f55e9df6fa98 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cee550c72ac472133a84c5d3728577e7 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cddada2b6514065818b7d8117b5bcaa7 2500w" />
</Frame>

The following questions will help you decide which approach is best for you:

1. **Do you want to group your metric by the value of a column in your query?** For example, if your metric is *sales volume per day*, rather than looking at a single metric that encompasses all sales globally, it might be more informative to group by country. In this case, Datafold will automatically compute sales volume separately for each country to assist with root cause analysis when there’s an unexpected change.
2. **Will your query return a single metric value (per group, if relevant) on every monitor run, or an entire time series?** We generally recommend starting with the simpler approach of providing a single metric value (per group) per monitor run. However, if you’ve already defined a time series elsewhere (e.g. in your BI tool) and simply want to copy/paste that query into Datafold, then you may prefer the latter approach.

<Note>
  **INFO**

  Datafold will only log a single data point per timestamp per group, which means you should only send data for a particular time period once that period is complete.
</Note>

1. **If your metric returns a single value per monitor run, will you provide your own timestamps or use the timestamps of monitor runs?** If your query returns a single value per run, we generally recommend letting Datafold provide timestamps based on monitor runs unless you have a compelling reason to provide your own. For example, if your metric always lags by one day, you could explicitly associate yesterday's date with each observation.

As you're writing your query, Datafold will let you know if the result set doesn't match one of the accepted patterns. If you have questions, please contact us and we'll be happy to help.

## Configure anomaly detection

Enable anomaly detection to get the most out of metric monitors. You have several options:

* **Automatic**: our automated anomaly detection uses machine learning to flag metric values that are out of the ordinary. Dial the sensitivity up or down depending on how many alerts you'd like to receive.
* **Manual**: specific thresholds beyond which you'd like the monitor to trigger an alert. **Fixed Values** are specific minimum and/or maximum values, while **Percent Change** measure the magnitude of change from one observation to the next.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dde08288db7476b9dde7ea5bdcf74fb7" data-og-width="1184" width="1184" data-og-height="532" height="532" data-path="images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d124cd790d7ccb2a3b4ccb9d8aa37362 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3252044af65d97323bed87564d17e65b 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3e9bdbb3e4ccc1babacddaf8ad5e6829 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e64d316d1dd09d938d20d609f0cff7f 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c9a611a0f41235b45c912276bdbaaa68 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f2c1502ca43decc8de2b523fcdd565da 2500w" />
</Frame>

## Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

## Add notifications

Send notifications via Slack or email when your monitor exceeds a threshold (automatic or manual):

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## Need help?

If you have any questions about how to use Metric monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
