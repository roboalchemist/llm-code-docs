# Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops

Title: About permissions and security groups - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

In this article, you learn about access levels and permissions through inheritance, security groups, roles, and more in Azure DevOps.

For an overview of default permissions, see [Default permissions quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops).

For more information, see [Security overview](https://learn.microsoft.com/en-us/azure/devops/organizations/security/security-overview?view=azure-devops).

All Azure DevOps users have an _access level_, which grants or restricts access to specific web portal features. Three main access levels exist: **Stakeholder**, **Basic**, and **Basic + Test Plans**. To give a user access to Agile portfolio management or test case management features, [change access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-access-levels?view=azure-devops), not permissions. For more information, see [About access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops).

All users in Azure DevOps belong to one or more default _security groups_. Assign _permissions_ to security groups that either **Allow** or **Deny** access to features or tasks.

*   Members inherit the permissions assigned to their security group.
*   Define permissions at different levels: organization/collection, project, or object.
*   Manage some permissions through _role-based assignments_ (for example, team administrator, extension management, or pipeline resource roles).
*   Administrators can define custom security groups to manage permissions for different functional areas.

Managing permissions in Azure DevOps involves two key groups: Project Collection Administrators and Project Administrators.

**Project Collection Administrators:**

*   Hold the highest authority within an organization or project collection.
*   Perform all operations for the entire collection.
*   Manage settings, policies, and processes for the organization.
*   Create and manage all projects and extensions.

**Project Administrators:**

*   Operate at the project level.
*   Manage security groups and permissions from the Project settings in the web portal.
*   Handle permissions for specific objects contributors create within the project.

Assign permissions to grant or restrict access:

**User or group has permission:**

*   Allow
*   Allow (inherited)
*   Allow (system)

**User or group doesn't have permission:**

*   Deny
*   Deny (inherited)
*   Deny (system)
*   Not set

| Permission state | Description |
| --- | --- |
| **Allow** | Explicitly grants users the ability to perform specific tasks, and isn't inherited from group membership. |
| **Allow (inherited)** | Grants group members the ability to perform specific tasks. |
| **Allow (system)** | Grants permission that takes precedence over user permissions. Uneditable and stored in a configuration database, invisible to users. |
| **Deny** | Explicitly restricts users from performing specific tasks, and isn't inherited from group membership. For most groups and almost all permissions, **Deny** overrides **Allow**. If a user belongs to two groups, and one of them has a specific permission set to **Deny**, that user can't perform tasks that require that permission even if they belong to a group that has that permission set to **Allow**. |
| **Deny (inherited)** | Restricts group members from performing specific tasks. Overrides an explicit **Allow**. |
| **Deny (system)** | Restricts permission that takes precedence over user permissions. Uneditable and stored in a configuration database, invisible to users. |
| **Not set** | Implicitly denies users the ability to perform tasks that require that permission, but allows membership in a group that does have that permission to take precedence, also known as **Allow (inherited)** or **Deny (inherited)**. |

Members of the **Project Collection Administrators** or **Team Foundation Administrators** groups might always receive permissions even if denied in another group. The following examples explain this scenario further:

*   A user might still access project settings or manage users. However, for tasks like work item deletion or pipeline management, being a member of the Project Collection Administrators group doesn't override **Deny** permissions set elsewhere.
*   If a user is denied permission to delete work items in a specific project, they can't delete work items even if they're part of the Project Collection Administrators group. Similarly, if pipeline permissions are denied, they can't manage or run pipelines despite their administrative role.

Warning

When you modify a permission for a group, it affects all users in that group. Even a single permission change can impact hundreds of users, so consider the potential effects before making any adjustments.

Permissions follow a hierarchy, so you can inherit permissions from a parent node or override them.

**Group inheritance:**

*   Users inherit permissions from the groups they belong to.
*   If a user has an **Allow** permission directly or through group membership but also has a **Deny** permission through another group, the **Deny** permission takes precedence.
*   Members of Project Collection Administrators or Team Foundation Administrators retain most allowed permissions, even if they belong to other groups that deny those permissions (except for work item operations).

**Object-level inheritance:**

You assign object-level permissions to nodes like areas, iterations, version control folders, and work item query folders. These permissions are inherited down the hierarchy.

**Permission inheritance and specificity rules:**

*   Explicit permissions always take precedence over inherited ones.
*   Permissions set at a higher-level node get inherited by all subnodes unless explicitly overridden.
*   If a permission isn't explicitly allowed or denied for a subnode, it inherits the permission from its parent.
*   If a permission is explicitly set for a subnode, the parent’s permission isn't inherited, regardless of whether it's allowed or denied.

**Specificity:**

In the object hierarchy, specificity trumps inheritance. The most specific permission takes precedence if conflicting permissions exist.

**Example:**

*   Explicitly **Deny** on `area-1` (parent node).
*   Explicitly **Allow** for `area-1/sub-area-1` (child node).
*   In this case, the user receives an **Allow** on `area-1/sub-area-1`, overriding the inherited **Deny** from the parent node.

To understand why a permission is inherited, pause over a permission setting, and then select **Why?** To open a **Security** page, see [View permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/view-permissions?view=azure-devops).

*   [Preview page](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#tabpanel_1_preview-page)
*   [Current page](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#tabpanel_1_current-page)

![Image 1: Screenshot showing Permissions dialog, preview page, Why link annotated.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/view-permissions/about-permissions-information-preview.png?view=azure-devops)

A new dialog opens that shows the inheritance information for that permission.

The preview user interface for the Project Permissions settings page isn't available for Azure DevOps Server 2020 and earlier versions.

Security groups assign specific permissions to their members.

When you create an organization, collection, or project, Azure DevOps creates a set of default security groups and automatically assigns default permissions to these groups. You define more security groups by using the following actions:

*   Creating custom security groups at the following levels: 
    *   Project-level
    *   Organization- or collection-level
    *   Server-level (on-premises only)

*   Adding a team, which creates a team security group

You can't create an object-level security group, but you can assign a custom group to an object-level and assign permissions to that level. For more information, see [Set object-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-object-level-permissions?view=azure-devops).

Most Azure DevOps users are added to the **Contributors** security group and granted the **Basic** access level. The **Contributors** group provides read and write access to repositories, work tracking, pipelines, and more. **Basic** access provides access to all features and tasks for using Azure Boards, Azure Repos, Azure Pipelines, and Azure Artifacts. Users who need access to manage Azure Test Plans require **Basic + Test Plans** or **Advanced** access.

The following security groups are defined by default for each project and organization. You typically add users or groups to the **Readers**, **Contributors**, or **Project Administrators** groups.

| Project | Organization or Collection |
| --- | --- |
| - Build Administrators - Contributors - Project Administrators - Project Valid Users - Readers - Release Administrators - _TeamName_ Team | - Project Collection Administrators - Project Collection Build Administrators - Project Collection Build Service Accounts - Project Collection Proxy Service Accounts - Project Collection Service Accounts - Project Collection Test Service Accounts - Project Collection Valid Users - Project-scoped Users - Security Service Group |

For a description of each of these groups, see [Security groups, service accounts, and permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops). For default permission assignments made to the most common default security groups, see [Default permissions and access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops).

The following security groups are defined by default for each project and project collection. You typically add users or groups to the **Readers**, **Contributors**, or **Project Administrators** groups.

Only add service accounts to [Azure DevOps service account groups](https://learn.microsoft.com/en-us/azure/devops/server/admin/service-accounts-dependencies). To understand valid user groups, see [Valid user groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#valid-user-groups) later in this article.

| Project level | Collection level |
| --- | --- |
| - Build Administrators - Contributors - Project Administrators - Project Valid Users - Readers - Release Administrators - _TeamName_ Team | - Project Collection Administrators - Project Collection Build Administrators - Project Collection Build Service Accounts - Project Collection Proxy Service Accounts - Project Collection Service Accounts - Project Collection Test Service Accounts - Project Collection Valid Users - Security Service Group |

Add users who manage project-level features to the **Project Administrators** group. These features include teams, area and iteration paths, repositories, service hooks, and service endpoints.

Add users who manage organization or collection-level features to the **Project Collection Administrators** group. These features include projects, policies, processes, retention policies, agent and deployment pools, and extensions. For more information, see [About user, team, project, and organization-level settings](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops).

Azure DevOps controls access through these three inter-connected functional areas:

*   **Membership management** supports adding individual user accounts and groups to default security groups. Each default group is associated with a set of default permissions. All users added to any security group are added to the Valid Users group. A valid user is someone who can connect to a project, collection, or organization.
*   **Permission management** controls access to specific functional tasks at different levels of the system. Object-level permissions set permissions on a file, folder, build pipeline, or a shared query. Permission settings correspond to **Allow**, **Deny**, **Inherited allow**, **Inherited deny**, **System allow**, **System deny**, and **Not set**.
*   **Access level management** controls access to web portal features. Based on what's purchased for a user, administrators set the user's access level to **Stakeholder**, **Basic**, **Basic + Test**, or **Visual Studio Enterprise** (previously **Advanced**).

Each functional area uses security groups to simplify management across the deployment. You add users and groups through the web administration context. Permissions are automatically set based on the security group that you add users to. Or permissions are based on the object, project, collection, or server level to which you add groups.

Security group members can be a combination of users, other groups, and Microsoft Entra groups.

You can populate security groups by adding individual users. But, for ease of management, it's more efficient to populate these groups using Microsoft Entra ID for Azure DevOps Services and Active Directory (AD) or Windows user groups for Azure DevOps Server. This approach allows you to manage group membership and permissions more effectively across multiple computers.

If you only need to manage a small set of users, you can skip this step. But, if you anticipate that your organization might grow, consider setting up Active Directory or Microsoft Entra ID. Also, if you plan to use extra services, it's essential to configure Microsoft Entra ID for use with Azure DevOps to support billing.

Note

Without Microsoft Entra ID, all Azure DevOps users must sign in using Microsoft accounts, and you must manage account access by individual user accounts. Even if you manage account access using Microsoft accounts, set up an [Azure subscription to manage billing](https://learn.microsoft.com/en-us/azure/devops/organizations/billing/set-up-billing-for-your-organization-vs?view=azure-devops#set-up-billing).

When you add user accounts directly to a security group, the users automatically become part of one of the following valid user groups.

*   **Project Collection Valid Users:** All members added to an organization-level group.
*   **Project Valid Users:** All members added to a project-level group.

*   _Server_\Azure DevOps Valid Users: All members added to server-level groups.
*   _ProjectCollectionName_\Project Collection Valid Users: All members added to collection-level groups.
*   _ProjectName_\Project Valid Users: All members added to project-level groups.

The default permissions assigned to these groups primarily provide read access, such as **View build resources**, **View project-level information**, and **View collection-level information**.

All users you add to one project can view the objects in other projects within a collection. To restrict view access, you can [set restrictions through the area path node](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops). If you remove or deny the **View instance-level information** permission for one of the Valid Users groups, no members of the group can access the project, collection, or deployment, depending on the group you set.

By default, users you add to an organization can view all organization and project information and settings. These settings include the list of users, the list of projects, billing details, usage data, and more, which you can access through **Organization settings**.

To restrict specific users, such as Stakeholders, Microsoft Entra guest users, or members of a particular security group, you can enable the **Limit user visibility and collaboration to specific projects** preview feature for the organization. Once enabled, any user or group you add to the **Project-scoped Users** group can't access the **Organization settings** pages, except for **Overview** and **Projects**. They only have access to the projects to which you add them.

Warning

Consider the following limitations when using this preview feature:

*   The limited visibility features described in this section apply only to interactions through the web portal. With the REST APIs or `azure devops` CLI commands, project members can access the restricted data.
*   Users in the limited group can only select users who are explicitly added to Azure DevOps and not users who have access through Microsoft Entra group membership.
*   Guest users who are members in the limited group with default access in Microsoft Entra ID, can't search for users with the people picker.

For more information, see [Manage preview features](https://learn.microsoft.com/en-us/azure/devops/project/navigation/preview-features?view=azure-devops).

Note

Security groups are managed at the organization level, even if they're used for specific projects. Depending on user permissions, some groups might be hidden in the web portal. To view all group names within an organization, you can use the Azure DevOps CLI tool or REST APIs. For more information, see [Add and manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-manage-security-groups?view=azure-devops).

Note

Security groups are managed at the collection level, even if they're used for specific projects. Depending on user permissions, some groups might be hidden in the web portal. To view all group names within a collection, you can use the Azure DevOps CLI tool or REST APIs. For more information, see [Add and manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-manage-security-groups?view=azure-devops).

With role-based permissions, you assign user accounts or security groups to a role, and each role has one or more permissions. The following resources support role-based permissions:

*   [Artifact or package feed security roles](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/feed-permissions?view=azure-devops)
*   [Marketplace extension Manager role](https://learn.microsoft.com/en-us/azure/devops/marketplace/grant-permissions?view=azure-devops)
*   [Pipeline security roles](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-security-roles?view=azure-devops)
*   [Team administrator role](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/manage-teams?view=azure-devops)

For more information, see [About pipeline security roles](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-security-roles?view=azure-devops).

The following image illustrates how security groups defined at the project and collection level can assign permissions to objects, projects, and the organization.

![Image 2: Conceptual diagram mapping default security groups to permission levels, cloud.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/about-security/security-groups-permission-management-cloud.png?view=azure-devops)

The following image illustrates how security groups defined at the project and collection-level can be assigned to permissions assigned at the object, project, and collection level. You can only define server-level security groups to server-level permissions.

![Image 3: Conceptual diagram mapping default security groups to permission levels, on-premises.](https://learn.microsoft.com/en-us/azure/devops/organizations/security/media/about-security/security-groups-permission-management-on-premises.png?view=azure-devops)

Members of the Project Administrators or Project Collection Administrators groups manage all team tools for all teams.

Feature flags control access to new features. Azure DevOps periodically introduces new features behind a feature flag. Project members and organization owners can enable or disable preview features. For more information, see [Manage or enable features](https://learn.microsoft.com/en-us/azure/devops/project/navigation/preview-features?view=azure-devops).

*   [Troubleshoot access and permission issues](https://learn.microsoft.com/en-us/azure/devops/organizations/security/troubleshoot-permissions?view=azure-devops)
*   [Learn about security, authentication, and authorization](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-security-identity?view=azure-devops)
*   [Reference permissions and groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops)
*   [Add and manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-manage-security-groups?view=azure-devops)

*   [Get started with AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ad-ds-getting-started)
*   [Reference permissions and groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops)
*   [Add users to a team or a project](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Add and manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-manage-security-groups?view=azure-devops)
