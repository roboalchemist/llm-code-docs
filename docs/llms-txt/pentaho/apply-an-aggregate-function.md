# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/advanced-topics/create-advanced-filters-in-interactive-reports/apply-an-aggregate-function.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-interactive-reports-cp/advanced-topics/create-advanced-filters-in-interactive-reports/apply-an-aggregate-function.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/advanced-topics/create-advanced-filters-in-interactive-reports/apply-an-aggregate-function.md

# Apply an aggregate function

You can assign an aggregate function to columns that contain numeric and non-numeric values in your report. Aggregate functions return a single value calculated from the values in a column.

1. Click the Down Arrow next to a report column that contains numeric values.
2. Select **Aggregation** from the menu, then choose the aggregation type. These types are described in the following table:

   | Function Name  | Description                                                                                      |
   | -------------- | ------------------------------------------------------------------------------------------------ |
   | None           | No aggregate function assigned                                                                   |
   | Average        | Calculates the average value in a given column                                                   |
   | Count          | Counts the items in a column; does not require a numeric value                                   |
   | Count Distinct | Counts the distinct occurrences of a certain value in a column; does not require a numeric value |
   | Maximum        | Identifies the highest or largest value in a column                                              |
   | Minimum        | Identifies the lowest or smallest value in a column                                              |
   | Sum            | Calculates a running total sum of the specified column                                           |
3. Save the report.
