# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/install-jdbc-driver-as-a-module-in-jboss/create-module-file-for-hsql-database.md

# Create module file for HSQL database

You will need to create a module file for the HSQL database.

**CAUTION:**

The version of HSQLDB used should be 2.3.2.

1. Download the supported JDBC driver for HSQLDB and place it in the `hsqldb/main` directory.
2. In the `hsqldb/main` directory, create a text file named `module.xml`.
3. Copy this code into the `module.xml` file, then modify it so that the name of the JDBC driver you just downloaded appears in the `resource-root` path.

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
       <module xmlns="urn:jboss:module:1.0" name="org.hsqldb">
           <resources>
               <resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
           </resources>
           <dependencies><module name="javax.api"/></dependencies>
       </module>
   ```
4. Save and close the `module.xml` file.
