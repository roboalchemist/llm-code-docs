# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/google-analytics-v4/google-analytics-v4-options/google-analytics-v4-filter-tab.md

# Filters tab

Use this tab to specify [filters](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/FilterExpression) on dimensions or metrics. Filters can be simple or complex nested expressions. The filters are added to requests against Google Analytics to narrow down the result sets and reduce quota usage. All the options in the buttons are also available as context menu options of the filter tree.

![Google Analytics v4 Filter tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-bceefa1a07165b77c87e2092b5584a9e276daf36%2FPDI%20Google%20Analytics%20step%20Filters%20tab.png?alt=media)

| Field          | Description                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| Add child      | Click to add an AND, OR, NOT, or FILTER expression to the currently selected item of the filter expression tree. |
| Insert parent  | Click to add a parent group (AND, OR, NOT) filter to the currently selected item of the filter expression tree.  |
| Change type to | Select a filter expression and click to change the filter expression's type.                                     |
| Delete         | Click to remove the selected item and its children.                                                              |
