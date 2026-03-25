# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mapreduce-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapreduce-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapreduce-output.md

# MapReduce Output

This step defines the key/value pairs for Hadoop output. The output of this step becomes the Hadoop output, and depends on how you have configured the transformation. This step may be included in a transformation used as a Mapper, Combiner, or Reducer.

When this step is included in a **Mapper** transformation type, and a combiner and/or reducer is configured, the output will be the input pairs for the combiner and/or the reducer. If no combiner or reducers are configured, the output is passed with the submitting Hadoop job’s format.

When this step is included in a **Combiner** transformation type, and a reducer is configured, the output will be the input pairs for the reducer. If no reducer is configured, the output is passed with the submitting Hadoop job’s format.

When this step is included in a **Reducer** transformation type, then the output is passed with the submitting Hadoop job’s format. The data type for the keys or values must be defined before this step.
