# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/configure-job-properties.md

# Configure job properties

Job properties are options that control how a job behaves and how it is logging what it is doing. To view the job properties, click `CTRL+T` or right-click the canvas and select **Properties** from the menu that appears. For transformation properties, See [Configure transformation properties](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/configure-transformation-properties).

* [Job tab](#job-tab)
* [Parameters tab](#parameters-tab)
* [Settings tab](#settings-tab)
* [Log tab](#log-tab)
* [Transactions tab](#transactions-tab)

## Job tab

General properties for jobs are found on the **Job** tab.

![Job settings job tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f9dcc32a19ec40ad728b1eb01b2b301abbb55596%2FPDI_Job%20settings%20job%20tab.png?alt=media)

This table describes all of the general job properties found on the **Job** tab:

| Option                   | Description                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Job Name**             | <p>The name of the job.</p><p><strong>Note:</strong> This information is required if you want to save to a repository.</p> |
| **Job filename**         | The file name of the job if it is not stored in the repository.                                                            |
| **Description**          | A user-defined short description of the job which is shown in the repository explorer.                                     |
| **Extended description** | A user-defined longer description of the job.                                                                              |
| **Status**               | The status of the job. The values are **draft** and **production**.                                                        |
| **Version**              | A description of the version.                                                                                              |
| **Directory**            | The directory in the repository where the job is kept.                                                                     |
| **Created by**           | The original creator of the job.                                                                                           |
| **Created at**           | The date and time when the job was created.                                                                                |
| **Last modified by**     | The name of the last user who modified the job.                                                                            |
| **Last modified at**     | The date and time when the job was last modified.                                                                          |

## Parameters tab

You can use the **Parameters** tab to define parameters for your jobs.

![Job settings Parameters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-39a7a03416bd8071f57bcf198ab2f0ab32ba43b9%2FPDI_Job%20settings%20Parameters%20tab.png?alt=media)

This table describes all of the general job properties found on the **Parameters** tab:

| Option            | Description                                      |
| ----------------- | ------------------------------------------------ |
| **Parameter**     | A user-defined parameter.                        |
| **Default value** | The default value of the user-defined parameter. |
| **Description**   | A description of the parameter.                  |

## Settings tab

The following options are available on the **Settings** tab:

![Job settings Setttings tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-323dd28d4b49bb66c2f8325477f3daf0221a6a7d%2FPDI_Job%20settings%20Settings%20tab.png?alt=media)

| Option                  | Description                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pass batch ID?**      | Select to pass the identification number of the batch to the transformation.                                                                                                                                                          |
| **Shared objects file** | PDI uses a single shared objects file for each user. The default filename is `shared.xml` and is located in the `.kettle` directory in the user’s home directory. You can define a different shared objects file, location, and name. |

## Log tab

Use the **Log** tab to specify logging settings.

![Job settings Log tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-50cb3c4a2d0d97739ff9da962c4cb50137d2949a%2FPDI_Job%20settings%20Log%20tab.png?alt=media)

This table describes all of the general job properties found on the **Log** tab:

| Option                         | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Log connection**             | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                          |
| **Log Schema**                 | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                     |
| **Log table**                  | Specify the name of the log table. f you are also using transformation logging, you must use a different table name for job logging.                                                                                                                                                                                                                                                        |
| **Logging interval (seconds)** | Specify the interval in which logs are written to the table. This property only applies to Transformation and Performance logging types.                                                                                                                                                                                                                                                    |
| **Log line timeout (days)**    | <p>Specify the number of days to keep log entries in the table before they are deleted. This property only applies to Transformation and Performance logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> for best practice information.</p> |
| **Log size limit in lines**    | Enter the limit for the number of lines that are stored in the `LOG_FIELD`. PDI stores logging for the transformation in a long text field (CLOB). This property only applies to Transformation and Performance logging types.                                                                                                                                                              |
| **SQL button**                 | Generates the SQL needed to create the logging table and allows you to execute this SQL statement.                                                                                                                                                                                                                                                                                          |

## Transactions tab

The **Transaction** tab has one option:

![Job settings Transactions tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a32cd9acbd584d53d8f7618fc0620de2635c17af%2FPDI_Job%20settings%20Transactions%20tab.png?alt=media)

| Option                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Make the job database transactional** | <p>You can use this property to open one unique connection per defined and used database connection in the job. Enabling this option is required to allow a failed job to be completely rolled back. See also the option within <a href="../work-with-transformations-cp">Work with transformations</a>.</p><p>Further information can be found in <a href="https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/386803253/Database+transactions+in+jobs+and+transformations">Database transactions in jobs and transformations</a>.</p> |
