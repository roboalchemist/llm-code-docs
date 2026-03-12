# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-10-update-the-security-file.md

# Step 10: Update the security file

The default configuration of the Pentaho suite includes an extra layer of protection which prevents certain types of session fixation vulnerabilities. This feature can only be enabled on application servers which support the Java Servlet standard 3.1 and later. Because versions of the JBoss web application server prior to JBoss 7.0 do not support this standard, the following changes are required.In the `applicationContext-spring-security.xml` file, remove the following beans so Pentaho starts correctly.

1. Navigate to the `pentaho-server/pentaho-solution/system` folder and open the `applicationContext-spring-security.xml file` with a text editor.
2. Find and remove all occurrences of the following string (including the comma):

   ```xml
   sessionMgmtFilter,
   ```
3. Find and remove the following code:

   ```xml
   <bean id="sas" class="org.springframework.security.web.authentication.session.ChangeSessionIdAuthenticationStrategy" />
   ```
4. Find and remove the following code:

   ```xml

   <property name="sessionAuthenticationStrategy" ref="sas" />
   ```
5. Find and remove the following code:

   ```xml
   <bean id="httpSessionSecurityContextRepository" class="org.springframework.security.web.context.HttpSessionSecurityContextRepository"/>
   ```
6. Find and remove the following block of code:

   ```xml
   <bean id="sessionMgmtFilter" class="org.springframework.security.web.session.SessionManagementFilter"> 
   <constructor-arg ref="httpSessionSecurityContextRepository"/> 
   <constructor-arg ref="sas"/> 
   </bean>
   ```
7. Save and close the file.
