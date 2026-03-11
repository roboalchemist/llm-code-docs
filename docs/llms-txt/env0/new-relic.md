# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/new-relic.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# New Relic Logs

> Forward env zero deployment and audit logs to New Relic using the Log API for centralized monitoring

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/dd9a513-new_relic_logo_horizontal.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=deff3c611121c1dad291e203890de728" alt="" width="3413" height="664" data-path="images/guides/integrations/logs-forwarding/dd9a513-new_relic_logo_horizontal.png" />

New Relic logs enable you to easily deploy log management with simplified log forwarding to search and correlate logs from on-prem or in-cloud sources.

## Setup

The integration with New Relic uses the Log API. Here are the steps to configure it:

1. Follow the [New Relic guide](https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/) to generate an `License-Key` which also refers to as `API-Key`
2. Choose the correct URL you would like to use:
   1. US - `https://log-api.newrelic.com`
   2. EU - `https://log-api.eu.newrelic.com`
   3. FedRamp - `https://gov-log-api.newrelic.com`
3. There are two ways to configure the integrations:

   1. ### In the env zero app

      In the organization's integrations page, click on New Relic and fill the form's fields:

      <Frame>
        <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/c0154560f044e57901f7211d63d7660148f3b82ab2bdd4cdb0e0ee7eb1293fa3-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=e6c1ab8868c7cdf96071b2a35cd69d51" alt="Log forwarding integration configuration form showing setup fields" width="1120" height="1152" data-path="images/guides/integrations/logs-forwarding/c0154560f044e57901f7211d63d7660148f3b82ab2bdd4cdb0e0ee7eb1293fa3-image.png" />
      </Frame>

   2. ### Using environment variables

      | Environment variable name | Comment                                                                                                                                                                                                                                                           | Mandatory |
      | :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
      | `ENV0_NEW_RELIC_API_URL`  | The URL you would like to get logs to. You can choose between US, EU, and Fedramp. Follow [this guide](https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/) to determine it, but make sure you only take the base URL (without the `log/v1` suffix) | Yes       |
      | `ENV0_NEW_RELIC_API_KEY`  | `License-Key`or `API-Key`- Follow [this guide](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/) to generate an API Key                                                                                                                         | Yes       |

Built with [Mintlify](https://mintlify.com).
