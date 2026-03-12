# Source: https://docs.pentaho.com/pba/pipeline-designer/working-with-transformations/edit-transformation-properties.md

# Edit transformation properties

Transformation properties describe the transformation and control its behavior. You can use transformation properties to customize the processing of your data to achieve the desired output.

To edit transformation properties, complete the following steps:

1. Log into the Pentaho User Console.

2. Open **Pipeline Designer**:&#x20;

   * If you are using the **Modern Design**, in the menu on the left side of the page, click **Pipeline Designer**.&#x20;
   * If you are using the **Classic Design**, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Pipeline Designer**.&#x20;

   **Pipeline Designer** opens with the **Quick Access** section expanded.

3. In the table at the bottom of the screen, select either the **Recently opened** or **Favorites** tab.

4. Open the transformation:&#x20;
   1. Search for or browse to the transformation, and then click **Open**.
   2. Click **Open files**, and then in the **Select File or Directory** dialog box, search for or browse to the transformation and click **Open**.

5. In the **Canvas Action** toolbar, click the **Settings** icon. The **Transformation Properties** window opens.

6. Edit the properties in each tab. To learn more about the properties in each tab, see the [Transformation properties](#transformation-properties) in this topic.

7. After updating options in the **Logging** tab, generate the SQL code necessary for creating the logging table by completing the following steps:

   1. Click **SQL**. One of the following results happens, depending on whether the table is new or existing:
      * If the logging table does not exist, the **Simple SQL editor** opens and displays the DDL (Data Definition Language) generated for the table based on the properties of the transformation.
      * If the logging table exists and you have updated options in the **Logging** tab, the **Simple SQL editor** opens and displays information about the table.

        **Note:** If you do not update the options in the logging tab, the **Simple SQL editor** does not open.
   2. (Optional) Edit the SQL statements. For details, see [Use the SQL Editor](https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/use-the-sql-editor).
   3. (Optional) To remove stored query results, metadata, or temporary data that the editor has cached from previous SQL executions, click **Clear cache**.
   4. Click **Execute**. The SQL statements run.

8. Click **Save**. The transformation properties are saved.

## Transformation properties

The following sections provide a detailed description of the available settings in the Transformation Properties window:

* [Transformation tab](#transformation-tab)
* [Parameters tab](#parameters-tab)
* [Logging tab](#logging-tab)
* [Dates tab](#dates-tab)
* [Dependencies tab](#dependencies-tab)
* [Miscellaneous tab](#miscellaneous-tab)
* [Monitoring tab](#monitoring-tab)

### Transformation tab

Use the **Transformation** tab to specify general properties about the transformation.

This tab includes the following options:

| Property                | Description                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| Transformation name     | The name of the transformation. This field is required to save the settings to a repository. |
| Transformation filename | The file name (\*.ktr) of the transformation.                                                |
| Description             | Short description of the transformation which displays in the repository explorer.           |
| Extended description    | Long extended description of the transformation.                                             |
| Status                  | Draft or production status                                                                   |
| Version                 | Version description                                                                          |
| Directory               | The directory in the repository where the transformation is stored.                          |
| Created by              | Name of the original creator of the transformation.                                          |
| Created at              | Date and time when the transformation was created.                                           |
| Last modified by        | The username of the last user that modified the transformation.                              |
| Last modified at        | Date and time when the transformation was last modified.                                     |

### Parameters tab

Use the **Parameters** tab to add parameters to customize your transformation.

This tab includes the following options:

| Property      | Description                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------- |
| Parameter     | Acts as a local variable that can be shared across all steps in an individual transformation. |
| Default Value | Value that is used if the parameter is not set somewhere else in the transformation.          |
| Description   | Description of the user-defined parameter.                                                    |

### Logging tab

Use the **Logging** tab to configure how and where logging information is captured.&#x20;

In the left navigation pane, select which type of logging you want to use. This tab includes the following options:

| Property                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Log Connection               | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Log table schema             | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Log table name               | Specifies the name of the log table. **Note:** If you are also using job logging, use a different table name for Transformation logging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Logging interval (seconds)   | Specify the interval in which logs are written to the table. This property only applies to Transformation and Performance logging types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Log record timeout (in days) | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>This property only applies to Transformation and Performance logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="https://app.gitbook.com/s/YwnJ6Fexn4LZwKRHghPK/data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p>                                                                                                                                                                       |
| Log size limit (in lines)    | <p>Enter the limit for the number of lines that are stored in the LOG\_FIELD. PDI stores logging for the transformation in a long text field (CLOB).</p><p>This property only applies to the Transformation logging type.</p>                                                                                                                                                                                                                                                                                                                                                                                                       |
| Fields to log                | <p></p><p>Select the fields you want to log in the <strong>Fields to log</strong> pane.</p><p><strong>Notes:</strong></p><ul><li>For effective deletion of expired logs, the <strong>LOGDATE</strong> and <strong>TRANSNAME</strong> fields in the Fields to log pane are enabled by default.</li><li>Monitoring the <strong>LOG\_FIELD</strong> field can negatively impact Pentaho Server performance. However, if you do not select all fields, including <strong>LOG\_FIELD</strong>, when configuring transformation logging, you will not see information about this transformation in the Operations Mart logging.</li></ul> |

### Dates tab

Use the **Dates** tab to configure date ranges and limits for this connection.

This tab includes the following options:

| Property                          | Description                                                                                                                                                                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maxdate connection                | Get the upper limit for a date range on this connection.                                                                                                                                                                                                                     |
| Maxdate table                     | Get the upper limit for a date range in this table.                                                                                                                                                                                                                          |
| Maxdate field                     | Get the upper limit for a date range in this field.                                                                                                                                                                                                                          |
| Maxdate offset (seconds)          | Increases the upper date limit with this amount. Use this for example, if you find that the field DATE\_LAST\_UPD has a maximum value of 2004-05-29 23:00:00, but you know that the values for the last minute are not complete. In this case, simply set the offset to -60. |
| Maximum date difference (seconds) | Sets the maximum date difference in the obtained date range. This will allow you to limit job sizes.                                                                                                                                                                         |

### Dependencies tab

Use the **Dependencies** tab to specify all of the dependencies for the transformation.

The **Dependencies** tab allows you to enter all of the dependencies for the transformation. For example, if a dimension depends on three lookup tables, make sure that the lookup tables have not changed. If the values in these lookup tables have changed, extend the date range to force a full refresh of the dimension.

Dependencies allow you to determine if a table has changed when you have a "data last changed" column in the table. Click **Get dependencies** to detect dependencies automatically.

| Property   | Description                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------- |
| Connection | A dropdown to select a database connection that has already been created for that transformation. |
| Table      | A specific table from the selected database connection.                                           |
| Field      | A specific field within the selected table.                                                       |

### Miscellaneous tab

Use the **Miscellaneous** tab to configure buffer and feedback size and performing various administrative tasks.

This tab includes the following options:

| Property                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of rows in rowset                       | Allows you to change the size of the buffers between the connected steps in a transformation. Do not change this parameter unless you are running low on memory, for example.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Show a feedback row in transformation steps?   | Controls whether or not to add a feedback entry into the log file while the transformation is being executed. By default, this feature is enabled and configured to display a feedback record every 5000 rows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The feedback size                              | Sets the number of rows to process before entering a feedback entry into the log. Set this higher when processing large amounts of data to reduce the amount of information in the log file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Make the transformation database transactional | <p>This allows you to open one unique connection per defined and used database connection in the transformation. Enabling this option is required to allow a failed transformation to be completely rolled back.</p><p>Enabling this option is also necessary when trying to alter connection settings before a query using an "Execute SQL script" step. (See also the <strong>Advanced</strong> section in the Database Connection dialog box "Enter the SQL statements (separated ...) to execute right after connecting")</p><p>Further information can be found in <a href="https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/386803253/Database+transactions+in+jobs+and+transformations">Database transactions in jobs and transformations</a>.</p><p><strong>Note:</strong> A transformation wide commit for all steps is done when the last step finishes. When the transformation fails, a rollback is done. It is not necessary to set any commit sizes since they are ignored.</p> |
| Shared objects file                            | Specifies the location of the XML file used to store shared objects like database connections, clustering schemas, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Manage thread priorities?                      | Allows you to enable or disable the internal logic for changing the Java thread priorities based on the number of input and output rows in the "rowset" buffers. This can be useful in some situations where the cost of using the logic exceeds the benefit of the thread prioritization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Monitoring tab

Use the **Monitoring** tab for enabling and disabling step performance monitoring and setting related performance parameters.

This tab includes the following options:

| Property                                   | Description                                                                                                                                                                                                                                                                                 |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable step performance monitoring?        | This activates performance monitoring for transformation steps. It shows how many rows of data are being written, read, inputted, or outputted for each step. These metrics can be viewed on the **Performance Graph** tab that’s part of the **Execution Results** panel below the canvas. |
| Step performance measurement interval (ms) | This is the interval in milliseconds used to take a snapshot. Example: 10 ms                                                                                                                                                                                                                |
| Maximum number of snapshots in memory      | Sets the maximum number of measurement snapshots that can be held in memory during runtime.                                                                                                                                                                                                 |
