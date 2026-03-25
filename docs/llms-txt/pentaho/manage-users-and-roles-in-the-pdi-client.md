# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/manage-users-and-roles-in-the-pdi-client.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/manage-users-and-roles-in-the-pdi-client.md

# With the PDI client

Control users and roles in the Pentaho Repository with the PDI client. You must login to the PDI client (also known as Spoon) as an administrator (or be assigned to a role that has administer security permission) to manage users and roles for Pentaho security.

Here is how you can manage users:

* [Add users](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Change user passwords](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Delete users](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Assign users to roles](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Edit user information](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)

Here is how you can manage roles:

* [Add roles](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Edit roles](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Delete roles](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Make changes to the administrator role](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Assign user permissions in the repository using the PDI client](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)
* [Enable system role permissions](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/broken-reference)

Before changing security settings, play it safe and back up these relevant files:

* If you installed PDI using the Pentaho suite installer or custom methods, back up all Data Integration directories.
* If you installed PDI using the manual method, back up the `pentaho.war` file and solutions.

You can control users and roles in the Pentaho Repository with a point-and-click user interface. The users and roles radio buttons allow you to switch between user and role settings. You can add, delete, and edit users and roles from this page.

#### Sample users, default roles, and permissions

By viewing the sample users and default roles you can get ideas about ways to define actual users and specific roles.

1. Open the PDI client and log into the repository.

   See the **Pentaho Data Integration** document for details on the Pentaho Repository.
2. Click **Tools** > **Repository** > **Explore**.

   The Repository explorer page appears.
3. Select the **Security** tab.

   Available users are shown.

   ![Repository explorer Security tab](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-f244bd2e3eb7a06c599f96b03d519f623ef7f36d%2FPDI_Repository_Explorer_Security_tab.png?alt=media)
4. Choose if you want to manage security by **Users**, **Roles**, or **System Roles**:
   * Select **Users** then highlight a user to display the user's role and a description, if any.
   * Select **Roles** then highlight a role in the **Available** list to display **Permissions** for the user's role, as defined by the checked boxes. These roles, added for convenience, can be removed or altered based on your needs.

| Default Role     | Sample User | Permissions                                                                                                                                                                    |
| ---------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Administrator    | admin       | <ul><li>Administer Security</li><li>Schedule Content</li><li>Read Content</li><li>Publish Content</li><li>Create Content</li><li>Execute</li><li>Manage Data Sources</li></ul> |
| Power User       | suzy        | <ul><li>Schedule Content</li><li>Read Content</li><li>Publish Content</li><li>Create Content</li><li>Execute</li></ul>                                                         |
| Report Author    | tiffany     | <ul><li>Schedule Content</li><li>Publish Content</li></ul>                                                                                                                     |
| Business Analyst | pat         | <ul><li>Publish Content</li></ul>                                                                                                                                              |

Each default role and sample user features a standard set of permissions, which provides for a specific set of capabilities when using Pentaho tools and the Pentaho Server.

| Permissions         | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administer Security | <p>The default Administrator role automatically conveys all operation permissions to users assigned to that role, even if the check box next to it is cleared. This includes the <strong>Read Content</strong> and <strong>Create Content</strong> permissions, which are required for accessing the Administration perspective:- Allows access to and the ability to manage all content in each perspective.</p><ul><li>Allows the ability to view and work with all user schedules in the Schedules perspective.</li></ul> |
| Schedule Content    | <ul><li>Allows the user to schedule reports and content.</li><li>Gives the user the ability to view, edit, or delete their own schedules using the Schedules perspective.</li></ul>                                                                                                                                                                                                                                                                                                                                          |
| Read Content        | <ul><li>Gives the user the ability to view content in each perspective.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Publish Content     | <ul><li>Allows the user to store reports or data models in the Pentaho Repository.</li><li>When also granted the Create Content permission, the user can publish reports or data models to the repository.</li></ul>                                                                                                                                                                                                                                                                                                         |
| Create Content      | <ul><li>Allows the user to create, import, delete, and save jobs and transformations to the repository.</li><li>Gives the user the ability to see the data sources that are used to create jobs and transformations.</li><li>When also granted the Execute permission, the user can export jobs and transformations, copy and paste, and save the file in a virtual file system (VFS).</li></ul>                                                                                                                             |
| Execute             | <ul><li>Allows the user to run, preview, debug, replay, verify, and schedule.</li><li>When also granted the Create permission, the user can export jobs and transformations, copy and paste, and save the file in a VFS.</li></ul>                                                                                                                                                                                                                                                                                           |
| Manage Data Sources | <ul><li>Allows the user to create, edit, or delete new data sources.</li><li>Gives the user the ability to see a list of repository data sources.</li></ul>                                                                                                                                                                                                                                                                                                                                                                  |

\- Select \*\*System Roles\*\* then highlight a role in the \*\*Available\*\* list to display the \*\*Permissions\*\* for the user's system role. System roles are built-in roles used to control default behaviors and permissions of the repository, handled implicitly or through system configuration, with automatic assignments.

#### Hide a user Home folder in PDI

