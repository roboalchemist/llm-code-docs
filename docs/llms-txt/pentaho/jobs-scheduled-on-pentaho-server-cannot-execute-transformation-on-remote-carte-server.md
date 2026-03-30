# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/jobs-scheduled-on-pentaho-server-cannot-execute-transformation-on-remote-carte-server.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/jobs-scheduled-on-pentaho-server-cannot-execute-transformation-on-remote-carte-server.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/jobs-scheduled-on-pentaho-server-cannot-execute-transformation-on-remote-carte-server.md

# Jobs scheduled on Pentaho Server cannot execute transformation on remote Carte server

You may see an error similar to the following message when trying to schedule a job to run on a remote Carte server:

```
ERROR 11-05 09:33:06,031 - !UserRoleListDelegate.ERROR_0001_UNABLE_TO_INITIALIZE_USER_ROLE_LIST_WEBSVC!
                com.sun.xml.ws.client.ClientTransportException: The server sent HTTP status code 401: Unauthorized 
```

You need to make the following configuration changes to remotely execute scheduled jobs:

**Note:** This process is also required for using the Pentaho Server as a load balancer in a dynamic Carte cluster.

1. Stop the Pentaho and Carte servers.
2. Copy the `repositories.xml` file from the `.kettle` folder on your workstation to the same location on your Carte slave. Without this file, the Carte slave will be unable to connect to the Pentaho Server to retrieve PDI content.
3. Open the `pentaho/server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/web.xml` file in a text editor.
4. Find the `Proxy Trusting Filter` section, then add your Carte server's IP address to the `param-value` element. The following code block is a sample of the `Proxy Trusting Filter` section:

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
5. Find the following code snippet in the `web.xm` file:

   ```xml

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/i18n</url-pattern>
     </filter-mapping>
   ```
6. After the code snippet above, add the following text in your file:

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
       <url-pattern>/api/session/userName</url-pattern>
     </filter-mapping>

     <filter-mapping>
       <filter-name>Proxy Trusting Filter</filter-name>
       <url-pattern>/api/system/authentication-provider</url-pattern>
     </filter-mapping>
     <!-- end trust -->
   ```
7. Save and close the file.
8. Edit the `Carte.bat` (Windows) or `carte.sh` (Linux) startup script on the machine that runs your Carte server.
9. Set an **OPT** variable to `-Dpentaho.repository.client.attemptTrust=true`, as shown in the following sample line of code:
   * Windows:

     ```java
     SET OPT=%OPT% "-Dpentaho.repository.client.attemptTrust=true"
     ```
   * Linux:

     ```java
     OPT="$OPT -Dpentaho.repository.client.attemptTrust=true"
     ```
10. Save and close the file, then start your Carte and Pentaho servers.

You can now schedule a job to run on a remote Carte instance.
