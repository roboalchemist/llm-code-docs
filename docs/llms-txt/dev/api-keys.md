# Source: https://dev.writer.com/api-reference/api-keys.md

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

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **API Keys** in the navigation menu. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=23be0594b7deaa8ac370e127772dd8e0" alt="" data-og-width="442" width="442" data-og-height="626" height="626" data-path="images/api/select-api-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c88f7a22b6abfac0ef61c50c39f94b6b 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=006fcf4047adb0c945a3451ccdc0556f 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7f5aee322948820bee554a15bf783fa7 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f79a1f28a3bd065c3a3854fc559f1d2d 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=0c79a2ebc12f55be894a88182df0bb4f 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/select-api-keys.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=42ac805a843c095506c35c236d1ba0e0 2500w" />
2. Click the **Create API agent** button in the top right corner of the page. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d7db42a5e42ec2b01bf096b4f50bb932" alt="" data-og-width="494" width="494" data-og-height="134" height="134" data-path="images/api/create-api-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e312e9748f45d6d3237af714dfd1ad6a 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=83bb18a636e355b2869d7b06968c7e47 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=8b57beeba59fd30968dc2b59c4c5bfb5 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=0fed2a886091403438deaf2bd7ed4452 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=618f819d9cebd7d4cec269ab7519c3a1 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/create-api-agent.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e63e61559077b2e555251de6480e2347 2500w" />
3. Click the agent's name to rename it to something descriptive, and provide a **short description** of your agent to help you keep track of what it does. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=824cea2266ac8e6f9d694ee9d9d329b0" alt="" data-og-width="866" width="866" data-og-height="534" height="534" data-path="images/api/rename-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=78d3d98187db5806c4715e3a3546bbe3 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=44ecd07ca5e14a963280247b0d3aa115 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b3b72f86fc6076fa8ad880a94be57162 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ac0fe2dbd179bfc976aa388318442d3f 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=91eea940cee0a56efc9bf7e2ab4214cf 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/rename-agent.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=0e3d67a920ff93aa1037bfd67f69f3f8 2500w" />

## Create an API key

Each API agent has a default API key, called `Production`. To create additional API keys:

1. Navigate to the API application. From the [AI Studio home page](https://app.writer.com/aistudio), click **API Keys** in the navigation menu.
2. Click the API agent's tile you want to generate a new key for.
3. Click **Generate a new key**. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b6d56602756da93bfd521d54c3ebae9d" alt="" data-og-width="2228" width="2228" data-og-height="332" height="332" data-path="images/api/generate-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f29aab59f38af4dc5b92d1261072d9f0 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a286ca6475f3f6925f3394da377b88cb 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5020b57202cd5ab1be69e9f0db357e73 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=bd5dda057bbdfaa6c405683c2dce4d3e 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=cfaf0bb1d99631e73bba3641cf78625c 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/generate-key.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9782a30feb59dfad2b02dde86a10b1d3 2500w" />
4. Give the key a name and click **Generate**.
5. Immediately after generating the key, copy the key and save it securely. You can't view the key again after you navigate away from this page.

<Info>
  Store the API key in a secure location, such as a `.env` file (for example, `WRITER_API_KEY=<API_KEY>`).
</Info>

## See your API agents and manage API keys

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **API Keys** in the navigation menu.
2. Click an individual agent's tile to navigate to the agent. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a55eee330942ed66f6609db0069e9f67" alt="" data-og-width="1352" width="1352" data-og-height="592" height="592" data-path="images/api/app-navigation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=6c7fb3fc7e1181d93ca45b32378e8897 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=6b89fa357a5565d273223fb4b5ccbb1c 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=65aa2388874770b03ae65716c7e3b6a1 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7905917f4f6e4602dd4d0c49a1637d19 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9656a683cb51a1d88fd0c2edd2a755dc 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/app-navigation.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=205295412afb6f0b5d708a9b7e80e578 2500w" />

You can't view the API key after creation. Copy it immediately and store it securely. To replace a lost key, generate a new key from the API agent page.

## Manage API agent permissions

API permissions are set at the agent level. To manage API agent permissions:

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **API Keys** in the navigation menu.
2. Click an individual agent's tile to navigate to the agent.
3. Under **Capabilities**, toggle to enable or turn off a specific capability for the API key. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=288b0814ca3a3b2083914cd7ad168c6f" alt="" data-og-width="2820" width="2820" data-og-height="862" height="862" data-path="images/api/enable-capability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=56dfab6dcc44a05e007716ea7b087950 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=bae3539a6df2604d117a3e1602a0009a 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e94eceedd2ce01933c14f6fe819a5140 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e8adbdd20382580e64ee393a5cb3fb06 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b0458dd104ff6d567c19a9951b9313c9 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/enable-capability.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d3bb50e31be9ec296750d0d4a7af3fe1 2500w" />
   <Info>Capabilities map to Writer API endpoints. Click **Read more** in the API Documentation column to learn more about the specific endpoints.</Info>

## Delete an API agent

To delete an API agent:

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **API Keys** in the navigation menu.
2. Click the dropdown menu (**...**) next to the agent you want to delete, and select **Delete**. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a74f28dbd62babf28e022a451819ae09" alt="" data-og-width="1406" width="1406" data-og-height="594" height="594" data-path="images/api/delete-api-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1d42f24eedb866cc34a2983dd493913f 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=4a74164bb63088cdc73475b5b8e45c1e 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c36dd785a54deeb33329366601a33855 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ec04460537ec4ae9e108584d6bfe5c76 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a77e3f560aeeeedffd02bc9eab9d3a19 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-api-agent.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f1dd12ca40109fe71347faad1faaddf7 2500w" />
3. Confirm the deletion by clicking **Delete**.

## Delete an API key

To delete an API key:

1. From the [AI Studio home page](https://app.writer.com/aistudio), click **API Keys** in the navigation menu.
2. Click an individual agent's tile to navigate to the agent.
3. Click the dropdown menu (**...**) next to the key you want to delete, and select **Revoke**. <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=6a1a152a6b5ae4dd32e07ce818f182db" alt="" data-og-width="2254" width="2254" data-og-height="460" height="460" data-path="images/api/delete-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f88640e72eef0f1ca05cfd042038e2c9 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=093f321ad67a75fbf1ccb7e5b48fde80 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b5fc4a337b173420532a4ec99171215e 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d569e247825ad6061752456908159963 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ad562c7f10cf6f4bf0ba541d7d7831e2 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/api/delete-key.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1131b5bf04d86eee5007822fab71462f 2500w" />
4. Confirm the deletion by clicking **Revoke key**.
