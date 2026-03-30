# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/tabnine-apis.md

# Tabnine APIs

## Enable APIs by Token

Use these APIs to query usage, retrieve audit data, and automate team administration in Tabnine Enterprise.

### Authentication

All APIs return JSON and require an access token.

Only users with Admin access can generate tokens.

1. Go to **Settings** > **Access Tokens**.
2. Click **Generate token**.
3. Enter a token description.
4. Click **Generate Token**.
5. Copy the token before closing the dialog.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5286a28e23d7f9224c90db46ff3377233f83ae16%2FGenerate%20Token.gif?alt=media" alt=""><figcaption><p>Generate a new token in the Access Tokens section</p></figcaption></figure>

If you lose a token, revoke it and generate a new one.

### USAGE METRICS

The Usage API, released with **5.18.0**, provides programmatic access to usage metrics across an organization.

It is available to Enterprise SaaS and private installations.

#### ORGANIZATIONS

Use these endpoints to retrieve organization-wide metadata and usage.

#### **GET CURRENT ORGANIZATION**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET LIST OF TEAMS**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization/teams" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET ACCOUNT USAGE INFO**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization/account-utilizations" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET ORG-LEVEL USAGE**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization/usage" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET USERS NOT ASSIGNED TO TEAMS**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization/users" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

### LICENSES & PERMISSIONS

Use these endpoints to validate entitlements and enabled permissions.

#### **GET LICENSE INFO**

Returns license metadata for the current Tabnine instance.

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/license" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET ACCOUNT PERMISSIONS INFO**

Returns the permissions enabled on this Tabnine instance.

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/instance/permissions" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

## TEAMS AND USERS

Use these endpoints to retrieve team-level and user-level usage data.

#### GET TEAM USERS

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/team/{teamId}/users" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET TEAM USAGE INFO**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/team/account-utilizations" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

**GET TEAM INFO BY `teamId`**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/team/{teamId}" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

**GET TEAM-WIDE USAGE**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/team/usage" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

**Get user info by `user_id`** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-60b98f79fd54e85f545d7a844438263e78077d99%2Ficon%3Duser%20settings.svg?alt=media" alt="" data-size="line">

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/user/{user\_id}" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

**Get user usage**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/user/usage" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

### AUDIT LOGS

The Audit Logs API, released with **5.25.0**, returns audit events for user management, team management, and authentication activity.

The audit log includes:

* Performing user
* Affected user
* Time of change
* Value change for each event

You can use the same mapping from the Usage Metrics API between `user_id` and email, and between `team_id` and team name.

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization/audit-logs" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

### USER MANAGEMENT

The User Management API, released with **5.27.0**, automates user role management and team membership.

#### UPDATE USER <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c70391665db98cc9cd90c01aae8ac3d9c1612f06%2Ficon%3Dreload%402x.png?alt=media" alt="" data-size="line">

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/{userId}" method="patch" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### Permissions

| Role      | Assign Team | Update Role                    | Activate/Deactivate | Invite                         |
| --------- | ----------- | ------------------------------ | ------------------- | ------------------------------ |
| Admin     | ✓           | ✓ (all roles)                  | ✓                   | ✓ (all roles)                  |
| Manager   | ✓           | ✓ (Member, Team Lead, Manager) | ✓                   | ✓ (Member, Team Lead, Manager) |
| Team Lead | ✗           | ✗                              | ✗                   | ✗                              |
| Member    | ✗           | ✗                              | ✗                   | ✗                              |

To use this API, you will need user and team data from the organization and team APIs above.

### TEAM REPOSITORIES

The Repository Management API, released with **5.27.0**, automates repository connection management for teams.

All endpoints follow this structure:

`/api/team/v1/{teamId}/connections/repositories`

As of 5.27.0, only Admins have permission for this endpoint.

#### LIST REPOSITORIES

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1/{teamId}/connections/repositories" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### ADD REPOSITORY

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1/{teamId}/connections/repositories" method="post" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### UPDATE REPOSITORY

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1/{teamId}/connections/repositories/{repositoryLink}" method="put" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### DELETE REPOSITORY

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1/{teamId}/connections/repositories/{repositoryLink}" method="delete" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### Field descriptions

