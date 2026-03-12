# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-7-add-jboss-deployment-structure-file-to-a-.war-file.md

# Step 6: Add JBoss Deployment Structure file to the WAR file

The `jboss-deployment-structure.xml` JDS file controls class loading. It prevents automatic dependencies from being added, adds dependencies, defines additional modules, changes isolated class loading behavior, and adds additional resource roots to a module.

You will need to create, then add a JBoss deployment structure file (`jboss-deployment-structure.xml`) to the `pentaho.war` file.

**CAUTION:**

If you have a different database than PostgreSQL, adjust the module name information in this section to match the ones in your environment.

1. Use a text editor to create a new file named: `jboss-deployment-structure.xml`
2. Copy the following code snippet to the `jboss-deployment-structure.xml` file.

   ```xml
   <jboss-deployment-structure>
   <deployment>
   <exclude-subsystems>
   <subsystem name="resteasy" />
   <subsystem name="jaxrs" />
   <subsystem name="webservices" />
   </exclude-subsystems>
   <dependencies>
   <module name="org.h2" />
   <module name="org.postgresql" />
   <module name="org.jboss.modules" />
   <module name="org.hsqldb" />
   </dependencies>
   </deployment>
   </jboss-deployment-structure>

   ```
3. Save and close the file.
4. Use a ZIP extraction utility (such as 7-Zip, Winzip, or Archive) to view the contents of the `pentaho.war` file. Do not unzip or extract the contents of the file.
5. Navigate to the `WEB-INF` directory and add the `jboss-deployment-structure.xml` file that you just created to it.
6. Close the `pentaho.war` file. The ZIP extraction utility that you used might show a prompt which asks whether you would like to update the file in the `pentaho.wararchive`. Confirm that you would like to update the file.
