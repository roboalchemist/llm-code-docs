# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-port-numbers-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-port-numbers-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-port-numbers-for-the-pentaho-server.md

# Change the port numbers for the Pentaho Server

Follow the instructions below to change the port through which the Pentaho Server runs:

1. Stop the Pentaho Server.
2. Navigate to the `/pentaho-server/tomcat/conf/` directory.
3. Open the `server.xml` file with any text editor, and search for the value for `Define a non-SSL HTTP/1.1 Connector`.

   Change the port number in the connector port element below from 8080 to your preferred port number.

   ```xml
   <!-- Define a non-SSL HTTP/1.1 Connector on port 8080 -->
       <Connector port="8080" maxHttpHeaderSize="8192"
                  maxThreads="150" minSpareThreads="25" maxSpareThreads="75"
                  enableLookups="false" redirectPort="8443" acceptCount="100"
                  connectionTimeout="20000" disableUploadTimeout="true" />
   ```
4. Save and close the `server.xml` file.
5. Navigate to the `/pentaho-server﻿/pentaho-solutions/system` directory and open the `server.properties` file with any text editor.
6. Change the `fully-qualified-server-url` entry to match the new port number you specified in `server.xml`.

   ```xml
   fully-qualified-server-url=http://localhost:8080/pentaho/
   ```
7. Save and close the file.
8. Restart the Pentaho Server.

If you recently upgraded to Pentaho 6.0, you may need to remove the `<context-param>` entry for the `fully-qualified-server-url` from the `/tomcat/webapps/pentaho/WEB-INF/web.xml`. If so, restart the Pentaho Server after removing it.
