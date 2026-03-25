# Source: https://docs.pentaho.com/pba-report-designer/function-reference/advanced-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/function-reference/advanced-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/function-reference/advanced-functions.md

# Advanced functions

The **Advanced** category contains functions that deal with developer-centric actions.

| Function Name               | Purpose                                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Message Format**          | Formats text according to the Java Message Format specification.                                                                                                                                                |
| **Resource Message Format** | Formats text from a resource bundle according to the Java Message Format specification.                                                                                                                         |
| **Lookup**                  | Maps a string from one column to another string. The possible mappings are given as (key, text) pairs. If the string from the column is null or matches none of the defined keys, a fallback value is returned. |
| **Indirect Lookup**         | Returns a value from a mapped field. The field's value is used as a key to the field-mapping. The expression maps the value to a new column name and returns the value read from this column.                   |
| **Resource Bundle Lookup**  | Performs a resource-bundle lookup using the value from the defined field as a key in the resource bundle. This expression behaves like a resource field.                                                        |
| **Open Formula**            | Enables you to create your own custom OpenFormula function using the built-in Formula Editor. This function will run before any other action in the report.                                                     |
