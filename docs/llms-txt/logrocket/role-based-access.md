# Source: https://docs.logrocket.com/docs/role-based-access.md

# Role-Based Access Control

## Overview

Customers can now define custom roles within their LogRocket accounts to limit access to potentially sensitive information, as well as restrict access on a per-project basis.  Please note that this feature is only available on the Professional plan.

To access these controls and define new roles, visit the [Team Roles Page](https://app.logrocket.com/r/settings/roles). Admin users only will see a 'Team Roles' page within Settings.

Roles that are defined on this page can then be assigned to individual team members on the Team Members page.  Each team member can be assigned multiple roles in the dropdown next to their name.

## Built-In Roles

LogRocket provides three built-in roles that are always available for you to use and cannot be modified or deleted.  These built-in roles automatically have access to **all projects**.  If project-restricted functionality is needed, you should create Custom Roles.

**Admin**\
Admin users have access to all functionality within LogRocket, including project controls, role creation and assignment, and billing functionality.  This is also the only role with access to specific product features, such as Audit Logging and GDPR/CCPA deletion.

**Developer**\
Developer users can access all Dashboard (including Errors and Metrics) and session playback features, as well as most Settings.  They cannot perform billing-related tasks or interact with Admin-only features.

**Guest**\
Guest users only have the ability to view session playback when a specific link is provided to them.  They cannot access the Dashboard or search for sessions.

Note that this is the only type of user that does **not** count against your seat count, but all Guests must still be invited and listed within your application for security purposes.

<Image align="center" className="border" border={true} src="https://files.readme.io/d7b7b4a-Screen_Shot_2024-05-15_at_11.36.56.png" />

## Custom Roles

You can create Custom Roles using the 'Add Role' button to reveal the Role Creation pane.

You can select whether the role has access to all projects or only limited access to selected projects.

<Image align="center" className="border" border={true} src="https://files.readme.io/844fa40-Screen_Shot_2024-05-15_at_11.33.13.png" />

> 🚧 Permissions across projects
>
> Please note that the selected set of permissions will apply across all projects the role has access to.  A user cannot be a Guest on one project and a Developer on another.

You have the ability to choose highly granular permissions to ensure that your employees only have access to exactly what they need.

**Permissions Options**

* Session Playback:  the ability to view session playback only.

  * Developer Pane:  the ability to view the developer pane (performance tabs and logging only) within the session replay.  If this is selected then please note that session playback is automatically selected as a permission.

    * Network Pane:  the ability to view the network pane as part of the session playback, not including the content of the request/response bodies

      * Request Bodies:  the ability to view full request/response bodies as part of a network request.  If this is selected then all permissions above are automatically applied

* Dashboard Features: the ability to view the Home and Sessions tabs, as well as use the search bar to locate and filter sessions. This permission alone is not sufficient to create or edit any charts or dashboards.

  * Custom Dashboards: the ability to view and edit all personal/team dashboards, as well as create and edit charts

  * Issues: the ability to view the Issues tab and ignore/resolve errors

  * Feedback surveys: the ability to view, create and edit feedback surveys

* General Settings: The ability to view and modify non-admin settings configurations (e.g set session limits, change the project name, configure issue & conditional recording settings, etc)

* Invite Users: The ability to invite new members to LogRocket with the specified roles. Users with this permission can create, edit and revoke invites to new members for the roles specified.

## Setting a Default Role

You can choose any custom or built-in role to serve as the default role for any new users joining your organization.  You can select this role from the Team Roles page by selecting the three dots in the top right corner of the role definition, or select it from a dropdown on the Team Members page.