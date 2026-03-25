# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/execute-sql-script-cp/options-execute-sql-script/optional-statistic-fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/execute-sql-script-cp/options-execute-sql-script/optional-statistic-fields.md

# Optional statistic fields

Use these optional fields to collect statistics when the **Execute for each row?** parameter is selected. Each option will create a field in the data stream that contains the specific type of statistic.

| Field                             | Description                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Field to contain insert stats** | Specify a field name to contain the statistic for the number of records that were inserted. |
| **Field to contain Update stats** | Specify a field name contain the statistic for the number of records that were updated.     |
| **Field to contain Delete stats** | Specify a field name to contain the statistic for the number of records that were deleted.  |
| **Field to contain Read stats**   | Specify a field name to contain the statistic for the number of records that were read.     |
