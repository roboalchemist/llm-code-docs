# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/grafana-loki.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Grafana Loki Logs

> Forward env zero deployment and audit logs to Grafana Loki for log aggregation and querying

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/grafana_loki.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=d1570203237223d3517e2b0c875fae20" alt="" width="500" height="500" data-path="images/guides/integrations/logs-forwarding/grafana_loki.png" />

[Grafana Loki](https://grafana.com/oss/loki/) is a log aggregation system designed to store and query logs from all your applications and infrastructure.\
env zero has the ability to send all of your deployment logs and audit logs directly to Grafana Loki.

## Setup

In order to set up Granfana Loki you will need to get the following data:

1. The Host URL
2. Authorization username and password

### Grafana Cloud

If you're using Grafana Cloud follow these steps to get the relevant data:

1. On the left side menu, go to the `Connections` tab
2. Search for `Hosted logs` and click on it.
3. In the `Configuration Details` tab under the `Configure promtail to send logs to your Grafana Cloud` section create a new `Access Policy token`
4. In the YAML section see the `url` under the `client` section
5. The URL consists of `https://{Number}:{Token}@{URL}`
6. The number is the `ENV0_LOKI_USERNAME` you will need to enter below in the environment variables section - for example: `875656`
7. The token is the `ENV0_LOKI_PASSWORD` you will need to enter below in the environment variables section.
8. The URL should be the `ENV0_LOKI_HOST` - Make sure you only take the Host part, and make sure you add an `https://` at the beginning. For example, a valid URL is `https://logs-prod-006.grafana.net>`

### Self Installation of Grafana

1. The URL should be the URL where `Loki` is deployed e.g `http://localhost:3100`
2. The username and password of the Loki server if it requires basic authentication.

There are two ways to configure the integrations:

1. ### In the env zero app

In the organization's integrations page, click on Grafana Loki and fill the form's fields:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/9adf6e33f08c2a0ed33e0ce43763014b588c7e2673a6ff0ea7eb5dcae7d5f0a6-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=bacd2efee18e23b2ec46f4275acc3d4a" alt="Log forwarding integration configuration form showing setup fields" width="1120" height="878" data-path="images/guides/integrations/logs-forwarding/9adf6e33f08c2a0ed33e0ce43763014b588c7e2673a6ff0ea7eb5dcae7d5f0a6-image.png" />
</Frame>

1. ### Using environment variables

   In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them:

   | Environment variable name | Description                                                                                                                                                              | Mandatory |
   | :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
   | `ENV0_LOKI_HOST`          | The URL where Loki is located - Should start with `http`or `https`and should not contain the full URL, just the domain. For example: `https://logs-prod-006.grafana.net` | Yes       |
   | `ENV0_LOKI_USERNAME`      | The Username for authentication                                                                                                                                          | No        |
   | `ENV0_LOKI_PASSWORD`      | The Password for authentication                                                                                                                                          | No        |

<Info>
  **Labels**

  By default we are adding a label called `app` with a value of `env0`
</Info>

Built with [Mintlify](https://mintlify.com).
