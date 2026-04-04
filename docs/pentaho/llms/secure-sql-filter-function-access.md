# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/secure-sql-filter-function-access.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/secure-sql-filter-function-access.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/secure-sql-filter-function-access.md

# Secure SQL filter function access

The Dashboard Designer has a SQL filter for greater control over a database query. By default, this feature is restricted to administrative users.

Perform the following steps to change these settings:

1. Ensure the Pentaho Server is not currently running; if it is, run the `stop-pentaho` script.
2. Open the `/pentaho-solutions/system/dashboards/settings.xml` file with a text editor.
3. Locate the following line and modify it accordingly:

   ```xml
   <!-- roles with sql execute permissions -->
   <sql-execute-roles>Administrator</sql-execute-roles>
   ```

   **Note:** Values are separated by commas, with no spaces between roles.
4. Locate the following line and modify it accordingly:

   ```xml
   <!-- users with sql execute permissions -->
   <sql-execute-users>Administrator</sql-execute-users>
   ```

   **Note:** Values are separated by commas, with no spaces between user names.
5. Save and close the text editor.
6. Restart the Pentaho Server with the `start-pentaho` script.

The SQL filter function is now available in Dashboard Designer to the users and roles you specified.
