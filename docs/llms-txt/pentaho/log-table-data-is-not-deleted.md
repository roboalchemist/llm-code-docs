# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/log-table-data-is-not-deleted.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/log-table-data-is-not-deleted.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/log-table-data-is-not-deleted.md

# Log table data is not deleted

When you run a job or transformation, data in the log table is not deleted as expected:

* When a job runs, the value in the **Log line timeout (days)** field, along with the **LOGDATE** and **JOBNAME** or **TRANSNAME** fields, which are selected in the **Log table field** pane, determine when to delete the data in the log table. These fields are in the Job properties window in PDI. See [Set up job logging](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-job-logging) for details.
* When a transformation runs, the value in the **Log record timeout (in days)** field, along with the **LOGDATE** and **TRANSNAME** fields, which are selected in the **Fields to log** pane, determine when to delete the data in the log table. These fields are in the Transformation properties window in PDI. See [Set up transformation logging](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-transformation-logging) for details.

If the name of an existing job or transformation is changed, then any log table entries with the previous name are no longer recognized and are no longer deleted from the table when the **Log line timeout (days)** or the **Log record timeout (in days)** value is present.

If you find that your log table is becoming too large, you should manually purge these unrecognized log table rows using your SQL editor.
