# Source: https://docs.pentaho.com/pba-metadata-editor/metadata-security-pentaho-metadata-editor-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/metadata-security-pentaho-metadata-editor-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/metadata-security-pentaho-metadata-editor-cp.md

# Metadata security

If you need to restrict access to certain portions of a metadata model that you are using as a data source, you must edit the model with Metadata Editor and add restrictions. The Pentaho metadata model offers table, column, and row-level authorization control. If you need to prevent certain users or roles from accessing it, you must change and republish the model.

* [Configure the security service](#configure-the-security-service)
* [Change security constraints](#change-security-constraints)
* [Remove security](#remove-security)
* [Remove security from the metadata domain repository](#remove-security-from-the-metadata-domain-repository)

## Configure the security service

The Pentaho Metadata Editor must be configured to connect to your Pentaho Server so that it can retrieve usernames, roles, and access control lists. You must know the base URL for the Pentaho Server (the default URL is `http://localhost:8080/pentaho`), as well as the name of the service to execute security information retrieval. The service that retrieves security information is ServiceAction.

Perform the following steps to define your security settings:

1. From the Pentaho Metadata Editor main window, select **Tools** > **Security**.

   The Security Service dialog box appears.
2. Type the correct URL in the **Service URL** text box.
3. Select the level of detailed security information you want: **All**, **Users**, or **Roles**.

   If you have hundreds of users in your system, you probably only want to return the roles, then use roles for security information properties. The access control lists are returned with all three options.
4. Type `admin` in the **User Name** text field.

   This is the default Admin user for the Pentaho User Console.
5. Type `password` in the **Password** text field.

   This password is associated with the default Admin user.
6. Click **Test**.

   If the information you entered is correct, a listing of users and roles appears, as shown in the following example:

   ![Security Service dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-1fa7fdfd654c33743c4b2599d44304269aa8f091%2FssPMESecurityService.png?alt=media)
7. Click **OK** to exit the test results, and then click **OK** to exit the Security Service dialog box.

### Retrieve security settings offline

If you want to work on your model and do not have access to the Pentaho Server, you can save your security information in a file. The Pentaho Metadata Editor retrieves your settings from the file instead of accessing the server every time you open your domain.

1. After you click **Test**, all of the XML between the `<content>` and `</content>` tags, including the tags, is provided in the XML dialog box.
2. Copy and paste the XML code into a text editor, and save the file as `metadata_security.xml` in a location of your choice.
3. Click **OK** to close the dialog box.
4. Click the **File** tab in the Security Service dialog box.
5. Browse to the file that you just saved.
6. Click **OK** to exit the dialog box.

## Change security constraints

Perform the following steps to change security constraints on a specific business table or column:

1. Open the Properties dialog box that contains the table or column you want to change.
2. Click the Plus Sign to add a property.

   ![Add Property button, Properties dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-ad66d6e15a1f1ef4b3fa6cb491d75d45c9aa5b11%2F41_pme_change_sec_constraints.png?alt=media)

   The Add New Property dialog box appears.
3. Select the **Security Information** property and click **OK**.
4. Scroll down to the **Metadata Security** section of the **Settings** panel and add the individual role or user permissions to the business model, table, or column.

   These permissions will be enforced in the Pentaho Server after publishing the new metadata model.

### Add column-level security constraints

You must have a connection to a data source in Metadata Editor and have one or more tables selected.

Perform the following steps to add user-based or role-based restrictions to your data source.

1. In the left pane, right-click the table or column you want to modify, then click **Edit** from the context menu.

   The Physical Table Properties dialog box appears.
2. Click **Add Property** above the **Available** field in the middle of the screen.

   The Add New Property dialog box appears.
3. Select **Metadata Security**, then click **OK**.
4. Click the new **Metadata Security** item in the **General** category.
5. Click the Plus Sign icon next to the **Selected Users/Groups** field in the right pane.

   A list of users and/or roles (depending on what you selected when configuring the security service earlier) appears.
6. Select the user or role in the **Available** list, and then click the Right Arrow in the middle of the window to assign permissions.

   The user or role moves from the **Available** list on the left to the **Assigned** list on the right.
7. Repeat this process for other users or roles you want to assign metadata permissions to, then click **OK**.
8. Change any other relevant metadata options, then click **OK** to return to the Metadata Editor main window.
9. When you are finished, save the metadata configuration as a domain using the **Save As** button, then publish it to the Pentaho Server as an XMI schema by selecting **Publish** from the **File** menu.

### Add global row-level security constraints

You must have a connection to a data source in Metadata Editor and have one or more tables selected.

A global constraint is an [MQL formula](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/mql-formula-syntax) statement that institutes a global restriction on the data you specify, down to the row level. Follow the instructions below to add custom global user- or role-based restrictions to your data source.

1. In the left pane, right-click the table or column you want to modify, then click **Edit** from the context menu.

   The Physical Table Properties dialog box appears.
2. Click the Plus Sign icon above the **Available** field in the middle of the screen.

   The Add New Property dialog box appears.
3. Select **Data Constraints**, then click **OK**.
4. Click the new **Data Constraints** item in the **General** category.
5. Select the **Global Constraint** option in the right pane.
6. Type in your constraint in the text box.
7. Change any other relevant metadata options, then click **OK** to return to the Metadata Editor main window.
8. When you are finished, save the metadata configuration as a domain using the **Save As** button, then publish it to the Pentaho Server as an XMI schema by selecting **Publish** from the **File** menu.

   When using the **Global Constraint**, a single MQL formula is used to define security for all users. In addition to the standard MQL functions available, there are also two additional functions:

   * `USER()`: Returns the name of the current user.
   * `ROLES()`: Returns a list of roles associated with the current user.\
     The following example defines an MQL formula that allows administrators full access:

   ```
   IN("Admin"; ROLES())
   ```

   **Note:** All other users have no access.

### Add user or role row-level security constraints

You must have a connection to a data source in Metadata Editor and have one or more tables selected.

A role-based constraint is an [MQL formula](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/mql-formula-syntax) statement that restricts access (on the row level) only to certain users or roles. Follow the instructions below to add fine-grained user- or role-based restrictions to your data source.

1. In the left pane, right-click the table or column you want to modify, then click **Edit** from the context menu.

   The Physical Table Properties dialog box appears.
2. Click the Plus Sign above the **Available** field in the middle of the screen.

   The **Add New Property** dialog box appears.
3. Select **Data Constraints**, then click **OK**.
4. Click the new **Data Constraints** item in the **General** category.
5. Select **Role Based Constraints** option in the right pane.
6. Click the Plus Sign next to the **Selected Users/Groups** field in the right pane.

   A list of users and/or roles (depending on what you selected when configuring the security service earlier) appears.
7. Click the user or role in the left pane that you want to assign permissions to, then click the Right Arrow in the middle of the window.

   The user or role moves from the **Available** list on the left to the **Assigned** list on the right.
8. Click the checkboxes for the permissions that you want to assign to the selected user or role.
9. Repeat this process for other users or roles you want to assign metadata permissions to, then click **OK**.
10. Change any other relevant metadata options, then click **OK** to return to the Metadata Editor main window.
11. When you are finished, save the metadata configuration as a domain using the **Save As** button, then publish it to the Pentaho Server as an XMI schema by selecting **Publish** from the **File** menu.

### Add role model-level security constraints

Row-level security allows you to control the results that are returned in a query based on a user's security level. You can specify which rows of data each User Role or User ID is allowed to retrieve from the database, based on a column of data or combination of columns of data. This is only valid at the business model-level.

In the Pentaho Metadata Editor, select the model to which you want to add row-level security, right-click the model, and select **Edit**.

![Business Model Properties dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-781595bfb39302814a660811e0716963c6c9f935%2F42_pme_role_based_security.png?alt=media)

Any data constraints defined below the model level, such as in a business table or business column, is ignored and not used. In the Business Model Properties dialog box, select the **General** > **Data Constraints**.

If you are using **Role Based Constraints**, the metadata engine determines which MQL constraints are appropriate for the current user and applies them to the current query. Constraints may be added for each Role and User in a system. If zero constraints match a user and his or her roles, no data is returned by the MQL query. If more than one constraint applies to a user, the constraints use the `OR` function to determine row visibility.

This example below defines an MQL formula for three different roles. The Admin role has full row visibility, the Sales and Engineering roles can access data that joins to rows associated with their specific department only.

| Role        | Constraint                      |
| ----------- | ------------------------------- |
| Admin       | `TRUE()`                        |
| Sales       | `[BC_DEPARTMENT]="Sales"`       |
| Engineering | `[BC_DEPARTMENT]="Engineering"` |

Row-level security constraints are applied at the MQL layer. The business columns referenced in the MQL security constraints will be resolved down to SQL table columns. The tables which contain column references included in security constraints will be joined to your query, based on the relationships defined in the business model. It is recommended that you do not use outer-joined business columns for the purposes of security constraints.

## Remove security

You can remove security by enabling anonymous access or by modifying data source management.

### Enable anonymous access

You can bypass the built-in security on the Pentaho Server by giving all permissions to anonymous users. An *"anonymousUser"* is any user, either existing or newly created, that you specify as an all-permissions, no-login user, and to whom you grant the Anonymous role.

**CAUTION:** The procedure below will grant full Pentaho Server access to the Anonymous role and never require a login.

All of the files you will be using are located in the `/pentaho/server/pentaho-server/pentaho-solutions/system` directory. Before you begin, stop the Pentaho Server.

#### Modify application security

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

#### Modify Pentaho configuration

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

#### Modify repository properties

Perform the following steps to modify the repository properties:

1. Open the `repository-spring.properties` file with the text editor.
2. Find the **singleTenantAdminAuthorityName** and replace the value with `Anonymous`.
3. Find the **singleTenantAdminUserName** and replace the value with the name\*\<your anonymous user>\*.
4. Save and close the `repository-spring.properties` file.

#### Map the appropriate role

Perform the following steps to map roles:

1. Find all references to the bean `id="Mondrian-UserRoleMapper"` and make sure that the only mapper uncommented (active) is the one shown in the following code example:

   ```xml

   <bean id="Mondrian-UserRoleMapper" name="Mondrian-SampleUserSession-UserRoleMapper" class="org.pentaho.platform.plugin.action.mondrian.mapper.MondrianUserSessionUserRoleListMapper" scope="singleton">
     <property name="sessionProperty" value="MondrianUserRoles" />
   </bean>

   ```
2. If you have made any changes to `pentahoObjects.spring.xml`, save and close the file.

You have now effectively worked around the security features of the Pentaho Server. If you are using the relational metadata database model, refer to **Remove Security from Metadata Domain Repository** for the next few steps.

### Remove security from data source management

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

## Remove security from the metadata domain repository

This procedure changes your default metadata domain repository so that it is no longer security-aware. It is a necessary step in completely removing security from the BA platform; however, this procedure does not, in itself, remove all security. To do that, start with by [enabling anonymous access](#enable-anonymous-access).

1. Stop the Pentaho Server and User Console.
2. Edit the `/pentaho-solutions/system/pentahoObjects.spring.xml` file.
3. Comment out the `IMetadataDomainRepositoryImpl` line, and uncomment the similar line below it. Alternatively, you can switch the value of `IMetadataDomainRepositoryImpl` from `org.pentaho.platform.plugin.services.metadata.SecurityAwareMetadataDomainRepository` to `org.pentaho.platform.plugin.services.metadata.PentahoMetadataDomainRepository`.

   ```
   <!-- <bean id="IMetadataDomainRepositoryImpl" 
     class="org.pentaho.platform.plugin.services.metadata.
       SecurityAwareMetadataDomainRepository" 
         scope="singleton"/> -->
   <!--  Use this schema factory to disable PMD security -->
   <bean id="IMetadataDomainRepositoryImpl" 
     class="org.pentaho.platform.plugin.services.metadata.PentahoMetadataDomainRepository" 
       scope="singleton"/>
   ```
4. Save and close the file.
5. Restart the Pentaho Server and User Console.

You have now switched the metadata domain repository to one that is not security aware. Access controls will no longer be enforced on various metadata objects.
