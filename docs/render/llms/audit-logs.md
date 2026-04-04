# Source: https://render.com/docs/audit-logs.md

# Audit Logs — Export a timeline of material actions performed by your organization.

With a Render Organization or Enterprise plan, admins can export audit logs of material events performed by team members over a specified time frame. Audit logs help you meet the requirements of various regulatory standards.

## Exporting audit logs

You can export an audit log of [workspace events](#workspace-events) for an individual workspace. With an Enterprise plan, you can also export a _separate_ audit log of [enterprise events](#enterprise-events) for your org.

### API

The [Render API](api) provides the following endpoints for audit logs:

| Action | Endpoint |
| --- | --- |
| *Export workspace events* | [List workspace audit logs](https://api-docs.render.com/reference/list-owner-audit-logs) |
| *Export organization events* | [List organization audit logs](https://api-docs.render.com/reference/list-organization-audit-logs) |

### Dashboard

Select a tab to view instructions for each type of audit log:

**Workspace events**

> Only workspace admins can export these audit logs.

1. In the [Render Dashboard](https://dashboard.render.com), navigate to your workspace's *Workspace Settings* page.
2. Scroll down to the *Compliance* section.
3. Under *Audit Logs*, select a start and end date, then click *Export as CSV*:

   [image: UI for exporting audit logs]

This audit log includes the event types listed under [Workspace events](#workspace-events).

**Enterprise events**

> Only org members with the [Enterprise Owner role](enterprise-orgs#the-enterprise-owner-role) can export these audit logs.

1. In the [Render Dashboard](https://dashboard.render.com), navigate to your Enterprise org's *Settings* page.
2. Scroll down to the *Audit Logs* section.
3. Select a start and end date, then click *Export as CSV*.

This audit log includes the event types listed under [Enterprise events](#enterprise-events).

## Availability of audit log data

- Render begins retaining audit log data for your team as soon as you upgrade to an Organization or Enterprise plan.
  - Event data from prior to upgrading is not available.
- Audit log data is available from *June 24, 2024* onward if you upgraded to an Organization or Enterprise plan before that date.
- Whenever Render adds a new audit log event type, tracking for that event begins on the date of the event's introduction.

## Audit log format

Audit logs are exported as a chronologically ordered CSV file with a separate row for each distinct event. The file includes the following columns:

------

###### Column

*timestamp*

###### Description

The UTC timestamp when the event occurred.

---

###### Column

*actor*

###### Description

The entity that performed the action. Depending on the type of actor, this value has one of two formats:

- The email address of the *existing Render user* that performed the action (e.g., `person@example.com`)
  - This is the most common actor type and format.
- The ID of the *deleted Render user* that performed the action (e.g., `Deleted User ID#123123123`)

---

###### Column

*event*

###### Description

The type of event that occurred. See below for all supported [workspace events](#workspace-events) and [enterprise events](#enterprise-events).

---

###### Column

*status*

###### Description

Indicates whether the event's associated action succeeded. One of the following values:

- `success`
- `error`

---

###### Column

*metadata*

###### Description

A JSON object containing additional details about the event. The fields of this object vary depending on the event type. For shell access events, metadata can include `service`, `instance`, `source_ip`, and `user_agent` (when available).

------

## Workspace events

The event types below appear in audit logs for individual Render workspaces.

### Member management

###### `InviteToTeamEvent`

A user was invited to the workspace.

###### `RemoveUserFromTeamEvent`

A user was removed from the workspace.

###### `AcceptTeamInviteEvent`

An invitation to join the workspace was accepted.

###### `ChangeTeamMemberRoleEvent`

A workspace member's [role](team-members#member-roles) was changed.

###### `ChangeTeamAllowedLoginMethodsEvent`

The workspace's set of allowed login methods was changed.

Currently, a workspace can either allow all Render-supported login methods or [require login via Google account](login-settings#google-account-login).

###### `ChangeTeam2FAEnforcementEvent`

[Two-factor authentication (2FA) enforcement](login-settings#two-factor-authentication) was enabled or disabled for the workspace.

###### `LoginEvent`

A workspace member logged in.

###### `LogoutEvent`

A workspace member logged out.

### Apps & services

> Render does not log events for services belonging to a [service preview](service-previews) or [preview environment](preview-environments).

###### `CreateServerEvent`

A web service, private service, background worker, or static site was created.

###### `SuspendServiceEvent`

A web service, private service, background worker, or static site was suspended.

###### `ResumeServiceEvent`

A previously suspended web service, private service, background worker, or static site was resumed.

###### `MaintenanceModeEnabledEvent`

[Maintenance mode](maintenance-mode) was toggled for a web service.

In the event's metadata, the `to` field is `true` if maintenance mode was enabled and `false` if it was disabled.

###### `MaintenanceModeURIUpdatedEvent`

The URL of a web service's [maintenance mode page](maintenance-mode#response-format) was changed.

###### `UpdateServiceNameEvent`

The name of a web service, private service, background worker, static site, or cron job was changed.

###### `DeleteServerEvent`

A web service, private service, background worker, or static site was deleted.

###### `StartShellEvent`

A service was accessed via SSH, either from the command line or from the service's *Shell* page in the Render Dashboard.

###### `EndShellEvent`

An SSH shell session for a service ended, either from the command line or from the service's *Shell* page in the Render Dashboard.

###### `ApplyBlueprintEvent`

A new [Blueprint](infrastructure-as-code) was created and applied to the workspace.

###### `CreateCronJobEvent`

A cron job was created.

###### `DeleteCronJobEvent`

A cron job was deleted.

###### `UpdateAutoDeployEvent`

[Auto-deploy](/deploys#configuring-auto-deploys) was enabled or disabled for a service.

###### `UpdateAutoDeployTriggerEvent`

The [auto-deploy trigger](/deploys#configuring-auto-deploys) settings (such as branch or path filters) were changed for a service.

###### `CreateCustomDomainEvent`

A [custom domain](custom-domains) was added to a service.

###### `DeleteCustomDomainEvent`

A [custom domain](custom-domains) was removed from a service.

### Datastores

#### General

###### `UpdateIPAllowListEvent`

The IP allow list was updated for a Render Postgres or Key Value instance.

#### Render Postgres

> These events are logged only for _primary_ Render Postgres instances, not for [high availability standby instances](postgresql-high-availability) or [read replicas](postgresql-read-replicas).

###### `CreatePostgresEvent`

A [Render Postgres](postgresql) database was created.

###### `DeletePostgresEvent`

A [Render Postgres](postgresql) database was deleted.

###### `SuspendPostgresEvent`

A [Render Postgres](postgresql) database was suspended.

###### `ResumePostgresEvent`

A previously suspended [Render Postgres](postgresql) database was resumed.

###### `DownloadDatabaseBackupEvent`

A [logical backup](postgresql-backups#logical-backups) of a [Render Postgres](postgresql) database was downloaded.

###### `ViewConnectionInfoEvent`

The connection URL or password for a [Render Postgres](postgresql) database was viewed.

#### Render Key Value

###### `CreateRedisEvent`

A [Render Key Value](key-value) instance was created.

###### `DeleteRedisEvent`

A [Render Key Value](key-value) instance was deleted.

###### `ViewConnectionInfoEvent`

The connection URL or password for a [Render Key Value](key-value) instance was viewed.

#### Persistent disks

###### `CreateServerDiskEvent`

The [persistent disk](disks) for a web service, private service, or background worker was created.

###### `DeleteServerDiskEvent`

The [persistent disk](disks) for a web service, private service, or background worker was deleted.

###### `RestoreDiskSnapshotEvent`

The [persistent disk](disks) for a web service, private service, or background worker was restored to a [snapshot](disks#disk-snapshots).

### Environment variables

###### `UpdateEnvVarsEvent`

One or more existing [environment variables](configure-environment-variables) were modified for a service.

###### `CreateEnvVarsEvent`

One or more [environment variables](configure-environment-variables) were created for a service.

###### `DeleteEnvVarsEvent`

One or more [environment variables](configure-environment-variables) were deleted for a service.

###### `ViewEnvVarValuesEvent`

One or more [environment variable](configure-environment-variables) values were viewed for a service.

###### `DeleteEnvGroupEvent`

An [environment group](configure-environment-variables#environment-groups) was deleted.

### Webhooks

###### `CreateWebhookEvent`

A [webhook](webhooks) was created.

###### `UpdateWebhookEvent`

A [webhook](webhooks) was changed.

###### `DeleteWebhookEvent`

A [webhook](webhooks) was deleted.

### Metrics

###### `CreateOtelIntegrationEvent`

A [metrics stream](metrics-streams) was created.

###### `DeleteOtelIntegrationEvent`

A [metrics stream](metrics-streams) was deleted.

###### `UpdateOtelIntegrationEvent`

A [metrics stream](metrics-streams) was changed.

### Projects & environments

###### `CreateProjectEvent`

A project was created.

This event is always accompanied by one [`CreateEnvironmentEvent`](#createenvironmentevent) event, because every project is created with a default environment.

###### `DeleteProjectEvent`

A project was deleted.

This event is always accompanied by at least one [`DeleteEnvironmentEvent`](#deleteenvironmentevent) event, because deleting a project also deletes all of its associated environments.

###### `CreateEnvironmentEvent`

A project environment was created.

###### `DeleteEnvironmentEvent`

A project environment was deleted.

###### `MoveEnvironmentResourceEvent`

A resource (such as a service or environment group) was moved into or out of a project environment.

###### `ChangeEnvironmentProtectionEvent`

[Protected access](projects#protected-environments) was enabled or disabled for a project environment.

###### `UpdateEnvironmentIsolatedEvent`

The [isolation setting](projects#blocking-cross-environment-traffic) was changed for a project environment.

### Compliance & documents

###### `DocumentDownloadEvent`

A workspace member downloaded a document from the [Render Document Center](certifications-compliance#view-compliance-documentation).

###### `SignNDAEvent`

A workspace member signed an NDA to view compliance documentation.

## Enterprise events

*The event types below are specific to [Enterprise orgs](enterprise-orgs).* They pertain to SSO and other org-level configuration.

These events appear _only_ in audit logs exported from your org's *Settings* page (not in audit logs exported for an individual workspace).

### Member management

###### `InviteToOrgEvent`

A user was invited to the org.

###### `AcceptOrgInviteEvent`

An invitation to join the org was accepted.

###### `AddOrgMemberEvent`

A user was added to the org.

###### `RemoveOrgMemberEvent`

A user was removed from the org.

###### `JoinTeamEvent`

An org member added themselves to a workspace in the org.

Enterprise Owners can add themselves to any workspace as an admin. Other org members can add themselves to [public workspaces](enterprise-orgs#per-workspace-access) only (they receive the Developer role).

###### `ChangeOrgRoleEvent`

An org member's role was changed.

This refers to a member's org-level role (such as [Enterprise Owner](enterprise-orgs#the-enterprise-owner-role)), not their role within a particular workspace.

###### `ChangeOrgAllowedLoginMethodsEvent`

The org's set of allowed login methods was changed.

###### `ChangeOrg2FAEnforcementEvent`

Two-factor authentication enforcement was enabled or disabled for the org.

### Workspace management

###### `CreateWorkspaceEvent`

A workspace was created in the org.

###### `DeleteWorkspaceEvent`

A workspace in the org was deleted.

###### `ChangeWorkspacePrivacyEvent`

The [access setting](enterprise-orgs#per-workspace-access) for a workspace in the org was changed.

### IdP management

###### `CreateOrgDomainEvent`

A domain was added to the org as part of [configuring SSO](saml-sso#sso-setup).

###### `VerifyOrgDomainEvent`

Ownership of a domain was verified as part of [configuring SSO](saml-sso#sso-setup).

###### `DeleteOrgDomainEvent`

A domain was removed from the org.

###### `CreateSSOConnectionEvent`

An [SSO connection](saml-sso) was created.

###### `UpdateSSOConnectionEvent`

An [SSO connection](saml-sso) was changed.

###### `DeleteSSOConnectionEvent`

An [SSO connection](saml-sso) was deleted.

###### `ProvisionOrganizationSCIMToken`

A [SCIM token](saml-sso#member-management-setup-scim) was provisioned for the org.

###### `RevokeOrganizationSCIMToken`

A [SCIM token](saml-sso#member-management-setup-scim) was revoked for the org.

## History of audit log event changes

------

###### Date

`2026-02-19`

###### Change

Added the following workspace event type:

- [`EndShellEvent`](#endshellevent)

Also added `source_ip` and `user_agent` metadata for audit events when available.

---

###### Date

`2025-01-20`

###### Change

Added the following workspace event types:

- [`UpdateAutoDeployEvent`](#updateautodeployevent)
- [`UpdateAutoDeployTriggerEvent`](#updateautodeploytriggerevent)
- [`CreateCustomDomainEvent`](#createcustomdomainevent)
- [`DeleteCustomDomainEvent`](#deletecustomdomainevent)
- [`UpdateEnvironmentIsolatedEvent`](#updateenvironmentisolatedevent)

---

###### Date

`2025-03-13`

###### Change

Added initial set of [enterprise events](#enterprise-events).

---

###### Date

`2025-03-11`

###### Change

Added the following workspace event types:

- [`CreateOtelIntegrationEvent`](#createotelintegrationevent)
- [`DeleteOtelIntegrationEvent`](#deleteotelintegrationevent)
- [`UpdateOtelIntegrationEvent`](#updateotelintegrationevent)
- [`CreateWebhookEvent`](#createwebhookevent)
- [`UpdateWebhookEvent`](#updatewebhookevent)
- [`DeleteWebhookEvent`](#deletewebhookevent)

---

###### Date

`2024-12-18`

###### Change

Added the following workspace event types:

- [`DocumentDownloadEvent`](#documentdownloadevent)
- [`SignNDAEvent`](#signndaevent)

---

###### Date

`2024-09-24`

###### Change

Added the following workspace event types:

- [`MaintenanceModeEnabledEvent`](#maintenancemodeenabledevent)
- [`MaintenanceModeURIUpdatedEvent`](#maintenancemodeuriupdatedevent)

---

###### Date

`2024-08-14`

###### Change

Added the following workspace event types:

- [`ViewEnvVarValuesEvent`](#viewenvvarvaluesevent)
- [`ViewConnectionInfoEvent`](#viewconnectioninfoevent) (Render Postgres)
- [`ViewConnectionInfoEvent`](#viewconnectioninfoevent-1) (Render Key Value)

---

###### Date

`2024-06-24`

###### Change

Added initial set of [Workspace events](#workspace-events).

------
