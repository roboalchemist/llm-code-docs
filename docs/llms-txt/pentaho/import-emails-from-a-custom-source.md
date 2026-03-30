# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/import-emails-from-data-sources/import-emails-from-a-custom-source.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/import-emails-from-data-sources/import-emails-from-a-custom-source.md

# Import emails from a custom source

You can import emails from other data sources into the Pentaho Server using the following procedure. Like any other emails in the Pentaho Repository, the imported emails can be organized in email groups as described in [Create an email group](https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-up-emails-for-scheduled-reports/create-an-email-group).

These instructions create a framework for importing emails from a CSV file.

The `pentaho-scheduler-ee-core-10.x.x.jar` file must be included in the project or resolved by using a Maven Project Object Model (POM) to ensure access to `AbstractEmailImportService` in the following procedure. If you are using a reference from a POM, it should be marked as `<scope>PROVIDED</scope>`, since it can be found in the plugin itself.

The `pentaho-scheduler-ee-core-10.x.x.jar` is included with the Scheduler plugin and is located in the `server/pentaho-server/pentaho-solutions/system/scheduler-plugin/lib` directory.

1. Create a class that extends `AbstractEmailImportService`.

   Example:

   ```
   public class CsvEmailImportService extends AbstractEmailImportService {}
   ```
2. Create a default constructor. Consider placing a log message in the body to aid in debugging.

   Example:

   ```
   public CsvEmailImportService() {}

   ```
3. Override the `importEmails()` method by using the following example. Replace *CSV* with a key that represents the name that you plan to use as the `email-source`, which is configured in the `settings.xml` file.

   ```
   String emailSource = EmailGroupsApi.getEmailSource();  
      if ( emailSource.toUpperCase().startsWith( "CSV" ) && !isAlreadyImported() ) {  
   	 super.importEmails();  
      }
   ```
4. Navigate to the `/pentaho-server/pentaho-solutions/system/scheduler-plugin` folder.
5. Open `settings.xml` and change the `email-source` setting to the `email-source` value that you specified when overriding the `importEmails()` method.

   For this example, you would update the `email-source` setting to `"CSV"`.
6. Override the `getEmails()` method by creating a list of `EmailEntity` that is imported into the system.

   ```
   public List<EmailEntity> getEmails() throws EmailImportException
   ```

   See the example in `com.example.CsvEmailImportService.java`.
7. In the `/pentaho-server/pentaho-solutions/system/scheduler-plugin` folder, add a bean definition for the new class in the `plugin.spring.xml` file. Any properties required by the bean can be exposed in the `plugin.spring.xml` file.

   Example:

   ```
   <bean id="csvEmailImport"  
     class="com.example.CsvEmailImportService"  
     init-method="importEmails"  
     lazy-init="false">  
   	<property name="csvFile" value="/<path>/CSVFile.csv"> 
   </bean>

   ```
