# Source: https://docs.fiddler.ai/observability/analytics/data-table-in-rca.md

# Events Table in RCA

Allow visualizing events corresponding to a certain bin in a monitoring chart. Note that this view is to provide example rows used for the computation. The maximum number of rows that can viewed is 1000.

### Analyzing a Sample of Events

* Navigate to the `Charts` tab in your Fiddler AI instance
* Click on the `Add Chart` button on the top right
* In the modal, select a project
* Select **Monitoring**
* Create a Monitoring chart and click on a time range
* This will display the RCA (Root Cause Analysis) tab
* In RCA, select the `Events Table` tab

### Support

This visualization is supported for any model and data type.

### Represented data

The displayed events are production events coming from the selected model and bin, and segment if it was selected in the monitoring chart.

![Monitoring Chart Configuration](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-e3493a530794166f349a0bd0fd01a1a34a4b0e64%2Fmonitoring-chart-selection.png?alt=media) ![Event Table Example](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-e3493a530794166f349a0bd0fd01a1a34a4b0e64%2Fmonitoring-chart-selection.png?alt=media)

### Available Controls

* **Column selection**: On the top right side of the table, select the columns to be displayed. By default all non-vector columns are displayed.

![Event Table Column Selection](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-71e8976188e8c249c12de270c4487a6c7dc334c6%2Fdata-table-column-selection.png?alt=media)

* **Vector columns**: By default the vector columns are not fetched for latency reasons. Toggle on if vectors need to be fetched.

![Event Table Vectors displayed](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-62b01e78901832a5d6d907a903753e96436203e8%2Fdata-table-vectors.png?alt=media)

* **Download**: Download the sample events to `CSV` or `PARQUET` format.

![Event Table Vectors Download](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-8a4d7f49135e0a07fee24a233e91dc017202af45%2Fdata-table-download.png?alt=media)
