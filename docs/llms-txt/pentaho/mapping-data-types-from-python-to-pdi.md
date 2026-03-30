# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab/mapping-data-types-from-python-to-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab/mapping-data-types-from-python-to-pdi.md

# Mapping data types from Python to PDI

When mapping a data type from Python to PDI, you will want to make the most precise mappings. This table lists the closest Python data types to the most similar PDI data types. Be sure to consider if you are using Pandas dataFrame in this mapping.

| Python Data Structure   | Python Data Type | PDI Data Type |
| ----------------------- | ---------------- | ------------- |
| Pandas dataFrame        | bool             | Boolean       |
| datetime64\[ns]         | Timestamp        |               |
| float64                 | BigNumber        |               |
| int64                   | Integer          |               |
| object                  | String           |               |
| Basic Python Data Types | bool             | Boolean       |
| datetime                | Timestamp        |               |
| float                   | BigNumber        |               |
| int                     | Integer          |               |
| str                     | String           |               |

**Note:** In the **Output** tab, you can also convert a matplotlib figure to an SVG string.
