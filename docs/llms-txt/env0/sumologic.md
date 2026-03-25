# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/sumologic.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sumo Logic Logs

> Forward env zero deployment and audit logs to Sumo Logic for cloud monitoring and log management

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/9d59b0f-sumologic_logo_sumoblue_rgb-1.gif?s=23dd6cc715bb72dc9e36edc93f447bb3" alt="" width="676" height="238" data-path="images/guides/integrations/logs-forwarding/9d59b0f-sumologic_logo_sumoblue_rgb-1.gif" />

Sumo Logic provides best-in-class cloud monitoring, log management, Cloud SIEM tools, and real-time insights for web and SaaS-based apps. env zero has the ability to send all of your deployment logs and audit logs directly to your Sumo Logic account.

## Setup

Here are the steps to configure it:

1. Generate Configure HTTP Source for Logs and Metrics using [this guide](https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/logs-metrics/)
2. There are two ways to configure the integrations:

   1. ### In the env zero app

   In the organization's integrations page, click on Sumo Logic and fill the form's fields:

   <Frame>
     <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/aef4e3032716bde6d21fafc9f26d54a6e034f6d4471ed6b277f09f3a50c0b1ad-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=6e9f91de8b96fe2299159c64fa9e4cdd" alt="Log forwarding integration configuration form showing setup fields" width="1120" height="1152" data-path="images/guides/integrations/logs-forwarding/aef4e3032716bde6d21fafc9f26d54a6e034f6d4471ed6b277f09f3a50c0b1ad-image.png" />
   </Frame>

   1. ### Using environment variables

      In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them:

      | Environment variable name | Description                                                                                                                                                               | Mandatory |
      | :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------- |
      | `ENV0_SUMOLOGIC_URL`      | The Generated unique URL is assigned to the source configured in step #1. The generated URL is a long string of letters and numbers and should be kept as sensitive data. | Yes       |

Built with [Mintlify](https://mintlify.com).
