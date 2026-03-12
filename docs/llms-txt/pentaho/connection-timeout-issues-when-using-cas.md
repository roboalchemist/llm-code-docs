# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/security-issues/connection-timeout-issues-when-using-cas.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/connection-timeout-issues-when-using-cas.md

# Connection timeout issues when using CAS

Connection timeout issues when using CAS with the Pentaho Server can result in the inability to login or re-load data in the web client page until you refresh the page. If you have problems with the session timing out, perform the following steps to configure the session timeout:

1. Stop the Pentaho Server.
2. Navigate to the `pentaho-server/tomcat/webapps/pentaho/WEB-INF` directory and open the `web.xml` file with any text editor.
   1. Find the `session-config` property and edit the `session-timeout` value (the default value is 120 minutes) to increase the period to a value that is greater than the setting used for your CAS server session timeout value:

      ```xml
      <session-config>
        <tracking-mode>COOKIE</tracking-mode>
        <session-timeout>120</session-timeout>
      </session-config>
      ```
   2. Locate the Pentaho Web Context Filter and add the following `init-param`:&#x20;

      ```xml
      <init-param>
        <param-name>ssoEnabled</param-name>
        <param-value>true</param-value>
      </init-param
      ```
   3. Save and close the file.
3. Activate the session timeout dialog box:
   1. Navigate to the `pentaho-server/pentaho-solutions/system` directory and open the `applicationContext-spring-security-cas.xml` file then locate the `httpSessionPentahoSessionContextIntegrationFilter` bean id.
   2. Find the `ssoEnabled` property and set the value from *true* to `false`.
   3. Save and close the file.
4. Restart the Pentaho Server.

If the session does timeout, a session timeout dialog box will now warn users when the session expires and then will reauthenticate the session through CAS when the dialog box is closed.
