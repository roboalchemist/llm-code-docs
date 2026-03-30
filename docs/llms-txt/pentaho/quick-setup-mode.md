# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/sqoop-import-job/general-sqoop-import/quick-setup-mode.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/sqoop-export-job/general-sqoop-export/quick-setup-mode.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/sqoop-import-job/general-sqoop-import/quick-setup-mode.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/sqoop-export-job/general-sqoop-export/quick-setup-mode.md

# Quick Setup mode

![PDI Sqoop export step Quick Setup mode](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-fab93af823734c7059d607b5b8984f6b5bdf7f87%2FPDI%20Sqoop%20export%20step%20Quick%20Setup%20mode.png?alt=media)

## Source

The source refers to the Hadoop cluster where your Sqoop data that you want to import into a database is stored.

| Option               | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hadoop Cluster**   | <p>The name of the Hadoop cluster that contains the data for export. Use the <strong>Use Advanced Options</strong> to specify configuration information for the host names and ports for HDFS, Job Tracker, and other big data cluster components (default).</p><p>Click <strong>Choose Available</strong> to select an existing cluster to use. If you do not have any existing cluster connections, click <strong>New.</strong></p><p>Information on Hadoop can be found in <a href="https://help.hitachivantara.com/Documentation/Pentaho/9.5/Work_with_data/Use_Hadoop_with_Pentaho">Use Hadoop with Pentaho</a>.</p> |
| **Edit**             | Click **Edit** to open the **Hadoop Cluster** dialog box where you can edit the configuration information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **New**              | Click **New** to open the **Hadoop Cluster** dialog box where you can add a new Hadoop cluster configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Export Directory** | Path of the HDFS directory containing the Sqoop data you want to export.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Browse**           | <p>Click <strong>Browse</strong> to display the <strong>Open File</strong> dialog box, which displays the file system of the cluster. Click the directory to select the directory with your Sqoop data.</p><p><strong>Note</strong>: <strong>Browse</strong> only works when you have a valid cluster connection configured and selected.</p>                                                                                                                                                                                                                                                                             |

\## Open File dialog box

When you have a valid cluster connection, click **Browse** to display the **Open File** dialog box to view the cluster files.

| Option                                   | Definition                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Open from Folder**                     | Indicates the path and name of the HDFS directory you want to browse. This directory becomes the active directory. |
| **Up One Level**                         | Displays the parent directory of the active directory shown in the **Open from Folder** field.                     |
| **Delete**                               | Deletes a folder from the active directory.                                                                        |
| **Create Folder**                        | Creates a new folder in the active directory.                                                                      |
| **Active Directory Contents (no label)** | Displays the active directory, which is the one that is listed in the **Open from Folder** field.                  |
| **Filter**                               | Applies a filter to the results displayed in the active directory contents.                                        |

## Target

The target refers to the database where you want to put your Sqoop data.

| Option                  | Definition                                                                                                                                                                                                                                                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Database Connection** | <p>Click <strong>Choose Available</strong> to select the name of an existing database connection that contains the data for export.</p><p>If you do not have an existing connection, click <strong>New</strong>. If you need to modify an existing connection, click <strong>Edit</strong>.</p> |
| **Edit**                | Click **Edit** to open the **Database Connection** dialog box if you need to modify an existing connection database.                                                                                                                                                                            |
| **New**                 | Click **New** to open the **Database Connection** dialog box where you can add a new database connection. See [Define data connections](https://help.hitachivantara.com/Documentation/Pentaho/9.5/Setup/Define_data_connections)                                                                |
| **Table**               | The name of the target destination table. If the source database requires a schema, you must supply it in the format: `SCHEMA.TABLE_NAME`. This table must exist in the destination database and its structure must match the input data’s format.                                              |
| **Browse**              | Click **Browse** to open the **Database Explorer** and explore configured database connections.                                                                                                                                                                                                 |
