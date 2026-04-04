# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-transformation-logging.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-transformation-logging.md

# Set up transformation logging

Follow the instructions below to create a log table that keeps a history of information associated with your field information.

1. Ask your system administrator to create a database or table space called `PdiLog`.
2. Right-click in the workspace (canvas) where you have an open transformation and select **Properties**, or press CTRL T.

   The Transformation properties dialog box appears.

   ![Transformation properties dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7ebaea9efbe698b707752080accbf6a884544fcb%2FPDI_TransformationProperties_Dialog.png?alt=media)
3. In the Transformation properties dialog box, click the **Logging** tab. In the left-side navigation pane, select which type of logging you want to use.

   ![Logging tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-927a40271d52442bf30caac47dc60e6842375796%2FPDI_TransformationProperties_Dialog_Log.png?alt=media)
4. In the **Logging** tab, enter the following information.

| Option                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Log Connection**               | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                                                                                     |
| **Log table schema**             | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Log table name**               | <p>Specify the name of the log table.</p><p><strong>Note:</strong> If you are also using job logging, use a different table name for transformation logging.</p>                                                                                                                                                                                                                                                                                       |
| **Logging interval (seconds)**   | <p>Specify the interval in which logs are written to the table.</p><p>This property only applies to <strong>Transformation</strong> and <strong>Performance</strong> logging types.</p>                                                                                                                                                                                                                                                                |
| **Log record timeout (in days)** | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>This property only applies to <strong>Transformation</strong> and <strong>Performance</strong> logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p> |
| **Log size limit in lines**      | <p>Enter the limit for the number of lines that are stored in the <strong>LOG\_FIELD</strong>. PDI stores logging for the transformation in a long text field (CLOB).</p><p>This property only applies to the <strong>Transformation</strong> logging type.</p>                                                                                                                                                                                        |

5\. Select the fields you want to log in the \*\*Fields to log\*\* pane, or keep the default selections.

```
**Note:** For effective deletion of expired logs, the **LOGDATE** and **TRANSNAME** fields in the **Fields to log** pane are enabled by default.
```

6\. Click the **SQL** button.

```
PDI checks the log table.
```

7\. If the Simple SQL editor opens, go to step 8. Otherwise, proceed to step 10.

8. Verify your table name, field selections and indices in the Simple SQL editor, and then click **Execute** to create your log table.

   PDI creates or revises the table and displays the results in the Results dialog box.
9. Click **OK** to exit the Results dialog box. Click **Close** to exit the Simple SQL editor.
10. Click **OK** to exit the Transformation properties dialog box.

The next time you run your transformation, logging information will appear under the **Execution History** tab.

**Note:** Monitoring the **LOG\_FIELD** field can negatively impact Pentaho Server performance. However, if you do not select all fields, including **LOG\_FIELD**, when configuring transformation logging, you will not see information about this transformation in the Operations Mart logging.
