# Source: https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control

Title: Role-Based Access Control

URL Source: https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control

Markdown Content:
Overview[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#overview)
---------------------------------------------------------------------------------------------------------------------------

Role-Based Access Control (RBAC) is a permission management system that restricts access to Fivetran resources based on user roles. Each user is assigned a role that determines what they can view or manage. RBAC ensures users only have access to the resources relevant to their responsibilities.

In our RBAC model, we provide a set of [standard](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#standardrolesinourrbacmodel) and [custom](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#customrolesinourrbacmodel) roles to grant or deny access to various Fivetran resources within an account:

*   [Account](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings)
*   [Destinations](https://fivetran.com/docs/destinations)
*   [Connections](https://fivetran.com/docs/core-concepts)
*   [Transformations](https://fivetran.com/docs/transformations)

Activations permissions are managed through Workspaces, separate from the Fivetran RBAC model. While all users can view the Activations tab, you must request workspace access from the Owners of the workspace or a Fivetran Account Administrator to use it. Learn more in our [Workspaces documentation](https://fivetran.com/docs/activations/misc/security-and-privacy/workspaces).

User roles also manage permissions for related areas of each resource, like the External logging services and Transformations for the Destinations resource.

Our RBAC model introduces the following features:

*   [Teams](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#teams) let you scale role and permission management across a large number of employees easily, while not affecting an individual employee's role and permissions.Delegating permissions from account-level user and team roles to users and teams — scoped per destination or connection — along with support for custom role creation and assignment.
*   The Destination Creator and Create Connection roles automatically give you and your team members control over the destinations or connections you or your team create. This access automation lets you eliminate any waiting time for the approval by the central data team and independently manage access permissions for the resource right after its creation.

* * *

RBAC model benefits[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#rbacmodelbenefits)
-----------------------------------------------------------------------------------------------------------------------------------------------

For enterprise customers, a typical team structure might look like this:

*   A core data team manages a central destination within the organization's Fivetran account.
*   One or more teams manage centralized destinations, such as Snowflake, and are responsible for the data that lands in the destinations.
*   One or several project or operational teams need to manage their specific data sources.

RBAC supports this typical team structure by offering flexibility in how roles and permissions are granted and delegated:

*   **Fast access** - Project and operational teams get immediate access to the data they need - without delays caused by dependencies on core data teams.
*   **Reduced burden** - Centralized teams avoid the overhead of manually managing access requests.
*   **Granular control** - Permissions can be precisely scoped to meet enterprise compliance and security requirements.

* * *

Standard roles in our RBAC model[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#standardrolesinourrbacmodel)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fivetran’s RBAC model supports fine-grained, hierarchical access control across three main resource types, listed from highest to lowest:

*   **Account** - Account-level roles grant permissions to manage all destinations and connections.
*   **Destination** - Destination-level roles allow control over a specific destination and its connections.
*   **Connections** - Connection-level roles only provide permissions for specific connections.

Roles assigned at a higher level cascade down to lower levels. For example, an account-level role may include permissions to manage all destinations and connections, whereas a connection-level role cannot access account-level settings.

For a user to have access to all destinations, assign an account-level role with the necessary permissions. For a user needing access to a specific destination and its connections, set a destination-level role.

The following table lists the user roles in our RBAC model:

| Current RBAC Model User Role | Legacy RBAC Model User Role | Description |
| --- | --- | --- |
| Account Administrator | Owner | View and edit [account information](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#accountmanagement), including [billing](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#billing), [usage](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#usage), [users](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#users), [roles](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#roles), [API access](https://fivetran.com/docs/rest-api), and [security settings](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#settings). Create, view, edit, and delete [destinations](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#destinations) and [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). Create, view, edit, and delete [transformations](https://fivetran.com/docs/transformations) and manage [external logging services](https://fivetran.com/docs/logs/external-logs). Register [HVR](https://fivetran.com/docs/hvr6) hub system. |
| Account Billing | Billing | View billing and usage information. _Cannot_ edit security settings, users, roles, destinations, and connections. |
| Account Analyst | N/A | View the list of destinations and users in the account. View destinations and view, create, edit and delete [transformations](https://fivetran.com/docs/transformations). Create, view, edit, and delete [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). _Cannot_ edit account information. _Cannot_ create, edit, or delete destinations. |
| Account Reviewer | Read Only | View account information, destinations, and connections. _Cannot_ edit account information. _Cannot_ create, edit, or delete destinations and connections. |
| Destination Creator | N/A | Create new [destinations](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#destinations). _Cannot_ view, edit, or delete existing destinations. _Cannot_ create, view, edit, or delete connections. _Cannot_ edit account information. Destination Creators are Destination Administrators in destinations they created. |
| Manage Destination | Destination Administrator | View, edit, and delete [destinations](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#destinations). Create, view, edit, and delete [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). Create, view, edit, and delete [transformations](https://fivetran.com/docs/transformations) and manage [external logging services](https://fivetran.com/docs/logs/external-logs). _Cannot_ edit account information. |
| Edit Destination | Destination Analyst | View destinations. Create, view, edit, and delete [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). Create, view, edit, and delete [transformations](https://fivetran.com/docs/transformations). _Cannot_ edit account information. |
| View Destination | Destination Reviewer | View the [destinations](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#destinations) that you are invited to and their associated [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). _Cannot_ create, edit, or delete destinations or connections. _Cannot_ edit account information. |
| Create Connection | Connection Creator | Create, view, edit, and delete [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). View [destinations](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#destinations) in which this role is assigned. _Cannot_ create, edit, or delete destinations. _Cannot_ edit account information. Connection Creators have the Manage Connection role for the connections they created. |
| Manage Connection* | Connection Administrator | View, edit, and delete [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors). _Cannot_ create new connections. _Cannot_ create, view, edit, and delete destinations. _Cannot_ edit account information. |
| Edit Connection* | Connection Collaborator | View and edit [connections](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors) assigned to the role. _Cannot_ create or delete connections. _Cannot_ view, create, edit, and delete destinations. _Cannot_ edit account information. |
| View Connection* | Connection Reviewer | View connections assigned to the role. _Cannot_ create, edit, or delete connections. _Cannot_ create, view, edit, or delete destinations. _Cannot_ edit account information. |

See our [Role Permission Matrix Tables documentation](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control/permission-matrix-tables) for more details on the permissions each standard role provides.

You can only use account-level roles with [Fivetran SCIM user provisioning](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/scim). Destination-level or connection-level roles are not supported in the Fivetran SCIM API.

### How our RBAC model works[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#howourrbacmodelworks)

Our RBAC model works as follows:

![Image 1: RBAC-model flow](https://fivetran.com/static-assets-docs/_next/static/media/rbac-how-it-works.61cb1719.png)

1.   Account administrators manage the entire account. They add users with the Destination Creator or Manage Destination role for existing destinations.
2.   Users with the Destination Creator role can create and manage destinations they add.
3.   Any user with the Manage Destination role can add teams that need to sync data to the destination.
4.   Each team has a team manager who adds users to the team as team members, or remove them from the team.
5.   Team roles in account, destinations, and connections allow delegating permissions in the corresponding resources in the same way as user roles do. This means that teams also don't have to rely on users with Manage Destination or Account Administrator roles to manage memberships. In turn, users with the Manage Destination role don't have to rely on Account Administrators to create destinations or add teams.

### How we recommend using our RBAC model[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#howwerecommendusingourrbacmodel)

#### Account permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#accountpermissions)

1.   Get a list of users who need access to the entire account.
2.   Set up a team and add these users to the team.
3.   Set the team's role to Account Administrators.

We recommend having at least two Account Administrators at all times. A single Account Administrator may be locked out due to a potential security breach, or be unavailable when, for example, a role needs to be assigned or unassigned.

#### Destination permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#destinationpermissions)

1.   Get a list of users who need to set up their own destinations.
2.   Map the list of destinations to the list of users who need to manage it.
3.   Create a team per destination or a set of destinations.
4.   Assign the team to each of those destinations.

We recommend having at least two users with the Manage Destination role at all times. A single user may be locked out due to a potential security breach, or be unavailable when, for example, a destination needs to be edited or deleted).

#### Connection permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#connectionpermissions)

1.   Get a list of connections syncing data to Fivetran.
2.   Get a list of teams who own those connections and map them out.
3.   Get a list of managers for those teams.
4.   Set up teams and associate connection level permissions.

We recommend having one team with the Manage Connection role per connection. If a user from another team needs to be added, that individual user can be added to the team that manages the connection.

* * *

Custom roles in our RBAC model[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#customrolesinourrbacmodel)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you're on the [Enterprise or Business Critical plan](https://www.fivetran.com/pricing/features), in addition to our [standard roles](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#standardrolesinourrbacmodel), you also can create and manage custom roles that allow modifying both the access scope and resource area permissions.

* * *

RBAC permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#rbacpermissions)
------------------------------------------------------------------------------------------------------------------------------------------

The following table describes the permissions we use in our RBAC model:

| Permission | Description |
| --- | --- |
| View | Allows user to view the relevant resource areas. Applicable for: * Settings, Billing, and Roles in Account * Destinations * Users, External logging services, and Transformations in Destinations * Connections |
| Create | Allows users to create and then view and manage only those objects of the relevant resource areas they created. Applicable for: * Destinations (the custom role must have **Account Access** enabled to create destinations) * Connections |
| Edit | Allows user to edit and view objects of the relevant resource areas. Applicable for: * Settings and Billing in Account * Connections * Destinations |
| Manage | Allows user to view, create, edit, and delete objects of the relevant resource areas. Applicable for: * Users and Roles in Account * Destinations * Users, External logging services, and Transformations in Destinations * Connections |
| None | Disables user's access to objects in the relevant resource area. Applicable for: * Users, Settings, Billing, and Roles in Account * Transformations in Destination |

The following tables show the list of permissions used for each resource area.

### Account permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#accountpermissions_1)

| Resource area | Permissions |
| --- | --- |
| Settings | Edit, View, None |
| Billing | Edit, View, None |
| Roles | Manage, View, None |
| Users | Manage, None |

### Destination permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#destinationpermissions_1)

| Resource area | Permissions |
| --- | --- |
| Destinations | Manage, Create*, Edit, View |
| Users | Manage, None |
| External logging services | Manage, None |
| Transformations | Manage, View, None |

*The custom role must have **Account Access** enabled to create destinations.

### Connection permissions[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#connectionpermissions_1)

You can grant the user role access to either **All**, **Selected** connection types, or **None**.

For connections, you can select one of the following permissions:

*   Manage
*   Create
*   Edit
*   View

You must be logged in as an Account Administrator or use a custom role with the **Roles:Manage** permission to create a custom user role.

* * *

Teams[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#teams)
---------------------------------------------------------------------------------------------------------------------

Teams allow you to organize users into logical groups that reflect your organizational structure, including external contractors. Teams simplify permissions management across destinations and connections by letting you assign roles to groups instead of individuals.

[Account Administrators](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#standardrolesinourrbacmodel) and [Team Managers](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#assignandunassignuserstheteammanagerrole) can add users to one or multiple teams. Each team has a standard or custom role in the account and one or several destinations as well as for each connection in the destinations. For each team member, the team role extends the account permissions and group/destination permissions, including the connection permissions that the team member is assigned as an account user. For example, if your role in the destination has View permissions for all connections, and your team role has the Manage permission for all connections, then you can manage all connections in the destination.

A team can be assigned permissions to create a destination. A team is assigned the Manage Destination role for any destination it creates. A team can manage destinations and connections where the team has the Manage Destination or Manage Connection role, respectively. This includes assigning roles in the relevant resource to users and teams.

You must be logged in as an Account Administrator or use a custom role with the **Roles:Manage** permission to create a custom user role. Therefore, you must have an [Enterprise or Business Critical plan](https://www.fivetran.com/pricing/features) to create and manage teams.

### Teams vs. organizations[](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#teamsvsorganizations)

We recommend using teams when you want to ensure that only the relevant users or groups of users have access to the relevant destinations, connections or account settings. We recommend using [organizations](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/organizations) when you need to use separate security settings - [SAML](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/sso) or [SCIM](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/scim).

Thanks for your feedback!

Was this page helpful?
