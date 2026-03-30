# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/set-system-max-row-limit-for-interactive-reports.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/set-system-max-row-limit-for-interactive-reports.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/set-system-max-row-limit-for-interactive-reports.md

# Set system max row limit for Interactive Reports

You can prevent too many resources from hitting your database server at once by setting a system-wide maximum row-limit for Pentaho Interactive Reports. Your users can still define their own design-time row limits in Interactive Reports, but they will never be able to go over the maximum number of rows that you have specified while designing their reports.

1. Shut down the Pentaho Server.
2. Locate the `/pentaho-server/pentaho-solutions/system/pentaho-interactive-reporting` directory.
3. Open the `settings.xml` file with any text editor.
4. Find the `<query-limit>` tag and change the default number of 100000 within the tags to the maximum number of rows desired.

   ```xml
   <!-- The maximum number of rows that will be rendered in a report on PIR edit and
   view mode. A zero value means no limit. -->
   <query-limit>100000</query-limit>
   ```
5. Save and close the `settings.xml` file.
6. Start the Pentaho Server.

If you are migrating content from a previous version, you will need to add the `<query-limit>` tag to your `settings.xml` for Interactive Reports.

## Roll back system max row limit

These instructions show you how to return the system maximum row limit to the Pentaho 5.3 settings.

1. Shut down the Pentaho Server.
2. Locate the `/pentaho-server/pentaho-solutions/system/pentaho-interactive-reporting` directory.
3. Open the `settings.xml` file with any text editor.
   1. To change the maximum number of rows that will be rendered in Pentaho Interactive Reports in edit or view mode, find the `<design-query-limit>` tag and change the default number of 500 back to `25`.

      FROM:

      ```xml
      <design-query-limit>500</design-query-limit>
      ```

      TO:

      ```
      <design-query-limit>25</design-query-limit>
      ```
   2. To turn the `design-query-limit` to be OFF by default, find the `<design-query-limit-enabled>` tags and change the value to `false`.

      ```xml
      <design-query-limit-enabled>false</design-query-limit-enabled>
      ```
4. Save and close the `settings.xml` file.
5. Restart the server.
