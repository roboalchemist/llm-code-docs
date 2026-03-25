# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/modify-connections/modify-connections-from-puc.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/modify-connections/modify-connections-from-puc.md

# Modify connections from PUC

Access other database-related connection tasks in PUC through the **More actions and options** menu in the Manage Data Sources dialog box, as shown below:

![More actions and options menu in the PUC Manage Data Sources dialog box](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-cda20df43d7b3d70b8ae03b262e2ce118ed3e139%2FssPUCManageDataSourcesOtherConnectionTasks.png?alt=media)

The following table describes these tasks:

| Task                | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Export**          | <p>Exports database connection information according to the type:- <strong>Metadata</strong> downloads an XMI file.</p><ul><li><strong>Analysis</strong> downloads an XML file.</li><li><p>Data Source Wizard downloads according to the source:</p><ul><li>Reporting only sources download an XMI file.</li><li>Reporting and analysis sources download a ZIP file.</li></ul></li></ul> |
| **Import Analysis** | <p>Imports data values from a Mondrian file into a specified data source, with the following options:- <strong>Select from available data sources</strong>.</p><ul><li><strong>Manually enter data source parameter values</strong>.</li></ul>                                                                                                                                           |
| **Import Metadata** | <p>Imports data values and creates a data source according to the model:- Data Source Wizard\*\*(Includes Analysis model)\*\* from a ZIP file created using the <strong>Export</strong> option.</p><ul><li><strong>Metadata model</strong> from an XMI file.</li></ul>                                                                                                                   |
