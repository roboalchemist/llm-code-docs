# Source: https://developers.make.com/api-documentation/authentication/api-scopes-overview.md

# Make roles and API scopes

Accessibility of Make API endpoints differs depending on the Make platform you use. On Make and our hosted cloud version, regular users cannot access the administration interface. Administration API resources are meant only for internal Make administrators.

In the on-premise version, any user with a platform administration role assigned can access the administration interface. These users can also access API endpoints that are meant for administrators.

Access to the Make API resources depends also on the scopes assigned to the authentication token. Some resources require more than one scope. There are two types of scopes - **read** and **write**.

**Read scope** `:read`

Allows you to use the `GET` method with endpoints, usually to get a list of resources or a resource detail. No modification is allowed.

**Write scope** `:write`

Allows you to use the `POST`, `PUT`, `PATCH`, or `DELETE` methods with endpoints to create, modify, or remove resources.

{% hint style="warning" %}
Even if you are not the administrator, you can assign to your token the scopes meant for administrators. However, if you try to access the admin resources as a regular user, you will receive the `403 Access denied` error in response.
{% endhint %}

## Administration scopes (only for administrators of Make White Label platforms)

<details>

<summary><strong>Administration</strong></summary>

`admin:read`

* Allows getting all resources and information available only to administrators -- all resources that are available in the administration interface, such as collections of all created users, templates, scenarios, and custom and native apps for the whole platform and all their details.

`admin:write`

* Allows performing all actions available only to administrators --- all actions that can be performed in the administration interface, such as creating organizations, deleting approved templates, reviewing custom apps, creating and deleting new users, overwriting scenarios and templates settings.

</details>

<details>

<summary><strong>Native apps</strong></summary>

`apps:read`

* Allows getting a collection of all native apps.
* Allows getting details of a native app.

`apps:write`

* Allows updating a native app.
* Allows deleting a native app.

</details>

<details>

<summary><strong>System settings</strong></summary>

`system:read`

* Allows reading the Make platform settings.

`system:write`

* Allows modifying the Make platform settings.

</details>

## Standard user scopes (for all users of Make platforms)

<details>

<summary><strong>Analytics</strong></summary>

`analytics:read`

* Allows retrieving analytics data for the specified organization.

</details>

<details>

<summary><strong>Connections</strong></summary>

`connections:read`

* Allows retrieving connections for a given team.
* Allows getting details of a connection.

`connections:write`

* Allows creating new connections.
* Allows updating connections.
* Allows deleting connections.
* Allows setting data for connections.
* Allows verifying connections.
* Allows checking if a connection scope is limited.

</details>

<details>

<summary><strong>Custom property structures</strong></summary>

`custom-property-structures:read`

* Allows retrieving the list of custom properties structures in the organization.
* Allows getting custom properties items.

`custom-property-structures:write`

* Allows creating custom properties structures.
* Allows creating custom property structure items.
* Allows updating custom property structure items.
* Allows deleting custom property structure items.

</details>

<details>

<summary><strong>Data stores</strong></summary>

`datastores:read`

* Allows getting all data stores for a given team.
* Allows getting records from a data store.

`datastores:write`

* Allows creating new data store.
* Allows updating data stores.
* Allows deleting data store.
* Allows modifying the records of a data store.

</details>

<details>

<summary><strong>Devices</strong></summary>

`devices:read`

* Allows retrieving all devices for a given team.
* Allows getting details of a device.

`devices:write`

* Allows creating new devices.
* Allows updating devices.
* Allows deleting devices.

</details>

<details>

<summary><strong>Incomplete executions</strong></summary>

`dlqs:read`

* Allows getting all incomplete executions of a given scenario.
* Allows getting details of an incomplete execution.
* Allows getting bundles, blueprints, and logs of an incomplete execution.

`dlqs:write`

* Allows updating incomplete executions.
* Allows deleting incomplete executions.

</details>

<details>

<summary><strong>Custom functions</strong></summary>

`functions:read`

* Allows getting data about the custom functions which belong to the team.
* Allows getting the history of updates to the custom functions.

`functions:write`

* Allows creating custom functions.
* Allows updating custom functions.
* Allows deleting custom functions.

</details>

<details>

<summary><strong>Hooks</strong></summary>

`hooks:read`

* Allows getting all hooks (mailhooks and webhooks) for a given team.
* Allows getting hook requests.
* Allows checking if a hook is active.

`hooks:write`

* Allows creating new hooks.
* Allows updating hooks.
* Allows deleting hooks.
* Allows enabling or disabling hooks.
* Allows starting or stopping the automatic determination of a data structure for a hook.
* Allows setting data for hooks.

</details>

<details>

<summary><strong>Keys</strong></summary>

`keys:read`

* Allows getting all keys for a given team.
* Allows getting key types.

