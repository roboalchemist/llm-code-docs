# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/report-parameters-that-include-accented-characters.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/report-parameters-that-include-accented-characters.md

# Report parameters that include accented characters

If you run a report containing parameters with accented characters, you may get an error message which reads, "This parameter value is of an invalid value."

To avoid this error message, modify the Tomcat server to include accented character support. This modification is especially necessary if you plan to use Spanish, French, or any other language that use accented character sets.

The following example shows how to implement accented character set support:

1. Stop the Tomcat service.

   ```
   sudo /etc/init.d/tomcat stop
   ```
2. Open the `/tomcat/server/conf/server.xml` file in a text editor.
3. Locate each `Connector` node (typically, there are four in a default Tomcat configuration).

   Add a **URIEncoding="UTF-8"** parameter to it, as shown in the following sample code block:

   ```xml
   <Connector URIEncoding="UTF-8" port="8080" protocol="HTTP/1.1"
                  connectionTimeout="20000"
                  redirectPort="8443" />
   ```
4. Save and close the file, then restart the Tomcat service.

   ```
   sudo /etc/init.d/tomcat start
   ```
