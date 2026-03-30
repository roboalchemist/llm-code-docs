# Source: https://docs.axonius.com/docs/identities-resources.md

# Identities Resources

The following are some of the resources included with Axonius Identities.

## Profiles

Profiles simplify and streamline managing user entitlements by allowing admins to create and manage groups of entitlements collectively. Additionally, Profiles enable consistent and secure permission assignments and they provide a more efficient process for users to request access to resources.

<Image align="center" alt="ProfilesAssets.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProfilesAssets.png" />

## Rules

Use the Rules page to manage all rules in the system. Admins can control rule usage and create, manage, and enforce them. Rules provide a set of consistent and manageable entitlements to users.

<Image align="center" alt="RulesAssets.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesAssets.png" />

## Role Mining

Role mining delves deep into your organization's access landscape, analyzing user access patterns to identify common combinations of entitlements. This process reveals the underlying roles and responsibilities within your organization, even those that may not be formally defined. By understanding these roles, you can optimize access controls, streamline user provisioning, and strengthen security by ensuring that individuals have the appropriate access rights for their specific responsibilities. This not only improves operational efficiency but also mitigates the risk of unauthorized access and data breaches.

The [Role Mining Simulator](/docs/using-the-role-mining-simulator) helps visualize the distribution of entitlements assigned to roles. You can also use the simulator to investigate entitlement drift.

<Image alt="RoleMiningSimExample.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMiningSimExample.png" />

## Peer Group Simulator

Peer group analysis compares an individual's performance, behavior, or characteristics against a group of similar individuals/peers. This approach is valuable for identifying anomalies, trends, or outliers by highlighting deviations from the norm within the peer group.

Organizations need help maintaining security and compliance when employees accumulate unnecessary or excessive permissions over time, leading to potential over-privilege or unauthorized access.

The [Peer Group Simulator](https://docs.axonius.com/axonius-help-docs/docs/peer-group-simulator) enhances security by automatically detecting drift, where an employee's entitlements significantly differ from their peers. This feature minimizes security risks by proactively identifying and managing these deviations.

By visualizing these comparisons, complex data is more accessible and easier to understand. This allows for quick identification of critical issues that otherwise would have been difficult to discover.

<Image alt="Peer Group Simulator" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeerGroupSimulator.png" />

You can configure the Peer Group Simulator in [System Settings](/docs/configuring-data-processing-settings#peer-group-analysis-settings).

## Queries

In addition to all the fields and operators available for all other adapters, Identities adapters also include the "Excessive Entitlements Count" field, which contains the number of excessive entitlements. Each assigned entitlement also has the additional attribute “Is Excessive”, which is set to TRUE if this entitlement is one of the excessive entitlements found or FALSE which indicates this is an entitlement that most of the team has.

<Image align="center" alt="ExcessiveEntitlementsPopup.png" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExcessiveEntitlementsPopup.png" />

## Compare Permission Chart

The Compare Permission chart can be added to any dashboard. It is a small version of the Peer Group Simulator chart. Adding this to a frequently used dashboard can enhance awareness of permission drift.

<Image align="center" alt="ComparePermissionChart.png" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ComparePermissionChart.png" />

## Rules Simulator

Use the [Rule Simulator](https://docs.axonius.com/axonius-help-docs/docs/rules-simulator) to build a Query Intersection Venn diagram to compare between rules that grant access and permissions. This helps you learn about the rules in your organization and determine when multiple rules can be condensed, making your rules easier to manage.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesSimulator\(1\).png)

## Campaigns

Use [Access Reviews](https://docs.axonius.com/axonius-help-docs/docs/campaigns-page) to set up and carry out periodic assessments to verify the continued need of users' previously granted access to software, applications, and permissions in your organization. After initiating a Campaign, you can monitor its progress, and determine whether to approve or revoke user access.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CampaignsPage.png)

## Entitlement Types

These are some of the entitlement types that can be managed with Axonius Identities.

### Group Membership

Being a member of a group automatically grants access to all permissions and other entitlements the group has. Most applications, if not all, have the concept of a group. This is probably the preferred way to manage access to applications instead of granting specific permissions to a user.

Managed Identity can have two types of group lists:

* **Assigned groups** - Groups that were directed and assigned to the user
* **Nested groups** - Groups that were assigned directly and indirectly through a group membership. In this case, there will always be additional detail on a group that shows how it was granted “Directly” or otherwise.

<Image align="center" alt="AssignedGroups.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignedGroups.png" />

<Image align="center" alt="NestedGroups.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NestedGroups.png" />

### Permissions

The lowest level of access available in an application provides very specific access to take a very specific action.

### Roles

A role is assigned to a user and granted permission. Not all applications have the concept of a Role. A list of assigned roles is available in the Assigned Roles table for each identity.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignedRoles.png)

### Resources

A resource is a data source or a computing service that does a task. It is usually an object to which you can manage access. Assigned resources are listed in the asset page for each managed identity.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignedFields.png)

### Justifications

[Justifications](https://docs.axonius.com/axonius-help-docs/docs/justifications) provide a clear and auditable record of why a user has access to specific resources or data. They support informed decision-making, risk mitigation, compliance adherence, and collaboration among stakeholders. Justifications enhance transparency and accountability in access management, ensuring that access decisions are well-documented and aligned with organizational policies.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JustificationsExample.png)