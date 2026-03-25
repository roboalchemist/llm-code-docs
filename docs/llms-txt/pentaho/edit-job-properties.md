# Source: https://docs.pentaho.com/pba/pipeline-designer/working-with-jobs/edit-job-properties.md

# Source: https://docs.pentaho.com/pdia-data-integration/pipeline-designer/working-with-jobs/edit-job-properties.md

# Edit job properties

\
Edit job properties
-------------------

Job properties control how a job behaves and how it logs what it is doing.To configure job properties, complete the following steps:Log into the Pentaho User Console.Open Pipeline Designer:If you are using the Modern Design, in the menu on the left side of the page, click Pipeline Designer.If you are using the Classic Design, click Switch to the Modern Design, and then in the menu on the left side of the page, click Pipeline Designer.Pipeline Designer opens with the Quick Access section expanded.In the table at the bottom of the screen, select either the Recently opened or Favorites tab.Open the job:Search for or browse to the job, and then click Open.Click Open files, and then in the Select File or Directory dialog box, search for or browse to the job and click Open.In the Canvas Action toolbar, click the Settings icon. The Job Properties window opens.Configure the properties in each tab. To learn more about the properties in each tab, see theJob propertiesin this topic.To generate the SQL code necessary for creating the logging table, take following actions:Click SQL. The Simple SQL editor opens with DDL (Data Definition Language) generated from the properties of the job.(Optional) Edit the SQL statements. For details, seeUse the SQL Editor.(Optional) To remove stored query results, metadata, or temporary data that the editor has cached from previous SQL executions, click Clear cache.Click Execute. The SQL statements run.Click Save. The job properties are saved.Job propertiesThe following sections provide a detailed description of the available settings in the Job Properties window:Job tabParameters tabSettings tabLog tabTransactions tabJob tabGeneral properties for jobs are found on the Job tab.This table describes all of the general job properties found on the Job tab:Job NameThe name of the job.Note: This information is required if you want to save to a repository.Job filenameThe file name of the job if it is not stored in the repository.DescriptionA user-defined short description of the job which is shown in the repository explorer.Extended descriptionA user-defined longer description of the job.StatusThe status of the job. The values are draft and production.VersionA description of the version.DirectoryThe directory in the repository where the job is kept.Created byThe original creator of the job.Created atThe date and time when the job was created.Last modified byThe name of the last user who modified the job.Last modified atThe date and time when the job was last modified.Parameters tabYou can use the Parameters tab to define parameters for your jobs.This table describes all of the general job properties found on the Parameters tab:

|                   |                                                  |
| ----------------- | ------------------------------------------------ |
| **Parameter**     | A user-defined parameter.                        |
| **Default value** | The default value of the user-defined parameter. |
| **Description**   | A description of the parameter.                  |

#### Settings tab <a href="#settings-tab" id="settings-tab"></a>

The following options are available on the **Settings** tab:

|                         |                                                                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pass batch ID?**      | Select to pass the identification number of the batch to the transformation.                                                                                                                                                          |
| **Shared objects file** | PDI uses a single shared objects file for each user. The default filename is `shared.xml` and is located in the `.kettle` directory in the user’s home directory. You can define a different shared objects file, location, and name. |

#### Logging tab <a href="#logging-tab" id="logging-tab"></a>

Use the **Logging** tab to specify logging settings.This table describes all of the general job properties found on the **Log** tab:

|                                |                                                                                                                                                                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Log connection**             | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                             |
| **Log Schema**                 | Specify the schema name, if supported by your database.                                                                                                                                                                        |
| **Log table**                  | Specify the name of the log table. f you are also using transformation logging, you must use a different table name for job logging.                                                                                           |
| **Logging interval (seconds)** | Specify the interval in which logs are written to the table. This property only applies to Transformation and Performance logging types.                                                                                       |
| **Log line timeout (days)**    | Specify the number of days to keep log entries in the table before they are deleted. This property only applies to Transformation and Performance logging types.                                                               |
| **Log size limit in lines**    | Enter the limit for the number of lines that are stored in the `LOG_FIELD`. PDI stores logging for the transformation in a long text field (CLOB). This property only applies to Transformation and Performance logging types. |
| **SQL button**                 | Generates the SQL needed to create the logging table and allows you to execute this SQL statement.                                                                                                                             |
