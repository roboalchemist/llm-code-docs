# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/remove-sample-data-from-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/remove-sample-data-from-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/remove-sample-data-from-the-pentaho-server.md

# Remove sample data from the Pentaho Server

By default, you have access to a sample data source and a solution directory filled with example content. These samples are provided for testing with sample data. When you are ready to move from a testing scenario to development or production, you can remove the sample content.

Perform the following steps to completely remove the sample data and content:

1. Stop the Pentaho Server.
2. Delete the `samples.zip` file from the `/pentaho-server/pentaho-solutions/system/default-content` directory.

   If you performed a manual WAR build and deployment, then the file path is: `/pentaho-server/pentaho-solutions/system`.
3. Edit the `/pentaho/WEB-INF/web.xml` file inside of the deployed `pentaho.war`.

   If you used an archive installation method, the path to the WAR file should be `/pentaho-server/tomcat/webapps/pentaho/WEB-INF/web.xml`. If you performed a manual WAR build and deployment, you must adjust the path to fit your specific configuration.
4. Remove the `hsqldb-databases` section from the `/pentaho/WEB-INF/web.xml` file:

   ```xml
   <!-- [BEGIN HSQLDB DATABASES] -->
       <context-param>
           <param-name>hsqldb-databases</param-name>
           <param-value>sampledata@../../data/hsqldb/sampledata</param-value>
       </context-param>
   <!-- [END HSQLDB DATABASES] -->
   ```
5. Remove the `hsqldb-starter` section from the `/pentaho/WEB-INF/web.xml` file:

   ```xml
   <!-- [BEGIN HSQLDB STARTER] --> 
   <listener> 
   <listener-class>org.pentaho.platform.web.http.context.HsqldbStartupListener</listener-class> 
   </listener> 
   <!-- [END HSQLDB STARTER] -->
   ```
6. Remove the `SystemStatusFilter`:

   **Note:** The `SystemStatusFilter` filter is not part of the samples. The filter shows error status messages that are only useful for development and testing purposes, and should be removed from a production system.

   ```xml
   <filter>
       <filter-name>SystemStatusFilter</filter-name>
       <filter-class>com.pentaho.ui.servlet.SystemStatusFilter</filter-class>
       <init-param>
           <param-name>initFailurePage</param-name>
           <param-value>InitFailure</param-value>
           <description>This page is displayed if the PentahoSystem fails to properly initialize.</description>
       </init-param>
   </filter>
   ```
7. Remove the filter mapping for the `SystemStatusFilter`:

   ```xml
   <filter-mapping>
       <filter-name>SystemStatusFilter</filter-name>
       <url-pattern>/*</url-pattern>
   </filter-mapping>
   ```
8. Save and close the `web.xml` file.
9. Delete the `/pentaho-server/data/` directory.

   The `/pentaho-server/data/` directory contains a sample database, control scripts for that database, the environment settings it needs to run, and SQL scripts to initialize a new repository.
10. Restart the Pentaho Server, then sign into the Pentaho User Console with the administrator username and password, go to the Browse Files page, and perform the following steps:
    1. In the **Folders** pane, expand the **Public** folder and click to highlight the folder containing the Steel Wheels sample data. Click **Move to Trash** in the **Folder Actions** pane and confirm the deletion.
    2. Highlight the folder containing the Pentaho Operations Mart sample data. Click **Move to Trash** in the **Folder Actions** pane and confirm the deletion.

The Pentaho Server instance is now cleaned of sample data and content.
