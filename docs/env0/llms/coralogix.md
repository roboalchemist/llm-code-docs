# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/coralogix.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Coralogix Logs

> Send env zero deployment and audit logs to your Coralogix account for real-time analysis

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/d6e7d18-coralogix.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=e77b30b604675de18dcb08dfa5fbc23d" alt="" width="600" height="315" data-path="images/guides/integrations/logs-forwarding/d6e7d18-coralogix.png" />

Coralogix is a SaaS platform that analyzes log, metric, and security data in real-time and uses machine learning to streamline delivery and maintenance processes for software providers.\
env zero has the ability to send all of your deployment logs and audit logs directly to your Coralogix account.

## Setup

For this setup, you'll need 2 things from Coralogix - an API key, and your cluster URL.

To get your API Key - follow [this documentation](https://coralogix.com/docs/user-guides/account-management/api-keys/api-keys/#send-your-data-api-keys) to obtain one. Make sure you create a "Send-Your-Data" API key.

To find out your cluster url - log into Coralogix, and note your address's top-level domain (the suffix), then - match it using the following table ([reference](https://coralogix.com/docs/integrations/coralogix-endpoints/#coralogix-rest-api-singles)):

| Coralogix Domain    | Coralogix AWS Region               | Cluster URL                 |
| :------------------ | :--------------------------------- | :-------------------------- |
| coralogix.com       | eu-west-1  \[EU1 - Ireland]        | ingress.coralogix.com       |
| coralogix.us        | us-east2  \[US1 - Ohio]            | ingress.coralogix.us        |
| coralogix.in        | ap-south1  \[AP1 - India]          | ingress.coralogix.in        |
| eu2.coralogix.com   | eu-north-1  \[EU2 - Stockholm]     | ingress.eu2.coralogix.com   |
| coralogixsg.com     | ap-southeast-1  \[AP2 - Singapore] | ingress.coralogixsg.com     |
| cx498.coralogix.com | us-west-2  \[US2 - Oregon]         | ingress.cx498.coralogix.com |
| ap3.coralogix.com   | ap-southeast-3  \[AP3 - Jakarta]   | ingress.ap3.coralogix.com   |

There are two ways to configure the integrations:

1. ### In the env zero app

In the organization's integrations page, click on Coralogix and fill the form's fields:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/3e7899fc046a1c1c3e31021f52bb82d487e6a728dedd11eb63a0a114dce3cfd0-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=8f322ccd8ad774e62ce1acb2ec74e73a" alt="Log forwarding integration configuration form showing setup fields" width="1120" height="1270" data-path="images/guides/integrations/logs-forwarding/3e7899fc046a1c1c3e31021f52bb82d487e6a728dedd11eb63a0a114dce3cfd0-image.png" />
</Frame>

1. ### Using environment variables

   In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) you would like to have them

   | Environment variable name        | Description                                                                                                                                                                                                            | Mandatory |
   | :------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
   | ENV0\_CORALOGIX\_TOKEN           | Your Coralogix private key. A unique ID that represents your company. The private key can be found under 'settings' -> 'send your logs'. It is located in the upper right corner                                       | Yes       |
   | ENV0\_CORALOGIX\_HOST            | Your cluster URL (According to the table above)                                                                                                                                                                        | Yes       |
   | ENV0\_CORALOGIX\_APP\_NAME       | The name of your environment, for example, a company named “SuperData” would probably insert the “SuperData” string parameter or if they want to debug their test environment they might insert the “SuperData– Test”. | Yes       |
   | ENV0\_CORALOGIX\_SUBSYSTEM\_NAME | Your application probably has multiple components, for example: Backend servers, Middleware, Frontend servers etc. in order to help you examine the data you need, inserting the subsystem parameter is vital.         | Yes       |

Built with [Mintlify](https://mintlify.com).
