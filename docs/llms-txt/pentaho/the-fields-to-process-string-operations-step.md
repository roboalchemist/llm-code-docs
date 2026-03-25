# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/string-operations/the-fields-to-process-string-operations-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/string-operations/the-fields-to-process-string-operations-step.md

# The fields to process

![The fields to process table in the String Operations step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-222188d54946ca239477d148a270e6252b386656%2FssPDITransStep_StringOperations_PropertiesDialogBox.png?alt=media)

Use **The fields to process** table to specify which operations you want to apply to your input strings.

The table contains the following columns:

| Column                       | Description                                                                                                                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **In stream field**          | Name of the field containing the string to be processed. Use **Get fields** to populate the table with fields from the incoming PDI data stream.                                                                                                                  |
| **Out stream field**         | (Optional) A new outgoing PDI field containing the results of the specified string operations. If you do not specify a value for this field, the **In stream field** is replaced by the resulting string.                                                         |
| **Trim type**                | Specifies whether to remove extra spaces before or after a field. You can trim a field on its left side, right side, or both. The default value is none.                                                                                                          |
| **Lower/Upper**              | Specifies whether to make all the characters in a field upper or lowercase. The default value is none.                                                                                                                                                            |
| **Padding**                  | Specifies whether to add extra characters before or after a field. You can pad a field on its left side or its right side. The default value is none.                                                                                                             |
| **Pad char**                 | The extra character added to a field for padding.                                                                                                                                                                                                                 |
| **Pad Length**               | The amount of extra characters used for padding.                                                                                                                                                                                                                  |
| **InitCap**                  | Specifies whether to capitalize the initial character in a field. The default value is N.                                                                                                                                                                         |
| **Escape**                   | <p>Specifies whether to use, ignore (escape), or process (unescape) if the following formats are present in a field:</p><ul><li>XML</li><li>HTML</li><li>CDATA</li><li>SQL</li></ul><p>The default value is None.</p>                                             |
| **Digits**                   | Specifies whether to return only or remove numeric characters (digits). The default value is none.                                                                                                                                                                |
| **Remove Special character** | <p>Specifies whether to remove any of the following special characters from a field:</p><ul><li>Carriage return (CR)</li><li>Line feed (LF)</li><li>Carriage return and line feed</li><li>Horizontal tab</li><li>Space</li></ul><p>The default value is none.</p> |
