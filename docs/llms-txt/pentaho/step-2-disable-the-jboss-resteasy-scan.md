# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-2-disable-the-jboss-resteasy-scan.md

# Step 2: Disable the JBoss RESTEasy scan

To load Pentaho REST services correctly, the RESTEasy scan in JBoss must be disabled.

This task explains how to disable the RESTEasy scan in JBoss.

1. Use a ZIP extraction utility such as 7-Zip, WinZip, or Archive to view the contents of the `<your jboss installation directory>/standalone/deployments/pentaho.war` file. Do not unzip the `pentaho.war` file, just view its contents.
2. Navigate to the `WEB-INF` directory in the `pentaho.war` file and open the `web.xml` file in a text editor.
3. At the end of the **\<context-param>** tags, add this code.

   ```xml

   <context-param>
                <param-name>resteasy.scan</param-name>
                <param-value>false</param-value>
           </context-param>
           <context-param>
                <param-name>resteasy.scan.resources</param-name>
                <param-value>false</param-value>
           </context-param>
           <context-param>
                <param-name>resteasy.scan.providers</param-name>
                <param-value>false</param-value>
   </context-param>

   ```
4. Save the changes and close the file.
5. The ZIP extraction utility that you used might show a prompt that asks whether you would like to update the file in the `pentaho.war` archive. If this happens, confirm that you would like to do this.
