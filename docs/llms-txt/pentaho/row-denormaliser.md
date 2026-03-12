# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser.md

# Row Denormaliser

The Row denormaliser step can be used to try to improve performance either by adding redundant copies of data values or by grouping data. You can also use this step to convert data types.

**Note:** The data must be normalized before you can denormalize it.

For example, consider the following set of normalized data:

| Produce Category | Delivery Time       | Produce Type |
| ---------------- | ------------------- | ------------ |
| fruit            | 2018/01/05 08:00:00 | apples       |
| fruit            | 2018/01/05 08:10:00 | oranges      |
| fruit            | 2018/01/05 08:20:00 | apples       |
| fruit            | 2018/01/05 08:30:00 | oranges      |

The data can be denormalized by grouping on the type of fruit, as shown in the following table:

| Produce Category | Apples              | Oranges             |
| ---------------- | ------------------- | ------------------- |
| fruit            | 2018/01/05 08:00:00 | 2018/01/05 08:10:00 |
| fruit            | 2018/01/05 08:20:00 | 2018/01/05 08:30:00 |
