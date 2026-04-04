# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift/options-bulk-load-into-amazon-redshift/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/options-user-defined-java-class/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/single-threader/options-single-threader/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation/options-simple-mapping/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/rest-client-step/options-rest-client/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapping/options-mapping-step/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift/options-bulk-load-into-amazon-redshift/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/options-user-defined-java-class/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/single-threader/options-single-threader/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation/options-simple-mapping/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/rest-client-step/options-rest-client/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping/options-mapping-step/parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/parameters-tab.md

# Parameters tab

![Job Executor step showing the Parameters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3e795c79323700a88deab558ae1082d5fe088e01%2Fpdi_step_job_executor_w550.png?alt=media)

This tab allows you to define or pass variables and/or parameters to the job. If multiple rows are passed to the job, the first row can be used to set the parameters or variables.

For each variable or parameter name that is added to table, you must assign a value to that parameter in either the **Variable / Parameter to use** field or the **Static input value** field. You cannot use both a variable and a static value.

| Option                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Variable / Parameter name**                 | Specify the name of the variable or parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Variable / Parameter to use**               | <p>The <strong>Variable / Parameter to use</strong> column is for setting the names of variables and/or parameters that are defined and passed to the child transformation.For this column, enter a value using one of the following methods:</p><ul><li>Select an incoming field using the drop-down menu.</li><li>Manually enter a variable name.</li><li>Use CTRL SPACE to select a value from a list of PDI environment variables.</li></ul><p>If you specify a field or value in <strong>Variable / Parameter to use</strong>, the <strong>Static input value</strong> column is disabled.When the <strong>Variable / Parameter to use</strong> contains a valid value, the <strong>Inherit all variables from transformation</strong> check box does not affect the <strong>Variable/Parameter to use</strong>.</p> |
| **Static input value**                        | Instead of a field, specify a static value to use.Entering a value in the **Static input value** field disables the **Variable / Parameter to use** field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Inherit all variables from transformation** | When this check box is selected, all the variables defined in the parent transformation are passed to the child transformation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Get Parameters**                            | Click this option to insert all the defined parameters of the specified transformation. The description of the parameter is inserted into the static input value field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
