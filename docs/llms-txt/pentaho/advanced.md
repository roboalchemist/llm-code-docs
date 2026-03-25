# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/content-tab/advanced.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/content-tab/advanced.md

# Advanced

Use these options to further refine the data returned from the queries specified in the **Settings** tab. For example, you may want to only query deleted records within a specified date range. The **Advanced** panel includes the following fields.

| Option                | Description                                                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Retrieve**          | Select which records you want to retrieve to further define your pool of data. You can select **All**, **Updated**, or **Deleted**. **All** is the default for retrieval. |
| **Query all records** | Select the check box to query all the records you are retrieving. Clear the check box to use the date fields to define a range of records to query.                       |
| **Start date**        | Specify the starting date for retrieving the records in the date range. The format is `yyyy-MM-dd HH:mm:ss`.                                                              |
| **End date**          | Specify the end date for retrieving the records in the date range. The format is `yyyy-MM-dd HH:mm:ss`.                                                                   |
