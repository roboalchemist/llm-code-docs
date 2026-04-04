# Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-remove-manage-user-group-security-group?view=azure-devops

Title: Add or Remove Users or Groups - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-remove-manage-user-group-security-group?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

This article explains how to manage permissions and access by using security groups. You can use default or custom groups to set permissions. You can add users and groups to multiple groups. For instance, you add most developers to the **Contributors** group. When they join a team, they also join the team’s group.

For more information, see the following articles:

*   [Add an Active Directory / Microsoft Entra group to a built-in security group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-ad-aad-built-in-security-groups?view=azure-devops)
*   [Add organization users and manage access](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-organization-users?view=azure-devops)
*   [Add users or groups to a team or project](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Remove user accounts](https://learn.microsoft.com/en-us/azure/active-directory/add-users-azure-active-directory#delete-a-user)
*   [Manage access to specific features using permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/restrict-access?view=azure-devops)
*   [Change project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)
*   [Change permissions at the organization or collection-level](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-organization-collection-level-permissions?view=azure-devops)

Users inherit permissions from the groups that they belong to. If a permission is set to _Allow_ for one group and _Deny_ for another group to which the user belongs, then their effective permission assignment is _Deny_. To learn more about inheritance, see [About permissions and security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#security-groups-and-membership).

Azure DevOps uses security groups for the following purposes:

*   Determine permissions allocated to a group or user
*   Determine access level allocated to a group or user
*   Filter work item queries based on membership within a group
*   Use `@mention` of a project-level group to send email notifications to members of that group
*   Send team notifications to members of a team group
*   Add a group to a role-based permission
*   Set object-level permissions to a security group

Note

Security groups are managed at the organization level, even if they're used for specific projects. Depending on user permissions, some groups might be hidden in the web portal. To view all group names within an organization, you can use the Azure DevOps CLI tool or REST APIs. For more information, see [Add and manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-manage-security-groups?view=azure-devops).

Note

Security groups are managed at the collection level, even if they're used for specific projects. Depending on user permissions, some groups might be hidden in the web portal. To view all group names within a collection, you can use the Azure DevOps CLI tool or REST APIs. For more information, see [Add and manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-manage-security-groups?view=azure-devops).

| Category | Requirements |
| --- | --- |
| **Permissions** | - To manage permissions or groups at the project level: Member of the **Project Administrators** security group. - To manage permissions or groups at the collection level: Member of the [Project Collection Administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/security/look-up-project-collection-administrators?view=azure-devops) group. Organization owners are automatically members of this group. |

Note

Users added to the **Project-Scoped Users** group can't access most **Organization settings** pages, including permissions. For more information, see [Limit user visibility](https://learn.microsoft.com/en-us/azure/devops/user-guide/manage-organization-collection?view=azure-devops#project-scoped-user-group).

Create a _project-level_ group when you want to manage permissions at the project or object level for a project. Create a _collection-level_ group when you want to manage permissions at the collection level. For more information, see [Change project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops) and [Change permissions at the organization or collection-level](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-organization-collection-level-permissions?view=azure-devops).

1.   Open the Azure DevOps web portal, and select the project where you want to add users or groups. To choose another project, see [Switch project, repository, team](https://learn.microsoft.com/en-us/azure/devops/project/navigation/go-to-project-repo?view=azure-devops).

2.   Select **Project settings**>**Permissions**.

![Image 1: Screenshot of the Permissions section under Project settings.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/permissions/project-settings-permissions.png?view=azure-devops)

3.   Select **New Group** to open the dialog for adding a group.

1.   Open the web portal and select the ![Image 2](https://learn.microsoft.com/en-us/azure/devops/media/icons/project-icon.png?view=azure-devops) Azure DevOps icon, and then select ![Image 3](https://learn.microsoft.com/en-us/azure/devops/media/icons/gear-icon.png?view=azure-devops)**Organization settings**.

![Image 4: Screenshot of Organization settings.](https://learn.microsoft.com/en-us/azure/devops/media/settings/open-admin-settings-vert-2.png?view=azure-devops)

2.   Under **Security**, select **Permissions**, and then choose **New group** to open the dialog for adding a group.

![Image 5: Screenshot of the button to create a new security group at the organization level.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/organization-permissions-add-group.png?view=azure-devops)

1.   In the dialog that opens, enter a **Name** for the group. Optionally, add members and a description for the group.

For example, here we define a Work Tracking Administrators group.

![Image 6: Screenshot of the security group dialog box to add a security group at the organization level.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/create-new-group-at-org-level.png?view=azure-devops)

2.   Choose **Create** when you're done.

1.   Open the Azure DevOps web portal, and select the project where you want to add users or groups. To choose another project, see [Switch project, repository, team](https://learn.microsoft.com/en-us/azure/devops/project/navigation/go-to-project-repo?view=azure-devops).

2.   Select **Project settings**>**Security**.

_To see the full image, select to expand_.

[![Image 7: Screenshot of the Security page under Project Settings.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/view-permissions/open-security-project-level-vert.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/view-permissions/open-security-project-level-vert.png?view=azure-devops#lightbox)

3.   Under **Groups**, choose one of the following options:

    *   **Readers**: To add users who require read-only access to the project.
    *   **Contributors**: To add users who contribute fully to this project or who were granted Stakeholder access.
    *   **Project Administrators**: To add users who need to administrate the project. For more information, see [Change project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops).

4.   Select the **Members** tab.

Here we choose the **Contributors** group.

![Image 8: Screenshot showing the security page, Contributors group, Membership page.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/add-users/add-members-to-contributors-group.png?view=azure-devops)

The default team group, and any other teams you add to the project, get included as members of the **Contributors** group. Add a new user as a member of a team instead, and the user automatically inherits Contributor permissions.

Tip

Managing users is much easier [using groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops), not individual users. 
5.   Choose ![Image 9](https://learn.microsoft.com/en-us/azure/devops/media/icons/add-light-icon.png?view=azure-devops)**Add** to add a user or a user group.

6.   Enter the name of the user account into the text box. You can enter several identities into the text box, separated by commas. The system automatically searches for matches. Choose the matches that meet your requirements.

![Image 10: Screenshot of Add users and group dialog, on-premises.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-level-permissions-add-a-user.png?view=azure-devops)

The first time you add a user or group to Azure DevOps, you can't browse to it or check the friendly name. After the identity gets added, you can just enter the friendly name.

7.   Choose **Save changes** when you're done.

8.   (Optional) You can customize a user's permission for other functionality in the project. For example, in [areas and iterations](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops) or [shared queries](https://learn.microsoft.com/en-us/azure/devops/boards/queries/set-query-permissions?view=azure-devops).

Note

Users with limited access, such as Stakeholders, can't access select features even if granted permissions to those features. For more information, see [Permissions and access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops). 

As roles and responsibilities change, you might need to change the permission levels for individual members of a project. The easiest way to do that is to add the user or a group of users to either a default or custom security group. If roles change, you can then remove the user from a group.

The following steps show how to add a user to the built-in **Project Administrators** group. The method is similar no matter what group you're adding. If your organization is connected to Microsoft Entra ID or Active Directory, then you can add security groups defined in those directories to Azure DevOps security groups. For more information, see [Add Active Directory / Microsoft Entra users or groups to a built-in security group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-ad-aad-built-in-security-groups?view=azure-devops).

If you need to add more than 10k users or groups to an Azure DevOps security group, we recommend adding an Azure Directory / Microsoft Entra group containing the users, instead of adding the users directly.

1.   Open the **Permissions** page for either the project-level or organization-level as described in the previous section, [Create a custom security group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-remove-manage-user-group-security-group?view=azure-devops#create-custom-group).

2.   Choose the security group whose members you want to manage, then choose the **Members** tab, and then choose **Add**.

For example, here we choose the **Project Administrators** group, **Members**, and then **Add**.

![Image 11: Screenshot showing Project Settings, Permissions, Add member.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/project-admin-members-add.png?view=azure-devops)

3.   Enter the name of the user account into the text box and then select from the match that appears. You can enter several identities recognized by the system into the **Add users and/or groups** box. The system automatically searches for matches. Choose the matches that meet your choices.

![Image 12: Screenshot showing Add users and group dialog, preview page.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/add-member-project-admin.png?view=azure-devops)

Note

Users with limited access, such as Stakeholders, can't access select features even if granted permissions to those features. For more information, see [Permissions and access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops). 
4.   Select **Save**.

1.   Open the **Permissions** page for either the project-level or organization-level as described in the previous section, [Create a custom security group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-remove-manage-user-group-security-group?view=azure-devops#create-custom-group).

2.   Choose the security group whose members you want to manage, then choose the **Members** tab, and then choose **Add**.

For example, here we choose the **Project Administrators** group, **Members**, and then **Add**.

![Image 13: Screenshot of Project Settings, Security, Add member page.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-level-permissions-add-member.png?view=azure-devops)

3.   Enter the name of the user account into the text box. You can enter several identities into the text box, separated by commas. The system automatically searches for matches. Choose the matches that meet your choice.

![Image 14: Screenshot of Add users and group dialog, on-premises.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-level-permissions-add-a-user.png?view=azure-devops)

Note

Users with limited access, such as Stakeholders, can't access select features even if granted permissions to those features. For more information, see [Permissions and access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops). 
4.   Choose **Save changes**. Choose the ![Image 15](https://learn.microsoft.com/en-us/azure/devops/media/icons/refresh.png?view=azure-devops) refresh icon to see the additions.

Because permissions are defined at different levels, review the following articles to open the dialog for the permissions you want to change:

*   [Set object-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-object-level-permissions?view=azure-devops)
*   [Change project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)
*   [Change collection-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-organization-collection-level-permissions?view=azure-devops)

1.   For the user or group you want to remove, select ![Image 16](https://learn.microsoft.com/en-us/azure/devops/media/icons/more-actions.png?view=azure-devops) the vertical ellipses, then choose **Remove**.

![Image 17: Screenshot of Remove a user, cloud version.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/remove-admin-member-s157.png?view=azure-devops)

2.   Select **Delete** to confirm removal of the group member.

![Image 18: Screenshot of Remove user confirmation dialog, cloud version.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/delete-member-confirm-dialog.png?view=azure-devops)

To remove a user from a group, choose **Remove** next to the user's name that you want to remove.

![Image 19: Screenshot of Remove user confirmation dialog, on-premises versions.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/remove-admin-member-server.png?view=azure-devops)

1.   Open the **Permissions** page for either the project-level or organization-level as described earlier in this article, [Create a custom security group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-remove-manage-user-group-security-group?view=azure-devops#create-custom-group).

2.   Choose the **Settings** tab. You can change a group description, add a group image, or delete a group through the group **Settings** page.

3.   From the **Project settings > Permissions** or **Organization settings**>**Permissions** page, choose the group you want to manage, and then choose **Settings**.

For example, here we open the Settings for the Work Tracking Administrators group.

![Image 20: Screenshot of Open group settings, preview page.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/group-settings.png?view=azure-devops)

You can modify the group name, group description, upload an image, or delete the group.

You can change a group name, description, add a group image, or delete a group.

1.   From the **Project > Settings > Security** or **Organization** page, choose the group you want to manage

2.   Choose from the **Edit** menu to either **Edit profile** or **Delete**.

For example, here we open the **Edit profile** for the Stakeholder Access group.

![Image 21: Screenshot of Open Edit group profile, on-premises versions.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/edit-group-profile-delete-project-level-current.png?view=azure-devops)

Change the description. You can change the name of the group as well.

![Image 22: Screenshot of Edit group dialog profile description, on-premises versions.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/project-collection/edit-project-level-group-current.png?view=azure-devops)

3.   Choose **Save** to save your changes.

For on-premises deployments, see these other articles:

*   [Add server-level administrators to Azure DevOps Server](https://learn.microsoft.com/en-us/azure/devops/server/admin/add-administrator)
*   [Service accounts and dependencies](https://learn.microsoft.com/en-us/azure/devops/server/admin/service-accounts-dependencies)

*   [Set object-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-object-level-permissions?view=azure-devops)
*   [Get started with permissions, access, and security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops)
*   [Permissions lookup reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-lookup-guide?view=azure-devops)
*   [Permissions and groups reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops)
*   [Manage teams and configure team tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/manage-teams?view=azure-devops)
