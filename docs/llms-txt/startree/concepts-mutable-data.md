# Source: https://docs.startree.ai/thirdeye/concepts-data-alerts-notifications/concepts-mutable-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Mutable Data

In most event systems, data is regarded as immutable, meaning that once it's been written, it can't
be altered.
This is not always true with Pinot. Data can be mutated in 2 ways:

* through [streaming upserts](https://docs.pinot.apache.org/basics/data-import/upsert)
* through [automatic segement refresh](/corecapabilities/manage-data/segment-refresh-task)

ThirdEye is compatible with these features.

## Principle - anomaly consolidation

In ThirdEye, a detection job can be run multiple times on the same timeframe.
New anomalies and existing anomalies are consolidated based on the following rules:

* if the data has not changed, no action is taken.
* if the data has changed and new anomalies are detected, they are created and notified.
* if the data has changed and some anomalies no longer exist, they are marked as outdated.
  They won't be visible in the UI by default, but their investigations and feedbacks are preserved.
* if the data has changed and an anomaly is detected on a timeframe where an anomaly already exists:
  * if the change is *significant enough* , the existing anomaly is marked as outdated, the new
    anomaly is
    created and notified.
  * if the change is not *significant enough*, the existing anomaly is updated with the latest value. It is not re-notified.
    The new anomaly is dropped.

To determine what constitutes a *significant enough* change, you can adjust
the `reNotifyPercentageThreshold`and `reNotifyAbsoluteThreshold` parameters. For more information, see
the [AnomalyMerger documentation](/thirdeye/operators/post-processor/anomaly_merger).

By default, **ThirdEye only runs detection jobs on data that it hasn't analyzed before. It does not
consider potential mutations in previously analyzed data.**
For example, if ThirdEye analyzed data up until Thursday, at the next scheduled detection job, it
will analyze data from Friday.

However, there are two methods to make ThirdEye re-process data that has already been analyzed:

* Use the `/api/alerts/{id}/run` endpoint. This can be done programmatically or via
  the [Swagger interface](/thirdeye/how-tos/use-the-api). The detection timeframe can be configured.
* Use the `mutabilityPeriod` [alert configuration](/thirdeye/alert-configuration#mutabilityperiod) parameter.
  At each scheduled
  detection job, ThirdEye will re-process the data that falls in the mutable period.
  For instance, if the mutable period is set to 3 days, and ThirdEye processed data up to Thursday, then at the
  next detection job ThirdEye will run from Tuesday (Friday - 3 days).
  The following day, ThirdEye will process data from Wednesday (Saturday - 3 days), and so on.

## Use cases

### Segment refresh

Data is loaded in daily batch in Pinot. The batch system is complex and has many sources of data.
Sometimes, a source of data is broken, resulting in missing data downstream in Pinot.
When this happens:

* ThirdEye detects the anomalies.
  <img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/_data_mutability_missing_data.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=49338de9fb81a60c1ac9a0a301696fff" alt="missing data" width="1774" height="542" data-path="img/thirdeye/_data_mutability_missing_data.png" />
* A data engineer will fix the issue and reload the data. Pinot segments are refreshed, the data is
  fixed. ThirdEye anomalies are now outdated:
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_data_mutability_te_outdated.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=16b4382a31a48638db0989c9bcc6dcea" alt="_data_mutability_te_outdated.png" width="1736" height="541" data-path="img/thirdeye/_data_mutability_te_outdated.png" />
* The data engineer uses the `/api/alerts/{id}/run` endpoint to re-run the detection. ThirdEye is
  up-to-date.
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_data_mutability_te_up_to_date.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=7375fe0472636b479d08db16447a247a" alt="thirdeye up to date" width="1739" height="547" data-path="img/thirdeye/_data_mutability_te_up_to_date.png" />

  In this case, there is still an anomaly! ThirdEye sends a notification for this new anomaly.

### Streaming upsert use case

Data is ingested in streaming. Because upserts is enabled, some rows can be mutated multiple times, up to 2 days in the past. The data is monitored by ThirdEye at a 15-minute granularity. (4 points per hour).\
Sometimes, rows in Pinot are mutated after the detection job of ThirdEye. This means some anomalies can get slightly outdated. To avoid this, a user can set the mutabilityPeriod to 2 days: `mutabilityPeriod=P2D`. This way, at each detection job, the detection will be re-run on the last two days of data, and ThirdEye results will stay up-to-date with the mutated data.

Built with [Mintlify](https://mintlify.com).
