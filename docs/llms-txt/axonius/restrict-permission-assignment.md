# Source: https://docs.axonius.com/docs/restrict-permission-assignment.md

# Special Permissions

This page includes some special permissions.

## Manage Permissions for Administrators

Axonius uses a combination of restriction of assignment of nonauthorized permissions together with a permission to 'Manage Admin users' to enable you to create groups of 'Restricted Administrators' with a subset of admin permissions.
Therefore, in an enterprise you can give limited admin permissions to users who are not necessarily administrators of the system, or create administrators with limited permissions. These 'Restricted Administrators' can assign roles and create and manage users, but cannot assign permissions that they do not have themselves, change system settings, or edit the 'admin' user.

<Callout icon="📘" theme="info">
  Note

  Make sure that you do not assign these users the "Update system settings" permission.
</Callout>

**To manage permissions for administrators:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/System%20Settings%20icon.png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Special Permissions**.
3. Toggle on **Restrict Assignment of non-authorized permissions**.
4. Clear the 'Manage admin users' permission for the restricted admin roles that you create.

<Callout icon="📘" theme="info">
  Note

  When 'Manage admin users' is enabled, the Administrator has complete administration of the system.
</Callout>

### Restricted Administrators

Once this is set, an administrator who does not have the 'Manage admin users' permission will only be able to assign permission that they themselves have both when creating new roles and when duplicating roles.

<Callout icon="📘" theme="info">
  Note

  You can give Restricted Administrators any permissions needed apart from 'Manage admin users' and 'Update system settings'.
</Callout>

You can give them any permissions needed apart from 'Manage admin users' and 'Update system settings'.

In addition, the 'Restricted Administrators' cannot assign the Administrator role or see it in the system and the following capabilities are therefore limited:
**Manage Users**

* Admin users is not available in the **Manage Users** page.
* The Admin role is not available in the Role Assignment dropdown for creating and editing users.

**Manage Roles**

* The Admin Role is not available in the **Manage Roles** page.

**Identity Providers Settings**

* The Admin role is not available in 'LDAP Role Assignment Settings'. If the Admin role was previously assigned as a default role for specific users, Restricted users will not be able to make changes to the way it was assigned.
* The Admin role is not available in 'SAML-Based Login Settings'. If the Admin role was previously assigned as a default role for specific users, Restricted users will not be able to make changes to the way it was assigned.

## Share Dashboards and Queries to All Data Scopes

Dashboards and queries can be shared across all data scopes, enabling users to create objects that can be shared with all users. See [Dashboards](https://docs.axonius.com/axonius-help-docs/docs/working-with-dashboard-spaces) and [Changing Dashboard Access Permissions](https://docs.axonius.com/axonius-help-docs/docs/changing-dashboard-access-permissions).

**To allow sharing dashboards and queries across all Data Scopes:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Special Permissions**.
3. In **Object Sharing Settings**, toggle on **Allow sharing dashboards and queries to all Data Scopes**.
   * When not enabled *(default)*, users cannot share dashboards or queries with all Data Scopes, even if they have the **Add or edit all Data Scopes** permission.

<Callout icon="📘" theme="info">
  Notes

  * Users cannot create new shared dashboards or queries.

  * Users cannot update existing dashboards or queries to be shared.

  * Existing shared dashboards or queries will continue to be shared.

  * Users cannot update existing shared dashboards or queries.

  * Users will not see the **Share with selected roles within all Data Scopes** option when creating or editing dashboards and queries.
</Callout>

* When enabled, users can share dashboards or queries with all Data Scopes.
* <Callout icon="📘" theme="info">
    **Note**:

    * Existing shared dashboards and queries will continue to be shared.
    * Users can create new shared dashboards or queries.
    * Users can update existing non-shared dashboards and queries to be shared (if they have the required permissions).
    * Users can update existing shared dashboards or queries.
    * A user that has the **Add or edit all Data Scopes** permission can select  **Share with selected roles within all Data Scopes** when creating or editing dashboards or queries.
    * A user that does **not** have the **Add or edit all Data Scopes** will not see the **Share with selected roles within all Data Scopes** option when creating or editing dashboards or queries.
  </Callout>