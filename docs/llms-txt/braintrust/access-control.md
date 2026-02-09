# Source: https://braintrust.dev/docs/admin/access-control.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Access control

> Set up permission groups and access controls

Braintrust provides flexible access control at organization, project, and object levels. Use permission groups to grant users specific permissions across resources.

## Built-in permission groups

Every organization starts with three permission groups:

* **Owners**: Full access to organization, data, and settings. Can invite/remove members, manage permissions, and delete resources
* **Engineers**: Can create, read, update, and delete projects and resources. Cannot manage members or access controls
* **Viewers**: Read-only access to projects and resources. Cannot create, update, or delete anything

These groups are scoped to the entire organization. Assign users to built-in groups when inviting them or from <Icon icon="settings-2" /> **Settings** > <Icon icon="users-round" /> **Members**.

## Create custom permission groups

Build groups with specific permissions:

1. Go to <Icon icon="settings-2" /> **Settings** > **Organization** > <Icon icon="shield-check" /> **Permission groups**.
2. Click **Create permission group**.
3. Enter group name and description.
4. Click **Create**.

After creating a group, configure its permissions.

## Set organization permissions

Grant organization-level permissions to custom groups:

1. Find the group in the permission groups list.
2. Click **Permissions**.
3. Select organization-level permissions:
   * **Manage settings**: Change organization configuration.
   * **Manage members**: Invite users.
   * **Remove members**: Remove users.
   * **Manage access**: Grant and revoke permissions (super-user ability).
4. Select permissions for all projects:
   * **Read**: View projects and their resources.
   * **Create**: Create experiments, logs, datasets.
   * **Update**: Modify existing resources.
   * **Delete**: Remove resources.
   * **Manage access**: Grant permissions on projects.
5. Click **Save**.

<Warning>
  **Manage access** is a super-user permission. Users with this permission can grant themselves any other permission. Assign it carefully.

  **Manage settings** grants users the ability to change organization-level settings like the API URL.
</Warning>

## Set project permissions

Limit group access for a specific project, including object-level permissions:

1. [Create a custom permission group](#create-custom-permission-groups).
2. In your project, go to <Icon icon="settings-2" /> **Settings** > **Project** > <Icon icon="shield-check" /> **Project permissions**.
3. Search for your group.
4. Click the pencil icon next to the group.
5. Select project permissions:
   * **Read**: View project and its resources.
   * **Create**: Create experiments, logs, datasets.
   * **Update**: Modify existing resources.
   * **Delete**: Remove resources.
   * **Manage access**: Grant permissions on this project.
6. Select object-level permissions for experiments, datasets, logs, prompts, and playgrounds:
   * **Create**: Create the object.
   * **Read**: View the object.
   * **Update**: Modify the object.
   * **Delete**: Remove the object.
   * **Manage access**: Grant permissions on this object.
7. Click **Save**.

Users must have Read permission on a project to see it in the UI.

## Manage group membership

Add or remove users from permission groups:

1. Go to <Icon icon="settings-2" /> **Settings** > **Organization** > <Icon icon="shield-check" /> **Permission groups**.
2. Find the group in the permission groups list.
3. Click **Group access**.
4. Click <Icon icon="user-round" /> **Users**.
5. To add: Search for users and click **Add**.
6. To remove: Click the **X** next to a user's name.

Users can belong to multiple permission groups. Their effective permissions are the union of all group permissions.

## Use service accounts

Service accounts provide credentials for system integrations:

1. Go to <Icon icon="settings-2" /> **Settings** > **Organization** > <Icon icon="server" /> **Service tokens**.
2. Click **+ Service token**.
3. Enter service account name.
4. Assign permission groups or grant specific permissions.
5. Click **Create**.
6. Copy and save the auto-generated service token somewhere safe and accessible. For security reasons, you will not be able to view it again. If you lose the service token, you must create a new one.
7. Use the token like an API key in SDK or API calls.

Service accounts are not tied to individual users. They maintain access even when team members leave.

<Note>
  Only organization owners can create and manage service accounts.

  For hybrid deployments, you must configure a service token for the data plane to enable features like data retention. See [Data plane manager](/admin/self-hosting/advanced#data-plane-manager) for more details.
</Note>

## Programmatic access control

To automate the creation of permission groups and their access control rules, use the Braintrust API. See the API reference for [groups](/api-reference/groups/list-groups) and [permissions](/api-reference/acls/list-acls).

## Next steps

* [Manage organizations](/admin/organizations) to invite members and assign groups
* [Manage projects](/admin/projects) to configure project-level permissions
* [Set up automations](/admin/automations) with service accounts
* [API reference](/api-reference/groups/list-groups) for programmatic access control
