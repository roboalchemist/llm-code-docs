# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation.md

# Simple Mapping (sub-transformation)

As you build a transformation, you may notice a sequence of steps you want to repeat. This sequence can be turned into a mapping.

Just like the [Mapping](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping) step, you can use the Simple Mapping (sub-transformation) step to turn the repetitive, re-usable part of a transformation into a mapping.

Compared to the Mapping step, the Simple Mapping (sub-transformation) step accepts one and only one input and output step. As such, it behaves like any other regular step which reads and writes rows of data.

Also, as with the Mapping step, input and output are defined by the following placeholder steps:

* [**Mapping input step**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping/mapping-input-specification)

  a placeholder where the mapping expects input from the parent transformation.
* [**Mapping output step**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping/mapping-output-specification)

  a placeholder from where the parent transformation can read data.

The mapping executed by the parent transformation through the Simple Mapping (sub-transformation) step is known as the sub-transformation.

You can run the Simple Mapping (sub-transformation) step in multiple copies, clusters, in single threading mode, or in any other execution model. You can also use this step in advanced data routing scenarios (filter rows and switch/case for example) or in partitioning or partitioning/clustering transformations.
