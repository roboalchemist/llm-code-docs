# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/set-default-select-distinct-for-interactive-reports.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/set-default-select-distinct-for-interactive-reports.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/set-default-select-distinct-for-interactive-reports.md

# Set default SELECT DISTINCT for Interactive Reports

By default, Interactive Reports queries data with the SQL `SELECT DISTINCT` statement to return only distinct (different) data values, which may require an extensive sorting operation in the database. If you want to reduce the cost of a system-wide sorting operation, you can set new reports to open with the **Select Distinct** option cleared.

Perform the following steps to change the default setting of the **Select Distinct** option in the **Query Setting** dialog box of new Interactive Reports:

1. Stop the Pentaho Server.
2. Locate the `server/pentaho-server/pentaho-solutions/system/pentaho-interactive-reporting` directory.
3. Open the `settings.xml` file with any text editor.
4. Find the `<default-select-distinct>` tag and change it to the desired setting.

   If you want the **Select Distinct** option cleared as the default, set the `<default-select-distinct>` tag to `false` as shown in the following example code:

   ```xml
   <!--  default select-distinct setting for a new report -->
   <default-select-distinct>false</default-select-distinct>
   ```
5. Save and close the `settings.xml` file.
6. Start the Pentaho Server.
