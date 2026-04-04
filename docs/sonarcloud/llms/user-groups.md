# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-groups.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups.md

# Managing user groups

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

With the Free plan organization, only the built-in groups are used and you cannot change them.

User groups are used to manage organization members and their permissions. This article describes how to create, update, or delete user groups. For more information about user groups, see [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention").

You must be an organization admin to be able to manage the user groups of the organization.

### Creating a new user group <a href="#create-group" id="create-group"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Groups**. The **Groups** page opens with the list of user groups for the organization.
3. Select the **Create Group** button. The **Create Group** dialog opens.
4. Enter the group name and description.
5. Confirm with **Create**. The new group is added to the list.
6. In the **Members** column, select the pen icon to add users to the group: see below.

### Adding/removing users to/from a group <a href="#add-remove-users" id="add-remove-users"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Groups**. The **Groups** page opens with the list of user groups for the organization.
3. In the **Members** column, select the pen icon next to the group you want to change. The **Update users** dialog opens.
4. Select the **All** option. All users belonging to the organization are listed.
5. Select or unselect the check box to add or remove a user to or from the group.
6. Select the **Close** button.

### Changing the name or description of a group <a href="#change-name-or-description" id="change-name-or-description"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Groups**. The **Groups** page opens with the list of user groups for the organization.
3. Select the three-dot menu to the far right of the group you want to change.
4. In the menu, select the **Update details** command. The **Update Group** dialog opens.
5. Edit the group details and select the **Update** button.

### Deleting a user group <a href="#delete-group" id="delete-group"></a>

You cannot delete the **Members** group. You can only delete a group if it does not result in the removal of all organization admins.

To delete a group:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Groups**. The **Groups** page opens with the list of user groups for the organization.
3. Select the three-dot menu to the far right of the group you want to delete.
4. In the menu, select the **Delete** command and confirm.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/introduction "mention") to Managing your subscription
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup
* [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention")
* [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention")
* [projects-management-page](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/projects-management-page "mention")
