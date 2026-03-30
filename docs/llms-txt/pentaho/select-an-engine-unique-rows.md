# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/unique-rows/select-an-engine-unique-rows.md

# Select an engine

You can run the Unique Rows step on the Pentaho engine or on the Spark engine.

The input stream must be sorted in a step prior to the Unique Rows step; otherwise, only consecutive double rows will be correctly analyzed and filtered. However, the rows do not have to be pre-sorted if you use the [Unique Rows (HashSet)](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Unique%20Rows%20\(HashSet\)=GUID-3D3F41A3-F02F-45A5-8FA5-FEF941A37555=6=en=.md) step, or if you use the Spark engine ([Spark Engine](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/unique-rows/broken-reference)) to run the transformation.

Depending on your selected engine, the transformation runs differently. Select one of the following options to view how to set up the Unique Rows step for your selected engine:

* [Using the Unique Rows step on the Pentaho engine](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/unique-rows/select-an-engine-unique-rows/using-the-unique-rows-step-on-the-pentaho-engine): Learn how to set up this step when using the Pentaho engine.
* [Using the Unique Rows step on the Spark engine](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/unique-rows/select-an-engine-unique-rows/using-the-unique-rows-step-on-the-spark-engine): Learn how to set up this step when using the Spark engine.

For instructions on selecting an engine for your transformation, see [Run configurations](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/run-configurations-work-with-transformations)
