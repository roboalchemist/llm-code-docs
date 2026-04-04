# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/what-happens-when-there-is-no-number-field-on-the-report-analyzer-report-options.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/what-happens-when-there-is-no-number-field-on-the-report-analyzer-report-options.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/what-happens-when-there-is-no-number-field-on-the-report-analyzer-report-options.md

# What happens when there is no number field on the report?

The following rules apply:

* If there is only one text field, such as 'Product Line', but no number field on the report, then all values will be displayed. For example, all product lines will be displayed, even those that did not have data.
* If there is more than one text field, such as 'Product Line' and 'Region', but no number field on the report, then the report will hide some values when showing rows or columns with measure and/or calculated measure data. You should not draw any conclusions from the report in this state. Instead, add a number field.

The rules above are designed to minimize the confusion which may result if an expected value does not appear, but you should also consider usability and performance when displaying every single combination of data elements.
