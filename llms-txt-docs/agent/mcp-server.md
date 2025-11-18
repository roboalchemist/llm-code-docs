# Source: https://docs.agent.ai/mcp-server.md

# MCP Server

> Connect Agent.ai tools to ChatGPT, Claude, Cursor, and other AI assistants.

## **Connect Agent.ai to Your AI Assistant**

> Use your Agent.ai tools with ChatGPT, Claude, Cursor, and other MCP-compatible applications

## What is MCP?

Model Context Protocol (MCP) allows AI assistants like ChatGPT and Claude to access your Agent.ai tools, agents, and actions. Once connected, you can ask your AI assistant to use any of your Agent.ai capabilities directly in conversation.

## Connection Methods

### ✨ Secure Sign-In (Recommended)

The easiest way to connect is using our secure sign-in method. Simply add Agent.ai to your AI assistant, and you'll sign in with your Agent.ai account - no API tokens needed!

**Server URL:** `https://mcp.agent.ai/mcp`

**Benefits:**

* ✅ Most secure - just sign in with your Agent.ai account
* ✅ Works with ChatGPT, Claude, Cursor, and other modern MCP clients
* ✅ No API tokens to copy or manage
* ✅ Automatic access to all your agents and tools

***

## Setup Instructions

Choose your AI assistant below for step-by-step instructions:

