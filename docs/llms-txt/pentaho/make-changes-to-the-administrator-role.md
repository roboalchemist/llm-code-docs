# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/manage-users-and-roles-in-the-pdi-client/make-changes-to-the-administrator-role.md

# Make changes to the administrator role

The assignment of action-based permissions associated with the administrator role (read, create, execute, and administrate) in the Pentaho Repository cannot be edited in the user interface. The administrator role is the only role that is assigned the administer security permission and controls user access to the **Security** tab.

**Note:** Deleting the administrator role will prevent all users from accessing the **Security** tab unless another role is assigned the administrator permission.

These are the scenarios that require a configuration change that is unavailable through the PDI client:

* You want to delete the administrator role
* You want to unassign the administrator permission from the administrator role
* You want to configure LDAP

Follow these instructions to change the administrator role:

1. Shut down the Pentaho Server.
2. Open the `repository.spring.xml` file located at `pentaho-server/pentaho-solutions/system`.
3. Locate the element with an ID of **immutableRoleBindingMap**.
4. Replace the entire node with the XML code shown below.

   Make sure you change **yourAdminRole** to the role that will have Administrate permission.

   ```
   <util:map id="immutableRoleBindingMap">
       <entry key="yourAdminRole">
         <util:list>
           <value>org.pentaho.di.reader</value>
           <value>org.pentaho.di.creator</value>
           <value>org.pentaho.di.securityAdministrator</value>
         </util:list>
       </entry>
   </util:map>
   ```
5. Restart the Pentaho Server.

   The administrator role changes according to your requirements.
