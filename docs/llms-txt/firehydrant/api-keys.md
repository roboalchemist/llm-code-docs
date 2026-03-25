# Source: https://docs.firehydrant.com/docs/api-keys.md

# API Keys

FireHydrant allows you to access [the API](https://developers.firehydrant.com) with an API key using token-based authentication. An API key can perform actions like any other user, and by default, it will have <Glossary>Owner</Glossary> permissions.

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions to access and create API keys.

## Creating the API key

<Image alt="Generating an API key in FireHydrant" align="center" width="650px" src="https://files.readme.io/e949f86-Screenshot_2024-01-18_at_6.03.20_PM.png">
  Generating an API key in FireHydrant
</Image>

1. Go to **Settings > API Keys**.
2. Click **+ Create API key**. The next page provides fields for a name and description of the key; these fields are for your reference and do not impact how the API is used.
3. Provide the name and description and click **Save**. You will be redirected to the API keys page, where your token is displayed.

> 🚧 Note:
>
> This token will only be displayed once.

4. Copy the API key and record it somewhere safe, as it grants access to the FireHydrant API on behalf of your organization.

## Next Steps

* Learn about some of our other configurations and settings like [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls)
* See how you can store [Secrets](https://docs.firehydrant.com/docs/secrets) and use them with the [Send a Webhook](https://docs.firehydrant.com/docs/runbook-step-send-a-webhook) Runbook step
* Check out [Command Extensions](https://docs.firehydrant.com/docs/command-extensions), which are custom chatbot commands you can create to make requests to external systems manually during incidents