# Source: https://docs.asapp.com/reporting.md

# Source: https://docs.asapp.com/generativeagent/reporting.md

# Source: https://docs.asapp.com/changelog/reporting.md

# Source: https://docs.asapp.com/reporting.md

# Reporting and Insights

ASAPP reports data back via several channels, each with different use cases:

<CardGroup>
  <Card title="File Exporter" href="/reporting/file-exporter">Retrieve data and reports via a secure API for programmatic access to ASAPP data.</Card>
  <Card title="S3 Reports" href="/reporting/retrieve-messaging-data">Download data and reports via S3.</Card>
  <Card title="Real Time Event API" href="/reporting/real-time-event-api">Access real-time data from ASAPP Messaging.</Card>
  <Card title="Send data to ASAPP" href="/reporting/send-sftp">Send data to ASAPP via S3 or SFTP.</Card>
  <Card title="Metadata Ingestion" href="/reporting/metadata-ingestion">Send conversation, agent, and customer metadata.</Card>
</CardGroup>

## Batch vs Realtime

One high-level differentiating feature of these channels is how the underlying data is processed for reporting:

* **Real-time**: Processed data flows to the reporting channel as it happens.
* **Batch**: Processed data aggregates into time-based buckets, delivered with some delay to the reporting channel.

For reference:

* Reports visible in ASAPP's Desk/Admin are considered *real-time reports*.
* RTCI reports are *real-time reports*.
* ASAPP's S3 reports are *batch reports,* delivered with a predictable time delay.
* Historical Reports are *batch reports*.

Often, metrics similar in both name and in underlying definition are delivered both via batch and via real-time channels.

This can be confusing: a metric in viewed in a real-time context (say, via ASAPP's Desk/Admin) might well differ in value from a similar metric viewed in a time-delayed batch context (say, via a report delivered by S3).

***In fact, customers should not expect that values for similar metrics will line up across real-time and batch reporting channels.***

The short explanation for such differences is that **real-time and batch processed metrics are necessarily calculated using different underlying data sets** (with the real-time set current up-to-the-minute, and the batch set delayed as a function of the time bucketing aggregation).

It is expected that different underlying data will yield different reported values for your metrics between delivery channels.

The balance of this document provides a few concrete examples to further explain the variance you will typically see between real-time and batch reported values for similar metrics.

### Batch vs Real-time Metric Discrepancies

Real-time metrics are calculated with a continual process, where computations are evaluated repeatedly with the most current data available.

With multiple active and potentially geographically dispersed instances of an application communicating asynchronously across a global message bus, at times the data used to calculate real-time metrics can be intermediate or incomplete.

On the other hand, metrics computed using batch processing are computed with all available, terminal data for each reported interaction, and so can provide a more accurate metric at the expense of a time delay vs real-time reporting.

ASAPP S3 reports, for example, are normally computed over hours or days, and can therefore incorporate the most complete set of data points required to calculate a metric.

As a simplified example, let's consider a metric that shows a daily average for customer satisfaction ratings. Let's assume:

* the day starts at 8:00AM
* batch processing works against hourly aggregate buckets
* batch calculations run at 5 minutes past the hour
* it is a *very slow* day :)

Over the course of our pretend day, the following interactions are handled by the system:

| TIME     | Rating | Real-time avg for day | batch avg for day |
| :------- | :----- | :-------------------- | :---------------- |
| 8:00 AM  | 4      | 4                     | N/A               |
| 8:05 AM  | 4      | 4                     | N/A               |
| 8:10 AM  | 4      | 4                     | N/A               |
| 12:00 PM | 1      | 3.25                  | 4                 |
| 12:05 PM | 1      | 2.8                   | 4                 |
| 1:10 PM  | 4      | 3                     | 2.8               |

At 8:00 AM, batch processing will not have incorporated the rating that was provided at 8:00AM. So the average rating can't be computed for a batch report. Since real-time reporting has access to up-to-the-minute data, real-time reporting shows a value of 4 for the daily average customer satisfaction rating.

At 12:00PM, the real-time metric shows an average satisfaction over 4 transactions as 3.25. The batch system shows the average satisfaction rating as 4 over 3 transactions, since the 12:00 transaction has not yet been incorporated into the batch processing calculation. Given our example scenario, the interactions at 12:00 and 12:05 would not be incorporated into the batch reported metric until 1:05PM.

In this simplified example, the batch processed metric would align with the real-time metric around 2:05 PM, once both the batch metric and the real-time metric are calculated against the same underlying data set.

The next example shows how values provided by real-time vs batch processing might show inconsistent values for "rep assigned time".

```json  theme={null}
8:00AM: NEW ISSUE
8:01AM: ENQUEUED
8:02AM: REP ASSIGNED: rep0
8:03AM: REP UNASSIGNED
8:04AM: REENQUEUED
8:05AM: REP ASSIGNED: rep0
8:06AM: ...
```

With real time reporting, the value for rep\_assigned\_time might show either 8:02AM or 8:05AM, depending on when the data is read and the real-time metric is viewed.

Batch processed data, however, will have the complete historical data, and so will consistently report 8:02AM for the rep\_assigned\_time.

Batch processed data and real-time processed data are almost always looking at different underlying data sets. Batch data is complete but time-delayed and real-time data is up-to-the-minute but not necessarily complete.

As long as the data sets underlying real-time vs. batch reporting differ, customers should expect that the metrics calculated from those different data sets will differ more often than not.
