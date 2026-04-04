# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/replace-in-string/fields-string-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/replace-in-string/fields-string-table.md

# Fields string table

![Fields string table in Replace in string](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ef584c68e35c309e27b627cc6018be7ac3addcdc%2FPDI_TransStep_Table_Replace-In-String.png?alt=media)

You can specify the replacement string and select options pertaining to it in the following table.

| Column                 | Description                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **In stream field**    | Specify the field to replace from the PDI input stream. Click **Get Fields** to add all fields from the input stream(s). |
| **Out stream field**   | Specify the new field name to output to the PDI stream.                                                                  |
| **use RegEx**          | Select **Y** (Yes) or **N** (No) to indicate whether to use a regular expression to search for values.                   |
| **Search**             | Specify whether to search for matched values of this string.                                                             |
| **Replace with**       | Specify the string to replace the matched value.                                                                         |
| **Set empty string?**  | Select **Y** (Yes) or **N** (No) to indicate whether to replace null values with empty strings.                          |
| **Replace with field** | Specify a field value that will be used to replace the matched value.                                                    |
| **Whole Word**         | Select **Y** (Yes) or **N** (No) to indicate whether to replace the entire word of the matched value.                    |
| **Case sensitive**     | Select **Y** (Yes) or **N** (No) to indicate whether the search is case sensitive.                                       |
| **Is Unicode**         | Select **Y** (Yes) or **N** (No) to indicate whether the search value is a sequence of Unicode characters.               |

Use **Get Fields** to add all fields from the PDI input stream.
