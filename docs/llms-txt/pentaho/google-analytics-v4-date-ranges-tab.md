# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/google-analytics-v4/google-analytics-v4-options/google-analytics-v4-date-ranges-tab.md

# Date ranges tab

The Google Analytics Data API allows up to [four date ranges](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/DateRange) to be specified per report request. A minimum of one date range is always required. If more than one date range is used, a special dimension called `DateRange` must be added as an output field in order to separate stacked output rows.

![Google Analytics v4 Date ranges tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-43c5f8dbd9867c952921516bdf357957875ca0ed%2FPDI%20Google%20Analytics%20step%20Date%20ranges%20tab.png?alt=media)

| Field          | Description                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Range name** | Specifies the optional name of the date range. This name displays in the **DateRange** dimension of an output report.                          |
| **Start spec** | Specifies the starting day of the date range. Value formats can be provided in `YYYY-MM-DD`, `NdaysAgo`, or values of `today` and `yesterday`. |
| **End spec**   | Specifies the ending day of the date range. Value formats can be provided in `YYYY-MM-DD`, `NdaysAgo`, or values of `today` and `yesterday`.   |
