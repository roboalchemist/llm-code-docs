# Source: https://docs.carv.io/d.a.t.a.-ai-framework/getting-started/d.a.t.a-framework-plugin-for-eliza.md

# D.A.T.A Framework Plugin for Eliza

## **Getting Started with the D.A.T.A Framework Plugin for Eliza**

The **D.A.T.A Framework** currently is designed as a plugin for the **Eliza AI framework**, providing AI agents with the ability to interact with both **on-chain** and **off-chain data** seamlessly. By integrating the D.A.T.A plugin into Eliza, developers can enhance their agents with real-time data-driven decision-making capabilities, including intelligent on-chain actions, cross-chain insights, and off-chain context.

Here’s a guide to get you started with setting up and using the **D.A.T.A Framework** plugin within Eliza.

***

#### **1. Installing the D.A.T.A Plugin**

To begin using the D.A.T.A Framework in your Eliza-powered AI agent, you first need to install the **D.A.T.A plugin**.

**Installation Steps**:

1. **Install the D.A.T.A Plugin**: Run the following command to install the plugin in your Eliza project:

   ```bash
   pnpm install @elizaos/plugin-d.a.t.a
   ```
2. **Import the Plugin**: In your agent’s code, you will need to import the D.A.T.A plugin to enable its functionality.

   ```javascript
   import { onchainDataPlugin } from "@elizaos/plugin-d.a.t.a";
   ```

***

#### **2. Configuring the D.A.T.A Plugin in Eliza**

Once the D.A.T.A plugin is installed, you can configure it within the **AgentRuntime**. The plugin will be conditionally injected based on the availability of necessary credentials (e.g., API keys).

**Basic Setup Example**:

```javascript
javascriptCopy codereturn new AgentRuntime({
    databaseAdapter: db,
    token,
    modelProvider: character.modelProvider,
    evaluators: [],
    character,
    plugins: [
        getSecret(character, "D_A_T_A_API_KEY") ? onchainDataPlugin : null,  // Conditionally add D.A.T.A plugin
        bootstrapPlugin,
        // Other plugins
    ].filter(Boolean),
    providers: [],
    actions: [],
    services: [],
    managers: [],
    cacheManager: cache,
    fetch: logFetch,
});
```

* **`onchainDataPlugin`** is added only if the **D.A.T.A API key** (`D_A_T_A_API_KEY`) is provided in the environment.
* The plugin is integrated into the **plugins array** and executed along with other necessary plugins like `bootstrapPlugin` and `confluxPlugin`.

***

#### **3. Using the D.A.T.A Plugin in Your AI Agent**

Once the D.A.T.A plugin is integrated, the plugin will enhance your Eliza agents with the following capabilities:

* **Providers**: Fetch on-chain and off-chain data (e.g., blockchain activity, wallet balances, user tags, etc.).
* **Evaluators**: Analyze fetched data and add actionable insights, such as detecting whales, traders, or identifying suspicious activity.
* **Actions**: Trigger actions based on insights—like sending alerts or executing on-chain transactions (e.g., airdrops or transfers).<br>

For more details you can check <https://github.com/carv-protocol/eliza-d.a.t.a>.
