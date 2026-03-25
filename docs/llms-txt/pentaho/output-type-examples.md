# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/output-type-examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/output-type-examples.md

# Output type examples

The following table provides examples of the string and non-string output types in PDI. Note that **Format**, **Length**, **Precision**, **Decimal**, and **Group** apply only when reading from, or outputting to, a string.

| String output type example                                             | Non-string output type example                    |
| ---------------------------------------------------------------------- | ------------------------------------------------- |
| Preview                                                                | Table Output when the target field is a number.   |
| Text File Output                                                       | Avro Output when the target field is a number.    |
| JSON Output                                                            | Parquet Output when the target field is a number. |
| XML Output                                                             | ORC Output when the target field is a number.     |
| Table Output when the target field is a varchar.                       | Any binary output type                            |
| Anything displayed by PDI including logs, error messages, and prompts. |                                                   |
