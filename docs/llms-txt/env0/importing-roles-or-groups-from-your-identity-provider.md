# Source: https://docs.envzero.com/guides/sso-integrations/importing-roles-or-groups-from-your-identity-provider.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sync Roles &  Groups From Your IdP

> Sync identity provider roles and groups to env zero teams for automated access management

env zero Teams can be synced with your Identity Provider's (IdP) roles or groups.

For example, in [Okta](/guides/sso-integrations/okta-integration) , when configuring the "Group Attribute Statements", this setting will determine which groups will get synced into env zero and mapped to [env zero Teams](/guides/admin-guide/user-role-and-team-management/teams).

<Info>
  The group sync described on this page happens at login time. If you need users to be provisioned and deprovisioned continuously without waiting for them to log in, see [SCIM Provisioning](/guides/sso-integrations/scim-provisioning).
</Info>

## Teams Sync

Whenever a **user** logs in, env zero will sync the **env zero Team** based on the user's group membership. Internally, we will search one of the following fields based on the SAML response:

1. `teams`
2. `groups`

Those fields can be either an array of strings or a comma-separated string, for example:

1. `["groupA", "groupB", "groupbC"]`
2. `"groupA,groupB,groupbC"`

Whenever a **user** logs in, if the **env zero Team** already exists (we check if a team with the same name already exists), the **user** will be added as a member to the Team, and thus have the same Project Roles based on previous assignments.\
Whenever a **user** is removed from a group, their **team** membership is also updated to help reflect their membership status.

The **env zero Team** can then be assigned a [env zero Project Role](/guides/admin-guide/user-role-and-team-management/user-management/#project-roles) in the Project Settings.

<Info>
  **Teams Syncing**

  Teams will be synced each time a user logins with the following logic:

  1. env zero will create a new team if one doesn't exist based on the group name we received from the SAML provider.
  2. If the team exists in env zero we will not create a new team.
  3. We will assign the user to all the teams in env zero based on the group names he/she is part of in the SAML provider.
  4. If the user was removed from a group in the SAML provider we will remove him/her from the team in env zero.
</Info>

## Teams Filtering

If you have a lot of groups in your identity provider, and only few of them are relevant for env zero you can control which group will be synced to env zero and which is not. Please [contact us](mailto:support@env0.com) to configure this feature.

## Admin Roles

In addition, env zero can also assign specific teams as Organization Admins automatically from your SAML provider. This advanced new feature can come in handy if you have (or planning to have) such groups which contain all users that should be Organization Admins on env zero.\
You can read more about user roles in env zero [here.](/guides/admin-guide/user-role-and-team-management/user-management/#organization-roles)

Whenever the **user** logs in to env zero, we will search for the pre-configured group name of your choice, and if the user is part of that group, we will promote him to an Organization Admin.\
Whenever a **user** is removed from that specific group, he will be demoted to a regular user role in your organization.

In order to configure this feature please [contact us.](mailto:support@env0.com)

<Warning>
  Admin  Roles

  If you enabled this feature, any manual role changes you made to a user might be overridden automatically by this process.\
  The user role is only updated upon logging into env zero.
</Warning>

Built with [Mintlify](https://mintlify.com).
