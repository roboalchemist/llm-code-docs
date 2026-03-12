# Source: https://docs.pentaho.com/analyzer-external-javascript-api/cv-apis-pentaho-analyzer-external-javascript-api-cp/report-apis-pentaho-analyzer-external-javascript-api/get-and-set-report-options-apis-pentaho-analyzer-external-javascript-api.md

# Get and Set Report Options APIs

There are two calls related to Report Options: `getReportOption` and `setReportOption`.

* The `setReportOption` is used to designate a value for a specific report option.
* The `getReportOption` allows you to view the current value assigned to that option.

```javascript
cv.api.report.setReportOption(name:string, value:string);
cv.api.report.getReportOption(name:string);

```

To ensure your changes are reflected in the report, the `refreshReport` method should be called:

```javascript
cv.api.operation.refreshReport();

```

Acceptable values for setting a report option are 'true' and 'false'. The `getReportOption` returns one of these same values.

The following lists report options.

## showRowGrandTotal

This option allows you to set the visibility of row grand totals for the pivot table.

```javascript
cv.api.report.setReportOption("showRowGrandTotal", "true");
cv.api.report.getReportOption("showRowGrandTotal"); // Returns "true"

```

## showColumnGrandTotal

This option allows you to set the visibility of column grand totals for the pivot table.

```javascript
cv.api.report.setReportOption("showColumnGrandTotal", "true");
cv.api.report.getReportOption("showColumnGrandTotal"); // Returns "true"

```

## useNonVisualTotals

This option allows you to set the visibility of non-visual totals for the pivot table.

```javascript
cv.api.report.setReportOption("useNonVisualTotals", "true");
cv.api.report.getReportOption("useNonVisualTotals"); // Returns "true"

```

## showEmptyCells (Deprecated)

This option has been deprecated. Please use `showEmptyEnum`.

This option allows you to set the visibility of cells with no data.

```javascript
cv.api.report.setReportOption("showEmptyCells", "true");
cv.api.report.getReportOption("showEmptyCells"); // Returns "true"

```

## showEmptyEnum

This option allows the user to set the options available for the parameter via a drop-down menu. The following values are allowed:

* SHOW\_MEASURE - Includes measure data. Default value.
* SHOW\_CALCULATED\_MEASURE - Includes measure and calculated measure data.
* SHOW\_EMPTY - Includes all measure and calculated measure data, including null measure data.

```javascript
cv.api.report.setReportOption("showEmptyEnum", "SHOW_MEASURE");
cv.api.report.getReportOption("showEmptyEnum"); // Returns "SHOW_MEASURE"

```

## showDrillLinks

This option allows you to set the visibility of drill-through links on cells for pivot table.

```javascript
cv.api.report.setReportOption("showDrillLinks", "true");
cv.api.report.getReportOption("showDrillLinks"); // Returns "true"

```

## autoRefresh

This option allows you to set the ability to automatically refresh the report when a user makes a report definition change.

```javascript
cv.api.report.setReportOption("autoRefresh", "true");
cv.api.report.getReportOption("autoRefresh"); // Returns "true"

```

## freezeColumns

This option allows you to set the freezing of the column headers in the pivot table when the user scrolls.

```javascript
cv.api.report.setReportOption("freezeColumns", "true");
cv.api.report.getReportOption("freezeColumns"); // Returns "true"

```

## freezeRows

This option allows you to set the freezing of the row headers in the pivot table when the user scrolls.

```javascript
cv.api.report.setReportOption("freezeRows", "true");
cv.api.report.getReportOption("freezeRows"); // Returns "true"

```

## URL Parameters

All of the above report options can also be set through the URL as URL parameters.

```javascript
http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ALeading%20Product%20Lines%20(pivot%20table).xanalyzer/editor?ts=1421660200377&showRowGrandTotal=true&showColumnGrandTotal=true&useNonVisualTotals=true&showEmptyCells=true&showDrillLinks=true&autoRefresh=true&freezeColumns=true&freezeRows=true
```
