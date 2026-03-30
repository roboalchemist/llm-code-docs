# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/manage-users-and-roles-in-the-pdi-client/enable-system-role-permissions.md

# Enable system role permissions

Pentaho requires the authenticated system role for users, including administrative users, to login to the Pentaho Repository. Pentaho Repository users are automatically assigned the **Authenticated** system role, in addition to the role you assigned them, at login. By default, the authenticated system role provides **Read Content** permission. You can change permissions as needed.

**Note:** The anonymous system role is non-functional and not being used at this time.

1. Click **System Roles**.

   System roles appear in the **Available** list.
2. Select the **Authenticated** role.
3. Under **Permissions**, select the check boxes to enable (or clear to disable) permissions for this role.
4. Click **Apply** to save your changes.

   The specified permissions are enabled for the authenticated system role.
