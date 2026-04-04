# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mapping.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapping.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping.md

# Mapping

As you build a transformation, you may notice a sequence of steps that you want to repeat. This repetitive part can be turned into a mapping.

A mapping is a transformation with placeholder input and output steps. The mapping transformation is executed through the Mapping step in a parent transformation. Because the parent transformation runs a separate transformation through a specific step, the mapping transformation is commonly referred as a sub-transformation. The sub-transformation must contain the following input and output steps:

* Mapping input: a placeholder where the mapping expects input from the parent transformation.
* Mapping output: a placeholder indicating, from where, the parent transformation can read data.

Use mapping when you want to re-use a certain sequence of steps in a transformation. The following image illustrates mapping and the relationship of the parent

![Transformation Mapping](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-423b4d2bec5d6fa55446a24017fabde77356e002%2FPDI_TransStep_Mapping_Transformation_Mapping.png?alt=media)
