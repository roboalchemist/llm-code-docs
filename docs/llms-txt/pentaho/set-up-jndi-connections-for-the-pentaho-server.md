# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server.md

# Set up JNDI connections for the Pentaho Server

If you installed the Pentaho Server using the manual installation method, then you specified data connections to the [Tomcat](http://tomcat.apache.org/) web application server. To modify existing connections or define more JNDI connections, perform the following set of instructions.

You must be an IT administrator, know where data you are managing is stored, how to connect to the data, details about the computing environment, and how to use the command line to issue commands for Microsoft Windows or Linux. You should also know how to install a database and a web application server.

## Defining JNDI connections for PDI clients

If you are publishing to the Pentaho Server from a PDI client, Pentaho supplies a method for you to configure your PDI client to have the same JNDI connection information as the Pentaho Server. By using this method, your application server will not be continuously running during the development and testing of transformations.

* To configure a JNDI connection for your PDI client, edit the `jdbc.properties` file to mirror the JNDI connection information of your application server data sources. The `jdbc.properties` file is located here: `/pentaho/design-tools/data-integration/simple-jndi`.

## Tomcat JNDI connections

If you installed the Pentaho Server using the manual installation method, then you specified data connections to your Tomcat web application server. If you want to modify existing connections or add more connections, perform the following tasks.

Database connection and network information, such as the username,
\
password, driver class information, IP address or domain name, and port
\
numbers for your Pentaho Repository database are stored in the context.xml
\
file. Modify this file to reflect the database connection and network information to reflect your operating environment. You also modify the values for the
\
validationQuery parameters in this file if you have chosen to use a Pentaho
\
Repository database other than PostgreSQL.

#### Procedure

1. Stop the Tomcat and Pentaho Servers. For instructions on starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Consult your database documentation to determine the class name and connection string for your database.
3. Edit the `/tomcat/webapps/pentaho/WEB-INF/web.xml` file.
4. At the end of the element, in the same part of the file where you see `<!-- insert additional resource-refs -->`, add the following XML snippet:

   ```shellscript
   <resource-ref>
       <description>myDataSource</description>
       <res-ref-name>jdbc/myDataSource</res-ref-name>
       <res-type>javax.sql.DataSource</res-type>
       <res-auth>Container</res-auth>
   </resource-ref>
   ```

   Change the `description` and `res-ref-name` nodes, as well as any others that apply to your situation and fit your database. You may need to consult the **JNDI Resources** article in the [Apache Tomcat documentation](https://tomcat.apache.org/) to see if there are other components to consider.
5. Save and close the `web.xml` file.
6. Edit the `/tomcat/conf/context.xml` with a text editor. Alternatively, you can modify the `/tomcat/webapps/pentaho/META-INF/context.xml` file if you want this data connection to be available only to the Pentaho Server. Adding JNDI connections to the `context.xml` makes them available to all of the webapps deployed to this Tomcat instance.
7. Anywhere inside of the `Context` element, add the following XML snippet:

   <pre class="language-shellscript"><code class="lang-shellscript">&#x3C;Resource name="jdbc/myDataSource"
       auth="Container" type="javax.sql.DataSource"
   <strong>    factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
   </strong>    maxActive="20"
       maxIdle="5"
       maxWait="10000"
       username="dbuser"
       password="password"
       driverClassName="org.postgresql.Driver"
       url="jdbc:postgresql://127.0.0.1:5432/myDataSource"
   />
   </code></pre>
8. The example above shows a simple PostgreSQL configuration. Replace the `Resource name`, `username`, `password`, `driverClassName`, and `url` parameters, or any relevant connection settings, to match your database connection information and the details you supplied in the `web.xml` file earlier.
9. Save and close the `context.xml` file.
10. Delete the `pentaho.xml` file located in the `/tomcat/conf/catalina/` directory. The `pentaho.xml` is a cached copy of the `context.xml` file you modified. Since the cache is not usually configured to update frequently, you have to delete the `pentaho.xml` file and let Tomcat recreate it when it starts up.
11. Start the Tomcat and Pentaho servers.&#x20;

**Result:** Tomcat can now properly connect to your data.

### Add drivers

The Pentaho Server needs the appropriate driver to connect to the database that stores your data. Your database administrator, Chief Intelligence Officer, or IT manager should be able to provide the appropriate driver. If not, you can download drivers from your database vendor's website. The [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) contains a list of drivers.

Once you have the correct driver, copy it to the following directories:

* Pentaho Server: `/pentaho/server/pentaho-server/tomcat/lib/`
* PDI client: `data-integration/lib`

You must restart PDI client for the driver to take effect.

There should be only one driver for your database in the directory. Ensure that there are no other versions of the same vendor's driver in this directory. If there are, back up the old driver files and remove them to avoid version conflicts. This is a concern when you are adding a driver for the same database type as your Pentaho Repository. If you have any concerns about how to proceed, contact [Pentaho Support](https://support.pentaho.com/).

#### Driver for Microsoft SQL Server

If you are using a Microsoft SQL Server (MSSQL), you might need to use an alternative, nonvendor-supported driver called JTDS. Contact [Pentaho Support](https://support.pentaho.com/) to ensure that you are adding the correct driver.

For Microsoft Windows, most JDBC drivers support Type 2 integrated authentication through
\
the integratedSecurity connection string property. To use integrated authentication,
\
copy the sqljdbc\_auth.dll file to all machines and directories to which you copied the
\
JDBC driver. You can find this file in this location: `<installation directory>\sqljdbc_<version>\<language>\auth\`

<table><thead><tr><th width="317">If running:</th><th>Use the sqljdbc_auth.dll file here:</th></tr></thead><tbody><tr><td>64-bit JVM on a x64 processor</td><td>x64 folder</td></tr><tr><td>64-bit JVM on an Itanium processor</td><td>IA64 folder</td></tr></tbody></table>
