# Source: https://www.apollographql.com/docs/graphos/platform/access-management/member-roles.md

# Members, Roles, and Permissions

A GraphOS organization can have any number of members, and each member can be assigned a *role* that defines their capabilities within the organization.

## Organization-wide member roles

Each organization member has one of the following roles:

| Name                | Description                                                                                                                                                                                                                                                                                                                                                                                   | Supported [plan types](https://www.apollographql.com/pricing?referrer=docs-content) |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------: |
| **Org Admin**       | Has management access to the entire organization, including its members, graphs, and configuration.                                                                                                                                                                                                                                                                                           |                                         All                                         |
| **Graph Admin**     | Has management access to the organization's graphs, but not to members or organization-level configuration. Intended for developers who are considered admins to the graph.                                                                                                                                                                                                                   |                               Enterprise and Standard                               |
| **Contributor**     | Can push new schemas to graphs, but cannot configure graph settings or integrations. Intended for backend developers who are authorized to make changes to graphs. Cannot push schema changes or report metrics for [protected variants](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only).                                   |                               Enterprise and Standard                               |
| **Documenter**      | Has all permissions of the Observer role, plus the ability to edit graph READMEs, descriptions, and similar non-operational metadata.                                                                                                                                                                                                                                                         |                               Enterprise and Standard                               |
| **Observer**        | Has view-only access to the organization's graph data, such as schemas and metrics. Can also execute queries in the Explorer. Intended for backend developers who are not authorized to make changes to graphs.                                                                                                                                                                               |                               Enterprise and Standard                               |
| **Consumer**        | Has view-only access to the organization's API schemas, but not supergraph or subgraph schemas, or metrics. Can also execute queries in the Explorer. Intended for application developers building clients against a graph.This role is available to all plan types. For plans that charge per user, Consumers do not count as billed users.                                                  |                                         All                                         |
| **Billing Manager** | Has management access to organization-level configuration and billing. Can also remove members (but not invite them). No access to graphs. [Learn more](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles.md#billing-managers).This role is available to all paid plan types. For plans that charge per user, Billing Managers do not count as billed users. |                                 All paid plan types                                 |

Only members with the **Org Admin** role can assign roles to other members. You can see which role you have in a particular organization from your [user settings page](https://studio.apollographql.com/user-settings), or from the organization's Members tab.

## Graph-specific member roles

You can override a member's organization-wide role for individual graphs. For example, if a member has the **Observer** role in your organization, you can assign them the **Contributor** role for a graph that they need extra access to.

A member's graph-specific role must have more permissions than their organization-wide role.

Members with the **Graph Admin** or **Org Admin** role can assign graph-specific roles from the Permissions tab of the graph's Settings page.

### Hidden graphs

If a graph is made [hidden](https://www.apollographql.com/docs/graphos/platform/access-management/org#internal-graph-visibility-enterprise-only), then only users with explicit overrides (as well as **Org Admin**s) can see the graph.

### Graph admin override

The **Graph Admin** and **Org Admin** roles have exactly the same permissions for a particular graph, so you can only grant a **Graph Admin** override, not an (equivalent) **Org Admin** override.

### Default on graph creation

When **Contributor**s in an organization create a new graph, they are automatically granted the **Graph Admin** role for that graph.

## Role permissions

### Organization management permissions

| Action                                                                                                                                                              | Org Admin | Graph Admin | Contributor | Observer / Documenter | Consumer |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------: | :---------: | :---------: | :-------------------: | :------: |
| Manage organization configuration (name, avatar, etc.)                                                                                                              |     ✓     |             |             |                       |          |
| Delete the organization                                                                                                                                             |     ✓     |             |             |                       |          |
| View and edit billing information                                                                                                                                   |     ✓     |             |             |                       |          |
| Invite members                                                                                                                                                      |     ✓     |             |             |                       |          |
| Remove members                                                                                                                                                      |     ✓     |             |             |                       |          |
| Change member roles                                                                                                                                                 |     ✓     |             |             |                       |          |
| Revoke [individual member's sessions](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles.md#revoking-member-sessions)               |     ✓     |             |             |                       |          |
| Change [organization session length](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles.md#studio-session-length) (enterprise only) |     ✓     |             |             |                       |          |
| Export [audit logs](https://www.apollographql.com/docs/graphos/platform/access-management/audit-log)  (enterprise only)                                             |     ✓     |             |             |                       |          |
| Manage which users have access to graphs                                                                                                                            |     ✓     |      ✓      |             |                       |          |

### Graph management permissions

| Action                                           | Org Admin | Graph Admin |                                                                   Contributor                                                                   | Observer / Documenter | Consumer |
| :----------------------------------------------- | :-------: | :---------: | :---------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------: | :------: |
| View and manage graph API keys                   |     ✓     |      ✓      |                                                                                                                                                 |                       |          |
| Manage graph integrations (Slack, Datadog, etc.) |     ✓     |      ✓      |                                                                                                                                                 |                       |          |
| Delete and rename graphs                         |     ✓     |      ✓      |                                                                                                                                                 |                       |          |
| Create graphs                                    |     ✓     |      ✓      |                                                                        ✓                                                                        |                       |          |
| Create new variants                              |     ✓     |      ✓      | Non-[protected](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only) variants only |                       |          |
| Push schemas to a graph                          |     ✓     |      ✓      | Non-[protected](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only) variants only |                       |          |
| Manage Explorer settings (URL, etc)              |     ✓     |      ✓      | Non-[protected](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only) variants only |                       |          |
| Report graph usage metrics 1                     |     ✓     |      ✓      | Non-[protected](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only) variants only |                       |          |
| See the schemas of subgraphs in federated graphs |     ✓     |      ✓      |                                                                        ✓                                                                        |           ✓           |          |
| View graph usage metrics and traces 2            |     ✓     |      ✓      |                                                                        ✓                                                                        |           ✓           |          |
| Edit variant READMEs                             |     ✓     |      ✓      |                                                                        ✓                                                                        |    Documenter only    |          |
| Query graphs with the Explorer                   |     ✓     |      ✓      |                                                                        ✓                                                                        |           ✓           |     ✓    |
| View graph schemas and changelogs                |     ✓     |      ✓      |                                                                        ✓                                                                        |           ✓           |     ✓    |

1. When you [report metrics from GraphOS Router or Apollo Server](https://www.apollographql.com/docs/graphos/platform/insights/sending-operation-metrics/#from-graphos-router-or-apollo-server)
   you should use a graph API key. For non-protected variants, the [graph API key role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles.md#graph-api-key-roles)
   must be Contributor, Org Admin, or Graph Admin. For [protected variants](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only),
   only Org and Graph Admin roles can report metrics.

2. Currently, graph usage metrics and traces are not displayed to Consumers
   via the Studio web app, but they are not blocked at the API layer. We intend to
   remove this capability from Consumers, but for the time being you should understand
   that Consumers are not fully prevented from accessing these metrics and traces.

### Schema checks permissions

Learn more about [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks).

| Action                                                                                                                             | Org Admin | Graph Admin | Contributor | Observer / Documenter | Consumer |
| :--------------------------------------------------------------------------------------------------------------------------------- | :-------: | :---------: | :---------: | :-------------------: | :------: |
| Modify schema checks configuration                                                                                                 |     ✓     |      ✓      |             |                       |          |
| Override [flagged checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks#overriding-flagged-changes) |     ✓     |      ✓      |             |                       |          |
| Run schema checks                                                                                                                  |     ✓     |      ✓      |      ✓      |           ✓           |          |

### Schema proposals permissions

The table below shows default schema proposal settings. You can [configure which roles can create, edit, and approve proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/configure#configure-permissions-and-approvals).

| Action                 | Org Admin | Graph Admin | Contributor | Observer / Documenter | Consumer |
| :--------------------- | :-------: | :---------: | :---------: | :-------------------: | :------: |
| Change proposal status |     ✓     |      ✓      |             |                       |          |
| Create proposals       |     ✓     |      ✓      |      ✓      |           ✓           |          |
| Edit proposals         |     ✓     |      ✓      |      ✓      |           ✓           |          |
| Add reviewers          |     ✓     |      ✓      |      ✓      |           ✓           |          |
| View proposals         |     ✓     |      ✓      |      ✓      |           ✓           |     ✓    |
| Make comments          |     ✓     |      ✓      |      ✓      |           ✓           |     ✓    |
| Approve proposals      |     ✓     |      ✓      |      ✓      |           ✓           |     ✓    |

### Contract permissions

Learn more about [contracts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview).

| Action                                            | Org Admin | Graph Admin | Contributor | Observer / Documenter | Consumer |
| :------------------------------------------------ | :-------: | :---------: | :---------: | :-------------------: | :------: |
| Create and modify contracts and contract variants |     ✓     |      ✓      |             |                       |          |
| View existing contracts                           |     ✓     |      ✓      |      ✓      |                       |          |

### Persisted queries permissions

Learn more about [persisted queries](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries).

| Action                                  | Org Admin (User) | Graph Admin (User) | Contributor (User) | Observer (User) | Consumer (User) | PQ Publisher (Graph Key) |
| :-------------------------------------- | :--------------: | :----------------: | :----------------: | :-------------: | :-------------: | :----------------------: |
| Create and modify persisted query lists |         ✓        |          ✓         |                    |                 |                 |             ✓            |
| View/read persisted query lists         |         ✓        |          ✓         |          ✓         |        ✓        |                 |                          |

### Billing managers

Members with the **Billing Manager** role can't see or manage graphs in their organizations, but they can:

* Remove members from the organization
* View and edit billing information (including changing the billing plan)
* Manage organization configuration (name, avatar, etc.)

Notably, **Billing Manager**s can't invite new members to the organization or update roles.

## Graph API key roles

Each [graph API key](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys) also has a corresponding member role. This role can be any of **Graph Admin** (the default), **Contributor**, **Documenter**, **Observer**, or **Consumer**. A graph API key provides access only to its associated graph. It does not provide access to actions associated with organizations or users.

An additional role called **Persisted Query Publisher** is only available for graph API keys, not for organization members. The role is only available for API keys for graphs in Enterprise organizations. API keys with this role can run the [`rover persisted-queries publish`](https://www.apollographql.com/docs/rover/commands/persisted-queries/) command to publish operations to [persisted query lists](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries). The role provides no other read or write access to the graph.

This role is appropriate for use in client development teams' deployment processes. If your graph uses [persisted queries](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries), some client teams may need to publish their operations to your graph's persisted query lists but should not be able to view your graph's schema, changelogs, or use other **Consumer**-level features.

Otherwise, a graph API key is equivalent in privileges to a user with the same role for the graph. For example, you can use a **Consumer** key to fetch a graph's schema, and you can use a **Graph Admin** key to manage integrations.

A few operations aren't listed in the table above because they are only supported by graph API keys, not personal API keys for users in the graph's organization. These are primarily operations that are performed by your GraphQL server, such as usage reporting (traces and performance metrics).

Before January 2021, graph keys did not have roles. Keys created before that date (shown as **Legacy Admin** keys) can perform the following operations:

* Create new variants
* Run schema checks
* View and manage graph API keys
* Push schemas to a graph
* See the schemas of subgraphs in federated graphs
* View graph schemas and changelogs
* Modify schema checks configuration

## Subgraph API keys

[Subgraph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys) have a predefined role containing permissions to
run checks on subgraphs, create subgraphs, or publish updates to subgraph schemas. Subgraph keys are ideal for integration into CI/CD pipelines.

## Membership management

### Inviting members

For organizations using single sign-on (SSO), access to GraphOS is exclusively managed through your identity provider (IdP).
Any invitation links created before SSO setup will be automatically revoked and you won't be able to create new invitation links once SSO is enabled.

**Org Admin**s can invite individual members by email address from your organization's **Members** tab in [GraphOS Studio](https://studio.apollographql.com/).
Organization admins can also create a persistent **invite link** from the organization's **Settings** tab, which can be shared to invite any number of members.
Using either method, an org admin can specify which role a new member receives.

**Never share invite links publicly**. Anyone with the link can join your organization.
If an invite link becomes compromised, an admin should revoke it from the **Settings > Invite links** section.

### Removing members

Both **Org Admin**s and **Billing Manager**s can remove members from your organization's Members tab in [GraphOS Studio](https://studio.apollographql.com/).

### Updating member permissions

**Org Admin**s can update other members' roles from the **Members** tab in [GraphOS Studio](https://studio.apollographql.com/). Click the **•••** menu to the right of a member's name and select **Update Role**.

### Revoking member sessions

**Org Admin**s can revoke other members' active sessions from the **Members** tab in [GraphOS Studio](https://studio.apollographql.com/). Click the **•••** menu to the right of a member's name and select **Revoke Active Sessions**. This logs the user out of their Studio account, requiring them to log back in to regain access.

## Studio session length

By default, all GraphOS Studio user sessions are 30 days. When an individual user's session expires, they are logged out of Studio and will need to log back in.
A user's session expiration is reset whenever they log out and back into Studio.

### Change Studio session length

Org admins can adjust their organization's user session length using the [Platform API](https://www.apollographql.com/docs/graphos/platform/platform-api) or in Studio in the **Settings > Security > User session length** section.
