# Source: https://docs.xano.com/xanoscript/agents.md

# Source: https://docs.xano.com/ai-tools/agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Agents

> Agents are used to perform 'fuzzy logic', or perform workflows that require intricate decision making, powered by an AI model of your choice

<Check>
  **Not looking for Agents, and just want to connect to your favorite AI models, like ChatGPT?**

  **Check out this resource instead:** [Chatbots](/building-backend-features/chatbots)
</Check>

<Info>
  **Quick Summary**

  AI agents in Xano refer to autonomous entities designed to perform tasks by leveraging artificial intelligence. Your Xano Agents can integrate with your database, APIs, tasks, and functions, as well as external systems.

  These agents can process data, make decisions, and execute actions without human intervention. AI agents in Xano can efficiently handle a variety of applications, from chatbots to data analysis tools, enhancing automation and productivity.
</Info>

<CardGroup cols={2}>
  <Card icon="youtube" horizontal href="https://www.youtube.com/watch?v=iEn20cy5LUw" img="/images/39ea4c72-image.jpeg">
    **Introduction to AI Agents**
  </Card>

  <Card icon="youtube" horizontal href="https://youtu.be/D1HtzC6yiO4" img="/images/5dd2e627-image.jpeg">
    **Tools for Agents & MCP Servers**
  </Card>
</CardGroup>

## What are Agents?

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/iEn20cy5LUw?si=v49lv5RM6x-EMyKT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

AI agents in Xano serve as integral components for building intelligent, automated systems as a part of your backend. These agents are designed to function autonomously, interacting with various elements of your app such as your APIs and database, as well as external systems, to streamline operations and enhance efficiency. AI agents can intelligently interpret inputs, process data, and deliver actionable outputs, all without the need for continuous human oversight.

Agents in Xano can leverage any of the most popular AI models once you provide an API key, such as:

* OpenAI
* Grok
* Anthropic / Claude
* Google Gemini

You can leverage the same visual builder you're used to using today to create workflows and functions that enable the agents to interact seamlessly with databases and external systems. With these foundational elements in place, AI agents can execute complex tasks, perform data analysis, or even serve as intelligent chatbots, making them versatile tools for a wide range of applications.

## Building Agents in Xano

1. From the left-hand navigation, click AI, then Agents
2. Click + Add Agent
3. Fill out the requested information

<Danger>
  Please note that **not all models support certain features** such as:

  * Structured outputs
  * Reasoning
  * Tool calls

  In addition, some models may support individual features, but not **combinations of features**, such as:

  * Structured outputs with tool calls
  * Tool calls with reasoning
</Danger>

## All Agents

