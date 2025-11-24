# Source: https://docs.agent.ai/user/integrations.md

# Integrations

> Manage your third-party integrations, API credentials, and MCP settings.

## Vendors

Connect third-party services like X, Google, and HubSpot to unlock agent actions powered by your own data.

From [**this page**](https://agent.ai/user/integrations#vendors), you can:

* Add, reconnect, or disconnect integrations
* Set a default account (for email or portal use)
* View agent-specific access when applicable

### **X Connection**

Connect your X (formerly Twitter) account to create a public **builder profile** and enable agents to perform X-specific actions like retrieving X accounts or posts.

* Your builder email alias will be based on your handle (e.g. [**yourhandle@agent.ai**](mailto:yourhandle@agent.ai))
* Click **Reconnect** or **Disconnect** to manage access

### **Google Connections**

Connect your Google account to enable agents to perform actions like creating Google Docs.

* Add multiple accounts and set a **default email**
* Click **Connect More Accounts** to add others
* Use **Reconnect** or **Disconnect** as needed

### **HubSpot Connections**

Connect your HubSpot portal to enable agents to perform CRM-related actions, including working with contacts and companies. You can connect to multiple HubSpot portals and:

* Set a **default portal**
* View which agents have private access to your portal
* Click **Connect More Portals** to add additional HubSpot accounts

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=2e65c0653329251f9d7a42b68ea474c1" alt="Vendors Pn" data-og-width="2764" width="2764" data-og-height="1238" height="1238" data-path="images/vendors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=f2664fca599ac591a1e177bdc9917fb8 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=051a205b4264c410082759e6a646170a 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=57d7d2c3cfd9bd73b3067de1916b20d7 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=9f58518be4e24edf47d96a5532a8c3ef 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=4607fcf44e58e6d244e467b04593eae6 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=d3ef7f5496629f5aa1dec2c9bd50f74a 2500w" />

## API

Your [API key](https://agent.ai/user/integrations#api) allows you to integrate [**Agent.ai**](http://Agent.ai) features directly into your own tools and workflows. You’ll find:

* Your **API key**
* Sample curl requests
* A link to the [**Agent.ai** API documentation](https://docs.agent.ai/welcome)

<Warning>
  Keep your API key private. It grants access to your [**Agent.ai**](http://Agent.ai) account and credit usage—treat it like a password. Don’t share it or commit it to public repositories.
</Warning>

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=2adb245de837217018a0024e7c8df61b" alt="Apiupdated Pn" data-og-width="2654" width="2654" data-og-height="1118" height="1118" data-path="images/apiupdated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=eca580cc811a4fe5e71f2846830b2d87 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=8d8ca7c01c634748b457361493503dde 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d4faa246df333349164646276cc9efaf 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=fe365d98d9165dce10ad6f4e303496ae 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3a393a547e1af5eb8cc61a06db09a920 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=e7274bc7dc7359455c1adc3967402d85 2500w" />

## MCP

Use the [MCP tab](https://agent.ai/user/integrations#mcp) to configure your [Agent.ai](http://Agent.ai) MCP server and manage which agents are available to external tools that support MCP, like Claude Desktop. You can also add additional MCP servers from this page and use [Agent.ai](http://Agent.ai) as an MCP client.

### [Agent.ai](http://Agent.ai) MCP Tools Listing Settings

Choose which agents you’d like to expose to your MCP environment:

* **Action Agents** (default)
* My Team Agents
* Private Agents
* Top Public Agents (rating > 4.2, reviews > 3)

Check the boxes you want, then click **Save**.

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=681ac51e8ce7b8a122399d065d58f4cd" alt="Mcp1updated Pn" data-og-width="2642" width="2642" data-og-height="1042" height="1042" data-path="images/mcp1updated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=03a33bd678540b9929dc8ebae7ecb0e7 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=697eb94179f1bf3bd4041310f0ae980d 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=515cf141dac3a1d91bac51e975c419ae 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ad0d5d18759362d45dbd5c49b4f91e33 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a598635a70eea9e2f9652740b1de2192 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=82b72aeeb65df30324f1b2d4d02de8cc 2500w" />

### Connection Methods

Use simple URL-based configuration to connect [Agent.ai](http://Agent.ai) to MCP clients (recommended) or use the provided config block to your MCP configuration file.

You can also add external MCP servers to use within Agent.ai (more below).

For full setup instructions, see the [**MCP Integration Guide**](https://docs.agent.ai/mcp-server).

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=dd7d1034b7941de4720773ed0e7c39a9" alt="Mcp2updated Pn" data-og-width="2650" width="2650" data-og-height="1492" height="1492" data-path="images/mcp2updated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=f5f4f66706d5f420e5d74975273850f6 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=1c04e3a71b7c1b2f61fead98ffe7d2d6 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=1d64986d976f1128ca2b4523ea770925 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3ce8982b2248b5a07eb1fdbf394deb9d 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bcae47c5a8127835661ea0529c724438 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=86f5e1e96a444702b9e38c87e927c6a6 2500w" />

## MCP Chat

After adding MCP servers to Agent.ai, you can select them and chat with them in [MCP Chat](https://agent.ai/user/integrations#mcpchat).

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=2b529b859c06a866cb9ce8ae0659a6a6" alt="Mcpchat Pn" data-og-width="2672" width="2672" data-og-height="1090" height="1090" data-path="images/mcpchat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=df07fe1f3d9c535f174d21825dedf31a 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=0ad2c261b9a76cd57d2dd0d59ab675a3 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=5e99e2a210d18a7c4b199d73a13b0fcd 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=b2c21db68ca4713a731ebfc021b2cdd1 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a9b09a4bca45bf55899d40c5a7a57c6f 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=94b9e4208633b19de79ea1551c0a5f8b 2500w" />

Reach out to our [**support team**](https://agent.ai/feedback) if you have any questions about integrations or navigating [Agent.ai](http://Agent.ai).