<Tabs>
  <Tab title="ChatGPT">
    ### Step 1: Open ChatGPT Settings

    Click on your profile icon in ChatGPT and select **Settings** from the dropdown menu.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=aeea20bf88170321b06c13a69761029c" alt="ChatGPT Settings" data-og-width="1370" width="1370" data-og-height="1206" height="1206" data-path="images/mcp/chatgpt/chatgpt_step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=362d9b38dbf947cb8c1bc5c6ea3b36eb 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=db09d6dd1991b208740ca4876ca864da 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=45475194ceefc958e291a6a679b951d9 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d7d1bc627531adac66e3c223e7fb98b9 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=88884732296ba0576c086068dad202a9 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9cbf5fa9df48d72b42cdfb75f5a55c14 2500w" />

    ***

    ### Step 2: Navigate to Apps & Connectors

    Go to the **Apps & Connectors** section and click on **Advanced Settings** to enable Developer mode.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f596ed4105e4b861f557ef666f841509" alt="ChatGPT Apps & Connectors" data-og-width="1380" width="1380" data-og-height="1212" height="1212" data-path="images/mcp/chatgpt/chatgpt_step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=43c016cea43f701c7f6da711744843e3 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=a40b76b8bb41acff563a97bb5bca19a6 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=dd67001cd0a5607698a457c5875c8c6b 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=31804338f7475b4bb05d86746584b974 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=58e6d76d7b1f9d37a15650f5b8fcd233 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f2393d2319cd90f27cc56aa5269fb625 2500w" />

    ***

    ### Step 3: Enable Developer Mode

    Toggle on Developer mode to access connector features.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=8e67c22898eea5678497639a96ad1138" alt="ChatGPT Developer Mode" data-og-width="1366" width="1366" data-og-height="1208" height="1208" data-path="images/mcp/chatgpt/chatgpt_step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=8820396478807218486227215c455a21 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5bc3504a65c5dd0f2b39c8560f771a6a 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=7982f3d4a71b3b64f477453cc1340a27 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d0b91a06f953cb5da630899ac2b32b5f 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5106700bb474caac4e10ab627d4d4bc7 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=93d3c388e734f1a7042afd66ba296802 2500w" />

    ***

    ### Step 4: Create New Connector

    Once in Developer Mode, click **Create (new connector)** in the top right of the "Apps and Connectors" section.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=1fa51f3d12a78dc052b378535ccb9e5b" alt="ChatGPT Create Button" data-og-width="1372" width="1372" data-og-height="1214" height="1214" data-path="images/mcp/chatgpt/chatgpt_step4.0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=4b27e0ae0fbf9d96f944bd7c6bbab3c6 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=6320a6e71d98273a7ef08b71deb69405 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=efe3bd6d1be896ab1eb5f4d0665ebe96 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=be5d83453f6efd9a1c284d60f9fd28a7 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=6659d6cc04c952bc19f4398e15184b76 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f4cd24394230d949eddeb4dadd26c168 2500w" />

    Enter **Agent.ai Tools** as the name and paste this URL:

    ```
    https://mcp.agent.ai/mcp
    ```

    Select **OAuth** for authentication and click **Create**. You'll be taken to sign in with your Agent.ai account.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=cc11cb2147507caecd0f7ef047e56246" alt="ChatGPT Create Connector" data-og-width="902" width="902" data-og-height="1310" height="1310" data-path="images/mcp/chatgpt/chatgpt_step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=55f5ff181b98d1eac16459e0ea6a766e 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=4a4fb2e6e791c77a806a99c5f54fcac3 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=e4c3c038143168c173667d2a6ef3f170 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5565aa65e02f0ebf3edf80b5e6ca32d3 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=66f1ef9ba63a7ee698816b6ac1c12cea 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=0a16e4071630571a98a3993177bdf14e 2500w" />

    ***

    ### Step 5: Start Using Agent.ai

    Click the **"+"** icon in ChatGPT, select **"More"** from the dropdown, then select your Agent.ai connector.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=7cd2250cbfcbc79edc88c2ad7b0f0d66" alt="ChatGPT Use Connector" data-og-width="1360" width="1360" data-og-height="1144" height="1144" data-path="images/mcp/chatgpt/chatgpt_step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=98bc477c781ba5c93ddc04dc2885b279 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=499bc77cb2a049d139acc94e6945d763 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=debc04f58e4cf67a37be1584b3694b94 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9a9d09b7785978edf4d75aef1d476fb4 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=87637418d1f0cb495253c42c8d7e4841 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=015bccd18cbb6f2f167baaa6516b0141 2500w" />

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=54df2490eebae585594fc8681b47b35b" alt="ChatGPT Select Agent.ai" data-og-width="1394" width="1394" data-og-height="494" height="494" data-path="images/mcp/chatgpt/chatgpt_step5.1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5298c8956b0bc3342dc4591b1359158c 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=69530520a8fdc4394a8ba2b463543fd8 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=df9becb70e22a42a1f447e86c52faa89 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f92b605d67616f4f7ba0b58799d1597d 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=3e47281020b72c12e777843eedd4b9bb 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=3d67ac7eca6e34d1a3088c538332c647 2500w" />

    <Check>
      **You're all set!** All your Agent.ai tools and agents are now available in ChatGPT. Try asking ChatGPT to use one of your agents or actions!
    </Check>
  </Tab>

  <Tab title="Claude">
    ### Step 1: Open Claude Settings

    In [Claude](https://claude.ai), go to **Settings** → **Connectors** section, then click **"Add custom connector"**.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=90d4c358987bfb442bf29058179afdca" alt="Claude Settings" data-og-width="2438" width="2438" data-og-height="1778" height="1778" data-path="images/mcp/claude/claude.step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=0f197e1c82b114449df0e195b2045c2a 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9be0d9ff599ee01f2fea2fdebff66107 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=a0a206e70e481eeff4796d856c26bcb5 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=740f9477d98d0bcba89657f1b3b5fdea 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d98ff27f85caf919920dfbbb7ad01ba5 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=04a93b6e2e297c700ebe08fad75bb138 2500w" />

    ***

    ### Step 2: Enter Name and URL

    Enter **Agent.ai Tools** as the name and paste this URL:

    ```
    https://mcp.agent.ai/mcp
    ```

    Click **"Add"** and you'll be taken to sign in with your Agent.ai account.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=feb07dc34a9095ce217872890caa6b9e" alt="Claude Add Connector" data-og-width="1088" width="1088" data-og-height="926" height="926" data-path="images/mcp/claude/claude.step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=294c2959db1ba07b66f4d5b3ab75ebb5 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=109b33c8ff6b88ec021f7a8f6bdd29f3 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9127fb1aa41dc6ea58d9adc81f75e6b3 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d3242cb9cccaac0713dc11cc196fb252 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=cfc24b4848e4a163731def5dc5d79c22 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=b0ccb407afcf68dac4206eb9b2ab3031 2500w" />

    ***

    ### Step 3: Enable and Start Chatting

    Click the **Tools icon** in Claude, toggle on your Agent.ai connector, and start using your tools!

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=54f5233695248f75dc5c9cdbc7fd8d87" alt="Claude Enable and Chat" data-og-width="1438" width="1438" data-og-height="1274" height="1274" data-path="images/mcp/claude/claude.step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=b1993edf3ac32dc423b28c783e09ac59 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=da1b677dc71461e1bdebd892fad6bef9 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f1ee8ce26bc36838d20df2961806e9e4 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=3f787101dd1d20cf70e6788a805edfdf 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=48ef7c33c04b82bd2af86a0ba01a99b5 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=dca5d960a0afa22f02b4e7b0994f7e50 2500w" />

    <Check>
      **You're all set!** All your Agent.ai tools and agents are now available in Claude. Just mention your agents or ask Claude to use specific tools!
    </Check>
  </Tab>

  <Tab title="Cursor IDE">
    ### Setting Up in Cursor

    1. Open Cursor Settings
    2. Navigate to **MCP** or **Model Context Protocol** section
    3. Add a new MCP server with this configuration:

    ```json  theme={null}
    {
      "agentai": {
        "url": "https://mcp.agent.ai/mcp"
      }
    }
    ```

    4. Restart Cursor
    5. You'll be prompted to sign in with your Agent.ai account

    <Check>
      **You're all set!** Your Agent.ai tools will appear in Cursor's AI assistant features.
    </Check>
  </Tab>
</Tabs>

***

## Security & Privacy

* ✅ Secure sign-in with your Agent.ai account
* ✅ AI assistants will always ask your permission before using tools
* ✅ You can approve tools once or for the entire conversation
* ✅ All communication is encrypted

***

## Troubleshooting

### Connection Issues

**"Can't connect" or "Authentication failed"**

* Make sure you're using the correct URL: `https://mcp.agent.ai/mcp`
* Try clearing your browser cache and signing in again
* Ensure you're logged into Agent.ai in your browser

**"No tools available"**

* Make sure you're signed in to Agent.ai
* Try disconnecting and reconnecting the Agent.ai connector

**AI assistant isn't using my tools**

* Make sure you've enabled the Agent.ai connector/tools in your conversation
* Try specifically mentioning the tool or agent by name

Still having issues? Contact our support team for help.

***

## Testing Your Connection

You can test your Agent.ai MCP server using the [Cloudflare MCP Playground](https://playground.ai.cloudflare.com/):

1. Visit [https://playground.ai.cloudflare.com/](https://playground.ai.cloudflare.com/)
2. Enter your MCP server URL: `https://mcp.agent.ai/mcp`
3. Click "Connect" and sign in with your Agent.ai account
4. The playground will list all your available tools
5. Test individual tools by selecting them and providing inputs

This is a great way to verify everything is working before using it with your AI assistant.

***

<Accordion title="Legacy Connection Methods (Alternative Options)">
  ### HTTP over SSE (Legacy)

  This method uses an API token instead of signing in. It still works but is not recommended for new setups.

  **For Claude Desktop:**

  1. Get your API token from the [integrations page](https://agent.ai/user/integrations)
  2. Open Claude Desktop Settings → Developer → Edit Config
  3. Add this configuration:

  ```json  theme={null}
  {
    "mcpServers": {
      "agentai": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-sse",
          "https://mcp.agent.ai/YOUR_API_TOKEN_HERE/sse"
        ]
      }
    }
  }
  ```

  4. Replace `YOUR_API_TOKEN_HERE` with your actual API token
  5. Restart Claude Desktop

  ### Standard I/O (Legacy)

  This is the original connection method using our NPM package.

  1. Get your API token from the [integrations page](https://agent.ai/user/integrations)
  2. Open Claude Desktop Settings → Developer → Edit Config
  3. Add this configuration:

  ```json  theme={null}
  {
    "mcpServers": {
      "agentai": {
        "command": "npx",
        "args": ["-y", "@agentai/mcp-server"],
        "env": {
          "API_TOKEN": "YOUR_API_TOKEN_HERE"
        }
      }
    }
  }
  ```

  4. Replace `YOUR_API_TOKEN_HERE` with your actual API token
  5. Restart Claude Desktop

  **Troubleshooting Legacy Methods:**

  * **"Connection refused"**: Verify your API token is correct and hasn't expired
  * **"Authentication failed"**: Get a fresh token from the [integrations page](https://agent.ai/user/integrations)
  * **NPM errors**: Ensure you have Node.js installed and npx is available
</Accordion>

***

<Accordion title="For Developers & Advanced Users">
  ## Technical Details

  ### Server Configuration

  Agent.ai's MCP server implements secure authentication with automatic client registration.

  **Endpoints:**

  * MCP Server: `https://mcp.agent.ai/mcp`
  * OAuth Discovery: `https://mcp.agent.ai/.well-known/oauth-authorization-server`
  * Health Check: `https://mcp.agent.ai/health`

  ### Authentication Flow

  1. Client discovers OAuth endpoints via `.well-known/oauth-authorization-server`
  2. Client automatically registers using Dynamic Client Registration (DCR)
  3. User is redirected to authenticate with their Agent.ai account
  4. Authorization code is exchanged for an access token
  5. Client uses Bearer token for MCP requests

  ### Security Features

  * OAuth 2.1 with PKCE (Proof Key for Code Exchange)
  * JWT access tokens validated against Auth0
  * Automatic token refresh for long-lived sessions
  * Dynamic client registration (no pre-configuration needed)

  ### Available Tools

  All your Agent.ai agents and tools are automatically available through the MCP server, including:

  * Action Tools: Core Agent.ai capabilities
  * Team Agents: Shared within your organization
  * Private Agents: Your personal agents
  * Public Agents: Community agents you've added

  ### Protocol Support

  The server supports multiple MCP protocol versions:

  * 2024-11-05
  * 2025-03-26

  Version negotiation happens automatically during client initialization.

  ### Integration Example

  For custom MCP clients:

  ```javascript  theme={null}
  import { Client } from '@modelcontextprotocol/sdk/client/index.js';

  const client = new Client({
    name: 'my-mcp-client',
    version: '1.0.0',
  }, {
    capabilities: {}
  });

  // Connect with OAuth support
  await client.connect('https://mcp.agent.ai/mcp');

  // List available tools
  const tools = await client.request({
    method: 'tools/list'
  }, ListToolsResultSchema);

  // Call a tool
  const result = await client.request({
    method: 'tools/call',
    params: {
      name: 'tool-name',
      arguments: { /* tool arguments */ }
    }
  }, CallToolResultSchema);
  ```

  ### NPM Package

  The legacy NPM package is available at:
  [https://www.npmjs.com/package/@agentai/mcp-server](https://www.npmjs.com/package/@agentai/mcp-server)

  Note: New integrations should use the OAuth method instead of the NPM package.
</Accordion>

***

For additional help or to report issues, please contact our support team.
