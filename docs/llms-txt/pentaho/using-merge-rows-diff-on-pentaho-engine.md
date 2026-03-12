# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/merge-rows-diff/select-an-engine-merge-rows-diff/using-merge-rows-diff-on-pentaho-engine.md

# Using Merge rows (diff) on the Pentaho engine

If you are running your transformation on the Pentaho engine, use the following instructions to set up the Merge rows (diff) step.

**Important:** When using the Pentaho transformation engine, the reference rows and compare rows must be sorted on the specified keys. When using the Merge rows (diff) step within a PDI transformation, such as with the [Sort rows](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Sort%20rows%20\(transformation%20step\)=GUID-DE76988A-FFA1-4B13-9F4D-8C357068552A=2=en=.md) step, sorting works correctly. However, if the data is sorted outside of PDI, such as in a SQL query, you may run into issues with the internal case sensitive/insensitive flag or other collations. If you are using the Merge rows (diff) step with the Spark engine, see [Using Merge rows (diff) on the Spark engine](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/merge-rows-diff/select-an-engine-merge-rows-diff/using-merge-rows-diff-on-spark-engine-article).
