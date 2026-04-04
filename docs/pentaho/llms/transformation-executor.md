# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/transformation-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor.md

# Transformation Executor

The Transformation Executor step allows you to execute a Pentaho Data Integration (PDI) transformation. It is similar to the [Job Executor](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/job-executor) step, but works with transformations.

Depending on your data transformation needs, the Transformation Executor step can be set up to function in any of the following ways:

* By default, the specified transformation will be executed once for each input row. You can use the input row to set parameters and variables. The executor step then passes this row to the transformation in the form of a result row.
* You can also pass a group of records based on the value in a field, so that when the field value changes dynamically, the specified transformation is executed. In these cases, the first row in the group of rows is used to set parameters or variables in the transformation.
* You can launch multiple copies of this step to assist in parallel transformation processing.
