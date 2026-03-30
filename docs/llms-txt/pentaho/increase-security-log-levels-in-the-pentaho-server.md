# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/security-issues/increase-security-log-levels-in-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/increase-security-log-levels-in-the-pentaho-server.md

# Increase security log levels in the Pentaho Server

The security logging facilities of the Pentaho Server are set to ERROR by default, which may not supply enough details for troubleshooting and testing.

The following procedure explains how to set up verbose logging which increases the level of detail in the Pentaho Server logs for security-related messages.

1. Stop the Pentaho Server with the following script

   ```
   sh /usr/local/pentaho/server/pentaho-server/stop-pentaho.sh
   ```
2. Open the `/pentaho/server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes/log4j2.xml` file with a text editor.
3. Change or add the ThresholdFilter value in the `<Console>` or \<RollingFile> sections to one of the following logging levels: `WARN`, `ERROR`, `FATAL`, or `DEBUG` (depending on which level you prefer):

   ```xml
   < Console name="PENTAHOCONSOLE" >
   <ThresholdFilter level="ERROR"/>
   <PatternLayout><Pattern>%d{ABSOLUTE} %-5p [%c{1}] %m%n</Pattern>
   </PatternLayout>
   </Console>

   ```
4. Add the following log statements directly above the root element:

   ```xml
   <!-- all Spring Security classes will be set to DEBUG -->
   <Logger name="org.springframework.security" level=”DEBUG”>
   <!-- all Pentaho security-related classes will be set to DEBUG -->
   <Logger name="org.pentaho.platform.engine.security" level=”DEBUG”>
   <Logger name="org.pentaho.platform.plugin.services.security" level=”DEBUG”>

   ```
5. Save and close the file, then edit the Spring Security configuration file that corresponds with your security back end in the `/pentaho/server/pentaho-server/pentaho-solutions/system/` directory. The file will be one of the following options:
   * `applicationContext-spring-security-memory.xml`
   * `applicationContext-spring-security-jdbc.xml`
   * `applicationContext-spring-security-ldap.xml`
6. Find the `daoAuthenticationProvider` bean definition, then add the following property anywhere inside of it (before the `</bean>` tag):

   ```xml
   <property name="hideUserNotFoundExceptions" value="false" />
   ```
7. Save the file and close the text editor.
8. Start the Pentaho Server with the following script:

   ```
   sh /usr/local/pentaho/server/pentaho-server/start-pentaho.sh
   ```

For this example, Pentaho Server security logging is now globally set to *DEBUG*, which provides verbose logging for debugging security configuration problems. All Pentaho Server messages will be collected in the `/pentaho/server/pentaho-server/logs/pentaho.log` file.

When you are finished configuring and testing the Pentaho Server, you should decrease verbose logging down to a less detailed level, such as `ERROR`, to prevent `pentaho.log` from growing too large.

## Enable extra LDAP security logging

If you need more LDAP-related security details in `pentaho.log`, or if you are specifically having difficulty with LDAP authentication configuration, perform the following steps to set up verbose logging.

**Note:** These instructions are for testing and pre-production only. User names and passwords will be displayed in the log file in plain text.

1. Stop the Pentaho Server
2. Go to the `/pentaho/server/pentaho-server/pentaho-solutions/system` directory and open the `applicationContext-spring-security-ldap.xml` file with a text editor.
3. Locate the bean declaration for `DefaultLdapAuthenticationProvider` and replace the `constructor-arg` bean with the following new bean:

   Old Bean:

   ```xml
   <constructor-arg>
   <ref bean="authenticator" />
   </constructor-arg>
   ```

   New Bean:

   ```xml
   <constructor-arg>
   <ref bean="ldapAuthenticatorProxy" />
   </constructor-arg>
   ```
4. In the same directory, locate and open the `pentaho-spring-beans.xml` file.
5. Add the following import line to the list of files:

   ```xml
   <import resource="applicationContext-logging.xml" />
   ```
6. Save and close the file.
7. Locate the `/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes` directory and open the `log4j2.xml` file with a text editor.
8. Add this category to the `log4j2.xml` file.

   ```xml
   <Logger name="org.springframework.security.providers" level="DEBUG"/>
   ```
9. Save and close the file, then start the Pentaho Server.

You will now have verbose LDAP-specific log messages in `pentaho.log`, which include login credentials for every user that tries to log on.

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.
