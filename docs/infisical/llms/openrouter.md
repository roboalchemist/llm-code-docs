# Source: https://infisical.com/docs/integrations/app-connections/openrouter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenRouter Connection

> Learn how to configure an OpenRouter (LLM router) connection for Infisical.

[OpenRouter](https://openrouter.ai/) is a unified LLM router that gives you access to hundreds of large language models through a single API. Infisical supports connecting to OpenRouter using an **API Key** (Provisioning API key). This connection is used to manage and rotate OpenRouter API keys via [Secret Rotation](/documentation/platform/secret-rotation/openrouter-api-key).

## Prerequisites

You need a **Provisioning API key** from OpenRouter. Provisioning keys are used only for key management (create, list, delete keys)—they cannot be used for model completion requests.

## Create an OpenRouter Provisioning API Key

<Steps>
  <Step title="Navigate to Provisioning Keys">
    In [OpenRouter Settings](https://openrouter.ai/settings/provisioning-keys), go to **Provisioning API Keys** and click **Create New Key**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/openrouter/step-1.png" alt="OpenRouter Provisioning Keys" />
  </Step>

  <Step title="Create and Copy Key">
    Complete the key creation flow and copy the generated Provisioning API key. Store it securely—you will use it when creating the Infisical connection.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/openrouter/step-2.png" alt="OpenRouter Key Created" />
  </Step>
</Steps>

<Tip>
  For more details on Provisioning API keys and key management, see [OpenRouter's documentation](https://openrouter.ai/docs/guides/overview/auth/provisioning-api-keys).
</Tip>

## Create OpenRouter Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, go to **Organization Settings** → **App Connections** (or the **Integrations** → **App Connections** tab in your project).

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select OpenRouter Connection">
        Click **Add Connection** and choose **OpenRouter** from the list of available connections.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/openrouter/openrouter-app-connection-option.png" alt="Select OpenRouter Connection" />
      </Step>

      <Step title="Fill out Connection Form">
        Complete the form with:

        * A **name** for the connection (e.g. `openrouter-prod`)
        * An optional **description**
        * Your **OpenRouter Provisioning API Key** (from the steps above)

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/openrouter/openrouter-app-connection-form.png" alt="OpenRouter Connection Form" />
      </Step>

      <Step title="Connection Created">
        After clicking **Create**, Infisical validates the key against OpenRouter's API. Your **OpenRouter Connection** is then ready to use for [OpenRouter API Key Secret Rotation](/documentation/platform/secret-rotation/openrouter-api-key).

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/openrouter/openrouter-app-connection-created.png" alt="OpenRouter Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    Create an OpenRouter connection via the [Create OpenRouter Connection](/api-reference/endpoints/app-connections/openrouter/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl --request POST \
      --url https://app.infisical.com/api/v1/app-connections/open-router \
      --header 'Content-Type: application/json' \
      --data '{
        "name": "my-openrouter-connection",
        "method": "api-key",
        "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
        "credentials": {
          "apiKey": "<YOUR-PROVISIONING-API-KEY>"
        }
      }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
        "id": "e5d18aca-86f7-4026-a95e-efb8aeb0d8e6",
        "name": "my-openrouter-connection",
        "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
        "description": null,
        "version": 1,
        "orgId": "6f03caa1-a5de-43ce-b127-95a145d3464c",
        "createdAt": "2025-04-23T19:46:34.831Z",
        "updatedAt": "2025-04-23T19:46:34.831Z",
        "isPlatformManagedCredentials": false,
        "credentialsHash": "...",
        "app": "open-router",
        "method": "api-key",
        "credentials": {}
      }
    }
    ```
  </Tab>
</Tabs>
