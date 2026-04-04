# Source: https://io.net/docs/guides/intelligence/api-keys-and-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Keys and Secrets

> Learn how to create and manage API keys and secrets for use across io.net Intelligence, including models, agents, and integrations.

The *API Keys and Secrets* tab within IO Intelligence provides a unified interface for managing both API keys and authentication secrets used across the platform. These credentials enable secure access to IO Intelligence APIs, whether interacting with models, agent endpoints, or third-party service integrations.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=913fde9fff68ca37ec8a2181a8a30249" alt="IO Intel API Key Secrets Nav Bar" data-og-width="1988" width="1988" data-og-height="360" height="360" data-path="images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?w=280&fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=17003db342beb127c747e35ce57affb5 280w, https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?w=560&fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=a97eb15485b4e229bf55451970eaf42e 560w, https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?w=840&fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=5f5dcceda7e972681eabd9e5994ebfc3 840w, https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?w=1100&fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=2b140cec414544178ef550fa971150b8 1100w, https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?w=1650&fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=475cd8b9fe755a31caa1e22a091c68a1 1650w, https://mintcdn.com/ionet-cca8037f/wGTyiAbHLxsF2dqF/images/docs/io-intelligence/API-Keys-and-Secrets/IOIntel_APIKeySecrets_NavBar.png?w=2500&fit=max&auto=format&n=wGTyiAbHLxsF2dqF&q=85&s=987c6a6831e1897251b779de068b37c4 2500w" />
</Frame>

## Overview

IO Intelligence APIs provide programmatic access to powerful AI models and agents. Before making API requests, credentials must be configured correctly to authenticate calls. This section explains how to create, manage, and use both **API Keys** and **Secrets** in IO Intelligence.

## API Keys

### What are API Keys?

API keys are authentication credentials that allow applications to securely interact with IO Intelligence APIs. They are required when accessing model inference endpoints, agent workflows, or other programmatic services.

### Creating API Keys

Use the following steps to create a new API key within the *API Keys and Secrets* tab.

<Note>
  The API key will only be displayed once. Store it securely, as it cannot be shown again.
</Note>

<Steps>
  <Step title="Navigate to the API Keys and Secrets tab" />

  <Step title="Click Create New API Key" />

  <Step title="Fill in the New API Key Form" />

  <Step title="Confirm and Save" />
</Steps>

### Managing API Keys

In the API Keys and Secrets tab, you can manage your API keys to control access to IO Intelligence APIs and maintain secure usage over time.

* **Search:** Use the search bar to quickly locate existing API keys by name, which is especially useful when managing multiple keys.
* **Edit:** Update an API key’s name or permissions to reflect changes in how the key is used, such as limiting access or aligning it with a specific workflow.
* **Revoke:** Revoke API keys that are no longer needed to immediately disable further use and reduce security risk.
* **Expiration:** Configure or review expiration settings so API keys are automatically invalidated after a defined period.

## Secrets

### What are Secrets?

Secrets are credentials or tokens required by certain agents or integrations, especially when interacting with third-party services, for example, GitHub, Jira, Linear, or other external APIs. These secrets enable authenticated access on your behalf and must be configured securely.

### Creating Secrets

There are two ways to create a new secret, through the API Keys and Secrets tab or from within an Agent's configuration.

<Tabs>
  <Tab title="API Keys and Secrets Tab">
    To create a ***Secret*** from the API Keys and Secrets Tab, follow these steps:

    <Steps>
      <Step title="Open the API Keys and Secrets tab" />

      <Step title="Click the Add Secret button" />

      <Step title="Enter your Secret Details">
        <Tip>
          For agent-specific instructions on obtaining required secrets, open the *Secrets Management* tab in the *Agent Details* view and follow the steps outlined for that agent.
        </Tip>
      </Step>

      <Step title="Save your Secret">
        Secrets created here are stored securely and will be available for use across agents.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Agent Details View">
    If you want to configure your secret while viewing an agent, it can be created or selected directly from the *Agent Details* view by completing the steps below:

    <Steps>
      <Step title="Navigate to the Secrets Management tab" />

      <Step title="Select an Existing Secret or Select 'Add New Secret'">
        Select a secret that has already been configured in the API Keys and Secrets tab, or choose **Add New Secret**. When adding a new secret, provide a *Secret Name* and *Secret Value* in the fields provided.
      </Step>

      <Step title="Click Save">
        Secrets created here are automatically stored and will also be available in the *API Keys and Secrets* tab.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### Managing Secrets

The *API Keys and Secrets* tab provides a centralized view of all secrets created within [io.net](http://io.net) Intelligence. From here, existing secrets can be reviewed and deleted when they are no longer in use. Deleting a secret immediately removes it and prevents it from being used by any agent or integration.

## Using API Keys and Secrets

API keys must be included in the **Authorization** header of all requests to IO Intelligence APIs.

For example:

```shellscript  theme={null}
curl -X GET “https://api.intelligence.io.solutions/api/v1/models” \
  -H “Authorization: Bearer $IOINTELLIGENCE_API_KEY”
```

<Note>
  Replace `$IOINTELLIGENCE_API_KEY` with your actual API key.
</Note>

For agents requiring third-party integrations, secrets must be configured before those features can be used or tested. Once a secret is set, the agent will use it to authenticate with the external service.

## FAQs

<AccordionGroup>
  <Accordion title="How do I secure my API Key?" icon="comment-question">
    Some best practices and tips:

    * Do not share your API key publicly.
    * Use environment variables to store API keys securely.
    * Rotate your API keys periodically.
  </Accordion>

  <Accordion title="What is the difference between an API key and a secret?" icon="comment-question">
    API keys authenticate requests to io.net Intelligence APIs, while secrets authenticate access to third-party services or integrations required by certain agents.
  </Accordion>

  <Accordion title="What do I do if a secret is compromised?" icon="comment-question">
    Revoke or rotate the secret immediately from the *API Keys and Secrets* tab.
  </Accordion>

  <Accordion title="What are the rate limits for the APIs?" icon="comment-question">
    The IO Intelligence API offers different **quotas**, depending on your [io.net](http://io.net) Intelligence Payment Plan. Refer to  [IO Intelligence Payment](/guides/payment/io-intelligence-payments)  for more information.
  </Accordion>
</AccordionGroup>
