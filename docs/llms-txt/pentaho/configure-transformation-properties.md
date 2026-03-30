# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/configure-transformation-properties.md

# Configure transformation properties

Transformation properties are a collection of properties that describe the transformation and configure its behavior. You can use transformation properties to customize the processing of your data to achieve the desired output.

To view the transformation properties, click CTRLT or right-click on the canvas and select **Properties** from the menu that appears.. The following sections provide a detailed description of the available settings:

* [Transformation tab](#transformation-tab)
* [Parameters tab](#parameters-tab)
* [Logging tab](#logging-tab)
* [Dates tab](#dates-tab)
* [Dependencies tab](#dependencies-tab)
* [Miscellaneous tab](#miscellaneous-tab)
* [Monitoring tab](#monitoring-tab)

After you have adjusted your settings, click SQL to generate the SQL code necessary for creating the logging table. The Data Definition Language (DDL) displays in the Simple SQL Editor allowing you to execute this or any other SQL statements against the logging connection. For information on how to use the SQL Editor, see [Use the SQL Editor](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-sql-editor).

## Transformation tab

Use the **Transformation** tab to specify general properties about the transformation.

![Transformation properties - Transformation tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-86a4a8563f52c325ae236ec945d185ece7f44acc%2FPDI_TransProperties_Transformation_Tab.png?alt=media)

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

## Parameters tab

Use the **Parameters** tab to add parameters to customize your transformation.

![Transformation properties - Parameters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f224d576d3c7cb7de698e26f0570292511675fef%2FPDI_TransProperties_Parameters_Tab.png?alt=media)

This tab includes the following options:

| Property      | Description                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------- |
| Parameter     | Acts as a local variable that can be shared across all steps in an individual transformation. |
| Default Value | Value that is used if the parameter is not set somewhere else in the transformation.          |
| Description   | Description of the user-defined parameter.                                                    |

## Logging tab

Use the **Logging** tab to configure how and where logging information is captured. For more information about how to configure transformation logging, see [Set up transformation logging](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-transformation-logging).

![Transformation properties - Logging tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9758780f23f1ae52bb686b337aeef504b3164c78%2FPDI_TransProperties_Logging_Tab.png?alt=media)

In the left navigation pane, select which type of logging you want to use. This tab includes the following options:

| Property                     | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Log Connection               | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                                                   |
| Log table schema             | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                                              |
| Log table name               | Specifies the name of the log table. **Note:** If you are also using job logging, use a different table name for Transformation logging.                                                                                                                                                                                                                                                                             |
| Logging interval (seconds)   | Specify the interval in which logs are written to the table. This property only applies to Transformation and Performance logging types.                                                                                                                                                                                                                                                                             |
| Log record timeout (in days) | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>This property only applies to Transformation and Performance logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p> |
| Log size limit (in lines)    | <p>Enter the limit for the number of lines that are stored in the LOG\_FIELD. PDI stores logging for the transformation in a long text field (CLOB).</p><p>This property only applies to the Transformation logging type.</p>                                                                                                                                                                                        |
| Fields to log                | Select the fields you want to log in the **Fields to log** pane.                                                                                                                                                                                                                                                                                                                                                     |

## Dates tab

Use the **Dates** tab to configure date ranges and limits for this connection.

![Transformation properties - Dates tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c6c4da9717dd4a46d018802738e8d0d1ba6d6664%2FPDI_TransProperties_Dates_Tab.png?alt=media)

This tab includes the following options:

| Property                          | Description                                                                                                                                                                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maxdate connection                | Get the upper limit for a date range on this connection.                                                                                                                                                                                                                     |
| Maxdate table                     | Get the upper limit for a date range in this table.                                                                                                                                                                                                                          |
| Maxdate field                     | Get the upper limit for a date range in this field.                                                                                                                                                                                                                          |
| Maxdate offset (seconds)          | Increases the upper date limit with this amount. Use this for example, if you find that the field DATE\_LAST\_UPD has a maximum value of 2004-05-29 23:00:00, but you know that the values for the last minute are not complete. In this case, simply set the offset to -60. |
| Maximum date difference (seconds) | Sets the maximum date difference in the obtained date range. This will allow you to limit job sizes.                                                                                                                                                                         |

## Dependencies tab

Use the **Dependencies** tab to specify all of the dependencies for the transformation.

![Transformation properties - Dependencies tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-282d42f007d185b78563a6c45aadfb98b9be33a2%2FPDI_TransProperties_Dependencies_Tab.png?alt=media)

The **Dependencies** tab allows you to enter all of the dependencies for the transformation. For example, if a dimension depends on three lookup tables, make sure that the lookup tables have not changed. If the values in these lookup tables have changed, extend the date range to force a full refresh of the dimension.

Dependencies allow you to determine if a table has changed when you have a "data last changed" column in the table. Click **Get dependencies** to detect dependencies automatically.

| Property   | Description                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------- |
| Connection | A dropdown to select a database connection that has already been created for that transformation. |
| Table      | A specific table from the selected database connection.                                           |
| Field      | A specific field within the selected table.                                                       |

## Miscellaneous tab

Use the **Miscellaneous** tab to configure buffer and feedback size and performing various administrative tasks.

![Transformation properties - Miscellaneous tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9cfadd695082206af01019a8fa243fed422d61ae%2FPDI_TransProperties_Miscellaneous_Tab.png?alt=media)

This tab includes the following options:

| Property                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of rows in rowset                       | Allows you to change the size of the buffers between the connected steps in a transformation. Do not change this parameter unless you are running low on memory, for example.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Show a feedback row in transformation steps?   | Controls whether or not to add a feedback entry into the log file while the transformation is being executed. By default, this feature is enabled and configured to display a feedback record every 5000 rows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The feedback size                              | Sets the number of rows to process before entering a feedback entry into the log. Set this higher when processing large amounts of data to reduce the amount of information in the log file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Make the transformation database transactional | <p>This allows you to open one unique connection per defined and used database connection in the transformation. Enabling this option is required to allow a failed transformation to be completely rolled back.</p><p>Enabling this option is also necessary when trying to alter connection settings before a query using an "Execute SQL script" step. (See also the <strong>Advanced</strong> section in the Database Connection dialog box "Enter the SQL statements (separated ...) to execute right after connecting")</p><p>Further information can be found in <a href="https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/386803253/Database+transactions+in+jobs+and+transformations">Database transactions in jobs and transformations</a>.</p><p><strong>Note:</strong> A transformation wide commit for all steps is done when the last step finishes. When the transformation fails, a rollback is done. It is not necessary to set any commit sizes since they are ignored.</p> |
| Shared objects file                            | Specifies the location of the XML file used to store shared objects like database connections, clustering schemas, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Manage thread priorities?                      | Allows you to enable or disable the internal logic for changing the Java thread priorities based on the number of input and output rows in the "rowset" buffers. This can be useful in some situations where the cost of using the logic exceeds the benefit of the thread prioritization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Monitoring tab

Use the **Monitoring** tab for enabling and disabling step performance monitoring and setting related performance parameters.

![Transformation properties - Monitoring tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-48dd3607a1f75b6d004f274eeed6966fa4dbaeb8%2FPDI_TransProperties_Monitoring_Tab.png?alt=media)

This tab includes the following options:

| Property                                   | Description                                                                                                                                                                                                                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Enable step performance monitoring?        | This activates performance monitoring for transformation steps. It shows how many rows of data are being written, read, inputted, or outputted for each step. These metrics can be viewed on the **Performance Graph** tab that’s part of the**Execution Results** panel below the canvas. |
| Step performance measurement interval (ms) | This is the interval in milliseconds used to take a snapshot. Example: 10 ms                                                                                                                                                                                                               |
| Maximum number of snapshots in memory      | Sets the maximum number of measurement snapshots that can be held in memory during runtime.                                                                                                                                                                                                |
