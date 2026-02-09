# Source: https://docs.upsun.com/administration/teams.md

# Administer teams


  **Feature Availability**

  This feature is available as part of the Advanced User Management add-on. You can [upgrade your organization to this add-on](https://docs.upsun.com/administration/billing/add-on-subscription.md#upgrade-to-the-advanced-user-management-add-on) in the Console.
For details about the other features included in this add-on, see the [Advanced User Management add-on](https://docs.upsun.com/administration/billing/add-on-subscription.md#advanced-user-management-add-on) help topic section; for pricing information, see the [Upsun pricing](https://upsun.com/pricing/) page.

Organizations on Upsun are made up of both [projects](https://docs.upsun.com/projects/) and [users](https://docs.upsun.com/administration/users.md).
While organizations by themselves allow you to assign project and environment type permissions to individual users on individual projects,
having many users and many projects calls for another method to group common access control settings.

**Teams** provide a grouping that connects a subset of an organization's users to another subset of that organization's projects.
That relationship enables organization owners to set default project and environment type access settings for each user and project from one place.

There is no limit to the number of teams that can be defined within a single organization.

## Create a new team

As an organization owner or member with **Manage users** permissions, 
you can create new teams.

Teams must belong to an organization, so [create one](https://docs.upsun.com/administration/organizations.md) first.
You can create new organizations with different payment methods and billing addresses
and organize your projects as you want, but keep in mind that both users and teams are restricted to single organizations.

 - Run the following command:

```bash {}
upsun team:create -o <ORGANIZATION_NAME>
```

 - Enter a team name.

 - Define your team’s project role (admin or viewer).

 - If your team has viewer rights on the project, define its role on each type of environment.

 - Enter ``Y`` to confirm.

**Note**: 

To view a list of all the existing teams in your organization, run the following command:

```bash {}
upsun team:list -o <ORGANIZATION_NAME>
```

## Delete an existing team

As an organization owner or member with **Manage users** permissions, 
you can delete existing teams.

Note that deleting teams and deleting users are not equivalent.
Deleting a team will remove member access permissions to projects described by the team,
but it will _not_ [remove users from the organization](https://docs.upsun.com/administration/users.md#remove-a-user-from-an-organization) (or your billing).

 - Run the following command:

```bash {}
upsun team:delete -o <ORGANIZATION_NAME>
```

 - Select the team you want to delete.

 - Enter ``Y`` to confirm.

## Manage team settings

As an organization owner or member with **Manage users** permissions, 
you can manage the settings of existing teams such as:

- [It's name](#team-name)
- [The environment type permissions granted to members on individual projects](#project--environment-type-permissions)
- [Team members](#team-members)
- [Project access](#team-access-to-projects)

### Team name

 - Run the following command:

```bash {}
upsun team:update -o <ORGANIZATION_NAME>
```

 - Select the team you want to rename.

 - Enter the new name.

 - Confirm or adjust the team permissions.

 - Enter ``Y`` to confirm.

### Project & environment type permissions

The primary purpose of teams is to allow organizations to quickly apply, audit, and update project and environment type permissions for groups of users. 

 - Run the following command:

```bash {}
upsun team:update -o <ORGANIZATION_NAME>
```

 - Select the team whose permissions you want to update.

 - Confirm or adjust the team name.

 - Adjust the team permissions.

 - Enter ``Y`` to confirm.

### Team members

#### Add users to a team

To join a team, a user must already have been added [to the organization](https://docs.upsun.com/administration/users.md#manage-organization-access),
where their [organization permissions](https://docs.upsun.com/administration/users.md#organization-permissions) are defined.

 - Run the following command:

```bash {}
upsun team:user:add -o <ORGANIZATION_NAME>
```

 - Select the team you want to add a user to.

 - Enter the user’s email address.

 - Enter ``Y`` to confirm.

**Note**: 

To view a list of all the users on a team, follow these steps:

 - Run the following command:

```bash {}
upsun team:user:list -o <ORGANIZATION_NAME>
```

 - Select the team whose users you want to display.

#### Remove users from a team

Note that deleting users from teams and deleting users from organizations are not equivalent.
Deleting users from a team will remove member access permissions to projects described by the team,
but it will _not_ [remove users from the organization](https://docs.upsun.com/administration/users.md#remove-a-user-from-an-organization) (or your billing).

 - Run the following command:

```bash {}
upsun team:user:delete -o <ORGANIZATION_NAME>
```

 - Select a team.

 - Select the user you want to remove from the team.

 - Enter ``Y`` to confirm.

### Team access to projects

#### Adding projects to a team's access

 - Run the following command:

```bash {}
upsun team:project:add -o <ORGANIZATION_NAME>
```

 - Select a team.

 - Select the project you want the team to access.

 - Enter ``Y`` to confirm.

**Note**: 

To view a list of all the projects added to a team, follow these steps:

 - Run the following command:

```bash {}
upsun team:project:list -o <ORGANIZATION_NAME>
```

 - Select the team whose projects you want to display.

#### Remove project from team's access

 - Run the following command:

```bash {}
upsun team:project:delete -o <ORGANIZATION_NAME>
```

 - Select a team.

 - Select the project whose access you want to revoke for the team.

 - Enter ``Y`` to confirm.


