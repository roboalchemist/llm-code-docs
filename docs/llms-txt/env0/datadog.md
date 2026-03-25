# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/datadog.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Datadog Logs

> Forward env zero deployment and audit logs to Datadog for centralized log management

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/integrations/logs-forwarding/0cb86af-datadog.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=733e1abf03463653582a2e892c9bddc9" alt="" width="945" height="283" data-path="images/guides/integrations/logs-forwarding/0cb86af-datadog.png" />

Datadog Log Management offers simple yet powerful tools for teams to transform disparate, unstructured streams of raw log data into centralized, structured datasets.\
env zero can send all of your deployment logs and audit logs directly to your Datadog account.

## Setup

Here are the steps to configure it:

1. Generate an API key in your Datadog account using [this guide](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)
2. There are two ways to configure the integrations:

   1. ### In the env zero app

      In the organization's integrations page, click on Datadog and fill the form's fields:

      <Frame>
        <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/3e1c827f291f71da4dd1021fd791b19756876d447ea67a68848bc64246e93965-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=fd617113158333ec46483694302af439" alt="Datadog integration configuration form showing fields for Datadog setup in env0 organization" width="1120" height="1152" data-path="images/guides/integrations/logs-forwarding/3e1c827f291f71da4dd1021fd791b19756876d447ea67a68848bc64246e93965-image.png" />
      </Frame>

   2. ### Using environment variables

      In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them:

      | Environment variable name | Description                                                                                                                                                                                                                                                                                                                                                | Mandatory                                        |
      | :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
      | `ENV0_DATADOG_API_KEY`    | The API key value you've created. This is for authentication against your Datadog account                                                                                                                                                                                                                                                                  | Yes                                              |
      | `ENV0_DATADOG_HOST`       | Specify a Datadog host. **You should put only the host and not the full url** Recommended hosts - `lambda-intake.logs.datadoghq.com` for US, `lambda-intake.logs.datadoghq.eu` for EU You can read more [here](https://docs.datadoghq.com/logs/log_collection/?tab=host#logging-endpoints).                                                                | Yes                                              |
      | `ENV0_DATADOG_PORT`       | Specify the port endpoint for your Datadog host. Datadog log forwarding in env0 uses TCP over TLS endpoints. If you are using the `lambda-intake.logs.datadoghq.com` or `lambda-intake.logs.datadoghq.eu` hosts, use the `443` port. You can read more [here](https://docs.datadoghq.com/logs/log_collection/?tab=host#logging-endpoints).Default: `10516` | No, but it is recommended to provide explicitly. |

env zero adds metadata according to the log type:

1. ### Audit Logs

   * `service` - `env0-audits`
   * `ddsource` - `env0-audit-logs`

2. ### Deployment Logs

   * `service` - `env0-deployments`
   * `ddsource` - `env0-deployment-logs`

Built with [Mintlify](https://mintlify.com).