If your organization implements multi-tenancy, you may not want individual users to see their Home folders for security reasons. If you need to keep all PDI user-created content in a centralized, secure folder location, you can hide individual users' Home folders. See the **Administer Pentaho Data Integration and Analytics** document for details.

#### Add users

* Select **Users**, then click the Plus Sign next to **Available**.

  The Add User dialog box appears.
* Enter the **User Name** and **Password** associated with your new user account in the appropriate fields.

  An entry in the **Description** field is optional.
* If you have available roles that can be assigned to the new user, under **Member**, select a role and click **OK**.

  The role you assigned to the user appears in the right pane under **Assigned**.
* Click **OK** to save your new user account and exit the Add User dialog box.

  The name of the user you added appears in the list of available users.

#### Change user passwords

* Select **Users**, then highlight the user for whose password you want to change then click the **Edit** icon.

  The Edit User dialog box appears.
* In the **Password** field, type the new password. Click **OK**.

  The password is changed and the user is able to login with the new password.

  **Note:** When you log in to the PDI client for the first time, it is a best practice to change the default administrator password.

#### Delete users

**Note:** We recommend that you disable a user or role instead of deleting it.

1. Select **Users**, then highlight the user to be deleted in the **Available** list.
2. Next to **Available**, click the **X** icon.

   A security message appears.
3. Click **Yes** to remove the user.

   The specified user is deleted.

If a user or role is deleted in the Pentaho Repository, content that refers to the deleted user, either by way of owning the content or having an ACL that mentions the user or role, is left unchanged. This situation makes it possible to create a new user or role using an identical name. In this scenario, content ownership and access control entries referring to the deleted user or role now apply to the new user or role. To avoid this problem, disable a user or role to prevent the creation of a user or role with an identical name. Use these alternatives rather than deleting the user or role.

| If...                    | Then...                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| You are disabling a role | Unassign all current members associated with the role.                                                          |
| You are disabling a user | Reset the password to a password that is so cryptic that it is impossible to guess and is unknown to any users. |

#### Assign users to roles

* Click **Roles**.

  The list of available roles appears.
* Select the role to which you are assigning users.

  If the role has users currently assigned to it, the names of the users appear in the table on the right under Members. You can assign or unassign any users to a role. You can select a single item or multiple items from the list of members. Click **Remove** to remove the user assignment.
* Next to **Members**, click the Plus Sign.

  The Add User to Role dialog box appears.
* Select the users you want assigned to the role and click the Right Arrow.

  The users assigned to the role appear in the right pane.
* Click **OK** to save your entries and exit the Add User to Role dialog box.

  The specified users are assigned to the specified role.

#### Edit user information

* Select **Users**, then highlight the user you want to edit in the **Available** list.
* Click the **Edit** icon.

  The Edit User dialog box appears.
* Make the appropriate changes to the user information.
* Click **OK** to save your changes and exit the Edit User dialog box.

#### Add Roles

* Click **Roles**.

  The list of available roles appear.
* Click the Plus Sign next to **Available**.

  The Add Role dialog box appears.
* Enter the **Role Name**.

  An entry in the **Description** field is optional.
* If you have users to assign to the new role, select them (using SHIFT or CTRL) from the list of available users and then click the Right Arrow.

  The user(s) assigned to your new role appear in the right pane.
* Click **OK** to save your entries and exit the Add Role dialog box.

  The specified role is created and is ready to be assigned to user accounts.

#### Edit roles

* Click **Roles**.

  The list of available roles appear.
* Select the role you want to edit and click the **Edit** icon.

  The Edit Role dialog box appears.
* Make the appropriate changes.
* Click **OK** to save your changes and exit the Edit Role dialog box.

#### Delete roles

* Click **Roles**.

  The list of available roles appears.
* Select the role you want to delete from the **Available** list.
* Click the **X** icon next to **Available**.

  A security message appears.
* Click **Yes** to remove the role.

  The specified role is deleted.

#### Make changes to the administrator role

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

#### Assign user permissions in the repository using the PDI client

You can restrict what users see by assigning roles to users. For example, you can create administrative groups who are allowed permissions in the repository to administer security and create new content.

1. Click **Roles**.

   The list of available roles appears.
2. In the **Available** list, highlight the role to which you are assigning permissions.
3. In the **Permission** list, select the check boxes to enable (or deselect to disable) permissions, then click **Apply**.

   The permissions you enabled for the role take effect the next time the specified user(s) login.

#### Enable system role permissions

Pentaho requires the authenticated system role for users, including administrative users, to login to the Pentaho Repository. Pentaho Repository users are automatically assigned the **Authenticated** system role, in addition to the role you assigned them, at login. By default, the authenticated system role provides **Read Content** permission. You can change permissions as needed.

**Note:** The anonymous system role is non-functional and not being used at this time.

1. Click **System Roles**.

   System roles appear in the **Available** list.
2. Select the **Authenticated** role.
3. Under **Permissions**, select the check boxes to enable (or clear to disable) permissions for this role.
4. Click **Apply** to save your changes.

   The specified permissions are enabled for the authenticated system role.
