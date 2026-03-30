# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/filter-rows.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/filter-rows.md

# Filter rows

To filter rows (remove the rows from the output for example) set the**trans\_Status** variable as follows:

```javascript
trans_Status = CONTINUE_TRANSFORMATION
if (/* add your condition here */) trans_Status = SKIP_TRANSFORMATION

```

All rows matching the specified condition are removed from the output.
