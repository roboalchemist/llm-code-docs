# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workspaces/team-members/role-based-access-control.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workspaces/team-members/role-based-access-control.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workspaces/team-members/role-based-access-control.md

# Source: https://docs.roboflow.com/workspaces/team-members/role-based-access-control.md

# Role-Based Access Control (RBAC)

{% hint style="info" %}
Role-Based Access Control is a **premium** feature. Without it, every user must be an Admin.

For up-to-date information on our plans and their associated features, see our [pricing page](https://roboflow.com/pricing).
{% endhint %}

Role-Based Access Control allows you to assign different access permissions to [team members](https://docs.roboflow.com/workspaces/team-members) in your workspace.

## Roles

Our Default Roles help facilitate better security practices while [building and improving computer vision models as a team](https://docs.roboflow.com/annotate/team-collaboration).

Roboflow supports three default roles:

* Creator/Admin - Full access to the platform
* Reviewer - Assign, review, and work on labeling jobs
* Labeler - Work on assigned labeling jobs

{% hint style="info" %}
The Creator role is an "honorific", signifying which account originally created the workspace. It has all the same permissions as the Admin role, but cannot be transferred or reassigned.
{% endhint %}

## Permissions

The permissions for these roles are broken out below:

|                                              | Admin                | Reviewer             | Labeler              | Custom   |
| -------------------------------------------- | -------------------- | -------------------- | -------------------- | -------- |
| View assigned labeling jobs                  | :white\_check\_mark: | :white\_check\_mark: | :white\_check\_mark: | Optional |
| Label images                                 | :white\_check\_mark: | :white\_check\_mark: | :white\_check\_mark: | Optional |
| Submit labeling jobs                         | :white\_check\_mark: | :white\_check\_mark: | :white\_check\_mark: | Optional |
| Review labeling jobs                         | :white\_check\_mark: | :white\_check\_mark: |                      | Optional |
| Assign labelers and reviewers                | :white\_check\_mark: | :white\_check\_mark: |                      | Optional |
| Approve and reject labeled images            | :white\_check\_mark: | :white\_check\_mark: |                      | Optional |
| Manage team members                          | :white\_check\_mark: |                      |                      | Optional |
| Upload, delete, and export images and labels | :white\_check\_mark: |                      |                      | Optional |
| Train models                                 | :white\_check\_mark: |                      |                      | Optional |
| Build workflows                              | :white\_check\_mark: |                      |                      | Optional |
| Deploy models                                | :white\_check\_mark: |                      |                      | Optional |
| View API keys                                | :white\_check\_mark: |                      |                      | Optional |
| View Credit Usage                            | :white\_check\_mark: |                      |                      | Optional |
| Manage billing                               | :white\_check\_mark: |                      |                      | Optional |

## Custom Roles

{% hint style="info" %}
Custom roles is a premium feature, available to select Enterprise plan customers. [Talk to our Sales team](https://roboflow.com/sales) to get access to Custom Roles.
{% endhint %}

Once Custom Roles are enabled for your workspace, you can manage them from the Team Members settings page:

1. Navigate to your workspace settings
2. Select Team Members from the sidebar
3. Click on the Roles tab

The Roles tab displays all available roles in your workspace, including system roles (Admin, Labeler, Reviewer) and any custom roles you've created:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FK8GX7LP3Kc2I87GFmnds%2Fimage.png?alt=media&#x26;token=e46112f6-ff24-445c-87ef-586c23c3a244" alt=""><figcaption></figcaption></figure>

### Managing Roles

#### Viewing Roles

The Roles page shows:

* Default Role: The role automatically assigned to new workspace members
* Role List: All available roles with their folder access settings
* Each role displays whether it has "All Folder Access" enabled

System roles like Admin, Labeler, and Reviewer come pre-configured with standard permission sets optimized for common use cases.

{% hint style="info" %}
Folder Permissions is a premium feature, available to select Enterprise plan customers. [Talk to our Sales team](https://roboflow.com/sales) to get access to Folder Permissions.
{% endhint %}

#### Creating a Custom Role

To create a new custom role:

1. Click the + New Role button in the top-right corner
2. In the role creation dialog: - Enter a Role Name: Choose a descriptive name for the role - Duplicate Permissions From: Select an existing role to use as a template (e.g., Admin, Labeler, Reviewer) - Click Duplicate to copy the selected role's permissions
3. Configure permissions by checking or unchecking options: - Grant All Folder Access: Allows users to bypass folder permission restrictions and see all folders - Permission Categories: Organized by function (e.g., Dataset Management, Dataset Create, Dataset Delete, Dataset Overview) - Each permission includes a description of what it grants
4. Use Select All to quickly enable all permissions
5. Click Create Role to save

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Frep8v0WRcUC3acE24G3P%2Fimage.png?alt=media&#x26;token=4ea2b33f-043d-4921-9af5-45e2050f4700" alt=""><figcaption></figcaption></figure>

#### Editing Custom Roles

To modify an existing custom role:

1. Locate the role in the roles list
2. Click the ... menu button on the right side of the role row
3. Select Edit Role from the dropdown menu
4. Modify permissions as needed
5. Save your changes

Note: System roles (Admin, Labeler, Reviewer) cannot be edited. You can only create custom roles or edit roles you've previously created.

#### Deleting Custom Roles

To remove a custom role:

1. Locate the role in the roles list
2. Click the ... menu button on the right side of the role row
3. Select Delete Role from the dropdown menu
4. Confirm the deletion

Important: Before deleting a role, ensure no users are currently assigned to it, or reassign those users to another role first. System roles cannot be deleted.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FqivTqOT7xKNMngdauHGz%2Fimage.png?alt=media&#x26;token=4ea62a7f-3e31-40ab-bc34-59200abce332" alt=""><figcaption></figcaption></figure>

#### Setting a Default Role

The default role is automatically assigned to new members when they join your workspace:

1. In the Default Role section at the top of the Roles tab
2. Click the dropdown menu
3. Select the role you want to use as the default
4. The change takes effect immediately for all future invitations

#### Assigning Custom Roles

Once Custom Roles are configured, you can assign them when inviting team members :

1. Navigate to the Members tab under Team Members
2. Click Invite Members
3. Choose the desired custom role from the role dropdown
4. Complete the invitation or update process

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FS6Bk3urZ4ktUfTSjHlAB%2Fimage.png?alt=media&#x26;token=11f43e22-68b4-4cbf-86e4-4292e6e378dd" alt=""><figcaption></figcaption></figure>

Custom Roles can be also assigned to existing members on same page:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FyC4mTOOuIUYbxxXQkiUL%2Ftutorial_team_members.png?alt=media&#x26;token=a0c84b36-5875-4799-9d76-c7d3404ad217" alt=""><figcaption></figcaption></figure>

#### Further Reading

For more information on team management and permissions, see:

* Inviting Team Members
* Folder Permissions
* Workspace Settings

Once Custom Roles are turned on, you can [Invite Team Members](https://docs.roboflow.com/workspaces/team-members/invite-a-team-member) as normal, specifying the Custom Role at time of invitation.

### Further Reading
