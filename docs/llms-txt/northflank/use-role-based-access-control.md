# Source: https://northflank.com/docs/v1/application/secure/use-role-based-access-control.md

# Use role-based access control

You can manage the permissions of your team members using role-based access control (RBAC). These roles define the resources that your team members can view and edit in the Northflank UI.

Roles can be given specific permissions based on CRUD operations for the different Northflank resources such as projects, services, jobs, pipelines and addons. Roles can also be restricted to certain projects, and be given permissions to manage aspects of the team itself.

You can use an organisation create and manage roles across teams, and to manage organisation permissions.

> [!note] 
> [Click here](https://app.northflank.com/s/account/roles) to view your team's roles.

## Default roles

#### Owner

When you create a team you are given the role of `owner` which grants all permissions across the entire team account. The owner cannot be removed from the team, you must transfer the owner role to another user before leaving the team.

#### Admin

The default `admin` role grants a user full permissions across the team to create, read, update, and delete resources and modify team settings. You should check and modify the permissions granted by the `admin` role when you create your team.

#### Default

When you invite a user to a team they are automatically assigned the `default` role which permits limited access to create, read, and update resources, but not to delete them, and only access to view team settings. You should check and modify the permissions granted by the `default` role when you create your team.

## Create and edit roles

The team `owner` and any role with permissions, such as the `admin` role, can create and modify roles in the team's account settings.

You can select members to be assigned to the role immediately, or grant the role to members later.

![Creating a role for a team in the Northflank application](https://assets.northflank.com/documentation/v1/application/secure/use-role-based-access-control/edit-rbac-role.png)

## Restrict roles

Roles can be restricted to specific projects, so that the role will only grant members the given permissions within the selected projects.

## Assign roles

Roles can be assigned to team members by editing the role in the team's account settings and selecting members from the drop-down list. Roles can be removed from members by deleting them from the list.

You can also add and remove roles from a member from the members page in the team's account settings and opening the role selector for that member. You can add and remove roles from invited users that have not yet been added to the team here as well.

## Create organisation roles

You can manage user roles on an organisational level to ensure compliance with your security policies.

### Directory groups

If you have [enabled directory sync](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation#sync-your-directory), you can select directory groups to associate with the role. Users in the directory groups will be assigned the role, and the role will be removed from users if they are removed from the directory group.

### Organisation permissions

You can grant roles permissions to create and manage teams, and to manage organisational settings.

### Team and project restrictions

Restricting the role to specific teams will allow organisation users with the role to only view and interact with the teams their roles grant them permission for, with the corresponding team permissions for those roles.

You can also further restrict roles to specific projects within teams, by expanding the entry for selected teams.

![Restricting an organisation role to certain projects within selected teams in the Northflank application](https://assets.northflank.com/documentation/v1/application/secure/use-role-based-access-control/organisation-roles-project-restrictions.png)

### Team permissions

You can configure the permissions that the role grants users to manage team configuration and resources, such as team members, domains, and cloud provider integrations.

### Project permissions

You can configure the project-level permissions that users with this role have, which will apply in the teams that the role has access to. This allows you to manage project permissions on the organisational level, rather than through individual team roles.

## Next steps

- [Create a team and invite members: Create a team and invite members to collaborate on projects.](/v1/application/collaborate/create-a-team)
- [Grant API access: Create API roles to grant access to the Northflank API, with granular permissions.](/v1/application/secure/grant-api-access)