<div id="agent-settings">
  <Columns cols={1}>
    <Card title="Name" icon="robot">
      Give your agent a name that describes its role or primary function.

      **Example:** `Order Processing Agent`
    </Card>

    <Card title="Description" icon="subtitles">
      Internal-only field describing what your agent does.

      **Example:** Analyzes incoming orders, decides on fulfillment priority, and triggers shipping workflows.
    </Card>

    <Card title="Agent Settings" icon="gear">
      Define dynamic inputs the Agent can accept from Function Stack workflows and reference environment variables.

      Use `{{ $args.propertyName }}` for workflow inputs and `{{ $env.variableName }}` for environment variables.
    </Card>

    <Card title="Model Host" icon="head-side-gear">
      Select the AI model host for the agent.

      **Options**

      * Anthropic (Claude)
      * OpenAI
      * Google Gemini

      Xano offers limited free Gemini credits for development.
      Choose *Xano Test Model (Free Gemini Credits)* to use them.
      Credits do not reset once used.
    </Card>

    <Card title="Max Steps" icon="arrow-down-1-9">
      Define how many steps the Agent can execute to complete its task.

      **Example:** `5`
    </Card>

    <Card title="System Prompt" icon="terminal">
      Core instructions that define your Agent's role, capabilities, and behavior.

      **Example**

      > You are a helpful AI Agent that completes tasks accurately.
      > When you need additional information to complete a task, use the available tools. Never make assumptions.
    </Card>

    <Card title="Prompt Type" icon="list">
      The type of prompt provided to the Agent.\
      Either `messages` (a list of prior conversation messages) or `prompt` (a single standard prompt).

      **Example:** `messages` or `prompt`
    </Card>

    <Card title="Prompt" icon="message">
      Additional context and instructions sent with each request.

      **Example**
      Please help the customer with their inquiry: `{{ $args.customer_message }}`.
      Their account ID is `{{ $args.account_id }}`.
    </Card>

    <Card title="Structured Outputs" icon="brackets-curly">
      Configure the Agent to return responses in a specific JSON format using your predefined schema.

      Toggle the checkbox to enable or disable.
    </Card>

    <Card title="Output Schema" icon="brackets-curly">
      Define the JSON structure for structured outputs.

      **Example keys**

      * `text`
      * `user_email`
    </Card>

    <Card title="Tags" icon="tags">
      Categories for organizing your Agents.

      **Example tags**

      * `contact`
      * `messaging`
    </Card>

    <Card title="Request History" icon="clock-rotate-left">
      Controls logging of requests to [Request History](/maintenance-monitoring-and-logging/request-history).

      **Modes**

      * **Inherit Settings:** Uses the currently defined workspace settings
      * **Disabled:** No logs recorded
      * **Enabled:** Logs requests with options for storage limits
    </Card>
  </Columns>
</div>

## Anthropic Settings

<div id="anthropic-settings">
  <Columns cols={1}>
    <Card title="API Key" icon="key">
      Your Anthropic API key.\
      Get your key <a href="https://console.anthropic.com/login?returnTo=%2F%3F">here</a>.

      **Example:** `sk-ant-apixx-xxxxxxxxx-xxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxx`
    </Card>

    <Card title="Model" icon="head-side-gear">
      The Anthropic model to use.\
      List of available models <a href="https://docs.anthropic.com/en/docs/about-claude/models/overview">here</a>.

      **Examples**

      * `claude-opus-4-1-20250805`
      * `claude-3-7-sonnet-latest`
    </Card>

    <Card title="Temperature" icon="thermometer">
      Controls randomness of the response.

      Higher values (e.g. `0.8`) make output more random;
      lower values (e.g. `0.2`) make it more focused.

      **Examples:** `0.1`, `0.9`
    </Card>

    <Card title="Send Reasoning" icon="lightbulb">
      For reasoning models, when enabled, Claude creates `thinking` content blocks showing internal reasoning before the final response.

      **Example:** Defaults to `true`
    </Card>

    <Card title="Thinking" icon="brain">
      Enables extended thinking and specifies a thinking budget.\
      More info <a href="https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#how-to-use-extended-thinking">here</a>.

      **Example JSON**

      ```json  theme={null}
      {
        "type": "enabled",
        "budget_tokens": 10000
      }
      ```
    </Card>
  </Columns>
</div>

## Google Generative AI (Gemini) Settings

<div id="gemini-settings">
  <Columns cols={1}>
    <Card title="API Key" icon="key">
      Your Gemini API key.\
      Get your key <a href="https://aistudio.google.com/app/apikey">here</a>.

      **Example:** `AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe`
    </Card>

    <Card title="Model" icon="head-side-gear">
      The Gemini model to use.\
      List of available models <a href="https://ai.google.dev/gemini-api/docs/models">here</a>.

      **Examples**

      * `gemini-2.5-pro`
      * `gemini-2.5-flash-lite`
    </Card>

    <Card title="Temperature" icon="thermometer">
      Controls randomness of the response (creativity).\
      Higher = more random, lower = more deterministic.\
      More info <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature">here</a>.

      **Examples:** `0.1`, `0.9`
    </Card>

    <Card title="Use Search Grounding" icon="google">
      Grounding with Google Search connects Gemini to real-time web content and enables verifiable sources.\
      Works with all <a href="https://ai.google.dev/gemini-api/docs/models/gemini#available-languages">available languages</a>.\
      Not all models support search grounding.\
      More info <a href="https://ai.google.dev/gemini-api/docs/google-search#supported_models">here</a>.

      **Example:** `on` or `off`
    </Card>

    <Card title="Thinking" icon="brain">
      Enables extended thinking and specifies a thinking budget.\
      More info <a href="https://ai.google.dev/gemini-api/docs/thinking">here</a>.

      **Example JSON**

      ```json  theme={null}
      {
        "thinkingBudget": 1024
      }
      ```
    </Card>
  </Columns>
