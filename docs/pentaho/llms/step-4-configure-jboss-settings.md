# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-4-configure-jboss-settings.md

# Step 4: Configure JBoss settings

The JBoss startup script needs to be modified to match the Pentaho Server's memory resource requirements.

If this step is not performed, the Pentaho Server will not start. Besides matching memory resources, the Tomcat connector must also be updated for UTF-8 encoding.

**CAUTION:**

We recommend increasing the time-outs even further than shown here if you have a large database and you are upgrading from 5.x.

1. Use a text editor to open the standalone configuration file.

   The file you open depends on your operating system.

   * Windows: `<your JBoss installation directory>\bin\standalone.conf.bat`
   * Linux: `<your JBoss installation directory>/bin/standalone.conf`
2. Find the section for JVM memory allocation, then locate **JAVA\_OPTS=-Xms1G -Xmx1G -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m**, and replace it with the following text:

   Windows:

   ```xml
   "JAVA_OPTS=-Xms4096m -Xmx6144m -XX:MetaspaceSize=96M and -XX:MaxMetaspaceSize=256m -DDI_HOME=%DI_HOME% -Dpentaho.installed.licenses.file=%PENTAHO_INSTALLED_LICENSE_PATH% -Djboss.as.management.blocking.timeout=3600"
   ```

   Linux:

   ```xml
   JAVA_OPTS="-Xms4096m –Xmx6144m -XX:MetaspaceSize=96M and -XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true" -DDI_HOME=$DI_HOME -Dpentaho.installed.licenses.file=$PENTAHO_INSTALLED_LICENSE_PATH -Djboss.as.management.blocking.timeout=3600"
   ```

   **Note:** The **DI\_HOME** variable is defined in a separate step. See [Starting the Pentaho Server](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/starting-the-pentaho-server).
3. Save the changes and close the file.
4. Use a text editor to open the `standalone.xml` file in the `<your JBoss installation directory>/standalone/configuration` folder.
5. Set the **org.apache.catalina.connector.URL\_ENCODING** and **org.apache.catalina.connector.USE\_BODY\_ENCODING\_FOR\_QUERY\_STRING** system properties by adding the following lines of code to the `standalone.xml` file. The following code must be added after the <`extensions`> section:

   ```xml
   <system-properties>
     <property name="org.apache.catalina.connector.URI_ENCODING" value="UTF-8"/>
     <property name="org.apache.catalina.connector.USE_BODY_ENCODING_FOR_QUERY_STRING" value="true"/>
   </system-properties>

   ```
6. Save the changes and close the file.
