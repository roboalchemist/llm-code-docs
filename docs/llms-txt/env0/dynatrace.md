# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/dynatrace.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynatrace Logs

> Forward env zero deployment and audit logs to Dynatrace for unified observability and security

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/bec0c85b135e27cdb63a32fd8c0376bbcb71acc9959bf1a8288e77b76310ee30-dynatrace_logo_color_positive_horizontal.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=c9fe07e33943c9741638d18c4ccc6554" alt="" width="2048" height="364" data-path="images/guides/integrations/logs-forwarding/bec0c85b135e27cdb63a32fd8c0376bbcb71acc9959bf1a8288e77b76310ee30-dynatrace_logo_color_positive_horizontal.png" />

[Dynatrace](https://www.dynatrace.com) is a unified observability and security platform that allows to simplify cloud complexity and innovate faster and more securely with the only analytics and automation platform powered by causal AI.

## Setup

Here are the steps to configure it:

1. [Create](https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication#dynatrace-api-tokens-and-authentication) a API token with an `Ingest logs` scope.
2. In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them:

| Environment variable name     | Description                                                                                                                                                                                                    | Mandatory              |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| `ENV0_DYNATRACE_HOST`         | Dynatrace host url - example: `fig29962.live.dynatrace.com`                                                                                                                                                    | Yes                    |
| `ENV0_DYNATRACE_TOKEN`        | The API token you created - read more about it [here](https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication#dynatrace-api-tokens-and-authentication) | Yes                    |
| `ENV0_DYNATRACE_SERVICE_NAME` | Logs will be added with a field called `serviceName` with this value                                                                                                                                           | No - Default: **env0** |

Built with [Mintlify](https://mintlify.com).
