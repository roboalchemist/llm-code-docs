# Source: https://docs.fiddler.ai/observability/platform/statistics.md

# Statistics

### Overview

Fiddler supports some simple statistic metrics which can be used to monitor basic aggregations over columns. These can be particularly useful when you have a custom metadata field which you would like to monitor over time in addition to Fiddler's other out-of-the-box metrics.

### What is being tracked?

Specifically, we support:

* **Average**: Takes the arithmetic mean of a numeric column
* **Sum**: Calculates the sum of a numeric column
* **Frequency**: Shows the count of occurrences for each value in a categorical or boolean column

### Monitoring Statistic Metrics

#### Charting Statistic Metrics

These metrics can be accessed in Charts and Alerts by selecting the Statistic Metric Type.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-aaf94292a5534c2cf3e775965a2513accbf8e35c%2F2b19cf0-Screen_Shot_2023-12-19_at_2.31.43_PM.png?alt=media)

#### Alerting on Statistic Metrics

Alert rules can be established based on statistics too. Like an alert rule, these can be setup using the Fiddler UI, the Fiddler python client or using Fiddler's RESTful API.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-aaf94292a5534c2cf3e775965a2513accbf8e35c%2F2b19cf0-Screen_Shot_2023-12-19_at_2.31.43_PM.png?alt=media)
