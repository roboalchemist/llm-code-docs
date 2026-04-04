# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/java-filter-pdi-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/java-filter-pdi-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/java-filter-pdi-step.md

# Java filter

The Java filter step refines a transformation data stream using a Java expression to set up conditional processing.

![Transformation using the Java filter step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a7a48c15bb1760bafbbe59d868ffd69d9ca7e2c1%2FPDI_TransStep_Java_filter_canvas_w365.png?alt=media)

As shown in the sample transformation above, the output stream from the Data grid step is processed by the Java filter step. Based on the specified condition, the Java filter step sends matching data to the true step and non-matching data to the false step. Below is the condition used in this sample transformation.

```
if( condition)
{matching step}

else
{non-matching step}
```
