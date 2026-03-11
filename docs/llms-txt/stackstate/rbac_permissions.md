# Source: https://archivedocs.stackstate.com/5.1/configure/security/rbac/rbac_permissions.md

# Source: https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/rbac_permissions.md

# Permissions

## Overview

Permissions in StackState allow Administrators to manage the actions that each user or user group can perform inside StackState and the information that will be shown in their StackState UI. Only the feature set relevant to each user's active role will be presented. The actions, information and pages that a user doesn't have access to are simply not displayed in their StackState UI.

{% hint style="info" %}
Permissions are stored in StackGraph. This means that:

* If you perform an upgrade with "clear all data", permission setup will also be removed.
* To completely remove a user, they must also be manually removed from StackGraph.
  {% endhint %}

## StackState permissions

There are two types of permission in StackState. **System permissions** scope user capabilities, such as access to settings, query execution and scripting. **View permissions** allow for CRUD operations on StackState Views, these can be granted for a specific view or for all views. For details of the permissions attached to each predefined role in StackState, see [predefined roles](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac_roles#predefined-roles)

The following permissions are available in StackState:

* `access-admin-api` -Access the administrator API.
* `access-analytics` - Access the [Analytics](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/analytics.md) page in the StackState UI.
* `access-cli` - Access the CLI page. This provides the API key to use for authentication with the StackState CLI.
* `access-explore` - Access the [Explore](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/explore_mode.md) page in the StackState UI.
* `access-log-data` - Access StackState logs using the CLI.
* `access-synchronization-data` - Access StackState synchronization status and data using the CLI.
* `access-topic-data` - Access StackState Receiver data using the CLI.
* `access-view` - A **View permission**. Access a specific view (when granted on a view) or all views (when granted on `everything`). Granted on the following views for predefined StackState roles:
  * Administrator: `everything` (all views)
  * Platform Administrator: `everything` (all views)
  * Power User: `everything` (all views)
  * Guest: `everything` (all views)
* `create-views` - [Create views](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/views/create_edit_views.md) in the StackState UI.
* `delete-view` - A **view permission**. Delete a specific view (when granted on a view) or all views (when granted on `everything`). Granted on the following views for predefined StackState roles:
  * Administrator: `everything` (all views)
  * Platform Administrator: -
  * Power User: `everything` (all views)
  * Guest: -
* `execute-component-actions` - Execute [component actions](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/perspectives/topology-perspective.md#actions).
* `execute-component-templates` - Invoke a component template API extension (internal use only).
* `execute-node-sync` - Reset or delete a synchronization.
* `execute-restricted-scripts` - Execute scripts using the [HTTP script API](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/develop/reference/scripting/script-apis/http.md) in the StackState UI analytics environment. Also requires `execute-scripts`.
* `execute-scripts` - Execute a query in the StackState UI Analytics environment. The `execute-restricted-scripts` permission is also required to execute scripts using the HTTP script API.
* `export-settings` - Export settings.
* `import-settings` - Import settings.
* `manage-annotations` - Persist and fetch Anomaly annotations in StackState.
* `manage-ingestion-api-keys` - Manage [API keys](https://archivedocs.stackstate.com/security/k8s-ingestion-api-keys) for data ingestion.
* `manage-metric-bindings` - Create, delete and change [metric bindings](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts)
* `manage-monitors` - Create, delete and change [monitors](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/alerting/monitors.md).
* `manage-notifications` - Create, delete, and modify [notifications](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/configure).
* `manage-service-tokens`- Create/delete [Service Tokens](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/security/security/authentication/service_tokens.md) in StackState.
* `manage-stackpacks` - Install/upgrade/uninstall StackPacks.
* `manage-star-view` - Add and remove [stars](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/views/about_views.md#starred-views) from views in the StackState UI.
* `manage-telemetry-streams` - [Create or edit new telemetry streams](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/metrics/add-telemetry-to-element.md) for components in the StackState UI.
* `manage-topology-elements` - Create/update/delete topology elements.
* `perform-custom-query` - Access the [topology filter](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/filters.md#filter-topology).
* `read-agents` - List connected agents with the cli `agent list` command
* `read-permissions` - List all granted permissions across the entire system using the CLI.
* `read-settings` - Access the Settings page in the StackState UI.
* `read-stackpacks`
* `read-system-notifications` - Access the system notifications in the UI
* `read-telemetry-streams` - Access the telemetry data for components in the StackState UI
* `read-traces` - Read and access trace data.
* `run-monitors` - Execute a [monitor](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/alerting/monitors.md) and make it run periodically.
* `save-view`- A **view permission**. Update a specific view (when granted on a view) or all views (when granted on `everything`). Granted on the following views for predefined StackState roles:
  * Administrator: `everything` (all views)
  * Platform Administrator: -
  * Power User: `everything` (all views)
  * Guest: -
* `unlock-node` - Unlock [locked configuration items](https://archivedocs.stackstate.com/configure-stackstate/about-stackpacks#locked-configuration-items).
* `update-permissions` - Grant/revoke permissions or change subjects.
* `update-settings` - Update settings.
* `update-visualization` - Change [visualization settings](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/views/visualization_settings.md).
* `upload-stackpacks` - Upload new (versions of) StackPacks.
* `view-metric-bindings` - View [metric bindings](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts) (via the cli)
* `view-monitors` - View monitor configurations.
* `view-notifications` - View notification settings.

## Manage permissions

StackState permissions can be managed using the `sts` CLI.

{% hint style="info" %}
**Important note:** All permissions in StackState are case sensitive.
{% endhint %}

### List all permissions

List all permissions:

```
sts rbac list-permissions
```

### Show granted permissions

Show the permissions granted to a specific role.

```
sts rbac describe-permissions --subject [role-name]
```

### Grant permissions

#### Allow a user to open a view

Give a subject with permission to open a view:

```
sts rbac grant --subject [role-name] --permission access-view --resource [view-name]
```

#### Allow a user to create (save) views

Give a subject with the system permission to create (save) views:

```
sts rbac grant --subject [role-name] --permission create-views
```

#### Allow a user to check StackState settings

Give a subject with the system permission to check StackState settings:

```
sts rbac grant --subject [role-name] --permission read-settings
```

#### Allow a user to add or edit event handlers

Give a subject with the system permission to add new event handlers and edit existing event handlers:

```
sts rbac grant --subject [role-name] --permission manage-event-handlers
```

### Revoke permissions

Revoke permissions for a subject to open a view:

```
sts rbac revoke --subject [role-name] --permission access-view --resource [view-name]
```

## StackState UI with no permissions

Below is an example of how the StackState UI would look for a user without any permissions:

![No permissions](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-1fe95c249c8bf297b41cf0e698923220adb17929%2Fnoperm.png?alt=media)
