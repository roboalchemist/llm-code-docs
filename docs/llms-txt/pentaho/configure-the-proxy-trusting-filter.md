# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/configure-the-proxy-trusting-filter.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/configure-the-proxy-trusting-filter.md

# Configure the proxy trusting filter

If you have set the Pentaho Server to run on a specific IP address or hostname other than the default 127.0.0.1, you must modify the trusted proxy to match that address or hostname for Pentaho plugins to run as expected. Additionally, if you have applications that access Pentaho Server resources, such as REST APIs, you must add that application's IP address so that the Pentaho Server will accept those requests.

1. Stop the Pentaho Server.
2. Open `pentaho-server/tomcat/webapps/pentaho/WEB-INF/web.xml` and search for `TrustedIpAddrs`.

   **Note:** The **param-value** immediately below `TrustedIpAddrs` is a comma-separated list of IP addresses that should be trusted.
3. Add the IP address of the host machine.

   ```xml
   <filter>
       <filter-name>Proxy Trusting Filter</filter-name>
       <filter-class>org.pentaho.platform.web.http.filters.ProxyTrustingFilter</filter-class>
           <init-param>
               <param-name>TrustedIpAddrs</param-name>
               <param-value>127.0.0.1</param-value>
               <description>Comma separated list of IP addresses of a trusted hosts.</description>
           </init-param>
   </filter>
   ```
4. Start the Pentaho Server.
