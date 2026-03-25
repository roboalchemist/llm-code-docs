# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-calculations-and-rounding.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-calculations-and-rounding.md

# Applying calculations and rounding

Number and date calculations performed in PDI do not apply the **Format**, **Length**, and **Precision** properties. For example, using the table below, A + B + B = `30.1` If you preview B, it will appear as `10.0`, so you would think `10.02 + 10.0 + 10.0` `= 30.02`. However, because B was never converted to a string for the calculation, `10.02 + 10.04 + 10.04` `= 30.1.`

| Field | Input   | **Format** | **Decimal** | **Group** | **Length** | **Precision** |
| ----- | ------- | ---------- | ----------- | --------- | ---------- | ------------- |
| A     | `10.02` | #.0        | .           | ,         | 5          | 1             |
| B     | `10.04` |            | .           | ,         | 5          | 1             |

If you want to truncate a string, use the [Strings cut](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/strings-cut) step.

If you want to round or truncate a number, use the following [Calculator](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/calculator) step features:

* Round function
* Floor and Ceil functions

Alternatively, you can convert the date or number to a string in the [Select Values](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/select-values) step, which applies the formatting specified in the metadata.
