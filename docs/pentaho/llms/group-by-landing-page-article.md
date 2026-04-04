# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/group-by-landing-page-article.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/group-by-landing-page-article.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/group-by-landing-page-article.md

# Group By

This step groups rows from a source, based on a specified field or collection of fields. A new row is generated for each group. It can also generate one or more aggregate values for the groups. Common uses are calculating the average sales per product and counting the number of an item you have in stock.

The Group By step is designed for sorted inputs. If your input is not sorted, only double consecutive rows are grouped correctly. If you sort the data outside of PDI, the case sensitivity of the data in the fields may produce unexpected grouping results.

You can use the [Memory Group By](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/memory-group-by) step to handle non-sorted input.
