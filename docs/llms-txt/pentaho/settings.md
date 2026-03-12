# Source: https://docs.pentaho.com/pba/pentaho-user-console/modern-design/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-upsert/options-salesforce-upsert/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-update/options-salesforce-update/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-insert/options-salesforce-insert/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/settings-tab/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-delete/options-salesforce-delete/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-upsert/options-salesforce-upsert/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-update/options-salesforce-update/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-insert/options-salesforce-insert/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/settings-tab/settings.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-delete/options-salesforce-delete/settings.md

# Settings

Enter the delete process settings in the following transformation step options:

| Option                      | Description                                                                                                                                                                                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time out**                | Specify the interval in milliseconds before step timeout occurs. 60000 ms is the default.                                                                                                                                                                                                                        |
| **Use compression**         | Select to compress (`.gzip`) data when connecting between PDI and Salesforce.                                                                                                                                                                                                                                    |
| **Rollback all changes on** | Revert changes unless all records are processed successfully. When you select this option, records without errors are deleted, while records with errors are marked `failed` in the deletion results. The default behavior is to allow partial success of deletion.                                              |
| **Batch Size**              | Indicate the number of records in the set of records (batch) to delete. 10 records is the default.                                                                                                                                                                                                               |
| **Module**                  | <p>Select the module (table) in which you want to delete records. Account is the default module.</p><p>This list will be populated upon successfully authenticating to Salesforce using the <strong>Test connection</strong> button.</p>                                                                         |
| **Fieldname id**            | <p>Select the name of the field containing the Salesforce ID of the first record in the set of records (batch) you want to delete.</p><p>This list is populated with field names received from the previous step in a transformation. For example, you can use the Salesforce Input step to get field names.</p> |
