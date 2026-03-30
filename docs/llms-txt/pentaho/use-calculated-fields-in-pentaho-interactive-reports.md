# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/use-calculated-fields-in-pentaho-interactive-reports.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/use-calculated-fields-in-pentaho-interactive-reports.md

# Use calculated fields in Pentaho Interactive Reports

You can create calculated fields from fields that are available in the data source and from other calculated fields. When you create a calculated field, a new field is generated in the **Calculated Fields** list. The values are determined by the kind of calculation the function performs. You can add these fields to the columns or groups in the layout to create more robust reports. Generic functions like `now()` or`2+5` cannot be added to an empty layout. These generic functions can be added after the layout has at least one column or group from a data source field. The **Filter**, **Prompt**, **Sort**, and **Aggregation** options are not supported for calculated fields.
