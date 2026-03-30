# Source: https://docs.vectara.com/docs/agents/agents-quickstart

Title: Quickstart | Vectara Docs

URL Source: https://docs.vectara.com/docs/agents/agents-quickstart

Markdown Content:
This guide walks you through creating and configuring a Research Assistant agent in the Vectara Console. In just a few minutes, you will have a working agent capable of searching the web to answer questions. The Create agent wizard lets you customize an agent including its model, instructions, tools, and other advanced options.

Step 1: Create the agent and configure general settings[​](https://docs.vectara.com/docs/agents/agents-quickstart#step-1-create-the-agent-and-configure-general-settings "Direct link to Step 1: Create the agent and configure general settings")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Start by accessing the Agents section and giving your agent a clear name and description to help identify its purpose and capabilities.

1.   Navigate to **Agents** in the sidebar.
2.   Click **Add Agent**.

The General information pane appears.
3.   Add a **Name** like `Research Assistant`.
4.   Add a **Description** like `A research assistant that can search the web for current information.`![Image 1: Create agent general information](https://docs.vectara.com/img/agents/create-agent-general.png)
5.   Click **Next**.

Step 2: Select the model[​](https://docs.vectara.com/docs/agents/agents-quickstart#step-2-select-the-model "Direct link to Step 2: Select the model")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Choose the Large Language Model (LLM) that you want for your agent's reasoning. Then, configure the model parameters. We'll set the creativity level with the temperature parameter.

1.   Select a **Model name** like `gpt-4o`.
2.   Set the `temperature` parameter to `0.3`.![Image 2: Create agent model selection](https://docs.vectara.com/img/agents/create-agent-model.png)

This temperature value provides more consistent results with factual accuracy and low creativity. This `0.3` value is like a _sweet spot_ for many use cases involving Q&As, research assistants, and technical outputs. 3. Click **Next** to open the Instructions pane.

Step 3: Add custom instructions[​](https://docs.vectara.com/docs/agents/agents-quickstart#step-3-add-custom-instructions "Direct link to Step 3: Add custom instructions")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instructions define your agent's behavior, personality, and how it should approach queries. Custom instructions give you full control over the agent's responses. You can use our recommended instructions, or you can choose your own.

1.   Click **Use our recommended instructions**.![Image 3: Select recommended instructions](https://docs.vectara.com/img/agents/use-recommended-instructions.png)
2.   Click **Next** to move to the Tools configuration.

Step 4: Add and configure the Web Search tool[​](https://docs.vectara.com/docs/agents/agents-quickstart#step-4-add-and-configure-the-web-search-tool "Direct link to Step 4: Add and configure the Web Search tool")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tools extend your agent's capabilities beyond its base knowledge. Proper tool configuration helps the agent understand when and how to use the tool effectively.

1.   Click **Add first tool**.

![Image 4: Add first tool](https://docs.vectara.com/img/agents/create-agent-tools-1.png)
2.   Enter **Web Search** and select the tool.

![Image 5: Add web search tool](https://docs.vectara.com/img/agents/create-agent-tools-2.png)
3.   Enter **web_search** as the **Name** and provide a description for this tool like:

_The web search tool that find up to date information from trustworthy sources and returns concise summaries with links. Use when a query needs current facts external references or verification beyond internal knowledge. Prefer authoritative sites such as documentation government and academic pages and avoid low quality or speculative content._

4.   Specify a **Limit** of `10` results.

You can learn more about the other options such as query, exclude domains, and include domains in the [API Reference](https://docs.vectara.com/docs/rest-api/create-agent).

![Image 6: Configure web search tool](https://docs.vectara.com/img/agents/web-search-tool.png)
5.   Click **Next** to move to the Advanced options pane.

Metadata helps you organize and categorize agents, making them easier to find and manage as your agent library grows.

This final step of the wizard lets you add metadata to help organize your agent.

1.   Add a **Research** category and **version** like `{  "category":"Research",  "version":"1.0" }`

![Image 7: Configure web search tool](https://docs.vectara.com/img/agents/create-agent-tools-advanced.png)
With all configurations complete, you can now create your agent and test it in the Console chat interface.

2.   Click **Create agent**.

Step 6: Test the agent[​](https://docs.vectara.com/docs/agents/agents-quickstart#step-6-test-the-agent "Direct link to Step 6: Test the agent")
-----------------------------------------------------------------------------------------------------------------------------------------------

After you finish the wizard, you get a message that the agent was created successfully.

1.   The **Preview** tab opens and you can now chat with your agent.
2.   (Optional) To update the agent's configuration from the previous steps, click the **Settings** tab.
3.   Because you configured the agent with the **web_search** tool, it will be able to retrieve information from the web to answer your question. For example, try asking, "What's the weather like in Tokyo today?"

tip

If you leave this page, go back to **Agents** and select the **Research Assistant** agent from the list of created agents.

Create an agent with the API[​](https://docs.vectara.com/docs/agents/agents-quickstart#create-an-agent-with-the-api "Direct link to Create an agent with the API")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Alternatively, you can create the same agent with the Create Agent API in this [**example**](https://docs.vectara.com/docs/agents/create-agent-examples).

We also have an [**Agent API tutorial notebook**](https://github.com/vectara/example-notebooks/blob/main/notebooks/api-examples/4-agent-api.ipynb). Create a research assistant that searches academic papers and documentation, maintains conversation context, and provides cited responses.

Read on to learn about agents, how to craft custom instructions, tools in our platform, and other information.
