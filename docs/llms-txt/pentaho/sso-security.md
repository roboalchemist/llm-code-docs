# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/sso-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/advanced-security-providers/sso-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/sso-security.md

# SSO security

This section contains instructions for configuring the Pentaho Server to work with the Central Authentication Service (CAS) single sign-on (SSO) framework.

You can integrate Pentaho with Central Authentication Service (CAS). You must have a CAS server installed and running before you continue.

Perform the following steps to integrate Pentaho with CAS.

1. Stop the Pentaho Server
2. Download the following files and copy them to the `pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib` directory.
   * <https://repo1.maven.org/maven2/org/jasig/cas/cas-client-core/3.1.10/cas-client-core-3.1.10.jar>
   * <https://repo1.maven.org/maven2/org/springframework/security/spring-security-cas-client/3.0.8.RELEASE/spring-security-cas-client-3.0.8.RELEASE.jar>
3. Navigate to the `pentaho-server/pentaho-solutions/system` directory and open the `pentaho-spring-beans.xml` file with any text editor.
   1. Add the `<import resource="applicationContext-spring-security-cas.xml"/>` to the list of imports after all the other `applicationContext*.xml` files.
   2. Save and close the file.
4. Navigate to the `pentaho-server/pentaho-solutions/system` directory and open the `applicationContext-spring-security-cas.xml` file with any text editor. Update the file using the following steps:

   **Note:** You must use the publicly available IP address for all URLs in this file.

   1. If you are using Pentaho with SSL, then update the references for <https://localhost:8443/cas> to your working CAS server URL.

      The CAS Server must use SSL. Contact your CAS Administrator if you need to add SSL security to your CAS instance.
   2. Locate the bean containing the ID for `casAuthenticationProvider`.

      ```xml
      <bean id="casAuthenticationProvider"
      class="org.springframework.security.providers.cas.CasAuthenticationProvider">
      <property name="userDetailsService">
       <ref bean="userDetailsService" />
      </property>
      ```
   3. Change the bean ID based on your configuration to the applicable one as shown below.

      ```xml
      casAuthenticationProvider.jdbcUserDetailsService
      ```

      ```xml
      casAuthenticationProvider.ldapUserDetailsService
      ```
   4. Save and close the file.
5. Navigate to the `pentaho-server/tomcat/webapps/pentaho/WEB-INF` directory and open the `web.xml` file.
   1. Add the following lines to their applicable sections in the file:

      ```xml
      <servlet>
        <servlet-name>casFailed</servlet-name>
        <jsp-file>/jsp/casFailed.jsp</jsp-file>
      </servlet>
      ```

      ```xml
      <servlet-mapping>
        <servlet-name>casFailed</servlet-name>
        <url-pattern>/public/casFailed</url-pattern>
      </servlet-mapping>casAuthenticationProvider.hibernateUserDetailsService
      ```

      ```xml
      <listener>
          <listener-class>org.jasig.cas.client.session.SingleSignOutHttpSessionListener</listener-class>  
      </listener>
      ```
   2. Save and close the file.

      **Note:** The casFailed entries are CAS login flow dependent and must be defined and configured by the CAS Administrator on the CAS server. These entries cover cases such as what happens when the user enters the wrong password or similar issues authenticating. The action taken depends on the CAS login flow definition.
6. Start the Pentaho Server.

The Pentaho Server is now configured to authenticate users against your central authentication server.

### Configure session timeout

Connection timeout issues when using CAS with the Pentaho Server can result in the inability to login or re-load data in the web client page until you refresh the page. To avoid problems with the session timing out, perform the following steps to configure the session timeout:

1. Stop the Pentaho Server.
2. Navigate to the `pentaho-server/tomcat/webapps/pentaho/WEB-INF` directory and open the `web.xml` file with any text editor.
   1. Find the **session-config** property and edit the **session-timeout** value (the default value is 120 minutes) to increase the period to a value that is greater than the setting used for your CAS server session timeout value:

      ```xml

      <session-config>
        <tracking-mode>COOKIE</tracking-mode>
        <session-timeout>120</session-timeout>
      </session-config>

      ```
   2. Locate the `Pentaho Web Context Filter` and add the following **init-param**:

      ```xml

      <init-param>
        <param-name>ssoEnabled</param-name>
        <param-value>true</param-value>
      </init-param>

      ```
   3. Save and close the file.
3. Activate the session timeout dialog box:
   1. Navigate to the `pentaho-server/pentaho-solutions/system` directory and open the `applicationContext-spring-security-cas.xml` file then locate the `httpSessionPentahoSessionContextIntegrationFilter` bean id.
   2. Find the **ssoEnabled** property and set the value from true to false.
   3. Save and close the file.
4. Restart the Pentaho Server.
