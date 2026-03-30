# Source: https://docs.envzero.com/guides/integrations/integrations.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# General Integrations

> Overview of env zero integrations for notifications, logs forwarding, OIDC, plugins, and more

env zero can be integrated with a variety of tools and workflows to accommodate your needs and to integrate with your current toolset and workflows.

## Notifications

Send deployment notifications to your messaging platform.\
env zero can send notifications to various tools:

* [Slack](/guides/integrations/notifications/slack)
* [Microsoft Teams](/guides/integrations/notifications/microsoft-teams)

For more details see [this](/guides/integrations/notifications)

## Logs Forwarding

env zero can forward its deployment and audit logs to the following integrations listed [here](/guides/integrations/logs-forwarding).

## OIDC Integrations

To securely manage your cloud deployments and your credentials you can use our OIDC integration. You can read more about it [here](/guides/integrations/oidc-integrations)

## Plugins

With env zero plugins, you can integrate with various tools when deploying your infrastructure as code to gain more out of the env zero platform. You can read more about it [here](/guides/integrations/plugins)

## Internal Developer Platforms (IDPs)

* [Backstage](/guides/integrations/internal-developer-platforms/backstage)

## API Reference

To integrate with your current workflows, env zero offers a full REST API. The env zero API is published [here](/api-reference/getting-started/authentication)

## CLI Tool

To integrate with your CI tools for creating and managing your IaC deployment, env zero offers a CLI tool. Written in NodeJS, you can install it via [npm](https://www.npmjs.com/package/@env0/cli).

For a detailed README, check out the [github repository](https://github.com/env0/env0-client-integrations/tree/master/node).

## env zero Terraform provider

If you wish to configure env zero using Terraform, you can do it using [our own provider](https://registry.terraform.io/providers/env0/env0/latest).\
You can also check out the [GitHub repository](https://github.com/env0/terraform-provider-env0) and the progress of that project [here](https://github.com/env0/terraform-provider-env0/projects/1).\
Feel free to open an issue, a feature request, or contribute your own PR.

Built with [Mintlify](https://mintlify.com).
