# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/modify-warehouse-pdi-job-entry/options-modify-warehouse-job-entry/activity-settings-modify-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/modify-warehouse-pdi-job-entry/options-modify-warehouse-job-entry/activity-settings-modify-warehouse.md

# Activity settings

This option controls what happens if the PDI job requests a Snowflake warehouse that does not exist.

| Option                              | Description                                                                                                                                                                                                                                                                                                                              |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fail if warehouse doesn't exist** | <p>Specify how the PDI job should behave if the requested warehouse does not exist.- Leave this check box selected (default) if you want the PDI job to fail.</p><ul><li>Clear this check box if you want the PDI job to continue when the requested warehouse does not exist. The PDI job moves to the next entry in the job.</li></ul> |
