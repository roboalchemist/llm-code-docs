# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/pentaho-server-security/pass-authentication-credentials-in-url-parameters/remove-pentaho-server-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/pentaho-server-security/remove-pentaho-server-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/pentaho-server-security/remove-pentaho-server-security.md

# Remove Pentaho Server security

You can remove Pentaho Server security by enabling anonymous access or by modifying data source management.

## Enable anonymous access

You can bypass the built-in security on the Pentaho Server by giving all permissions to anonymous users. An *"anonymousUser"* is any user, either existing or newly created, that you specify as an all-permissions, no-login user, and to whom you grant the Anonymous role.

**CAUTION:** The procedure below will grant full Pentaho Server access to the Anonymous role and never require a login.

All of the files you will be using are located in the `/pentaho/server/pentaho-server/pentaho-solutions/system` directory. Before you begin, stop the Pentaho Server.

### Modify application security

Perform the following steps to modify application security:

1. Open the `applicationContext-spring-security.xml` file with any text editor.
2. Make sure that a default anonymous role is defined. Match your bean definition and property value to the code shown in the following example:

   ```xml

   <bean id="anonymousProcessingFilter" class="org.springframework.security.web.authentication.AnonymousAuthenticationFilter">
     <constructor-arg value="foobar" />
     <constructor-arg value="anonymousUser" />
     <constructor-arg>
       <list>
         <bean class="org.springframework.security.core.authority.SimpleGrantedAuthority">
           <constructor-arg value="Anonymous" />
         </bean>
       </list>
     </constructor-arg>
   </bean>

   ```

   **Note:** These next steps permit PDI client tools to publish to the Pentaho Server without having to supply a user name and password.
3. Find these two beans in the same file from the previous step.
   * `filterInvocationInterceptor`
   * `filterInvocationInterceptorForWS`
4. Locate the **securityMetadataSource** property inside the beans and match the contents to the code shown in the following example:

   ```xml

   <bean id="filterInvocationInterceptor" class="org.springframework.security.web.access.intercept.FilterSecurityInterceptor">
     <property name="authenticationManager" ref="authenticationManager" />
     <property name="accessDecisionManager" ref="httpRequestAccessDecisionManager" />
     <property name="securityMetadataSource">
       <sec:filter-security-metadata-source request-matcher="ciRegex" use-expressions="false">
         <!-- all patterns have Anonymous role access -->
         <sec:intercept-url pattern="\A/.*\Z" access="Anonymous,Authenticated" />
       </sec:filter-security-metadata-source>
     </property>
   </bean>

   ```
5. Save and close the `applicationContext-spring-security.xml` file.

### Modify Pentaho configuration

Perform the following steps to modify the Pentaho configuration:

1. Open the `pentaho.xml` file with the text editor.
2. Find the `anonymous-authentication` lines of the `pentaho-system` section, and define the anonymous user and role as shown in the following code example:

   ```xml

   <pentaho-system>
   <!-- omitted -->
     <anonymous-authentication>
       <anonymous-user>anonymousUser</anonymous-user>
       <anonymous-role>Anonymous</anonymous-role>
     </anonymous-authentication> <!-- omitted -->
   </pentaho-system>

   ```
3. Save and close the `pentaho.xml` file.

### Modify repository properties

Perform the following steps to modify the repository properties:

1. Open the `repository-spring.properties` file with the text editor.
2. Find the **singleTenantAdminAuthorityName** and replace the value with `Anonymous`.
3. Find the **singleTenantAdminUserName** and replace the value with the name\*\<your anonymous user>\*.
4. Save and close the `repository-spring.properties` file.

### Map the appropriate role

Perform the following steps to map roles:

1. Find all references to the bean `id="Mondrian-UserRoleMapper"` and make sure that the only mapper uncommented (active) is the one shown in the following code example:

   ```xml

   <bean id="Mondrian-UserRoleMapper" name="Mondrian-SampleUserSession-UserRoleMapper" class="org.pentaho.platform.plugin.action.mondrian.mapper.MondrianUserSessionUserRoleListMapper" scope="singleton">
     <property name="sessionProperty" value="MondrianUserRoles" />
   </bean>

   ```
2. If you have made any changes to `pentahoObjects.spring.xml`, save and close the file.

You have now effectively worked around the security features of the Pentaho Server. If you are using the relational metadata database model, refer to **Remove Security from Metadata Domain Repository** for the next few steps.

## Remove security from data source management

This procedure changes your data source management so that an anonymous user can access it. These steps are necessary to completely remove security from the Pentaho Server. However, this procedure does not remove all security. If you need to remove all security, enable anonymous access as described above.

Perform the following steps to completely remove security from the Pentaho Server:

1. If you need to, **stop the Pentaho Server**
2. Open `/pentaho/server/pentaho-server/pentaho-solutions/system/data-access/settings.xml` file with a text editor.
   1. Find the `<data-access-roles>Administrator</data-access-roles>` line in the file and change the following text:

      ```
      Administrator to Anonymous
      ```
   2. Find the `<data-access-view-roles>Authenticated,Administrator</data-access-view-roles>` line in the file and change the following text:

      ```
      Authenticated,Administrator to Anonymous
      ```
   3. Find the `<data-access-view-users>suzy</data-access-view-users>` line and change the following text:

      ```
      suzy to anonymousUser
      ```
   4. Find the `<data-access-datasource-solution-storage>admin</data-access-datasource-solution-storage>` line and change the following text:

      ```
      admin to anonymousUser
      ```
3. Save and close the file.
4. Restart the Pentaho Server.
