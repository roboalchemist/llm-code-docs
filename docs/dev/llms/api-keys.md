# Source: https://dev.writer.com/api-reference/api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage API keys

> Learn how to create, manage, and delete API keys.

This guide helps you create and manage API keys for the Writer API. To create and manage API keys, you must be logged in to [AI Studio](https://app.writer.com/aistudio).

## About API keys

The Writer API uses token authentication for API requests. API keys are used as tokens, which you pass in the `Authorization` header of your requests:

```
Authorization: Bearer <api-key>
```

### API agents and API keys

Writer API keys are attached to AI Studio API agents.

API permissions and scopes are set at the agent level. Within an API-based agent, you can create multiple API keys that share the permissions of the agent. To create keys with different permissions, create multiple API agents.

## Create an API agent

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **Admin Settings** in the navigation menu, then select **API Keys**. <img src="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=ed6789392b9eed8d9c936c380d661a3d" alt="" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/api/select-api-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?w=280&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=f9981c0bb0ee7b4e659389a640cfe935 280w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?w=560&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=3d568efff04fa70425e6c5b8b5d6539a 560w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?w=840&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=5a74c53bb5049b7d20f44b063dfd1881 840w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?w=1100&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=63436437b1719564f2daa5e27a4712f3 1100w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?w=1650&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=554fa2c415863c3481a12b5b2315ff92 1650w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/select-api-keys.png?w=2500&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=42437d72dfdfe29d04687fd8f999d68f 2500w" />
2. Click the **Create API agent** button in the top right corner of the page.
3. Click the agent's name to rename it to something descriptive, and provide a **short description** of your agent to help you keep track of what it does.

## Create an API key

Each API agent has a default API key, called `Production`. To create additional API keys:

1. Navigate to the API application. From the [AI Studio home page](https://app.writer.com/aistudio), click **Admin Settings** in the navigation menu, then select **API Keys**.
2. Click the API agent's tile you want to generate a new key for.
3. Click **Generate a new key**. <img src="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=08b0b31f0a321fd688dfb0080015503a" alt="" data-og-width="316" width="316" data-og-height="64" height="64" data-path="images/api/generate-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?w=280&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=9b2ca2ee38a22153369ad987689d32a4 280w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?w=560&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=6d72e6490bd44e8b0a1dade7c3f79ebd 560w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?w=840&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=988ca822e941e04de8b5dd55396d65c1 840w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?w=1100&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=b3df7913542b14b53a7629aace82a7ac 1100w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?w=1650&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=339364d8716b0c8cc0b6469403efb5da 1650w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/generate-key.png?w=2500&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=ead43489d64ddbf7cfc164f63531f39d 2500w" />
4. Give the key a name and click **Generate**.
5. Immediately after generating the key, copy the key and save it securely. You can't view the key again after you navigate away from this page.

<Info>
  Store the API key in a secure location, such as a `.env` file (for example, `WRITER_API_KEY=<API_KEY>`).
</Info>

## See your API agents and manage API keys

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **Admin Settings** in the navigation menu, then select **API Keys**.
2. Click an individual agent's tile to navigate to the agent. <img src="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=d050647bf2a0d281f8d4841b499328c6" alt="" data-og-width="2320" width="2320" data-og-height="562" height="562" data-path="images/api/app-navigation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?w=280&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=479ed6278942c2ddf9615bf19151500f 280w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?w=560&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=bac9477997184229d052524b7ff03286 560w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?w=840&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=569489a754ed770c86ecccfd72fba928 840w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?w=1100&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=0418bb85a1fa780d36b3dd27a78d448a 1100w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?w=1650&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=9340cc73efd208ba333ff2c213886594 1650w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/app-navigation.png?w=2500&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=bb9e79cb15afc354a4b3a384a1bc5261 2500w" />

You can't view the API key after creation. Copy it immediately and store it securely. To replace a lost key, generate a new key from the API agent page.

## Manage API agent permissions

API permissions are set at the agent level. To manage API agent permissions:

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **Admin Settings** in the navigation menu, then select **API Keys**.
2. Click an individual agent's tile to navigate to the agent.
3. Under **Capabilities**, toggle to enable or turn off a specific capability for the API key. <img src="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=e2fdc4f33501e1c916c95b55e10974c4" alt="" data-og-width="2760" width="2760" data-og-height="824" height="824" data-path="images/api/enable-capability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?w=280&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=dd2d3a432b62e8b2ea498a26eda2bd4e 280w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?w=560&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=120820dfe2d423d0d65a41995d0296fc 560w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?w=840&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=1ad6ac4be5a176b6c108581a55f665cd 840w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?w=1100&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=0fbb50e152ec0d2854c958275e90b5ab 1100w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?w=1650&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=69320bd3558a7d30e8891de8b49705a7 1650w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/enable-capability.png?w=2500&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=84f47329a4393d87ebbb6720564c4204 2500w" />
   <Info>Capabilities map to Writer API endpoints. Click **Read more** in the API Documentation column to learn more about the specific endpoints.</Info>

## Delete an API agent

To delete an API agent:

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **Admin Settings** in the navigation menu, then select **API Keys**.
2. Click the dropdown menu (**...**) next to the agent you want to delete, and select **Delete**. <img src="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=b9447162f65b05087684fe0892920047" alt="" data-og-width="256" width="256" data-og-height="112" height="112" data-path="images/api/delete-api-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?w=280&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=6b7c018700dfb6b7460323db7cf0daf7 280w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?w=560&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=564938b0c585ca800e96deeee9049389 560w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?w=840&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=eb036bade17d1405b5b25c45e9bb6731 840w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?w=1100&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=e66b3cb4c9f9fcdbf20e89f094fe8a0b 1100w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?w=1650&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=24cc769f4f734e4ea18ed9c41d841b39 1650w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-api-agent.png?w=2500&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=31a05050db4aaa282ecd62e0ad8fd97d 2500w" />
3. Confirm the deletion by clicking **Delete**.

## Delete an API key

To delete an API key:

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **Admin Settings** in the navigation menu, then select **API Keys**.
2. Click an individual agent's tile to navigate to the agent.
3. Click the dropdown menu (**...**) next to the key you want to delete, and select **Revoke**. <img src="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=b0816c5e2e0c87374040d1d0ea162072" alt="" data-og-width="258" width="258" data-og-height="186" height="186" data-path="images/api/delete-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?w=280&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=e49137c6d2cd68554168552f7e4cc593 280w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?w=560&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=40a51fdd0c2b1b5bf7b42a35c6dc4833 560w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?w=840&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=52bd5a7278fbf438e4042af078208f85 840w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?w=1100&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=2c5545b66666a73bf4d8a88ff647dfe0 1100w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?w=1650&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=21d70b896c7d2c487595399c31d406e3 1650w, https://mintcdn.com/writer/iFcBhFLiDWce7SgN/images/api/delete-key.png?w=2500&fit=max&auto=format&n=iFcBhFLiDWce7SgN&q=85&s=c39d689b50212796f65f934ecadd4e7b 2500w" />
4. Confirm the deletion by clicking **Revoke key**.
