# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging/add-jboss-logging-for-version-7.0-or-later-manual-installation.md

# Add JBoss logging

Perform the following steps for JBoss logging:

1. Open the `standalone.xml` file in the `*&lt;your jboss directory&gt;*/standalone/configuration` directory.
2. Find the logging subsystem definition (for example, `<subsystem xmlns="urn:jboss:domain:logging:3.0">`) and add the following lines of code just after that opening tag:

   ```xml
   <add-logging-api-dependencies value="false"/>
   <use-deployment-logging-config value="false"/>

   ```
3. Save and close the file.
4. Navigate to the `pentaho/server/pentaho-server/<your jboss installation directory>/standalone/deployments` directory.
5. Use a ZIP extraction utility to view the contents of the `pentaho.war` file. Do not unzip or extract the contents of the file.
6. Navigate to the `WEB-INF/classes` directory and open the `log4j2.xml` file in a text editor. By default, all log files are configured to be written to `../logs` which, if not changed, will translate to `*&lt;your jboss directory&gt;*/logs`.
7. Replace all occurrences of `../logs` with `${jboss.server.log.dir}`.
8. Save and close the file. The ZIP extraction utility might show a prompt asking if you would like to update the file in the `pentaho.war` archive. If this prompt appears, confirm that you would like to update the file.
