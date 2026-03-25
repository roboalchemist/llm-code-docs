# Source: https://documentation.onesignal.com/docs/en/manage-team-members.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Team Members

> Manage OneSignal user access by adding, removing, or updating team member roles at the app or organization level. Learn role permissions and plan availability.

## Overview

OneSignal allows you to manage user access either at the **Organization level** (all apps) or at the **App level** (specific apps). Each user can be assigned a role—**Admin**, **Editor**, or **Viewer**—based on their needs and responsibilities.

For example:

* An **analyst** who needs to review messaging performance across apps could be an **Organization Viewer**.
* A **developer** or **marketer** working on one app can be assigned as an **App Admin**.

<Note>For details on how Apps and Organizations work together, see [Apps, orgs, & accounts](./apps-organizations).</Note>

***

## Managing team access

You can grant access at either the **Organization** level (all apps) or **App** level (specific apps).

### Organization-level access

Organization Admins can invite users and assign them roles that apply to all apps in the org.

To invite a new team member:

1. Navigate to **Organizations > \[Your Organization] > Team Members**
2. Click **Invite to Organization**
3. Choose a role: Admin, Editor, or Viewer

<Frame caption="Inviting a new team member to an organization">
  <img src="https://mintcdn.com/onesignal/dkNDLeCi_Ev9iHwJ/images/dashboard/dashboard-org-team-members.png?fit=max&auto=format&n=dkNDLeCi_Ev9iHwJ&q=85&s=64947b7b033826b0582a30627d9d4787" width="1986" height="798" data-path="images/dashboard/dashboard-org-team-members.png" />
</Frame>

### App-level access

App Admins can invite users to a single app.

To invite someone to a specific app:

1. Go to your App's **Settings > Team Members**
2. Click **Invite to App**
3. Assign the user a role for that app

<Frame caption="Inviting a new team member to an app">
  <img src="https://mintcdn.com/onesignal/dkNDLeCi_Ev9iHwJ/images/dashboard/dashboard-app-team-members.png?fit=max&auto=format&n=dkNDLeCi_Ev9iHwJ&q=85&s=0ab2729a37cfa67223da222c6b623de9" width="2014" height="880" data-path="images/dashboard/dashboard-app-team-members.png" />
</Frame>

### Update or remove user access

To update a role or remove someone:

1. Go to your **Team Members** page for the **Organization** or **App**
2. Click the **Options** menu (⋮) next to the user's email
3. Select **Update Role** or **Remove**

<Frame caption="Updating an existing team member's role">
  <img src="https://mintcdn.com/onesignal/dkNDLeCi_Ev9iHwJ/images/dashboard/dashboard-team-members-update-remove.png?fit=max&auto=format&n=dkNDLeCi_Ev9iHwJ&q=85&s=c87b2682f6c5e8e2596050f95ed627e6" width="1914" height="798" data-path="images/dashboard/dashboard-team-members-update-remove.png" />
</Frame>

***

## Roles and permissions

Organization roles take priority over App roles. This means if someone is an Organization Admin, they will have full access to all apps within the organization.

### Role types

| Role   | Best for                     | Access summary                                                                                 |
| ------ | ---------------------------- | ---------------------------------------------------------------------------------------------- |
| Admin  | 🛠️ Developers, Owners       | Full control over settings, messaging, users, integrations, and permissions                    |
| Editor | 📣 Marketers, PMs            | Can create, edit, and send messages. Can view/export analytics but not change app/org settings |
| Viewer | 📊 Analysts, Read-only users | Can view analytics, messages, and templates. Cannot edit or send messages                      |

### Permission matrix

| **Permission**                                              | **Viewer** | **Editor** | **Admin** |
| :---------------------------------------------------------- | :--------: | :--------: | :-------: |
| Send messages (Journeys, Automations, Webhooks)             |      ❌     |      ✅     |     ✅     |
| Segments                                                    |  Read-only |      ✅     |     ✅     |
| Data Tags                                                   |  Read-only |      ✅     |     ✅     |
| CSV Import                                                  |      ❌     |      ❌     |     ✅     |
| Templates                                                   |  Read-only |      ✅     |     ✅     |
| Exporting                                                   |      ❌     |      ✅     |     ✅     |
| Analytics                                                   |  Read-only |      ✅     |     ✅     |
| API Key Access                                              |      ❌     |      ❌     |     ✅     |
| App Usage                                                   |      ✅     |      ✅     |     ✅     |
| 2FA / Email / Password change                               |      ✅     |      ✅     |     ✅     |
| Auth Key / Delete Key access                                |      ❌     |      ❌     |     ✅     |
| App Settings (Integrations, Platform Settings, Roles)       |      ❌     |      ❌     |     ✅     |
| Org Settings (Upgrades, Role Management, SSO, Org-wide 2FA) |      ❌     |      ❌     |    ✅\*    |

<Info>
  **\*** Org Settings access is limited to users with the **Organization Admin** role. App-level-only Admins do not have permission to modify organization-level settings such as billing, plan upgrades, SSO, or org-wide 2FA.
</Info>

### Role availability by plan

| Role Type | Free Plan | Growth Plan | Professional Plan | Enterprise |
| --------- | --------- | ----------- | ----------------- | ---------- |
| Admin     | ✅         | ✅           | ✅                 | ✅          |
| Editor    | ❌         | ❌           | ✅                 | ✅          |
| Viewer    | ❌         | ✅           | ✅                 | ✅          |

<Note>
  [View full pricing and plan features](https://onesignal.com/pricing).
</Note>

***

## Best practices

* ✅ **Assign the minimum role needed**—for example, don't give full Admin access if View or Edit is enough.
* 🧠 **Use org-level roles** for users who need access across many apps (like analysts or leadership).
* 🔒 **Limit API key access** to trusted technical users with Admin roles.
* 🆓 **Free plans** only support Admins—upgrade to add Viewers and Editors.

***

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
