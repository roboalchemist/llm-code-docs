# Source: https://docs.aporia.com/administration/rbac.md

# Role Based Access Control (RBAC)

Aporia supports full role based access control. Using account-level and workspace-level permissions, users will only have access to the data and actions for which they are permitted.&#x20;

## Aporia roles & permissions

### Account level roles

An **`account`** is the highest level entity in Aporia and represents your company/organization.&#x20;

Every user in Aporia must be associated with an **`account`**. There are two types of roles at the **`account`** level:

| Account Role   | Permissions                                                                                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| account.admin  | Account admins can manage users (invite new users & update their associated permissions/roles). Account admins are admins of all workspaces in their account (top-down inheritance). |
| account.member | Account members (the default permission of a user) can access the Aporia platform in your organization's account.                                                                    |

An **`account.admin`** may create multiple **`workspaces`** within your Aporia **`account`.** &#x20;

### Workspace level roles

A **`workspace`** is a silo created for separate teams. Each **`workspace`** represents a team/group within your organization and acts as an independent entity, i.e. a workspace encapsulate models, dashboards, monitors, etc. and these entities are ***not*** shared between workspaces.

There are three types of roles at the **`workspace`** level:

| Workspace Role   | Permissions                                                                                                                                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workspace.admin  | <p>Manage user permissions of existing workspace users and ability to invite existing account members to the respective workspace. <br>Edit & view permissions across all Aporia entities within the workspace, i.e. models, versions, dashboards, monitors, segments, & metrics.</p> |
| workspace.editor | Edit & view permissions across all Aporia entities within a workspace, i.e. models, versions, dashboards, monitors, segments, & metrics.                                                                                                                                              |
| workspace.viewer | View-only permissions for all entities in the workspace.                                                                                                                                                                                                                              |

## Roles management

#### Via Aporia platform

As an account admin you can manage roles as follows:

1. Log in to the Aporia platform
2. Go to the `Teams` page
3. Manage your account and workspace level permissions by adding, removing, and editing roles.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F3KLyJrBsKLqtBk6MoCZa%2Frbac.gif?alt=media&#x26;token=8fab3b1a-3d32-4256-91c6-5f6295727683" alt=""><figcaption><p>Account management via Aporia Platform</p></figcaption></figure>
