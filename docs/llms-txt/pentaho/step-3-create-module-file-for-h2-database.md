# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-3-create-module-file-for-h2-database.md

# Step 3: Create module file for H2 database

You need to create a module file for the H2 database.

1. In the `h2/main` directory, create a text file named `module.xml`.
2. Copy this code into the `module.xml` file, then modify it so that the name of the JDBC driver you just downloaded appears in the `resource-root` path.

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <module xmlns="urn:jboss:module:1.0" name="org.h2">
   <resources>
   <resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
   </resources>
   <dependencies><module name="javax.api"/></dependencies>
   </module>
   ```
3. Save and close the `module.xml` file.
