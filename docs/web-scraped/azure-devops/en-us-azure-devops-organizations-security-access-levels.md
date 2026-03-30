# Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops

Title: About access levels - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Access levels in Azure DevOps control which web portal features are available. Access levels supplement security groups, which allow or deny specific tasks. Administrators ensure that their user base has access to the features they need and only pay for those specific features. For more information, see [Stakeholder access quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/stakeholder-access?view=azure-devops) and [Manage users and access](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-organization-users?view=azure-devops).

Important

![Image 1: Select a version from Azure DevOps Content Version selector.](https://learn.microsoft.com/en-us/azure/devops/media/version-selector.png?view=azure-devops)

When you add a user or group to a team or project, they automatically gain access to the features associated with the default access level and security group. For most users, assigning them to the **Basic** access level and the **Contributors** security group provides access to most features. For a simplified overview of the permissions assigned to the most common groups **Readers**, **Contributors**, and **Project Administrators**, see [Default permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops).

Assign users or groups of users to one of the following access levels:

*   **Basic**: Provides access to most features. Assign to users with a Visual Studio Professional subscription, an Azure DevOps Server CAL, and to users for whom you're paying for Basic access in an organization.
*   **Basic + Test Plans**: Provides access to all features included in **Basic** and Azure Test Plans. Assign to users with a Visual Studio Test Professional or MSDN Platforms subscription, and to users for whom you're paying for Basic + Test Plans access in an organization.
*   **Stakeholder**: Provides limited access to private projects and nearly full access to public projects. Assign to an unlimited number of users without requiring a license or subscription, ideal for those needing access to a restricted set of features. Stakeholders can perform various tasks, including viewing work items, participating in discussion, and accessing dashboards.
*   **Visual Studio subscriber**: Assign to users who already have a Visual Studio subscription. The system automatically recognizes the user's subscription—Visual Studio Enterprise, Visual Studio Professional, Visual Studio Test Professional, or MSDN Platform—and enables any other features included in their subscription level. If you assign **Basic** or **Stakeholder**, they also receive their Visual Studio subscription benefits upon sign-in. Tip

As a best practice when adding new users, assign the **Visual Studio Subscriber** level when appropriate (as opposed to Basic) to prevent being charged the **Basic** rate before the user signs in for the first time. 
*   **GitHub Enterprise**: The system automatically recognizes users with a GitHub Enterprise license the next time they sign in to Azure DevOps. Regardless of a user's assigned access level (for example, they could be assigned **Stakeholder** access), they receive **Basic** access when they're associated with a GitHub Enterprise license.

*   **Stakeholder**: Provides partial access, can assign to unlimited users for free. Assign to users with no license or subscriptions who need access to a limited set of features.
*   **Basic**: Provides access to most features. Assign to users with an Azure DevOps Server CAL, with a Visual Studio Professional subscription, and to users for whom you're paying for Basic access in an organization.
*   **Basic + Test Plans**: Provides access for users who have a monthly Test Manager subscription, Visual Studio Test Professional, or MSDN Platforms subscription.
*   **VS Enterprise**: Provides access to premium features. Assign to users with a subscription to Visual Studio Enterprise.

The following table indicates those features available for each supported access level. Visual Studio Test Professional and MSDN Platform subscriptions grant access to the same features as Visual Studio Enterprise.

* * *

**Feature**

**Stakeholder**

**Basic**, **GitHub Enterprise**, &

**Visual Studio Professional**

**Basic + Test Plans &**

**Visual Studio Enterprise**

* * *

**Feature**

**Stakeholder**

**Basic**&

**Visual Studio Professional**

**Basic + Test Plans**&

**Visual Studio Enterprise**

* * *

[**Administer organization**](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops)

 Can configure resources when also added to a security group or role: team administrator, Project Administrator, or Project Collection Administrator.

✔️

✔️

✔️

* * *

**Advanced backlog and sprint planning tools**

 Includes full access to all [backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops) and [sprint planning](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/scrum-overview?view=azure-devops) tools.

✔️

✔️

* * *

✔️

✔️

* * *

**Advanced portfolio management**

 Includes full access to define features and epics from a [portfolio backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops) or [board](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-epics-features-stories?view=azure-devops).

✔️

✔️

* * *

**Agile boards**

 Stakeholders get limited access to [boards](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-quickstart?view=azure-devops) and [Taskboards](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/task-board?view=azure-devops). Stakeholders use drag-and-drop to create and change work items, but they can only change the State field on cards. They can only view [the sprint capacity settings](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/set-capacity?view=azure-devops).

✔️

✔️

✔️

* * *

**Agile Portfolio Management**

 Includes limited access to [portfolio backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops) and [boards](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-epics-features-stories?view=azure-devops). Stakeholders can't change the backlog priority order, can't assign items to an iteration, can't use the mapping pane, or can't exercise forecasting.

✔️

✔️

✔️

[**Artifacts**](https://learn.microsoft.com/en-us/azure/devops/artifacts/start-using-azure-artifacts?view=azure-devops)

 Includes full access to all Azure Artifacts features, up to 2-GiB free storage.

✔️

✔️

✔️

* * *

✔️

✔️

✔️

**Basic backlog and sprint planning tools**

 Includes limited access to add and modify items on [backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops) and [sprint backlogs and Taskboards](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/scrum-overview?view=azure-devops). Stakeholders can't assign items to an iteration, use the mapping pane, or forecasting.

✔️

✔️

✔️

✔️

✔️

**Chart Authoring**

 Can create work tracking [query charts](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/charts?view=azure-devops).

✔️

✔️

* * *

**Chart Viewing**

 Can only view work tracking query charts. Stakeholders can't view query charts from the Queries page. They can view them when added to a dashboard.

✔️

✔️

* * *

✔️

✔️

* * *

[**Delivery Plans**](https://learn.microsoft.com/en-us/azure/devops/boards/plans/review-team-plans?view=azure-devops)

 Includes full access to add and view Delivery plans.

✔️

✔️

* * *

[**Delivery Plans**](https://learn.microsoft.com/en-us/azure/devops/boards/plans/review-team-plans?view=azure-devops)

 Includes full access to add and view Delivery plans.

✔️

✔️

* * *

✔️

✔️

* * *

**Standard Features**

 Includes [working across projects](https://learn.microsoft.com/en-us/azure/devops/project/navigation/work-across-projects?view=azure-devops), [view dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops), [view wikis](https://learn.microsoft.com/en-us/azure/devops/project/wiki/filter-print-wiki?view=azure-devops), and [manage personal notifications](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-your-personal-notifications?view=azure-devops). Stakeholders can't view Markdown README files defined for repositories and can only view wiki pages. Access might be restricted based on specific project or organization permissions. For full functionality, including the ability to view all wiki features, a **Basic** license is recommended.

✔️

✔️

✔️

* * *

✔️

✔️

* * *

✔️

* * *

✔️

✔️

* * *

✔️

✔️

✔️

* * *

✔️

✔️

✔️

* * *

✔️

✔️

✔️

* * *

Visual Studio subscribers get **Visual Studio subscription** features as a subscriber benefit. When you add those users, assign them the **Visual Studio subscription** access level.

The system automatically recognizes their subscription and enables any other features included, based on their subscription level.

Visual Studio Enterprise subscribers get **VS Enterprise** access as a subscriber benefit. When you add those users, assign them the **VS Enterprise** access level.

With Visual Studio Enterprise (VS Enterprise) access, users gain access to any fee-based, Marketplace extension published by Microsoft that is included for active Visual Studio Enterprise subscribers.

Advanced access gives users all the Basic features, plus [web-based test case management tools](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops). You can [buy monthly access](https://learn.microsoft.com/en-us/azure/devops/organizations/billing/buy-access-tfs-test-hub?view=azure-devops#buy-monthly-access-to-test-plans) or add users who already have a Visual Studio Test Professional with MSDN or MSDN Platforms subscription.

You can manage access levels programmatically by using the [`az devops user add` (Azure DevOps Services only)](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-organization-users?view=azure-devops) or the [User Entitlement - Add REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/user-entitlements/add). The following table provides a mapping of the access level selected through the user interface and the `AccountLicenseType`, `licensingSource`, and `msdnLicenseType` parameters.

| Access level (user interface) licenseDisplayName | accountLicenseType | licensingSource | msdnLicenseType | GitHubLicenseType |
| --- | --- | --- | --- | --- |
| Basic | express | account | none | none |
| Basic + Test Plans | advanced | account | none | none |
| Visual Studio Subscriber | none | msdn | eligible | none |
| Stakeholder | stakeholder | account | none | none |
| Visual Studio Enterprise subscription | none | msdn | enterprise | none |
| GitHub Enterprise | none | gitHub | none | enterprise |

Note

The `earlyAdopter` accountLicenseType is an internal value used solely by Microsoft.

You can manage access levels programmatically by using the [User Entitlement - Add REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/user-entitlements/add). The following table provides a mapping of the access level selected through the user interface and the `AccountLicenseType`, `licensingSource`, and `msdnLicenseType` parameters.

| Access level (user interface) licenseDisplayName | accountLicenseType | licensingSource | msdnLicenseType |
| --- | --- | --- | --- |
| Basic | express | account | none |
| Basic + Test Plans | advanced | account | none |
| Visual Studio Subscriber | none | msdn | eligible |
| Stakeholder | stakeholder | account | none |
| VS Enterprise | none | msdn | enterprise |

If a user belongs to a group that has **Basic** access and another group that has **VS Enterprise** access, the user can access all features available through **VS Enterprise**, which is a superset of **Basic**.

Add Azure DevOps [service accounts](https://learn.microsoft.com/en-us/azure/devops/server/admin/service-accounts-dependencies) to the default access level. If you make Stakeholder the default access level, you must add the service accounts to Basic or Advanced/VS Enterprise access.

Service accounts don't require a CAL or other purchase.

*   [Stakeholder access quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/stakeholder-access?view=azure-devops)
*   [Get started as a Stakeholder](https://learn.microsoft.com/en-us/azure/devops/organizations/security/get-started-stakeholder?view=azure-devops)
*   [Export a list of users and their access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/export-users-audit-log?view=azure-devops)
*   [Default permissions and access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops)

*   [Stakeholder access quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/stakeholder-access?view=azure-devops)
*   [Change access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-access-levels?view=azure-devops)
*   [Get started as a Stakeholder](https://learn.microsoft.com/en-us/azure/devops/organizations/security/get-started-stakeholder?view=azure-devops)
*   [Compare features between plans](https://azure.microsoft.com/services/devops/compare-features/)
