# Source: https://docs.tavily.com/documentation/integrations/agent-builder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Agent Builder

> Integrate OpenAI’s Agent Builder with Tavily’s MCP server to empower your AI agents with real-time web access.

## Getting Started

Before you begin, make sure you have:

* A [Tavily API key](https://app.tavily.com/home) (sign up for free if you don't have one)
* An OpenAI account with [organization verification](https://help.openai.com/en/articles/10910291-api-organization-verification)

<Step title="Create a new workflow in Agent Builder">
  Navigate to [Agent Builder](https://platform.openai.com/agent-builder) and click **Create New Workflow** to begin building your AI agent.

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=d032fb19494be5ccd0c516de7bfc1b4d" alt="Create New Workflow" width="1431" height="510" data-og-width="2542" data-og-height="1524" data-path="images/create-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=67d795b79ffe8af95b94781b4e171bfe 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=f243bd47f8e916566904f21d0d5df4b5 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=ba9864ddc063f9ef3f58d9c77b170d84 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=52fbd67d6f4c4fbbdc017020e6409695 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=fe5bbe6bac2d0b7f95b41265769417a8 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=ed84ddb72b4a33da8fe7f3b8dbf62ba5 2500w" />
</Step>

<Step title="Select the agent node in your workflow" stepNumber={2}>
  Click on the agent node in your workflow canvas to open the configuration panel.

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=5b1b592b5b703df7f85a26626c05dc4d" alt="Agent Block" width="1339" height="618" data-og-width="3018" data-og-height="1716" data-path="images/agent-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=45f215f1abf8c284ea8c270e741ea1b3 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=be5e43e63143db8acb7a15065750597d 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=5bd15c7f863307d449fc53ce49f28be6 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=b724e3f26320f5bfd77a37bdc6976e5e 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=f617aeba65eb75f638b126b65f28948e 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=169346237fda5e7b9268cf6de5b3be2e 2500w" />
</Step>

<Step title="Open the Tools configuration" stepNumber={3}>
  In the configuration panel, locate and click on **Tools** in the sidebar to add external capabilities to your agent.

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=18bf6ac9a2dda471ef124ef7f21216fc" alt="Tools Panel" width="375" height="529" data-og-width="750" data-og-height="1080" data-path="images/agent-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=7782e4dab411fcc279736f3b8895dd5d 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=087dad80f234ffef547f622a47f302e1 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=e0d2bd554ddb3a34f9803af07844868b 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=df7ee3e07a9bfebf9ada53016c30ded9 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=624eb4feb9a4345492db19d68b5e40e0 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=b0905e0b00c03abdf5390e497c845420 2500w" />
</Step>

<Step title="Connect Tavily's MCP server" stepNumber={4}>
  In the MCP configuration section, paste the Tavily MCP server URL:

  ```bash  theme={null}
  https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_API_KEY
  ```

  Remember to replace `YOUR_API_KEY` with your actual Tavily API key.

  {" "}

  <Tip>
    Need an API key? Get one instantly from your [Tavily
    dashboard](https://app.tavily.com/home)
  </Tip>

  Click **Connect** to establish the connection to Tavily.

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=2f39df29a22f845ed5d2f9bf7883d0fd" alt="Tavily MCP Configuration" width="524" height="668" data-og-width="1072" data-og-height="1428" data-path="images/tavily-mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=4581d097de536382a930b224924dc5a8 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=e9adb46882cc7a1aa83cf106eeb6d532 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=1fd82ede8766b583ac66386545cfb5f3 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=2d2d126e42caca4476a0731e71a10ef7 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=a8e6f4f9d4fe3f6ac25048975b307889 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=5076a16b287676cdaf4913f7d069fc59 2500w" />
</Step>

<Step title="Enable Tavily capabilities for your agent" stepNumber={5}>
  Once connected, you'll see Tavily's suite of tools available:

  * **tavily\_search** - Execute a search query.
  * **tavily\_extract** - Extract web page content from one or more specified URLs.
  * **tavily\_map** - Traverses websites like a graph and can explore hundreds of paths in parallel with intelligent discovery to generate comprehensive site maps.
  * **tavily\_crawl** - Traversal tool that can explore hundreds of paths in parallel with built-in extraction and intelligent discovery.

  Select the tools you want to activate for this agent, then click **Add** to integrate them.

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=d9e0d214e5b6c0d9c0ab3943289d6729" alt="Tavily Tools Available" width="522" height="566" data-og-width="1072" data-og-height="1172" data-path="images/tavily-mcp-tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=45f5ce56b89415a2d13d14c7a72905c7 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=ec93c69f5a058a557e16814fb7e8e10d 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=8a7085f7335e901d1186c5dffdee1089 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=baa5f8f8e977c0e8eae835eaee37024b 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=490957023b658a1dd831061e476690b0 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=9395faf44997c5e3bee6bfa161876f9c 2500w" />
</Step>

<Step title="Customize your agent's behavior" stepNumber={6}>
  Now configure your agent:

  * **Name**: Choose a descriptive name for your agent
  * **Instructions**: Define the agent's role and how it should use Tavily's tools
  * **Reasoning**: Set the appropriate reasoning effort level
  * Click **Preview** to test the configuration

  **Sample instructions:**

  ```
  You are a research assistant that uses Tavily to search the web for up-to-date information.
  When the user asks questions that require current information, use Tavily to find relevant and recent sources.
  ```

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=899b9db4ad2c6f8e785ef24dcdf17bbc" alt="Agent Configuration Panel" width="356" height="556" data-og-width="754" data-og-height="1164" data-path="images/agent-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=e7fabd6f8f12ff769f3292af638b88be 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=c6dc79e60f015c0400e2daa1f2ef103d 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=10364283f2a50fe29fee45df5c89447b 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=c507f50641a6a0b2f33a6134a0084d18 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=f47d3a77e950301c3ca52925d2c92cae 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=4cc8a87b7f89acd2bcbfd28e14e958c3 2500w" />
</Step>

<Step title="Verify your agent works correctly" stepNumber={7}>
  Test your agent with queries that require real-time information to verify everything is working as expected.

  <img src="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=6b2dca8e3bb276e711fd5e09b5fa5e63" alt="Agent Testing Interface" width="1672" height="746" data-og-width="3002" data-og-height="1620" data-path="images/test-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=280&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=d191fbfea2a653f1280495651d5291d4 280w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=560&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=502783869267fbbb5c40ce6722294670 560w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=20d40de348c4941ef95ad9c97f6531ad 840w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=1100&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=9e67d3989acfc8129597d447b4573d65 1100w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=1650&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=96dca0369adff8ed9c33743fa1232638 1650w, https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=2500&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=281573bd2e9c6fab227ccedc36f7578a 2500w" />
</Step>

## Real-World Applications

### Market Research Agents

Build agents that continuously monitor industry trends, competitor activities, and market sentiment by searching for and analyzing relevant business information.

### Content Curation Systems

Create agents that automatically find, extract, and summarize content from multiple sources based on your specific criteria and preferences.

### Competitive Intelligence

Develop agents that crawl competitor websites, map their content strategies, and extract pricing, features, and positioning information.

### News & Event Monitors

Build agents that track breaking news on specific topics by leveraging Tavily's news search mode, providing real-time updates with citations.
