# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/teams.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Teams

> Create and manage teams to group users and assign permissions across your env zero organization

Teams allow you to manage permissions across your env zero organization more easily by setting a role for an entire group of users as a single entity. Assigning a team's role is now available across all scopes, including organization, project, and environment levels, offering great flexibility and control.

A team belongs to a single [Organization](/guides/admin-guide/organizations). Teams are managed at the Organization Settings level, and are not shared between multiple organizations.

Teams can be synced from your identity provider's groups. With SSO, groups sync at login time. For continuous sync that doesn't depend on login events, see [SCIM Provisioning](/guides/sso-integrations/scim-provisioning).

## Creating a Team

In order to create a team, you must be an Organization Admin.

1. Go to **Organization Settings**
2. Click on the **Teams** tab.
3. Click the **Add Team** button
4. Fill in the team's `name` and `description`
5. Click **Confirm** to create the team.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/7789123-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=c08af0ba0a7cba48c005d9ab622c442f" alt="Interface screenshot showing configuration options" width="2425" height="1247" data-path="images/guides/admin-guide/7789123-image.png" />
</Frame>

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/60e7d13-screen_shot_2020-10-20_at_17.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=67455c7d216087f18d97fda4d7fc5780" alt="" width="637" height="438" data-path="images/guides/admin-guide/60e7d13-screen_shot_2020-10-20_at_17.png" />

## Managing Members

To manage team's members, go to **Organization Settings**, and then to **Teams** tab.

1. Click on the "Users" icon next to the team you would like to change.
2. You will now be redirected to the "Manage Team" page, which lets you edit the team's information, and manage the members of the team.

<Info>
  **Adding Users to a Team**

  Only existing users in the Organization may be added as team members - to add new users to your organization follow the [Users Management guide](/guides/admin-guide/user-role-and-team-management/user-management)
</Info>

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/27c92f7-screen_shot_2020-10-20_at_17.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=e50846833cf2312d4dac498d52293c36" alt="" width="1463" height="777" data-path="images/guides/admin-guide/27c92f7-screen_shot_2020-10-20_at_17.png" />

## Managing Team Access to a Project

Either an Organization Admin or a Project Admin can manage the access of members, or teams, of your organization to a project.

This role will cascade into every member of the team. See [Users & Roles](/guides/admin-guide/user-role-and-team-management/user-management/#project-users) for more information on roles.

<Warning>
  Users With Multiple Roles

  In the case a user is assigned to a project with multiple roles (such as being the member of two different teams who each have a different role), then the highest permission role for that project will take precedence.
</Warning>

To modify permissions on a project

1. Go to **Project Settings**, and then to the **Teams** tab.
2. You will see all teams for the organization, assign your desired Teams to the project by clicking the check mark and picking a role for that team from the dropdown.
3. Click on Save when you are done

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/e22dc43-screen_shot_2020-10-20_at_17.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=ebf1ef7a25ce0075c5f81e9b872925af" alt="" width="1494" height="530" data-path="images/guides/admin-guide/e22dc43-screen_shot_2020-10-20_at_17.png" />

## Next Steps

Now that you understand team management, learn how to control access with Role-Based Access Control (RBAC):

<CardGroup cols={2}>
  <Card title="Default Roles" icon="shield-check" href="/guides/admin-guide/user-role-and-team-management/default-roles">
    Learn about built-in roles and their permissions at organization, project, and environment levels
  </Card>

  <Card title="Custom Roles" icon="settings" href="/guides/admin-guide/user-role-and-team-management/custom-roles">
    Create and manage custom roles with tailored permissions
  </Card>

  <Card title="Assigning Roles" icon="user-plus" href="/guides/admin-guide/user-role-and-team-management/role-assignment">
    Step-by-step guides for assigning roles to users and teams
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
