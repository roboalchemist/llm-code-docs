# Source: https://developers.webflow.com/data/reference/enterprise/workspace-audit-logs/event-types.mdx

***

title: Workspace audit log event types
slug: reference/enterprise/workspace-audit-logs/event-types
description: Review the event types and payloads for the Workspace Audit Logs API.
'og:title': Workspace audit log event types
'og:description': Review the event types and payloads for the Workspace Audit Logs API.
subtitle: >-
Monitor and debug workspace activity with detailed audit logs. Each event
captures who did what, when, and how - from user logins to role changes.
Explore the available event types and their Payload schemas below.
hidden: false
-------------

## `user_access`

Login and logout events for users in the workspace.

##### Event subtypes

| Value    | Description       |
| -------- | ----------------- |
| `login`  | A user logged in  |
| `logout` | A user logged out |

#### Payload schema

| Field       | Type   | Description                                                       |
| ----------- | ------ | ----------------------------------------------------------------- |
| `method`    | string | How the user logged in, enum: `dashboard`, `sso`, `api`, `google` |
| `location`  | string | The geolocation based on the logged IP address                    |
| `ipAddress` | string | The captured IP address of the user                               |

## `custom_role`

Tracks when custom roles are created, updated, or deleted in your workspace. [Learn more about custom roles](https://help.webflow.com/hc/en-us/articles/37207901526419-Create-and-manage-custom-roles).

##### Event subtypes

| Value          | Description                    |
| -------------- | ------------------------------ |
| `role_created` | A custom role has been created |
| `role_updated` | A custom role has been updated |
| `role_deleted` | A custom role has been deleted |

#### Payload schema

| Field              | Type   | Description                          |
| ------------------ | ------ | ------------------------------------ |
| `roleName`         | string | The name of the custom role          |
| `previousRoleName` | string | The previous name of the custom role |

## `workspace_membership`

Tracks when users join or leave the workspace, and when their roles change within it.

##### Event subtypes

| Value               | Description                                |
| ------------------- | ------------------------------------------ |
| `user_added`        | A user has been added to the workspace     |
| `user_removed`      | A user has been removed from the workspace |
| `user_role_updated` | A user's role has been updated             |

#### Payload schema

| Field              | Type   | Description                                                                 |
| ------------------ | ------ | --------------------------------------------------------------------------- |
| `targetUser`       | object | The affected user, with properties `id` and `email`                         |
| `method`           | string | How access was managed, enum: `sso`, `dashboard`, `admin`, `access_request` |
| `userType`         | string | Type of user, enum: `member`, `guest`, `reviewer`, `client`                 |
| `roleName`         | string | The role assigned to the user                                               |
| `previousRoleName` | string | The previous role (for role updates)                                        |

## `site_membership`

Tracks when users are added to or removed from a specific site, and when their site-specific roles change or their granular access to resources. This is similar to workspace membership events, but focused on site-level access instead of workspace-level access.

##### Event subtypes

| Value                          | Description                                                       |
| ------------------------------ | ----------------------------------------------------------------- |
| `user_added`                   | A user has been added to a site                                   |
| `user_removed`                 | A user has been removed from a site                               |
| `user_role_updated`            | A user's site role has been updated                               |
| `user_granular_access_updated` | A user's granular access has been updated for a specific resource |

#### Payload schema

| Field              | Type   | Description                                                                                   |
| ------------------ | ------ | --------------------------------------------------------------------------------------------- |
| `site`             | object | The affected site, with properties `id` and `slug`                                            |
| `targetUser`       | object | The affected user, with properties `id` and `email`                                           |
| `method`           | string | How access was managed, enum: `sso`, `invite`, `scim`, `dashboard`, `admin`, `access_request` |
| `userType`         | string | Type of user, enum: `member`, `guest`, `reviewer`, `client`                                   |
| `roleName`         | string | The role assigned to the user                                                                 |
| `previousRoleName` | string | The previous role (for role updates)                                                          |
| `granularAccess`   | object | The granular access settings for the user, with properties `id`, `name`, `type`, `restricted` |

## `workspace_invitation`

Tracks the lifecycle of workspace invitations from when they're sent to when they're accepted, declined, or canceled.

##### Event subtypes

| Value                     | Description                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `invite_sent`             | A workspace invite was sent                                                                                                               |
| `invite_accepted`         | A workspace invite was accepted                                                                                                           |
| `invite_updated`          | A workspace invite was updated                                                                                                            |
| `invite_canceled`         | A workspace invite was canceled                                                                                                           |
| `invite_declined`         | A workspace invite was declined                                                                                                           |
| `access_request_accepted` | A [guest access request](https://help.webflow.com/hc/en-us/articles/33961349456915-Agency-or-Freelancer-guest-role-overview) was accepted |

#### Payload schema

| Field              | Type   | Description                                                                                                                                                                       |
| ------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `targetUser`       | object | The invited user, with properties `id` and `email`                                                                                                                                |
| `method`           | string | How the invitation was managed, enum: `sso`, `dashboard`, `admin`                                                                                                                 |
| `userType`         | string | Type of user invited, enum: `member`, `guest`, `reviewer`, `client`                                                                                                               |
| `roleName`         | string | The role assigned to the user in the invitation                                                                                                                                   |
| `previousRoleName` | string | The previous role (for updated invitations)                                                                                                                                       |
| `targetUsers`      | array  | List of users approved from a [guest access request](https://help.webflow.com/hc/en-us/articles/33961349456915-Agency-or-Freelancer-guest-role-overview) with an `id` and `email` |

## `workspace_setting`

Tracks changes to Workspace settings.
Currently, this event is triggered only when the AI enablement setting changes, not on any other Workspace setting changes.

##### Event subtypes

| Value             | Description       |
| ----------------- | ----------------- |
| `setting_updated` | A setting changed |

#### Payload schema

| Field           | Type   | Description                                             |
| --------------- | ------ | ------------------------------------------------------- |
| `method`        | enum   | How the value was changed: `admin` or `dashboard`       |
| `previousValue` | string | The previous value of the setting                       |
| `setting`       | enum   | An identifier for the setting that changed: `ai_toggle` |
| `value`         | string | The new value of the setting                            |
