# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-job-logging.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-job-logging.md

# Set up job logging

Follow the instructions below to create a log table that keeps a history of information associated with your job information.

1. Ask your system administrator to create a database or table space called `PdiLog`.
2. Right-click in the workspace (canvas) where you have an open job and select **Properties**, or press CTRL T.

   The Job properties dialog box appears.

   ![Job properties dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-141e9f62d021f6757307649da8c86eb0e3c48607%2FPDI_JobProperties_Dialog.png?alt=media)
3. In the Job properties dialog box, click the **Log** tab. In the left-side navigation pane, select which type of logging you want to use.

   ![Log tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a27cc7c32ce622f6433b73268153ef2e36fbe5e1%2FPDI_JobProperties_Dialog_Log.png?alt=media)
4. In the **Log** tab, enter the following information.

| Option                         | Description                                                                                                                                                                                                                                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Log Connection**             | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                 |
| **Log schema**                 | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                            |
| **Log table**                  | <p>Specify the name of the log table.</p><p><strong>Note:</strong> If you are also using transformation logging, use a different table name for jobs.</p>                                                                                                                                                                          |
| **Logging interval (seconds)** | <p>Specify the interval in which logs are written to the table.</p><p>This property only applies to <strong>Job log table</strong> logging type.</p>                                                                                                                                                                               |
| **Log line timeout (days)**    | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p> |
| **Log size limit in lines**    | <p>Enter the limit for the number of lines that are stored in the <strong>LOG\_FIELD</strong>. PDI stores logging for the job in a long text field (CLOB).</p><p>This property only applies to <strong>Job log table</strong> logging type.</p>                                                                                    |

5\. Select the fields you want to log in the \*\*Log table fields\*\* pane, or keep the default selections.

```
**Note:** For effective deletion of expired logs, the **LOGDATE**, and **JOBNAME** \(or **TRANSNAME**\) fields in the **Log table fields** pane are enabled by default.
```

6\. Click the **SQL** button.

```
PDI checks the log table.
```

7\. If the Simple SQL editor opens, proceed to the next step. If it does not open, go to step 10.

8. Verify your table name, field selections and indices in the Simple SQL editor, and then click **Execute** to create your log table.

   PDI creates or revises the table and displays the results in the Results dialog box.
9. Click **OK** to exit the Results dialog box. Click **Close** to exit the Simple SQL editor.
10. Click **OK** to exit the Job properties dialog box.

The next time you run your job, logging information will appear under the **History** tab.

**Note:** Monitoring the **LOG\_FIELD** field can negatively impact Pentaho Server performance. However, if you do not select all fields, including **LOG\_FIELD**, when configuring transformation logging, you will not see information about this transformation in the Operations Mart logging.
