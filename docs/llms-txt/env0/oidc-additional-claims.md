# Source: https://docs.envzero.com/changelogs/2022/10/oidc-additional-claims.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🖇 OIDC Additional Claims

> env0 enables easy OIDC integration by passing an environment variable named ENV0_OIDC_TOKEN to your deployments - its value contains a short lived OIDC token (JWT) for authentication via a third party application. Your authorization server could leverage our newly added claims for more secure and fine grained authorization, for example, here are a few possible verifications: Only a specific team can deploy...

env0 enables easy OIDC integration by passing an environment variable named `ENV0_OIDC_TOKEN` to your deployments - its value contains a short lived OIDC token (JWT) for authentication via a third party application.

## ✨ Improved Authorization ✨

Your authorization server could leverage our newly added claims for more secure and fine grained authorization, for example, here are a few possible verifications:

* Only a specific team can deploy to a specific environment
* A specific template can only be deployed to your `dev` / `staging` projects and not to the `production` project
* Enforce a workspace name pattern in your organization

We added the following claims to the OIDC token:

* `organizationId`
* `projectId`
* `templateId`
* `templateName`
* `environmentId`
* `environmentName`
* `workspaceName`
* `deploymentLogId`
* `deployerEmail`

Learn more about [OIDC integration](/guides/integrations/oidc-integrations).

Built with [Mintlify](https://mintlify.com).
