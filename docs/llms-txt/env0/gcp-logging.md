# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/gcp-logging.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Cloud Logging

> Send env zero deployment and audit logs to Google Cloud Logging for real-time monitoring and analysis

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/2e5891d-gcp-logging.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=5977b3911686f88bb5842a6440a8fe9f" alt="" width="440" height="402" data-path="images/guides/integrations/logs-forwarding/2e5891d-gcp-logging.png" />

[Google Cloud Logging](https://cloud.google.com/logging) empowers customers to manage, analyze, monitor, and gain insights from log data in real time.\
env zero has the ability to send all of your deployment logs and audit logs directly to Google Cloud Logging.

## Setup

Here are the steps to configure it:

1. [Create](https://cloud.google.com/iam/docs/keys-create-delete) a service account with permissions to write logs '**Logs Writer**'
2. There are two ways to configure the integrations:

   1. ### In the env zero app

      In the organization's integrations page, click on Google Cloud Logging and fill the form's fields:

      <Frame>
        <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/1ee02838e32f62b710d77c9cffbda6a8aa07d4c73d0dd4692c70de32ab19808a-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=175cd594c44d6a4ab32ea118ee58ed2f" alt="Log forwarding integration configuration form showing setup fields" width="1120" height="1270" data-path="images/guides/integrations/logs-forwarding/1ee02838e32f62b710d77c9cffbda6a8aa07d4c73d0dd4692c70de32ab19808a-image.png" />
      </Frame>

   2. ### Using environment variables

      In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them:

      | Environment variable name             | Description                                                                     | Mandatory                          |
      | :------------------------------------ | :------------------------------------------------------------------------------ | :--------------------------------- |
      | `ENV0_GCP_PROJECT_ID`                 | Google cloud project id. inside this project, the logs will be stored           | Yes                                |
      | `ENV0_GCP_SERVICE_ACCOUNT_CREDENTIAL` | Service account credential file - Copy-Paste of the file payload (JSON format). | Yes                                |
      | `ENV0_GCP_LOG_NAME`                   | Logs will be stored under this log name                                         | No - Default: **env0-deployments** |

      \* These environment variables can only override deployment logs forwarding configuration

env zero sets the log name according to the log type:

1. ### Audit Logs

   * `logName` - `env0-audits`

2. ### Deployment Logs

   * `logName` - `env0-deployments`

Built with [Mintlify](https://mintlify.com).
