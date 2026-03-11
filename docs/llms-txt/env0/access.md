# Source: https://docs.envzero.com/guides/admin-guide/environments/access.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Access

> Control RBAC permissions at the environment level in env zero to grant users access only to relevant environments

In every organization, there is a need to establish custom permission assignments tailored to their specific needs. For example, when collaborating with outsourced teams, it becomes crucial to grant permissions exclusively to the areas they are directly involved in, without providing unnecessary access. To address this requirement, env zero lets you control RBAC Permissions all the way to the granularity of a specific environment.

With this feature, administrators can precisely define permissions at the environment level, ensuring that users are granted access only to the environments directly relevant to their tasks. This capability offers organizations the flexibility to maintain security, optimize collaboration, and tailor permissions according to specific teams or projects

<Warning>
  Role To Contorl Environment Access

  In order to configure Environment Access, the assigning user needs to have the `ASSIGN ROLE ON ENVIRONMENT` permission.

  Project and Organization admins have that permission by default.

  [Read more here](/guides/admin-guide/user-role-and-team-management/user-management)
</Warning>

## How to assign Access to an Environment

### Preconditions

There are 2 things you need before assigning access to an environment:

1. The [Environment](/guides/admin-guide/environments/env-zero-setting-up-a-new-environment) should exist beforehand
2. You need to have a [Custom Role](/guides/admin-guide/user-role-and-team-management/custom-roles) with the specific permissions you wish to assign

<Note>
  Roles

  At the moment - only custom roles are supported for environment access
</Note>

### Assigning Access

1. Navigate to an existing environment, and click on the ACCESS tab

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/5bd01cd-project_envs_access_1_fix.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=262c31702b38cecd05cc81880775c7f3" alt="Interface screenshot showing configuration options" width="1682" height="840" data-path="images/guides/admin-guide/environments/5bd01cd-project_envs_access_1_fix.png" />
</Frame>

1. While in that tab, you can assign access to either individual Users or entire Teams
2. On the two tables, you can see the entire collection of users and teams in your organization (respectively)
3. To assign one a role on the current environment, make sure the checkbox on the left-hand side is ticked, and select the role you wish to assign
   <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/010be27-screenshot_2023-06-08_at_15.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=a9bc85564d5ddae2b8368aa18119adcd" alt="" width="1303" height="543" data-path="images/guides/admin-guide/environments/010be27-screenshot_2023-06-08_at_15.png" />
4. Finally, hit "save"
   <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/57e2c71-screenshot_2023-06-08_at_15.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=7ea6ab5c00feb0a46e9a44ceb8607324" alt="" width="1302" height="543" data-path="images/guides/admin-guide/environments/57e2c71-screenshot_2023-06-08_at_15.png" />

And you're good to go!

<Warning>
  Project View

  When a user is given permissions to a specific environment - they can see all ancestor projects leading up to it. This is purely for traversal, and they won't have any other permissions for those projects, so keep in mind this is not the same as them having `VIEW PROJECT` permissions for the project tree
</Warning>

Built with [Mintlify](https://mintlify.com).
