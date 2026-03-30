# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/build-large-reports/distinct-values-build-large-reports-in-pir.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-interactive-reports-cp/build-large-reports/distinct-values-build-large-reports-in-pir.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/build-large-reports/distinct-values-build-large-reports-in-pir.md

# Distinct values

By default, Interactive Reports queries data with the SQL `SELECT DISTINCT` statement when no `GROUP BY` is used in the SQL query. This SQL statement returns only distinct (different) values, which may require an extensive sorting operation in the database. To stop the query from returning distinct values, clear the **Select Distinct** option in the Query Settings dialog box. Your setting of the **Select Distinct** option is saved with your report. For example, if you clear **Select Distinct** then save and close your report, this option will be cleared when you reopen the report.

**Note:** If you are logged in as an administrator, you can right click on the toolbar and select **View SQL** to verify if `DISTINCT` is a part of the SQL statement.

If you want to clear the **Select Distinct** option by default for new reports, ask your system administrator to review the **Administer Pentaho Data Integration and Analytics** document for further information.
