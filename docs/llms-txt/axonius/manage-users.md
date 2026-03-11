# Source: https://docs.axonius.com/docs/manage-users.md

# Managing Users

Implement Axonius Role Based Access Control (RBAC) and compartmentalized access by assigning each Axonius user to a specific role and Data Scope. A role consists of a predefined set of permissions for working with Axonius modules and capabilities. This means that any changes to the role permissions affect all the users to whom the role is assigned. Assign users a [data scope](/docs/data-scope-management) to control the data each user can see.

All changes to users and roles are recorded in the [Activity Log](/docs/activity-logs-page).

See [Manage Roles](/docs/manage-roles) for more information about managing roles.

## Required Permissions

To manage users, a user must have an administrator role and have the Manage Users permission.

## Accessing the Users Page

**To access the Users page:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/System%20Settings%20icon.png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Users**.

The page displays the list of defined Axonius users, and each user's role and permissions.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsersPageNew.png)

## Searching and Filtering the Users List

Use the Search bar at the top of the page to find a specific user and to filter the list of users displayed.

<Image alt="UsersSearchBar.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsersSearchBar.png" />

* **Search** - Enter a  user name, first name, last name, email, department or job title to search by one of these parameters; the system returns all users whose details contain these values.
* **User Status** - Every user in the system has a status and you can filter the table by user status. See [Managing User Status](https://docs.axonius.com/axonius-help-docs/docs/manage-users#managing-user-status).
* **Role** - Filter users by role. This includes both the system roles, and any custom roles that were added. All users with that role are displayed. Click **Clear All** to clear all selections.
* **Data Scope** - Filter users by data scope.
* **Source** - Use **Source** to filter the display users according to their Identity Providers Settings: Internal, LDAP or SAML. Click **Clear All** to clear all selections.
* **Date** - Use the date picker to filter the display by users whose last login was on a certain date or in a certain date range.

Click **Reset** to clear the search and filters. The User Status filter defaults back to show only "Active" and "Inactive" users, while users with a status of "Deleted" are not shown.

## Adding a New User

1. From the **Users** page, click **Add User**. The New User drawer appears.

<Image align="center" alt="NewUserDrawer3.png" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/NewUserDrawer3.png" />

2. In the **New User** drawer, specify the following user details:
   * **User Name** *(required)* - The user name of the user as it should appear in the Axonius system. This is a unique field and cannot be changed. Note that the user name is case sensitive.
   * **User Status** *(required)* - Select a status for the user: Active or Inactive. See [Managing User Status](https://docs.axonius.com/axonius-help-docs/docs/manage-users#managing-user-status)
   * **Role** *(required)* - Select a role from the predefined roles. Roles can be reassigned later per user or by using bulk operation. Axonius provides a few predefined roles. You can set more roles according to your own requirements. See [Managing Roles](https://docs.axonius.com/axonius-help-docs/docs/manage-roles).
   * **Main Data Scope** - Select the data scope this user has access to when they log in to Axonius. Data scopes determine what data, dashboards, queries and other objects a user can see. See [Managing Data Scopes](/docs/data-scope-management) for more information on Data Scopes. The data scope name appears in the *Data Scope* column on the Users page. Admin users are automatically assigned the *Global* data scope.
   * **Allow visiting other Data Scopes** - Users with the "Move between data scopes" permission can [access other Data Scopes](/docs/switch-data-scopes) in addition to the Main data scope selected above. Select one of the following:

     * **All data scopes** - Available only for users with Global data scope as their main data scope. Select if this user is authorized to connect to all data scopes.
     * **Specific data scopes** - Select if this user is authorized to connect to specific data scopes only. Select the authorized data scopes from the list.

     <Image align="center" alt="ManageRoles-AuthorizedDataScopes.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageRoles-AuthorizedDataScopes.png" />

<Callout icon="📘" theme="info">
  NOTE

  Admin users with the **Manage data scopes** permission can assign data scopes to other users.
</Callout>

* (When logging in with a SSO) **Ignore user assignment rules** - Ignore the configured rules for when this user logs in. See [Using Identity Providers](/docs/identity-providers-settings).
  * (When logging in with a SSO) **Source** - Identifies the SSO source of the login.
  * **Password** *(required)* - Select one of the following:

    * **Generate reset password link** - This generates a reset password link URL which you can copied or send to the user, where they can set their own password.
    * **Set password** - Enter a password to associate with the user. The password is visible for 5 seconds.

3. Under **Optional Details**, enter these details for the user:

* **First Name** and **Last Name** - The first and last name of the user.
* **Email** - The email of the user. This is used to create or to reset a password.
* **Department** - The department in which the user works.
* **Job Title** - The job title of the user.

4. Click **Save**.

<Callout icon="📘" theme="info">
  Note

  If you are using an [Identity Provider Login](/docs/identity-providers-settings), for example SAML, any user logging in for the first time is added to the users list. The user is assigned to a role based on the configured role assignment rules. For details, see [Identity Provider Settings](/docs/identity-providers-settings).
</Callout>

## Managing User Status

Axonius makes it easy to set user status. When creating users, the user status can be set to "Active" or "Inactive".

<Image align="center" alt="CreateNewAxoniusUserStatus.png" border={false} width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/CreateNewAxoniusUserStatus.png" />

The "User Status" field on the Users page indicates the current status of all users, and the table can be filtered by user status.

<Image alt="UsersPagewithStatus.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/64e254a972fbf0c64355661ba4577e171fa6f304/img/settings/UsersPagewithStatus.png" />

The following statuses are available:

* **Active** - The user can log in and perform tasks for which they have permission.
* **Inactive** - The user exists but cannot log in to Axonius. A user with an "Inactive" status can be changed to "Active".
* **Deleted** - The user has been deleted and cannot log in but is maintained in the system. See [Deleting Users](https://docs.axonius.com/axonius-help-docs/docs/manage-users#deleting-users). Deleted users have a status of "Deleted" and are filtered out by default. To show users with a status of "Deleted" by default, either clear all filters or select "Deleted" in the User Status filter field. This selection is persistent.

<Callout icon="📘" theme="info">
  **Notes:**

  * You can [impersonate a user](https://docs.axonius.com/axonius-help-docs/docs/impersonating-users) with "Deleted" status to view items that were private to that user and not available any other way.
  * When performing bulk actions on more than one user, select only users with the same user status.
</Callout>

## Editing an Existing User

1. To update an existing user, from the **Users** page, click a user record. The User details drawer appears.
2. Update the user's configuration:
   * For internal users, you can change the user's: first name, last name, email, department, job title, role or password.
   * For external users (SAML/LDAP), you can change:
     * The user's role.
     * Select whether to enforce the current user's role regardless of the **Role Assignment Settings** configuration under the [Identity Providers Settings](/docs/identity-providers-settings). When **Ignore user assignment rules** is enabled the role assignment settings are ignored for all future logins.
     * The user's Main data scope.
     * The data scopes the user is allowed to move between. When a user is granted permission to move between **Specific data scopes**, you must select at least one data scope the user is allowed to visit. The user must be granted the "Move between data scopes" permission.
3. Click **Save**.

<Callout icon="📘" theme="info">
  Notes

  * You can only edit internal users  who were created in Axonius by an Admin or by any other authorized user.

  * Only **Admin** users can modify the system default Admin user. Allowed changes are limited to email and password.
</Callout>

## Reset a User Password

1. To reset a password for an existing user, from the **Users** page, click a user record. The **User** drawer appears.
2. You can choose to reset a password using one of the following methods:
   1. Setting a new password manually
      * Enter a new password in the **Password** field and then click **Save**.
   2. Creating a reset password link for the user to reset their own password.
      a. Click the **Reset Password** icon in the title bar of the user drawer.
      ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ResetUserPassword.png)

      b.  A new reset password link will be generated each time and will be visible in a dialog.

      * The reset password link is valid according to the expiration configured in the [Password Reset Settings](/docs/managing-password-settings#password-reset-settings).
      * The reset password link also expires when the user sets a new password through the reset password link or when a new reset password link is generated for this user.
      * The reset password link can either be copied or sent by Email (If an Email server is configured in the [Email Settings](/docs/configuring-email-settings)).
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ResetUserPasswordNewsecure.png)

## Deleting Users

When users are deleted, they are retained in the system with a user status of "Deleted" and are listed on the Users page with that status. You may need to adjust the **User Status** filter to show deleted users.

<Image alt="UsersPageStatusFilter.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/UsersPageStatusFilter.png" />

**To delete a user:**

* Do one of the following:
  * On the **Users** page, click a user record, and then click **Delete** ( ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/deleteusericon.png) ) in the title bar.
  * Hover over a user and click Delete Users.
  * On the **Users** page, select one or more users, and click **Delete Users**.

<Image alt="DeleteUsers.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteUsers.png" />

<Callout icon="📘" theme="info">
  Note

  The system **admin** user cannot be deleted.
</Callout>

## Assigning a Role Users

**To assign role to a users:**

1. On the **Users** page, select the relevant users and click **Assign Role**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsersAssignRole.png)

2. In the dialog, select the role to be assigned for the selected users and click **Assign**.

<Image align="center" alt="NewRolesSelection.png" border={false} width="350px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewRolesSelection.png" />

<br />

## Assigning a Data Scope to Users

You can assign users a data scope from the Users page. See also [Managing Data Scopes](https://docs.axonius.com/axonius-help-docs/docs/data-scope-management).

**To assign a Data Scope:**

1. On the Users page, hover over a user or select one or more users. The More Actions menu is available.
2. From the More Actions menu, select **Assign Data Scope**.
3. Select a Data Scope from the list and click **Assign**.

## Exporting User Data to CSV

You can export Users table data to a CSV file.

**To export user data to CSV:**

* Above the right side of the **Users** table, click **Export CSV**. The file is automatically downloaded to your local computer.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).