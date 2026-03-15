# Source: https://docs.firehydrant.com/docs/role-based-access-controls.md

# Role-Based Access Controls (RBAC)

<Image align="center" border={false} caption="User roles in FireHydrant" src="https://files.readme.io/68520e9239b203523226a04239c095a2d615522e875079a04b9d447816ec512e-image.png" width="650px" />

FireHydrant offers user roles to help restrict and define access to parts of the platform, enabling you to create a secure and scalable incident management process.

## Users, Roles, and Definitions

### Licensed vs. Unlicensed users

* **Licensed users** - Users with FireHydrant accounts and login access, split into 4 access roles (see next section)
* **Unlicensed users** - Everyone else. Users who cannot log in and perform the vast majority of actions with one exception.

Any user in Slack or Microsoft Teams, including unlicensed, can still join incident channels/chats, keep tabs on an open incident, and participate in conversations within those channels. However, unlicensed users can't take any actions that change the incident state, such as running most commands, posting updates, assigning/completing tasks, being assigned roles, etc.

Depending on your settings, Unlicensed users can perform a set of basic essential tasks from integrated chat applications like Slack or MS Teams:

* **Declare incidents** (can be configured in Integration settings)
* **Page and Lookup On-Call** (Slack only)
* ...and more

For full details, visit the command docs pages for <Anchor label="Slack" target="_blank" href="doc:slack-integration">Slack</Anchor> and <Anchor label="Microsoft Teams" target="_blank" href="doc:microsoft-teams-integration">Microsoft Teams</Anchor>.

### Access Roles vs. Incident Roles

**Access roles** (this page) are for determining user access to different features and capabilities on the FireHydrant platform. These should not be confused with <Anchor label="Incident Roles" target="_blank" href="doc:incident-roles">Incident Roles</Anchor>, which are titles provided to specific users on incidents and can change what tasks are assigned to them and impact other automations in Runbooks.

### Organization vs. Team-Level Permissions

FireHydrant allows you to customize permissions both at an organization level (access roles) as well as within a team (called **Team-Level Permissions**). Certain permissions at the organization level will override team-level permissions (e.g., access roles with **Manage Teams** permission can manage and modify members and settings on any of the teams), but within a team, users can be given permissions to modify team-only items like schedules, policies, team membership, and more.

**Access Roles**, custom or out-of-box, are defined at the organization level. For more information about team-level permissions, see <Anchor label="Team-Level Permissions" target="_blank" href="#team-level-permissions">Team-Level Permissions</Anchor> below.

## Predefined Access Roles

FireHydrant offers four access roles out-of-box. Any modifications or other desired behaviors should be done via <Anchor label="Custom Access Roles" target="_blank" href="#custom-access-roles">Custom Access Roles</Anchor>.

* **Owner**: Full access to the full platform, including user administration, integrations, API Keys, and other organization settings
* **Member**: Full access to update incident management processes, Runbooks, Settings, Teams, and Alert configurations
* **Collaborator**: Basic incident response access but cannot update settings or Runbooks. Same as Viewer for creating and responding to alerts if assigned
* **Viewer**: Read-only access to incidents and analytics in the FireHydrant web app. Ability to create and respond to alerts if they're assigned
* **Unlicensed**: Not a custom access role, but included to visually demonstrate what people without FireHydrant accounts can do.

### Alerts & On-Call Permissions

Note that users may have Viewer role permissions but can still be on-call and respond to pages.

