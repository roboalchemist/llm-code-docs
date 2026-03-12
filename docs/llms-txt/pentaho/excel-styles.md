# Source: https://docs.pentaho.com/pba-report-designer/style-properties-reference/excel-styles.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/style-properties-reference/excel-styles.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/style-properties-reference/excel-styles.md

# Excel styles

**Excel** styles control Microsoft Excel XLSX worksheet output options.

**Note:** Starting with Report Designer v10.2, Excel XLSX is the only supported worksheet format.

The following table describes the Excel style properties:

| Property Name        | Data Type | Purpose                                                                                                       |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------- |
| **sheet-name**       | String    | The title of the sheet or table generated in table exports                                                    |
| **format-override**  | String    | Override setting that provides Excel-specific cell formats                                                    |
| **formula-override** | String    | Override setting that provides a formula to print in the generated Excel cell instead of the original content |
| **wrap-text**        | Boolean   | Override setting that defines whether Excel cells should have **text-wrapping** enabled                       |
