# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/strings-cut/the-fields-to-cut-strings-cut-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/strings-cut/the-fields-to-cut-strings-cut-step.md

# The fields to cut

![The fields to cut table in the Strings cut step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-61e78c2ae3391f49f48fbbaf1ac3f0994ef6ca87%2FssPDITransStep_StringsCut_PropertiesDialogBox.png?alt=media)

Use **The fields to cut** table to specify what fields to cut and where to cut them.

The table contains the following columns:

| Column               | Description                                                                                                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **In stream field**  | Name of the field containing the string to cut. Use **Get fields** to populate the table with fields from the incoming PDI data stream.                                                                                                                                                 |
| **Out stream field** | (Optional) A new outgoing PDI field containing the resulting substring. If you do not specify a value for this field, the **In stream field** is replaced by the resulting substring.                                                                                                   |
| **Cut from**         | The character location at the starting point of the substring. This value is zero-based. The first character of the entire input string has an index of `0`.                                                                                                                            |
| **Cut to**           | The character location after the ending point of the substring, such that the substring cuts up to but not including the value entered. The value is zero-based but is exclusive. For example, setting **Cut to** to a value of `1` returns the first character in **In stream field**. |

The maximum length of the resulting string is **Cut to** minus **Cut from**.
