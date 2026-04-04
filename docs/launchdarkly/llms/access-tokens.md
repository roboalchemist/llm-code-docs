# Source: https://launchdarkly.com/docs/api/access-tokens.md

The access tokens API allows you to list, create, modify, and delete access tokens programmatically.

When using access tokens to manage access tokens, the following restrictions apply:
- Personal tokens can see all service tokens and other personal tokens created by the same team member. If the personal token has the "Admin" role, it may also see other member's personal tokens. To learn more, read [Personal tokens](https://launchdarkly.com/docs/home/account/api#personal-tokens).
- Service tokens can see all service tokens. If the token has the "Admin" role, it may also see all personal tokens. To learn more, read  [Service tokens](https://launchdarkly.com/docs/home/account/api#service-tokens).
- Tokens can only manage other tokens, including themselves, if they have "Admin" role or explicit permission via a custom role. To learn more, read [Personal access token actions](https://launchdarkly.com/docs/home/team/role-actions#personal-access-token-actions).

Several of the endpoints in the access tokens API require an access token ID. The access token ID is returned as part of the [Create access token](https://launchdarkly.com/docs/api/access-tokens/post-token) and [List access tokens](https://launchdarkly.com/docs/api/access-tokens/get-tokens) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.

To learn more about access tokens, read [API access tokens](https://launchdarkly.com/docs/home/account/api).
