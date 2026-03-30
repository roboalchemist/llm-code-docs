# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/google-analytics-v4/google-analytics-v4-options/google-analytics-v4-options-tab.md

# Options tab

Use this tab to define additional step behavior.

![Google Analytics v4 Options tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e3a55e211dfb6ebffdd12b70b27e65ff4747b2ad%2FPDI%20Google%20Analytics%20step%20Options%20tab.png?alt=media)

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Limit**     | Specifies the maximum number of output rows from the step. If the value is 0 the step returns the full dataset.                                                                                                                                                                                                                                                            |
| **Page size** | Specifies the number of analytics rows to buffer in memory between requests to Google Analytics. The range is from 10,000 (default) to 100,000. The step fully supports [pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination), so it will make multiple queries until the limit is reached or the report rows are exhausted. |
