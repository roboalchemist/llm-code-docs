# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-web-application-name-or-port.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-web-application-name-or-port.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-web-application-name-or-port.md

# Change the web application name or port

The Pentaho Server and web application default port number is 8080. The default web application name is `pentaho`, which is the name of the WAR file archive, the name of the directory that your application server creates, and also part of the URL structure for all content in the User Console.

If you need to change the User Console application name to something else, or if your Web application server is running on a port other than 8080, follow these instructions.

## Change the web application name on Tomcat

These instructions only work on Tomcat servers that are configured to accept `context.xml` overrides built into deployed WAR files. Some Tomcat deployments may not have this feature turned on. You can change the Tomcat configuration on your own, or consult your Tomcat documentation to learn about other methods of changing a web application context. Use the XML snippet in these instructions in whichever configuration file you end up creating or modifying.

Follow these instructions to change the web application context for a `pentaho.war` file that you deployed to a Tomcat server. While the example below uses `sample` as the context name, you can use whatever context name you choose.

1. Stop the server.
2. Open the `pentaho/server/pentaho-server/tomcat/webapps/pentaho/META-INF/context.xml` file in a text editor, and change the `pentaho` references in the `context path` tag to your preferred context name.

   For example, to specify a context name of `sample`, modify `context path` as follows.

   ```xml
   <context path="/sample" docbase="webapps/sample/">
   ```
3. Save and close the file.
4. Navigate to the `pentaho/server/pentaho-server/tomcat/webapps` folder, and rename the `pentaho` folder to your preferred context name. In this example, rename the `pentaho` folder to `sample`.
5. Edit the `pentaho/server/pentaho-server/tomcat/webapps/ROOT/index.jsp` file to change the `pentaho` reference in the `URL` property to your preferred context name.

   In this example, use the following line of code to specify '`sample`' as the new context name:

   ```xml
   <meta http-equiv="refresh" content="0;URL=/sample">
   ```
6. Edit the `pentaho/server/pentaho-server/pentaho-solutions/system/server.properties` file to change `pentaho` in the value of the `fully-qualified-server-url` setting to your preferred context name.

   In this example, set the `fully-qualified-server-url` as follows.

   ```xml
   fully-qualified-server-url=http://localhost:8080/sample/
   ```
7. Start the server.
