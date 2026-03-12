# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/set-blank-measure-display.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/set-blank-measure-display.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/set-blank-measure-display.md

# Set blank measure display

You can control what to show when a cell contains a blank value in your Analyzer report. Analyzer reports are designed to break down number fields, such as 'Sales', by text fields such as 'Product Name'. If a product did not sell, it will appear either as zero dollars or as a blank or a dash ("-"). In some reporting situations, the absence of a value could mean the same as a zero, but in other cases, zero might have a different meaning. The report calculations in the background behave differently depending on whether a value is 'blank' or a 'zero'. For example, when the report calculates averages, zeroes are considered whereas blanks are not.

* To modify how blank measures display in your report, use the**Blank measures display as** field in the **Blank Cells** section of theReport Options dialog box.
