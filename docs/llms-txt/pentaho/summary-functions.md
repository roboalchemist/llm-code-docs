# Source: https://docs.pentaho.com/pba-report-designer/function-reference/summary-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/function-reference/summary-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/function-reference/summary-functions.md

# Summary functions

The **Summary** category contains mathematical functions that count, add, and divide report data in groups.

| Function Name            | Purpose                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sum**                  | Calculates the sum of the selected numeric column. This produces a global total.                                                                |
| **Count**                | Counts the total number of items contained in a group. If no group is specified, all items in the entire report are counted.                    |
| **Count by Page**        | Counts the total number of items contained in a group on one rendered page. If no group is specified, all items on the entire page are counted. |
| **Group Count**          | Counts the total number of items in the selected groups. If no group is specified, all items in all groups are counted.                         |
| **Minimum**              | Identifies the lowest or smallest value in a group.                                                                                             |
| **Maximum**              | Identifies the highest or largest value in a group.                                                                                             |
| **Sum Quotient**         | Performs simple division on the sum totals from two columns and returns a numeric value.                                                        |
| **Sum Quotient Percent** | Performs simple division on the sum totals from two columns and returns a percentage value.                                                     |
| **Calculation**          | Stores the result of a calculation. This function can be used to convert a group of **Running** functions into a single total Summary function. |
| **Count For Page**       | Counts items on a page according to the specified criteria. This value is reset to zero when a new page is reached.                             |
| **Sum For Page**         | Adds all of the specified items on one page and produces a total. This value is reset to zero when a new page is reached.                       |
