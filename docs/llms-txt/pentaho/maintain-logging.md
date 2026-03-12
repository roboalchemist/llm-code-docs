# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/maintain-logging.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/maintain-logging.md

# Maintain logging

You can maintain your system logs by using rotation and by monitoring the execution status of transformations and jobs.

## Log rotation

This procedure assumes that you do not have or do not want to use an operating system-level log rotation service. If you are using such a service on your Pentaho Server, connect to the Pentaho Server and use that instead of implementing this solution.

The Pentaho Server uses the Apache log4j Java logging framework to store server feedback. The default settings in the `log4j2.xml` configuration file comes pre-configured for a rolling file appender. This appender will cause the log files to archive the previous day’s log file and roll over to a new file each day.

To configure a size-based strategy to roll over log files when they reach a specific size, perform the following steps to configure a `SizeBasedTriggeringPolicy` appender.

1. Stop all relevant servers.
2. Edit the `log4j2.xml` settings file for the Pentaho Server. This XML file is located in: `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes/`
3. Modify the `PENTAHOFILE` `RollingFile` appenders to match the log rotation conditions that you prefer. In this example, we change the `TimeBasedTriggeringPolicy` to a `SizeBasedTriggeringPolicy`. You may need to consult the log4j documentation to learn more about other configuration options.

   ```
   <RollingFile name="PENTAHOFILE" fileName="../logs/pentaho.log" filePattern="../logs/pentaho.log.%i">
               <PatternLayout>
                   <!-- The default pattern: Date Priority [Category] Message\n -->
                   <Pattern>%d %-5p [%c] %m%n</Pattern>
                   <!-- The full pattern: Date MS Priority [Category] (Thread:NDC) Message\n
                   <Pattern>%d %-5r %-5p [%c] (%t:%x) %m%n</Pattern>
                    -->
               </PatternLayout>
               <Policies>
                   <SizeBasedTriggeringPolicy size="10 MB" />
               </Policies>
               <DefaultRolloverStrategy max="1" />
        </RollingFile>

   ```
4. Save and close the file.
5. Start all affected servers to test the configuration.

You have an independent log rotation system in place for all modified servers.

## Execution status

You can view remotely executed and scheduled job and transformation details, including the date and time that they were run, and their status and results, through the PDI Status page. To view it, navigate to the `/pentaho/kettle/status` page on your Pentaho Server (change the host name and port to match your configuration):

```
http://localhost:8080/pentaho/kettle/status
```

You must be logged in to ensure you are redirected to the login page.

You can get to a similar page in the PDI client by using the Monitor function of a slave server. This page clears when the server is restarted, or at the interval specified by the **object\_timeout\_minutes** setting.

### On Carte

Any action done through the Carte server embedded in the Pentaho Server is controlled through the `/pentaho/server/pentaho-server/pentaho-solutions/system/kettle/slave-server-config.xml` file. Notice the **Configuration details** table at the bottom of the screen. This shows the three configurable settings for schedule and remote execution logging.

**Note:** To make modifications to `slave-server-config.xml`, you must stop the Pentaho Server.

The three configurable options in the `slave-server-config.xml` file are explained in the following table:

| Property                       | Values                                                                      | Description                                                              |
| ------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **max\_log\_lines**            | Any value of `0` (zero) or greater. `0` indicates that there is no limit.   | Truncates the execution log when it goes beyond this many lines.         |
| **max\_log\_timeout\_minutes** | Any value of `0` (zero) or greater. `0` indicates that there is no timeout. | Removes lines from each log entry if it is older than this many minutes. |
| **object\_timeout\_minutes**   | Any value of `0` (zero) or greater. `0` indicates that there is no timeout. | Removes entries from the list if they are older than this many minutes.  |

The following code block is an example of the `slave-server-config.xml` file:

```xml
<slave_config>
  <max_log_lines>0</max_log_lines>
  <max_log_timeout_minutes>0</max_log_timeout_minutes>
  <object_timeout_minutes>0</object_timeout_minutes>
</slave_config>
```

## Best practices for logging

Kettle logging provides extensive flexibility that allows you to determine log locations, granularity, as well as what information is captured. Here are the best practices for setting up logging in your environment. For more information on logging in PDI, see the **Pentaho Data Integration** document.

* Store logs in a centralized database. By default, log files are stored locally. The PDI client, Carte, and Pentaho Server logs are stored separately. To make log information easier to find, place logs in a central database. As an added bonus, centralized logging makes it easier to use PDI’s performance monitoring more effectively.
* Obtain full insert accesses for tables. Logging can fail if you do not have the appropriate accesses. Having the appropriate accesses minimizes this risk. To learn more about table access, consult the documentation for your database.
* Install JDBC Drivers Locally and on Each Server. This helps you avoid `Driver not found` errors. For a list of suported drivers, see the **JDBC drivers reference** in the **Try Pentaho Data Integration and Analytics** document.
* Use implied schemas when possible. Implied schemas result in fewer places to troubleshoot should logging fail. Of course, you can still specify a schema if needed.
* Make templates for transformation and job files. Include logging configurations in the template so that they can be reused with ease.
* Use Kettle global logging variables when possible. To avoid the work of adding logging variables to each transformation or job, consider using global logging variables instead. You can override logging variables by adding information to individual transformations or jobs as needed.
* Use different logging tables for jobs and transformations. If you find logging table data is deleted unexpectedly, see **Log table data is not deleted** in the **Pentaho Data Integration** document.

If you choose to use the `kettle.properties` file, observe the following best practices.

* Backup your `kettle.properties` files. If you are making many changes to the `kettle.properties` file, consider backing up the file first. This will make it easier to restore should issues occur.
* Maintain a master copy of the `kettle.properties` file. It is usually easiest to use the `kettle.properties` file for the PDI client, then to overwrite the Carte and Pentaho Server copies if changes are made. Make sure that values that might change, such as directory paths, are maintained however.
* Test thoroughly. Test your settings by saving your kettle.properties file locally, then restarting the PDI client. Make sure the `kettle.properties` file loads properly. Execute a transformation or job that uses the settings. Try executing the transformation locally and remotely on the Pentaho Server to ensure that log variables reference the same places.
