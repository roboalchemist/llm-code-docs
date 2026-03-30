# Source: https://docs.brightdata.com/integrations/xpander-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With xpander.ai

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

[xpander.ai](https://xpander.ai/) is a Backend-as-a-Service platform for building autonomous AI agents. It is a no-code solution designed to help enterprise developers efficiently build, test, and deploy AI agents. It also comes with an open-source SDK to programmatically build and run AI agents.

## Available Bright Data Tools

<Card>
  <CardGroup cols={1}>
    <Card title="Start Data Collection Job by Dataset ID" icon="1">
      Launches a scraping job for a specified dataset using the Web Scraper APIs.
    </Card>

    <Card title="Execute Proxy Request by URL" icon="2">
      Sends an HTTP request through Bright Data’s proxy network for accessing the content of any web page.
    </Card>

    <Card title="Download Dataset Snapshot by ID" icon="3">
      Downloads a snapshot of a dataset in various formats, passing the data to the AI.
    </Card>
  </CardGroup>
</Card>

## How to Integrate Bright Data With xpander.ai

<Steps>
  <Step title="Prerequisites" stepNumber="0">
    * [xpander.ai account](https://app.xpander.ai/login)
    * [Bright Data API key](https://docs.brightdata.com/api-reference/authentication#api-key)
  </Step>

  <Step title="Create a new agent" stepNumber="1">
    1. In your [profile dashboard](https://app.xpander.ai/agents) and press the “New Agent” button to add a new agent:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=f4a1cf2098d30ba59acc70d17ea158a8" alt="Clicking the “Agents > New Agent” button" data-og-width="2048" width="2048" data-og-height="624" height="624" data-path="images/integrations/xpander-ai/new-agent-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?w=280&fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=0e1667d7405eec16be12b60f7ec8925f 280w, https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?w=560&fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=e02270cee67cceba0adb4154bbffbda3 560w, https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?w=840&fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=825de4f2d0eb6f200a3ef91c72ff5e43 840w, https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?w=1100&fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=9a6ae5337ac77de6a893ea1b5e8dc488 1100w, https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?w=1650&fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=9f3d6d74349437c5b3236e62693340f8 1650w, https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-button.png?w=2500&fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=f49044ec69a418baeddda3d0d51259d5 2500w" />
    </Frame>
  </Step>

  <Step title="Basic Configuration" stepNumber="2">
    1. Choose an appropriate name for your agent. For example, if you want to create a web scraping agent, you can call it “Web Scraper Agent”.

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/new-agent-name.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=2564305dacdb937845207cc781fb4241" alt="Calling the new agent “Web Scraper Agent”" width="3054" height="1495" data-path="images/integrations/xpander-ai/new-agent-name.png" />
    </Frame>

    2. Leave all other settings in the “General” tab as they are. The defaults are enough for a simple setup like this one. By default, xpander.ai will use [OpenAI’s GPT-4o as the LLM model](https://openai.com/index/hello-gpt-4o/).
  </Step>

  <Step title="Add Bright Data integration tools" stepNumber="3">
    1. Go to the “Tools” tab on your agent’s page, then click the “Add tools” button:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/add-tools-button.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=165b415cca37ea6cb3c1e4a33668cbb4" alt="Clicking the “Add tools” button" width="3054" height="1491" data-path="images/integrations/xpander-ai/add-tools-button.png" />
    </Frame>

    2. Search for “bright data” on the right side panel and select the Bright Data integration:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/select-bright-data-connector.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=8bbfc5ce22807e5e686c54b60126641f" alt="Selecting the Bright Data connector" width="825" height="495" data-path="images/integrations/xpander-ai/select-bright-data-connector.png" />
    </Frame>
  </Step>

  <Step title="Configure the Bright Data Connector" stepNumber="4">
    The following modal will show up:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/connector-configuration-form.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=2d098b0928d1ef723f59882d0e8e88b4" alt="Filling out the Bright Data connector configuration form" width="1176" height="1485" data-path="images/integrations/xpander-ai/connector-configuration-form.png" />
    </Frame>

    Fill it out as follows:

    | Configuration Option | Value                                          |
    | :------------------- | :--------------------------------------------- |
    | Connector name       | Bright Data Connector (or any name you prefer) |
    | Authentication mode  | API Key                                        |
    | Authentication scope | Integration user                               |
    | API Key              | \[Your Bright Data API key]                    |
    | Authentication type  | Bearer                                         |

    Once everything is filled in, press the “Save” button.
  </Step>

  <Step title="Select the Bright Data Tools" stepNumber="5">
    Now, you will be prompted to select the specific Bright Data tools you want to enable in your agent:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/select-bright-data-tools.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=5b6f85671a1d1d8324d516bfabf764cb" alt="Selecting the Bright Data tools to enable" width="790" height="657" data-path="images/integrations/xpander-ai/select-bright-data-tools.png" />
    </Frame>

    We recommend selecting all tools to unlock full web scraping capabilities. As of this writing, the available tools are:

    * **Start Data Collection Job by Dataset ID**: Launches a scraping job for a specified dataset using the [Web Scraper APIs](https://brightdata.com/products/web-scraper).
    * **Execute Proxy Request by URL**: Sends an HTTP request through [Bright Data’s proxy network](https://brightdata.com/proxy-types/) for accessing the content of any web page.
    * **Download Dataset Snapshot by ID**: Downloads a snapshot of a dataset in various formats, passing the data to the AI.
  </Step>

  <Step title="Add the Tools to Your Agent" stepNumber="6">
    Once you have selected the desired tools, click the “Add to agent” button in the bottom-right corner:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/add-to-agent-button.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=5f6a7e9b5c4638a0ca3eb9195a0afd03" alt="Clicking the “Add to agent” button" width="811" height="127" data-path="images/integrations/xpander-ai/add-to-agent-button.png" />
    </Frame>

    The “Tools” tab of your agent will now show the Bright Data connector with the tools you configured:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/configured-bright-data-tools.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=61f690bae0da0d55fb039457840cd2fb" alt="Note the configured Bright Data tools" width="1163" height="622" data-path="images/integrations/xpander-ai/configured-bright-data-tools.png" />
    </Frame>

    Notice that you can click on any tool to view or adjust its configuration.

    Fantastic! Your AI agent is now fully integrated with Bright Data tools and ready to scrape the web.
  </Step>

  <Step title="Specialize Your AI Scraping Agent" stepNumber="7">
    Now that your agent has access to the Bright Data tools for web scraping, give it a custom [system prompt](https://www.promptlayer.com/glossary/system-prompt). This tells the agent what it is and how it should operate.

    To do this, click on the “Instructions” tab and paste something like the following into the “System prompt” textarea:

    ```
    You are an AI agent capable of grounding your responses by scraping data from the web
    ```

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/agent-system-prompt.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=5f40000b2997f2a6c724176b6b6d1c58" alt="Adding a system prompt to your agent" width="1144" height="1178" data-path="images/integrations/xpander-ai/agent-system-prompt.png" />
    </Frame>

    For more specialized agents, you can also add custom rules and goals.

    Amazing! Your xpander scraping agent is ready.
  </Step>

  <Step title="View the Agent Graph" stepNumber="8">
    Click on the “Agent graph” button to view your current AI agent workflow:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/agent-graph.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=6caa0a83ed7069fd52e487f011038fdc" alt="The agent graph" width="1759" height="1161" data-path="images/integrations/xpander-ai/agent-graph.png" />
    </Frame>

    You will see a single agent with access to the three configured Bright Data tools for web scraping.

    Well done! All that is left is to test the agent and see it in action.
  </Step>

  <Step title="Send a Prompt to Your Agent" stepNumber="9">
    Go back to the “Tester Chat” tab and try out your agent with a prompt like this:

    ```
    Search for top 3 headphones under $100 and provide me info from their PDP's
    ```

    This instructs your web scraping agent to dynamically look online for the top 3 headphones priced under \$100 and retrieve information directly from their [product detail pages (PDPs)](https://www.dynamicyield.com/glossary/product-detail-page/).

    As you can imagine, a standard LLM would be able to handle this kind of task without access to dedicated scraping tools like those provided by Bright Data.

    Paste the prompt into the chat input and send it to your agent:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/ai-scraping-agent-in-action.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=4d42d4f69cb73c8a33cfd22b884b9818" alt="The AI scraping agent in action" width="1080" height="486" data-path="images/integrations/xpander-ai/ai-scraping-agent-in-action.png" />
    </Frame>
  </Step>

  <Step title="Analyze the Agent's Response" stepNumber="10">
    The agent uses the LLM and Bright Data tools to:

    1. Perform a web search and find the top 3 headphones.
    2. For each product, start a data collection job and download data from Amazon.
    3. Summarize the information into a short, accurate response, complete with real-world links to the Amazon product detail pages.
  </Step>

  <Step title="Inspect the Tool Calls" stepNumber="11">
    If you expand one of the tool sections in the interface, you will see something like this:

    <Frame>
            <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/xpander-ai/tool-call-io-details.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=61d6121ed1e7038d10f7207f1f7fec38" alt="The I/O details from a tool call" width="1657" height="1029" data-path="images/integrations/xpander-ai/tool-call-io-details.png" />
    </Frame>

    This proves that, behind the scenes, the AI agent automatically detected which Bright Data tools to use to complete the task. In detail, it called them with the right parameters to fetch fresh scraped data (in this case, directly from Amazon product pages).
  </Step>
</Steps>

Et voilà! You now have a fully functional scraping agent on xpander.ai, powered by Bright Data’s AI data infrastructure.