| Action                                                                                                                                                                                                                                                                                                                                                     | Owner | Member | Collaborator | Viewer |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---- | :----- | :----------- | :----- |
| Create <Anchor label="Alerts" target="_blank" href="doc:signals-alert-rules">Alerts</Anchor> and Page Others                                                                                                                                                                                                                                               | ✅     | ✅      | ✅            | ✅      |
| <Anchor label="Request Coverage for Shifts" target="_blank" href="https://docs.firehydrant.com/docs/signals-on-call-schedules#requesting-coverage-for-a-shift">Request Coverage for Shifts</Anchor>, <Anchor label="Claim Shifts" target="_blank" href="https://docs.firehydrant.com/docs/signals-on-call-schedules#claiming-shifts">Claim Shifts</Anchor> | ✅     | ✅      | ✅            | ✅      |
| <Anchor label="Respond" target="_blank" href="doc:signals-introduction">Respond</Anchor> to Alerts^                                                                                                                                                                                                                                                        | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Alerts" target="_blank" href="doc:signals-alert-rules">Alerts</Anchor>                                                                                                                                                                                                                                                                 | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Alert Grouping" target="_blank" href="doc:alert-grouping">Alert Grouping</Anchor>                                                                                                                                                                                                                                                      | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Alert Rules/Triggers" target="_blank" href="doc:signals-alert-rules">Alert Rules/Triggers</Anchor>                                                                                                                                                                                                                                     | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Call Routes" target="_blank" href="doc:live-call-routing">Call Routes</Anchor>                                                                                                                                                                                                                                                         | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Escalation Policies" target="_blank" href="doc:signals-escalation-policies">Escalation Policies</Anchor>                                                                                                                                                                                                                               | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Event Sources" target="_blank" href="doc:signals-integrations">Event Sources</Anchor>                                                                                                                                                                                                                                                  | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="On-Call Schedules & Shifts" target="_blank" href="doc:signals-on-call-schedules">On-Call Schedules & Shifts</Anchor>                                                                                                                                                                                                                   | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Team Support Hours" target="_blank" href="doc:team-support-hours">Team Support Hours</Anchor>                                                                                                                                                                                                                                          | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Webhook Alert Targets" target="_blank" href="doc:signals-webhook-alert-targets">Webhook Alert Targets</Anchor>                                                                                                                                                                                                                         | ✅     | ✅      | ✅            | ✅      |
| Manage <Anchor label="Personal Notification Preferences" target="_blank" href="doc:signals-notification-preferences">Personal Notification Preferences</Anchor>                                                                                                                                                                                            | ✅     | ✅      | ✅            | ✅      |
| Manage <Anchor label="On-Call Shifts/Shift Overrides" target="_blank" href="doc:signals-on-call-schedules">On-Call Shifts/Shift Overrides</Anchor>                                                                                                                                                                                                         | ✅     | ✅      | ✅            |        |
| Manage <Anchor label="Alert Grouping" target="_blank" href="doc:alert-grouping">Alert Grouping</Anchor>                                                                                                                                                                                                                                                    | ✅     | ✅      |              |        |
| Manage <Anchor label="Alert Rules/Triggers" target="_blank" href="doc:signals-alert-rules">Alert Rules/Triggers</Anchor>                                                                                                                                                                                                                                   | ✅     | ✅      |              |        |
| Manage <Anchor label="Call Routes" target="_blank" href="doc:live-call-routing">Call Routes</Anchor>                                                                                                                                                                                                                                                       | ✅     | ✅      |              |        |
| Manage <Anchor label="Escalation Policies" target="_blank" href="doc:signals-escalation-policies">Escalation Policies</Anchor>                                                                                                                                                                                                                             | ✅     | ✅      |              |        |
| Manage <Anchor label="Event Sources" target="_blank" href="doc:signals-integrations">Event Sources</Anchor>                                                                                                                                                                                                                                                | ✅     | ✅      |              |        |
| Manage <Anchor label="On-Call Schedules" target="_blank" href="doc:signals-on-call-schedules">On-Call Schedules</Anchor>                                                                                                                                                                                                                                   | ✅     | ✅      |              |        |
| Manage <Anchor label="Team Support Hours" target="_blank" href="doc:team-support-hours">Team Support Hours</Anchor>                                                                                                                                                                                                                                        | ✅     | ✅      |              |        |
| Manage <Anchor label="Webhook Alert Targets" target="_blank" href="doc:signals-webhook-alert-targets">Webhook Alert Targets</Anchor>                                                                                                                                                                                                                       | ✅     | ✅      |              |        |
| Read [Global Notification Policy Compliance](https://docs.firehydrant.com/docs/global-notification-policy)                                                                                                                                                                                                                                                                               | ✅     |        |              |        |
| Manage <Anchor label="Global Notification Policy" target="_blank" href="doc:global-notification-policy">Global Notification Policy</Anchor>                                                                                                                                                                                                                | ✅     |        |              |        |

<Callout icon="📘" theme="info">
  ^**Note**:

  Users will always be able to interact with alerts that are targeted at them, even if they don't have explicit "Respond to Alerts" permission.
</Callout>

### Analytics Permissions

| Action                                                                                        | Owner | Member | Collaborator | Viewer |
| :-------------------------------------------------------------------------------------------- | :---- | :----- | :----------- | :----- |
| Read <Anchor label="Analytics" target="_blank" href="doc:analytics-basics">Analytics</Anchor> | ✅     | ✅      | ✅            | ✅      |

### Incident Management Permissions

| Action                                                                                                                                                                                                                                                                                                                                  | Owner | Member | Collaborator | Viewer |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---- | :----- | :----------- | :----- |
| <Anchor label="Create Incidents" target="_blank" href="doc:starting-incidents">Create Incidents</Anchor> (manually or from alerts)                                                                                                                                                                                                      | ✅     | ✅      | ✅            | ✅      |
| <Anchor label="Invited" target="_blank" href="doc:runbook-step-invite-to-slack-incident-channel">Invited</Anchor> to Slack incident channels                                                                                                                                                                                            | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Incidents" target="_blank" href="doc:the-command-center">Incidents</Anchor> (including via Tabs in MS Teams)                                                                                                                                                                                                        | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Incident Settings" target="_blank" href="doc:incident-fields">Incident Settings</Anchor>                                                                                                                                                                                                                            | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Status Templates" target="_blank" href="doc:status-templates">Status Templates</Anchor>                                                                                                                                                                                                                             | ✅     | ✅      | ✅            | ✅      |
| Run <Anchor label="General Slack Commands" target="_blank" href="doc:slack-commands">General Slack Commands</Anchor>                                                                                                                                                                                                                    | ✅     | ✅      | ✅            | ✅      |
| View [Internal](https://docs.firehydrant.com/docs/internal-status-pages) and [External](https://docs.firehydrant.com/docs/external-status-pages) Status Pages                                                                                                                                                                                                                                       | ✅     | ✅      | ✅            | ✅      |
| **Respond to Incidents**                                                                                                                                                                                                                                                                                                                |       |        |              |        |
| ↳ Assigned <Anchor label="Incident Roles" target="_blank" href="doc:incident-roles">Incident Roles</Anchor>                                                                                                                                                                                                                             | ✅     | ✅      | ✅            |        |
| ↳ Assigned <Anchor label="Tasks" target="_blank" href="doc:managing-tasks">Tasks</Anchor> and Follow-Ups                                                                                                                                                                                                                                | ✅     | ✅      | ✅            |        |
| ↳ Attach/Execute <Anchor label="Runbooks" target="_blank" href="doc:intro-to-runbooks">Runbooks</Anchor>                                                                                                                                                                                                                                | ✅     | ✅      | ✅            |        |
| ↳ Manage Incidents in the <Anchor label="web application" target="_blank" href="doc:the-command-center">web application</Anchor>, <Anchor label="Slack" target="_blank" href="doc:slack-integration">Slack</Anchor>, or <Anchor label="Microsoft Teams" target="_blank" href="doc:microsoft-teams-integration">Microsoft Teams</Anchor> | ✅     | ✅      | ✅            |        |
| ↳ Manage and Edit <Anchor label="External Status Page" target="_blank" href="doc:external-status-pages">External Status Page</Anchor> Updates                                                                                                                                                                                           | ✅     | ✅      | ✅            |        |
| ↳ Participate in <Anchor label="Retrospectives" target="_blank" href="doc:incident-followup">Retrospectives</Anchor>                                                                                                                                                                                                                    | ✅     | ✅      | ✅            |        |
| ↳ Post <Anchor label="Incident Updates" target="_blank" href="doc:posting-updates">Incident Updates</Anchor> (not including to external status pages)                                                                                                                                                                                   | ✅     | ✅      | ✅            |        |
| ↳ Run most <Anchor label="Slack Commands" target="_blank" href="doc:slack-commands">Slack Commands</Anchor> or <Anchor label="Microsoft Teams Commands" target="_blank" href="doc:microsoft-teams-commands">Microsoft Teams Commands</Anchor>, with some exceptions (see the docs)                                                      | ✅     | ✅      | ✅            |        |
| ↳ Star Events or Other <Anchor label="Incident Timeline" target="_blank" href="doc:incident-timeline">Incident Timeline</Anchor> Actions                                                                                                                                                                                                | ✅     | ✅      | ✅            |        |
| Manage <Anchor label="Incident Settings" target="_blank" href="doc:incident-fields">Incident Settings</Anchor>                                                                                                                                                                                                                          | ✅     | ✅      |              |        |
| Read <Anchor label="Private Incidents" target="_blank" href="doc:private-incidents">Private Incidents</Anchor>\*\*                                                                                                                                                                                                                      | ✅     |        |              |        |
| Manage <Anchor label="Status Templates" target="_blank" href="doc:status-templates">Status Templates</Anchor>                                                                                                                                                                                                                           | ✅     |        |              |        |

<Callout icon="📘" theme="info">
  \*\***Note**:

  Users without private incident access (all-encompassing) can be added to individual private incidents ad-hoc by people who have access. This permission only allows viewing/accessing Private Incidents - in order to respond to Private Incidents, you will also need the `Manage Incidents` permissions above.

  For more information, see [Private Incidents](https://docs.firehydrant.com/docs/private-incidents).
</Callout>

### Integration Management Permissions

| Action                                                                                                     | Owner | Member | Collaborator | Viewer |
| :--------------------------------------------------------------------------------------------------------- | :---- | :----- | :----------- | :----- |
| Read <Anchor label="Integrations" target="_blank" href="doc:integrations-overview">Integrations</Anchor>   | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Webhooks" target="_blank" href="doc:webhooks">Webhooks</Anchor>                        | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Secrets" target="_blank" href="doc:secrets">Secrets</Anchor>                           | ✅     |        |              |        |
| Manage <Anchor label="Integrations" target="_blank" href="doc:integrations-overview">Integrations</Anchor> | ✅     |        |              |        |
| Manage <Anchor label="Secrets" target="_blank" href="doc:secrets">Secrets</Anchor>                         | ✅     |        |              |        |
| Manage <Anchor label="Webhooks" target="_blank" href="doc:webhooks">Webhooks</Anchor>                      | ✅     |        |              |        |

### Resource Management Permissions

| Action                                                                                                                        | Owner | Member | Collaborator | Viewer |
| :---------------------------------------------------------------------------------------------------------------------------- | :---- | :----- | :----------- | :----- |
| Read <Anchor label="Audiences" target="_blank" href="doc:ai-powered-incident-summaries">Audiences</Anchor>                    | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Change Events" target="_blank" href="doc:change-events">Change Events</Anchor>                            | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Organization Settings" target="_blank" href="doc:miscellaneous-settings">Organization Settings</Anchor>   | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Runbooks" target="_blank" href="doc:intro-to-runbooks">Runbooks</Anchor>                                  | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Service Catalog" target="_blank" href="doc:intro-to-service-catalog">Service Catalog</Anchor>             | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Teams" target="_blank" href="doc:team-management">Teams</Anchor>                                          | ✅     | ✅      | ✅            | ✅      |
| Manage <Anchor label="Audiences" target="_blank" href="doc:ai-powered-incident-summaries">Audiences</Anchor>                  | ✅     | ✅      |              |        |
| Manage <Anchor label="Change Events" target="_blank" href="doc:change-events">Change Events</Anchor>                          | ✅     | ✅      |              |        |
| Manage <Anchor label="Runbooks" target="_blank" href="doc:intro-to-runbooks">Runbooks</Anchor>                                | ✅     | ✅      |              |        |
| Manage <Anchor label="Service Catalog" target="_blank" href="doc:intro-to-service-catalog">Service Catalog</Anchor>           | ✅     | ✅      |              |        |
| Manage <Anchor label="Teams" target="_blank" href="doc:team-management">Teams</Anchor>                                        | ✅     | ✅      |              |        |
| Manage <Anchor label="Organization Settings" target="_blank" href="doc:miscellaneous-settings">Organization Settings</Anchor> | ✅     |        |              |        |
| Read <Anchor label="Audit Logs" target="_blank" href="doc:audit-logs">Audit Logs</Anchor>                                     | ✅     |        |              |        |

### User Access Control Permissions

| Action                                                                                     | Owner | Member | Collaborator | Viewer |
| :----------------------------------------------------------------------------------------- | :---- | :----- | :----------- | :----- |
| Read Roles & Permissions                                                                   | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="Users" target="_blank" href="doc:user-administration">Users</Anchor>   | ✅     | ✅      | ✅            | ✅      |
| Read <Anchor label="API Keys" target="_blank" href="doc:api-keys">API Keys</Anchor>        | ✅     |        |              |        |
| Manage <Anchor label="API Keys" target="_blank" href="doc:api-keys">API Keys</Anchor>      | ✅     |        |              |        |
| Manage Roles & Permissions                                                                 | ✅     |        |              |        |
| Manage <Anchor label="Users" target="_blank" href="doc:user-administration">Users</Anchor> | ✅     |        |              |        |

## Custom Access Roles

Any <Glossary>Owner</Glossary> or access role with `Manage Roles & Permissions` can navigate to the Roles & Permissions page and create/make changes to custom access roles.

In addition, any <Glossary>Owner</Glossary> or access role with `Manage Users` permission can navigate to the Users page and update another user's access role. The exception to this is that users cannot update their own roles if they're not Owners - they must request another user with adequate permissions to modify their assigned access role.

Additionally, you can update user roles using our SCIM API and your IDP (Okta, Active Directory, etc.). Read our [SCIM Configuration](https://docs.firehydrant.com/docs/scim-configuration) docs to learn about provisioning users and roles.

### Creating a Custom Role

<Image align="center" border={false} caption="Adding a custom access role" src="https://files.readme.io/2e2beea447fd5341bb9bf5e5c0c6dc810f961bf7fc287b7eeccdf321d947b578-image.png" width="650px" />

1. Navigate to **Settings > Roles & Permissions** and then click on "+ Add role."
2. On this next page, supply a **Name** and **Description** for this custom role you're creating.
3. Below on the same page, you can select the permissions you would like this particular role to have. The full list of selectable permissions can be browsed below.
   1. **NOTE**: Certain permissions will require and automatically check other prerequisite permissions/dependencies. For example, to fully read incidents, the user must also have read access to several other objects like teams and alerts. You'll receive a popup notification stating what additional permissions will be checked, if any.
4. Once configured, click "Create role" at the top right.
5. Remember to go to **Settings > Users** and assign your new custom role to one or more users in order to set and customize their permissions.

On the role creation page, you also have some utility buttons:

1. **Deselect all** will uncheck all boxes
2. **Select all** will check all boxes
3. **Reset** will revert the selections back to their last saved state. If editing a role, it reverts permissions to their prior state, and if creating a new role, it does the same thing as Clear.

## Team-Level Permissions

<Image align="center" border={false} caption="Managing individual team members' permissions" src="https://files.readme.io/7643eec90688a762742608da14852231faa222672789ea41788c882e15ce8203-image.png" width="650px" />

In addition to organization-level access roles, teams can lock down configurations for their teams. This will federate permissions for each team member to modify specific resources within the team, even if they don't have permissions broadly across the org to do the same (e.g., they can manage Users within the team, but they cannot broadly manage Users in the organization).

These permissions can be found by clicking on the ellipses next to each member in the members list.

<Image align="center" border={false} caption="Team-level permissions" src="https://files.readme.io/52f9f2ba0723fb5428c84b80f270d1963ebae7a8fc08ffe8aa40d4fe97ec936e-image.png" width="400px" />

[Runbooks](https://docs.firehydrant.com/docs/intro-to-runbooks) and [Service Catalog ](https://docs.firehydrant.com/docs/service-catalog-basics) components can have assigned **Owning Teams**, which prevents non-team members from modifying or managing those resources once assigned. Team-level permissions, in these cases, will take precedence over org-level permissions.

For example, let's say Service A is owned by Team A, User X is part of the team, and User X doesn't have **Manage Service** permissions within the team. At this point, it doesn't matter if the user's assigned organization role has Manage Service permissions - they will not be able to edit Service A. See the following graphic for a visual representation:

<Image align="center" border={false} caption="Flowchart of permissions precedence" src="https://files.readme.io/63d9cf0d8e3daa11274aa2000a1ea043b35d6a939c25bf46bf8573fc97477510-image.png" width="650px" />

For Signals-specific features (Alert Rules, Schedules, Policies, etc.), see the next subsection.

<Callout icon="📘" theme="info">
  **Note**:

  Team-level permissions override org-level permissions, with only one exception. In other words:

  * If Service A or Runbook A are owned by Team A, then nobody outside of Team A can modify that service or runbook even if they have `Manage Service Catalog` or `Manage Runbooks` permissions assigned to their org-level role.
  * If Team A has chosen to lock down its Signals settings, then even users with `Manage Escalation Policies` permission at the organization level cannot edit Team A's escalation policies.

  The exception to this is for users with <Glossary>Owner</Glossary> access role. **Owners** can be thought of as superadmins with access to everything.
</Callout>

### Signals-Specific Feature Permissions

<Image align="center" border={false} caption="Restricting the modification of a team's Signals configurations to only within the team" src="https://files.readme.io/65728768059d36781d0c4a5ec3a97e3cec86fde09c9078814441db337272530b-image.png" width="400px" />

To maintain existing behavior for customers, FireHydrant has not automatically locked down permissions for Signals configurations by team to prevent a sudden loss of editing permissions from existing users.

To enable the behavior, go into a Team's settings and enable this switch for **Enable Team-Only Signals Resource Management**. As soon as this setting is enabled, only users who are explicitly on the membership list of this team will be allowed to modify any Signals-related config on the team (e.g., Schedules, Policies, etc.), and only if they have the team-level permission required to do so.

## Frequently asked questions

> **I want to make sure users can only modify their own team's settings. How do I achieve this?**

1. First, ensure that a user does not have <Glossary>Owner</Glossary> permissions, as **Owners** can modify all configurations on any team.
2. Users assigned `Manage Teams` permissions at the organization level can modify Team details, settings, and memberships across all teams. If you don't want this, make sure that a user only has `Read Teams` permission.
3. Then, make sure that the individuals on the team have the team-level permissions enabled for anything you want them to be able to manage.

This flow is useful for configuring e.g., **Team Leads**, who can manage their own teams but not other teams.

> **Can an unlicensed user access incident retrospectives?**

FireHydrant's incidents and retrospectives are a part of the web application and require a license to access. Retrospectives can be exported as PDF or supported integrations like Confluence and Google Docs to be shared broadly.

For more information, visit [Preview & Export Retrospectives](https://docs.firehydrant.com/docs/preview-export-retrospectives).

> **Can a Viewer or non-licensed user “star” events to be included in the export timeline?**

Starring events is considered a state-altering action, and subsequently is not available for the default Viewer role or anyone without `Manage Incidents` permission.

> **If a Viewer or unlicensed user posts chat messages into the incident Slack or Microsoft Teams channel, will those still be recorded by FireHydrant into the timeline**

Yes, all messages in incident channels are recorded in the incident timeline regardless of who they're from.

> **Can a Viewer or non-licensed user be assigned action-items?**

Users must at least have `Manage Incidents` permissions or be Collaborator+ (of the out-of-box roles).

> **Can a non-licensed user view a status page?**

Yes. You do not need to be a licensed user on FireHydrant to view a status page.