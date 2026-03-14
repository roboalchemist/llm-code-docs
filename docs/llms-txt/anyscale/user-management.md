# Source: https://docs.anyscale.com/administration/organization/user-management.md

# Manage users

[View Markdown](/administration/organization/user-management.md)

# Manage users

This page describes how to add, remove, and modify users in your Anyscale organization. You must be an organization owner to manage users.

For role definitions and permissions, see [Roles and permissions](/administration/organization/permissions.md).

To configure single sign-on (SSO), see [Configure SSO for your Anyscale organization](/administration/organization/configure-sso.md).

## Add users to an organization[​](#add-org "Direct link to Add users to an organization")

To invite users to your organization, do the following:

1. Click your user icon.
2. Click **Users & IAM**.
3. Click **Invite**.
4. Enter the email addresses of the invitees, separated by commas.
5. Click **Send invites**.

Invitees receive an email with a link to register and join your organization.

## Add users to a cloud[​](#add-cloud "Direct link to Add users to a cloud")

Organization owners must add users to each cloud to grant access. For cloud role definitions, see [Cloud roles](/administration/organization/permissions.md#cloud-roles).

To add users to a cloud, do the following:

1. Go to the [Clouds page](https://console.anyscale.com/v2/clouds).
2. Click the cloud you want to grant access to.
3. Click **Grant permission**.
4. Select users from the organization.
5. Assign a role (collaborator, owner, or read-only).

### Auto add users to a cloud[​](#auto-add "Direct link to Auto add users to a cloud")

Cloud owners can enable auto add to grant all organization users cloud collaborator permissions automatically. When a new user joins the organization, Anyscale assigns cloud collaborator permissions within 30 seconds.

To enable auto add, do the following:

1. Go to the [Clouds page](https://console.anyscale.com/v2/clouds).
2. Click the cloud name.
3. Click **Settings**.
4. Click **Auto add users**.
5. Click to toggle the **Auto add users** setting.

You can also enable auto add with the CLI:

```
anyscale cloud update <cloud-name> --enable-auto-add-user
```

note

Disabling auto add users doesn't revoke existing permissions. It only stops automatic additions for new users.

## Modify user roles[​](#modify "Direct link to Modify user roles")

To change a user's organization role, do the following:

1. Click your user icon.
2. Click **Users & IAM**.
3. Click **Manage access**.
4. Find the user and click the edit icon ![Edit icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAUCAYAAACAl21KAAABU2lDQ1BJQ0MgUHJvZmlsZQAAGJVtkD0sQ2EUhp9WpZQIYTR0EH8pkdJgrA4iQZqi/qbb26ombd3cXhGJTSIWIxOLwWyrUcRELAiJ3WCSkHShrnNbtMVJ3pwnb97vy5sDdhRNSzqAVNrQQ6Mj7rn5BbfzCSc2amlmSFEzmj8YHJcI37tycneSlbnpsf46POjYfd4JP17WvFwsnnW7/uYrxhWNZVTZ76J2VdMNsLUJB9cMzWIRLbqUEt62OF7kfYsjRT4uZKZDAeFz4UZ1WYkK3wp7ImV+vIxTyVX1q4PVvj6Wnpmy+ohaCTOJl0GG5S7/5wYKuQAraKyjkyDOMgZu/OJoJIkJj5FGpRePsJc+kc+67++7lbzEFvhE9uuSF72Ckw2pPFHyOjeh6QNOGzRFV36uacs5Mkv93iLXZaF6zzRfZ8HZBfl703zLmmb+CKoe5G3uE9a9YtwqEWfPAAAARGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAACoAIABAAAAAEAAAASoAMABAAAAAEAAAAUAAAAAN+Z0lsAAAICaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xODwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yMDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo46BEmAAAAxUlEQVQ4Ea3Uiw2EIAwG4Hq5SWAWZmElmIVZYJU7f5ISwGp9NVFB6icvXX5r0AvxuWKUUnbTT0MpJQohUIxRxE5BQHBYaynnLGIqxIhzjrz3hKuEHUI9AgDB82SMGYa4C0kI5ge9AcowayJ0FQG2ge4gG+guMkBPkAY9RRqEAgIbDnG0OjVBOH37e+gZYm+J+9y5PEAAENI+mR+c68tbv5HaI2x77s38Jq2OecXnUiEgPD/ag1I7oDY0/hilRO3eAGnJWvsfEn+dcYp+Fp8AAAAASUVORK5CYII=).
5. Use the **Select a base role** dropdown to choose a role for the user.
6. Click **Save**.

warning

Demoting an organization owner to collaborator removes all implicit permissions for clouds and projects. You must explicitly grant cloud roles to allow access.

## Delete users[​](#delete "Direct link to Delete users")

To remove a user from your organization, do the following:

1. Click your user icon.
2. Click **Users & IAM**.
3. Select the users to remove.
4. Click **Delete**. A confirmation displays.
5. Click **Delete** to confirm.

warning

To delete an organization owner, first demote them to collaborator.

warning

If your organization uses SSO, also remove the user from your identity provider's Anyscale integration to fully restrict access.

### What happens to resources created by deleted users?[​](#what-happens-to-resources-created-by-deleted-users "Direct link to What happens to resources created by deleted users?")

Removing a user from an organization doesn't delete their workloads or resources:

| Resource                   | Behavior                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------- |
| Workspaces, jobs, services | Remain running. Duplicate to assume ownership.                                                          |
| Schedules                  | Continue until permission errors occur. Any user can resume and becomes the creator of subsequent jobs. |
| Projects, clouds           | Organization owner becomes the implicit owner and can transfer ownership.                               |

note

If you re-invite a previously deleted user, they receive a new user ID. Previous roles and permissions don't restore automatically.
