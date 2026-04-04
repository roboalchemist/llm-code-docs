# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/schedule-jobs-to-run-on-a-remote-carte-server.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/schedule-jobs-to-run-on-a-remote-carte-server.md

# Schedule Jobs to Run on a Remote Carte Server

The following instructions are needed to schedule a job to run on a remote Carte server. Without making these configuration changes, you will be unable to remotely run scheduled jobs.

**Note:** This process is also required for using the Pentaho Server as a load balancer in a dynamic Carte cluster.

1. Stop the Pentaho Server and remote Carte server.
2. Copy the `repositories.xml` file from the `.kettle` directory on your workstation to the same location on your Carte slave. Without this file, the Carte slave will be unable to connect to the Pentaho Repository to retrieve PDI content.
3. Open the `/pentaho/server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/web.xml file` with a text editor.
4. Find the **Proxy Trusting Filter** filter section, and add your Carte server's IP address to the **param-value** element.

   ```xml
   <filter>
       <filter-name>Proxy Trusting Filter</filter-name>
       <filter-class>org.pentaho.platform.web.http.filters.ProxyTrustingFilter</filter-class>
       <init-param>
         <param-name>TrustedIpAddrs</param-name>
         <param-value>127.0.0.1,192.168.0.1</param-value>
         <description>Comma separated list of IP addresses of a trusted hosts.</description>
       </init-param>
       <init-param>
         <param-name>NewSessionPerRequest</param-name>
         <param-value>true</param-value>
         <description>true to never re-use an existing IPentahoSession in the HTTP session; needs to be true to work around code put in for BISERVER-2639</description>
       </init-param>
   </filter>
   ```
5. Uncomment the proxy trusting filter-mappings between the `<!-- begin trust -->` and `<!-- end trust -->` markers.

   ```xml
   <!-- begin trust --> 
     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/authorizationPolicy</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/roleBindingDao</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/userRoleListService</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/unifiedRepository</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/userRoleService</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/Scheduler</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/webservices/repositorySync</url-pattern>
     </filter-mapping>
     
     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/api/system/authentication-provider</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/api/session/userName</url-pattern>
     </filter-mapping>
     <!-- end trust -->
   ```
6. Save and close the file.
7. If your Carte server is running on Windows, perform the following steps to add `-Dpentaho.repository.client.attemptTrust=true` to the `Carte.bat` startup script:
   1. Open the `Carte.bat` startup script with a text editor.
   2. Add the following command in between the `REM` comment for `-Dloginmodulename=%JAAS_LOGIN_MODULE_NAME%` and the call to `Spoon.bat`:

      `SET OPT=%OPT% -Dpentaho.repository.client.attemptTrust=true org.pentaho.di.www.Carte "${1+$@}"`
   3. Save and close the file.
8. If your Carte server is running on Linux, perform the following steps to add `-Dpentaho.repository.client.attemptTrust=true` to the `Carte.sh` startup script:
   1. Open the `Carte.sh` startup script with a text editor.
   2. Add the following command after the `if/fi` condition for `-Djava.awt.headless=true` and before `export OPT`:

      `OPT="$OPT -Dpentaho.repository.client.attemptTrust=true org.pentaho.di.www.Carte \"${1+$@}\""`
   3. Save and close the file.
9. Start your Carte server and Pentaho Server

You can now schedule a job to run on a remote Carte instance.
