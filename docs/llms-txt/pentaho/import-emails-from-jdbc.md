# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/import-emails-from-data-sources/import-emails-from-jdbc.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/import-emails-from-data-sources/import-emails-from-jdbc.md

# Import emails from JDBC

You can import emails from external JDBC tables using the following procedure.

* You need to have administrator privileges to perform this task.
* If using another database than Postgres, a JDBC driver must be added to the `/jdbc-distribution/lib` folder.

1. Navigate to the `/pentaho-server/pentaho-solutions/system/scheduler-plugin` folder.
2. Open the `settings.xml` file and change the `email-source` setting to `jdbc`.
3. Update the file `applicationContext-email-import.properties` by providing JDBC connection and table information.

   In the following properties file, ask your administrator to provide JDBC connection information.

   ```
   # This file is the source for creating the datasource for the jdbcEmailImport bean
   # and its properties structure.
   #
   # Editing of connection info should be done in this file
   #
   # In addition the query is defined here. The datasource.emails-query MUST return the first name,
   # last name, and email in that order.
   #
   # The password are encrypted using Encr utility. Encr.bat and Encr.sh exist along the startup script for the server
   #
   # The jdbc.emails-imported property defines if emails have already been imported. If true
   # then no more emails will be imported. After initial import this property is automatically
   # set to "true". If more imports are done from a different datasource then this property will
   # need to be set back to "false"
   #
   # NOTE: The correct JDBC driver must be in the classpath for this to work.
   jdbc.driver.classname=org.postgresql.Driver
   jdbc.url=jdbc:postgresql://localhost:5432/emailgroups
   jdbc.username=pentaho_user
   jdbc.password=Encrypted 2be98afc86aa7f2e4bb18bd63c99dbdde
   jdbc.validation.query=SELECT 1
   jdbc.max.idle=4
   jdbc.min.idle=0
   jdbc.emails-query=SELECT fname, lname, email FROM public.emails ORDER BY email ASC
   # The above query is an example the actual query will be dependent on the source RDBMS.
   # Field names are table dependent on the table columns that are being imported
   # the ORDER BY clause isn't required. The SELECT statement is very arbitrary but
   # the result set MUST return IN THIS ORDER -> firstName, lastName, email

   ```

   The `jdbc.password` is encrypted using the `encr` utility. This utility is provided along with other startup scripts in the `/server/pentaho-server` folder.
