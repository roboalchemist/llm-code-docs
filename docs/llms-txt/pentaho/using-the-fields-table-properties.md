# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties.md

# Using the fields table properties

You define properties for the fields to read or write using the fields table. The properties in the fields table determine the field-level processing options for your row data, including the metadata attributes. Some commonly used steps that include a fields table are [Split Fields](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Split%20Fields=GUID-36055D0C-1602-4F21-BEA7-BEEDF325CAAD=2=en=.md), [Select Values](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Select%20Values=GUID-14FD2047-C05A-4E28-A0E9-8C8696823EC4=2=en=.md), [Text File Output](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp), and [Concat Fields](http://wiki.pentaho.com/display/EAI/Concat+Fields).

When using the fields table the following definitions and processing rules apply.

**Note:** Depending on the transformation step or job entry, some fields tables may feature only a portion of the columns listed below.

![PDI fields table](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-111aff0b329d7b44e6e9f31ed3d8d8f503dfc7b6%2FPDI_format_table_example.png?alt=media)

* **Name**

  The name of the field.
* **Type**

  The type of the field. For example, String, Date, or Number. See [Data type mappings](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/data-type-mappings) for more information.
* **Format**

  Defines the format mask to use when converting the value to, or reading the value from, a string. The **Format** drop-down menu offers suggestions, but you can enter your own mask. **Format** is only used when converting a non-string data type to a string data type. **Format** overrides **Length** and **Precision**. See [Applying formatting](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-formatting) for formatting details.
* **Length**

  Defines the length to use when converting the value to, or reading the value from, a string. The numbers before the decimal point, or a value that is longer than the maximum length, will not be truncated. **Length**, also called Precision in some databases, is a metadata component. PDI converts to the required metadata type when the data is resulted to a string, not during the transformation (or job) or if resulted to non-string data types. See [Output type examples](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/output-type-examples) for a listing of string and non-string types. **Length** is not used when **Format** is specified.
* **Precision**

  Defines the number of digits after the decimal point to use when converting the value to, or reading the value from, a string. The numbers before the decimal point will not be truncated. **Precision**, also called Scale in some databases, is a metadata component. PDI converts to the required metadata type when the data is resulted to a string, not during the transformation (or job) or if resulted to non-string data types. See [Output type examples](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/output-type-examples) for a listing of string and non-string types. **Precision** is not used when **Format** is specified.
* **Currency**

  Used in conjunction with **Format** to interpret numbers such as `$10,000.00` or `E5.000,00`. If the format mask contains the Unicode currency symbol ¤ (`\u00A4`), then it replaces the symbol by the value in the currency column. In Pentaho, you must use the copy and paste method to apply this symbol. See [Common Formats](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats) for information on valid number formats.
* **Decimal**

  Represents the character that replaces the period (.) in the format mask. Only applies when converting the value to, or reading the value from, a string.
* **Group**

  Represents the character that replaces the comma (,) in the format mask. Only applies when converting the value to, or reading the value from, a string.
* **Null if**

  Converts the value to null if the input value matches.

  **Note:** This value is case-sensitive.
* **Default**

  Defaults to this value if the value is null.
* **Trim type**

  Defines the type of trimming to perform on the input or the output string. Trimming removes the white space on either side of a string. Options are both, left, right, or none.
* **Repeat**

  Determines how null rows are handled. If the value in this row is null, then the value from the last row where the column was not null is used.
