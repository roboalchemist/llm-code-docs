# Source: https://docs.axonius.com/docs/comp-query-previous-date.md

# Comparing Today's Query Results to a Previous Date

This feature is available for the following chart types:

* [Field Summary](/docs/field-summary-chart)
* [Query Comparison](/docs/query-comparison-chart)
* [Field Segmentation](/docs/field-segmentation-chart)
* [Adapter Segmentation](/docs/adapter-segmentation-chart)

## Comparing Results

The **Compare results** feature allows you to compare today’s query results to results of a previous date. This gives context to the data and makes changes in the results more apparent. Changes are indicated by color as set in **Change indicator color**.

Toggle on **Compare results to a previous date** to compare today's results to a date relative to today or to a fixed date.

<Image alt="CompareResultsSettings.png" width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CompareResultsSettings.png" />

Color coding is applied to the asset count change indication to the right of the chart.

<Image alt="CompareResultsChart.png" width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CompareResultsChart.png" />

**To compare today's results to results of a previous date:**

1. Choose one of the following:
   * **Relative date before** - Enter a value in the text box and then select the time unit: days, weeks, months or years. Today’s results are compared to results of a relative date for which there is data.
   * **Specific date** - Use the date picker to select a specific date. Today’s results are compared to results of a specific date for which there is data.

<Callout icon="📘" theme="info">
  Note

  Only dates for which there is data can be selected.
</Callout>

2. In the **Change color indicator** section, select colors for the following:

   * **Increase** - There are *more* results today than on the comparison date.
   * **Same** - There are the *same* number of results today as on the comparison date.
   * **Decrease** - There are *less* results today than on the comparison date.