# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-3-set-the-location-of-the-solutions-directory.md

# Step 3: Set the location of the solutions directory

To deploy JBoss correctly, Pentaho recommends that you define the location of the `pentaho-solutions` directory in the `web.xml` file.

Perform the following steps to define the location.

1. If you have not done so already, use a ZIP extraction utility such as 7-Zip, WinZip, or Archive to view the contents of the `<your jboss installation directory>/standalone/deployments/pentaho.war` file. Do not unzip the `pentaho.war` file; just view its contents.
2. Navigate to the `WEB-INF` directory in the `pentaho.war` file and open the `web.xml` file in a text editor.
3. Locate the following **\<context-param>** tags.

   ```xml
   <context-param>
         <param-name>solution-path</param-name>
         <param-value></param-value>
    </context-param>
   ```
4. Set the parameter value of the **solution-path** to the **pentaho-solutions** path. An example of the code is below.

   ```xml
   <context-param>
        <param-name>solution-path</param-name>
        <param-value>/home/pentaho/server/pentaho-server/pentaho-solutions</param-value>
    </context-param>

   ```
5. Save the changes and close the file
