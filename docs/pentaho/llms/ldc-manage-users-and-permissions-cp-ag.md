# Source: https://docs.pentaho.com/pdc-admin/ldc-manage-users-and-permissions-cp-ag.md

# Manage users and permissions

Pentaho Data Catalog comes with a set of default user roles that define role-based access for PDC users. Administrators can further refine this access by creating **communities** that group users with similar responsibilities and apply additional permissions or restrictions. For more information, see [User roles and permissions in Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-user-roles-and-permissions "mention") in the [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ "mention") guide.

Users with the **Admin** role, or users who have been granted **Admin permissions** through a community, can manage **user accounts and access permissions** through the **Manage Your Environment** page. From there, administrators can add, edit, or remove users, assign roles, and manage community membership.

You can also import users from **Microsoft Active Directory (AD)** for centralized identity and access management. When Active Directory integration is enabled, **users should not be created directly in the catalog**. Communities, however, must always be created and managed within Data Catalog to control permissions and access scopes. For more information, see [Integrate Active Directory with Pentaho Data Catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#integrate-active-directory-with-pentaho-data-catalog).

## Add a user

You can add new users to Data Catalog from the **Manage Your Environment** page. Each user must be assigned at least one role or community to define access permissions.

{% hint style="info" %}
If your environment is integrated with Microsoft Active Directory (AD), you must add and manage users in AD instead of in Data Catalog. Communities are always created and managed within Data Catalog.
{% endhint %}

Perform the following steps to add a user:

**Prerequisites**

1. On the left navigation main menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. On the Manage Your Environment page, click the **Users & Communities** card, click **Add New,** and select **Add User**.

   The **Create User page** opens.
3. Enter the information for the user.
4. (Optional) Click **Add to Community**.

   The Available Communities window opens.
5. (Optional) Select one or more checkboxes for a community to which you want to add the user, and click **Done**.
6. (Optional) Click **Add Roles**.

   The Available Roles window opens.
7. (Optional) Select one or more checkboxes for the role or roles to assign to the user.

   **Note:** If you try to assign an Expert user role to the user but have reached the limit allowed by your license agreement, you see a message that you have exceeded the licensed limit and cannot assign the role.
8. When you are finished assigning permissions, click **Done**.

The user is created.

## Add a community

Administrators can create **communities** in **Pentaho Data Catalog** to fine-tune access beyond default user roles. A community acts as a **custom role** that groups users with similar responsibilities and grants additional or restricted permissions for specific catalog assets.

{% hint style="info" %}
When Data Catalog is integrated with Microsoft Active Directory (AD), users are imported from AD. However, communities must always be created and managed within Data Catalog to control permissions and scope.
{% endhint %}

Perform the following steps to add a community:

**Prerequisites**

* You must have the **Admin** role or **Admin permissions** through a community.
* Identify the **base role** (for example, *Data Steward* or *Business User*) on which you want to model the community permissions.
* Determine which users will be members of the new community and which catalog assets they should access.

**Procedure**

1. On the left navigation main menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. On the Manage Your Environment page, click the **Users & Communities** card, click **Add New,** and select **Add Community**.

   The **Create Community** page opens.
3. Enter a name for the community.
4. Select a role to be the basis of the permissions for the community.
5. (Optional) Enter a description of the community.
6. In the **Users** area, select users to add to the community.
7. In the **Permissions** area, select the checkboxes of permissions per feature that you want the users in the community to have.

   The following image shows a partial view of the default permissions for the Data Steward role. Checkboxes that are grayed out cannot be selected.

   ![Permissions table in add or edit community page](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-d8992f390c8afeb1ff91b4094c504d5780f25705%2FPDC%20community%20permissions%20table%20with%20checkboxes.png?alt=media)
8. In the **Scope** area, click the plus sign at the end of the row for a listed Data Catalog feature to show the options within the features that are available to add to the community, such as **Business Glossary** or **Data Sources**.

   The following image shows a sample **Scope** table:

   ![Scope table in add or edit community page](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-1828402fcdebc9bed0143523454585ed9c864137%2FPDC%20Scope%20table%20in%20add%20or%20edit%20community%20page.png?alt=media)

   After clicking a plus sign, an Add Scope window opens. The following screen shows an Add Scope window for data sources. By default, all data sources are selected, with a checkmark in the **All** checkbox. To restrict the data source access for someone in this community, clear the **All** checkbox and select the checkboxes for other data sources to which you want to allow access.

   ![Add Scope window in add or edit community page](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-5d96f8a878fb342be791d1a01c5c6abfdbcdcc23%2FPDC%20Add%20Scope%20window.png?alt=media)
9. After defining the scope, click **Done** to close the window.
10. Click **Done** to add the community.

The community is added to the Data Catalog, and users can be added to it.

## Edit a user

You can change the permissions for a Pentaho Data Catalog user by editing the user to add a role or community. You can also update the user's profile information.

{% hint style="info" %}
If you have users imported from Microsoft Active Directory (AD), you need to use AD to edit users instead of using the PDC **Users & Communities** card.
{% endhint %}

In Data Catalog, access permission for data source types is governed by communities. To update a user's data source access permissions, you need to update the community to which the user is assigned, or update the community itself. To see the data source access for an existing community, see [Edit a community](#edit-a-community) or you can [Add a community](#add-a-community).

Perform the following steps to edit a user's information:

1. On the left navigation main menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. On the **Users & Communities** card, click **Users**.\
   The Users page opens.
3. Locate the user you want to edit. At the end of the row, click the pencil icon.

   The user-specific page opens.
4. Edit the user as necessary. You can add or remove a user from a community, add or remove roles, and update the user's profile information.

   **Note:** When a user has more than one role, the role access permissions are cumulative, meaning that the user's resulting access contains the permissions for the individual roles.

   You can perform one or more of the following actions:

<table><thead><tr><th width="237.3333740234375">Action</th><th>Instructions</th></tr></thead><tbody><tr><td><strong>Update user name</strong></td><td>Under <strong>User Information</strong>, update the <strong>First name</strong> or <strong>Last name</strong> fields.</td></tr><tr><td><strong>Add user to a community</strong></td><td><ol><li>In the <strong>Add User to Communities</strong> table, click <strong>Add to Community</strong>.</li><li>Select the checkbox next to one or more communities to assign to the user.</li><li>Click <strong>Done</strong>.</li></ol></td></tr><tr><td><strong>Remove user from a community</strong></td><td><ol><li>In the <strong>Add User to Communities</strong> table, select the checkbox next to one or more communities to remove.</li><li>Click <strong>Delete</strong>.</li></ol></td></tr><tr><td><strong>Add a role to the user</strong></td><td><ol><li>In the <strong>Add Role(s) to User</strong> table, click <strong>Add Roles</strong>.</li></ol><p>The Available Roles window opens.</p><ol start="2"><li>In the Available Roles window, select the checkbox next to one or more roles to assign to the user.</li><li>Click <strong>Done</strong>. <strong>Note:</strong> If you try to assign an Expert user role to the user but have reached the limit allowed by your license agreement, you see a message that you have exceeded the licensed limit and cannot assign the role.</li></ol></td></tr><tr><td><strong>Remove a role from the user</strong></td><td><ol><li>In the <strong>Add Role(s) to User</strong> table, select the checkbox next to one or more roles to remove.</li><li>Click <strong>Delete</strong>.</li></ol></td></tr></tbody></table>

4\. When you are finished updating, click **Edit**.

The user information is updated.

## Edit a community

You can update the role that gives the community its base permissions, add or remove users, add or remove permissions for various actions, and adjust the scope of the community, such as the resources on which the actions can be performed.

{% hint style="info" %}
It is helpful to other users if the description of a community includes information about the permissions it conveys to the users in the community.
{% endhint %}

Perform the following steps to edit a community:

1. On the left navigation main menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. On the **Users & Communities** card, click **Communities**.\
   The **Communities** page opens.
3. Locate the community you want to edit. At the end of the row, click the pencil icon.

   The community-specific page opens.
4. Edit the community as necessary. You can update the community information, add or remove users, select or deselect permissions assigned to the community, or update the scope of the community's permissions. You can perform one or more of the following actions:

   <table><thead><tr><th width="197.333251953125">Action</th><th>Instructions</th></tr></thead><tbody><tr><td><strong>Update the community information</strong></td><td>You can change the role that gives the community its base permissions, or you can update the description. To change the role, click the down arrow at the end of the <strong>Role</strong> field and select a different role.</td></tr><tr><td><strong>Add users to the community</strong></td><td><ol><li>In the <strong>Users</strong> table, click <strong>Add Users</strong>.</li><li>Select the checkbox next to one or more users to add.</li><li>Click <strong>Done</strong>.</li></ol></td></tr><tr><td><strong>Remove users from the community</strong></td><td><ol><li>In the <strong>Users</strong> table, select the checkbox next to one or more users to remove.</li><li>Click <strong>Delete</strong>.</li></ol></td></tr><tr><td><strong>Update community permissions</strong></td><td>In the <strong>Permissions</strong> table, you can select any unselected checkbox that is available, or not blocked from being selected.Select or clear checkboxes for the permissions you want for the community.</td></tr><tr><td><strong>Update community scope</strong></td><td>In the <strong>Scope</strong> table, you can update the scope of the features the community can access, such as data source types.</td></tr></tbody></table>

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If the community permissions are changed while a user is logged in, request the user to refresh the browser to apply the updated permissions. Alternatively, the user can sign out and sign back in to ensure the changes take effect.</p></div>
5. When you are finished updating, click **Edit**.

The community information is updated.

## Remove a user

You can remove a user if they no longer need access to Data Catalog.

{% hint style="info" %}
If you have users imported from Microsoft Active Directory (AD), you need to use AD to remove users instead of using the PDC **Users & Communities** card.
{% endhint %}

Perform the following steps to remove a user:

1. On the left navigation main menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. On the **Users & Communities** card, click **Users**.\
   The Users page opens.
3. Locate the user you want to remove, and select the checkbox at the beginning of the row.

   The user-specific page opens.
4. Click **Delete**.

   A confirmation window opens.
5. Click **Delete** to confirm.

The user is removed.

## Remove a community

You can remove a community from Data Catalog if it is no longer required. Perform the following steps to remove a community:

1. On the left navigation main menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. On the **Users & Communities** card, click **Communities**.\
   The **Communities** page opens.
3. Locate the community you want to remove, and select the checkbox at the beginning of the row.

   The user-specific page opens.
4. Click **Delete**.

   A confirmation window opens.
5. Click **Delete** to confirm.

The community is removed.
