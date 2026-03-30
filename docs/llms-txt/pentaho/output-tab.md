# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake/options-snowflake-bulk-loader/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift/options-bulk-load-into-amazon-redshift/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation/options-simple-mapping/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/query-hcp/options-query-hcp/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapping/options-mapping-step/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake/options-snowflake-bulk-loader/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift/options-bulk-load-into-amazon-redshift/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation/options-simple-mapping/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/query-hcp/options-query-hcp/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping/options-mapping-step/output-tab.md

# Output tab

![Mapping Output Tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e3065547b572e19a0f2cf62caf329db38c08fe34%2FPDI_TransStep_Mapping_Output_Tab.png?alt=media)

By default, one output entry is available; however, you can add more output entries using the Plus Sign button by the **Available outputs** pane. Each of the output entries correspond to one Mapping output specification step in the mapping or sub-transformation. That means you can have any number of output entries (or none) in a single mapping step.

| Options                            | Description                                                                                                                                                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Available outputs (Add output)** | <p>Use the Plus Sign button to add a tab to specify an output mapping for the specified sub-transformation.</p><p>You can remove an output entry by clicking the X icon.</p>                                                                               |
| **Main data path**                 | Check this if you only have one output mapping and you can leave the two following fields (**Mapping source step name**and **Output target step name**) empty.                                                                                             |
| **Mapping source step name**       | The name of a Mapping output specification step in the sub-transformation where data will be read from. Use the **Choose** button to select this step from a list.                                                                                         |
| **Output target step name**        | The name of the step in the current transformation (parent) that is to receive the rows from the Mapping source step. This can be any step whose incoming hop is connected to the Mapping step. Use the **Choose** button to select this step from a list. |
| **Description**                    | Add a description to this output step mapping here.                                                                                                                                                                                                        |
| **Mapping**                        | Not enabled on the **Output** tab.                                                                                                                                                                                                                         |
