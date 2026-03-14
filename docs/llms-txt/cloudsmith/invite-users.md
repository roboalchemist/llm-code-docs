# Source: https://help.cloudsmith.io/docs/invite-users.md

# Users

You can add users (also known as "Accounts") to Cloudsmith directly via the UI, or you can use [SCIM](https://help.cloudsmith.io/edit/scim).

## Invite new users

To invite people to your organization:

1. Click on the "Accounts" Tab
2. Click the blue "Invite Users" button

<Image title="invite-users-button.png" alt={1327} align="center" width="80%" src="https://files.readme.io/cce8732ea52a7f4c9099fb779a25f8963fbacdd631fb71c648155cf47d20cd09-invite-users-button.png">
  Invite Users button
</Image>

You will then be presented with the "Invite user(s)" form:

<Image title="invite-users.png" alt={594} align="center" width="80%" border={true} src="https://files.readme.io/67b2a8ef4d084add3452112fc9a9cbf07192977f00e0f6fc8b90512fa167b26f-invite-users-form.png">
  Invite New Users form
</Image>

To invite new users, enter one (or more) complete email addresses for the user(s) you wish to invite. To save time, you can bulk invite new users however they must share the same Organization role

## Roles

When inviting users, you specify a role that all invited users will assume when they join the organization. These roles are:

| Organization Role | Description                                                                                                                                               |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owner             | Can manage organization administration and settings and have all permissions implicitly. They can manage other owners and delete the account              |
| Manager           | Can manage organization settings, teams and non-manager user roles (excluding owners), and inherit privileges from the organization and team memberships. |
| Member            | Can see other members and visible teams, and inherit privileges from teams they belong to.                                                                |
| Collaborator      | Can only see other team members and inherit privileges from teams they belong to.                                                                         |

> 📘 NOTE
>
> Owners are the "superusers" of the organization. Managers have access to organization settings, can manage the organization itself and can join teams, but managers have to join teams explicitly to get access to repositories due to the principle of least privilege.