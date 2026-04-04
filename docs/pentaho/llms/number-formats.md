# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/common-formats/number-formats.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats/number-formats.md

# Number formats

The following table describes common number formats used by PDI transformation steps and job entries:

| Symbol             | Location             | Localized? | Meaning                                                                                                                                                                                              |
| ------------------ | -------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                  | Number               | Yes        | Digit                                                                                                                                                                                                |
| #                  | Number               | Yes        | Digit, zero shows as absent                                                                                                                                                                          |
| .                  | Number               | Yes        | Decimal separator or monetary decimal separator                                                                                                                                                      |
| <ul><li></li></ul> | Number               | Yes        | Minus sign                                                                                                                                                                                           |
| ,                  | Number               | Yes        | Grouping separator                                                                                                                                                                                   |
| E                  | Number               | Yes        | <p>Separates mantissa and exponent in scientific notation.</p><p>Note: E does not need to be in quotation marks within a prefix or a suffix.</p>                                                     |
| ;                  | Sub-pattern boundary | Yes        | Separated positive and negative sub-patterns                                                                                                                                                         |
| %                  | Prefix or suffix     | Yes        | Multiply by 100 and show as percentage                                                                                                                                                               |
| ‰ (\u2030)         | Prefix or suffix     | Yes        | Multiply by 1000 and show as per mile                                                                                                                                                                |
| ¤ (\u00A4)         | Prefix or suffix     | No         | Currency sign, replaced by currency symbol. If doubled, replaced by international currency symbol. If present in a pattern, the monetary decimal separator is used instead of the decimal separator. |
| '                  | Prefix or suffix     | No         | Used to quote special characters in a prefix or suffix, for example, `'#'#` formats 123 to `#123`. To create a single quote itself, use two in a row: `# o''clock`.                                  |