**Common fields**

<table><thead><tr><th width="294.4755859375">Field</th><th width="121.595703125">Type</th><th width="122.1923828125">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>repo_type</code></td><td>string</td><td>Yes</td><td>Repository type: "git" or "perforce"</td></tr><tr><td><code>repository_link</code></td><td>string</td><td>Yes</td><td>Git: repository URL in SSH or HTTPS format. Perforce: depot path such as //depot/main</td></tr><tr><td><code>latest_status</code></td><td>string</td><td>Read-only</td><td>Current indexing status</td></tr><tr><td><code>last_indexed_successfully</code></td><td>string or null</td><td>Read-only</td><td>ISO 8601 timestamp of last successful indexing, or null if never indexed</td></tr></tbody></table>

**Git-specific fields**

<table><thead><tr><th width="294.3095703125">Field</th><th width="122.3916015625">Type</th><th width="121.6357421875">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>authentication_method</code></td><td>string</td><td>Yes</td><td>"ssh" or "https"</td></tr><tr><td><code>authentication_credentials_name</code></td><td>string</td><td>Conditional</td><td>Required when <code>authentication_method</code> is "https"</td></tr><tr><td><code>view_source_link_pattern</code></td><td>string</td><td>No</td><td>URL pattern for viewing source code. Supports <code>{sha}</code>, <code>{path}</code>, and <code>{line}</code></td></tr></tbody></table>

**Perforce-specific fields**

<table><thead><tr><th width="293.7822265625">Field</th><th width="122.4013671875">Type</th><th width="121.73828125">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>authentication_credentials_name</code></td><td>string</td><td>Yes</td><td>Must match an existing Perforce credential name for the team</td></tr><tr><td><code>view_source_link_pattern</code></td><td>string</td><td>No</td><td>Currently not used for Perforce</td></tr></tbody></table>

**Status values**

| Status     | Description                               |
| ---------- | ----------------------------------------- |
| `pending`  | Repository is queued for initial indexing |
| `cloning`  | Repository is being cloned                |
| `indexing` | Repository is currently being indexed     |
| `success`  | Repository was successfully indexed       |
| `failed`   | Last indexing attempt failed              |

{% hint style="info" %}
Perforce depots typically skip `cloning` and go directly to indexing.
{% endhint %}

### TEAM MANAGEMENT

Use these APIs to manage teams, users, and invitations in Tabnine Enterprise.

#### CREATE A TEAM

Introduced in 6.0.0.

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1" method="post" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **GET TEAM BY ID**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1/{id}" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **RENAME TEAM**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/team/v1/{id}" method="put" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

### USER MANAGEMENT

#### **GET USER INFO**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/{userId}" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### UPDATE USER PROPERTIES

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/{userId}" method="patch" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **LOOK UP USER BY EMAIL**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/by-email/{email}" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **LIST USER'S ALLOWED TEAMS**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/{userId}/allowed-teams" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

**Add teams to a user's allowed list**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/{userId}/allowed-teams" method="patch" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

**Remove teams from a user's allowed list**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/user/v1/{userId}/allowed-teams" method="delete" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

### INVITATION MANAGEMENT

#### **INVITE USER BY EMAIL**

Use this endpoint to invite a user to a team by email.

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/invitation/v1" method="post" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **LIST PENDING INVITES**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/invitation/v1" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

#### **REVOKE INVITES BY ID**

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/invitation/v1" method="delete" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}

### AGENT USAGE

This API returns aggregated usage analytics for your organization, broken down by AI tools such as agent, chat, code completions, and instruct over a time range.

#### TOOLS USAGE

{% openapi src="<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>" path="/api/v1/organization/usage" method="get" %}
<https://raw.githubusercontent.com/Gedalyah-Reback-Tab9/t9-api-yamls/refs/heads/main/docs/unified-tabnine-api.yaml>
{% endopenapi %}
