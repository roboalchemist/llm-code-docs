# Define roles and permissions within a Postman team

Certain team options are only available with **[paid plans](https://www.postman.com/pricing/)**. To learn which roles are available with your plan, go to your **[web dashboard](https://go.postman.co/settings/team/roles)**.

Roles define user permissions within a Postman team and a user's level of access to a Postman element, like a collection or an API.

## Team roles

With the Admin role, you have the power to define Postman access at the team level. You can use Postman's role-based access control system to limit visibility of team resources, define your development workflow, and give access to administrative and billing personnel. Each user on a team must have at least one role attached to them, and can hold multiple roles simultaneously.

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/) one or more role types to team members, based on the functions those team members require:

- **Super Admin** ([Enterprise plans only](https://www.postman.com/pricing/)) - Manages everything within a team, including team settings, members, roles, and resources. This role can view and manage all elements in [internal and public workspaces](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#change-workspace-visibility). Super Admins can perform all actions that other roles can perform. For information on assigning this role, see [Manage Super Admins](/docs/administration/managing-your-team/team-members/manage-roles/#manage-super-admins).
- **Admin** - Manages team members and team settings. Can also view monitor metadata and pause and resume monitors.
- **Billing** - Manages team plan and payments. Billing roles can be granted by a Super Admin, Team Admin, or by a fellow team member with a Billing role.
- **Developer** - Has access to all team resources and workspaces.
- **Community Manager** ([Professional and Enterprise plans only](https://www.postman.com/pricing/)) - Manages the public visibility of workspaces and team profile.
- **Partner Manager** (Internal, [Enterprise plans only](https://www.postman.com/pricing/)) - Manages all [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/manage/) within an organization. Controls Partner Workspace settings and visibility, and can invite, remove, and manage partners. To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).
- **Partner** (External, [Professional and Enterprise plans only](https://www.postman.com/pricing/)) - All partners are automatically granted the Partner role at the team level. Partners can only access the [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/manage/) they've been invited to. To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).
- **Guest** (Internal) - Views collections and sends requests in collections that have been shared with them. This role can't be directly assigned to a user. To learn more, see [Share collections with guest users](/docs/collaborating-in-postman/sharing/#share-collections-with-guests).

If you are on a [Postman Enterprise plan](https://www.postman.com/pricing/), you can also assign roles at the [group level](/docs/administration/managing-your-team/user-groups/).

Team roles offer high-level access control:

| Permission | Super Admin | Admin | Billing | Developer | Community Manager |
| --- | --- | --- | --- | --- | --- |
| Add users | &nbsp;&nbsp; | &nbsp;&nbsp; | | | |
| Remove users | &nbsp;&nbsp; | &nbsp;&nbsp; | | | |
| Update user email for other members of the team by SCIM | &nbsp;&nbsp; | &nbsp;&nbsp; | | | |
| Manage team Admins and Developers | &nbsp;&nbsp; | &nbsp;&nbsp; | | | |
| Manage SSO | &nbsp;&nbsp; | &nbsp;&nbsp; || | |
| Add and edit custom domains | &nbsp;&nbsp; | &nbsp;&nbsp; | | | &nbsp;&nbsp; |
| Delete custom domains | &nbsp;&nbsp; | &nbsp;&nbsp; | | | &nbsp;&nbsp; |
| View audit logs | &nbsp;&nbsp; | &nbsp;&nbsp; | | | &nbsp;&nbsp; |
| View usage data | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Manage Billing members | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | | |
| Manage payment | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | | |
| Change plan | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | | |
| View shared APIs, collections, environments, mock servers, monitors, and flows | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View and create internal workspaces | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Change visibility of workspaces to internal or public | &nbsp;&nbsp; | &nbsp;&nbsp; || | | &nbsp;&nbsp; |
| Enable public team profile | &nbsp;&nbsp; | &nbsp;&nbsp; | | | &nbsp;&nbsp; |
| Manage a team's Private API Network | &nbsp;&nbsp; | &nbsp;&nbsp; || | | &nbsp;&nbsp; |

There are additional specialized roles for [Enterprise](https://www.postman.com/pricing/) teams:

- **API Network Manager** - Manages a team's [Private API Network](/docs/collaborating-in-postman/private-api-network/overview/). To learn more, see [Network roles](#network-roles).
- **API Governance Manager** - Manages [API governance](/docs/api-governance/api-governance-overview/) within a team, including governance [rules](/docs/api-governance/configurable-rules/configuring-api-governance-rules/), [functions](/docs/api-governance/configurable-rules/configuring-custom-governance-functions/), and [workspace groups](/docs/api-governance/configurable-rules/configuring-api-governance-rules/#turn-configured-rules-on-and-off).
- **Partner** (External, [Professional and Enterprise plans only](https://www.postman.com/pricing/)) - All partners are automatically granted the Partner role at the team level. Partners can only access the [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/manage/) they've been invited to. To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).
- **Partner Lead** (External, [Enterprise plans only](https://www.postman.com/pricing/)) - Can invite other partners from their organization to join a [Partner Workspace](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/manage/). To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).

Partner team and Partner Workspace roles relate to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/) and are applied at the team, workspace, and collection levels. There are different team and Partner Workspace roles you can assign to team members and external partners:

|  | For team members | For partners |
| --- | --- | --- |
| **Team level** | Partner Manager | Partner |
| **Workspace level** | Admin, Viewer, Editor | Viewer, Editor |
| **Collection level** | Viewer, Editor | Viewer, Editor |

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/) the Partner Manager role to team members at the team level, and [invite](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/setup/#invite-collaborators-to-a-partner-workspace) partners with the Partner role:

- **Partner Manager** - Manages all Partner Workspaces within an organization. Controls Partner Workspace settings and visibility, and can send invites to partners. If no Partner Manager role is assigned, the Team Admin is auto-assigned the Partner Manager role when they create their first Partner Workspace.
- **Partner** - Can only access the Partner Workspaces they've been invited to. All partners are assigned [Workspace Editor or Viewer](#workspace-roles) roles when invited to a Partner Workspace. You can edit Partner Workspace permissions for partners at the workspace and collection levels.

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-workspace-roles) Partner Workspace roles to partners at the workspace level:

- **Partner Lead** - Can invite other partners from their organization to join a Partner Workspace.
- **Editor** - Partners can create and edit Partner Workspace resources, [import and export](/docs/getting-started/importing-and-exporting/importing-and-exporting-overview/) elements, and [fork](/docs/collaborating-in-postman/using-version-control/forking-elements/) elements to Partner Workspaces within the same team.
- **Viewer** - Partners can view Partner Workspace resources and [fork](/docs/collaborating-in-postman/using-version-control/forking-elements/) elements to another Partner Workspace within the same team where they're assigned the Workspace Editor role.

You can also [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles) Partner Workspace roles to partners at the collection level:

- **Editor** - Partners can [export collections](/docs/getting-started/importing-and-exporting/exporting-data/#export-collections). They can also [fork collections](/docs/collaborating-in-postman/using-version-control/forking-elements/) within the same Partner Workspace or to another Partner Workspace within the same team. They can't fork collections outside the team.
- **Viewer** - Partners can [fork collections](/docs/collaborating-in-postman/using-version-control/forking-elements/) to another Partner Workspace within the same team where they're assigned the Workspace Editor role. They can't fork elements outside the team. Also, they can't export collections.

To learn more about collaborating as a team member or partner, see [Collaborate in a Partner Workspace](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/collaborate/).

## Workspace roles

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-workspace-roles) three role types in Postman workspaces: **Admin**, **Editor**, and **Viewer**. Partner Workspaces offer an additional role type: **Partner Lead**.

- **Admin** - Can manage workspace resources and settings.
- **Editor** ([Professional and Enterprise plans only](https://www.postman.com/pricing/)) - Can create and edit workspace resources.
- **Viewer** ([Professional and Enterprise plans only](https://www.postman.com/pricing/)) - Can view, fork, and export workspace resources.
- **Partner Lead** (External, [Enterprise plans only](https://www.postman.com/pricing/)) - Can invite other partners from their organization to join a [Partner Workspace](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/manage/). To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).

Partners have different permissions for Workspace Editor and Viewer roles in Partner Workspaces ([Enterprise plans only](https://www.postman.com/pricing/)). To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).

You can use the Postman API to programmatically manage users and user groups for workspaces. For more information, see the [Postman API collection](https://api.postman.com/).

The following roles control access at a workspace level:

| Action | Admin | Editor | Viewer |
| --- | --- | --- | --- |
| Join and leave workspaces | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Send requests | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add APIs, collections, environments, flows, and specifications | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Edit and delete specifications | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Move and delete APIs, collections, environments, and flows | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Restore and permanently delete collections | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Manage integrations | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Add and delete monitors and mock servers | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Move mock servers | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Create and delete workspaces | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Edit workspace details | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Add and remove members | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Manage workspace roles | &nbsp;&nbsp; | &nbsp;&nbsp; || |
| Manage workspace visibility | &nbsp;&nbsp; | &nbsp;&nbsp; || |

Workspace Editors can't move or delete any API. They must have the API Admin role on APIs they want to move or delete.

On Professional and Enterprise plans, an Admin for a workspace must request to change its visibility to public. This request will go to the [Community Manager](#team-roles). On Basic and Free plans, or if a team has no Community Manager assigned, an Admin for a workspace can control its visibility.

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-workspace-roles) Partner Workspace roles to partners at the workspace level:

- **Partner Lead** - Can invite other partners from their organization to join a Partner Workspace.
- **Editor** - Partners can create and edit Partner Workspace resources, [import and export](/docs/getting-started/importing-and-exporting/importing-and-exporting-overview/) elements, and [fork](/docs/collaborating-in-postman/using-version-control/forking-elements/) elements to Partner Workspaces within the same team.
- **Viewer** - Partners can view Partner Workspace resources and [fork](/docs/collaborating-in-postman/using-version-control/forking-elements/) elements to another Partner Workspace within the same team where they're assigned the Workspace Editor role.

You can also [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles) Partner Workspace roles to partners at the collection level:

- **Editor** - Partners can [export collections](/docs/getting-started/importing-and-exporting/exporting-data/#export-collections). They can also [fork collections](/docs/collaborating-in-postman/using-version-control/forking-elements/) within the same Partner Workspace or to another Partner Workspace within the same team. They can't fork collections outside the team.
- **Viewer** - Partners can [fork collections](/docs/collaborating-in-postman/using-version-control/forking-elements/) to another Partner Workspace within the same team where they're assigned the Workspace Editor role. They can't fork elements outside the team. Also, they can't export collections.

To learn more about collaborating as a team member or partner, see [Collaborate in a Partner Workspace](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/collaborate/).

## Element-based roles

At the [element](/docs/getting-started/basics/postman-elements/) level, you can assign roles to team members that decide their level of access to the following elements:

- [Collections](#collection-roles)
- [APIs](#api-roles)
- [Environments](#environment-roles)
- [Mock servers](#mock-server-roles)
- [Monitors](#monitor-roles)

## Collection roles

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles) two role types in Postman collections: **Editor** and **Viewer**.

- **Editor** - Can edit collections directly
- **Viewer** - Can view, fork, and export collections

Partners have different permissions for Collection Editor and Viewer roles in Partner Workspaces ([Enterprise plans only](https://www.postman.com/pricing/)). To learn more, see [Partner team and Partner Workspace roles](#partner-team-and-partner-workspace-roles).

You can assign a limited Viewer role to a coworker who isn't in your Postman team by [allowing them to view specific collections](/docs/collaborating-in-postman/sharing/#share-collections-with-guests). Users with this role can only view specific collections and send requests in the collections that have been shared with them.

The following roles control access at a collection level:

| Collections | Editor | Viewer |
| --- | --- | --- |
| Edit, delete, and restore collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View deleted collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Manage roles on collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Export collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Fork collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Merge forks on collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Publish collection documentation and add to API Network | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Share collection variables | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Share collections to a different workspace | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Tag collections | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add, edit, and delete mock servers | &nbsp;&nbsp; | &nbsp;&nbsp; |

## API roles

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles) three role types in Postman APIs: **Admin**, **Editor**, and **Viewer**.

- **Admin** - Can publish, move, and delete APIs
- **Editor** - Can edit APIs and API definitions
- **Viewer** - Can view published API versions

If you have the [Workspace Admin](/docs/administration/roles-and-permissions/#workspace-roles) role, you will automatically inherit Admin permissions for all APIs in the workspace, even if you are assigned the Editor or Viewer role for an API.

The following roles control access at an API level:

| APIs | Admin | Editor | Viewer |
| --- | --- | --- | --- |
| Edit APIs and API definitions | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Publish APIs | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Move and delete APIs | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Manage roles on APIs | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Comment on APIs | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Comment on published API versions | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Share APIs | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Generate collections from the API definition | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add and remove API documentation collections | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add and remove API test collections | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add and remove CI integrations | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add and remove APM integrations | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Add and remove API gateway integrations | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View reports for APIs | &nbsp;&nbsp; | &nbsp;&nbsp; | &nbsp;&nbsp; |

API Editors can assign users the Viewer or Editor role. API Editors can't assign a user the Admin role, or change an Admin to an Editor or Viewer.

## Environment roles

You can [assign](/docs/sending-requests/variables/team-environments/#share-an-environment) two role types for Postman environments: **Editor** and **Viewer**.

- **Editor** - Can edit and manage environments
- **Viewer** - Can view and use environments

The following roles control access at an environment level:

| Environment | Editor | Viewer |
| --- | --- | --- |
| View environment | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Use environment | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Edit environment variables | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Share environment variables | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Edit and delete environments | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Manage environment roles | &nbsp;&nbsp; | &nbsp;&nbsp; |

## Mock server roles

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles) two role types for Postman mock servers: **Editor** and **Viewer**.

- **Editor** - Can edit and manage mock servers
- **Viewer** - Can view mock servers and associated metadata

The following roles control access at the mock server level:

| Mock server | Editor | Viewer |
| --- | --- | --- |
| View mock server | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View mock server call logs and call log details | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View mock server metadata | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Edit and delete mock servers | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Manage mock server roles | &nbsp;&nbsp; | &nbsp;&nbsp; |

## Monitor roles

You can [assign](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles) two role types for Postman Monitors: **Editor** and **Viewer**.

- **Editor** - Can view monitor metadata, metrics, jobs, and runs. Can also run, update, delete, pause, and resume the monitor.
- **Viewer** - Can view monitor metadata, metrics, jobs, and runs.

Monitors | Editor | Viewer |
| --- | --- | --- |
| View monitor | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View monitor metadata, results, activity, and summary metrics | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Create monitor read integrations | &nbsp;&nbsp; | &nbsp;&nbsp; |
| View monitor based integrations | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Edit and delete monitor | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Run, pause, and resume monitor | &nbsp;&nbsp; | &nbsp;&nbsp; |
| Update monitor roles | &nbsp;&nbsp; | &nbsp;&nbsp; |