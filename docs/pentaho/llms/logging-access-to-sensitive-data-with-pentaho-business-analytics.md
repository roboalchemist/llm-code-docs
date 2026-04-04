# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/logging-access-to-sensitive-data-with-pentaho-business-analytics.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/logging-access-to-sensitive-data-with-pentaho-business-analytics.md

# Tracking access to sensitive data

You can set up audit trail properties for tracking access to sensitive data in analytics and reporting tools using Pentaho logging tools. You can configure tracking properties to log statements across Pentaho’s reporting and analysis tools to track user access to sensitive data or investigate data breaches. This configuration generates logs that correlate users and IP addresses to SQL, MDX and parameter values for discovering:

* The data a specific user viewed and where they viewed it.
* The specific piece of sensitive data a user accessed and when they accessed it.

These tracking properties are supported within the logging functions of the following Pentaho analytics and reporting tools:

* Analyzer
* Mondrian
* Interactive Reports (PRTI)
* Dashboards
* Report Designer (PRPT)
* CTools (specifically, CDA)
* Any content executed by the Pentaho Scheduler

The tracking properties use log4j’s Mapped Diagnostic Context (MDC) feature that provides the method to add additional user/session contextual information to all log statements within a thread and related threads.

## Mapped Diagnostic Context (MDC) tracking properties

You can track access to sensitive data by configuring specific properties in the Pentaho `log4j2.xml` file. These properties use log4j's Mapped Diagnostic Context (MDC) feature and allow you to customize the logging statements that the `log4j2.xml` file collects:

* **sessionId**

  The Pentaho session ID, typically related to the JSession cookie.
* **sessionName**

  A user name, for example, Suzy.
* **instanceId**

  The UUID that identifies a report and instances when it ran.
* **remoteAddr**

  The IP address of the user who ran the report.
* **remoteHost**

  The user remote host.
* **remotePort**

  The user remote port.
* **serverName**

  The server name access by the user (possibly a load balancer).
* **serverPort**

  The server port accessed by the user.
* **localAddr**

  The local server IP (actual Pentaho BA Server behind load balancer).
* **localName**

  The local server name.
* **localPort**

  The local server port.

Once you configure your selected properties, Pentaho generate a daily rolling log file with the name `session.data.access.log` that includes the SQL, MDX, and parameter values. To meet your needs, you can configure the file size, date, time, and file compression for `session_data_access.log` in the `log4j2.xml` file.

## Activate logging with MDC tracking properties

Follow these steps to enable and configure the log4j Mapped Diagnostic Context (MDC) tracking-related properties you want to use in the Pentaho logs:

1. Stop the Pentaho Server.
2. Navigate to the `log4j2.xml` file, which is located in the `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes` directory.
3. Open the file with any text editor.
4. Add or uncomment the following log4j `appender` anywhere inside the \<Appenders> node and modify the appender's `ConversionPattern` to add or remove the MDC tracking properties you want to use.

   ```xml
   <!-- ========================================================== -->
           <!-- Special log file specifically for sensitive data access    -->
           <!-- on a per user/session/IP level                             -->
           <!-- Available MDC properties:                                  -->
           <!-- sessionId, sessionName, instanceId, remoteAddr, remoteHost,-->
           <!-- remotePort, serverName, serverPort,                        -->
           <!-- localAddr, localName, localPort                            -->
           <!-- ========================================================== -->

           <RollingFile name="SESSION_DATA_ACCESS_LOG" fileName="../logs/session_data_access.log" filePattern="../logs/session_data_access.log.%d{yyyy-MM-dd}">
               <PatternLayout>
                   <Pattern>%d %-5p [%c] sessionId:%X{sessionId} sessionName:%X{sessionName} instanceId:%X{instanceId} remoteAddr:%X{remoteAddr} %m%n</Pattern>
               </PatternLayout>
               <Policies>
                   <TimeBasedTriggeringPolicy />
               </Policies>
               <DefaultRolloverStrategy />
           </RollingFile>

   ```
5. Add or uncomment the following log4j `Loggers` anywhere inside the `<Loggers>` node:

   ```
   <!-- =========================== -->
           <!-- Sensitive Data Access       -->
           <!-- =========================== -->
           <Logger name="mondrian.rolap.RolapUtil" level="DEBUG" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="org.pentaho.metadata.query.impl.sql.SqlGenerator" level="TRACE" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="org.pentaho.reporting.engine.classic.core.modules.misc.datafactory.sql" level="DEBUG" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="org.pentaho.reporting.platform" level="INFO" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="org.pentaho.reporting.engine.classic.core.parameters" level="DEBUG" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="org.pentaho.reporting.platform.plugin.ExecuteReportContentHandler" level="DEBUG" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="org.pentaho.platform.plugin.action.sql.SQLLookupRule" level="DEBUG" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>
           <Logger name="pt.webdetails.cda.dataaccess.SimpleDataAccess" level="DEBUG" additivity="false">
               <appender-ref ref="SESSION_DATA_ACCESS_LOG"/>
           </Logger>

   ```
6. Restart the Pentaho Server.

This configuration generates a daily, rolling `session_data_access.log` file with SQL, MDX, and parameter values. Open the file to view the logging results. You can configure the `session_data_access.log` file's size, date, time, and file compression to suit your needs in the `log4j2.xml` file.

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

## Working with Pentaho Operations Mart

The log4j Maped Diagnostic Context (MDC) tracking properties work in combination with the Pentaho [Business Analytics Operations Mart](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/business-analytics-operations-mart) and provide you with greater detail into the SQL, MDX and parameter values used in each report execution instance. The logging attributes directly join with the Ops Mart PRO\_AUDIT table as follows:

| MDC Property | Ops Mart PRO\_AUDIT table |
| ------------ | ------------------------- |
| sessionID    | PRO\_AUDIT.INST\_ID       |
| sessionName  | PRO\_AUDIT.ACTOR          |
| instanceID   | PRO\_AUDIT.MESSAGE\_NAME  |

## Correlating Pentaho logs with third-party tools

As a best practice for working with large log files, you can combine, index and search the output of multiple Pentaho logs using third-party tools such as Splunk. You can also use an open-source ELK stack to index and search log files.