</div>

## OpenAI Settings

<div id="openai-settings">
  <Columns cols={1}>
    <Card title="API Key" icon="key">
      Your OpenAI API key.\
      Get your key <a href="https://platform.openai.com/api-keys">here</a>.

      **Example:** `sk-Am1rLw7xUwGxGuBasGsNt3BlbkFjdBgBUgBBK5BuG9y6oWWB`
    </Card>

    <Card title="Model" icon="head-side-gear">
      The OpenAI model to use.\
      List of available models <a href="https://platform.openai.com/docs/models">here</a>.

      **Examples**

      * `gpt-4.1-mini`
      * `gpt-5`
    </Card>

    <Card title="Temperature" icon="thermometer">
      Controls randomness of the response.

      Higher values (e.g. `0.8`) make output more random;
      lower values (e.g. `0.2`) make it more focused.

      **Examples:** `0.1`, `0.9`
    </Card>

    <Card title="Reasoning Effort" icon="gauge">
      For <a href="https://platform.openai.com/docs/guides/reasoning">reasoning models</a>, sets how much effort the model spends thinking during generation.

      **Examples:** `low`, `medium`, `high`
    </Card>
  </Columns>
</div>

## Adding Tools to an Agent

An Agent needs tools to function — the tools are essentially single functions that the Agent can perform, such as looking up user data or cancelling a subscription.

1. From the left-hand navigation, click AI, then Tools
2. Click + Add Tool
3. Fill out the requested information

   <iframe width="560" height="315" src="https://www.youtube.com/embed/D1HtzC6yiO4?si=95TQG1XlvyeQyfoC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

   ### Using Existing Function Stacks as Tools

In the existing function stack, click the ⋮ settings icon in the upper-right corner of another function stack, and click Use As AI Tool

Choose the Agent or MCP Server you'd like to add the tool to, and give it a name. This name is what the command will be, so make sure it's understandable

A new tool will be created in your chosen destination with a function to call the function stack. Xano will not make a copy of your existing function stack; instead, it will use a Run Endpoint function and call that function stack internally. This is ideal, so you only have to maintain one function stack.

<Frame caption="A tool created from an existing API endpoint">
    <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5d3f516b-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=8ff4d5282229416c6d9a733fcdb38c13" alt="" width="1987" height="1124" data-path="images/5d3f516b-image.jpeg" />
</Frame>

Head to your tool's settings and add instructions. Instructions are important to have so the AI models and clients interacting with this tool understand how to use it.

### Creating Tools from Scratch

From the left-hand navigation menu, click Tools, then + Add Tool

Fill out the required information.

* **Name**
  * Give your tool a recognizable name. This is also the command that will be used to execute your tool.
* **Description**
  * This is an internal-only field just for you to describe the purpose of the tool.
* **Allow Connections**
  * Enable or diffsable connection to this specific tool
* **Add Tag**
  * Tag your tools for easier search across your Xano workspace
* **Authentication**
  * Determine if this tool requires an authentication token
* **Tool Instructions**
  * These instructions are what your clients will use to understand how to send requests to the tool, and what the expected result will be. Markdown format is recommended.

Build your tool's function stack. If you haven't already, make sure you're familiar with [Building with Visual Development](/building/visually)

Add the tool to an Agent or MCP Server. From the Agent or MCP Server, choose + Add Tool and select the tool you just created.

## Structured Outputs

