# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/business-analytics-operations-mart.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/business-analytics-operations-mart.md

# Business Analytics Operations Mart

Pentaho automatically sets up a way for using the Operations Mart and Analyzer, Interactive Reports, Report Designer, and Dashboards. The Business Analytics (BA) Operations Mart aggregates data from the Pentaho Server log files into pre-built audit reports that provide information you might need.

If these reports do not meet your needs, you can use [Data Integration Operations Mart](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart) to change them.

## Download and install Operations Mart files

Operation Mart files are stored in a pre-packaged ZIP file. To install the files, you must stop the Pentaho Server, download and unpack the ZIP file, and then restart the Pentaho Server to import the files.

1. Stop the Pentaho Server.

   **Note:** See the **Install Pentaho Data Integration and Analytics** document for instructions on stopping and starting the Pentaho Server.
2. Download the `pentaho-operations-mart-10.2.0.0-<build number>.zip` file from the [Support Portal](https://support.pentaho.com/hc/en-us).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **10.x** list, click **Pentaho 10.2 GA Release**.
   4. Scroll to the bottom of the Pentaho 10.2 GA Release page.
   5. In the file component section, click the `Operations Mart` folder.
   6. Download the `pentaho-operations-mart-10.2.0.0-<build number>.zip` file.
3. Unpack the `pentaho-operations-mart-10.2.0.0-<build number>.zip` file in a temporary directory.
4. Move the unpacked files to the `pentaho/server/pentaho-server/pentaho-solutions/system/default-content` directory.
5. In the `default-content` directory, delete any files that you don't need for the repository database type.

   The following table lists the files to keep for each type of Pentaho Repository database.

| Repository database type                                                                                                                                                                                                                                                              | Files to keep                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PostgresSQL                                                                                                                                                                                                                                                                           | <ul><li><code>pentaho-operations-mart-clean-10.2.0.0-\<build number>.zip</code> \*</li><li><code>pentaho-operations-mart-etl-10.2.0.0-\<build number>.zip</code></li><li><code>​pentaho-operations-mart-operations-bi-10.2.0.0-\<build number>.zip</code></li></ul>                    |
| MySQL                                                                                                                                                                                                                                                                                 | <ul><li><code>pentaho-operations-mart-clean-mysql5-10.2.0.0-\<build number>.zip</code> \*</li><li><code>pentaho-operations-mart-etl-mysql5-10.2.0.0-\<build number>.zip</code></li><li>​<code>pentaho-operations-mart-operations-bi-10.2.0.0-\<build number>.zip</code></li></ul>      |
| Oracle                                                                                                                                                                                                                                                                                | <ul><li><code>pentaho-operations-mart-clean-oracle10g-10.2.0.0-\<build number>.zip</code>\*</li><li><code>pentaho-operations-mart-etl-oracle10g-10.2.0.0-\<build number>.zip</code></li><li><code>​pentaho-operations-mart-operations-bi-10.2.0.0-\<build number>.zip</code></li></ul> |
| MS SQL Server                                                                                                                                                                                                                                                                         | <ul><li><code>pentaho-operations-mart-clean-mssql-10.2.0.0-\<build number>.zip</code> \*</li><li><code>pentaho-operations-mart-etl-mssql-10.2.0.0-\<build number>.zip</code></li><li><code>​pentaho-operations-mart-operations-bi-10.2.0.0-\<build number>.zip</code></li></ul>        |
| \* Keep the `pentaho-operations-mart-clean-<database>-10.2.0.0-<build number>.zip` file only if you plan for Pentaho to automatically delete entries from the operations mart on a regular schedule. For more information, see [Clean up Operations Mart](#clean-up-operations-mart). |                                                                                                                                                                                                                                                                                        |

6\. Restart the Pentaho Server.

The Operations Mart is ready to be used.

## Increase the maximum character length in audit table fields

You can increase the maximum number of characters permitted in an audit table field from 200 to 1024 characters.

**Note:** The scripts in the following procedure adjust the column width and re-index the Operations Mart tables.

Complete the following steps to increase the maximum number of characters:

1. Stop the Pentaho Server.

   **Note:** See the **Install Pentaho Data Integration and Analytics** document for instructions on stopping and starting the Pentaho Server.
2. Download the `pentaho-server-ee-10.2.0.0-<build number>.zip` file from the [Support Portal](https://support.pentaho.com/home).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **10.x** list, click **Pentaho 10.2 GA Release**.
   4. Scroll to the bottom of the Pentaho 10.2 GA Release page.
   5. In the file component section, navigate to the `Pentaho Server/Archive Build (Suggested Installation Method)` folder.
   6. Download the `pentaho-server-ee-10.2.0.0-<build number>.zip` file.
3. Unpack the `pentaho-server-ee-10.2.0.0-<build number>.zip` file in a temporary directory.
4. In the temporary directory, navigate to `pentaho\server\pentaho-server\data` directory.
5. In the `data` directory, navigate to the directory for your repository database type.
   * `mysql`
   * `oracle`
   * `postgresql`
   * `sqlserver`
6. In the directory for your repository database type, locate the following files:
   * `alter_script_<repository database type>_BISERVER-13674.sql`
   * `pentaho_mart_upgrade_audit_<repository database type>.sql`
7. Use the SQL client tool for the repository type to run the following scripts, in order:
   1. `alter_script_<repository database type>_BISERVER-13674.sql`
   2. `pentaho_mart_upgrade_audit_<repository database type>.sql`
8. After you run the scripts, delete the temporary directory that you created in the previous step.
9. Start the Pentaho Server.

The maximum field length for audit tables is 1024 characters.

## Choose a pre-built Operations Mart report

We provide pre-built Interactive Reports and a data mart called the Pentaho Operations Mart. The Operations Mart contains all the data from system log files. This table shows the reports that we have pre-built for you. Choose the report that fits your needs and follow the instructions in [View and edit Operations Mart reports](#view-and-edit-operations-mart-reports).

| Information Shown                                                                        | Report Name                            |
| ---------------------------------------------------------------------------------------- | -------------------------------------- |
| Amount of time it takes a report to run                                                  | Content Duration                       |
| File names of all content failures within a defined length of time                       | Content Failures                       |
| Compare login metrics for days within a specified month                                  | Content Request Day of Month           |
| Compare login metrics for a days in a week within a specified year                       | Day of Week Request and Login Metrics  |
| List of content sorted by type, used within a defined length of time                     | Content Type Usage                     |
| List of content usage within a defined length of time                                    | Content Usage                          |
| Compare login metrics by hour for a specified day                                        | Hours in Day Request and Login Metrics |
| Length of time for logins and the number of logins per user for specified length of time | Session Duration Counts                |

## View and edit Operations Mart reports

Perform the following steps to view and edit Operations Mart reports:

1. Identify the report that you want to open from **Choose a Pre-Built Operations Mart Report**.
2. Double-click **Browse Files**.
3. Click on: **public** > **Pentaho Operations Mart** > **BA Audit Reports**
4. Select the appropriate file and click **Open**. Your monitoring and logging data appears in the pre-built report.
5. If you need to edit this report, you can do so from within the opening tool.

See the **Pentaho Business Analytics** document for more information about editing a report in Analyzer or Interactive Reports.

See the **Pentaho Report Designer** document for more information about editing a report using the designer.

See [Data Integration Operations Mart](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart) for more information.

## Create Operations Mart reports

If the reports we provide are not quite right for you, you can create your own reports.

1. From within the User Console, select **Create New** and then choose the type or report you want to create.
2. Select the data source that you need.

   | Information Shown                                                                                                        | Data Source                                                    |
   | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
   | Detail information related to the execution of the .xactions. that run the reports on the Pentaho Server                 | pentaho\_operations\_mart: BA Operations Mart - Component      |
   | Information related to the execution of content , such as which tool or which user ran the content on the Pentaho Server | pentaho\_operations\_mart: BA Operations Mart - Content        |
   | Information for the Pentaho Server related to a user, such as number of sessions, how long, and what time                | pentaho\_operations\_mart: BA Operations Mart - User Session   |
   | Information about individual job entry executions on the Pentaho Server                                                  | pentaho\_operations\_mart: PDI Operations Mart - Job Entry     |
   | Detailed performance information for the Pentaho Server                                                                  | pentaho\_operations\_mart: - PDI Operations Mart - Performance |
   | Detailed information about individual step executions on the Pentaho Server                                              | pentaho\_operations\_mart: PDI Operations Mart - Step          |
   | Information related to transformations and jobs run on the Pentaho Server                                                | pentaho\_operations\_mart: PDI\_Operations\_Mart               |
3. Create a new report as described in the appropriate user section.

See the **Pentaho Business Analytics** document for more information about editing a report in Analyzer or Interactive Reports.

See the **Pentaho Report Designer** document for more information about editing a report using the designer.

## Update the Operations Mart

You may need to update the report date and time, or the data that is populated into the report itself.

1. From within the User Console, select: **Browse Files** > **public** > **Pentaho Operations Mart** > **Update Audit Mart**
2. Double-click either: **Update Operations Mart Date & Time** or **Update BA Operations Mart Data**
3. View a report to confirm that the updates applied.

## Clean up Operations Mart

The operational data in Operations Mart tables are set to automatically remove entries older than 365 days. If you want to change this schedule so that the operational data is deleted using a different time frame, you will need to add a variable, named *ba.cleanup.max.age*, in the `kettle.properties` file located in the `{user.home}/.kettle` directory.

1. Stop the Pentaho Server.
2. Open the `kettle.properties` file located in the administrative user's `{user.home}/.kettle` directory.
3. Add the *ba.cleanup.max.age* variable to indicate the age above which entries are deleted.

   If you want to delete entries that are older than 30 days, add this:

   ```
   ba.cleanup.max.age=30
   ```
4. Save and close the `kettle.properties` file.
5. Restart your Pentaho Server for the setting to take effect.
