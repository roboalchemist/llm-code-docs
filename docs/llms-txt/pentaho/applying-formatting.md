# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-formatting.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-formatting.md

# Applying formatting

Format masks define how data returned for a field is converted to, or from, a string. For example, a field might return the value "`7000`", but you want to display it as "`$7,000.00`". To do this, you apply a format mask to the field. The original data is not truncated when using a format mask.

As shown in the table below, when **Format** is used with **Decimal**, the period (.) in the format mask is replaced with the indicated character. Alternatively, when **Format** is used with **Group**, the comma (,) in the format mask is replaced with the indicated character. See [Common Formats](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats) for information on valid number formats.

| Input / Output value | **Format** | **Decimal** | **Group** |
| -------------------- | ---------- | ----------- | --------- |
| 10.0                 | #.#        | .           | ,         |
| 1,546.99             | #,###.##   | .           | ,         |
| 1g546d99             | #,###.##   | d           | g         |
| €1.546,99            | €#,###.00  | ,           | .         |
| $1,546.99            | $#,###.00  | .           | ,         |

The following table shows that when \*\*Format\*\*, \*\*Decimal\*\*, \*\*Group\*\*, \*\*Length\*\*, and \*\*Precision\*\* are used together. \*\*Format\*\* always overrides \*\*Length\*\* and \*\*Precision\*\*.

| Input    | **Format** | **Decimal** | **Group** | **Length** | **Precision** | String output | Number output |
| -------- | ---------- | ----------- | --------- | ---------- | ------------- | ------------- | ------------- |
| 10.0     | #.#        | .           | ,         | 5          | 2             | 10.0          | 10.0          |
| 10.0     |            | .           | ,         | 5          | 2             | 010.00        | 10.0          |
| 10.01    |            | .           | ,         | 2          | 1             | 10.0          | 10.01         |
| 1,546.99 | #,###.##   | .           | ,         | 10         | 3             | 1,546.99      | 1546.99       |
| 1,546.99 | 0#,###.000 | .           | ,         |            |               | 01,546.990    | 1546.99       |
