# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/pdi-logging.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pdi-logging.md

# PDI logging

You can troubleshoot issues without having to examine the comprehensive log of server executions using PDI logging. PDI logging contains transformation and job logs for both PDI client and Pentaho Server executions, which are separate from the comprehensive logging data.

For information on comprehensive logging, see **Logging and performance monitoring** in the **Pentaho Data Integration** publication.

## Set up the log file

Transformation and job logging is enabled by default. Logging levels and rotations are configured separately for the PDI client and Pentaho Server, while the date formatting configures both log outputs. Perform the following steps to configure logging for the Pentaho Server or PDI client:

1. Stop all relevant servers or exit the PDI client.
2. Navigate to the following directory and open the `log4j2.xml` file with any text editor:

| **Pentaho Server** | `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes` |
| ------------------ | -------------------------------------------------------------- |
| **PDI client**     | `design-tools/data-integration/classes`                        |

3\. Set your desired logging levels in the XML \<Logger> elements for \`org.pentaho.di.trans.Trans\` and \`org.pentaho.di.job.Job\`. You can set different logging levels for transformations than for jobs. The following table maps PDI logging levels to the corresponding Apache log4j2 levels:

```
|PDI Log Level|Log4j Log Level|
|-------------|---------------|
|BASIC|INFO|
|DETAILED|INFO|
|MINIMAL|WARN|
|DEBUG|DEBUG|
|ERROR|ERROR|
|ROWLEVEL|TRACE|
```

4\. Set your desired log file rotation (`rollingPolicy`) value by editing the **FileNamePattern** parameter in the `log4j2.xml` file for the `pdi-execution-appender`. The parameters are:

```
|Parameter|Description|
|---------|-----------|
|**yyyy-MM-dd**|Specify a daily rotation. \(Default\)|
|**yyyy-MM**|Specify a monthly rotation.|
|**yyyy-MM-dd-HH-mm**|Specify a rotation every minute.|
```

5\. Navigate to the `design-tools/data-integration/classes` directory and open the `log4j2.xml` file with any text editor.

6. Set your desired log file date and timestamp (`RollingFile`) format by editing the **Pattern** parameter in the `log4j2.xml` file for the `pdi-execution-appender`.

   You can use the default format or define a custom format as shown using the examples in the following table.

   | Parameter                      | Example                           |
   | ------------------------------ | --------------------------------- |
   | {**yyyy-MM-dd HH:mm:ss.SSS**}  | 2012-11-02-14:34:02.123 (Default) |
   | {**HH:mm:ss,SSS**}             | 14:34:02,123                      |
   | {**dd MMM yyyy HH:mm:ss,SSS**} | 02 Nov 2012 14:34:02,123          |
   | {**MMM dd,yyyy HH:mm:ss**}     | Nov 02,2012 14:34:02              |

   **Note:** See Java’s [SimpleDateFormat](https://docs.oracle.com/javase/6/docs/api/java/text/SimpleDateFormat.html) for a definition of the parameter variables. If you set a date format that cannot be parsed by SimpleDateFormat, then the hard-coded default format (yyyy/MM/dd HH:mm:ss) is used for the `pdi.log` and PDI console log.
7. Optionally, you can set a localized time in the date format by adding a second set of braces and a time zone id value in the (`RollingFile`) format of the **Pattern** parameter for the `pdi-execution-appender`, as shown in the table below. If not set, your current time is used.

   **Note:** See [java.util.TimeZone.getTimeZone](https://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html#getTimeZone\(java.lang.String\)) for time zone value details.

   | Parameter                                | Example                 |
   | ---------------------------------------- | ----------------------- |
   | {**yyyy-MM-dd HH:mm:ss.SSS**}{**GMT-5**} | 2012-11-02 05:34:02.123 |
   | {**HH:mm:ss**}{**GMT+0**}                | 10:34:02                |
8. Save and close the file, then start all affected servers or the PDI client to test the configuration.

## Use the log file

The log files are located in the following directories:

| Pentaho Server | `server/pentaho-server/logs/pdi.log`         |
| -------------- | -------------------------------------------- |
| PDI client     | `design-tools/data-integration/logs/pdi.log` |

Navigate to a log file and open the file to view the contents. The log entry fields in the log files are:

| Field         | Description                                        |
| ------------- | -------------------------------------------------- |
| DateTimeStamp | Date and time of the log                           |
| LogThreshold  | Logging level (INFO, ERROR, DEBUG, WARN, or TRACE) |
| ThreadID      | Unique key for the job or transformation execution |
| Filepath      | Absolute path of the transformation or job         |
| Message       | Log message                                        |

The following is an example of a log entry:

`2018-03-07 11:40:36.290 INFO <Launch transformation UUID: 1246b616-a845-4cbc-9f4c-8a4a2cbfb4f1> [C:\build\pdi-ee-client-8.1.0.0-267\data-integration\samples\jobs\run_all\Run all sample transformations.kjb file:///C:/build/pdi-ee-client-8.1.0.0-267/data-integration/samples/jobs/run_all/Define FILENAME Variable and execute.kjb] Starting entry`

This entry contains these values for the following fields:

| Field         | Description                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DateTimeStamp | 2018-03-07 11:40:36.290                                                                                                                                                                                |
| LogThreshold  | INFO                                                                                                                                                                                                   |
| ThreadID      | \<Launch transformation UUID: 1246b616-a845-4cbc-9f4c-8a4a2cbfb4f1>                                                                                                                                    |
| Filepath      | `[C:\build\pdi-ee-client-8.1.0.0-267\data-integration\samples\jobs\run_all\Run all sample transformations.kjb file:///C:/build/pdi-ee-client-8.1.0...run_all/DefineFILENAME Variable and execute.kjb]` |
| Message       | Starting entry                                                                                                                                                                                         |
