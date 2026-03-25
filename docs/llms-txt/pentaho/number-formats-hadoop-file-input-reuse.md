# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/fields-tab-hadoop-file-input-reuse/number-formats-hadoop-file-input-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/fields-tab-hadoop-file-input-reuse/number-formats-hadoop-file-input-reuse.md

# Number formats

Use the following table to specify number formats. For further information on valid numeric formats used in this step, view the [Number Formatting Table](http://wiki.pentaho.com/display/Reporting/Number+Formatting+Table).

| Symbol     | Location            | Localized | Meaning                                                                                                                                                                                              |
| ---------- | ------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0          | Number              | Yes       | Digit.                                                                                                                                                                                               |
| #          | Number              | Yes       | Digit, zero shows as absent.                                                                                                                                                                         |
| .          | Number              | Yes       | Decimal separator or monetary decimal separator.                                                                                                                                                     |
| -          | Number              | Yes       | Minus sign.                                                                                                                                                                                          |
| ,          | Number              | Yes       | Grouping separator.                                                                                                                                                                                  |
| E          | Number              | Yes       | Separates mantissa and exponent in scientific notation. Need not be quoted in prefix or suffix.                                                                                                      |
| ;          | Subpattern boundary | Yes       | Separates positive and negative patterns.                                                                                                                                                            |
| %          | Prefix or suffix    | Yes       | Multiply by 100 and show as percentage.                                                                                                                                                              |
| ‰(/u2030)  | Prefix or suffix    | Yes       | Multiply by 1000 and show as per mille.                                                                                                                                                              |
| ¤ (/u00A4) | Prefix or suffix    | No        | Currency sign, replaced by currency symbol. If doubled, replaced by international currency symbol. If present in a pattern, the monetary decimal separator is used instead of the decimal separator. |
| ‘          | Prefix or suffix    | No        | Used to quote special characters in a prefix or suffix, for example, '#'# formats `123` to `#123`. To create a single quote itself, use two in a row: `# o''clock`.                                  |
