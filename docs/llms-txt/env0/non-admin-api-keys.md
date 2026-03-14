# Source: https://docs.envzero.com/changelogs/2022/05/non-admin-api-keys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🗝️ Non Admin API Keys

> There are many ways to interact with the env0 platform that requires an API key for authentication and authorization. Our public API, the env0 Terraform provider, and the env0 CLI. Now, With our new non-admin API key, you can provide members of your team with the ability to use API keys, while maintaining your organization's RBAC. When creating a user API key, you can then provide it with specific project permissions, assign it to a specific team, and basically treat it like any other user in the system.

There are many ways to interact with the env0 platform that requires an API key for authentication and authorization. Our public [API](https://developer.env0.com/docs/api/), env0 [Terraform provider](https://registry.terraform.io/providers/env0/env0/latest), and the env0 [CLI](https://www.npmjs.com/package/@env0/cli). Now, with our new non-admin API key, you can provide members of your team with the ability to use API keys, while maintaining your organization's RBAC. A user API key can be created with specific project permissions, assigned to a team, and basically treated like any other user in the system.

### ✨ Creating a Non Admin API Key ✨

When creating a new API key from the *Organization Settings* page, you can now choose its role. It can be either an Admin or a User. When choosing a User, the API key will behave exactly like a user in the env0 platform. As a User type, you have control of the RBAC for that API key, specific project, or specific team it belongs to. As part of a team, it will also inherit the team's RBAC.
You can [read more here](/guides/admin-guide/user-role-and-team-management/api-keys).

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/05/screen_shot_2022-05-26_at_100605.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=d50a9e60168a0ad66c97ccae5b853adc" alt="Screen Shot 2022-05-26 at 10.06.05" width="513" height="492" data-path="images/changelogs/2022/05/screen_shot_2022-05-26_at_100605.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/05/screen_shot_2022-05-26_at_101348.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=87153e27288e78a2e6de57734e35be1d" alt="Screen Shot 2022-05-26 at 10.13.48" width="891" height="715" data-path="images/changelogs/2022/05/screen_shot_2022-05-26_at_101348.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