Structured Outputs are used for providing a specific format that you need your agent to return its result as. This is especially useful when you are calling agents from other agents and want to ensure that the output from Agent 1 is clear and easy to understand for Agent 2.

You can add structured outputs to your Agent in the settings by checking the Structured Outputs checkbox, and then clicking **+ Add Output Schema** to build your output schema.

<Frame caption><img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/dfb82767-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=fdad7c67342d8359bc25d92b9c961957" alt="" width="576" height="326" data-path="images/dfb82767-image.jpeg" /></Frame>

## Example Agents

### 🤖 Customer Support Agent

**Purpose**

This Agent is designed to handle customer inquiries that don't typically need human interaction.

**Tools**

An Agent designed for this purpose might have the following tools available:

* **Get User Information**
  * Retrieves user information from the database
* **Update User Information**
  * Retrieves existing user information from the database, and updates it per a user's request, such as changing their phone number or address
* **Send Verification Code**
  * This tool could be used as a secondary security measure to verify that the request is coming from the user that the data belongs to
* **Change Subscription**
  * Based on the user's request, this could be used to stop an upcoming renewal, or cancel a subscription immediately. Because Agents excel at 'fuzzy logic' depending on certain circumstances, this could also be used for things like churn prevention — dynamically offering the user a discount to stay, for example
* **Search Documentation**
  * Calls an external API from your chosen documentation platform to search your product documentation in an attempt to solve the user's query without human intervention
* **Create Support Ticket**
  * In the case that the Agent does not have the necessary tools to solve the user's concerns, create a support ticket for human intervention

### Agent Configuration

| Parameter Name     | Purpose                                                                                                      | Example                                                                                                                                                                                                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name               | Give your agent a name that describes its role or primary function                                           | Customer Support Agent                                                                                                                                                                                                                                                                                                                          |
| Description        | Internal only field for describing what your agent does                                                      | Handles customer inquiries that don't typically need human interaction. Can retrieve user information, update accounts, send verification codes, manage subscriptions, search documentation, and escalate to human support when needed.                                                                                                         |
| Agent Settings     | Define dynamic inputs the Agent can accept from Function Stack workflows and reference environment variables | `{{ $args.customer_message }}`, `{{ $args.user_id }}`, `{{ $args.ticket_priority }}`, `{{ $env.SUPPORT_API_KEY }}`                                                                                                                                                                                                                              |
| Model Host         | Select the AI model host for the agent                                                                       | Claude Sonnet 4                                                                                                                                                                                                                                                                                                                                 |
| Max Steps          | Define how many AI requests the Agent can execute to complete a task                                         | 8                                                                                                                                                                                                                                                                                                                                               |
| System Prompt      | The core instructions that define your Agent's role, capabilities, and behavior                              | You are a helpful Customer Support Agent that resolves customer inquiries efficiently. Always verify user identity before making account changes. Use available tools to gather information and resolve issues. If you cannot resolve an issue, create a support ticket for human intervention. Be polite, professional, and solution-oriented. |
| Prompt             | Additional context and instructions sent with each request                                                   | Customer inquiry: `{{ $args.customer_message }}`. User ID: `{{ $args.user_id }}`. Account status: `{{ $args.account_status }}`. Please help resolve this customer's issue while following security protocols.                                                                                                                                   |
| Structured Outputs | Configure your Agent to return responses in JSON format using structured outputs and your predefined schema  | ✅ Enabled                                                                                                                                                                                                                                                                                                                                       |
| Output Schema      | Define the JSON structure for agent responses                                                                | response\_message, action\_taken, ticket\_created, follow\_up\_required                                                                                                                                                                                                                                                                         |
| Tags               | Categories for organizing your Agents                                                                        | customer-service, support, automation                                                                                                                                                                                                                                                                                                           |
| Request History    | Controls logging of tool requests                                                                            | Enabled: Logs requests with options for storage limits                                                                                                                                                                                                                                                                                          |


Built with [Mintlify](https://mintlify.com).