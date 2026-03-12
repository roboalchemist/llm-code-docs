# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/variables-for-build-model-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/variables-for-build-model-job-entry.md

# Variables for Build Model job entry

These variables are generated when the model is created. You can only see these specific variables for the Build Model job entry if you press CTRL Space after the first run.

You can use these variables to know more about the model you created. For example, if you have scheduled a job to run at regular intervals, you can include these variables in the Mail job entry to alert you to any issues during the run.

| Variable                                                | Variable Type           | Definition                                                                                                                                                                |
| ------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JobEntryBuildModel.DatabaseConnection.\<Model Name>** | String                  | Returns the name of the database connection used by the transformation on the source. This connection information is specified in the Build Model job entry.              |
| **JobEntryBuildModel.XMI.\<Model Name>**                | String                  | Returns all the contents of the XML file published on the Pentaho Server (It may or may not contain the OLAP components.)                                                 |
| **JobEntryBuildModel.XMI.DSW.\<Model Name>**            | Boolean (True or False) | Indicates if the XMI should be delivered as a Data Source Wizard data source. Typically, when this is 'true', we only generate the DSW data source and no other contents. |
