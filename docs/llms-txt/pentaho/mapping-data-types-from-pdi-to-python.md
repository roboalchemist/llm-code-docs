# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/input-tab/mapping-data-types-from-pdi-to-python.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/input-tab/mapping-data-types-from-pdi-to-python.md

# Mapping data types from PDI to Python

When mapping a data type from PDI to Python, you will want to make the most precise mappings. This table lists the closest PDI data types to the most similar Python data types. Be sure to consider if you are using Pandas dataFrame or NumPy array in this mapping.

| Python Data Structure   | PDI Data Type   | Python Data Type |
| ----------------------- | --------------- | ---------------- |
| Pandas dataFrame        | BigNumber       | float64          |
| Boolean                 | bool            |                  |
| Date                    | datetime64\[ns] |                  |
| Integer                 | int64           |                  |
| Number                  | float64         |                  |
| String                  | object          |                  |
| Timestamp               | datetime64\[ns] |                  |
| NumPy array             | BigNumber       | float64          |
| Boolean                 | bool            |                  |
| Integer                 | int64           |                  |
| Number                  | float64         |                  |
| Basic Python Data Types | BigNumber       | float            |
| Boolean                 | bool            |                  |
| Integer                 | int             |                  |
| Number                  | float           |                  |
| String                  | str             |                  |
| Timestamp               | datetime        |                  |
