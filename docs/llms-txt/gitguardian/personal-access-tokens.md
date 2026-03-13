# Source: https://docs.gitguardian.com/api-docs/personal-access-tokens.md

# Personal access tokens

> How to create and manage personal access tokens for authenticating with the GitGuardian API and ggshield on local workstations.

## Prelude

**Personal access tokens are used to authenticate calls to the GitGuardian API**. They are intended to be used by developers on their local workstations to scan for secrets with the help of [ggshield](../ggshield-docs/getting-started.md) (in [pre-commit](../ggshield-docs/integrations/git-hooks/pre-commit.md) or [pre-push](../ggshield-docs/integrations/git-hooks/pre-push.md) git hooks).

## Creating a personal access token

1. Go to the [Personal access tokens page](https://dashboard.gitguardian.com/api/personal-access-tokens) in the API section of your workspace. Click on `Create token`
2. Name your key according to its use-case (for example `<Git Hook Name>-<Environment or Machine>`)
3. Set an expiry date for your token (in 1 week, 1 month, 3 months, 6 months, 1 year, or never). If you set an expiry date, you will receive an email to notify you 5 days before expiration.
4. Click on `Create token`

Make sure you copy the token, it will no longer be visible to you in the future.

![Personal access tokens modal](/img/api/personal_access_tokens_modal.png)

## Additional thoughts

- A user provisioning a personal access token with any data scope will allow them to **only retrieve resources following what they have access to via the UI**.
- Each user is allowed 5 personal access tokens in total.
- A personal access token is tied to the user who created it. If the user is deleted, their personal access tokens are also deleted. This is especially useful for deprovisioning purposes in a large organization.
- If you are a member of more than one workspace, you will need to specify which workspace your personal access token is attached to.

## Managing personal access tokens

In the Business plan, workspace Managers can administrate the personal access tokens issued for their GitGuardian workspace. They can view, filter, and revoke personal access tokens of all workspace members directly from the table.

![Personal access tokens table](/img/api/personal_access_tokens_table.png)
