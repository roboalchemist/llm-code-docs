# Source: https://docs.axonius.com/docs/deleting-the-local-admin-account.md

# Deleting the Default admin Account

The default **admin** user account can be deleted. There must be at least one other active user account assigned the **Admin** role to delete the default **admin** account.

![DeleteAdminUserAccount-1.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteAdminUserAccount-1.png)

See [Manage Roles](/docs/manage-roles) or [Permissions List](/docs/permissions-list) for more information about roles and permissions.

**To delete the default admin user account:**

1. From the top right corner of any page, click ![System Settings icon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/System%20Settings%20icon.png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Users**.
3. Click on the **admin** user.
4. In the header of the drawer, click the trashcan icon to delete the account.
5. Click **Delete** to confirm the deletion.

<Callout icon="📘" theme="info">
  NOTES

  * To delete the default **admin** account, you must have been assigned the **Admin** role by a user with the **Admin** role and have the **Manage admin users** permission.

  * A user that has permission to manage admin users, but is not assigned the **Admin** role, won't be able to delete the default **admin** user.

  * Once the **admin** account has been deleted, the User Name *admin* can no longer be assigned. An error message will display saying that this User Name is not allowed.)
</Callout>