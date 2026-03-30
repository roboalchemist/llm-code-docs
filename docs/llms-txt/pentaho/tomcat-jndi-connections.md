# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/tomcat-jndi-connections.md

# Tomcat JNDI connections

If you installed the Pentaho Server using the manual installation method, then you specified data connections to your Tomcat web application server. If you want to modify existing connections or add more connections, perform the following tasks.

**Note:** Database connection and network information, such as the username, password, driver class information, IP address or domain name, and port numbers for your Pentaho Repository database are stored in the `context.xml` file. Modify this file to reflect the database connection and network information to reflect your operating environment. You also modify the values for the **validationQuery** parameters in this file if you have chosen to use a Pentaho Repository database other than PostgreSQL.

1. Stop the Tomcat and Pentaho Servers.
2. Consult your database documentation to determine the class name and connection string for your database.
3. Edit the `/tomcat/webapps/pentaho/WEB-INF/web.xml` file.
4. At the end of the `<web-app>` element, in the same part of the file where you see `<!-- insert additional resource-refs -->`, add the following XML snippet:

   ```xml
   <resource-ref>
       <description>myDataSource</description>
       <res-ref-name>jdbc/myDataSource</res-ref-name>
       <res-type>javax.sql.DataSource</res-type>
       <res-auth>Container</res-auth>
   </resource-ref>
   ```

   Change the `description` and `res-ref-name` nodes, as well as any others that apply to your situation and fit your database. You may need to consult the [JNDI Resources](https://tomcat.apache.org/tomcat-7.0-doc/index.html) article in the Apache Tomcat documentation to see if there are other components to consider.
5. Save and close the `web.xml` file.
6. Edit the`/tomcat/conf/context.xml` with a text editor. Alternatively, you can modify the `/tomcat/webapps/pentaho/META-INF/context.xml` file if you want this data connection to be available only to the Pentaho Server. Adding JNDI connections to the `context.xml` makes them available to all of the webapps deployed to this Tomcat instance.
7. Anywhere inside of the `Context` element, add the following XML snippet:

   ```xml
   <Resource name="jdbc/myDataSource"
       auth="Container" type="javax.sql.DataSource"
       factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
       maxActive="20"
       maxIdle="5"
       maxWait="10000"
       username="dbuser"
       password="password"
       driverClassName="org.postgresql.Driver"
       url="jdbc:postgresql://127.0.0.1:5432/myDataSource"
   />
   ```
8. The example above shows a simple PostgreSQL configuration. Replace the **Resource name**, **username**, **password**, **driverClassName**, and **url** parameters, or any relevant connection settings, to match your database connection information and the details you supplied in the `web.xml` file earlier.
9. Save and close the `context.xml` file.
10. Delete the `pentaho.xml` filed located in the `/tomcat/conf/catalina/` directory. The `pentaho.xml` is a cached copy of the context.xml file you modified. Since the cache is not usually configured to update frequently, you have to delete the `pentaho.xml` file and let Tomcat recreate it when it starts up.
11. [Start the Tomcat and Pentaho servers](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration).

Tomcat can now properly connect to your data.
