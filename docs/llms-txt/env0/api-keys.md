# Source: https://docs.envzero.com/guides/collaborate-securely/collaboration-and-dev-tools/command-line-and-api-access/api-keys.md

# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/api-keys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User API Keys

> Create and manage API keys for programmatic access to the env zero platform and Terraform provider

As an organization admin, it is possible to create API keys that can use env zero without interacting with the UI. for example, you can use our [API](/api-reference/getting-started/authentication) directly, work with our [Terraform Provider](https://github.com/env0/terraform-provider-env0) or use our [Private Module Registry](/guides/admin-guide/private-registry/modules).

<Warning>
  Deleting an API key

  When deleting an API key it might take up to 1 hour for it to be complety expire.
</Warning>

## How to create an API key

From *Organization Settings*  navigate to *API Keys* tab:

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/55ece3b-screen_shot_2022-05-24_at_12.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=2e548de9416493175553bd64d5d19f8f" alt="" width="1695" height="864" data-path="images/guides/admin-guide/user-role-and-team-management/55ece3b-screen_shot_2022-05-24_at_12.png" />

Click the + button to see the create API key modal.\
By default, the role of the key will be Admin, but you can also assign it to a user role, and provide specific project permission (just like when inviting a new user to the platform):

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/87bb66d-screen_shot_2022-05-24_at_16.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=90da1989fdd6978e5cf46d3974dfa1a3" alt="" width="1028" height="650" data-path="images/guides/admin-guide/user-role-and-team-management/87bb66d-screen_shot_2022-05-24_at_16.png" />

## Admin API Key

With an admin API key, you can perform any request that requires admin permission: changing organization settings, deploying and approving environments, etc.\
You can check our full API [here](https://developer.env0.com/docs/api/b2d4626c51e6b-env0-api).

## Non-Admin API Key

With a non-admin (User) API key, you can provide members of your team with the ability to use our API, while maintaining your organization's RBAC.\
When creating a user API key, it can be configured with specific project permissions, assigned to a team, and treated like any other user in the system.

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/ff6e406-screen_shot_2022-05-24_at_18.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=9da1519619c2080840902fe28290fb99" alt="" width="2250" height="1160" data-path="images/guides/admin-guide/user-role-and-team-management/ff6e406-screen_shot_2022-05-24_at_18.png" />

## Personal API Key

With a personal API key, members of your team can be provided with the ability to use our API with the same permissions they have configured in their env zero account.

Every user can generate a personal API key, you can read more about it in our [API docs](/api-reference/credentials/create-api-key).

Built with [Mintlify](https://mintlify.com).