`keys:write`

* Allows creating new keys.
* Allows updating keys.
* Allows deleting keys.

</details>

<details>

<summary><strong>Notifications</strong></summary>

`notifications:read`

* Allows getting all notifications for a given user.
* Allows getting details of a notification.

`notifications:write`

* Allows marking notifications as read.
* Allows deleting notifications.

</details>

<details>

<summary><strong>Organizations</strong></summary>

`organizations:read`

* Allows getting all organizations to which the authenticated user belongs.
* Allows getting installed apps, invitations, user roles, and basic details of organizations.

`organizations:write`

* Allows creating new organizations (only for admins).
* Allows updating organizations.
* Allows deleting organizations.
* Allows accepting invitations to organizations.
* Allows adding members to organizations.

`organizations-variables:read`

* Allows getting data of organization variables to which the authenticated user belongs.
* Allows getting the history of updates of custom organization variables.

`organizations-variables:write`

* Allows creating custom organization variables.
* Allows updating custom organization variables.
* Allows deleting custom organization variables.

</details>

<details>

<summary><strong>Scenarios</strong></summary>

`scenarios:read`

* Allows getting all scenarios for a given team or organization.
* Allows getting details of a scenario.
* Allows getting properties of triggers included in scenarios.
* Allows getting scenario blueprints.
* Allows getting blueprint versions.
* Allows getting scenario logs.
* Allows getting scenario folders.
* Allows inspecting scenario interface.
* Allows retrieving custom scenario properties data.

`scenarios:write`

* Allows creating new scenarios and scenario folders.
* Allows updating scenarios and scenario folder.
* Allows cloning scenarios.
* Allows verifying whether module settings are set or not.
* Allows activating and deactivating scenarios.
* Allows deleting scenarios and scenario folders.
* Allows updating scenario interface.
* Allows adding custom scenario properties data.
* Allows updating custom scenario properties data.
* Allows deleting custom scenario properties data.

`scenarios:run`

* Allows running scenarios with the API.

</details>

<details>

<summary><strong>Custom apps</strong></summary>

`sdk-apps:read`

* Allows getting all custom apps for the authenticated user.
* Allows getting information from specific configuration sections of a custom app.
* Allows getting invitation details for an app.

`sdk-apps:write`

* Allows creating custom apps.
* Allows managing configuration of custom apps.
* Allows cloning custom apps.
* Allows requesting review of custom apps.
* Allows rolling back changes made in custom apps.
* Allows uninstalling custom apps from organizations.
* Allows deleting custom apps.

</details>

<details>

<summary><strong>Teams</strong></summary>

`teams:read`

* Allows getting all teams that belong to a given organization.
* Allows getting details of a team.
* Allows getting all team roles.
* Allows getting details of a team role.

`teams:write`

* Allows creating new teams.
* Allows updating teams.
* Allows deleting teams.

`teams-variables:read`

* Allows getting data of team variables to which the authenticated user belongs.
* Allows getting the history of updates of custom team variables.

`team-variables:write`

* Allows creating custom team variables.
* Allows updating custom team variables.
* Allows deleting custom team variables.

</details>

<details>

<summary><strong>Templates</strong></summary>

`templates:read`

* Allows retrieving all private templates for a given team.
* Allows getting all public templates.
* Allows getting private or public template details.
* Allows getting private or public template blueprints.

`templates:write`

* Allows creating new templates.
* Allows updating templates.
* Allows deleting templates.
* Allows publishing private templates.
* Allows requesting approval of published templates.

</details>

<details>

<summary><strong>Data structures</strong></summary>

`udts:read`

* Allows retrieving all data structures for a given team.

`udts:write`

* Allows creating new data structures.
* Allows updating data structures.
* Allows deleting data structures.
* Allows cloning data structures.

</details>

<details>

<summary><strong>Users</strong></summary>

`user:read`

* Allows getting all users who belong to a given team or organization.
* Allows getting API authentication tokens assigned to the currently authenticated user.
* Allows getting organization invitations assigned to the currently authenticated user.
* Allows getting organization invitations assigned to a user.
* Allows getting organization and team roles that can be assigned to any user.
* Allows getting a number of unread notifications for the currently authenticated user.
* Allows getting organizations invitations for a user.
* Allows getting details of an invitation to an organization for a user.
* Allows getting details of a notification assigned to a user in a given team.
* Allows getting team roles of a user.

`user:write`

* Allows setting a user role for a given team.
* Allows setting a user role in a given organization.
* Allows transferring organization ownership to a user.
* Allows updating a notification for a user in a given team.
* Allows creating a new API authentication token for a currently authenticated user.
* Allows deleting an API authentication token identified by timestamp for a currently authenticated user.
* Allows deleting an account of a currently authenticated user.
* Allows updating details of a user.

</details>
