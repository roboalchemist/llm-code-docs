# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-ports-and-urls.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-ports-and-urls.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-ports-and-urls.md

# Change Ports and URLs

The Pentaho Server has associated default port numbers. You can change these port numbers to adjust the Pentaho Server to your system. Since the port number of the Pentaho Server is a part of its URL, you will also have to change that address.

## List of server ports used by PDI

The following port numbers must be available internally on the machine that runs the Pentaho Server:

| Service                         | Port Number |
| ------------------------------- | ----------- |
| Pentaho Server                  | 8080        |
| H2 (SampleData)                 | 9092        |
| Embedded Pentaho Server (Jetty) | 10000       |

The SampleData database is an exception. It is only for evaluation and demonstration purposes and is not necessary for production systems.

**Note:** The Embedded Pentaho Server (Jetty) server port is hard-coded in Pentaho Data Integration and cannot be changed. If port 10000 is unavailable, the system will increment by 1 until an available port is found.

## Change Pentaho Server (Tomcat) port numbers

Edit the `/pentaho/server/pentaho-server/tomcat/conf/server.xml` file and change the port numbers as shown in the following example code:

```xml
<!-- A "Connector" represents an endpoint by which requests are received
         and responses are returned. Documentation at :
         Java HTTP Connector: /docs/config/http.html (blocking & non-blocking)
         Java AJP  Connector: /docs/config/ajp.html
         APR (HTTP/AJP) Connector: /docs/apr.html
         Define a non-SSL HTTP/1.1 Connector on port 8080
    -->
    <Connector URIEncoding="UTF-8" port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="9443" />
    <!-- A "Connector" using the shared thread pool-->
    <!--
    <Connector URIEncoding="UTF-8" executor="tomcatThreadPool"
               port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="9443" />
```

**Note:** You may also have to change the SSL and SHUTDOWN ports in this file, depending on your configuration.

Next, follow the directions in [Change the Pentaho Server URL](#change-the-pentaho-server-url) to accommodate for the new port number.

## Change the Pentaho Server URL

You can change the Pentaho Server hostname from `localhost` to a specific IP address, hostname, or domain name by following these instructions. This procedure is also a requirement if you are changing the Pentaho Server port number.

1. Stop the Pentaho Server.
2. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system` directory and open the `server.properties` file with any text editor.
3. Modify the value of the `fully-qualified-server-url` element appropriately.

   ```xml
   fully-qualified-server-url=http://localhost:8080/pentaho/
   ```
4. Save and close the file.
5. Start the Pentaho Server.

The Pentaho Server is now configured to reference itself at the specified URL.

**Note:** If you recently upgraded to Pentaho 6.x or higher from a version earlier than 6.0, you may need to remove the `<context-param>` entry for the `fully-qualified-server-url` from the `/tomcat/webapps/pentaho/WEB-INF/web.xml`. If so, restart the Pentaho Server after removing it.
