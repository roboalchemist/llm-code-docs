# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/memory-group-by.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/memory-group-by.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/memory-group-by.md

# Memory Group By

The Memory Group By step groups rows in memory from a source step. The resulting rows are grouped based on a specified field or collection of fields. A new row is generated for each group. This step differs from the [Group By](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Group%20By%20-%20landing%20page%20article=GUID-A08851B3-A78C-4416-BF7E-052B32B949AF=3=en=.md) step by processing all rows in memory, and is designed to handle non-sorted input. If the number of rows you want to group is too large to fit into memory, you must use a combination of the [Sort rows](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/sort-rows-transformation-step) and Group By steps.
