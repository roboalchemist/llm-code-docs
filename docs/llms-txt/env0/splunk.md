# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/splunk.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Splunk Logs

> Send env zero deployment and audit logs to Splunk using the HTTP Event Collector integration

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/638.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=50b4cc2e818dc565baa644eb6cb1202d" alt="" width="638" height="193" data-path="images/guides/integrations/logs-forwarding/638.png" />

Splunk is one of the most popular data platforms for searching, analyzing, visualizing and acting on your data.\
env zero has the ability to send all of your deployment logs and audit logs directly to your Splunk account.

## Setup

Here are the steps to configure it:

1. The integration with Splunk uses the HTTP Event Collector, so you will need to set up it in your Splunk instance:

* For Splunk Enterprise follow [this guide](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector)
* For Splunk Cloud follow [this guide](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Cloud_Platform)

1. While creating a new HTTP Event Collector you will also create a token. Make sure the token has access to the [index](https://docs.splunk.com/Splexicon:Index) you would like to use. You will need this token to configure the integration inside the env zero platform.
2. By default, env zero uses an index called `env0-deployment-logs-index` for deployment logs and an index called `env0-audit-logs-index` for audit logs.\
   To create an index for audit logs follow [this guide](https://docs.splunk.com/Documentation/SplunkCloud/latest/Admin/ManageIndexes). The deployment logs' index name can be it can be overridden. Either create the `env0-deployment-logs-index` index, or use an existing index.
3. By default env zero will use `sourcetype: env0-sourcetype`, `source: env0-deployment-logs-source` for deployment logs and `source: env0-audit-logs-source` for audit logs - this can not be overridden.
4. There are two ways to configure the integrations:

   1. ### In the env zero app

      In the organization's integrations page, click on Splunk and fill the form's fields:
      <Frame>
        <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/f37c483b6c0336497f5e07ee04ede2aec089ac6a2fe57c97a6604edab4312112-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=9f0396206b621fc3e0d9614fa47cb13c" alt="Splunk integration configuration form showing fields for Splunk setup in env0 organization" width="1120" height="1152" data-path="images/guides/integrations/logs-forwarding/f37c483b6c0336497f5e07ee04ede2aec089ac6a2fe57c97a6604edab4312112-image.png" />
      </Frame>

   2. ### Using environment variables

      In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them:

      | Environment variable name | Description                                                                                                                                                                                                                                                                                           | Mandatory                                  |
      | :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
      | `ENV0_SPLUNK_URL`         | [The URL of your Splunk instance](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#Send_data_to_HTTP_Event_Collector_on_Splunk_Cloud_Platform) in the following format: `<protocol>://<instance url/ip>:<port>`. For example: `https://example.splunkcloud.com:8088` | Yes                                        |
      | `ENV0_SPLUNK_TOKEN`       | The HTTP Event Collector token value. This is usually a GUID format token. For example: `a90c7a14-8aac-4523-bbbb-dea20352aa4d`                                                                                                                                                                        | Yes                                        |
      | `ENV0_SPLUNK_INDEX`       | The index you would like env zero to push the data to.                                                                                                                                                                                                                                                | No - Default: `env0-deployment-logs-index` |

      \*These environment variables can only override deployment logs forwarding configuration

Built with [Mintlify](https://mintlify.com).
