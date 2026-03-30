# Source: https://docs.port.io/sso-rbac/rbac-overview.md

# Port RBAC capabilities overview

This page provides a comprehensive summary of all of Port's RBAC capabilities, and links to their associated documentation pages. They are grouped into 3 key topics:

[1 - Catalog RBAC & Ownership](#catalog-rbac--ownership)

[2 - RBAC for Self Service Actions](#rbac-for-self-service-actions)

[3 - RBAC for operating the Port platform](#rbac-for-operating-the-port-platform)

## Catalog RBAC & Ownership[â](#catalog-rbac--ownership "Direct link to Catalog RBAC & Ownership")

### Hide & show catalog pages dynamically[â](#hide--show-catalog-pages-dynamically "Direct link to Hide & show catalog pages dynamically")

With Port, you can offer a personalized experience for the various personas of your organization.

For instance, you can create:

* A unique Costs dashboard only visible to team leaders.
* A deep-dive view of services for developers.
* A security dashboard & catalog view for security teams.

![](/img/software-catalog/role-based-access-control/overview/personalizedcatalog.png)

<br />

<br />

To achieve this, you can assign user or team ownership permissions to the various personas logging in to Port.<br /><!-- -->To configure who can see which pages, refer to the [Page Permissions](/customize-pages-dashboards-and-plugins/page/page-permissions.md) page.

### Configuring team ownership[â](#configuring-team-ownership "Direct link to Configuring team ownership")

Port allows you to assign ownership of specific entities to teams in your organization, enabling personalized views such as "**show me my teamâs services**" or "**my pull requests**".

`User` and `Team` are blueprints, enabling to create relations and inherit ownership.

![](/img/software-catalog/role-based-access-control/overview/user-and-teams.png)

For more details about **ownership** in Port, see the [relevant documentation](/sso-rbac/users-and-teams/manage-users-teams.md#ownership).

### Dynamic team filtering[â](#dynamic-team-filtering "Direct link to Dynamic team filtering")

Once the team ownership is properly configured we can create dynamic filtering, and show users personalized views such as "`my open Pull Requests`" or "`my teamâs services`". We can also lock views to prevent a user from seeing services that are outside of his/her teamâs scope.

#### My Team filter & Lock page view[â](#my-team-filter--lock-page-view "Direct link to My Team filter & Lock page view")

By using the `My Teams filter` you will only see entities that belong to one of your teams. This means you will only see entities from teams that you are a member of.

![](/img/software-catalog/role-based-access-control/overview/myteamfilter.png)

<br />

<br />

You may "Save this view" to permanently keep the filters.<br /><!-- -->For more details about view customization, see the [customization documentation](/customize-pages-dashboards-and-plugins/page/catalog-page.md#my-teams-filter).

#### Filter a catalog page to the user's team[â](#filter-a-catalog-page-to-the-users-team "Direct link to Filter a catalog page to the user's team")

Another way to personalize a catalog page view is to use [initial filters](/customize-pages-dashboards-and-plugins/page/catalog-page.md#initial-filters). These allow you to create advanced and dynamic filters, invisible to "regular" users.

With initial filters you can create views such as:

* Filter all entities owned by `My Team` (or more dynamic queries).
* Filter entities based on dates (e.g. PRs created in the last 90 days).

Leveraging teams as blueprints, we can create advanced business logics, such as services belonging to a specific product:

![](/img/software-catalog/role-based-access-control/overview/businesslogic.png)

<br />

<br />

To achieve this, you can use the `Owning Teams` value to `My Teams`, or use the `relatedTo` dynamic filters, for example:

![](/img/software-catalog/role-based-access-control/overview/initial-filters.png)

<br />

<br />

Initial filters offer an easy way to **lock a Catalog Page view dynamically for the logged in user's team**.

#### Dynamic filters for dashboard widgets[â](#dynamic-filters-for-dashboard-widgets "Direct link to Dynamic filters for dashboard widgets")

Advanced filters and dynamic filters are also available for [dashboard widgets](/customize-pages-dashboards-and-plugins/dashboards/overview.md) in your catalog or homepage, using the same logic as described in the **Filters** or **Initial Filters** section above.

You can create widgets with data dynamically based on the logged in userâs identity or team's ownserhip.

### Granular entity permission control[â](#granular-entity-permission-control "Direct link to Granular entity permission control")

It is possible to assign more granular permissions on **entities** to prevent users from reading or editing certain properties or relations.

This is an advanced feature and is only recommended in large enterprises with complex RBAC use cases. In most cases dynamic filtering would be a simpler and more effective way to achieve the same outcome.

[Granular Entity RBAC](/build-your-software-catalog/set-catalog-rbac/.md#set-granular-access-controls-to-catalog-data)

## RBAC for Self Service Actions[â](#rbac-for-self-service-actions "Direct link to RBAC for Self Service Actions")

### Self Service permissions[â](#self-service-permissions "Direct link to Self Service permissions")

When creating/editing self-service actions, you can set permissions for who can trigger or approve an action.

![](/img/software-catalog/role-based-access-control/overview/ssapermissions.png)

<br />

<br />

For more details about action permissions, see the [relevant documentation](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/.md#configure-permissions-for-actions).

### Dynamic permissions for Self Service actions[â](#dynamic-permissions-for-self-service-actions "Direct link to Dynamic permissions for Self Service actions")

Port allows setting `dynamic permissions` for executing and/or approving execution of self-service actions, based on any properties/relations of an action's corresponding blueprint.

Potential use-cases:

* Ensure that action executions requested by a team member can only be approved by his/her direct manager.
* Perform validations/manipulations on inputs that depend on data from related entities.
* Ensure that only those who are on-call can perform rollbacks of a service with issues.

Dynamic permissions for RBAC can run any query on the Port data model.

For more details about dynamic permissions, see the [relevant documentation](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/dynamic-permissions/.md).

## RBAC for operating the Port platform[â](#rbac-for-operating-the-port-platform "Direct link to RBAC for operating the Port platform")

### Port administration roles[â](#port-administration-roles "Direct link to Port administration roles")

Port supports 3 role types:

| Role                         | Description                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Admin**                    | Can perform any operation on the platform.                                                                            |
| **Moderator** of a Blueprint | Can perform any operation on a specific blueprint and its entities. A user can be a moderator of multiple blueprints. |
| **Member**                   | Has read-only permissions + permissions to execute actions.                                                           |

Configurable permissions

The roles above have configurable permissions that are described in the following section. It is possible to have multiple moderator roles, allowing highly granular permission management across the developer portal.

In addition to the permissions designated for each role, permissions are also inherited based on the following hierarchy: **Admin** > **Moderator** > **Member**.

For more details about Port roles, see the [relevant documentation](/sso-rbac/users-and-teams/manage-users-teams.md#roles--permissions).

### Support user access[â](#support-user-access "Direct link to Support user access")

Port's support team may require access to your organization to provide technical assistance. This access is controlled through support user permissions which can be edited in the [Builder](https://app.getport.io/settings/data-model) page of your portal under the `Organization settings` in the left sidebar.

For more information, see the [support user permissions](/sso-rbac/users-and-teams/manage-users-teams.md#support-user-permissions).

### Blueprint permissions[â](#blueprint-permissions "Direct link to Blueprint permissions")

Blueprint permissions allow a granular configuration of the various roles: admin, member or blueprint collaborator. You can decide, for example, that a member has edit permissions for a specific Blueprint but not for another.

For more details about Blueprint permissions, see the [relevant documentation](/build-your-software-catalog/set-catalog-rbac/examples.md#use-cases-).
