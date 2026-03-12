# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/create-warehouse-pdi-job-entry/options-create-warehouse-job-entry/activity-settings-create-warehouse-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/create-warehouse-pdi-job-entry/options-create-warehouse-job-entry/activity-settings-create-warehouse-job-entry.md

# Activity settings

You can define the initial state of the warehouse once it is created. You can also determine what happens within the PDI job if the requested new warehouse already exists.

| Option                                         | Description                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **If warehouse exists**                        | <p>Select a result for the PDI job if the identified warehouse already exists.- <strong>Fail (default)</strong></p><p>The PDI job stops. No warehouse is created.</p><ul><li><strong>Replace</strong></li></ul><p>The PDI job replaces the existing warehouse and the job continues.</p><ul><li><strong>Continue</strong></li></ul><p>The PDI job continues.</p> |
| **Initially suspend warehouse after creation** | <p>Specify whether the warehouse is created initially in the suspended state.- Leave this checkbox cleared (default) to start the warehouse after it is created.</p><ul><li>Select this checkbox to suspend the warehouse after it is created.</li></ul>                                                                                                         |
