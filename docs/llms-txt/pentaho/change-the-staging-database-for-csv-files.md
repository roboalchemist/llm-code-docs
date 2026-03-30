# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-staging-database-for-csv-files.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-staging-database-for-csv-files.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-staging-database-for-csv-files.md

# Change the staging database for CSV files

Hibernate is the default staging database for CSV files. Follow these instructions if you want to change the staging database.

1. Go to `/pentaho-solutions/system/data-access` and open the `settings.xml` file with any text editor.
2. Edit the `settings.xml` file as needed.

   The default value is shown in the sample below:

   ```xml
   <!-- settings for Agile Data Access -->
   <data-access-staging-jndi>hibernate</data-access-staging-jndi>
   ```

   This value can be a JNDI name or the name of a Pentaho database connection. See the **Install Pentaho Data Integration and Analytics** document for more information on database connections.
3. Save and close the file.
4. Restart the User Console
