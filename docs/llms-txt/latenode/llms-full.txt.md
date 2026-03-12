# Source: https://documentation.latenode.com/llms-full.txt

# Documentation

Latenode is a low-code platform that combines the simplicity of visual building with the power of JavaScript and AI.

</Cards>

# Account Settings

Some account actions are handled through support to ensure the security of your data.

## Changing Password

If you registered using email and password:

1. Log out of your account
2. On the login page, click **Forgot Password**
3. Enter your email and follow the instructions in the email

***

## Changing Email

To change the email address associated with your account, write to **[help@latenode.com](mailto:help@latenode.com)** from your current email.

Include in your message:

* Current account email
* New email you want to switch to

***

## Account Deletion

To completely delete your account and all associated data, send a request to **[help@latenode.com](mailto:help@latenode.com)**.

  Account deletion is irreversible. All scenarios, databases, integration credentials, and execution history will be permanently deleted without the possibility of recovery.

Before deleting, we recommend:

* Cancel your active subscription
* Export needed scenarios (JSON export)

# Subscription Managing

## Billing Page

When a paid plan or trial is active, the **Billing** section becomes available in your account's left menu. On this page, you can see your current plan, the number of available credits, a **Manage payments** button, and tabs for **Extra Credits**, **Boosts**, and **Plug\&Play Tokens**.

Below, you�ll find all available plans: **Micro**, **Starter**, **Grow**, and **Prime**. Each plan card displays:

* The number of included credits
* Limits on scenarios, flows, triggers, etc.
* A button to start a trial or activate the plan (if not activated before)

The current balance is also always visible in the left menu on any Latenode page:

***

## How to Activate a Subscription

1. Go to **Plans & Pricing**
2. Choose the plan you need
3. Click **Start trial (14 days)** or proceed with direct payment
4. Confirm the payment � your subscription is now active

***

## How to Cancel a Subscription

1. Click **Manage payments**



2. The Stripe interface will open

3. Find the active subscription

4. Disable auto-renew or cancel the subscription completely

Alternatively, you can cancel the subscription from the active plan menu by clicking **Cancel subscription**

***

# Usage Statistics

Access a dedicated page to:

* View data about your tariff plan.
* Analyze statistics for all executed scenarios.

## Key Information

***Each scenario consumes 1 credit every 30 seconds during its execution.***

To ensure your scenarios run smoothly, monitor your current credit balance. If there are no available credits, the scenario will not execute.

The number of available credits depends on your selected pricing plan.

  Running a single node does not require credits, enabling free scenario customization. When executing a scenario that includes a Nodul type scenario, credits will be consumed based on the execution time of the main scenario. The execution time of the Nodul scenario itself is not counted towards credit usage.

If a scenario runs for less than 30 seconds, the number of credits used will depend on your pricing plan:

* **Starter:** Minimum charge is 1 credit (30 seconds or less).
* **Grow:** Minimum charge is 0.5 credits (15 seconds or less).
* **Prime:** Minimum charge is 0.1 credits (3 seconds or less).

## Rate plans

Your current tariff plan is displayed in the right widget **(1)**. The payment day is shown just below it **(2)**:

## Understanding Credits

A **credit** is a virtual currency used by scenarios during execution. One credit equals 30 seconds of scenario execution.

The number of nodes in a scenario does not directly impact credit consumption. For example, scenarios with 10 nodes and 2 nodes, each running for less than 30 seconds, will consume only one credit during execution.

  Scenarios with many nodes generally take longer to execute than those with fewer nodes. Additionally, scenarios that transform or process large amounts of data also require more

  Consider the following example of credit consumption:

  1. Run the test scenario. In the execution history, the initial run on 07.04.24 **(1)** took eighteen seconds and performed 22 operations **(2)**:



  2. On the statistics page, review the total number of credits spent on 07.04.24 and the credits used for running the test scenario.

  * The total number of credits is sixteen **(1)**.
  * One credit was spent on the test scenario **(2)**.



  3. Run the test scenario again with an increased amount of processed data. In the execution history, the second run on 07.04.24 **(1)** took 1 minute and 24 seconds and performed 271 operations **(2)**:



  4. On the statistics page, view the updated total number of credits spent on 07.04.24 and the new credits used for running the test scenario.

  * The total number of credits is nineteen **(1)**.
  * Four credits were spent on the test scenario **(2)**.

  During the second run, three additional credits were consumed because the scenario ran for about a minute and a half.



  ## Statistics of Credit Consumption by Scenarios

  View credit consumption statistics for your scenarios by setting filters at the top of the page.

  The graph **(1)** and the table **(2)** display the scenarios executed during the specified period and the corresponding credit usage for each. The table can be sorted by scenario name or credit consumption.

  Click on a scenario name in the table to view detailed information about that scenario.



  ***

# Workspace Management

Workspace Management lets you grant an existing Latenode user access to your workspace with management permissions (excluding subscription and user management). This is designed for partners who need access to client accounts and seamless one-click switching between workspaces.

  This is not a classic invite system. You can only add a user who is already registered, activated, and has an active account (subscription, trial, or LTD).

## Access Rights

The added user can:

* View, run, edit, and delete scenarios
* Manage account structure, scenarios, and databases
* **Cannot**: change the plan, manage billing, or add/remove other users

## How to Add a User

1. Open **Workspace Management**.

2. Enter the email of another active Latenode account and click **Grant Access**.

3. The user will appear in the access list.

## Switching Between Accounts

After being added, the user will be able to switch between their own and connected accounts using the workspace switcher in the top menu.

The account you've granted access to can switch to your workspace by clicking the **account switcher menu** in the top navigation and selecting your account from the dropdown list.

## Remove access

You can remove access at any time by clicking **Remove** next to the user in the access list.

# Agent Design Foundations

## Overview

Latenode AI Agents are powered by a built-in LLM and driven by two key components you control:

* **Instructions** � define the agent�s behavior, logic, and decisions.
* **Tools** � connected nodes that the agent can call to perform actions or retrieve data.

This page explains how to design those components effectively to build reliable, task-oriented agents.

***

## How It Works

Each time the AI Agent node receives a message, it:

1. Reads the instructions.
2. Analyzes the input.
3. Decides whether to call a tool or generate a direct reply.
4. Executes the logic based on your setup.

The quality of this process depends on how clearly you structure the agent�s instructions and tools.

***

## Instructions

Instructions define how the agent should behave. They are written in plain language and describe what the agent is allowed to do, how it should react to user inputs, and how to use the available tools.

***

## Recommendations

***

* Be explicit about allowed and disallowed actions.
* Include fallback logic for missing data.
* Keep instructions focused on one scenario.
* Use simple, direct language.
* **Clearly describe each tool�s purpose** � the agent relies on these descriptions to decide which tool to call.
* **Avoid vague tool labels or descriptions** � instead of �get info�, say �fetch current weather data� or �retrieve currency exchange rate�.

  The more accurately you define what each tool does, the better the agent can reason and choose the right one for the task.

***

## Tools

Tools are the external actions the agent can take. In Latenode, these are the connected nodes � such as HTTP requests, Notion, or Google Sheets.

***

### Best Practices

* Use descriptive names: `create_invoice`, `send_email`
* Avoid connecting too many tools per agent
* Design each tool to do one task well
* Test tools separately before connecting

```
{{fromAIAgent("email"; "Customer email address")}}
```

***

# AI Agent Examples

Latenode's **AI Agent** is flexible enough to support multiple architectures: from a single dynamic assistant to modular multi-agent systems and external knowledge integration.

***

## 1. AI Agent Basic Workflow Example

A single AI Agent receives user prompts and decides which tools to use, if any. This setup is lightweight but powerful � capable of parsing, routing, and composing responses dynamically.

### Scenario Structure

* One central `AI Agent`
* Connected to:
  * `weather_tool` (e.g. wttr.in)
  * `exchangerate_tool` (e.g. exchangerate.host)
  * `web_search_tool` (e.g. factual search)
* Input from `Trigger`, output to `SetVariables`

***

### Call Example 1 � Weather + Currency

**Prompt:**

> �What�s the weather in Berlin and how much is 100 EUR in USD?�

* The agent triggers:
  * `weather_tool` with the city "Berlin"
  * `exchangerate_tool` for EUR to USD
* Skips unrelated tools

**Expected output:**

```
It's currently 17�C in Berlin. 100 EUR is about 108 USD.
```

***

### Call Example 2 � Simple Fact

**Prompt:**

> �Who is the CEO of Apple?�

* Agent skips weather and currency
* Only triggers `web_search_tool`

**Expected output:**

```
The CEO of Apple is Tim Cook.
```

?? This scenario is great for lightweight assistants that respond contextually without complex logic trees.

**?? You can copy this template here: [AI Agent Basic Workflow Example](https://app.latenode.com/templates/shared/684725a0ed2b4d6c0a7d111c)**

***

## 2. Multiagent - AI Multi-Agent Interaction Example

This approach uses a **main agent** to break down user requests and forward sub-tasks to specialized agents. Each sub-agent operates independently and can have its own API logic.

### Scenario Structure

* `main_agent` controls the overall logic
* Delegates to:
  * `weather_agent`
  * `finance_agent`
  * `web_search_tool`
* Each sub-agent is connected to dedicated APIs or logic blocks

***

### Call Example 1 � Weather + BTC

**Prompt:**

> �What�s the weather in Tokyo and what�s the BTC price?�

* `main_agent` sends:

  * Weather part > `weather_agent`
  * Bitcoin price part > `finance_agent`



**Expected output:**

```
The current weather in Tokyo is 27�C and sunny. The current price of Bitcoin (BTC) is $119,218 USD.
```

***

### Call Example 2 � CEO + HQ Weather

**Prompt:**

> �Who is the CEO of Apple and what�s the weather like at their HQ?�

* Agent parses:

  * Apple HQ location > via `web_search_tool`
  * Weather in that location > via `weather_agent`



**Expected output:**

```
The CEO of Apple is Tim Cook. He has held this position since August 2011, succeeding Steve Jobs.

As for the weather at Apple�s headquarters in Cupertino, California, it is currently 27�C and sunny.
```

?? This pattern fits well for scalable assistants, where logic needs to be cleanly split.

**?? You can copy this template here: [AI Multi-Agent Interaction Example](https://app.latenode.com/templates/shared/684725a0cd09a51e3217b514)**

***

## 3. AI Agent with Cloudflare AutoRAG Database

***

Integrate an AI Agent with [Cloudflare AutoRAG](https://developers.cloudflare.com/autorag/usage/rest-api/) to retrieve structured external knowledge � such as product documentation, policies, or internal data.

### Scenario Structure

* `cloudflare_rag_agent` handles free-form prompts
* Two HTTP tools connected:
  * `rag_database_docs` � deep semantic retrieval
  * `raw_data` � fast, factual lookups

  Before using this scenario, you must:

  * [Create an account](https://developers.cloudflare.com/autorag/get-started/) on Cloudflare AutoRAG
  * Create a **database instance**
  * Upload your own documents via the dashboard or API
  * **Replace all placeholders** (`YOUR_ACCOUNT_ID`, `YOUR_RAG_ID`, `YOUR_API_TOKEN`) in the scenario�s HTTP request blocks with your actual values from the Cloudflare dashboard

  Most modern RAG platforms - including AutoRAG - automatically generate embeddings server-side. You don�t need to preprocess documents or manage vectors manually.

***

### Call Example 1 � Documentation Question

**Prompt:**

> �How does the billing system of Cloudflare work?�

* Agent detects it�s a high-level question
* Selects `rag_database_docs` to retrieve semantic context
* Responds based on indexed content

**Expected output:**

```
Cloudflare's billing system uses a monthly subscription model with pro-rated charges...
```

***

### Call Example 2 � Quick Data Point

**Prompt:**

> �What�s the max bandwidth on the free Cloudflare plan?�

* The agent determines it's a factual request
* Selects `raw_data` for direct value retrieval

**Expected output:**

```
The free Cloudflare plan includes up to 1 TB of monthly bandwidth.
```

?? Use AutoRAG-style integrations for assistants that can reason over your documents and give context-aware, accurate replies � without hosting your own vector database or embeddings pipeline.

**?? You can copy this template here: [AI Agent with Cloudflare AutoRAG Database](https://app.latenode.com/templates/shared/684725a0efb7b1fe5317711f)**

***

## Best Practices

* Name all nodes descriptively � they become visible "tools" to the agent
* Use `Agent ID` to maintain session-based memory
* Set `Max Iterations` to prevent loops
* Use `Output JSON Schema` if the response needs to be structured

# AI Agent Node

**AI Agent** is a component of the Latenode platform designed to build intelligent scenarios based on large language models (LLMs). It allows you to integrate external functions, conduct contextual dialogues, and perform sequential actions based on user input.

## Purpose

The AI Agent is used for:

* generating responses to user queries
* calling other nodes in a scenario as functions
* working with short-term memory within a session
* receiving structured JSON responses
* executing scenarios with a limited number of iterations

***

## AI Agent Interface

### Main Fields

| Field              | Description                                                                                                                                                                                                                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model              | The name of the LLM model used (e.g., openai/gpt-4.1) determines the quality and cost of execution.                                                                                                                                                                                                                                     |
| **Session ID**     | Identifier used to load and separate conversation history. If provided, the agent will include the corresponding conversation history in the context. If empty or omitted, each request will be treated as a new session without history.For example, this can be a chat ID or a user ID to distinguish different conversation threads. |
| **User Prompt**    | The user's main query. Supports variable interpolation.                                                                                                                                                                                                                                                                                 |
| **System Message** | Instruction for the language model. Controls the agent's behavior (tone, style, restrictions, etc.).                                                                                                                                                                                                                                    |

### Additional Settings

| Context Window Length      | Specifies the number of most recent message pairs (user and assistant) to include in the context window passed to the LLM. Increasing this value allows the model to consider a longer conversation history, which can improve coherence, but may also consume more tokens and affect performance                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Max Iterations**         | Defines the upper limit of tool invocations allowed for the LLM agent in a single reasoning process. If this threshold is reached, the agent will halt execution and respond with a message indicating it was stopped due to reaching the maximum iteration count.                                                                |
| Temperature                | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.                                                                                                                                              |
| Max Tokens                 | An upper bound for the number of tokens that can be generated for a completion                                                                                                                                                                                                                                                    |
| Structured output (switch) | When enabled, the LLM will be forced to respond in JSON format. You should define the expected JSON structure and formatting rules in the prompt or in "Output JSON Schema”                                                                                                                                                       |
| Output JSON Schema         | When specified, this JSON Schema defines the exact structure, types, and constraints of the expected JSON output from the LLM. The model will be guided to strictly follow this schema during generation. Example: `{ "type": "object", "properties": { "output": { "type": "string", "description": "Provide output here" } } }` |
| Quick Preview Schema       | This field lets you format response data for easy reading. Define key-path pairs in JSON, where the key is the header and the value is the data path                                                                                                                                                                              |

  To explore all available models, their names, prices, and descriptions, you can use the **List Models node**. It returns a structured list of models supported by the AI Agent node.

***

## How It Works

***

AI Agent implements the concept of Function Calling (as defined by OpenAI) or Tool Call. When launched, it forms a standard chat request with roles (system, user) and a list of available **tools**, based on connected nodes.

The request includes:

* `User Prompt` (1) — the user’s request (role: user),
* `System Message` (2) — the system message (role: system),
* **Tool metadata** — each connected node must provide:



  * a **name (3)** (taken from the node's title),
  * a **description (4)** (from the `Tool Description` field),
  * a list of **arguments (5)** defined via `fromAIAgent()` inside input fields.

***

**Example:**

```
{{fromAIAgent("Email Body"; "Include an email body as either plain text or HTML. If HTML, make sure to set the "Body Type" prop to html")}}
```

Each such node is treated as a callable function with a name, arguments, and description. If the model decides to call one of the functions, Latenode executes the corresponding node and returns the result to the AI Agent.

  The model decides on its own which tools to invoke depending on the meaning of the user request. You can connect multiple tools- only relevant ones will be triggered based on context.

### AI Chat

On the right side of the node configuration, there is an **AI Chat** tab. You can use it to talk to the assistant in real-time and test its behavior. This is useful for verifying how the model interprets the prompt, what actions it suggests, and which tools it decides to call.

***

## Connecting Tools to the Agent

To make AI Agent use other scenario blocks, they must be **visually connected from the bottom** via the constructor interface.

There are two ways to do this:

* **Drag and drop** the desired node (e.g., HTTP Request, Telegram, Search, etc.) and connect it to the **bottom connector** of the AI Agent node.
* Or, click on the connector of the AI Agent and manually link it to an existing node.

Once connected, the linked node becomes available as a callable **tool** for the agent.

***

## Passing Parameters to Connected Tools

To pass data from the AI Agent into the connected node, use the `fromAIAgent()` operator. This operator acts as a **placeholder for dynamic input** — the agent will automatically substitute it with relevant values during execution.

You can place `{{fromAIAgent("parameter_name"; "parameter description")}}` inside any input field of the connected node (such as `Request Body`, `Prompt`, `Text`, etc.).

This expression defines the expected argument for the tool:

* `"parameter_name"` — the internal name of the parameter
* `"parameter description"` — shown to the model and used in function schema

***

**Format:**

```
{{fromAIAgent("parameter_name"; "description")}}
```

**Example:**

```
{{fromAIAgent("Email Body"; "Include an email body as either plain text")}}
```

***

This will register the node as an available function with:

* its **name** (taken from the node title),
* a **description** (taken from the `Tool Description` field),
* a list of **parameters** defined via `fromAIAgent()` expressions.

  Each node must have a unique name. If the name is missing, execution will fail.

***

## Example: Weather Forecast (No Authorization Required)

Let’s see how AI Agent works using a weather forecast request.

1. Place an **AI Agent** on the canvas.

2. In the `System Message` field, write:

   ```
   You are an assistant who can get the weather. Use the appropriate tool.
   ```

3. Add an `HTTP Request` node below it.

4. Name the node, e.g., `Weather forecast`

5. Set method to: `GET`

6. In the URL field, insert:

   ```
   https://wttr.in/{{fromAIAgent("city"; "City name for the weather forecast")}}?format=3
   ```

7. Launch AI Agent with the prompt:

   ```
   What's the weather like in Berlin?
   ```

As a result:

* The AI Agent receives the user request;
* analyzes that a weather forecast is needed;
* finds the node named `weather_forecast`, which uses `fromAIAgent` with the `city` parameter;
* substitutes the value “London” and makes the HTTP request;
* receives a brief forecast and sends it back to the user.

***

## Example: Flexible Telegram Chatbot

AI Agent also works well in chatbot format. You can connect **multiple nodes** and let the model decide which to use.

For instance, here’s a basic Telegram chatbot:

Telegram trigger connected to AI Agent, and from AI Agent to:

* `Web Search` (Perplexity);
* `Create Note` (Notion);
* `Current Weather`

In this scenario:

* If the user sends a general message, the agent simply replies with text without calling tools.

* If the user asks to create note, it uses the `Create Note`node.

* If the user asks to do something complex, such as getting the weather and searching for information online, two tools - `Web Search` and `Current Weather`  - will be triggered sequentially, and their results will be included in the response.

Each node is registered with `fromAIAgent()` to pass parameters. The model understands which tool to use - and ignores the rest.

This makes the chatbot dynamic and modular.

***

## Multi-Agentic Workflows

While basic and modular agents are suitable for most simple and mid-level use cases, **multi-agentic workflows** allow for advanced coordination between multiple agents - each acting independently and fulfilling a specialized role.

In these scenarios, agents can exchange data, trigger one another conditionally, and take on distinct responsibilities within a single request. For example, one agent may serve as a **copywriter**, another as an **editor**, and a third as a **fact-checker**. This separation of roles helps reduce hallucinations that typically occur when a single agent is overloaded with multiple objectives.

These patterns are particularly useful for:

* multi-step reasoning;
* tool orchestration;
* AI pipelines that require clear logic separation and internal feedback loops.

> 📘 For more detailed, step-by-step examples of how AI Agents behave and coordinate in different scenarios, see the full article:

  [AI Agents Examples](https://latenode.com/docs/ai-agents-examples)

***

# How to Use Your Own API Keys

This guide covers how to integrate any **OpenAI API-compatible** (LLM) into your Latenode workflow, including self-hosted and third-party services. Both the **Custom LLM Node** and the **AI Agent Node** share the exact same connection method.

***

## 1. Establishing the Custom LLM Connection

The connection mechanism relies on the widely adopted OpenAI API structure, allowing you to use external services (like Groq, Perplexity, or Ollama) by correctly specifying the Base URL.

### A. Creating a New Authorization

1. Click **"Choose"** and select **"New authorization"**.

2. Fill in the connection details:
   * **API Key:** Your secret key provided by the LLM service.
   * **Base URL:** The URL endpoint that accepts OpenAI-compatible chat completion requests. This is the **most crucial field** for compatibility.
   * **Model:** The model identifier (e.g., `gpt-4-turbo`, `llama-3`).

**Compatible Base URL Examples:**

| Service        | Base URL                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| OpenAI         | `https://api.openai.com/v1/chat/completions`                                                                       |
| Groq           | `https://api.groq.com/openai/v1/chat/completions`                                                                  |
| Perplexity     | `https://api.perplexity.ai/chat/completions`                                                                       |
| Ollama (Local) | `http://localhost:11434/v1/chat/completions`                                                                       |
| Azure OpenAI   | `https://[YOUR-RESOURCE].openai.azure.com/openai/deployments/[MODEL-NAME]/chat/completions?api-version=2024-02-15` |

### B. Sharing the Connection with the AI Agent Node

The authorization created in Step 1 is reusable. This allows you to power your AI Agents with the same custom models.

1. In the **AI Agent Node**, toggle the **"Use Custom LLM Connection"** switch to ON.

2. Click **"Create an authorization"**.

3. Choose the authorization you created earlier (and click **"Authorization"** to create a new one).

Your authorization has been successfully added.

***

## 2. Advanced Settings: Controlling LLM Behavior

These settings are found under **"Show advanced settings"** in the Custom LLM Node and provide granular control over the model's output, creativity, and context management.

### Context and Input Parameters

| Parameter               | Description                                                                                   | Use Case                                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **File Content**        | Accepts a URL or a variable containing file data.                                             | Used for **multimodal** models to analyze images or process non-image files like PDFs (when paired with **File Name**). |
| **File Name**           | Required for non-image files (text, PDF, documents) when passing data via **File Content**.   |                                                                                                                         |
| **Dialog History JSON** | A valid JSON array detailing the conversation history (`{"role": "user", "content": "..."}`). | Essential for maintaining **context** in multi-turn chatbot conversations.                                              |

### Generation and Creativity Parameters

These parameters control the quality and diversity of the generated response. It is recommended to adjust either **Temperature** or **Top P**, but not both.

| Parameter          | Description                                                                                                                            | Effect                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Max Tokens**     | The maximum number of tokens the model can generate in its output.                                                                     | Controls the **length** of the response.                              |
| **Temperature**    | Sampling temperature. **Lower values** (e.g., 0.1) result in more focused and deterministic output.                                    | Best for accurate, factual tasks.                                     |
| **Top P**          | Nucleus sampling parameter. **Lower values** make the output more focused by limiting token consideration to a small probability mass. | Alternative control for response **diversity**.                       |
| **Stop Sequences** | A list of tokens that, when generated, cause the model to immediately stop outputting text.                                            | Used to prevent the model from continuing beyond a desired end point. |

### Structuring and Tool Use

| Parameter                      | Description                                                                                                          | Primary Function                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Structured Output (Toggle)** | Forces the LLM to respond using a **JSON format**.                                                                   | Ideal for reliable data extraction into variables.                            |
| **Output JSON Schema**         | A valid JSON Schema defining the precise fields, types, and required properties of the expected output.              | Guarantees structured, predictable output for downstream nodes.               |
| **Tools JSON**                 | A JSON object describing the **functions** the model can call to fulfill a user request.                             | Enables **Function Calling** or **Tool Use** capabilities of advanced models. |
| **Tool Choice JSON**           | Controls which tool (if any) the model is allowed to call (`none`, `auto`, `required`, or a specific function name). | Determines the model's action when tools are available.                       |
| **Frequency Penalty**          | Reduces the likelihood of repeating tokens based on their existing frequency in the text.                            | **Discourages** the model from repeating words.                               |
| **Presence Penalty**           | Reduces the likelihood of reusing tokens that have already appeared in the context.                                  | **Encourages** the model to introduce new topics or concepts.                 |

# Guardrails for AI Agents

## Overview

Guardrails are strategies that help ensure AI Agents operate safely, consistently, and within clearly defined boundaries. They are especially important in production scenarios where unpredictable behavior can lead to incorrect tool usage, malformed outputs, or unintended consequences.

This guide explains how to implement guardrails on the levels of instructions, tools, and scenario logic using Latenode.

***

### Why Use Guardrails

AI Agents powered by large language models (LLMs) are inherently flexible and probabilistic. Without constraints, they can:

* Misinterpret vague input
* Call the wrong tools
* Generate unstructured responses
* Act outside of intended use

Guardrails help maintain stability, protect user experience, and prevent failures in downstream logic.

***

### Instruction-Level Guardrails

Use the **Instructions** field to define:

* What the agent is allowed and not allowed to do
* What conditions must be met before taking action
* How to handle missing or invalid inputs
* How to respond to irrelevant messages
* What tone or format the output should follow

### Example

📄 **Paste this into the System Message field:**

```
You handle refund requests only. Do not respond to unrelated topics. If the message is not about a refund, reply: “I can only help with refund-related questions.” Do not call any tool unless both email and order_id are provided. Use polite, brief language.
```

***

### Tool-Level Guardrails

Control behavior through connected tools:

* Only connect needed nodes
* Use clear parameter names (`user_email`, not `input1`)
* Validate required fields before execution
* Return structured error messages

### Output Example

```json
{
  "status": "error",
  "message": "Missing required field: email"
}
```

Avoid ambiguous outputs like `"done"` or `"ok"`.

***

### Scenario-Level Guardrails

Use logic blocks to enforce restrictions before or after the agent call:

* Roiting — validate input presence
* **Set Variables node** — normalize or sanitize input
* **Max Iterations** — prevent infinite tool loops

***

### Output Validation

Use the **Output JSON Schema** field to enforce response structure.

### Example schema:

```json
{
  "type": "object",
  "properties": {
    "status": { "type": "string" },
    "summary": { "type": "string" }
  },
  "required": ["status"]
}

```

Validate the output before continuing the scenario.

***

### Safety Prompts

Embed rules directly in the **System Message**, such as:

* "Never make assumptions about user identity."
* "Do not respond to unsupported topics."
* "Request confirmation before processing sensitive actions."

These reduce the risk of misuse or incorrect tool calls.

***

### Best Practices

* Limit agents to focused use cases
* Connect only necessary tools
* Validate inputs with logic blocks
* Enforce JSON output schemas
* Monitor execution logs regularly

***

# Multi-Agent Systems

## Overview

In advanced scenarios, you can use multiple AI Agents to handle different domains of knowledge or task types. Each agent has its own instructions and set of tools - enabling modular, scalable workflows.

This setup improves clarity, separates responsibilities, and allows for more focused instruction design.

***

### When to Use

Use multiple AI agents when:

* Your workflow spans **distinct areas** like weather, finance, or general web lookup
* You want to **keep agent logic focused** (no bloated all-in-one prompts)
* You need **modular agents** that are easier to test, reuse, or extend
* Different agents require **different tools, models, or language settings**

***

### Agent Roles in This Example

| Agent           | Task                                                    |
| --------------- | ------------------------------------------------------- |
| `main_agent`    | Parses the user input and routes to the right sub-agent |
| `finance_agent` | Handles currency conversion and crypto price checks     |
| `weather_agent` | Handles weather summaries and current condition lookups |

Each sub-agent is connected only to tools relevant to its domain (e.g., `finance_agent` > `currency_converter`, `crypto_price_checker`).

***

### Tool Isolation

Keep each agent connected to only what it needs.

* `weather_agent` > `quick_weather_summary`, `current_weather_via_coordinates`
* `finance_agent` > `currency_converter`, `crypto_price_checker`
* `web_search_tool` is accessible globally or from `main_agent`

This way the main agent acts like a dispatcher, and the sub-agents remain focused.

***

### Routing Between Agents

The `main_agent` can detect intent from the message itself and trigger the right branch of logic.

***

### Best Practices

* Assign a clear responsibility to each agent
* Keep agent prompts short and purpose-specific
* Use tool descriptions and names that match their role
* Let the main agent **route and orchestrate**, not perform everything
* Test sub-agents independently

***

# Think & Plan Tools

## Overview

Think Tool and Plan Tool are special reasoning tools that extend the capabilities of an AI Agent. They do not perform business actions themselves � instead, they enforce structured reasoning inside the agent.

Both tools improve result quality and transparency, but they differ in timing and cost:

* **Think Tool**: inserts reasoning between every step.
* **Plan Tool**: generates a plan once before execution starts.

***

## Think Tool

Think Tool forces the agent to pause and write out its reasoning before each action. This reasoning log can be inspected later, making the decision process fully transparent.

When the **Force Think Tool** option is enabled, the tool is injected automatically into every step. When disabled, it behaves like a normal optional tool, and the agent may choose to call it only if prompted.

The log is customizable: the `description` field can guide the style and length of the agent�s notes. For example, the agent can be instructed to keep reasoning concise, or to explicitly confirm progress toward the user�s request after each step.

In testing, Think Tool dramatically increased accuracy:

* Without it, a complex decryption task failed in all runs.
* With it, **7 out of 8** runs produced the correct result.

The trade-off is higher token usage and slower execution time, since every step includes an additional reasoning call.

***

## Plan Tool

Plan Tool requires the agent to generate a structured plan at the very beginning of execution. The plan is stored in the reasoning log, and then the agent follows it through step by step.

Unlike Think Tool, Plan Tool is called only once, so execution is faster and more economical.

In tests, Plan Tool improved accuracy compared to no reasoning at all, though results were less consistent than with Think Tool:

* About **3�4 successful runs out of 8**
* Average runtime was shorter and token usage lower

Plan Tool is best for medium-complexity or repetitive workflows where efficiency is more important than maximum accuracy. It offers some transparency, since the initial plan is visible, but does not record reasoning after every action.

***

## Comparison

| Aspect       | Think Tool                           | Plan Tool                     |
| ------------ | ------------------------------------ | ----------------------------- |
| Invocation   | Before and between every action      | Once at the beginning         |
| Log          | Step-by-step reasoning entries       | Initial plan only             |
| Accuracy     | Very high                            | Improved, but less consistent |
| Performance  | Slower, higher token usage           | Faster, lower token usage     |
| Transparency | Full trace of reasoning at each step | Single plan for the run       |
| Flexibility  | Can adapt between steps              | Fixed once plan is written    |

***

## Practical Use

* Choose **Think Tool** when correctness and traceability matter most, such as debugging complex workflows or critical automation. Expect longer runtime and higher cost, but nearly guaranteed improvement in reliability.
* Choose **Plan Tool** when you need speed and lower token consumption, and can accept some loss in accuracy. It works well for batch scenarios and straightforward tasks.

Both tools return their logs in the UI, so you can always inspect what the agent was �thinking� or �planning.�

# Tool Design for AI Agents

## Overview

Tools are nodes connected to the AI Agent that perform specific actions or return data. They must be well-defined so the agent can use them reliably.

***

### Naming

Agents refer to tools by their node names. Use clear, descriptive names that directly reflect the purpose of the tool.

### ? Good:

* `create_event_tool`
* `send_email_draft`
* `retrieve_calendar_tool`

### ? Poor:

* `Node 3`
* `tempTool`
* `doStuff`

  Tool names are a key part of the agent's reasoning. If the name doesn�t convey the purpose, the agent may ignore or misuse the tool.

***

### Behavior Guidelines

* Tools should be deterministic and return consistent results
* If the tool performs irreversible actions (e.g. sending an email, booking a meeting), ensure that the agent logic confirms intent before calling it
* Tools should return helpful errors when required input is missing or invalid � in a format the agent can interpret

***

### Tool Descriptions

Each tool should include a short description that explains its function. This is used by the agent to decide when (and if) to use it.

> ?? The tool description is not just for documentation � it is also passed via API and directly affects how the agent reasons about and chooses to call the tool. A vague or missing description can lead to the tool being ignored or misused.

### ? Good:

> create\_event\_tool: "Creates a new calendar event using title, time, and participant list."

### ? Poor:

> "Does stuff with the calendar"
>
> `"Test tool"`

> ?? Keep descriptions short, specific, and action-oriented. Write them for the agent � not just for humans.

***

### Testing

Always test each tool in isolation before connecting it to an agent. Validate that the tool:

* Executes reliably with real input
* Returns usable results
* Fails gracefully when needed

***

# Writing Effective Instructions (Prompting guide)

The **System Message** field in the AI Agent node on **Latenode** defines the agent�s role, behavior, and decision-making. These instructions are written directly inside the **System Message** section in the agent�s settings. This field determines how the agent responds to user input, when it calls tools, and how it handles ambiguity or missing data.

Structured instructions are essential for predictable, helpful, and controlled agent behavior across domains like customer support, onboarding, automation, education, or internal tools. This is especially true for AI agents built and orchestrated on **Latenode**, where clear system logic is crucial to creating scalable automations.

***

## Core Structure

On **Latenode**, effective instructions typically consist of six building blocks:

1. **Personality** � Who the agent is and how it acts
2. **Environment** � The context in which it operates
3. **Tone** � The communication style
4. **Goal** � What the agent is trying to accomplish
5. **Guardrails** � What the agent must not do
6. **Tools** � What it can access and how

***

## 1. Personality

The agent�s personality defines its identity, attitude, and behavioral traits. A consistent personality makes interactions feel coherent and intentional.

**Include:**

* **Name and role**

  *Example:* �You are Sarah, a patient and knowledgeable setup assistant.�

* **Core traits**

  *Example:* �You're empathetic, direct, curious, and always focused on clarity.�

* **Behavior anchors**

  *Example:* �You acknowledge user emotions briefly and redirect to solutions without dwelling.�

* **Backstory (optional)**

  Include only if it influences how the agent should behave. Avoid fluff.

**Example � Expressive personality:**

```markdown
You are John, a nurturing virtual wellness coach.
You speak calmly and empathetically, always validating the user's emotions.
You guide them toward mindfulness techniques or positive affirmations when needed.
You're naturally intuitive and thoughtful.
```

***

## 2. Environment

Defines the situational or technical context in which the agent operates. This helps the agent adapt tone, verbosity, or content structure.

**Specify:**

* Platform/channel (chat, web app, embedded widget, etc.)
* Limitations (e.g. "you cannot see the user�s screen")
* User state (e.g. "the user may be frustrated due to recent failures")

**Example � Technical support environment:**

```markdown
You are embedded in a SaaS platform�s live chat widget.
Users reach you while using the product, often mid-task or blocked.
You don�t have access to screen content or telemetry.
Assume technical issues are common, and users may be stressed.
```

On **Latenode**, agents often run inside real-time workflows, so your environment description should reflect this automation context clearly.

***

## 3. Tone

Tone governs how the agent communicates: the level of formality, choice of language, pacing, and linguistic rhythm.

**Define:**

* Level of formality and typical sentence length
* Use of affirmations ("Got it", "That makes sense")
* Whether to use filler words, hedging, etc.
* Adapting tone to user emotional state or technical background

**Example � Supportive tone:**

```markdown
Your responses are clear, concise, and solution-oriented.
You use affirmations like �I understand� or �Great question� to maintain flow.
You adapt technical language based on user familiarity.
If frustration is detected, acknowledge it briefly before returning to problem-solving.
Keep responses under three sentences unless further detail is essential.
```

**Example � Documentation assistant tone:**

```markdown
You speak with calm authority and technical clarity.
You format code, commands, and paths clearly in your replies.
You avoid emojis, humor, or casual language.
```

***

## 4. Goal

The goal defines what the agent is supposed to achieve in each session or interaction.

**Clarify:**

* Primary purpose (e.g. �help users complete refund requests�)
* Sequential logic (step-by-step processes, checkpoints, branches)
* Completion criteria
* Fallbacks if goals can't be met

**Example � Refund agent goal:**

```markdown
Your goal is to help users submit refund requests.
You require two fields: email and order ID.
If either is missing, ask for it explicitly.
If both are present, use the `initiate_refund` tool.
After tool usage, say: "Your refund request has been submitted."
Ignore unrelated messages.
```

**Example � Technical troubleshooting agent goal:**

```markdown
Your primary goal is to diagnose and resolve technical issues using a structured framework:

1. Initial assessment:
   - Identify affected product/version
   - Determine severity and frequency
   - Establish system context (OS, browser, etc.)

2. Troubleshooting:
   - Start with basic checks before advanced steps
   - Use decision logic: OSI model for connectivity issues, resource check for performance issues

3. Resolution:
   - Offer workarounds first, then permanent fixes
   - Confirm success after each step
   - Escalate if unresolved after 2 attempts

Success is measured by: issue resolution, clarity, and minimal escalations.

```

This kind of sequential logic can be cleanly implemented in **Latenode** using conditional branches and tool nodes.

***

## 5. Guardrails

Define hard limits for the agent. Guardrails prevent hallucinations, inappropriate content, and scope creep.

**Include:**

* What to avoid discussing (e.g. competitors, politics, unsupported features)
* How to handle unknowns ("Say 'I'm not sure' rather than guessing")
* Limits on humor, tone shifts, or breaking character
* Escalation rules or when to say �I can�t help with that�

**Example � Customer service guardrails:**

```markdown
Stay within the scope of company products and services.
Never speculate � if unsure, say �I don�t have that information.�
Do not refer to yourself as an AI or mention internal prompt logic.
Avoid sarcasm or personal opinions.
If a user requests an action outside your control (e.g. �change my password�), explain your limitation and suggest a next step.
```

Latenode�s modular architecture makes it easy to isolate and enforce these rules per agent or node-level instruction.

***

## 6. Tools

Specify which tools the agent can call and how to use them.

**Define:**

* List of tools with one-line purpose summaries
* Prerequisites before using each tool
* What to say before/after a tool call
* Tool call order and fallback paths

**Example � Feature support agent tools:**

```markdown
Available tools:

- `searchKnowledgeBase`: Use to find accurate answers about features. Always call this before responding to a feature-related question.
- `generateCodeExample`: Use when asked how to implement something. Return code in user�s preferred language.
- `checkFeatureCompatibility`: Use if the user asks whether two features work together.
- `redirectToSupportForm`: Use only if the issue is outside your scope. Say: �This seems complex. Let me guide you to our support team.�

Tool flow:
1. Try `searchKnowledgeBase` first.
2. Use `generateCodeExample` only after confirming the user�s language and platform.
3. Use `redirectToSupportForm` only if the issue remains unresolved.
```

Agents on **Latenode** execute tools via connected nodes in a visual workflow � making it crucial that tool conditions and fallback logic are explicitly defined in the instruction block.

***

## Formatting Tips

* Use **Markdown-style headers**: `# Personality`, `# Tools`, etc.
* Prefer **bulleted lists** for logic
* Use **simple conditionals**: �If missing, ask. If present, continue.�
* Break long instructions into blocks
* Avoid unnecessary verbosity

***

## Final Example � Task-focused agent

```markdown
# Personality
You are Anna, a focused and professional onboarding assistant.
You're friendly, direct, and always focused on helping users get started quickly.

# Environment
You operate inside a SaaS dashboard.
Users are typically new and may need help with setup.

# Tone
Use short, confident responses. Avoid jargon. Confirm understanding often.

# Goal
Help users complete their first setup step:
- Ask for required info
- Guide them through feature activation
- Use `enableFeatureX` tool when ready
- Confirm completion

# Guardrails
Never provide legal advice. If unsure, redirect to documentation.
Do not speculate or invent information.

# Tools
- `enableFeatureX`: Call only after user confirms setup details
- `searchDocs`: Use if a user asks �how does X work?�
```

***

By following this structure, AI agents on **Latenode** become predictable, scalable, and easy to maintain - even in large automation systems. Whether you're designing a refund bot, internal helper, or user onboarding assistant, this framework ensures your instructions are solid from the first message to the last.

# Changelog

Stay up to date with the latest features, improvements, and bug fixes in Latenode.

</Cards>

# Introduction

Latenode helps you automate processes with flexible no-code and low-code scenarios. The platform combines the simplicity of a visual editor with the power of code where it’s truly needed. This makes Latenode a great fit both for non-technical professionals and for developers who value speed and flexibility.

This guide will walk you through the basics of automation and show how Latenode can take repetitive work off your plate.

***

## What is a scenario?

A scenario is a sequence of steps you take to achieve a result. For example, imagine you are a marketer working with leads:

* Receive a lead from a website form or CRM
* Verify the lead’s data
* Send a welcome email
* Create a task for a manager
* If needed, sync data with other services

Even a simple process like this can take a lot of time and requires switching between tools. Latenode helps you automate these steps — from routine actions to complex logic integration.

Automation is not only about technology, but also about mindset. Starting with basic scenarios and ready-made templates, you will gradually discover more and more processes that can be automated.

***

## Two types of workflows in Latenode

In Latenode, you can build both **condition-based workflows** and **agentic workflows** that can make decisions and use tools.

### Condition-based workflows (predictable automation)

Condition-based workflows are deterministic scenarios: the same input follows a consistent execution path.
Use them when you need reliability, clear logic, and scale.

In practice, they are built around nodes + **routes with conditions** (branching, fallback paths), variables, and data transformations.

### Agentic workflows (decision-making automation)

Agentic workflows are scenarios powered by LLMs. They can interpret a request, decide what to do next, and call connected nodes as **tools** step-by-step (tool calling).
Use them when tasks are open-ended, require reasoning, or need dynamic tool selection.

Agentic workflows can also use internal data sources like a built-in **RAG storage** to search knowledge and ground responses in your documents and datasets.

***

## AI assistants that make building easier

Latenode includes multiple AI helpers designed to make scenario creation as easy as possible:

* Generate scenario drafts from a plain-language description, then iterate in the visual editor
* Help you test, troubleshoot, and refine scenarios faster
* Write JavaScript for custom logic when you need a low-code solution beyond standard nodes

***

## What makes Latenode different

### 500+ apps and integrations

Connect Latenode to **500+ apps** — from CRMs and messengers to databases and internal APIs.

### 500+ AI models + Plug‑n‑Play (one billing)

Use **500+ AI models** inside scenarios — including text models, image generation, video generation, and more — and combine them with your workflows, data, and tools.
All of this works with **a single Latenode balance** (you can also use your own API keys).

***

## MCP: expose scenarios as tools for AI clients

With **MCP (Model Context Protocol)**, you can turn your scenarios into tools for MCP-compatible clients like **Cursor** or **Claude Desktop**.
This bridges reliable workflows and external AI systems: your scenario becomes an actionable tool that an AI client can discover and call.

***

And much more.

# Integrations

Connect your favorite apps and services with Latenode.

</Cards>

# Customer Data Protection & Encryption

Latenode meets the highest security standards, implementing industry-leading protocols to ensure your data is protected at every step. Our commitment to security provides you with the confidence to automate workflows securely and efficiently.

# User accounts, authentication, and authorization

### Latenode Cloud

When you sign up for an Latenode cloud account, you create an account directly with Latenode. When you create an account on Latenode.cloud with a username and password, Latenode implements best practices for account management. For example, Latenode salts and hashes your password, then stores the hashed password in a database that�s encrypted at rest.

### Third-party accounts

A key part of Latenode's functionality is linking third-party services. When you link an account from a third-party application, you may need to either authorize Latenode OAuth application access to your account, or provide an API key or other credentials.

Latenode recommends using [OAuth](https://oauth.net/2/) for third-party applications that support it. The OAuth protocol allows Latenode to request scoped access to specific resources in your third-party account without you having to provide long-term credentials directly. Latenode must request short-term access tokens at regular intervals, and most applications provide a way to revoke Latenode's access to your account at any time.

Some third-party applications don't provide an OAuth interface. To access these services, you must provide the required authorization mechanism (often an API key). As a best practice, if your application provides such functionality, Latenode recommends limiting that API key's access to only the resources you need to access within Latenode.

When you use credentials in a workflow, Latenode loads them into the execution environment of your Latenode instance. For Latenode Cloud, customer instances are logically isolated from one another. Latenode doesn't log or export credentials by default. If you log their values you can always delete the data for that execution. The platform deletes execution data automatically based on your account�s retention settings.

You can delete your OAuth grants or key-based credentials at any time. Deleting OAuth grants within Latenode doesn't revoke Latenode�s access to your account. You must revoke that access wherever you manage OAuth grants in your third-party application.

### User authentication

A username and password are required to authenticate into the app.

### Cloud hosting & storage

Latenode cloud uses Microsoft Azure for hosting.

Latenode further secures access to Azure resources through a series of controls, including:

* Using multi-factor authentication to access Azure
* Hosting services within a private network that�s inaccessible to the public internet.

Latenode stores all OAuth tokens, key-based credentials, and the rest of your Cloud instance's database on a disk that's encrypted at rest using Azure server side encryption (at the time of writing, using AES256 and a FIPS-140-2 compliant implementation). For Latenode cloud, this database also resides in a private network. Backups of that database are also encrypted.

### Data encryption

### Latenode Cloud

When you use the Latenode web application, it encrypts traffic between your client and Latenode services in transit. The same applies for traffic related to the public API or webhook trigger nodes. Latenode uses Cloudflare to manage and renew SSL certificates.

### Network protection

An operational audit system constantly monitors Latenode's cloud infrastructure and sends alerts to appropriate personnel when necessary. We only use configurations that implement approved networking ports and protocols, including firewalls. For example, we maintain a Web Application Firewall to protect Latenode�s web application from malicious traffic and outside threats. And an Intrusion Detection System to detect potential intrusions.

### Audit logging

Latenode collects and stores all your server logs in a central location. Authorized users can query the log info as necessary to trace actions to individual users. We keep audit log history and historical activity records for at least 3 months, with at least the last one months immediately available for analysis.

# Secure development practices

### Version control system

Latenode uses a version control system to manage source code, documentation, release labeling, and other change management tasks. Any employee must get their access approved by a system admin to make code changes.

### Code review process

When Latenode's application code changes, someone other than the person who made the change reviews and tests the new code.

### Separate testing and production environments

Latenode uses separate environments for testing and production for our application.

### Restricted production code changes

Only authorized Latenode personnel can push or make changes to production code.

### Static Application Security Testing (SAST)

Latenode uses static application security testing (SAST) or an equivalent tool as part of the CI/CD pipeline to detect vulnerabilities in its code base. When vulnerabilities are identified, corrections are implemented before release as appropriate based on the nature of the vulnerability.

### Systems Monitoring

Latenode monitors its code, infrastructure, and core applications for known vulnerabilities and addresses critical vulnerabilities promptly.

# Access controls

### Strictly �need-to-know� access to data

Latenode grants employees access to systems containing sensitive data on a least-privilege basis. This means employees only have access to the data they need to perform their job. The company reviews system access quarterly, on any change in role, and upon termination.

### Restricted production code access

Latenode uses GitLab to store and version all production code. Employees use multi-factor authentication to access the GitLab organization. And only authorized Latenode personnel can deploy or make changes to production code.

### Required multi-factor authentication

We require MFA wherever it is available.

### Encrypted web-based access

Latenode uses encryption to protect user authentication and admin sessions of the internal admin tool transmitted over the Internet. All connections happen over SSL/TLS with a valid certificate from a reliable Certificate Authority.

# Corporate security

### Rigorous hiring process

Job candidates must pass through multiple stages of comprehensive background checks and interviews to ensure they comply with relevant laws, regulations, and ethics. All new employees must sign our data protection policy on hire.

### Strict offboarding process

When an employee leaves Latenode, we use a termination checklist to ensure that the employee's system access, including physical access, gets removed within one business day and all organization assets (physical or electronic) get returned.

# Threat & vulnerability management

### Vulnerability scans

Latenode conducts third-party vulnerability scans of its production environment at least once every 90 days.

### Penetration tests

Latenode conducts third-party penetration tests of its production environment at least once a year.

### Intrusion detection

Latenode operates an intrusion detection system (IDS) to detect potential intrusions and alert personnel when a potential intrusion is detected. Including a continuously updated anti-malware solution that scans continuously to detect, remove, or block all types of known malware.

### Phishing simulations

Latenode conducts periodic phishing simulations as part of the company's security awareness initiatives.

### Threat intelligence

Latenode has implemented mechanisms to collect threat information and produce threat intelligence (e.g., commercial cyber threat intelligence tools, security product/vendor intelligence feeds, open source feeds, etc.) in accordance with defined threat intelligence objectives.

### Backup, recovery, and business continuity

Latenode stores customer data in a secure production account in Azure. Latenode automatically backs up all customer and system data daily to protect against catastrophic loss due to unforeseen events that impact the entire system. This process backs up or replicates data to a separate region in the same country. And the backups are encrypted in the same way as live production data.

Latenode�s backup service monitors the entire backup process, and any failures automatically trigger an alert to the Incident Response Team.

Latenode has a defined and regularly tested Business Continuity Plan outlining the procedures to respond, recover, resume, and restore operations following a major natural disaster or catastrophic system failure.

### Disaster recovery plan

Latenode has formulated a detailed disaster recovery plan outlining the roles, responsibilities, and detailed procedures for recovering systems in case of failure.

### Security logs

Latenode collects and stores server logs in a central location. The system can be queried in an ad hoc fashion by authorized users.

### Information security policy

Latenode has an Information Security Policy to define security obligations for employees and contractors, together with its disciplinary process for violations of the policy.

### Vulnerability disclosure

Latenode has a dedicated process for employees to report security, confidentiality, integrity, and availability failures, incidents, and concerns.

In addition, Latenode maintains customer-accessible support documentation where you can find support contact information. We�re committed to ensuring Latenode is a safe and secure tool for all our users. So should you find any operational or security failures, incidents, system problems, concerns, or other issues/complaints, please don�t hesitate to contact the relevant Latenode personnel.

Last updated on August 4, 2025

# Data Processing Addendum

Available here [https://latenode.com/docs/data-processing-agreement-gdpr-statement](https://latenode.com/docs/data-processing-agreement-gdpr-statement)

Last updated on August 4, 2025

# Subprocessors

This is a list of sub-processors authorized to process customer data for latenode’s service. Latenode audits each sub-processor's security controls and applicable regulations for the protection of personal data.

## Core Infrastructure Subprocessors

| Sub-processor name                             | Nature of Processing                                                                        | Location |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------- | -------- |
| Microsoft Azure                                | Hosting                                                                                     | US       |
| Cloudflare, Inc., San Francisco, United States | Hosting, Global CDN to enhance the application performance and mitigate cybersecurity risks | Globally |
| Amazon Web Services                            | Hosting                                                                                     | US       |

## Other Subprocessors

| Name        | Nature of Processing | Location |
| ----------- | -------------------- | -------- |
| Intercom    | Support              | US       |
| Posthog.com | Product Analytics    | EU       |
| Fillout.com | Forms                | US       |

# Connecting to MCP Tools

This guide explains how to connect popular **MCP clients** (for example, **Cursor** and **Claude Desktop**) to your tools published via **MCP Trigger** in Latenode.

## Before you start

You'll need:

* A scenario with **MCP Trigger** configured (see [MCP Nodes](/mcp/mcp-nodes))

{/* Example:
  [Image: Copy Server URL in MCP Trigger]
  */}

## Step 2 — Connect using your MCP client

Below are quick setup steps for common clients. The UI labels can differ between versions, but the idea is always the same:
**add a new MCP server/connector** and paste your **Server URL**.

### Cursor

1. Open **Cursor**
2. Go to **Settings**
3. Find **MCP** (or **MCP Servers / Tools**)
4. Click **Add server**
5. Paste the **Server URL** you copied from Latenode
6. If prompted for auth, provide your **API key**
7. Save, then open the tools list and confirm your Latenode tools are visible

{/* TODO: Add screenshot(s) of Cursor MCP server setup */}

{/* Example:
  [Image: Cursor MCP server setup]
  */}

### Claude Desktop

1. Open **Claude Desktop**
2. Open **Settings**
3. Go to **Connectors**
4. Click **Add custom connector**
5. Paste the **Server URL** from Latenode
6. If prompted for auth, provide your **API key**
7. Save, then verify the connector is enabled

{/* TODO: Add screenshot(s) of Claude Desktop connector setup */}

{/* Example:
  [Image: Claude Desktop connector setup]
  */}

### ChatGPT (MCP-compatible client)

If you’re using a ChatGPT setup that supports MCP servers (directly or via a connector/bridge), the steps are the same:

1. Open your client’s **Connectors / Tools / MCP** settings
2. Add a new MCP server
3. Paste the **Server URL** from Latenode
4. Provide the **API key** if your MCP Trigger requires it
5. Verify tools are listed and callable

### OpenAI (Chat) / OpenAI API (MCP-compatible client)

If your OpenAI setup supports MCP (directly or via a compatible MCP client):

1. Add a new MCP server in your MCP client / middleware
2. Paste the **Server URL**
3. Configure authentication if required
4. Verify tool discovery works, then call a tool in a test prompt

### Vapi (MCP-compatible client)

If you use Vapi through an MCP-capable integration:

1. Add your Latenode MCP server in the Vapi MCP integration settings
2. Paste the **Server URL**
3. Provide the **API key** if required
4. Test by calling a tool from a simple voice agent flow

## Troubleshooting

### Tools don’t appear

* Make sure **Tool Name** is set on the nodes connected to **MCP Trigger** (otherwise tools won’t be discoverable).
* Confirm you copied the correct **Server URL** from **MCP Trigger**.
* If your scenario requires auth, confirm the client is actually sending the required credentials.

### Connection drops or times out

* MCP uses a streaming connection (SSE). Ensure a stable network connection.
* Keep tool execution fast and return only what you need (use **MCP Response**).

### Authentication errors (401/403)

* Confirm **Authentication** is enabled/disabled as expected in MCP Trigger.
* If enabled, regenerate/recopy your API key and update it in the client.

# MCP Nodes

Latenode **MCP server** allows external AI systems (AI agents) to run your scenarios as tools.
**Model Context Protocol (MCP)** is a communication standard between AI systems and external systems, enabling them to interact by defining endpoints and providing authentication.

With Latenode MCP, you can expose your scenarios to AI clients like **Claude Desktop**, **Cursor**, or any MCP-compatible application.

## MCP Trigger

**MCP Trigger** turns your scenario into an MCP server. Each node connected directly to MCP Trigger becomes a separate **tool** that AI clients can discover and call.

### Server settings

| Parameter              | Description                                   |
| ---------------------- | --------------------------------------------- |
| **Server Description** | Description of your MCP server for AI context |
| Server URL             | Copy this URL to use in your MCP client.      |
| **Version**            | Version identifier (any text, e.g., `1.0`)    |
| **Authentication**     | Enable to require API Key for access          |

### Tool configuration

Each node connected to MCP Trigger becomes a tool. Configure it in the first connected node's settings:

| Parameter            | Description                                                          |
| -------------------- | -------------------------------------------------------------------- |
| **Tool Name**        | Required. Unique tool identifier (e.g., `create_lead`, `send_email`) |
| **Tool Description** | Description helping AI understand when to use this tool              |

> ?? Important: Without **Tool Name**, the tool won't be visible to AI clients.

### Input parameters

Parameters define what data AI will pass when calling the tool.

| Field           | Description                                 |
| --------------- | ------------------------------------------- |
| **Key**         | Parameter name (e.g., `email`, `user_name`) |
| **Type**        | Select `fromMCP` for AI-fillable parameters |
| **Description** | Explanation for AI � what data to pass      |

**Example � lead creation tool parameters:**

| Key   | Type    | Description             |
| ----- | ------- | ----------------------- |
| name  | fromMCP | Contact name            |
| email | fromMCP | Contact email address   |
| phone | fromMCP | Phone number (optional) |

### Multiple tools

You can create **unlimited tools** in one MCP server by connecting multiple branches to MCP Trigger.

Each branch:

* Has its own **Tool Name** and **Description**
* Can contain any number of nodes
* Can use conditions, loops, AI agents, and any other Latenode nodes
* Operates independently

### Automatic routing

When connecting nodes to MCP Trigger, a **route filter** is created automatically. This filter routes requests to the correct tool branch.

> ?? The filter is auto-generated and non-editable.

## MCP Response

By default, the **output of the last node** in the tool chain is returned to the AI client. This often includes unnecessary data like headers or status codes.

**MCP Response** lets you specify exactly what data to return.

### When to use

* Return only specific fields (e.g., just `body` from HTTP response)
* Create a custom response structure
* Hide technical details from AI

### Configuration

Specify the data to return using variables from previous nodes.

## Example: Simple Echo Tool

### Step 1: Add MCP Trigger

1. Create a new scenario
2. Add **MCP Trigger** node
3. Set **Server Description**: `Test MCP server`

### Step 2: Configure Tool

1. Connect a Code node to MCP Trigger
2. Set **Tool Name**: `echo`
3. Set **Tool Description**: `Returns the provided text. Use for testing.`
4. Add parameter:
   * Key: `message`
   * Type: `fromMCP`
   * Description: `Text to return`

### Step 3: Return Result

In the Code node:

```javascript
return {
  result: msg.message
}
```

### Step 4: Deploy

1. Save the scenario
2. Copy URL from MCP Trigger
3. Connect to your MCP client

## Best practices

### Descriptions

Write clear descriptions so AI understands when and how to use your tools.

**? Good:**

```plain
Creates a task in Asana. Accepts task title and optional deadline.
Returns created task ID and link.
```

**? Bad:**

```plain
Creates task
```

### Parameters

* Use descriptive names (`user_email` not `param1`)
* Specify expected format in description (`Date in YYYY-MM-DD format`)
* Mark optional parameters

### Response data

* Return only necessary data via **MCP Response**
* Avoid exposing technical details
* Structure responses for AI readability

## Limitations

* MCP uses SSE (Server-Sent Events) � requires stable connection
* Tool execution time is limited by scenario timeout
* Binary data (files, images) requires additional handling

# Build with AI (Beta)

Check back later!

## AI Builder (Beta): scenario-wide assistant

Build with AI (Beta) in **Latenode Workflow Builder** helps you create, refine, and debug workflows using natural language.

Instead of manually picking nodes and wiring everything step-by-step, you can describe your goal and let the builder propose a workflow structure, connect nodes, and prefill configuration where possible. This can significantly reduce the time it takes to get a working scenario � especially for first drafts and troubleshooting.

## Working with the builder

1. **Describe what you want to automate**: start from an example prompt or type your requirements in plain language (what triggers the workflow, what data should be used, and what the result should be).
2. **Monitor the build process**: the builder shows progress as it iterates through planning, selecting nodes, connecting them, and setting parameters.
3. **Review and refine**: verify credentials, required inputs, and any assumptions; then ask the builder to adjust the workflow (for example, add error handling, logging, or additional branches).

{/* TODO: Add screenshot of Build with AI (Beta) in Latenode Workflow Builder */}

{/* Example:
  [Image: Build with AI (Beta) in Latenode]
  */}

### Billing

Work done by the **AI Builder (Beta)** is billed using **PnP tokens**.

## JavaScript AI Assistant: inside the JavaScript node

Use this when you want help writing, explaining, or debugging code **inside a JavaScript node**. You can open it directly in the node, or via the **AI Node** button.

### Billing

The JavaScript AI Assistant includes a **monthly number of free requests** depending on your plan. After the free limit is reached, requests are billed using **PnP tokens**.

See the current limits on the [pricing plans page](https://latenode.com/pricing-plans).

The builder does **not** send:

* Credential secrets (API keys, tokens, passwords)
* Past execution history of your workflows

# Authorizations

The **Authorizations** section is where all your app authorizations (Google, Slack, Zoom, etc.) used by scenario nodes are stored. The section is available in the app at: [app.latenode.com/connections](https://app.latenode.com/connections).

## What you can do in the section

* **Rename an authorization** — click the authorization name in the **Name** column, enter the new name, and save.
* **Reauthorize** — in the row menu, select **Reauthorize** to sign in to the service again (e.g. if the token expired or the password changed).
* **Delete an authorization** — in the row menu, select **Delete**. After confirmation, the authorization is permanently removed; scenario nodes that used it will need a new authorization.

For more on creating and configuring authorizations, see [Adding and Configuring Authorizations](/integrations/authorizations/adding-and-configuring-authorizations).

# Error Handling

All action nodes on Latenode include error handling settings in the advanced configuration. This feature allows you to automatically retry nodes when requests fail, and to repeatedly poll APIs until they return the expected result.

## When You Need This

### 1. API Returns an Error

The service you're calling returns an error — 500, 503, timeout, 429 "Too Many Requests", etc.

Normally, this would stop your scenario. But with retry enabled, the system automatically repeats the request a specified number of times with a defined pause between attempts.

**Enable:** `Retry if This Node Returns an Error`

**When to use this:**

* API sometimes responds with 500 or 503
* Timeouts occur during high load
* Service returns 429 when rate limit is exceeded

### 2. API Isn't Ready to Return Data Yet

The API formally responds successfully (status 200), but the task is still processing. This is especially important for content generation — video, audio, images, documents.

**When to use this:**

* Working with "Get Result" type nodes, where one node starts the process and returns a launch ID, and another retrieves the result after some time
* Applicable to almost all AI services (except text-based ones)

Typical example — video generation API:

```json
// First request — task queued
{"status": "queued", "id": "abc123"}

// After 5 seconds — processing
{"status": "processing", "id": "abc123"}

// After 10 seconds — done!
{"status": "completed", "url": "https://..."}
```

You need to wait for `completed` with a ready file link. You specify trigger words (`queued`, `processing`) — while they're present in the response, the node restarts after the specified time. Once `completed` arrives (without trigger words), the node completes successfully, and the result (file) is passed to the scenario for further processing.

**Enable:** `Retry if This Node Returns Incorrect Data`

  For content generation (video, audio, images): use 5-10 attempts with 20-30 second delays. For regular API errors: use 2-3 attempts with 3-5 second delays.

## Error Handling Settings

**Retry if This Node Returns an Error** — Enable automatic retry when the node throws an error.

**Retry if This Node Returns Incorrect Data** — Enable automatic retry when the response doesn't match the expected pattern.

**Number of Retry Attempts** — How many times to retry the request (default: 2)

**Delay between Retries (sec)** — Pause between attempts in seconds (default: 3)

**REGEXP (Regular Expression)** — Retry functionality is configured using regular expressions. Used for filtering errors and validating API responses.

### RegExp (Regular Expressions)

You specify **trigger words** — if they're found in the response, the node restarts after the specified time. If no trigger words are found — it's a success, the node completes and passes the result to the next step in the scenario.

**Important:** Without `.*`, the pattern will only work if the entire response exactly matches your word. Always write `.*(your_pattern).*`

**Pattern Examples:**

| Use Case                            | Pattern                                          |
| ----------------------------------- | ------------------------------------------------ |
| Restart while status is `queued`    | `.*queued.*`                                     |
| Restart while `queued` or `pending` | `.*(queued\|pending).*`                          |
| Restart during processing           | `.*(queued\|pending\|processing\|in_progress).*` |
| Restart while `ready` = false       | `.*"ready":\s*false.*`                           |

## Example: Waiting for Video Generation

**Task:** A video generation API first returns `in_progress`, then `queued`, and finally `completed` with a ready link.

**Configuration:**

1. Enable `Retry if This Node Returns Incorrect Data`
2. REGEXP (Regular Expression): `.*(in_progress|queued).*`
3. Number of Retry Attempts: 5
4. Delay between Retries (sec): 30

**How it works:**

* **Iteration 1:** `"status": "in_progress"` — Contains trigger word. Node restarts in 30 seconds.

* **Iteration 2:** `"status": "queued"` — Contains trigger word. Node restarts in 30 seconds.

* **Iteration 3:** `"status": "completed"` — No trigger words! Success. Node completes, result (video) is passed to the next node in the scenario.

**Summary:** The node restarts every 30 seconds until it receives a response without trigger words (`queued`, `in_progress`). While trigger words are present — data is NOT passed forward, the node restarts again. Once a successful response arrives (`completed`) — the file/data is passed to the scenario for further processing.

## Technical Details

* Uses **Go (RE2)** regular expression engine
* Supported: `\d` (digits), `\s` (whitespace), `\w` (word chars), `|` (or), `()` (groups)
* Not supported: lookahead `(?=...)` and lookbehind `(?<=...)`

## What's Next


</Cards>

# Interface

The **Scenarios** page is where you view, organize, and manage your scenarios and folders.

***

## Scenarios and folders

Existing scenarios are available on the **Scenarios** page. You can also organize scenarios into folders (including nested subfolders).

### Create a folder and move a scenario

1. Click **Add new folder** and enter the folder name.

2. Click **Save**.

3. In the **All Scenarios** table, open the scenario row menu (**⋯**).

4. Click **Move Scenario** and select the target folder.

  You can add subfolders by using **Add new folder** from the parent folder menu.



***

## All Scenarios table

You can view key attributes of each scenario in the **All Scenarios** table.

* **Scenario Name**: shown in the **Name** column. You can use the “gear” icon to switch the column to show the scenario’s webhook URL trigger instead of the name.

* **Scenario Status**: shown in the **Status** column (for example, **Pause** or **Active**).
* **Scenario Creation Date**: shown in the **Creation Date** column. You can use the “gear” icon to show the modification date instead of the creation date.

* **Scenario Type**: shown in the **Type** column.
* **Menu**: actions available for each scenario.

### Scenario menu

The scenario menu allows you to:

* **Enable** or **Disable** a scenario (changes status without opening the scenario).
* **Move** a scenario to a different folder.
* **Copy** a scenario to paste its content into external tools, or into another scenario.

  For details, see [Copying Scenarios and Nodes](./nodes/copy_nodes).

* **Export** a scenario (downloads a JSON file with the scenario content).
* **Delete** a scenario.

  After you confirm deletion in the modal, the scenario is permanently deleted.

***

## Searching and filtering

### Table filters

Use the filters above the table to show:

* **All**: scenarios in any status
* **Active Scenarios**: only active scenarios
* **Inactive Scenarios**: only paused scenarios

### Search and type filter

At the top of the page, you can use:

* **Search**: type a scenario name
* **Type filter**: filter by scenario type (for example, **All Scenarios**, **Scenario**, **Nodul**)

***

## Import & Export (folders and scenarios)

  If you’re looking specifically for transfer steps, see [Import & Export](./scenarios/import_export).

### Export a folder

You can export a folder only if it contains at least one scenario (empty folders can’t be exported).

1. Open the folder menu (next to the folder or from the folder row in the table).

2. Click **Export folder**.

After export, you’ll get an archive that contains folders and scenario JSON files. Folder names and hierarchy are preserved.

### Export a scenario

1. Open the scenario row menu (**⋯**).

2. Click **Export Scenario**.

### Import a scenario (or a folder)

You can import into **All Scenarios** or into a specific folder.

1. Open the menu next to **All Scenarios** or next to a folder.

2. Click **Import a folder or scenario**.

3. Select a file and confirm upload.
4. Verify that the imported scenario appears (by default, it is not active and not published).

  When importing a scenario, Latenode checks that the imported **Trigger on Webhook** node is unique by URL. If the URL is not unique, the import won’t proceed.

***

## Creating a scenario

To create a new scenario, click **Create new scenario** (or **Add new scenario**) on the scenarios list page.

After you click it, Latenode opens the scenario editor.

  You can add scenarios to specific folders by using **Add new scenario** from the folder menu.

# Routes

The platform has no dedicated router or merger nodes. To branch scenario execution or merge branches back together, you simply connect nodes with **routes** (connectors)—from one route point to another. Below is how to add routes and set conditions.

## Adding a Route

If a node is added through the **route point** of an existing node, a route between these nodes is established automatically.

If a node is added through the **Add Node** button, you should set up the route manually by connecting the two route points of the desired nodes in the correct direction.

## Route Configuration, Conditions

  When there are multiple routes through which the scenario can proceed, the route with a value of **TRUE** in the **Condition** field will be chosen.

**Example of a route** with a **Condition** value of **TRUE**:

* If 1.body.ValueWH = 45, then TRUE;
* If 1.body.ValueWH = 125, then FALSE.

After adding the **route**, you can access its settings by clicking the **Setup a filter** button.

In the **route** configuration window, you can:

* Change the route name in the **Name** field (**1**)
* Enter filter conditions in the **Condition** field (**2**), selecting logical operators for expressions in the **Operators** window (**3**) and values/parameters from previous nodes in the **Data** window (**4**)
* Save the changes by clicking the **Save** button (**5**)

## Fallback routes

A fallback route (reserve route) triggers **only when none of the outgoing routes from the node evaluates to TRUE**.

* At least one route is TRUE → execution continues through the matching route.
* All routes are FALSE → the fallback route is triggered (if configured).
* If no fallback route is configured → the scenario may stop at that node (because there is no valid next route).

  See also [Building scenarios](/visual-builder/scenarios/building-scenarios) for scenario examples using conditions in routes

# Administration

## Requirements

To follow the steps described below, you must already have a White Label administrator account on the Latenode platform, as well as a secret key for signing JWT tokens.

## Creating Custom Subscription Plans

Before you begin authorizing users from your organization within the Latenode platform, you need to create at least one subscription plan that will be automatically assigned to new users.

Initially, your organization will be provided with defined maximum and minimum values for various characteristics that can be configured for each plan. These characteristics are referred to as quotas.

List of configurable characteristics and quotas for your organization:

* **Execution Microcredits**

  A 1 platform credit equals 1 million microcredits. Depending on the minimum execution fee (see corresponding section), users may spend less than 1 credit per scenario execution.

* **Plug\&Play Microtokens**

  1 token equals 1 million microtokens. Used for Plug\&Play nodes (e.g., AI nodes without connection setup), as well as for some integrations.

* **Active Scenarios Limit**

* **Parallel Executions Limit**

* **Min Execution Charging Period (Microseconds)**

  1 second equals 1 million microseconds. By default, 1 credit (1 million microcredits) is charged for every 30 seconds of scenario execution. You can reduce the charging interval. For example, setting it to “3000000” will charge 0.1 credit (or 100,000 microcredits) every 3 seconds of execution.

* **AI Assistant Requests Limit**

* **Connected Accounts Limit**

* **Minimum Trigger Interval (Seconds)**

* **Execution History Availability Period (Minutes)**

### Creating a Plan

To create a plan:

1. Log in to the administrator dashboard using your username and password
2. Go to the "White Label" → "Plans" section
3. Click the "Create Plan" button
4. Fill in the plan name, its quotas, and click the "OK" button

  After clicking the "OK" button, a new entry will appear in the plans table.\
  You will need the ID of the created plan later. Its value can be found in the "ID" column.

Below is an interactive video showing how to create a plan.

## Subscription Management and Resource Usage Monitoring

To view the list of existing subscriptions, go to the “Subscriptions” section:

Here, you can see total credit and plug\&play token usage for the current billing period:

You’ll also see a table of usage per subscription for each user, with an option to cancel subscriptions:

To add a subscription for a user, click the “Add Subscription” button:

In the modal window, select the user and the subscription plan to assign:

## Managing the User List

To view the user list, go to the “Users” section. On this page, you can see the list of users along with their assigned subscriptions. The subscription assignment functionality is also available here:

  Users are not limited in the number of subscriptions.\
  When a user has more than one subscription, the best quotas will be applied.

# API Usage

## Creating an API Token

To use the API, you need to create an API token in your personal dashboard. This can be done in the “Access Tokens” section:

1. Log in to the platform
2. Go to White Label → Access Tokens section
3. Click on "Create Token" button
4. Fill out the token creation form and click "OK"
5. Copy the generated token

  This token is not stored on the platform's servers.\
  After clicking the "Done" button, you will no longer be able to access it.\
  Be sure to copy and store the token in a safe place.

## Using the API Token in Requests

To authenticate, add a `query` parameter named `AUTH_TOKEN` with the value of your created token from the “Access Tokens” section to each request. For example, to retrieve the list of created subscription plans, the request URL would look like this:

```jsx
https://api.latenode.com/latenode/v1/whitelabel/plans?AUTH_TOKEN=YOUR_API_TOKEN
```

This applies similarly to all other requests.

## Common Response Container for All Requests

Each request described in this article returns a standard response format:

```json
{
  "success": true,
  "request_id": "Spawv468Km1GW7ljPqGR",
  "data": {},
  "errors": []
}
```

The `data` field contains the data related to the specific endpoint. This `data` field will be described as the response format for each endpoint.

## Response Codes

For successful requests, the response code is always `200`. For failed requests, the response code can be either `200` or `500`. Always check the `success` field in the common response container. If an error occurs, this field will be `false`, and the `errors` array will not be empty.

An exception is unauthorized access to the API. In this case, the response code will always be `401`.

## Error Handling

The general format of an error response looks like this:

```json
{
  "success": false,
  "data": null,
  "errors": [
    {
      "message": "error message",
      "code": "error.code"
    }
  ],
  "request_id": "IvqOBSrwjaIozf2afu98"
}
```

To retrieve the error code, always refer to index `0` of the `errors` array. This index is reserved and always used to transmit the error code to the client.

For example, for unauthorized access to the API, you will receive the following response:

```json
{
  "success": false,
  "data": null,
  "errors": [
    {
      "message": "Unauthorized",
      "code": "auth.Unauthorized"
    }
  ],
  "request_id": "xbpvv24sh4m3mALFhyZk"
}
```

## Retrieve the List of Quotas for Your Organization

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/quotas
```

**Query Parameters:**

None

**Method:**

GET

**Response Format (`data`):**

```yaml
- Field:       quotas
  Type:        array
  Description: List of quotas
  Contents:
    - Field:       alias
      Type:        string
      Description: Quota alias. Possible values:
                   min_execution_charging_period_in_mcs — Minimum execution charge (Microseconds)
                   regular_microcredits — Execution microcredits
                   connected_accounts_limit — Connected accounts limit
                   parallel_executions_limit — Parallel executions limit
                   ai_assistant_request_limit — AI assistant request limit
                   plug_and_play_microcredits — Plug&Play microtokens
                   min_triggering_interval_in_seconds — Minimum trigger interval (Seconds)
                   active_scenarios_limit — Active scenarios limit
                   exec_history_availability_period_in_min — Execution history availability period (Minutes)
      ---
    - Field:       value
      Type:        object
      Description: Object with quota value
      Contents:
        - Field:       int64
          Type:        string
          Description: Numeric value of the quota (if applicable)
          ---
        - Field:       bool
          Type:        boolean
          Description: Boolean value of the quota (if applicable)

```

**Request Example:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/quotas?AUTH_TOKEN=YOUR_API_TOKEN'
```

**Response Example:**

```json
{
  "success": true,
  "request_id": "UrUNdGscccEE3TJViSL0",
  "data": {
    "quotas": [
      {
        "alias": "min_execution_charging_period_in_mcs",
        "value": {
          "int64": "3000000",
          "bool": false
        }
      },
      {
        "alias": "ai_assistant_request_limit",
        "value": {
          "int64": "5000",
          "bool": false
        }
      },
      {
        "alias": "parallel_executions_limit",
        "value": {
          "int64": "5000",
          "bool": false
        }
      },
      {
        "alias": "exec_history_availability_period_in_min",
        "value": {
          "int64": "6000",
          "bool": false
        }
      },
      {
        "alias": "plug_and_play_microcredits",
        "value": {
          "int64": "5000000000000",
          "bool": false
        }
      },
      {
        "alias": "active_scenarios_limit",
        "value": {
          "int64": "5000",
          "bool": false
        }
      },
      {
        "alias": "min_triggering_interval_in_seconds",
        "value": {
          "int64": "20",
          "bool": false
        }
      },
      {
        "alias": "connected_accounts_limit",
        "value": {
          "int64": "5000",
          "bool": false
        }
      },
      {
        "alias": "regular_microcredits",
        "value": {
          "int64": "10000000",
          "bool": false
        }
      }
    ]
  },
  "errors": []
}
```

## Retrieve List of Created Plans

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/plans
```

**Query Parameters:**

None

**Method:**

GET

**Response Format:**

```yaml
- Field:        plans
  Type:         array
  Description:  List of pricing plans
  Content:
    - Field:       id
      Type:        string
      Description: ID of the pricing plan
      ---
    - Field:       name
      Type:        string
      Description: Name of the pricing plan
      ---
    - Field:       status
      Type:        string
      Description: Current status of the pricing plan.
                   Possible values:
                   plan_status_archived – plan is archived
                   plan_status_active – plan is active
      ---
    - Field:       features
      Type:        array
      Description: List of pricing plan features
      Content:
        - Field:       alias
          Type:        string
          Description: Feature alias. Possible values:
                       min_execution_charging_period_in_mcs – Minimum execution charge (microseconds)
                       regular_microcredits – Execution microcredits
                       connected_accounts_limit – Connected accounts limit
                       parallel_executions_limit – Parallel executions limit
                       ai_assistant_request_limit – AI assistant request limit
                       plug_and_play_microcredits – Plug&Play microtokens
                       min_triggering_interval_in_seconds – Minimum trigger interval (seconds)
                       active_scenarios_limit – Active scenarios limit
                       exec_history_availability_period_in_min – Execution history availability period (minutes)
        ---
        - Field:       value
          Type:        object
          Description: Object containing the feature value
          Content:
            - Field:       int64
              Type:        string
              Description: If the feature is numeric, it is provided here
              ---
            - Field:       bool
              Type:        boolean
              Description: If the feature is boolean, it is provided here
      ---
    - Field:       created_at
      Type:        string
      Description: Date the plan was created
      ---
    - Field:       updated_at
      Type:        string
      Description: Date the plan was last updated

```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/plans?AUTH_TOKEN=YOUR_API_TOKEN'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "dPuN9LQBj1GUG805x27B",
  "data": {
    "plans": [
      {
        "id": "0",
        "name": "Demo Test Plan",
        "status": "plan_status_active",
        "features": [
          {
            "alias": "min_execution_charging_period_in_mcs",
            "value": {
              "int64": "3000000",
              "bool": false
            }
          },
          {
            "alias": "regular_microcredits",
            "value": {
              "int64": "10000000000",
              "bool": false
            }
          },
          {
            "alias": "connected_accounts_limit",
            "value": {
              "int64": "100",
              "bool": false
            }
          },
          {
            "alias": "parallel_executions_limit",
            "value": {
              "int64": "10",
              "bool": false
            }
          },
          {
            "alias": "ai_assistant_request_limit",
            "value": {
              "int64": "500",
              "bool": false
            }
          },
          {
            "alias": "plug_and_play_microcredits",
            "value": {
              "int64": "10000000",
              "bool": false
            }
          },
          {
            "alias": "min_triggering_interval_in_seconds",
            "value": {
              "int64": "120",
              "bool": false
            }
          },
          {
            "alias": "active_scenarios_limit",
            "value": {
              "int64": "100",
              "bool": false
            }
          },
          {
            "alias": "exec_history_availability_period_in_min",
            "value": {
              "int64": "1440",
              "bool": false
            }
          }
        ],
        "created_at": "2025-04-29T13:00:15Z",
        "updated_at": "2025-04-29T13:00:15Z"
      }
    ]
  },
  "errors": []
}
```

## Create a Pricing Plan

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/plans
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        name
  Type:         string
  Description:  Name of the new pricing plan
  ---

- Field:        features
  Type:         array
  Description:  List of features for the new plan
  Content:
    - Field:       alias
      Type:        string
      Description: Feature alias. Possible values:
                   min_execution_charging_period_in_mcs – Minimum execution charge (microseconds)
                   regular_microcredits – Execution microcredits
                   connected_accounts_limit – Connected accounts limit
                   parallel_executions_limit – Parallel executions limit
                   ai_assistant_request_limit – AI assistant request limit
                   plug_and_play_microcredits – Plug&Play microtokens
                   min_triggering_interval_in_seconds – Minimum trigger interval (seconds)
                   active_scenarios_limit – Active scenarios limit
                   exec_history_availability_period_in_min – Execution history availability period (minutes)
      ---
    - Field:       value
      Type:        object
      Description: Object containing the feature value
      Content:
        - Field:       int64
          Type:        string
          Description: Provided if value is numeric
          ---
        - Field:       bool
          Type:        boolean
          Description: Provided if value is boolean

```

**Response Format (`data`):**

```yaml
- Field:        plan
  Type:         object
  Description:  Object containing the created plan's data
  Content:
    - Field:       id
      Type:        string
      Description: ID of the new pricing plan
      ---
    - Field:       name
      Type:        string
      Description: Name of the new pricing plan
      ---
    - Field:       status
      Type:        string
      Description: Plan status. Possible values:
                   plan_status_archived – plan is archived
                   plan_status_active – plan is active
      ---
    - Field:       features
      Type:        array
      Description: List of features
      Content:
        - Field:       alias
          Type:        string
          Description: Feature alias
          ---
        - Field:       value
          Type:        object
          Description: Feature value object
          Content:
            - Field:       int64
              Type:        string
              Description: Numeric value, if applicable
              ---
            - Field:       bool
              Type:        boolean
              Description: Boolean value, if applicable
      ---
    - Field:       created_at
      Type:        string
      Description: Plan creation date
      ---
    - Field:       updated_at
      Type:        string
      Description: Plan last update date

```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/plans?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Plan Name",
    "features": [
        {
            "alias": "active_scenarios_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "connected_accounts_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "plug_and_play_microcredits",
            "value": {
                "int64": "1000000",
                "bool": false
            }
        },
        {
            "alias": "min_triggering_interval_in_seconds",
            "value": {
                "int64": "120",
                "bool": false
            }
        },
        {
            "alias": "min_execution_charging_period_in_mcs",
            "value": {
                "int64": "3000000",
                "bool": false
            }
        },
        {
            "alias": "exec_history_availability_period_in_min",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "regular_microcredits",
            "value": {
                "int64": "1000000",
                "bool": false
            }
        },
        {
            "alias": "parallel_executions_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "ai_assistant_request_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        }
    ]
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "Iit8HDuiyKSO6CuGGHzW",
  "data": {
    "plan": {
      "id": "0",
      "name": "Plan Name",
      "status": "plan_status_active",
      "features": [
        {
          "alias": "plug_and_play_microcredits",
          "value": {
            "int64": "1000000",
            "bool": false
          }
        },
        {
          "alias": "min_execution_charging_period_in_mcs",
          "value": {
            "int64": "3000000",
            "bool": false
          }
        },
        {
          "alias": "parallel_executions_limit",
          "value": {
            "int64": "1",
            "bool": false
          }
        },
        {
          "alias": "ai_assistant_request_limit",
          "value": {
            "int64": "1",
            "bool": false
          }
        },
        {
          "alias": "active_scenarios_limit",
          "value": {
            "int64": "1",
            "bool": false
          }
        },
        {
          "alias": "connected_accounts_limit",
          "value": {
            "int64": "1",
            "bool": false
          }
        },
        {
          "alias": "min_triggering_interval_in_seconds",
          "value": {
            "int64": "120",
            "bool": false
          }
        },
        {
          "alias": "exec_history_availability_period_in_min",
          "value": {
            "int64": "1",
            "bool": false
          }
        },
        {
          "alias": "regular_microcredits",
          "value": {
            "int64": "1000000",
            "bool": false
          }
        }
      ],
      "created_at": "2025-05-05T14:57:47.716Z",
      "updated_at": "2025-05-05T14:57:47.716Z"
    }
  },
  "errors": []
}
```

## Update Plan

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/plans/update
```

**Method:**

POST

**Query Parameters:**

None

**Body Parameters:**

  This API does not support partial updates.\
  The `name` and `features` fields are required and must contain the complete new (or old, if no changes are needed) values.

```yaml
- Field:        plan_id
  Type:         string
  Description:  ID of the plan to be updated
  ---
- Field:        name
  Type:         string
  Description:  New name for the plan
  ---
- Field:        features
  Type:         array
  Description:  Updated list of plan features
  Contents:
    - Field:       alias
      Type:        string
      Description: Feature alias. Possible values:
                   min_execution_charging_period_in_mcs — Minimum execution charge (Microseconds)
                   regular_microcredits — Execution microcredits
                   connected_accounts_limit — Connected accounts limit
                   parallel_executions_limit — Parallel executions limit
                   ai_assistant_request_limit — AI assistant request limit
                   plug_and_play_microcredits — Plug&Play microcredits
                   min_triggering_interval_in_seconds — Minimum triggering interval (Seconds)
                   active_scenarios_limit — Active scenarios limit
                   exec_history_availability_period_in_min — Execution history availability period (Minutes)
      ---
    - Field:       value
      Type:        object
      Description: Feature value object
      Contents:
        - Field:       int64
          Type:        string
          Description: Integer value, if applicable
          ---
        - Field:       bool
          Type:        boolean
          Description: Boolean value, if applicable

```

**Response Format (`data`):**

```json
Response body is empty. See the `success` field in the common response container.
```

**Request Example:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/plans/update?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "plan_id": "0",
    "name": "new plan name",
    "features": [
        {
            "alias": "active_scenarios_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "connected_accounts_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "plug_and_play_microcredits",
            "value": {
                "int64": "1000000",
                "bool": false
            }
        },
        {
            "alias": "min_triggering_interval_in_seconds",
            "value": {
                "int64": "120",
                "bool": false
            }
        },
        {
            "alias": "min_execution_charging_period_in_mcs",
            "value": {
                "int64": "3000000",
                "bool": false
            }
        },
        {
            "alias": "exec_history_availability_period_in_min",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "regular_microcredits",
            "value": {
                "int64": "1000000",
                "bool": false
            }
        },
        {
            "alias": "parallel_executions_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        },
        {
            "alias": "ai_assistant_request_limit",
            "value": {
                "int64": "1",
                "bool": false
            }
        }
    ]
}'
```

**Response Example:**

```json
{
  "success": true,
  "request_id": "Spawv468Km1GW7ljPqGR",
  "data": {},
  "errors": []
}
```

## Archive Plan

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/plans/archive
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        plan_id
  Type:         string
  Description:  ID of the plan to be archived

```

**Response Format (`data`):**

```json
Response body is empty. See the `success` field in the common response container.

```

**Request Example:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/plans/archive?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "plan_id": "0"
}'
```

**Response Example:**

```json
{
  "success": true,
  "request_id": "rG0F38nQ4aE8Gy0TDh3C",
  "data": {},
  "errors": []
}
```

## Get Subscription List

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/subscriptions/list
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        options
  Type:         object
  Description:  Request options
  Contents:
    - Field:       include_consumption
      Type:        boolean
      Description: Whether to include resource consumption info in the response
  ---

- Field:        filters
  Type:         object
  Description:  Filters for selecting subscriptions
  Contents:
    - Field:       user_id
      Type:        string
      Description: Filter by user ID. Can be empty
      ---
    - Field:       statuses
      Type:        array
      Description: Array of subscription statuses for filtering.
                   Possible values:
                   subscription_status_active — active subscription
                   subscription_status_cancelled — cancelled subscription
      ---
    - Field:       consumption
      Type:        object
      Description: Resource consumption filters
      Contents:
        - Field:       resources
          Type:        array
          Description: Resource types to analyze consumption.
                       Possible values:
                       billing_resource_execution_credits — execution credits
                       billing_resource_plug_and_play_credits — Plug&Play credits
          ---
        - Field:       start
          Type:        string
          Description: Start date of the analysis period. If not set, defaults to first usage
          ---
        - Field:       end
          Type:        string
          Description: End date of the analysis period. If not set, defaults to current time

```

**Response Format (`data`):**

```yaml
- Field:        subscriptions
  Type:         array
  Description:  List of subscriptions
  Contents:
    - Field:       id
      Type:        string
      Description: Subscription ID
      ---
    - Field:       plan_id
      Type:        string
      Description: Associated plan ID
      ---
    - Field:       user_id
      Type:        string
      Description: User ID
      ---
    - Field:       status
      Type:        string
      Description: Current subscription status
                   Possible values:
                   subscription_status_active — active subscription
                   subscription_status_cancelled — cancelled subscription
      ---
    - Field:       consumption
      Type:        object
      Description: Resource consumption info (if requested)
      Contents:
        - Field:       execution_credits
          Type:        object
          Description: Execution microcredits usage
          Contents:
            - Field:       total
              Type:        string
              Description: Total consumed credits
              ---
        - Field:       plug_and_play_credits
          Type:        object
          Description: Plug&Play microtokens usage
          Contents:
            - Field:       total
              Type:        string
              Description: Total consumed tokens
      ---
    - Field:       created_at
      Type:        string
      Description: Subscription creation date
      ---
    - Field:       cancelled_at
      Type:        string
      Description: Subscription cancellation date (if cancelled)

```

**Request Example:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/subscriptions/list?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "options": {
        "include_consumption": true
    },
    "filters": {
        "user_id": "my_test_user_1",
        "statuses": ["subscription_status_active"],
        "consumption": {
            "resources": ["billing_resource_execution_credits"],
            "start": "2025-04-04T15:09:23.879Z",
            "end": "2025-05-05T15:09:23.879Z"
        }
    }
}'
```

**Response Example:**

```json
{
  "success": true,
  "request_id": "HMI8jfzAIiuGH8bB2J1F",
  "data": {
    "subscriptions": [
      {
        "id": "0",
        "plan_id": "0",
        "user_id": "my_test_user_1",
        "status": "subscription_status_active",
        "consumption": {
          "execution_credits": {
            "total": "1"
          },
          "plug_and_play_credits": null
        },
        "created_at": "2025-05-05T14:19:39Z",
        "cancelled_at": null
      }
    ]
  },
  "errors": []
}
```

## Assign a Subscription to a User

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/subscriptions
```

**Method:**

POST

**Query Parameters:**

None

**Body Parameters:**

```yaml
- Field:       user_id
  Type:        string
  Description: The ID of the user to whom the subscription will be assigned
  ---

- Field:       plan_id
  Type:        string
  Description: The ID of the pricing plan for the subscription

```

**Response Format (`data`):**

```yaml
- Field:       subscription
  Type:        object
  Description: Object containing the created subscription data
  Contents:
    - Field:       id
      Type:        string
      Description: Subscription ID
      ---
    - Field:       plan_id
      Type:        string
      Description: ID of the associated pricing plan
      ---
    - Field:       user_id
      Type:        string
      Description: ID of the user
      ---
    - Field:       status
      Type:        string
      Description: Current status of the subscription.
                   Possible values:
                   subscription_status_active — active subscription
                   subscription_status_cancelled — cancelled subscription
      ---
    - Field:       consumption
      Type:        null
      Description: Always null, since no usage could have occurred yet
      ---
    - Field:       created_at
      Type:        string
      Description: Subscription creation timestamp
      ---
    - Field:       cancelled_at
      Type:        null

```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/subscriptions?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": "my_test_user_1",
    "plan_id": "0"
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "VbCf0CMPIJ8m3pc4u9vI",
  "errors": [],
  "data": {
    "subscription": {
      "id": "0",
      "plan_id": "0",
      "user_id": "my_test_user_1",
      "status": "subscription_status_active",
      "consumption": null,
      "created_at": "2025-05-05T15:26:10.320Z",
      "cancelled_at": null
    }
  }
}
```

## Cancel a Subscription

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/subscriptions/cancel
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:       subscription_id
  Type:        number
  Description: ID of the subscription to be cancelled

```

**Response Format (`data`):**

```json
No response body. Refer to the `success` field in the common response container.

```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/subscriptions/cancel?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "subscription_id": "0"
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "J9KWRLlKIlP0tTPQOj6B",
  "errors": [],
  "data": {}
}
```

## Get Users List

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/users/list
```

**Method:**

POST

**Query Parameters:**

None

**Body Parameters:**

```yaml
- Field:        options
  Type:         object
  Description:  Request options
  Contents:
    - Field:       include_subscriptions
      Type:        boolean
      Description: Whether to include subscription information
      ---
    - Field:       include_consumption
      Type:        boolean
      Description: Whether to include resource consumption information
  ---

- Field:        filters
  Type:         object
  Description:  Resource consumption filters
  Contents:
    - Field:       consumption
      Type:        object
      Description: Consumption filters
      Contents:
        - Field:       resources
          Type:        array
          Description: Types of resources to filter by. Possible values:
                       billing_resource_execution_credits — execution credits
                       billing_resource_plug_and_play_credits — Plug&Play credits
          ---
        - Field:       start
          Type:        string
          Description: Start date of the period. If not provided, defaults to first usage
          ---
        - Field:       end
          Type:        string
          Description: End date of the period. If not provided, defaults to the current time

```

**Response Format (`data`):**

```yaml
- Field:       users
  Type:        array
  Description: List of users
  Contents:
    - Field:       user_id
      Type:        string
      Description: Unique user ID
      ---
    - Field:       subscriptions
      Type:        array
      Description: User's subscriptions (if include_subscriptions = true)
      Contents:
        - Field:       id
          Type:        string
          Description: Subscription ID
          ---
        - Field:       plan_id
          Type:        string
          Description: ID of the associated pricing plan
          ---
        - Field:       user_id
          Type:        string
          Description: User ID
          ---
        - Field:       status
          Type:        string
          Description: Current subscription status.
                       Possible values:
                       subscription_status_active — active subscription
                       subscription_status_cancelled — cancelled subscription
          ---
        - Field:       consumption
          Type:        object
          Description: Resource consumption info (if include_consumption = true)
          Contents:
            - Field:       execution_credits
              Type:        object
              Description: Execution microcredits usage
              Contents:
                - Field:       total
                  Type:        string
                  Description: Total used credits
                ---
            - Field:       plug_and_play_credits
              Type:        object
              Description: Plug&Play token usage
              Contents:
                - Field:       total
                  Type:        string
                  Description: Total used tokens
          ---
        - Field:       created_at
          Type:        string
          Description: Subscription creation timestamp
          ---
        - Field:       cancelled_at
          Type:        string
          Description: Subscription cancellation timestamp (if cancelled)
      ---
    - Field:       spaces
      Type:        array
      Description: Spaces to which the user is connected
      Contents:
        - Field:       id
          Type:        string
          Description: Space ID
          ---
        - Field:       name
          Type:        string
          Description: Space name

```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/users/list?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "options": {
        "include_subscriptions": true,
        "include_consumption": true
    },
    "filters": {
        "consumption": {
            "resources": ["billing_resource_execution_credits"],
            "start": "2025-05-01T15:00:00.000Z",
            "end": "2025-05-06T15:00:00.000Z"
        }
    }
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "iPl0JoZDJmQZnjkxoJXU",
  "data": {
    "users": [
      {
        "user_id": "my_test_user_1",
        "subscriptions": [
          {
            "id": "0",
            "plan_id": "0",
            "user_id": "my_test_user_1",
            "status": "subscription_status_active",
            "consumption": {
              "execution_credits": {
                "total": "1"
              },
              "plug_and_play_credits": null
            },
            "created_at": "2025-05-05T14:19:39Z",
            "cancelled_at": null
          },
          {
            "id": "0",
            "plan_id": "0",
            "user_id": "my_test_user_1",
            "status": "subscription_status_cancelled",
            "consumption": null,
            "created_at": "2025-05-05T15:26:10Z",
            "cancelled_at": null
          }
        ],
        "spaces": [
          {
            "id": "32",
            "name": "test_space_1"
          },
          {
            "id": "53",
            "name": "test_space_2"
          }
        ]
      }
    ]
  },
  "errors": []
}
```

## Get Resource Consumption Report

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/reports/consumption
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        start
  Type:         string
  Description:  The start date of the period. If not provided, the first usage date is used.
  ---

- Field:        end
  Type:         string
  Description:  The end date of the period. If not provided, the current time is used.
  ---

- Field:        options
  Type:         object
  Description:  Options for generating the report
  Contents:
    - Field:       include_total
      Type:        boolean
      Description: Whether to include total consumption across all users.
      ---
    - Field:       include_per_user
      Type:        boolean
      Description: Whether to include consumption details for each user.
  ---

- Field:        filters
  Type:         object
  Description:  Filters for resource types
  Contents:
    - Field:       resources
      Type:        array
      Description: A list of resource types. Possible values:
                   billing_resource_execution_credits — execution credits
                   billing_resource_plug_and_play_credits — Plug&Play credits

```

**Response Format (`data`):**

```yaml
- Field:        total
  Type:         object
  Description:  Total resource consumption (if include_total = true)
  Contents:
    - Field:       execution_credits
      Type:        object
      Description: Consumption of execution microcredits
      Contents:
        - Field:       total
          Type:        string
          Description: Total number of credits used
      ---
    - Field:       plug_and_play_credits
      Type:        object
      Description: Consumption of Plug&Play microtokens
      Contents:
        - Field:       total
          Type:        string
          Description: Total number of tokens used
  ---

- Field:        users
  Type:         array
  Description:  Consumption details per user (if include_per_user = true)
  Contents:
    - Field:       user_id
      Type:        string
      Description: User ID
      ---
    - Field:       consumption
      Type:        object
      Description: Resource consumption
      Contents:
        - Field:       execution_credits
          Type:        object
          Description: Consumption of execution microcredits
          Contents:
            - Field:       total
              Type:        string
              Description: Total number of credits used
          ---
        - Field:       plug_and_play_credits
          Type:        object
          Description: Consumption of Plug&Play tokens
          Contents:
            - Field:       total
              Type:        string
              Description: Total number of tokens used
  ---

- Field:        start
  Type:         string
  Description:  Start date of the report period
  ---

- Field:        end
  Type:         string
  Description:  End date of the report period
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/reports/consumption?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "start": "2025-05-01T15:00:00.000Z",
    "end": "2025-05-06T15:00:00.000Z",
    "options": {
        "include_total": true,
        "include_per_user": true
    },
    "filters": {
        "resources": [
            "billing_resource_execution_credits",
            "billing_resource_plug_and_play_credits"
        ]
    }
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "Vwauyaa7L4lOjn4ZK2Xy",
  "data": {
    "total": {
      "execution_credits": {
        "total": "1"
      },
      "plug_and_play_credits": null
    },
    "users": [
      {
        "user_id": "my_test_user_1",
        "consumption": {
          "execution_credits": {
            "total": "1"
          },
          "plug_and_play_credits": null
        }
      }
    ],
    "start": "2025-05-01T15:00:00Z",
    "end": "2025-05-06T15:00:00Z"
  },
  "errors": []
}
```

## Credit charge

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/billing/resource
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        user_id
  Type:         string
  Description:  USER ID
  ---

- Field:        resource
  Type:         string
  Description:  Added resource type
  ---

- Field:        quantity
  Type:         int64
  Description:  Added resource quantity
```

**Response Format (`data`):**

```json
Response body is empty. See the `success` field in the common response container.
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/billing/resource?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": "10011",
    "resource": "billing_resource_plug_and_play_credits",
    "quantity": 10
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "Spawv468Km4877fGR",
  "data": {},
  "errors": []
}
```

## Add user to space

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/space/access/grant
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        grantee_user_id
  Type:         string
  Description:  Internal ID of the user connected to the space
  ---

- Field:        owner_user_id
  Type:         string
  Description:  Internal ID of the space owner user. Skipped when add_to_tenant_space = true
  ---

- Field:        add_to_tenant_space
  Type:         boolean
  Description:  If true, user will only be connected to the tenant space
  ---

- Field:        role_id
  Type:         int64
  Description:  ID of the provided role

```

**Response Format (`data`):**

```json
Response body is empty. See the `success` field in the common response container.
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/space/access/grant?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "grantee_user_id": "test_user_2",
    "owner_user_id": "test_user_1",
    "add_to_tenant_space": false,
    "role_id": 3
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "Spawakhdfm4877fGR",
  "data": {},
  "errors": []
}
```

## Delete user from space

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/space/access/revoke
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        grantee_user_id
  Type:         string
  Description:  Internal ID of the user connected to the space
  ---

- Field:        owner_user_id
  Type:         string
  Description:  Internal ID of the space owner user. Skipped when revoke_from_tenant_space = true
  ---

- Field:        revoke_from_tenant_space
  Type:         boolean
  Description:  If true, user will only be revoked to the tenant space
```

**Response Format (`data`):**

```json
Response body is empty. See the `success` field in the common response container.
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/space/access/revoke?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "grantee_user_id": "test_user_2",
    "owner_user_id": "test_user_1",
    "revoke_from_tenant_space": false
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "Spa78377hfwakhdfm48GR",
  "data": {},
  "errors": []
}
```

## Update space name

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/space/update
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        space_id
  Type:         string
  Description:  ID of the space
  ---

- Field:        name
  Type:         string
  Description:  New name of the space
```

**Response Format (`data`):**

```yaml
- Field: space
  Type: object
  Description: The changed space
  Contents:
    - Field: id
      Type: string
      Description: ID of the space
      ---
    - Field: name
      Type: string
      Description: The new name of the space
      ---
    - Field: status
      Type: string
      Description: Status of the name
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/space/update?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "space_id": "32",
    "name": "new_name"
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "KMBhDbT7734zuaR7CR",
  "data": {
    "space": {
      "id": "32",
      "name": "new_name",
      "status": "new"
    }
  },
  "errors": []
}
```

## Get scenarios from space

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/scenarios/list
```

**Method:**

POST

**Body Parameters:**

```yaml
- Field:        space_id
  Type:         string
  Description:  ID of the space
  ---

- Field:        options
  Type:         object
  Description:  Response options
  Contents:
    - Field: count_only
      Type: boolean
      Description: If true only count will be provided
```

**Response Format (`data`):**

```yaml
- Field: scenarios_count
  Type: string
  Description: Total number of scenarios available for the tenant
  ---

- Field: folders
  Type: array
  Description: List of scenario folders with scenarios
  ---

- Field: scenarios
  Type: array
  Description: List of scenarios
  Contents:
    - Field: id
      Type: string
      Description: Unique identifier of the scenario
      ---

    - Field: title
      Type: string
      Description: Scenario title
      ---

    - Field: description
      Type: string
      Description: Scenario description
      ---

    - Field: node_count
      Type: string
      Description: Number of nodes in the scenario
      ---

    - Field: active
      Type: boolean
      Description: Indicates whether the scenario is active
      ---

    - Field: status
      Type: string
      Description: Current scenario status (e.g. deployed)
      ---

    - Field: last_version
      Type: string
      Description: Latest deployed version of the scenario
      ---

    - Field: folder_id
      Type: string
      Description: Identifier of the folder the scenario belongs to
      ---

    - Field: created_at
      Type: string
      Description: Scenario creation timestamp in ISO 8601 format
      ---

    - Field: last_modified_at
      Type: string
      Description: Timestamp of the last scenario modification in ISO 8601 format
      ---

    - Field: created_by
      Type: object
      Description: Information about the user who created the scenario
      Contents:
        - Field: user_id
          Type: string
          Description: Identifier of the user who created the scenario
          ---

    - Field: last_modified_by
      Type: object
      Description: Information about the user who last modified the scenario
      Contents:
        - Field: user_id
          Type: string
          Description: Identifier of the user who last modified the scenario
          ---
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/scenarios/list?AUTH_TOKEN=YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "space_id": 32,
    "options": {
        "count_only": false
    }
}'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "Y3X5oDrjJz93j4hgg3CXcb",
  "data": {
    "scenarios_count": "1",
    "folders": [],
    "scenarios": [
      {
        "id": "29adf0adfa7df8df6adff",
        "title": "Test scenario",
        "node_count": "2",
        "active": true,
        "status": "deployed",
        "last_version": "3",
        "folder_id": "",
        "description": "",
        "created_at": "2025-04-15T17:46:56.055Z",
        "last_modified_at": "2025-04-15T17:50:12.217Z",
        "created_by": {
          "user_id": "test_user_1"
        },
        "last_modified_by": {
          "user_id": "test_user_1"
        }
      }
    ]
  },
  "errors": []
}
```

## Get execution

**URL:**

```jsx
https://api.latenode.com/latenode/v1/whitelabel/scenarios/execution
```

**Method:**

GET

**Query Parameters:**

```yaml
- Field:        execution_id
  Type:         string
  Description:  ID of the execution
```

**Response Format (`data`):**

```yaml
- Field: execution
  Type: object
  Description: Information about scenario execution
  Contents:
    - Field: id
      Type: string
      Description: Unique identifier of the execution
      ---

    - Field: scenario_id
      Type: string
      Description: Identifier of the executed scenario
      ---

    - Field: version
      Type: string
      Description: Scenario version used for execution
      ---

    - Field: status
      Type: string
      Description: Execution status (e.g. success, error)
      ---

    - Field: environment
      Type: string
      Description: Execution environment (e.g. dev, prod)
      ---

    - Field: nodes
      Type: array
      Description: List of executed nodes and their statuses
      Contents:
        - Field: id
          Type: string
          Description: Unique identifier of the node execution instance
          ---

        - Field: node_id
          Type: string
          Description: Identifier of the node in the scenario
          ---

        - Field: status
          Type: string
          Description: Execution status of the node (e.g. success, error)
          ---

    - Field: error
      Type: object
      Description: Error details if execution failed
      Contents:
        - Field: entity_id
          Type: string
          Description: Identifier of the entity where the error occurred
          ---

        - Field: entity_type
          Type: string
          Description: Type of entity where the error occurred (e.g. node)
          ---

        - Field: message
          Type: string
          Description: Error message description
          ---

    - Field: gateways
      Type: array
      Description: List of gateways evaluated during execution
      Contents:
        - Field: id
          Type: string
          Description: Unique identifier of the gateway execution instance
          ---

        - Field: node_id
          Type: string
          Description: Identifier of the gateway node in the scenario
          ---

        - Field: purpose
          Type: string
          Description: Purpose of the gateway (e.g. output)
          ---

        - Field: routes
          Type: array
          Description: List of evaluated routes for the gateway
          Contents:
            - Field: condition
              Type: object
              Description: Condition evaluated for the route
              Contents:
                - Field: type
                  Type: string
                  Description: Type of the condition
                  ---

                - Field: expression
                  Type: object
                  Description: Condition expression details
                  Contents:
                    - Field: value
                      Type: string
                      Description: Expression value
                      ---

            - Field: node_id
              Type: string
              Description: Identifier of the next node for this route
              ---
```

**Example Request:**

```bash
curl --location 'https://api.latenode.com/latenode/v1/whitelabel/scenarios/execution?AUTH_TOKEN=YOUR_API_TOKEN&execution_id=adf7asdbfdad99da8f6adfdf' \
--header 'Content-Type: application/json'
```

**Example Response:**

```json
{
  "success": true,
  "request_id": "xsHJOZ7v4623g46kk2i",
  "data": {
    "execution": {
      "id": "698c5bd8f76d78f6s87d6f",
      "scenario_id": "868247bj2h832424j272423",
      "version": "8",
      "status": "error",
      "environment": "dev",
      "nodes": [
        {
          "id": "698c5bd8f76d78f6s87d6f_698c5bf3b485b357900bc763",
          "node_id": "28374bj4bj3b23b4b433b43",
          "status": "success"
        },
        {
          "id": "698c5bd8f76d78f6s87d6f_698c5bf3bba69ee56218634a",
          "node_id": "698c50823bj23b823b23n4",
          "status": "error"
        }
      ],
      "error": {
        "entity_id": "698c50823bj23b823b23n4",
        "entity_type": "node",
        "message": "Get \"\": unsupported protocol scheme \"\""
      },
      "gateways": [
        {
          "id": "698c5bd8f76d78f6s87d6f_698c5bf3bba69ee562186349",
          "node_id": "28374bj4bj3b23b4b433b43",
          "routes": [
            {
              "condition": {
                "type": "",
                "expression": {
                  "value": ""
                }
              },
              "node_id": "698c50823bj23b823b23n4"
            }
          ],
          "purpose": "output"
        }
      ]
    }
  },
  "errors": []
}
```

# Embedded SDK functions

Starting from SDK version 0.1.5, Latenode Embedded SDK allows programmatic interaction with the platform directly from your application.

You can now execute, deploy, and manage scenarios.

All methods are **asynchronous** unless otherwise specified and return a `Promise`.

***

## **Run Once**

Runs the currently opened scenario once.

```tsx
async runOnce(): Promise<void>
```

**Description:**

Triggers a one-time execution of the current scenario in test mode.

**Example:**

```tsx
await sdk.runOnce();
```

***

## **Save**

Saves the currently opened scenario.

```tsx
async save(): Promise<void>
```

**Description:**

Saves all current changes in the scenario editor.

**Example:**

```tsx
await sdk.save();
```

***

## **Deploy**

Deploys the currently opened scenario.

```tsx
async deploy(): Promise<void>
```

**Description:**

Publishes the scenario and applies all saved changes to the production environment.

**Example:**

```tsx
await sdk.deploy();
```

***

## **Activate / Deactivate Scenario**

Toggles the active state of the current scenario.

```tsx
toggleActiveScenarioState(): void
```

**Description:**

Activates or deactivates the scenario depending on its current state.

**Example:**

```tsx
sdk.toggleActiveScenarioState();
```

***

## **Create Empty Scenario**

Creates an empty scenario with the specified name.

```tsx
async createEmptyScenario(title?: string): Promise<void>
```

**Parameters:**

* `title` *(optional, string)* — name of the new scenario.

**Example:**

```tsx
await sdk.createEmptyScenario("New empty scenario");
```

***

## **Get Node Types**

Retrieves all available node types that can be added to a scenario.

```tsx
async getNodeTypes(): Promise<NodeType[]>
```

**Returns:**

An array of node type objects.

**Example:**

```tsx
const nodeTypes = await sdk.getNodeTypes();
console.log(nodeTypes);
```

***

## **Add New Node**

Adds a new node of the specified type to the scenario canvas.

```tsx
async addNewNode(nodeTypeId: string, title?: string): Promise<void>
```

**Parameters:**

* `nodeTypeId` *(string, required)* — type identifier of the node (retrieved via `getNodeTypes()`).
* `title` *(optional, string)* — name for the new node.

**Example:**

```tsx
const types = await sdk.getNodeTypes();
await sdk.addNewNode(types[0].id, "My new node");
```

***

## **Get Scenario Webhooks URLs**

Returns an array of webhook URLs for all webhook nodes in the current scenario.

```tsx
async getScenarioWebhooksUrls(): Promise<ScenarioWebhookEntry[]>
```

**Interface:**

```tsx
interface ScenarioWebhookEntry {
  nodeId: string;
  url: {
    dev: string;
    prod: string;
  };
}
```

**Example:**

```tsx
const urls = await sdk.getScenarioWebhooksUrls();
console.log(urls);
```

***

## **Create Webhook Scenario**

Creates a new scenario with a webhook node and returns its URLs.

```tsx
async createWebhookScenario(
  scenarioTitle?: string,
  nodeTitle?: string
): Promise<ScenarioWebhookEntry>
```

**Parameters:**

* `scenarioTitle` *(optional, string)* — name for the scenario.
* `nodeTitle` *(optional, string)* — name for the webhook node.

**Returns:**

Webhook URLs for both `dev` and `prod` environments.

**Example:**

```tsx
const webhook = await sdk.createWebhookScenario("Incoming data", "Webhook");
console.log(webhook.url.dev);
```

***

## **Set Scenario Running State Changed Listener**

Registers an event listener that triggers when the scenario's running state changes (e.g., when it starts or stops running).

```tsx
setScenarioRunningStateChangedListener(
  handler: ({ isScenarioRunning }: { isScenarioRunning: boolean }) => void
): () => void
```

**Parameters:**

* `handler` *(function)* — callback function that receives the scenario running state.

**Returns:**

A cleanup function to remove the listener.

**Example:**

```tsx
const removeListener = sdk.setScenarioRunningStateChangedListener(({ isScenarioRunning }) => {
  console.log("Scenario running:", isScenarioRunning);
});

// later, to remove listener
removeListener();
```

# White Label

Offer Latenode's automation capabilities to your own customers under your brand.

</Cards>

# Installing the embedded SDK

This article describes how to integrate the Latenode platform into your project using the SDK.

### Container Setup Inside the Website

To use the SDK, you need to prepare a container where the iframe will be rendered. Ensure that the container is already present in the DOM tree.

### SDK Configuration

Add the following tag to your website:

```html

```

Once this script is executed, the `LatenodeEmbeddedSDK` class will be added to the global `window` object.

## Methods of SDK

### configure

The method allows rendering an `iframe`. To do this, you need to call the method on an instance of the `LatenodeEmbeddedSDK` class.

```jsx
const latenodeSDK = new LatenodeEmbeddedSDK();
latenodeSDK.configure({
	allowCookies: true,
  token: 'USER_JWT_TOKEN',
  container: 'lowCodeDivContainer',
  ui: {
  "scenarios": {
    "hideEmptyScenariosGreetings": false,
    "hideExploreAppsButton": true,
    "logo": {
      "src": "YOUR_LOGO_URL",
      "style": {
        "width": 150,
        "height": 150,
        "margin": ""
      }
    },
    "activeStateFilterStyle": "",
    "activeStateFilter": {
      "variant": "",
      "selectedBgColor": "",
      "selectedTextColor": "",
      "unselectedBgColor": "",
      "unselectedTextColor": ""
    },
    "foldersPanelWidth": 250,
    "buttons": {
      "createScenario": {
        "iconSvg": "",
        "type": "",
        "padding": "",
        "transparent": false
      },
      "startWithTemplate": {
        ... same structure as createScenario ...
      },
      "importScenario": {
        ... same structure as createScenario ...
      },
      "addNewScenario": {
        ... same structure as createScenario ...
      },
      "addNewFolder": {
        ... same structure as createScenario ...
      }
    },
    "reverseMainActionBtnsOrder": false,
    "paddingTop": "",
    "scenariosTable": {
      "scenarioIconBgColor": "",
      "sortArrow": {
        "activeColor": "",
        "inactiveColor": ""
      }
    },
    "searchInput": {
      "borderRadius": ""
    }
  },
  "scenario": {
    "showGrid": false,
    "nodeTypeList": {
      "requestNewAppURL": "YOUR_REQUESTING_APP_URL",
      "categoriesSideBar": {
        "backgroundColor": ""
      },
      "nodeTypeListNodeBackgroungSvg": "",
      "listTitleFont": {
        "fontSize": "",
        "fontWeight": "",
        "fontFamily": "",
        "color": ""
      },
      "nodeTitleFont": {
        ... same structure as listTitleFont ...
      },
      "nodeDescriptionFont": {
        ... same structure as listTitleFont ...
      }
    },
    "actionBlock": {
      "buttons": {
        "runOnce": {
          "iconSvg": "",
          "type": "",
          "padding": "",
          "transparent": false
        },
        "deploy": {
          ... same structure as runOnce ...
        },
        "save": {
          ... same structure as runOnce ...
        },
        "addNode": {
          ... same structure as runOnce ...
        },
        "aiNode": {
          ... same structure as runOnce ...
        },
        "aiBuilder": {
          ... same structure as runOnce ...
        },
        "alignNodes": {
          ... same structure as runOnce ...
        },
        "addSticker": {
          ... same structure as runOnce ...
        },
        "undo": {
          ... same structure as runOnce ...
        },
        "redo": {
          ... same structure as runOnce ...
        }
      },
      "mainLineStyle": {
        "background": "",
        "paddingTop": 0,
        "paddingBottom": 0,
        "paddingLeft": 0,
        "paddingRight": 0,
        "boxShadow": "",
        "borderRadius": ""
      },
      "activeSwitchLabelFont": {
        "fontSize": "",
        "fontWeight": "",
        "fontFamily": "",
        "color": ""
      }
    },
    "nodeDataPanel": {
      "operators": {
        "textColor": "",
        "backgroundColor": ""
      },
      "buttons": {
        "newAuthorization": {
          "iconSvg": "",
          "type": "",
          "padding": "",
          "transparent": false
        }
      }
    },
    "scenarioNodeBackgroundSvg": "",
    "templates": {
      "buttons": {
        "cloneThisTemplate": {
          "iconSvg": "",
          "type": "default",
          "padding": "4px 16px",
          "transparent": true
        }
	    }
    }
  },
  "main": {
    "hideSideMenu": false,
    "documentationURL": "YOUR_DOCS_URL"
  },
  "theme": {
    "font": {
      "fontFamily": "",
      "load": {
        "googleFontFamily": "",
        "custom": {
          "url": "",
          "format": ""
        }
      }
    },
    "primaryColor": "#2394ae",
    "button": {
      "default": {
        "default": {
          "backgroundColor": "white",
          "textColor": "#2394ae",
          "borderColor": "#2394ae"
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      },
      "primary": {
        "default": {
          ... same structure as default ...
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      },
      "action": {
        "default": {
          "backgroundColor": "#233849",
          "textColor": "white",
          "borderColor": "#233849"
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      },
      "success": {
        "default": {
          "backgroundColor": "#233849",
          "textColor": "white",
          "borderColor": "#233849"
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      },
      "danger": {
        "default": {
          "backgroundColor": "#bf161f",
          "textColor": "white",
          "borderColor": "#bf161f"
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      },
      "subtle": {
        "default": {
          "backgroundColor": "white",
          "textColor": "#2394ae",
          "borderColor": "#2394ae"
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      },
      "text": {
        "default": {
          "backgroundColor": "",
          "textColor": "",
          "borderColor": ""
        },
        "active": {
          ... same structure as default ...
        },
        "hover": {
          ... same structure as default ...
        },
        "disabled": {
          ... same structure as default ...
        },
        "borderWidth": "2px",
        "borderRadius": "20px",
        "gap": "",
        "padding": ""
      }
    },
    "input": {
      "borderRadius": "20px"
    },
    "switch": {
      "checkedBackgroundColor": "",
      "uncheckedBackgroundColor": "",
      "height": "",
      "width": "",
      "padding": ""
    },
    "scenario": {
      "backgroundColor": "#f1f1f1",
      "nodeTypeList": {
        "nodeBackgroundSize": ""
      },
      "historyDrawer": {
        "headerBgColor": "",
        "alert": {
          "backgroundColor": "",
          "borderColor": "",
          "iconColor": "",
          "linkColor": ""
        }
      },
      "unsavedChangesModal": {
        "mainActionBtnColor": ""
      },
      "nodeSettings": {
        "headerBgColor": "#256AF4",
        "bodyBgColor": "#CFD8DB",
        "footerBgColor": "#1A1B20"
	    }
    },
    "templates": {
      "tabBtnsColor": "red"
    }
  },
  "translations": {
    "currentLng": "",
    "overrides": {
      "en": {
        "latenode_scenariosPage_allScenariosTitleLabel": "All scenarios"
      }
    }
  }
},
  navigation: {
    handler: ({ route }) => {
      console.log('user navigated to ' + route);
    }
  }
}).then(() => {
 console.log('iframe rendered');
});
```

This method returns a `Promise` that resolves once the `iframe` has been loaded and rendered inside the specified `container`.

### Configuration Parameters

```yaml
auth:
  - field: token
    type: string
    required: true
    description: JWT token that was generated for the user

embed:
  - field: container
    type: string | HTMLElement
    required: true
    description: ID of the container or a DOM element reference where the iframe will be rendered

ui:
  scenarios:
    - field: hideEmptyScenariosGreetings
      type: boolean
      required: false
      description: Hide greeting message when scenario list is empty

    - field: hideExploreAppsButton
      type: boolean
      required: false
      description: Hide "Explore Apps" button

    - field: logo.src
      type: string
      required: false
      description: Custom logo URL

    - field: logo.style.width
      type: number | string
      required: false
      description: Logo width (px or css value)

    - field: logo.style.height
      type: number | string
      required: false
      description: Logo height (px or css value)

    - field: logo.style.margin
      type: string
      required: false
      description: CSS margin for logo

    - field: activeStateFilterStyle
      type: string
      required: false
      description: Style of active state filter (e.g. "tabs")

    - field: activeStateFilter.variant
      type: string
      required: false
      description: Variant of active state filter

    - field: activeStateFilter.selectedBgColor
      type: string
      required: false
      description: Background color for selected filter

    - field: activeStateFilter.selectedTextColor
      type: string
      required: false
      description: Text color for selected filter

    - field: activeStateFilter.unselectedBgColor
      type: string
      required: false
      description: Background color for unselected filter

    - field: activeStateFilter.unselectedTextColor
      type: string
      required: false
      description: Text color for unselected filter

    - field: foldersPanelWidth
      type: number
      required: false
      description: Width of the folders panel in px

    - field: buttons.[name].iconSvg
      type: string
      required: false
      description: Icon for scenario button (inline SVG)

    - field: buttons.[name].type
      type: string
      required: false
      description: Button type (e.g. "primary", "text")

    - field: buttons.[name].padding
      type: string
      required: false
      description: CSS padding for button

    - field: buttons.[name].transparent
      type: boolean
      required: false
      description: Transparent background flag for button

    - field: reverseMainActionBtnsOrder
      type: boolean
      required: false
      description: Reverse order of main action buttons

    - field: paddingTop
      type: string
      required: false
      description: Padding from the top of scenarios area

    - field: scenariosTable.scenarioIconBgColor
      type: string
      required: false
      description: Background color of scenario icons

    - field: scenariosTable.sortArrow.activeColor
      type: string
      required: false
      description: Color of active sort arrow

    - field: scenariosTable.sortArrow.inactiveColor
      type: string
      required: false
      description: Color of inactive sort arrow

    - field: searchInput.borderRadius
      type: string
      required: false
      description: Border radius for search input

  scenario:
    - field: showGrid
      type: boolean
      required: false
      description: Show grid background in scenario editor

    - field: nodeTypeList.requestNewAppURL
      type: string
      required: false
      description: URL for requesting new app integration

    - field: nodeTypeList.categoriesSideBar.backgroundColor
      type: string
      required: false
      description: Sidebar background color in node type list

    - field: nodeTypeList.nodeTypeListNodeBackgroungSvg
      type: string
      required: false
      description: Custom background SVG for node type list

    - field: nodeTypeList.listTitleFont.[*]
      type: string
      required: false
      description: Font properties for list titles

    - field: nodeTypeList.nodeTitleFont.[*]
      type: string
      required: false
      description: Font properties for node titles

    - field: nodeTypeList.nodeDescriptionFont.[*]
      type: string
      required: false
      description: Font properties for node descriptions

    - field: actionBlock.buttons.[name].iconSvg
      type: string
      required: false
      description: Inline SVG icon for action button

    - field: actionBlock.buttons.[name].type
      type: string
      required: false
      description: Button type (primary, text, etc.)

    - field: actionBlock.buttons.[name].padding
      type: string
      required: false
      description: CSS padding for action button

    - field: actionBlock.buttons.[name].transparent
      type: boolean
      required: false
      description: Transparent background flag for action button

    - field: actionBlock.mainLineStyle.[*]
      type: string | number
      required: false
      description: CSS style settings for main action line

    - field: actionBlock.activeSwitchLabelFont.[*]
      type: string
      required: false
      description: Font properties for active switch labels

    - field: nodeDataPanel.operators.textColor
      type: string
      required: false
      description: Text color for operators in node data panel

    - field: nodeDataPanel.operators.backgroundColor
      type: string
      required: false
      description: Background color for operators in node data panel

    - field: nodeDataPanel.buttons.newAuthorization.[*]
      type: string | boolean
      required: false
      description: Button properties for "New Authorization" action

    - field: scenarioNodeBackgroundSvg
      type: string
      required: false
      description: Background SVG for scenario nodes

    - field: templates.buttons.cloneThisTemplate.iconSvg
      type: string
      required: false
      description: Icon for cloninig scenario button (inline SVG)

    - field: templates.buttons.cloneThisTemplate.type
      type: string
      required: false
      description: Button type (e.g. "primary", "text")

    - field: templates.buttons.cloneThisTemplate.padding
      type: string
      required: false
      description: CSS padding for button

    - field: templates.buttons.cloneThisTemplate.transparent
      type: string
      required: false
      description: Transparent background flag for button

  main:
    - field: hideSideMenu
      type: boolean
      required: false
      description: Hide main side navigation menu

    - field: documentationURL
      type: string
      required: false
      description: Custom documentation link

  theme:
    - field: font.fontFamily
      type: string
      required: false
      description: Base font family

    - field: font.load.googleFontFamily
      type: string
      required: false
      description: Google Font family name to load

    - field: font.load.custom.url
      type: string
      required: false
      description: Custom font URL

    - field: font.load.custom.format
      type: string
      required: false
      description: Custom font format (woff2, ttf, etc.)

    - field: primaryColor
      type: string
      required: false
      description: Primary accent color

    - field: button.[type].[state].[*]
      type: string
      required: false
      description: Button styles per type and state

    - field: input.borderRadius
      type: string
      required: false
      description: Border radius for input fields

    - field: switch.[*]
      type: string | number
      required: false
      description: Switch element style properties

    - field: scenario.backgroundColor
      type: string
      required: false
      description: Background color of scenario area

    - field: scenario.nodeTypeList.nodeBackgroundSize
      type: string
      required: false
      description: Size of node background image in scenario

    - field: scenario.historyDrawer.headerBgColor
      type: string
      required: false
      description: Background color of history drawer header

    - field: scenario.historyDrawer.alert.[*]
      type: string
      required: false
      description: Alert styles in history drawer

    - field: scenario.unsavedChangesModal.mainActionBtnColor
      type: string
      required: false
      description: Color of main action button in unsaved changes modal

    - field: scenario.nodeSettings.headerBgColor
      type: string
      required: false
      description: Background color of node settings popup header

    - field: scenario.nodeSettings.bodyBgColor
      type: string
      required: false
      description: Background color of node settings popup body

    - field: scenario.nodeSettings.footerBgColor
      type: string
      required: false
      description: Background color of node settings popup footer

    - field: templates.tabBtnsColor
      type: string
      required: false
      description: Color of selected tab

  translations:
    - field: currentLng
      type: string
      required: false
      description: Current language code (e.g. "en", "ru")

    - field: overrides.[lng].[key]
      type: string
      required: false
      description: Override translation string for specific language

navigation:
  - field: navigation.handler
    type:
      (data: { route: string }) => void
    required: false
    description: Navigation event handler inside the iframe. This function will be called each time the application route changes
```

### navigate

This method allows navigation within the iframe. For example:

```jsx
LatenodeSDK.navigate({ to: '/scenarios' });
```

### cleanup

The SDK has side effects in its operation. To properly finalize work with the `iframe`, it is recommended to call the cleanup method, which will remove all registered callbacks in `window`, for example:

```jsx
LatenodeSDK.cleanup();
```

# Overview

Latenode can be embedded into your frontend and styled to look like part of your application.

In general, embedding Latenode consists of three stages:

1. Getting to know with the [admin panel](./administration.mdx)
2. [Installing the embedded SDK](./installing-the-embedded-sdk.mdx) and [authorizing users](./user-authorization.mdx) through your existing authentication system (so they don't need a separate Latenode login)

Latenode is embedded in your application as an iframe, and users who are already logged into your platform get all the benefits of the system as if it were a native part of your application.

# User Sandbox

## User Authorization in the Platform

A [sandbox repository](https://github.com/latenode-com/whitelabel-example) is available for testing user authorization. You can find setup instructions in the repository's [README.md](https://github.com/latenode-com/whitelabel-example/blob/main/README.md).

### Token Generation

1. After launching the sandbox, open the "JWT Generation" section. This section helps you generate a JWT token for a user in your organization. You can use this token to authorize the user in the embedded mode of the Latenode platform.

2. Paste your private key into the "Private Key" input field and select the signing algorithm corresponding to your key pair.

3. Fill in the Tenant ID, User ID, and Plan ID fields, where:

   `Tenant ID` – Required. Your tenant ID in the Latenode platform

   `User ID` – Required. A unique string that clearly identifies the user in your organization

   `Plan ID` – Optional. The ID of the subscription plan to be assigned to the user during their first login. For future logins, this field is not required. In this example, the created plan ID is "35"

4. Click the "Generate Token" button to create a new JWT token, which you can copy using the "Copy" button.

  Token generation is done locally without network requests. This ensures your private key is not sent to the Latenode platform or any third parties.

Below is an interactive video showing token generation

### Using token

Once the JWT token is generated, go to the "White Label" section. Paste the copied value into the "JWT Token" field. In the "UI Config JSON" field, insert the following:

```json
{
  "scenarios": {
    "hideEmptyScenariosGreetings": true
  },
  "main": {
    "hideSideMenu": false
  }
}
```

Then click the "Init" button. After that, an embedded version of the Latenode platform will appear on the right side of the screen, with the new user already authorized, in this case with ID = `tu_2`.

# User Authentication

## **User Authentication**

A key advantage of Latenode integration is its authentication simplicity. Users sign in through your application, receiving a special token to access Latenode functions. The system uses JSON Web Token (JWT), secured by a unique private key from Latenode. The JWT contains user data from your system. After Latenode platform verifies the JWT signature, the user receives client privileges and can work with integrations within their account.

## Signature Private Key

Before you can generate a JWT, you will need a valid **signature key** from Latenode. Contact support to obtain the key.

  Keep this key in a secure location – it will be used to verify user authentication in your application.

## **Creating and Signing JWT**

Now that you have the signature key, you can create and sign a JSON Web Token (JWT). To do this, you can use one of the [libraries](https://jwt.io/libraries) suitable for your backend.

The JWT that you generate for the user must have the following properties:

* **Header** must specify the encryption algorithm and look something like this::

  ```json
  {
    "alg": "RS512",
    "typ": "JWT"
  }
  ```

  Supported JWT algorithms:

  * RS256, RS384, RS512
  * ES256, ES256K, ES384, ES512
  * PS256, PS384, PS512
* Private signature key issued by Latenode
* Payload with the following data:

  * `tenant_id` - Required numeric field. Provided by the Latenode platform.
  * `user_id` - Required field. ID of the user in your organization. A unique string value that uniquely identifies the user.
  * `plan_id` - Optional numeric field. ID of the tariff plan that will be set for the user **if this is the user's first authorization on the platform**. This field does not need to be filled in afterwards.
  * `no_personal_space` — Optional boolean field. If `true`, the user will be created **without a personal space**.
  * `grant_access` — Optional array that allows assigning the user to one or more existing spaces with specified roles.
    **Required** if `no_personal_space` is set to `true`.
  * `exp` — Required numeric field. The token is considered valid until the specified timestamp  is reached.

  JWT `Payload` example

  ```json
  {
    "tenant_id": 1,
    "user_id": "1",
    "plan_id": 35,
    "no_personal_space": true,
    "grant_access": [{
      "space_id": 2,
      "role_id": 2
    }],
    "exp": 1768417200
  }
  ```

In this example:

* The user belongs to tenant **1**.
* The user will be created **without a personal space**.
* Since `no_personal_space` is `true`, the `grant_access` field is required.
* The user will receive access to the space with ID **2** and be assigned the role with ID 2.
* The token is considered valid until `1768417200`.

### **Available Roles**

Latenode provides a role-based access model for users within each space.

Each role defines what actions a user can perform.

| **Role**                   | **Description**                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Admin** (`role_id`: 1)   | Has full access to the space and all its configurations. Can create, edit, and delete scenarios, manage users, and change space settings. Only **one admin** can exist per space. Created automatically when a new space is created. |
| **Manager** (`role_id`: 2) | Has almost the same permissions as the Admin but **cannot add or remove users** from the space.                                                                                                                                      |
| **No-code** (`role_id`: 3) | Can create, edit, delete, activate/deactivate, and move scenarios between folders. Does **not** have access to folder, user or space management.                                                                                     |
| Read only (`role_id`: 4)   | Can view and run scenarios. Does **not** have access to folder, user or space management.                                                                                                                                            |

Creating a JWT token is sufficient to register or authorize a user on the Latenode platform. Use this token in the [`configure`](https://www.notion.so/Installing-the-embedded-SDK-1b657d45a06780a8af8bca11990b981c?pvs=21) sdk method. If the user is new, they will be automatically registered and authorized.

***

## ⚠️ Known Browser Limitations (Safari & Incognito Mode)

When using the standard authentication flow inside an iframe, some browsers — notably **Safari** and **incognito/private mode** in Chrome — may block third-party cookies. Since our authorization relies on cookies inside an iframe, this may lead to failed login attempts.

**Recommendations:**

* If you're using **Safari**, you can:
  * Add the iframe parent domain to the list of trusted sites
  * Or disable "Prevent cross-site tracking" in Safari settings
* If you're using **incognito mode**, please use a regular browser session instead — incognito mode disables third-party cookie storage by default.

# Plans Overview

You can always find the latest plan details and current pricing on our pricing page: **[latenode.com/pricing-plans](https://latenode.com/pricing-plans)**.

## Choosing a plan

When evaluating a plan, consider both the included limits and the features you need:

* **Free**: Best for exploring the platform, building and testing scenarios, and running a small number of workflows.
* **Mini**: Great for individuals who run workflows occasionally and want access to advanced features like **webhook triggers**, **database**, and **headless browser**.
* **Start**: Best value for production usage with frequent runs (higher workflow execution quota, faster billing granularity, and a 1-minute trigger interval).
* **Team**: Ideal for teams that need high throughput (more parallel executions, longer history, more connected accounts, and team collaboration).
* **Custom plan**: Best for enterprise requirements (custom limits, custom webhook domain, static egress IP, dedicated support).

## How credits are consumed

Latenode charges **only for processing time**, not per node/operation.

* **What is a CPU credit**: 1 credit equals **30 seconds** of scenario execution time.
* **How charging works**: during execution, credits are consumed based on total run time. The minimum charge per execution depends on your plan (see table above).

# January 28 — Platform Updates

</div>

* Improved iterator connection logic: right connector is hidden until the top one is used (to prevent incorrect scenario assembly)
* Added Retry mechanism and enhanced error handling in scenario nodes

</div>

**New Apps:**

* ChartMogul
* Expensify
* Straico
* Agendor
* Holded
* ActiveTrail
* Quickfile
* Luxafor
* Freshservice
* Clearout
* Detrack
* Tookan
* Lob
* RepairShopr

**Updates:**

* LlamaCloud - updates and parsing
* OpenAI Speech - updates
* Bitrix24 - new node
* Browser Use - API update
* Clio - updates
* Netsuite - fixes
* Telegram / WhatsApp - personal account support
* Systeme.io - fixes
* Mailchimp - fixes

</div>

* Fixed issue with empty arrays and null in AI agent responses
* Fixed scroll in long forms (no longer jumps to top when inserting functions)
* Large number of fixes in AI builder logic
* Minor frontend and integration fixes

</div>

* New page: [Error Handling](/visual-builder/error-handling)

# February 11 — Platform Updates

</div>

**AI Agent — stability and UX**

* Validation for `fromAIAgent` / `fromMCP`: when invalid characters are entered in parameters, the UI indicates incorrect format
* Agent chat no longer crashes if the second argument (description) is missing in `fromAIAgent`
* Fix for `letAIDecide` button: spaces in parameter keys are now replaced with underscores, invalid characters are trimmed
* Important: the first argument is now taken from the parameter's system key (`key`), not from `title` — this avoids issues with invalid names in MCP and the agent
* Chat now reacts to node settings changes in real time without saving — system message, session ID, and connected tools apply immediately
* Chat now shows clear errors in various cases: two tools with the same name, two `fromAIAgent` calls with the same first argument, Structured Output enabled without the word JSON in the prompt, invalid Output JSON Schema
* Fixed issue with Think tool being invoked incorrectly when settings were unsaved

**AI Agent — tool execution results**

* Tool execution results now return detailed information: status, IDs, start time, size, errors, and other data
* The agent now sees the actual execution output, not just `success` / `error` — so it can detect and fix incorrectly filled parameters on its own
* Limits added for data size: input — 1500 characters, output — 3000 characters; a note is added when content is trimmed

**AI Builder — performance**

* Backend updated architecturally
* Average time before calling the LLM reduced by 4 seconds

**Subscription — scenario management on plan change**

* On downgrade or subscription cancellation, the user receives an email and has 24 hours to manage active scenarios

* After that period, excess scenarios are deactivated automatically

* Updated execution history button on the canvas: more visible, vertical bar removed

</div>

**New apps:**

* Azure DevOps
* Paystack
* Axonaut
* Hunter
* Datadog
* Geckoboard
* CircleCI
* Workbooks CRM
* Reamaze
* Infobip
* Salesflare

**Updates:**

* Tally - new nodes
* Twitter/X - new nodes
* Telegram / WhatsApp / LinkedIn Personal Accounts - fixes
* Pinterest - fixes

**New models:**

* OpenAI Speech-to-Text
* Anthropic Claude Opus 4.6

</div>

* Fixed routing bug: interface flickering when opening connection settings between nodes
* Fixed: WhatsApp, Telegram, and LinkedIn personal account nodes were not appearing in the PNP category filter in the app list
* Fixed duplicate URL generation in Webhook and MCP Trigger when creating multiple scenarios without page reload
* Fixed: duplicate MCP Trigger URLs are now correctly rejected on save

# February 25 — Platform Updates

</div>

**Interface improvements**

* Improved animations and interface smoothness
* Added background blur when opening execution history and some other windows
* Improved modal rendering
* Improved scroll in lists with many items
* Added scroll for the user Spaces list
* Improved interface behavior with many authorizations
* Removed square brackets in Select field mapping mode

**Scenario import**

* Fixed import logic: scenario type (scenario, module, etc.), scenario structure, and visibility settings are now preserved correctly on import

**Performance**

* Optimized scenario list loading and some platform API endpoints

**OAuth authorization**

* Improved internal OAuth logic: the platform can now add integrations for services with complex or non-standard OAuth flows that were previously problematic

</div>

**New apps:**

* Endorsal
* RemoveBG
* Snipcart
* Svix
* Zoho Bookings
* Zoho Assist
* Google Slides
* Zoho People
* Convert Spreadsheet to JSON
* DataForSEO
* Gladia.io
* Table Parser
* Zoho Recruit
* SendGrid
* Mailbluster
* TinyURL
* TMetric
* Freedcamp
* JMESPath
* Sentry
* Uploadcare
* Zenkit
* Zixflow

**Updates:**

* LinkedIn Unipile - updates
* Google Tasks - update
* YouTube - fixes
* PostgreSQL - fixes
* Etsy - fixes
* ElevenLabs - new nodes and model
* Claude - update
* OpenAI Responses - update
* Mistral - new nodes
* Replicate - update
* Jira - updates
* Bitrix24 - updates
* Evolution AI Cloud - updates

</div>

* Fixed issue where node execution indicator could hang after stopping Run Once
* Fixed a number of AI Builder errors
* Fixed scenario hang issues
* Improved platform stability and backend optimizations

# 2026 Updates

Choose a date to see the release notes:

* [February 25 — Platform Updates](/changelog/2026/02-25)
* [February 11 — Platform Updates](/changelog/2026/02-11)
* [January 28 — Platform Updates](/changelog/2026/01-28)

# Modifying data in a collection

When you want to modify data in a collection, you need to select objects and apply a set of modifiers to them.

### There are two ways to select objects:

* specify the identifier of a specific object

### There are two ways to select objects:

* specify the identifier of a specific object
* apply a set of filters to select multiple objects (see [querrying collection](../querying_collection.mdx))

## Modifiers

We use `YAML` for the modifier format.

```json
- Field:        path
  Type:         string
  Description:  Address inside the object that is being modified.
                If you specify "." then the modification will replace the entire
                content of the object.
---
- Field:        set
  Type:         Expression
  Description:  Expression to calculate the value.
```

### Note

All filter sets start with the keyword `conditions` , and all modifier sets start with the keyword `items`

### Example

Let's imagine that we have an object that we can get using the following filter:

```yaml
conditions:
  - operation: equal
    query:
      field: "object_id"
    expected:
      value: "5bd4b778-1f7f-4fce-ab89-dd6eb6dfaf98"
```

Object value:

```yaml
{
  "test": 123
}
```

Let's apply modifiers

```yaml
items:
  - path: "."
    set:
      value:
        a:
          b:
            id: "123"
  - path: "a.b.i"
    set:
      value: 123
  - path: "a.b.s"
    set:
      value: "string"
  - path: "a.b.f"
    set:
      field: "object_id"
  - path: "a.b.p"
    set:
      path: "a.b.i"
```

The first modifier replaces all objects with the described object.

```yaml
{
  "a": {
    "b": {
      "id": "123"
    }
  }
}
```

The second modifier adds a value of type number to the object.

```yaml
{
  "a": {
    "b": {
      "id": "123",
      "i": 123
    }
  }
}
```

The third modifier adds a value of type string to the object.

```yaml
{
  "a": {
    "b": {
      "id": "123",
      "i": 123,
      "s": "string"
    }
  }
}
```

The fourth modifier adds a value of type string to the object, and the value is taken from the object\_id field from the system information about the object.

```yaml
{
  "a": {
    "b": {
      "id": "123",
      "i": 123,
      "s": "string",
      "f": "aebe4239-0fb9-4e87-9f52-9dc8228467e8"
    }
  }
}
```

The fifth modifier adds a value to the object taken from the same object after the previous modifiers.

```yaml
{
  "a": {
    "b": {
      "id": "123",
      "i": 123,
      "s": "string",
      "f": "aebe4239-0fb9-4e87-9f52-9dc8228467e8",
      "p": 123
    }
  }
}
```

## Expressions

This section lists all the expressions that you can use in the conditions.

```yaml
- Expression:  Field
  Field:       field
  Type:        string
  Description: This extension allows you to get the value of a record field in its entirety.
               Below you can see the available values for this extension:
               • object_id
               • value
               • created_at
---
- Expression:  Path
  Field:       path
  Description: This extension allows you to look inside an object value.
               To view nested values, use the dot separator.
               Examples:
               • a
               • a.b
               • a.b.c
---
- Expression:  Value
  Field:       value
  Type:        string, number, array, object, bool
  Description: This extension allows you to specify a specific value for further comparison
```

# Querying Collection

When querying data from a collection, you can use a set of constraints to filter objects.

To filter, you need to specify a set of conditions (filters if you like).

We use `YAML` for the request format.

## Note

All filter sets start with the keyword `conditions` , all filters at the first level are applied by the `AND` condition

```yaml
conditions:
  - {operation}
  - {operation}
```

### Example

```yaml
conditions:
  - operation: equal
    query:
      path: name
    expected:
      value: Jon
```

## Conditions

```
- Field:       operation
  Type:        string
  Description: Each condition must contain an operation field
  ---
- Field:       Condition body
  Description: Depending on the selected operation, the set of fields may vary
```

## Operations

This section lists all the operations that you can use in the conditions.

```
- Operation:   and
  Fields:      conditions
  Type:        []Condition
  Description: Contains a set of conditions
---
- Operation:   or
  Fields:      conditions
  Type:        []Condition
  Description: Contains a set of conditions
---
- Operation:   equal
  Fields:      query, expected
  Type:        Expression
  Description: query: Expression for calculating the value,
               expected: Expression for calculating the expected value
---
- Operation:   not_equal
  Fields:      query, expected
  Type:        Expression
  Description: query: Expression for calculating the value,
               expected: Expression for calculating the expected value
---
- Operation:   has_keys
  Fields:      keys
  Type:        []string
  Description: Set of paths to check for availability
---
- Operation:   not_has_keys
  Fields:      keys
  Type:        []string
  Description: Set of paths to check for unavailability
```

## Expressions

This section lists all the expressions that you can use in the conditions.

```
- Expression:  Field
  Field:       field
  Type:        string
  Description: This extension allows you to get the value of a record field in its entirety.
               Below you can see the available values for this extension:
               • object_id
               • value
               • created_at
---
- Expression:  Path
  Field:       path
  Description: This extension allows you to look inside an object value.
               To view nested values, use the dot separator.
               Examples:
               • a
               • a.b
               • a.b.c
---
- Expression:  Value
  Field:       value
  Type:        string, number, array, object, bool
  Description: This extension allows you to specify a specific value for further comparison
```

### Note for Path expression

Consider an example object and two filters

```jsx
{
  "t1": {
    "ddd": "ewwflsdk",
    "grz": "d123",
    "aaa": "123"
  }
}
```

The filter that will work:

```yaml
conditions:
  - operation: equal
    query:
      path: t1.grz
    expected:
      value: d123
```

Filter that won't work:

```yaml
conditions:
  - operation: equal
    query:
      path: t1
    expected:
      value:
        grz: d123
```

This behavior is due to the fact that we compare the entire result obtained in the `Path` expression with the entire result obtained in the `Value` expression.

For cases when you need to compare only part of the received object, you can create an expression from two or more filters.

For example, the following expression will ignore part of the object at the address `t1` but compare two values from the nested object at once:

```yaml
conditions:
  - operation: equal
    query:
      path: t1.grz
    expected:
      value: d123
  - operation: equal
    query:
      path: t1.ddd
    expected:
      value: ewwflsdk
```

## Filtering examples

All examples will be carried out based on the following input data.

```json
[
  {
    "storage_id": "c9d6b296-ab57-435e-a28b-6b207b9674b8",
    "collection_name": "users",
    "object_id": "8f842609-b710-479b-96d3-0b0f3be62571",
    "value": {
      "name": "Marta",
      "age": 35,
      "info": {
        "verified": true
      },
      "labels": [
        "author",
        "reader"
      ]
    },
    "created_at": "2006-01-02 15:04:05.999999999 -0700 MST"
  },
  {
    "storage_id": "c9d6b296-ab57-435e-a28b-6b207b9674b8",
    "collection_name": "users",
    "object_id": "88c90cbe-6aab-43dd-81cb-e7a37580e813",
    "value": {
      "name": "Joe",
      "age": 40,
      "info": {
        "verified": false,
        "banned": true
      },
      "labels": [
        "reader",
        "critic"
      ]
    },
    "created_at": "2006-01-02 15:04:05.999999999 -0700 MST"
  }
]
```

## Basic Filter

First, let's find a match by path in object value. For this we will need the operator `equal`.

```yaml
conditions:
  - operation: equal
    query:
      path: name
    expected:
      value: Marta
```

This will return all the objects where the field name is equal to Marta.

```json
{
  "storage_id": "c9d6b296-ab57-435e-a28b-6b207b9674b8",
  "collection_name": "users",
  "object_id": "8f842609-b710-479b-96d3-0b0f3be62571",
  "value": {
    "name": "Marta",
    "age": 35,
    "info": {
      "verified": true
    },
    "labels": [
      "author",
      "reader"
    ]
  },
  "created_at": "2006-01-02 15:04:05.999999999 -0700 MST"
}
```

Now let's find all users whose name is not Marta. For this we will need the operator `not_equal`.

```yaml
conditions:
  - operation: not_equal
    query:
      path: name
    expected:
      value: Marta
```

This will return all the objects where the field name is not equal to Marta. In our case, we will get an object with the user Joe.

```json
{
  "storage_id": "c9d6b296-ab57-435e-a28b-6b207b9674b8",
  "collection_name": "users",
  "object_id": "88c90cbe-6aab-43dd-81cb-e7a37580e813",
  "value": {
    "name": "Joe",
    "age": 40,
    "info": {
      "verified": false,
      "banned": true
    },
    "labels": [
      "reader",
      "critic"
    ]
  },
  "created_at": "2006-01-02 15:04:05.999999999 -0700 MST"
}
```

Now let's request all users with a complete match of a part of the object.

```yaml
conditions:
  - operation: equal
    query:
      path: info
    expected:
      value:
        verified: false
        banned:   true
```

The value expression automatically determines the value type (string, object, list, number).

In this case, we will again get the user object Joe.

```json
{
  "storage_id": "c9d6b296-ab57-435e-a28b-6b207b9674b8",
  "collection_name": "users",
  "object_id": "88c90cbe-6aab-43dd-81cb-e7a37580e813",
  "value": {
    "name": "Joe",
    "age": 40,
    "info": {
      "verified": false,
      "banned": true
    },
    "labels": [
      "critic"
    ]
  },
  "created_at": "2006-01-02 15:04:05.999999999 -0700 MST"
}
```

## Multiple Filters

### Filtering with OR

```yaml
conditions:
  - operation: or
    conditions:
      - operation: equal
        query:
          path: info.banned
        expected:
          value:true
      - operation: equal
        query:
          path: info.verified
        expected:
          value:false
```

### Filtering with AND

```yaml
conditions:
  - operation: and
    conditions:
      - operation: equal
        query:
          path: info.banned
        expected:
          value:true
      - operation: equal
        query:
          path: info.verified
        expected:
          value:false
```

## Nested Filters

You can nest conditions within each other to get the best filtering result.

```yaml
conditions:
  - operation: and
    conditions:
      - operation: equal
        query:
          path: age
        expected:
          value: 40
      - operation: or
        conditions:
          - operation: equa;
            query:
              path: info.verified
            expected:
              value:false
          - operation: equal
            query:
              path: info.banned
            expected:
              value:true
```

## Search for complex objects

Sometimes you may want to find an object where the fields of the object are somehow related to each other.

In this case, you can use two Path expressions and compare their values with each other.

```yaml
conditions:
  - operation: equal
    query:
      path:
        path: first_name
      expected:
        path: last_name
```

In this example, if someone specifies the same first and last name, we will get such users in the response.

You can also combine different types of expressions in one query.

```yaml
conditions:
  - operation: and
    conditions:
      - operation: equal
        query:
          path: first_name
        expected:
          path: last_name
      - operation: not_equal
        query:
          path: first_name
        expected:
          path: Joe
```

# Using Databases from JS Code

From JavaScript node code, you can work with databases, collections, and objects.

Below are code examples with the main concepts.

### Working with Collections

All methods can be called using ORM: to create a database js-object, use `db.database('database_id')` and specify the specific ID of your database (you can find it on the "Database" page in the left menu).

```jsx
export default async function run({execution_id, input, data, store, db}) {
	const database_id = '4da687c4-2ba1-476f-9ff2-c5942aab2fbd'

	const database = db.database(database_id)
}

```

To access collection and object management methods, you need to create a collection js-object:

```jsx
export default async function run({execution_id, input, data, store, db}) {
	const database_id = '4da687c4-2ba1-476f-9ff2-c5942aab2fbd'

	const database = db.database(database_id)
	const collection = database.collection('collection_name')
}

```

The `collection()` method does **not** create a new collection. If you need to create a new collection, you can call the method `await database.createCollection('collection_name')`. If such a collection already exists, an error is **not** returned.

### Working with Objects

To create an object in a collection, use the method `await collection.createObject()`. As a parameter, you can pass a string, number, boolean value, array, or js-object of any nesting. The method returns a string with the object ID:

```jsx
export default async function run({execution_id, input, data, store, db}) {
	const database_id = '4da687c4-2ba1-476f-9ff2-c5942aab2fbd'

	const database = db.database(database_id)
	const collection = database.collection('collection_name')

	const object_id = await collection.createObject({
		testField: {
		  field: "test"
		}
	})

	return {
		object_id
	}
}

```

To output a list of objects, use the method `await collection.findObjects(limit, offset, filter)`. The limit parameter sets the number of rows to read in one request, offset - the start of reading shift (standard parameters as for pagination). The filter parameter is optional and can be set as a string (YAML and JSON) or as a js-object:

```jsx
export default async function run({execution_id, input, data, store, db}) {
	const database_id = '4da687c4-2ba1-476f-9ff2-c5942aab2fbd'

	const database = db.database(database_id)
	const collection = database.collection('collection_name')

	const objects1 = await collection.findObjects(50, 0)

	const filterStr = `
	conditions:
	  - operation: "equal"
	    query:
	      path: "example"
	    expected:
	      value: "example_js"
	`

	const objects2 = await collection.findObjects(50, 0, filterStr)

	const filterObj = {
		conditions: [
			{
				operation: "equal",
				query: {
					path: "example"
				},
				expected: {
					value: "example_js"
				}
			}
		]
	}

	const objects3 = await collection.findObjects(50, 0, filterObj)

	return {
		objects1,
		objects2,
		objects3
	}
}

```

To update objects, use the method `await collection.updateObjects(filter, updater)`. The updater parameter, similar to the filter, can be either a string (YAML and JSON) or a js-object. The method returns a number - the count of updated objects:

```jsx
export default async function run({execution_id, input, data, store, db}) {
	const database_id = '4da687c4-2ba1-476f-9ff2-c5942aab2fbd'

	const database = db.database(database_id)
	const collection = database.collection('collection_name')

	const filterStr = `
conditions:
  - operation: "equal"
    query:
      path: "example"
    expected:
      value: "example_js"
	`
	const updaterStr = `
items:
  - path: "example"
     set:
       value: "example_js_2"`
	`

	const count1 = await collection.updateObjects(filterStr, updaterStr)

	const filterObj = {
		conditions: [
			{
				operation: "equal",
				query: {
					path: "example"
				},
				expected: {
					value: "example_js_2"
				}
			}
		]
	}
	const updaterObj = {
		items: [
			{
				path: "example",
				set: {
					value: "example_js_3"
				}
			}
		]
	}

	const count2 = await collection.updateObjects(filterObj, updaterObj)

	return {
		count1,
		count2
	}
}

```

## Table of All Methods Description

### Database JS-object

```yaml
- Method name:          collection(collection_name)
  Parameters:           collection_name - string
  Description:          Used to get a collection js-object, which is used for further work with objects.
  Return value:         Collection js-object
---
- Method name:          createCollection(collection_name)
  Parameters:           collection_name - string
  Description:          Creates a new collection with the given name. If the collection already exists, no error is returned.
  Return value:         Collection js-object
---
- Method name:          listCollections()
  Parameters:
  Description:          Get a list of collections for the specified database.
  Return value:         Array of objects:
                         [
                           {
                             "storage_id": "id",
                             "collection_name": "name"
                           }
                         ]

```

### Collection JS-object

```yaml
- Method name:          get()
  Parameters:
  Description:          Requests the collection from the database.
  Return value:         Example of collection:
                         {
                           "storage_id": "id",
                           "collection_name": "name"
                         }
---
- Method name:          updateCollectionName(new_collection_name)
  Parameters:           new_collection_name - string
  Description:          Updates the collection name.
  Return value:
---
- Method name:          truncate()
  Parameters:
  Description:          Deletes all objects in the collection.
  Return value:
---
- Method name:          delete()
  Parameters:
  Description:          Deletes the collection.
  Return value:
---
- Method name:          findObjects(limit, offset, filter = '')
  Parameters:           limit - int
                        offset - int
                        filter - string/object (optional parameter)
  Description:          Searches for objects with or without a filter.
  Return value:         Array of objects
---
- Method name:          getObjectByID(object_id)
  Parameters:           object_id - string
  Description:          Gets an object by its ID.
  Return value:         Object
---
- Method name:          createObject(object)
  Parameters:           object - any JS data type
  Description:          Creates an object.
  Return value:         ID of the created object
---
- Method name:          updateObjects(filter, updater)
  Parameters:           filter - string/object
                        updater - string/object
  Description:          Updates objects by filter.
  Return value:         Number of updated objects
---
- Method name:          deleteObject(object_id)
  Parameters:           object_id - string
  Description:          Deletes an object by its ID.
  Return value:         If the object existed and was deleted - 1
                        If the object was not found or already deleted - 0
---
- Method name:          deleteObjectsByFilter(filter)
  Parameters:           filter - string/object
  Description:          Deletes objects by filter.
  Return value:         Number of deleted objects

```

# AI Data Storage

RAG is currently in beta. Pricing, behavior, and limitations may change.

### Purpose

AI Data Storage (RAG) is a component of the Latenode platform designed for storing and indexing text files, images, and other knowledge sources.

  This tool is primarily intended to be used in conjunction with the AI Agent — it provides documents in the form of chunks, which the agent can then use to generate responses.

Use cases include:

* Uploading and storing structured or unstructured content
* Generating embedding vectors for fast semantic search
* Running natural language search queries
* Connecting to the **RAG Search** node inside a scenario

***

### How to Access

You can access this feature via **Data Storage → AI Data Storage (RAG)** in the left-hand side menu.

***

### Creating Storage

Click **Create Storage** to open the setup modal:

Fill in the required fields: **Storage Name, Chunk Size, Chunk Overlap**

***

### What are Chunk Size and Overlap?

* **Chunk Size** — the number of tokens in a single chunk. Smaller chunks provide higher accuracy but increase the total number of chunks.
* **Chunk Overlap** — the percentage of token overlap between neighboring chunks. Helps maintain context across them.

***

### Managing Storage

Created storages are displayed in a table:

| Field         | Description                 |
| ------------- | --------------------------- |
| Name          | Storage name                |
| Chunk Size    | Number of tokens per chunk  |
| Chunk Overlap | Overlap between chunks in % |
| Created       | Creation date               |
| Updated       | Last updated date           |

***

### Uploading Files

Open a storage to access the upload interface. Drag-and-drop is supported.

After uploading:

* Each file is processed and indexed (status: **Processing**)
* Files are listed with size, upload date, and status
* Editing or downloading files is currently **not supported**

***

### Multimodal RAG Features

For working with images and non-textual data, RAG Storage uses an advanced approach:

* **Automatic Image Description:** When uploading images (JPEG, PNG), the system automatically generates their textual description (summary) using a multimodal LLM and indexes this description along with the text content.
* **Text Indexing:** Text extracted via OCR from images (or PDF files) is also split into chunks and indexed.

This allows the AI Agent to effectively find answers to questions based on both textual and visual content.

***

### Features & Limits

| Feature             | Status                                 |
| ------------------- | -------------------------------------- |
| OCR                 | Supported (English and Russian)        |
| Image Upload        | Supported (if image contains text)     |
| File Editing        | Not supported                          |
| File Download       | Not yet available                      |
| Automatic Indexing  | Yes                                    |
| Supported Formats   | PDF, TXT, JSON, MD, PNG, JPG, and more |
| Upload via scenario | Not yet supported                      |

***

### Technical Details

| Parameter       | Value                                                       |
| --------------- | ----------------------------------------------------------- |
| Max file size   | 20 MB (50 MB planned)                                       |
| Embedding model | Cloudflare + LlamaIndex                                     |
| Vector limit    | 5 000 000 vectors per account                               |
| Billing         | 0.0066 PNP tokens per page, charged only during file upload |

***

### Billing

* [PNP tokens](/get-started/frequently_asked_questions/what-is-pnp-nodes) are deducted upon file upload
* Billing is based on pages/chunks
* Vectorization cost: **0.0066 [PNP tokens](/get-started/frequently_asked_questions/what-is-pnp-nodes) per page**
* "1 page" corresponds to approximately 1000 words or 5000 characters of text
* For unstructured data (e.g. TXT, MD), the same linear pricing model applies — cost is proportional to total text length

**Examples:**

* 10 pages (PDF/DOCX/PPTX) → 0.066 PNP tokens ($0.066)

* TXT ≈ 10 000 words (≈ 50 000 chars) → 0.066 PNP tokens ($0.066)

* MD ≈ 20 000 words (≈ 100 000 chars) → 0.132 PNP tokens ($0.132)

* 100 pages → 0.66 PNP tokens ($0.66)

* Queries via RAG Search **are not additionally billed**

# RAG Search Node

### Node: RAG Search

To use stored data inside a scenario, connect the **RAG Search** node from the **AI Agent > Actions** category.

##

### Main Fields (RAG Search Node)

| Field        | Description                                      |
| ------------ | ------------------------------------------------ |
| **Storage**  | Select the storage to search in                  |
| **Question** | Natural language query                           |
| **Top\_k**   | Number of chunks to return (default: 5, max: 20) |

***

### How It Works

1. You upload a document into a storage
2. The document is automatically split into chunks and indexed
3. RAG Search receives a query and performs embedding-based retrieval
4. The node returns raw chunks that match the query

***

### Node Execution Example

A natural language query is passed into the node, which returns a list of matching chunks based on the specified `top_k`.

***

# Using AI Agent with RAG

### Working with AI Agent

Example scenario with an **AI Agent** using RAG Search as a tool:

***

### Prompt Configuration for Agent

The agent is configured with a system prompt instructing it to use the RAG Search tool when the user asks for documentation-related information:

***

### RAG Search Tool Setup

The RAG Search node is connected to the agent using `fromAIAgent()`. A storage is selected, `top_k` is set, and the tool description helps the model understand its capabilities.

***

### End-to-End Example

1. The user sends a question to the agent

2. The agent uses RAG Search to retrieve relevant chunks



3. The agent composes and returns a final response

# How to get Support

We’re a small but passionate team doing our best to provide you with maximum value at a fair price.

There may be more of you than there are of us — and that’s exactly what inspires us. It means we’re building something that truly matters. 💛

While we strive to respond quickly, we may not always be able to reply immediately on a free support plan.

Please be patient — we’ll always get back to you as soon as we can.

To help you get answers quickly and keep moving forward, we’ve put together all available support options below:

***

## Premium Support Plans

  Get personal guidance, faster resolutions, and workflow design help tailored to your team’s needs.

  👉 [Request a Premium Support Plan](https://latenode.com/request/premium-support-plan)

***

## Free Support Options

### Option #1: Documentation and AI Assistant (self-service)

Use the built-in search in our docs — we regularly update it with solutions to common questions.

Our **AI assistant** is available 24/7 inside the platform. It can help with errors, explain features, and connect you to a live agent if needed.

***

### Option #2: Ask in the Latenode Community Forum

The [**Latenode Community Forum**](https://community.latenode.com) is our primary support channel.

You can post questions, report issues, and share feedback publicly.

We actively monitor the forum, and it’s the fastest way to get a response — both from our team and the wider community.

By asking questions there, you also help others facing similar challenges.

***

### Option #3: Discord Community

Our secondary channel for real-time conversations, quick questions, and idea-sharing.

It’s informal and great for live discussions with both our team and other users.

👉 [Join Discord](https://discord.gg/nQDyg4MJYW)

***

### Option #4: Email

Please use email **only if you’re unable to access your account or facing a critical issue**:

📧 [help@latenode.com](mailto:help@latenode.com)

***

## Request Format

If you want us to help fast — help us help you.

When reaching out, please include:

* A clear description of the problem
* What you expected to happen vs. what actually happened
* Steps to reproduce the issue, if possible

And whenever you can, attach:

* 📷 **Screenshots**
* 🎥 **Screencasts**
* 🔗 **A link to the scenario** where the issue occurred

The more context you provide, the faster (and more accurately) we can assist you.

***

## Response Time and Availability

* Our support team is available **Monday to Friday, from 10:00 to 22:00 (Central European Time)**
* On weekends, we respond when possible
* **Average response time**: a couple of hours (may be slightly longer during peak times)

🙏 Thank you for your patience — we’ll always get back to you as soon as we can!

# Latenode IP Address for Whitelisting

When adding Latenode to the allowlist of external services such as databases, webhooks, or APIs, please use the following static IP address:

**172.214.62.12**

This IP address is static and can be safely whitelisted across your infrastructure.

## Verifying the IP

To check which IP address is being used by your scenario when making outbound requests, you can call any external service that returns the requester's public IP.

**Example using HTTP Request node:**

```bash
curl https://api.ipify.org?format=json
```

If you run this inside a Latenode scenario, the response should be:

```json
{"ip":"172.214.62.12"}
```

This will confirm that your scenario's outbound requests are coming from the correct IP address.

# What Are Credits?

## Latenode Credits (Execution Credits)

**Latenode Credits** are the primary unit used for executing scenarios on the platform.

### How it works

* **1 credit** starts a scenario execution and grants up to **30 seconds** of execution time.
* Within this time frame, you can run any number of operations and nodes (apps, JavaScript, headless browser, etc.).
* Credit consumption depends **only on total execution time**, not on the number of operations.

### Minimum credit usage

* The minimum number of credits charged per execution depends on your pricing plan.
* Even if a scenario runs for only a few seconds, the minimum amount defined by your plan will be charged.
* For up-to-date minimum values, see the [pricing page](https://latenode.com/pricing-plans).

> You can view detailed usage statistics for Execution Credits on the [Statistics page](https://app.latenode.com/statistic).

***

## Boosts

**Boosts** are add-ons that expand your plan’s capabilities. Depending on the boost type, they can:

* Add more credits
* Increase limits for triggers, flows, or accounts
* Reduce the minimum scenario interval

Boosts are purchased separately and **do not expire** at the end of the month.

***

## Extra Credits

If your included credits aren’t enough, you can purchase **Extra Credits**. They are added to your balance and used **after** the monthly limit is reached.

* Extra Credits **do not expire**
* Extra Credits are used **after** the included credits are depleted

# Plug-n-Play (PnP) Tokens

## What are PnP tokens?

**PnP tokens** are an **optional** billing unit used for nodes marked with the **`$`** icon.

These nodes interact with external paid resources (third-party APIs, AI models, etc.) **without requiring you to provide your own API keys or maintain external accounts**.

Instead, you work with Latenode as an intermediary: usage is billed through a **single, unified account**, and tokens are charged accordingly.

***

## Pricing and billing

* **1 PnP token = 1 USD**. When a node is executed, the cost is calculated based on actual provider usage, and the equivalent number of tokens is deducted.
* PnP tokens are charged **in addition to** Execution Credits during a scenario run.
* **Pay-as-you-go**: you are charged for actual provider usage, not “per request”.
* Each PnP node shows pricing in its interface (typically provider rate + a small markup for processing costs).

***

## Billing modes

### Pay-per-use (default)

Applies to most PnP nodes such as AI models, file converters, enrichment nodes, and AI agents. Tokens are charged **based on usage**.

### Monthly subscription for authentication

This applies **only** to personal account connections for the following services. In this case, the **`$`** icon means the connection itself is paid and costs **10 PnP tokens per month**:

* Telegram (Personal account)
* WhatsApp (Personal account)
* LinkedIn (Personal account)

You will see a clear warning about this when creating the authorization:

***

## Viewing usage

Each PnP node shows its **detailed pricing** in a collapsible section inside the node configuration.

After scenario execution, you can view:

* The exact number of PnP tokens spent
* The actual execution cost of the node

This data is available under the **Log** tab on the right side of the node.

You can also track overall PnP token usage in **Execution History** (clock icon in the top-right corner of the interface):

> You can view detailed usage statistics for PnP Tokens on the [Statistics page](https://app.latenode.com/statistic).

# Build your first scenario

Latenode is a workflow automation platform. Automations in Latenode are called **scenarios**. A scenario is built from **nodes** (steps) connected by **routes** (connections).

In this quickstart, you’ll build a simple scenario:

* A **Gmail** trigger detects a new unread email
* An **AI** action generates a reply

## Prerequisites

* A Latenode account
* Access to a Gmail inbox (for the example trigger)

## Step 1 — Add a trigger node

  Watch: [Add a trigger node](https://youtu.be/SgRvfcmJIZk?si=-Q_6qVir5AWrIdbr).

  [  ](https://youtu.be/SgRvfcmJIZk?si=-Q_6qVir5AWrIdbr)

The trigger node starts the scenario. A scenario can be triggered by:

* An event in an external application (e.g., a message in **Telegram** or a new email in **Gmail**).
* Clicking **Run once**.
* Sending an HTTP request.

### Select a trigger node

To select the appropriate trigger node:

1. On the scenario page, click any **Add Node** button.

2. In the **Choose Application** window, go to the **Triggers** tab, search for, and select the desired node. For example, select the **New Email** trigger from the **Gmail** group.

### Authorize the app (if needed)

When you open a node for the first time, you’ll either see configuration fields or a **Create Authorization** button. If you see **Create Authorization**, this node requires authorization to work (most app nodes do).

To authorize (using **New Email** as an example):

1. Click the **Create Authorization** button.

2. Click **New Authorization**.

3. In the **Choose Service** window, select the required application. For the **New Email** node, this is the **Gmail** application.

4. Confirm Latenode access in the authorization dialogs.

5. Verify in the **New Email** node that:

* The **Connection** field shows the connection.
* The node configuration fields are available.

### Configure the trigger node

Almost every added node needs to be configured by filling in the required and optional fields.

For the **New Email** node, for example, you can fill in the **Labels** field. If you set the **Labels** field to **UNREAD**, the node will trigger the scenario when there is a new unread message.

### Test the trigger node

To test the node:

1. Save the node settings.

2. Save the scenario.

3. Right-click the trigger node and select **Run Node Once**.

4. Send an email to the account used for authorization.

5. Wait for the node to execute and check for a success message.

  The node can execute even if you don’t send a new email when there are already unread messages in the inbox. If there are no unread messages, send a new email to trigger it.

## Step 2 — Add an action node

  Watch: [Add an action node](https://youtu.be/kMCda3QFrf4?si=w5S_lmfh-NfRYrT8).

  [  ](https://youtu.be/kMCda3QFrf4?si=w5S_lmfh-NfRYrT8)

After the trigger node executes, the action node runs next. Action nodes perform work based on the trigger output.

For example: When a new unread message arrives in Gmail, a response should be generated for that email.

In this case, the action is generating a response based on the email text. You can do this with an AI node.

### Add an action node (and create a route)

To select the appropriate action node:

1. Click the right connection point of the trigger node to create a **route**.

2. In the **Choose Application** window on the **Actions** tab, search for and select the desired node. For generating a response, choose the **AI Anthropic Claude 3** node from the **AI ChatGPT Alternatives** group.

### Configure the action node

Unlike the **New Email** node, the **AI Anthropic Claude 3** node does not require authorization and can be configured immediately. To configure this node:

1. Right-click the added **AI Anthropic Claude 3** node.

2. Fill in the required fields:

* **Model**: Choose an AI model, such as Sonnet.
* **User Prompt**: Enter a prompt, for example: "Generate a reply to the email text: X."

3. Define the value of X, i.e., the email text to which you are responding. The email text is provided by the **New Email** trigger node as output data during execution.

Since the email text can vary, you need to input the parameter from the previous node rather than the actual text. To do this:

* Click the **User Prompt** field in the **AI Anthropic Claude 3** node.
* In the **Data** tab, select the **decodedContent** parameter from the **New Email** node.
* Save the node settings.

  To see output parameters in the **Data** tab, the previous nodes must have executed successfully (you’ll see a green status icon on the node). Also, nodes must be connected (directly or through other nodes) for their data to be available.

### Test the action node

To test how the added node performs the action:

1. Right-click the trigger node and select **Run Node Once**.

2. Review the execution results, including the generated text.

## Step 3 — Run and deploy your scenario

  Watch: [Run and deploy a scenario](https://youtu.be/tvog1vmTDNM?si=0ugunrBmFo3zbFRR).

  [  ](https://youtu.be/tvog1vmTDNM?si=0ugunrBmFo3zbFRR)

Save your scenario. To test it, click **Run once**. After this, when the trigger event occurs, Latenode will execute the nodes in order, and you can review results in the node details and in **Execution History**.

When everything looks good, click **Deploy** to activate the scenario. It will then run automatically when a new unread email appears in the inbox.

# Learning curve

Check back later!

# Available App Integrations

Latenode offers a wide range of available integrations.

If you didn’t find the app you need:

* [Add it to our roadmap](https://roadmap.latenode.com/apprequests) — it may be considered for development.
* [Follow our guide for a custom integration](https://latenode.com/request-new-app) and start using it right away.
* Or order paid development — our team will build the app within 10 business days.

Learn more about all available options here: [Request New App](https://latenode.com/request-new-app)

***

## 1–9

* [123FormBuilder](https://latenode.com/integrations/123formbuilder)
* [7todos](https://latenode.com/integrations/7todos)

## A

* [ABC Fitness Solutions](https://latenode.com/integrations/abc-fitness-solutions)
* [AI Agent](https://latenode.com/integrations/ai-agent)
* [AI GPT Router](https://latenode.com/integrations/ai-gpt-router)
* [AI: Automatic Speech Recognition](https://latenode.com/integrations/ai-automatic-speech-recognition)
* [AI: ChatGPT Alternatives](https://latenode.com/integrations/ai-chatgpt-alternatives)
* [AI: Image Classification](https://latenode.com/integrations/ai-image-classification)
* [AI: Image To Text](https://latenode.com/integrations/ai-image-to-text)
* [AI: Minimax](https://latenode.com/integrations/ai-minimax)
* [AI: Mistral](https://latenode.com/integrations/ai-mistral)
* [AI: Object Detection](https://latenode.com/integrations/ai-object-detection)
* [AI: Perplexity](https://latenode.com/integrations/ai-perplexity)
* [AI: Speech-To-Text](https://latenode.com/integrations/ai-speech-to-text)
* [AI: Stability](https://latenode.com/integrations/ai-stability)
* [AI: Summarization](https://latenode.com/integrations/ai-summarization)
* [AI: Text Classification](https://latenode.com/integrations/ai-text-classification)
* [AI: Text Embeddings](https://latenode.com/integrations/ai-text-embeddings)
* [AI: Text Generation](https://latenode.com/integrations/ai-text-generation)
* [AI: Text To Image](https://latenode.com/integrations/ai-text-to-image)
* [AI: Text-To-Speech](https://latenode.com/integrations/ai-text-to-speech)
* [AI: Tools](https://latenode.com/integrations/ai-tools)
* [AI: Translation](https://latenode.com/integrations/ai-translation)
* [AITable](https://latenode.com/integrations/aitable)
* [AWeber](https://latenode.com/integrations/aweber)
* [Acapela Cloud](https://latenode.com/integrations/acapela-cloud)
* [ActiveCampaign](https://latenode.com/integrations/activecampaign)
* [Acuity Scheduling](https://latenode.com/integrations/acuty-scheduling)
* [Adalo](https://latenode.com/integrations/adalo)
* [Agile CRM](https://latenode.com/integrations/agile-crm)
* [Airparser](https://latenode.com/integrations/airparser)
* [Airtable](https://latenode.com/integrations/airtable)
* [Alegra](https://latenode.com/integrations/alegra)
* [Amazon Redshift](https://latenode.com/integrations/amazon-redshift)
* [Amazon S3](https://latenode.com/integrations/amazon-s3)
* [Amazon SES](https://latenode.com/integrations/amazon-ses)
* [Amazon SNS](https://latenode.com/integrations/amazon-sns)
* [Apify](https://latenode.com/integrations/apify)
* [Apollo](https://latenode.com/integrations/apollo)
* [Asana](https://latenode.com/integrations/asana)
* [Atera](https://latenode.com/integrations/atera)
* [Attio](https://latenode.com/integrations/attio)
* [Avaza](https://latenode.com/integrations/avaza)
* [Awork](https://latenode.com/integrations/awork)

## B

* [BambooHR](https://latenode.com/integrations/bamboohr)
* [Basecamp](https://latenode.com/integrations/basecamp)
* [Baserow](https://latenode.com/integrations/baserow)
* [Basin](https://latenode.com/integrations/basin)
* [Beamer](https://latenode.com/integrations/beamer)
* [Beehiiv](https://latenode.com/integrations/beehiiv)
* [Bexio](https://latenode.com/integrations/bexio)
* [Bigin by Zoho CRM](https://latenode.com/integrations/bigin-by-zoho-crm)
* [Bitbucket](https://latenode.com/integrations/bitbucket)
* [Bitly](https://latenode.com/integrations/bitly)
* [Bitrix24](https://latenode.com/integrations/bitrix24)
* [Bland AI](https://latenode.com/integrations/bland-ai)
* [Blue](https://latenode.com/integrations/blue)
* [Booqable](https://latenode.com/integrations/booqable)
* [Bouncer](https://latenode.com/integrations/bouncer)
* [Box](https://latenode.com/integrations/box)
* [Brevo (Sendinblue)](https://latenode.com/integrations/brevo-sendinblue)
* [Brilliant Directories](https://latenode.com/integrations/brilliant-directories)
* [Browser Use](https://latenode.com/integrations/browser-use)
* [Bubble](https://latenode.com/integrations/bubble)
* [Businessmap](https://latenode.com/integrations/businessmap)

## C

* [Cal.com](https://latenode.com/integrations/cal-com)
* [Calendly](https://latenode.com/integrations/calendly)
* [Campaign Monitor](https://latenode.com/integrations/campaign-monitor)
* [Canny](https://latenode.com/integrations/canny)
* [Canva](https://latenode.com/integrations/canva)
* [Captions](https://latenode.com/integrations/captions)
* [Caspio](https://latenode.com/integrations/caspio)
* [Chargebee](https://latenode.com/integrations/chargebee)
* [Chatwork](https://latenode.com/integrations/chatwork)
* [Circle](https://latenode.com/integrations/circle)
* [Cleverreach](https://latenode.com/integrations/cleverreach)
* [ClickMeeting](https://latenode.com/integrations/clickmeeting)
* [ClickSend](https://latenode.com/integrations/clicksend)
* [ClickUp](https://latenode.com/integrations/clickup)
* [Clickup](https://latenode.com/integrations/clickup)
* [Clio](https://latenode.com/integrations/clio)
* [Clockify](https://latenode.com/integrations/clockify)
* [Close CRM](https://latenode.com/integrations/close-crm)
* [CloudConvert](https://latenode.com/integrations/cloudconvert)
* [CloudTalk](https://latenode.com/integrations/cloudtalk)
* [Cloudinary](https://latenode.com/integrations/cloudinary)
* [Cloze](https://latenode.com/integrations/cloze)
* [Coda](https://latenode.com/integrations/coda)
* [Code](https://latenode.com/integrations/code)
* [Confluence](https://latenode.com/integrations/confluence)
* [Constant Contact](https://latenode.com/integrations/constant-contact)
* [Contacts+](https://latenode.com/integrations/contacts)
* [ConvertAPI](https://latenode.com/integrations/convertapi)
* [ConvertKit](https://latenode.com/integrations/convertkit)
* [Converter](https://latenode.com/integrations/converter)
* [Creatomate](https://latenode.com/integrations/creatomate)
* [CryptoPro](https://latenode.com/integrations/cryptopro)
* [Customer.io](https://latenode.com/integrations/customer-io)

## D

* [Data Enrichment](https://latenode.com/integrations/data-enrichment)
* [Database](https://latenode.com/integrations/database)
* [Databricks](https://latenode.com/integrations/databricks)
* [Deepgram](https://latenode.com/integrations/deepgram)
* [Delighted](https://latenode.com/integrations/delighted)
* [Demio](https://latenode.com/integrations/demio)
* [Discord bot](https://latenode.com/integrations/discord-bot)
* [Discourse](https://latenode.com/integrations/discourse)
* [Docparser](https://latenode.com/integrations/docparser)
* [Docusign](https://latenode.com/integrations/docusign)
* [DonationAlerts](https://latenode.com/integrations/donationalerts)
* [Drip](https://latenode.com/integrations/drip)
* [Dropbox](https://latenode.com/integrations/dropbox)

## E

* [Email](https://latenode.com/integrations/email)
* [Encharge](https://latenode.com/integrations/encharge)
* [Enrich Layer](https://latenode.com/integrations/enrich-layer)
* [Etsy](https://latenode.com/integrations/etsy)
* [Eventbrite](https://latenode.com/integrations/eventbrite)

## F

* [Facebook Ads Campaign Management](https://latenode.com/integrations/facebook-ads-campaign-management)
* [Facebook Conversions](https://latenode.com/integrations/facebook-conversions)
* [Facebook Lead Ads](https://latenode.com/integrations/facebook-lead-ads)
* [Facebook Messenger](https://latenode.com/integrations/facebook-messenger)
* [Facebook Pages](https://latenode.com/integrations/facebook-pages)
* [Facebook](https://latenode.com/integrations/facebook)
* [Fauna](https://latenode.com/integrations/fauna)
* [Feedly](https://latenode.com/integrations/feedly)
* [Fibery](https://latenode.com/integrations/fibery)
* [Figma](https://latenode.com/integrations/figma)
* [Fillout](https://latenode.com/integrations/fillout)
* [FireText](https://latenode.com/integrations/firetext)
* [Firecrawl](https://latenode.com/integrations/firecrawl)
* [Fireflies.ai](https://latenode.com/integrations/fireflies-ai)
* [FlyMy.AI](https://latenode.com/integrations/flymy-ai)
* [Follow Up Boss](https://latenode.com/integrations/follow-up-boss)
* [Fomo](https://latenode.com/integrations/fomo)
* [Formaloo](https://latenode.com/integrations/formaloo)
* [Formsite](https://latenode.com/integrations/formsite)
* [Formstack](https://latenode.com/integrations/formstack)
* [Fotor](https://latenode.com/integrations/fotor)
* [FreeAgent](https://latenode.com/integrations/freeagent)
* [FreshBooks](https://latenode.com/integrations/freshbooks)
* [Freshdesk](https://latenode.com/integrations/freshdesk)
* [Front](https://latenode.com/integrations/front)

## G

* [Gender API](https://latenode.com/integrations/gender-api)
* [Generatebanners](https://latenode.com/integrations/generatebanners)
* [Getform](https://latenode.com/integrations/getform)
* [Getresponse](https://latenode.com/integrations/getresponse)
* [Ghost](https://latenode.com/integrations/ghost)
* [Giphy](https://latenode.com/integrations/giphy)
* [GitLab](https://latenode.com/integrations/gitlab)
* [Github](https://latenode.com/integrations/github)
* [Glide](https://latenode.com/integrations/glide)
* [Gmail](https://latenode.com/integrations/gmail)
* [GoCanvas](https://latenode.com/integrations/gocanvas)
* [GoToWebinar](https://latenode.com/integrations/gotowebinar)
* [Google AI](https://latenode.com/integrations/google-ai)
* [Google Ads](https://latenode.com/integrations/google-ads)
* [Google Analytics](https://latenode.com/integrations/google-analytics)
* [Google AppSheet](https://latenode.com/integrations/google-appsheet)
* [Google Business Profile](https://latenode.com/integrations/google-business-profile)
* [Google Calendar](https://latenode.com/integrations/google-calendar)
* [Google Chat](https://latenode.com/integrations/google-chat)
* [Google Cloud BigQuery (REST)](https://latenode.com/integrations/google-cloud-bigquery-rest)
* [Google Cloud BigQuery](https://latenode.com/integrations/google-cloud-bigquery)
* [Google Cloud Firestore](https://latenode.com/integrations/google-cloud-firestore)
* [Google Cloud Pub/Sub](https://latenode.com/integrations/google-cloud-pub-sub)
* [Google Cloud Speech-To-Text](https://latenode.com/integrations/google-cloud-speech-to-text)
* [Google Cloud Storage](https://latenode.com/integrations/google-cloud-storage)
* [Google Cloud Text-To-Speech](https://latenode.com/integrations/google-cloud-text-to-speech)
* [Google Cloud Translate](https://latenode.com/integrations/google-cloud-translate)
* [Google Dialogflow ES](https://latenode.com/integrations/google-dialogflow-es)
* [Google Drive](https://latenode.com/integrations/google-drive)
* [Google Forms](https://latenode.com/integrations/google-forms)
* [Google Groups](https://latenode.com/integrations/google-groups)
* [Google Meet](https://latenode.com/integrations/google-meet)
* [Google Programmable Search Engine](https://latenode.com/integrations/google-programmable-search-engine)
* [Google Sheets](https://latenode.com/integrations/google-sheets)
* [Google Vertex AI](https://latenode.com/integrations/google-vertex-ai)
* [Google calendar](https://latenode.com/integrations/google-calendar)
* [Google contacts](https://latenode.com/integrations/google-contacts)
* [Google docs](https://latenode.com/integrations/google-docs)
* [Google slides](https://latenode.com/integrations/google-slides)
* [Google tasks](https://latenode.com/integrations/google-tasks)
* [Gravity Forms](https://latenode.com/integrations/gravity-forms)
* [Grist](https://latenode.com/integrations/grist)
* [Gumroad](https://latenode.com/integrations/gumroad)

## H

* [Harvest](https://latenode.com/integrations/harvest)
* [Help Scout](https://latenode.com/integrations/help-scout)
* [HeyGen](https://latenode.com/integrations/heygen)
* [HighLevel](https://latenode.com/integrations/highlevel)
* [Hive](https://latenode.com/integrations/hive)
* [Http](https://latenode.com/integrations/http)
* [HubSpot](https://latenode.com/integrations/hubspot)

## I

* [Inoreader](https://latenode.com/integrations/inoreader)
* [Insightly](https://latenode.com/integrations/insightly)
* [Instagram for Business](https://latenode.com/integrations/instagram-for-business)
* [Instantly](https://latenode.com/integrations/instantly)
* [Intercom](https://latenode.com/integrations/intercom)

## J

* [Jibble](https://latenode.com/integrations/jibble)
* [Jira](https://latenode.com/integrations/jira)
* [JobNimbus](https://latenode.com/integrations/jobnimbus)
* [Jonas Fitness](https://latenode.com/integrations/jonas-fitness)
* [Jotform](https://latenode.com/integrations/jotform)
* [JustCall](https://latenode.com/integrations/justcall)

## K

* [Kintone](https://latenode.com/integrations/kintone)
* [Klaviyo](https://latenode.com/integrations/klaviyo)
* [Knack](https://latenode.com/integrations/knack)
* [Kommo](https://latenode.com/integrations/kommo)

## L

* [Landbot.io](https://latenode.com/integrations/landbot-io)
* [Lark](https://latenode.com/integrations/lark)
* [Launch27](https://latenode.com/integrations/launch27)
* [LeadMagic](https://latenode.com/integrations/leadmagic)
* [LearnDash](https://latenode.com/integrations/learndash)
* [Lemlist](https://latenode.com/integrations/lemlist)
* [Lessonspace](https://latenode.com/integrations/lessonspace)
* [Lexoffice](https://latenode.com/integrations/lexoffice)
* [Linear](https://latenode.com/integrations/linear)
* [LinkedIn Data Scraper](https://latenode.com/integrations/linkedin-data-scraper)
* [LinkedIn Personal Account](https://latenode.com/integrations/linkedin-personal-account)
* [LinkedIn](https://latenode.com/integrations/linkedin)
* [LiveChat](https://latenode.com/integrations/livechat)
* [Livestorm](https://latenode.com/integrations/livestorm)
* [LlamaCloud](https://latenode.com/integrations/llamacloud)
* [Loyverse](https://latenode.com/integrations/loyverse)

## M

* [Magento 2(OpenSource)](https://latenode.com/integrations/magento-2-opensource)
* [Magento](https://latenode.com/integrations/magento)
* [Mailchimp](https://latenode.com/integrations/mailchimp)
* [Mailerlite](https://latenode.com/integrations/mailerlite)
* [Mailgun](https://latenode.com/integrations/mailgun)
* [Mailhook](https://latenode.com/integrations/mailhook)
* [Mailjet](https://latenode.com/integrations/mailjet)
* [Mailmodo](https://latenode.com/integrations/mailmodo)
* [ManyChat](https://latenode.com/integrations/manychat)
* [Mautic](https://latenode.com/integrations/mautic)
* [Memberstack](https://latenode.com/integrations/memberstack)
* [Microsoft Excel](https://latenode.com/integrations/microsoft-excel)
* [Microsoft OneDrive](https://latenode.com/integrations/microsoft-onedrive)
* [Microsoft OneNote](https://latenode.com/integrations/microsoft-onenote)
* [Microsoft Outlook](https://latenode.com/integrations/microsoft-outlook)
* [Microsoft Power BI](https://latenode.com/integrations/microsoft-power-bi)
* [Microsoft SQL Server](https://latenode.com/integrations/microsoft-sql-server)
* [Microsoft SharePoint Online](https://latenode.com/integrations/microsoft-sharepoint-online)
* [Microsoft Teams](https://latenode.com/integrations/microsoft-teams)
* [Microsoft To Do](https://latenode.com/integrations/microsoft-to-do)
* [Miro](https://latenode.com/integrations/miro)
* [Missive](https://latenode.com/integrations/missive)
* [Mixpanel](https://latenode.com/integrations/mixpanel)
* [Moco](https://latenode.com/integrations/moco)
* [Monday](https://latenode.com/integrations/monday)
* [MongoDB](https://latenode.com/integrations/mongodb)
* [Monster API](https://latenode.com/integrations/monster-api)
* [Moosend](https://latenode.com/integrations/moosend)
* [Motion](https://latenode.com/integrations/motion)
* [Moxie](https://latenode.com/integrations/moxie)
* [MySQL](https://latenode.com/integrations/mysql)

## N

* [NetHunt](https://latenode.com/integrations/nethunt)
* [NetSuite](https://latenode.com/integrations/netsuite)
* [Netlify](https://latenode.com/integrations/netlify)
* [NeverBounce](https://latenode.com/integrations/neverbounce)
* [Nimble](https://latenode.com/integrations/nimble)
* [NoCRM](https://latenode.com/integrations/nocrm)
* [NocoDB](https://latenode.com/integrations/nocodb)
* [Nocodb](https://latenode.com/integrations/nocodb)
* [Notion](https://latenode.com/integrations/notion)

## O

* [OCR Space](https://latenode.com/integrations/ocr-space)
* [Ocean.io](https://latenode.com/integrations/ocean-io)
* [Odoo](https://latenode.com/integrations/odoo)
* [Okta](https://latenode.com/integrations/okta)
* [Omnisend](https://latenode.com/integrations/omnisend)
* [OneSignal](https://latenode.com/integrations/onesignal)
* [Ontraport](https://latenode.com/integrations/ontraport)
* [Open Weather](https://latenode.com/integrations/open-weather)
* [OpenAI ChatGPT](https://latenode.com/integrations/openai-chatgpt)
* [OpenAI DALL-E](https://latenode.com/integrations/openai-dall-e)
* [OpenAI GPT Assistants](https://latenode.com/integrations/openai-gpt-assistants)
* [OpenAI Image Generation](https://latenode.com/integrations/openai-image-generation)
* [OpenAI Responses](https://latenode.com/integrations/openai-responses)
* [OpenAI Vision](https://latenode.com/integrations/openai-vision)
* [OpenPhone](https://latenode.com/integrations/openphone)
* [Ortto](https://latenode.com/integrations/ortto)
* [Other tools](https://latenode.com/integrations/other-tools)
* [Outscraper](https://latenode.com/integrations/outscraper)

## P

* [PDF.co](https://latenode.com/integrations/pdf-co)
* [PDFMonkey](https://latenode.com/integrations/pdfmonkey)
* [PagerDuty](https://latenode.com/integrations/pagerduty)
* [PandaDoc](https://latenode.com/integrations/pandadoc)
* [Paperform](https://latenode.com/integrations/paperform)
* [Paramount Acceptance](https://latenode.com/integrations/paramount-acceptance)
* [Patreon](https://latenode.com/integrations/patreon)
* [Paypal](https://latenode.com/integrations/paypal)
* [Phantombuster](https://latenode.com/integrations/phantombuster)
* [Pinecone](https://latenode.com/integrations/pinecone)
* [Pinterest](https://latenode.com/integrations/pinterest)
* [Pipedrive](https://latenode.com/integrations/pipedrive)
* [Pipefy](https://latenode.com/integrations/pipefy)
* [Podio](https://latenode.com/integrations/podio)
* [PostgreSQL](https://latenode.com/integrations/postgresql)
* [Postmark](https://latenode.com/integrations/postmark)
* [Process Street](https://latenode.com/integrations/process-street)
* [Productboard](https://latenode.com/integrations/productboard)
* [Pushbullet](https://latenode.com/integrations/pushbullet)
* [Pushover](https://latenode.com/integrations/pushover)

## Q

* [Quentn](https://latenode.com/integrations/quentn)
* [QuestionPro](https://latenode.com/integrations/questionpro)
* [QuickBooks](https://latenode.com/integrations/quickbooks)
* [Quickbase](https://latenode.com/integrations/quickbase)
* [Qwilr](https://latenode.com/integrations/qwilr)

## R

* [RD Station](https://latenode.com/integrations/rd-station)
* [RSS](https://latenode.com/integrations/rss)
* [ReachInbox](https://latenode.com/integrations/reachinbox)
* [Realgeeks](https://latenode.com/integrations/realgeeks)
* [Recraft](https://latenode.com/integrations/recraft)
* [Recruitee](https://latenode.com/integrations/recruitee)
* [Recut](https://latenode.com/integrations/recut)
* [Reddit](https://latenode.com/integrations/reddit)
* [Render](https://latenode.com/integrations/render)
* [Replicate](https://latenode.com/integrations/replicate)
* [RingCentral](https://latenode.com/integrations/ringcentral)
* [RocketReach](https://latenode.com/integrations/rocketreach)
* [Rss.app](https://latenode.com/integrations/rss-app)

## S

* [SOS Inventory](https://latenode.com/integrations/sos-inventory)
* [Salesforce](https://latenode.com/integrations/salesforce)
* [Salesmate](https://latenode.com/integrations/salesmate)
* [Scoro](https://latenode.com/integrations/scoro)
* [Scrapeless](https://latenode.com/integrations/scrapeless)
* [SendFox](https://latenode.com/integrations/sendfox)
* [SendPulse](https://latenode.com/integrations/sendpulse)
* [Sendgrid](https://latenode.com/integrations/sendgrid)
* [Sendinblue](https://latenode.com/integrations/sendinblue)
* [Sendy](https://latenode.com/integrations/sendy)
* [Serper](https://latenode.com/integrations/serper)
* [ServiceM8](https://latenode.com/integrations/servicem8)
* [Shippo](https://latenode.com/integrations/shippo)
* [Shopify](https://latenode.com/integrations/shopify)
* [Signnow](https://latenode.com/integrations/signnow)
* [Simplesat](https://latenode.com/integrations/simplesat)
* [Simplybook](https://latenode.com/integrations/simplybook)
* [Sinch](https://latenode.com/integrations/sinch)
* [Slack bot](https://latenode.com/integrations/slack-bot)
* [Slack](https://latenode.com/integrations/slack)
* [SmartSuite](https://latenode.com/integrations/smartsuite)
* [Smartsheet](https://latenode.com/integrations/smartsheet)
* [Smsapi](https://latenode.com/integrations/smsapi)
* [Soax](https://latenode.com/integrations/soax)
* [Softr](https://latenode.com/integrations/softr)
* [SpaceX](https://latenode.com/integrations/spacex)
* [Spotify](https://latenode.com/integrations/spotify)
* [Square](https://latenode.com/integrations/square)
* [Squarespace](https://latenode.com/integrations/squarespace)
* [Sticker](https://latenode.com/integrations/sticker)
* [Straker Verify](https://latenode.com/integrations/straker-verify)
* [Strava](https://latenode.com/integrations/strava)
* [Streak](https://latenode.com/integrations/streak)
* [Streamtime](https://latenode.com/integrations/streamtime)
* [Stripe](https://latenode.com/integrations/stripe)
* [Supabase](https://latenode.com/integrations/supabase)
* [Systeme IO](https://latenode.com/integrations/systeme-io)

## T

* [Tamtam](https://latenode.com/integrations/tamtam)
* [Tavily](https://latenode.com/integrations/tavily)
* [Teachable](https://latenode.com/integrations/teachable)
* [Teamleader](https://latenode.com/integrations/teamleader)
* [Teamwork](https://latenode.com/integrations/teamwork)
* [Telegram Personal Account](https://latenode.com/integrations/telegram-personal-account)
* [Telegram bot api](https://latenode.com/integrations/telegram-bot-api)
* [Telegram](https://latenode.com/integrations/telegram)
* [Textmagic](https://latenode.com/integrations/textmagic)
* [Thankster](https://latenode.com/integrations/thankster)
* [Thinkific](https://latenode.com/integrations/thinkific)
* [TickTick](https://latenode.com/integrations/ticktick)
* [Ticket Tailor](https://latenode.com/integrations/ticket-tailor)
* [TidyCal](https://latenode.com/integrations/tidycal)
* [TimeCamp](https://latenode.com/integrations/timecamp)
* [TimePaste.com](https://latenode.com/integrations/timepaste-com)
* [Todoist](https://latenode.com/integrations/todoist)
* [Toggl Track](https://latenode.com/integrations/toggl-track)
* [Tools](https://latenode.com/integrations/tools)
* [Trainerize](https://latenode.com/integrations/trainerize)
* [Trint](https://latenode.com/integrations/trint)
* [Try it on](https://latenode.com/integrations/try-it-on)
* [Tumblr](https://latenode.com/integrations/tumblr)
* [Twilio](https://latenode.com/integrations/twilio)
* [Twist](https://latenode.com/integrations/twist)
* [Twitch](https://latenode.com/integrations/twitch)
* [Typebot](https://latenode.com/integrations/typebot)
* [Typeform](https://latenode.com/integrations/typeform)

## U

* [Unbounce](https://latenode.com/integrations/unbounce)
* [Userback](https://latenode.com/integrations/userback)

## V

* [Vapi](https://latenode.com/integrations/vapi)
* [VideoAsk](https://latenode.com/integrations/videoask)
* [Vimeo](https://latenode.com/integrations/vimeo)
* [Vitally](https://latenode.com/integrations/vitally)
* [Volunteero](https://latenode.com/integrations/volunteero)

## W

* [Wachete](https://latenode.com/integrations/wachete)
* [Wave](https://latenode.com/integrations/wave)
* [Wealthbox](https://latenode.com/integrations/wealthbox)
* [Webflow (Legacy)](https://latenode.com/integrations/webflow-legacy)
* [Webflow](https://latenode.com/integrations/webflow)
* [Webhook](https://latenode.com/integrations/webhook)
* [WhatConverts](https://latenode.com/integrations/whatconverts)
* [WhatsApp Business Cloud](https://latenode.com/integrations/whatsapp-business-cloud)
* [WhatsApp Personal Account](https://latenode.com/integrations/whatsapp-personal-account)
* [WildApricot](https://latenode.com/integrations/wildapricot)
* [Wix](https://latenode.com/integrations/wix)
* [WooCommerce](https://latenode.com/integrations/woocommerce)
* [Woodpecker](https://latenode.com/integrations/woodpecker)
* [WordPress.com](https://latenode.com/integrations/wordpress-com)
* [Wrike](https://latenode.com/integrations/wrike)
* [Wufoo](https://latenode.com/integrations/wufoo)

## X

* [X (Twitter)](https://latenode.com/integrations/x-twitter)
* [Xero](https://latenode.com/integrations/xero)

## Y

* [YouCanBookMe](https://latenode.com/integrations/youcanbookme)
* [YouTube](https://latenode.com/integrations/youtube)
* [Youform](https://latenode.com/integrations/youform)

## Z

* [Zapier](https://latenode.com/integrations/zapier)
* [Zendesk Sell](https://latenode.com/integrations/zendesk-sell)
* [Zendesk](https://latenode.com/integrations/zendesk)
* [ZeroBounce](https://latenode.com/integrations/zerobounce)
* [Zoho Books](https://latenode.com/integrations/zoho-books)
* [Zoho CRM](https://latenode.com/integrations/zoho-crm)
* [Zoho Campaigns](https://latenode.com/integrations/zoho-campaigns)
* [Zoho Cliq](https://latenode.com/integrations/zoho-cliq)
* [Zoho Creator](https://latenode.com/integrations/zoho-creator)
* [Zoho Desk](https://latenode.com/integrations/zoho-desk)
* [Zoho Inventory](https://latenode.com/integrations/zoho-inventory)
* [Zoho Invoice](https://latenode.com/integrations/zoho-invoice)
* [Zoho Mail](https://latenode.com/integrations/zoho-mail)
* [Zoho Zeptomail](https://latenode.com/integrations/zoho-zeptomail)
* [Zoom](https://latenode.com/integrations/zoom)

# Setting up App Nodes

Let's consider the node configuration fields using the example of the **Delete File** node in the **Google Drive** group.

When configuring nodes, it is often necessary to select folders or files. When you click on the configuration field:

## File and Folder Display

File and folder names are displayed, taking their identifiers into account:

* If a file is located within a folder, the name is displayed in the format **Folder Name > File Name** (1)
* If the file is located outside of a folder, the name is displayed without additional comments (2)
* The folder name is also displayed without additional comments

## Loading More Items

The first 100 items of the dropdown list are displayed (2). By clicking the **Load More** button (1), the next 100 items in the list are loaded for selection. The **Load More** button disappears when the entire list of values has been loaded.

## Search Functionality

Text input for searching values is available:

* When entering a search value (1), the number of found values out of the total number of loaded values is displayed (2), and unsuitable values disappear.

* The search is conducted within the loaded values, for example, within 100 values (2) out of the existing 107. By clicking the **Continue Search** button (1), a search is performed for the next hundred values. The **Continue Search** button disappears when the search has been conducted across the entire list of values.

# Adding and configuring authorizations

## New authorization

To add a new  authorizations, you need to click on the **New authorization** button on the page with the list of authorizations.

After clicking the add authorization button, you should choose the desired service from the provided list in the **Choose a service** window\*\*.\*\*

  It is possible to add authorization after creating a node by clicking the **New authorization** button **(1)**. When adding authorization from the node, there is **no need to select a service**, it is determined automatically **(2)**.

## Authorization Setup

To configure a authorization, for example, to Google Sheets, you need to:

1. Select the appropriate service in the **Choose a Service** window\*\*:\*\*

2. Choose the required authorization and click on the **Sign in with Google** button:

3. Authenticate using your Google account;

4. Confirm that you have the necessary rights for Latenode and click on the **Continue** button:

## Using the authorization

To utilize the added authorization when configuring script nodes, follow these steps:

1. Choose and add a specialized node that corresponds to the configured authorization. For example,�**Add Quick Event:**

2. Click the **Create an authorization** button **(1)** and choose the corresponding authorization from the list **(2).**

  Only authorizations that correspond to the node are displayed in the list. For example, only **Google Calendar** authorizations will be displayed for **Google Calendar** group nodes.

1. Review the value in the **Connection** field and fill in the other node configuration fields;

4. To modify authorization, click on the edit icon **(1)** and select a new authorization **(2)**. The current authorization is marked in blue **(3)**.

## All Authorizations

Existing authorizations are available for viewing on the **Authorizations** page\*\*.\*\*

You can view the main attributes of a authorization in the respective columns of the **Authorizations** table\*\*:\*\*

* (**1**) Authorization name - in the **Name** column. It can be edited if needed by clicking on it;

* (**2**) Service authorization - in the **Service** column. For example, Google Sheets;

* (**3**) Authorization creation Date - in the **Created Date** column. Using the gear icon, you can reconfigure the column to display the date of modification instead of the creation date;



* Menu (**4**) available for each row and allowing you to:

**Reauthorize** if necessary;

**Delete** the authorization.

  After clicking the **Delete** button and confirming the action in the modal window, the authorization will be permanently deleted.

For ease of viewing and managing authorizations, a text filter is available for entering the desired authorization name.

# GetGlobalVariables

## Node Description

**GetGlobalVariables** — an action-type node, necessary for obtaining and further using a global variable set in the **SetGlobalVariables** node.

For more information about global variables, see [Global Variables](../../visual-builder/variables/creating-and-editing-variables.mdx).

## Node Configuration

To configure the **GetGlobalVariables** node, it is necessary to fill in the **Variables (1)** field with the corresponding parameter name from the previous **SetGlobalVariables (2)** node or from the list of already created global variables (displayed on the Variables tab **(3)**).

  If the global variable is being created for the first time in the scenario, a specific sequence of scenario nodes should be observed when using nodes for variable input and retrieval. The **SetGlobalVariables** node must be executed before the **GetGlobalVariables** node.

# GetVariables

## **Node Description**

**GetVariables** - an action-type node used to retrieve and subsequently utilize a variable specified in the **SetVariables** node.

## **Node Configuration**

To configure the **GetVariables** node, you need to fill in the **Variables (1)** field with the corresponding name of the parameter from the previous **SetVariables (2)** node.

  When using nodes for variable input and retrieval, it's important to follow a specific sequence of script nodes. The **SetVariables** node should be executed before the **GetVariables** node.

# HTTP Request

## **Node Description**

**HTTP Request** � an action-type node used to send requests to an external application's API.

This node supports sending requests over both HTTP and HTTPS protocols.

## **Node Configuration**

To configure the **HTTP Request** node, you need to fill in both required and optional fields.

The required **fields** are:

* **URL;**
* **Method.**

### **URL**

The **URL** field is where you input the URL of the external application's API that you want to send a request to.

  Variables and parameters from other nodes can be inserted into the URL using the "?" symbol

### **Method**

The field is used to enter the name of the method used in the request (GET/POST/PUT/PATCH/DELETE).

### **Proxy**

The configuration block with fields includes:

* **Enter proxy address**: A field for entering the address of the proxy through which the request should be routed.
* **Enter login**: A field for entering credentials for using the proxy.
* **Enter password**: A field for entering credentials for using the proxy.

These fields are filled in when access to the external application's API is restricted to the local network.

### **Body**

The block of fields for configuring and filling in the request body includes:

Before filling in the field, you need to select the format in which the request body will be transmitted (you can see a more detailed description [here](https://developer.mozilla.org/ru/docs/Web/HTTP/Methods/POST)):

* **raw**;
* **form-data;**
* **x-www-form-urlencoded.**

When selecting the **form-data** and **x-www-form-urlencoded** options, you have access to:

* The **Add a param** button (**1**) for adding a new Key-Value pair;
* The **Delete** button (**2**) for removing a Key-Value pair.

### **Headers**

The block of fields for filling in request headers:

* **Key** � a field for entering additional information about the request. For example, the format � **content-type;**
* **Value** � a field for entering the value of additional information about the request. For example, the value of the format � **application/json.**

To add a new Key-Value pair, use the **Add a header** button (**1**). To delete a Key-Value pair, use the **Delete** button (**2**).

  When authorizing via a Bearer token, one of the request headers should be the pair with the Key `Authorization` and the Value \`Bearer `<token>`.

### **Authorization**

A block of fields for selecting an authentication method and entering authentication credentials.\
The following authentication methods are available for selection:

* **Without authentication** � for sending requests that do not require authentication or require authentication via a Bearer token;
* **Basic auth** � for sending requests that require basic authentication;
* **Digest auth** � for sending requests that require digest authentication;
* **NTLM auth** � for sending requests that require NTLM authentication.

When choosing the authentication methods **Basic auth/Digest auth**, you need to enter credentials, which include a username and password.\
In the case of selecting the **NTLM auth** method, you must input a username, password, and domain.

### **Hiding data in history**

A toggle switch for data hiding.

Additional logic for data concealment can be configured in the field that appears when clicking the **Advanced Settings** button.

## **Quick node configuration**

Applications that provide APIs may specify HTTP request examples in CURL format. For example:

```
curl -X GET https://api.test.com/v1/email/balance \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Bearer $API_TOKEN'
```

To quickly configure an **HTTP Request** node, follow these steps:

1. Click on **Create from Example (CURL)**.

2. Copy the example request and paste it into the modal window. Then, click the **Create** button:

3. Review the filled fields for the **HTTP Request** node.

# Iterator

The **Iterator** processes data one element at a time: you pass it an array or object, and it feeds each item into the chain in order. Use it to loop over lists, object properties, or query results.

You can pass a **JSON array** (iteration over elements) or a **JSON object** (iteration over key–value pairs).

  Training video: [here](https://www.youtube.com/watch?v=q5lNoPncj5g). General topic: [Iterating](/visual-builder/data-flow/iterating).

## Configuration

### Data to iterate field

In the single **Data to iterate** field, specify the array or object to loop over. You can reference data from a previous node (e.g. `{{node.field}}`) or enter a fixed value.

### Connectors

* **Top connector** — connect nodes that should run **for each** element (the loop). They run as many times as there are items in the data.
* **Right connector** — runs **once after** all iterations finish. Useful for e.g. sending a webhook response or a final step.

  A node connected to the **right** connector runs only once. Nodes on the **top** connector run on every iteration.

## Example

Typical flow: trigger or data node → **Iterator** (in Data to iterate, use an array like `["aaa", "bbb", "ccc"]` or a reference to a previous node’s output). Connect a node that processes one item (JavaScript, HTTP Request, Set Variables, etc.) to the **top** connector. Optionally connect a node that runs after the loop (e.g. Webhook Response) to the **right** connector.

# JSON Parse

## **Node Description**

**JSON Parse** - an action-type node used for converting the provided string into JSON format.

## **Node Configuration**

To configure the JSON Parse node, it is necessary to fill in the mandatory field **JSON string**.

### **JSON string**

This field is required for entering the string that needs to be converted into JSON format.

  In the **JSON string** field, you can input text, variables from other nodes, or parameters from responses of other nodes.

## **Example of Node Usage**

To obtain a string converted to JSON format, you need to create a scenario with nodes:

1. **Trigger on Webhook** node is used to trigger the scenario and pass the string `{"Fruit": "Apple", "Sum": 10}` into it;

2. **JSON string** node is used to perform the conversion of the string;

3. **Webhook response** node is used to receive the result of the string conversion.

The result of executing this scenario is a JSON object.

### JSON

```jsx
{
	"Fruit": "Apple",
	"Sum": 10
}
```

# SetGlobalVariables

## Node Description

**SetGlobalVariables** — an action-type node necessary for introducing a new global variable into the scenario. The added variable can subsequently be used in any account scenario.

  The added global variable can be modified during the execution of nodes. If two **SetGlobalVariables** nodes are placed consecutively and both define the value of the same variable, the final value for the variable will be set by the last **SetGlobalVariables** node.

For more information about global variables, see [Global Variables](../../visual-builder/variables/creating-and-editing-variables.mdx).

## Node Configuration

To configure the **SetGlobalVariables** node, it is necessary to fill in key-value pairs.

* **(1) Key** - a field for entering the name of the global variable;
* **(2) Value** - a field for entering the value of the global variable.

After creation using the **SetGlobalVariables** node, the global variable will be displayed in the table of all existing global variables.

If the **SetGlobalVariables** node is connected to a node through the top Iterator connection point and is executed multiple times sequentially, the node's output data is displayed with an indication of **Iterations**. Each iteration corresponds to its output data.

# SetVariables

## **Node Description**

**SetVariables** - an action-type node used to introduce a new variable into the script. The added variable can be subsequently used within the script.

  The added variable is unique within the script and can be changed during the execution of script nodes. If two **SetVariables** nodes are placed in sequence and both define the value of the same variable, the final value for the variable will be set by the last **SetVariables** node.

## **Node Configuration**

To configure the **SetVariables** node, you need to fill in pairs of Key-Value fields.

* **(1) Key** - the field for entering the variable name;
* **(2) Value** - the field for entering the variable's value.

If a **SetVariables** node is connected to an **Iterator** node and is executed multiple times sequentially, the node's output is displayed with an indication of **Iterations**. Each iteration corresponds to its own output data.

# Trigger on Mailhook

## Node Description

Mailhook is a trigger node that launches a scenario when an email is received at a unique, automatically generated email address. It's used to automate processes based on incoming emails - such as handling notifications, client messages, or system alerts.

***

## Node Configuration

Once the Mailhook node is added, two email addresses are automatically generated:

* **Production Email** — used in a published scenario. The scenario is triggered every time an email is received. It remains active as long as the scenario is running.
* **Development Email** — used for testing. The scenario is triggered once upon receiving an email, and then it automatically stops.

Both email addresses are shown in the `Path` field of the node and can be copied for use.

***

## Usage

To trigger the scenario, simply send an email to one of the Mailhook addresses.

Examples:

* Manually sending an email from a client like Gmail or Outlook;
* Receiving automated email notifications from third-party services;
* Using Mailhook as an entry point for client communications.

***

## Input

Mailhook does not accept data from upstream nodes. It triggers the scenario based solely on incoming emails.

***

## Output

The Mailhook node returns a structured JSON object containing the full details of the received email, including metadata, headers, message content, and attachments.

### Example output:

````````````````````````json
{
  "headers": [
    {
      "key": "subject",
      "value": "Example Subject"
    },
    {
      "key": "from",
      "value": "Sender Name ```````````````````````<sender@example.com>```````````````````````"
    }
    // ...
  ],
  "from": {
    "address": "sender@example.com",
    "name": "Sender Name"
  },
  "to": [
    {
      "address": "your-mailhook-id@mailhook-latenode.com",
      "name": ""
    }
  ],
  "subject": "Example Subject",
  "messageId": "```````````````````````<unique-message-id@example.com>```````````````````````",
  "date": "2025-05-19T09:26:58.000Z",
  "html": "```",
  "text": "Hello",
  "attachments": [
    {
      "filename": "document.pdf",
      "mimeType": "application/pdf",
      "disposition": "attachment",
      "related": true,
      "contentId": "```````````````````````<unique-content-id>```````````````````````",
      "content": {}
    }
  ]
}
````````````````````````

### Fields explained:

* `headers` — array of all original email headers (`key`/`value` pairs).
* `from` — sender’s name and email address.
* `to` — list of recipients (usually just your Mailhook address).
* `subject` — email subject line.
* `messageId` — unique identifier of the email.
* `date` — date and time the email was sent (ISO format).
* `html` — HTML version of the email body.
* `text` — plain text version of the email body.
* `attachments` — array of file objects attached to the email.

### Attachment object fields:

* `filename` — name of the attached file.
* `mimeType` — MIME type of the file.
* `disposition` — usually `"attachment"`, may also be `"inline"`.
* `related` — `true` if it's part of the email content (e.g., embedded image).
* `contentId` — identifier for inline referencing (e.g. `<image1@cid>`).
* `content` — file content

***

## Testing and Debugging

For debugging, use the Development Email address. The scenario will run once and stop, making it safe to test logic and inspect the structure of the output data.

***

# Trigger on Run once

## Node Description

**Trigger on Run once** is a trigger-type node that allows manually starting a scenario by clicking the **Run once** button. Unlike other triggers, it does not require external requests or specific events to activate. The node allows passing input parameters (text or files) into the scenario.

## **Example of Node Usage**

### **Example 1: Processing Text with JavaScript**

In this example, the user inputs text, the scenario processes it using JavaScript, and the result is stored as a variable.

### **Scenario Structure**

1. **Trigger on Run once** – Starts the scenario manually and receives text input.
2. **JavaScript** – Processes the text (e.g., converts to uppercase or counts words).

### **Scenario Setup**

#### **1. Configuring the Trigger on Run Once Node**

* Click on the **Trigger on Run once** node.
* In the **Params** section, add a text parameter.
* Specify a name for the variable (e.g., `input_text`).
* Enter a sample text value for testing.

* Click **Save** and **Run once** to pass the data into the scenario.

#### **2. Processing Data with JavaScript**

Add a **JavaScript** node and insert the following code, then press **Generate params**:

```jsx
/** @CustomParams
{
  "text": {
    "key": "text",
    "title": "Text",
    "description": "Text to convert to uppercase",
    "type": "string"
  }
}
*/
export default async function run({ data }) {
  const { text } = data;

  // Validate the input text
  if (!text) {
    throw new Error('The text parameter is required.');
  }

  const upperCaseText = text.toUpperCase();

  return { upperCaseText };
}
```

* Pass the input variable containing text.

* Run the scenario.
* The output will be the formatted text.

***

### **Example 2: Recognizing Image Content Using AI**

In this example, an image is uploaded and sent to an AI service for content recognition.

### **Scenario Structure**

1. **Trigger on Run once** – Starts the scenario manually and allows image upload.
2. **AI Image Processing** – Sends the image to an AI service for recognition.

### **Scenario Setup**

#### **1. Configuring the Trigger on Run Once Node**

* Click on the **Trigger on Run once** node.
* In the **Params** section, add a **File** parameter.
* Specify a name for the variable (e.g., `input_image`).

* Upload a sample image for testing.

* Click **Save** and **Run once** to pass the data into the scenario.

#### **2. Sending the Image to AI for Analysis**

* Add an AI-based image recognition node (e.g., GPT or another service).

* Pass the **file content**, **filename**, and **prompt for analysis** into the corresponding fields.

* Run the scenario to receive the recognized result.

***

### **Node Behavior on Execution**

* The **first** execution stores the processed values.
* Subsequent executions overwrite previous values.
* Uploaded files are processed and passed into the scenario with metadata.

These examples demonstrate how the **Trigger on Run once** node can be used to process text and file data within automated workflows while saving results for later use.

# Trigger on Schedule

## **Node Description**

**Trigger on Schedule** - a trigger-type node, used to initiate a script based on a schedule.

## **Node Configuration**

To configure the **Trigger on Schedule** node, you need to fill in the mandatory fields.

### Schedule

This field is necessary for setting up a schedule. Using dropdown menus, configure the frequency for:

* Year;
* Month;
* Day of the month;
* Day of the week;
* Hours;
* Minutes.

You don't need to fill in all the listed time parameters; it's sufficient to fill in only those parameters that will provide the desired schedule.

  The CRON expression field is automatically populated in accordance with the configured parameters.

  The scenario will operate based on the corresponding CRON expression if the scenario itself is **active** and deployed in the **Production** branch.

  To disable the scenario from running on a schedule, you can either set it to an inactive state (**Paused** status) using the **Activity** toggle or remove the **Trigger on Schedule** node from the scenario.

### Timezone

This is the field for selecting the timezone in which you want to configure the schedule.

# Trigger on Webhook

## **Node Description**

**Trigger on Webhook** is a trigger node type that serves as the entry point into the scenario. Requests are sent to the URL of the **Trigger on Webhook** node, initiating the execution of the scenario.

## **Node Configuration**

After adding the **Trigger on Webhook** node, two versions of its URL are automatically generated. Both URL versions are displayed in the **Path** field:

* The **Production-version** is accessible by clicking the **Production URL**. Sending requests to this URL version can be continuous, and the scenario execution will not stop until the scenario is manually halted or a critical error occurs.;
* The **Development-version** is accessible by clicking the **Development URL**. Sending a request to this URL version runs the scenario once, after which the scenario stops its operation. This is useful for testing and debugging the scenario temporarily without prolonged execution.

The generated URL can be either partially modified (**1**) or copied (**2**), for later inclusion in the request sent to trigger the scenario.

  You can send requests to the **Trigger on Webhook** node's address using the **POST** method (if data needs to be transmitted to the node) or the **GET** method (if a simple node triggering is required).

*building js code is failed: Node build fatal error*

# Wait

## Node Description

**Wait** - an action-type node necessary for introducing a pause during scenario execution using:

* setting a delay time, for example, 30 minutes;
* setting a specific time until which the wait is required, for example, 2024-01-01T00:00:00Z.

  The **Wait** node can be placed between scenario nodes. This allows for a temporal gap in the execution of scenario nodes before the **Wait** node and those after the **Wait** node.

## Node Configuration

To configure the Wait node, it is necessary to fill in the required or optional fields in one of the two tabs: **Wait until** or **Delay.**

### **Wait until**

The **Wait until** tab is necessary for setting the time until which one must wait before executing the scenario nodes that follow the **Wait** node. Configuration is done using the fields:

* **Date and Time** - a field for selecting the date and time in the [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format when the scenario nodes following the **Wait** node should be executed.
* **Timezone** (mandatory field) - a field for selecting the timezone according to which the pause should be set.

### **Delay**

The **Delay** tab is necessary for setting the waiting period after which the scenario nodes following the **Wait** node should be executed. Configuration is done using the fields:

* **Days** - a field for selecting the number of days in the waiting period;
* **Hours** - a field for selecting the number of hours in the waiting period;
* **Minutes** - a field for selecting the number of minutes in the waiting period;
* **Seconds** - a field for selecting the number of seconds in the waiting period.

When calculating the waiting time, the values entered in the fields are summed up. For example, the waiting time will be 1 day, 4 hours, 32 minutes, and 59 seconds if the field values are:

* **Days** - 1;
* **Hours** - 4;
* **Minutes** - 32;
* **Seconds** - 59.

# Webhook Response

## **Node Description**

**Webhook Response** is an action node that generates a response to a request sent to the **Trigger on Webhook** node.

## **Node Configuration**

To configure the **Webhook Response** node, you need to fill in both required and optional fields.

The only required\*\*\*\*\* field is:

* **Status**.

### Status

This field is used to input the response code to the request from the previous node. For example, a response code like 200.

### Body

The response field generated by the **Webhook Response** node when it receives a response code from the **Status** field of the previous node.

  In the **Body** field, you can input text, variables from other nodes, or response parameters from other nodes.

### Other Params

A section of fields for filling in response headers:

* **Key** - a field to enter additional information about the response, such as the format, e.g., **content-type;**
* **Value** - a field to enter the value of additional information about the response, such as the format value, e.g., **application/json.**

To add a new Key-Value pair, you can use the **Add a header** button (**1**). To remove a Key-Value pair, you can use the **Remove** button (**2**).

# Creating a dynamic form for a scenario of the Nodul type

To meet business needs, it may be necessary to dynamically display fields in a scenario node of the **Nodul** type.

Let's create a custom node with dynamic field rendering. To do this, you need to create auxiliary scenarios with nodes such as **NodulInput**, **NodulOutput**, **Nodul Form Input**, **Nodul Form Output**, and then verify the operation of the created node.

## **Creating Auxiliary Scenarios**

1. Create a scenario of type **Nodul**:

* Add a **NodulInput** node with configured parameters:

**URL** - a mandatory parameter of type String;

**Method** - a mandatory parameter of type Select with the option for a single choice and a list of values to choose from: GET, POST, PUT, DELETE. You can choose GET as the default value;

**Body type** - an optional parameter of type Select with the option for a single choice and a list of values to choose from: Raw, form-data, x-www-form-urlencoded. Fill in the **Fetch events** characteristic with the value **Change** to trigger the update of the entire node form when selecting a parameter value.

* Add a node to perform the scenario function, for example, an�**Java Script**�node to send requests to an external application.
* Add a�**NodulOutput**�node to receive the response from the Nodul type scenario.

2. Save and activate the scenario of type **Nodul**;

3. On the same page, create a scenario using the **Nodul Form Input** and **Nodul Form Output** nodes. This scenario will ensure dynamic display of a **Nodul** type scenario form based on the selected parameters:

* Add a�**Nodul Form Input**�node to retrieve parameters from the **Nodul** type scenario form;
* Add a�**JavaScript**�node with the following code:

```jsx
export default async function run({execution_id, input, data}) {
    const current_form_values = data["{{3.`current_form_values`}}"];
    console.log(current_form_values);
    const formValuesRaw = JSON.parse(current_form_values);
    const formValues = formValuesRaw.reduce((acc, item) => {
        acc[item.key] = item.type === 'select' ? {
            ...item,
            value: {
                select: item.value.select[0],
            }
        } : item;
        return acc;
    }, {});
    const changedKeys = JSON.parse(data["{{3.event.`param_keys`}}"]).reduce((acc, item) => {
        acc[item] = true;
        return acc;
    }, {});

    return {
        formValues,
        changedKeys,
    }
}
```

* Create a connection with the condition `{{4.changedKeys.bodytype = true and 4.formValues.bodytype.value.select = "raw"}}` to trigger the corresponding branch of the scenario when the "Raw" value is selected in the�**Body type**�parameter;
* Add another�**JavaScript**�node with the following code:

```jsx
export default async function run({execution_id, input, data}) {
    return {
        data: {
            params: {
                set: [{
                    key: 'body',
                    type: 'text',
                    title: 'Row',
                    required: true,

                }]
            }
        }
    }
}
```

* Add a�**Nodul Form Output**�node to display form parameters after selecting "Raw" in the�**Body type**�parameter\*\*;\*\*
* Create a connection with the condition `{{4.changedKeys.bodytype = true and (4.formValues.bodytype.value.select = "form-data" or 4.formValues.bodytype.value.select = "x-www-form-urlencoded")}}` to trigger the corresponding branch of the scenario when "form-data" or "x-www-form-urlencoded" values are selected in the�**Body type**�parameter;
* Add another�**JavaScript**�node with the following code:

```
export default async function run({execution_id, input, data}) {
    return {
        data: {
            params: {
                set: [{
                    key: 'body',
                    type: 'string_to_string',
                    title: data["{{4.`formValues`.bodytype.value.select}}"],
                }]
            }
        }
    }
}
```

* Add a�**Nodul Form Output**�node to display form parameters after selecting "Raw" in the�**Body type**�parameter\*\*.\*\*

## **The result of auxiliary scenarios**

To check the result of the created scenarios, you need to:

1. Create a new scenario;

2. Add the created node using the **Add Node** button. The node will be placed in the node group according to the scenario name, under the **Nodul** type.

For example, if the scenario name is **Al Tools/Action/Nodul3** then the node will be placed in the **Al Tools** group, under the **Action** subgroup, and named **Nodul3**.

3. The added node will display fields corresponding to the parameters of the **NodulInput** node\*\*:\*\*

* When selecting the "Raw" parameter in the **Body type** field, the node's form will be updated, and a mandatory **Row** field will be added to the existing fields\*\*;\*\*

* When selecting the "form-data" or "x-www-form-urlencoded" parameter in the **Body type** field, the node's form will be updated, and pairs of Key-Value fields will be added to the existing fields.

4. Each time the node is updated, an auxiliary scenario is triggered. The history and results of the execution are displayed in the **History** section on the scenario page.

# How to create your own nodes

**Scenario** type �**Nodul�** is often used for quickly integrating into another scenario that involves preconfigured and repetitive actions.

Often a scenario of type **Nodul** is used to quickly embed an already customized and repetitive action into another, main scenario. The generated scenario of type Nodul is selectable in the list of all nodes and visually represents a customized node.

When executing **Production-branch** of the scenario that uses a scenario of type Nodul, the status of the scenario of type Nodul is important:

* If the status of the Nodul type scenario is **Pause** and the **Trigger on Webhook** node is the trigger for the main scenario, an error will occur during scenario execution indicating that the Nodul type scenario needs to be activated.

* If the status of the scenario is of the Nodul **Pause** type and the **Trigger on RunOnce** node is the trigger for the main scenario, no error will occur and the scenario will be executed.
* If the status of the scenario is of type Nodul **Active**, then no error will occur at any trigger of the main scenario and the scenario will be executed.

If the **Development-branch** of the scenario is running, no error will occur and the scenario will be executed.

Let's consider the algorithm for creating a **Nodul** scenario with an example.

We will create a scenario that records a string in a Google Sheet. Recording a string of text in a Google Sheet will be considered the repetitive action. Retrieving data from a source and transforming it, if necessary, will be considered the specific action.

To achieve this, you need to:

1. Create a�**Scenario**�of type�**Scenario**�with the preliminary name "String to Table," the result of which is a frequently repeated action, i.e., entering information into a Google Sheet:

* Add a **Trigger on Webhook** node to trigger the scenario;
* Add an **Add Single Row** node to write a row to the Google Sheet according to your settings\*\*;\*\*

* Add a **Webhook Response** node to return a response upon scenario execution\*\*;\*\*

* **Save** and activate the scenario;

2. In the "String to Table" scenario, replace the **Trigger on Webhook** node with a **NodulInput** node and replace the **Webhook Response** node with a **NodulOutput** node;

> ??

You can add XML code for the icon in the "Icon (svg)" field to make the scenario easier to identify.

3. Change the current scenario name "String to Table" to "Al Tools/Actions/GoogleSheetAddRow";

> ?? The "Al Tools/Actions" part of the name is necessary for storing the scenario as an **Action** node in the Al Tools folder.

4. Change the scenario type to **Nodul**;

> ?? Next to the scenario name, after changing the type, icons are used to denote "Nodul" (a sign of a **Nodul** type scenario) and "Private" (indicating no public access to the scenario).

5. \*\*\*\*Add a parameter to the **NodulInput** node, for example, **User** - a text string. You can add parameters using the "Add Parameter" button.

6\*\*.\*\* Adjust the settings of the **Add Single Row** node so that the text added to the table row is equal to the value of the **User** parameter in the **NodulInput** node.

7\*\*.\*\* Add the execution result of the "Ok" scenario to the **Result** field of the **NodulOutput** node\*\*;\*\*

8. Create a scenario of type **Scenario** with the name "Get and Write Users," where the result of execution involves retrieving user data, transforming it, and writing the username to a Google Sheet.

* Add a **Trigger on Webhook** node to trigger the "Get and Write Users" scenario and pass JSON with user data into it:

```json
{
	"Surname": "John",
	"Name": "Doe",
	"Email": "a0128997@gmail.com"
}
```

* Add a **JavaScript** node to create the full user name based on the data received in the **Webhook** using code:

```jsx
export default async function run({execution_id, input, data}) {

const SurName = data["{{1.body.Surname}}"];
const Name = data["{{1.body.Name}}"];
const FullName = Name +' '+ SurName;

    return {
      FullName
    }
}
```

* Add a **GoogleSheetAddRow** node (**Nodul** type scenario) to write the full user name obtained in the **JavaScript** node into a Google Sheet;

* Add a **Webhook response** node to receive a response from the **GoogleSheetAddRow** node indicating successful execution.

9. **Save** and activate the scenario.

The result of the scenario is the recording of a row in a Google Sheet and a successful row recording response.

In the future, if user information comes from new sources or requires different processing, the **GoogleSheetAddRow** node can be reused without reconfiguring the logic for recording rows in Google Sheets.

# NodulInput

## **Node Description**

**NodulInput** - a node of the action type, necessary for creating a scenario of the **Nodul** type. This node serves as an entry point into the **Nodul** type scenario and defines the form of the scenario node, i.e., its parameters.

> 💡 See [Utilizing the NodulInput node to create a scenario of the Nodul type](../../get-started/introduction.mdx)

## **Node Configuration**

To configure the **NodulInput** node, it is necessary to fill in optional fields, including the creation of node parameters.

### Parameter Constructor

Adding parameters to the node is available by clicking the **Add parameter** button.

When adding a parameter, it is necessary to specify the **Parameter type** (e.g., string) and the **Parameter key** (e.g., Value) and then click the **Add** button.

After adding the parameter, it is necessary to define its **Name** in the respective field and, if needed, fill in optional parameters:

* Determine the requirement attribute by checking the **Required (1)** checkbox;
* Add a description of the parameter in the **Description (2)** field for subsequent tooltip display;

* Add a value in the **Default Value** field to display it in the parameter field when the node is initially opened.

### Parameter Constructor. Options

In the **Options** section, you can define additional characteristics of the parameter:

* **Min length** - the minimum allowable number of characters in the parameter's value. If the character count is less than this, the parameter will be highlighted;
* **Prefix;**
* **Fetch events** - the need to update the node's form when selecting a parameter value:

If **Change** is selected, the node's form will be updated every time the parameter is reselected.

If **Init** is selected, the node's form will be updated during the initial parameter input.

If both **Change** and **Init** are selected, the node's form will be updated every time the parameter is reselected and during the initial node opening.

### Personalization of Nodul

A scenario of the **Nodul** type, created using the **NodulInput** node, is displayed in the list of all nodes after pressing the add node buttons.

The icon of such a scenario can be personalized by filling in the fields of the **NodulInput** node:

* **Color (HEX) (1)** - color representation in HEX format;
* **Icon (svg)** **(2)** - icon representation in svg format.

# NodulOutput

## **Node Description**

**NodulOutput** - an action type node necessary for creating a **Nodul** type scenario. This node is required to generate a response for a **Nodul** type scenario in response to an incoming request.

> 💡 See [Utilizing the NodulInput node to create a scenario of the Nodul type](../../get-started/introduction.mdx).

## **Node Configuration**

To configure the **NodulOutput** node, it is necessary to fill in the optional fields.

### Output Type

Field for configuring the type of response to the request in a **Nodul** type scenario. The response can be either a successful execution (Ok) or an error (Error). There is a toggle switch above the field called Selection/Substitution. Depending on the chosen value in the **Output Type** field, you can:

* Select a value from the dropdown list: Ok, Error;

> 💡

* Substitute any values, including values or parameters from other nodes. Operators can also be used.

### Result

This field represents the response generated by the **NodulOutput** node upon receiving the selected response from the previous node specified in the **Output Type** field.

> 💡 In the **Result** field, you can input text, variables from other nodes, or parameters from responses received from other nodes.

> 💡

Any value other than Ok will be interpreted as an error, similar to the Error value.

# Bun

## **Node Description**

The **Bun** runtime executes JavaScript code inside automation scenarios.

It is largely compatible with **Node.js**, but provides higher performance and additional built-in features such as **SQLite**, a fast package manager, and improved APIs.

In the low-code environment, **Bun** works the same way as **Node.js** — through the [JavaScript](./javascript.mdx) node, with a runtime switch available in settings.

## Adding Code to a Scenario

To add **Bun** code:

1. Add a **JavaScript** node to your scenario.
2. In the node settings, switch the runtime to **Bun**.
3. Edit the code template manually or with AI assistance.

## Data Exchange Between Nodes

### Using Data from Previous Nodes

You can access output data from previous nodes via the `data` object:

```jsx
export default async function run({ data }) {
  const username = data["{{1.body.user}}"];
  return { user: username };
}
```

### Passing Processed Data to Subsequent Nodes

A **Bun** node can return strings, numbers, JSON objects, or arrays:

```jsx
export default async function run() {
  return {
    status: "ok",
    count: 42,
  };
}
```

## Using NPM Packages

**Bun** supports importing **npm** libraries with the `import` statement.

Dependencies are installed automatically after saving the scenario.

```jsx
import axios from "axios";

export default async function run() {
  const response = await axios.get("https://api.github.com/repositories");
  return { total: response.data.length };
}
```

  Some libraries may behave differently in Bun than in Node.js. Always check compatibility.

## Bun-Specific Features

### SQLite Support

**Bun** provides a built-in `bun:sqlite` module:

```jsx
import { Database } from "bun:sqlite";

export default async function run() {
  const db = new Database(":memory:");
  db.run("CREATE TABLE users (id INTEGER, name TEXT)");
  db.run("INSERT INTO users VALUES (?, ?)", [1, "Alice"]);

  const row = db.query("SELECT * FROM users").get();
  return { user: row };
}
```

### Logging

Use `console.log` for debugging. Output will appear in the **Log** tab.

## Limitations in Low-Code Environment

  The environment is isolated: listening to ports, running HTTP/WebSocket servers, or background daemons is not possible.

* Maximum execution time: **2 minutes**
* Only **JavaScript** is supported. TypeScript/JSX syntax (`: type`, interfaces, generics) is not available
* Use `import` instead of `require`
* Some Node.js core modules are not supported
* Not all npm packages are guaranteed to work
* `Bun.serve` and any server creation are not supported

# Code examples

Table of contents:

1. **Integration with Mongo DB Atlas**
2. **JS Node. Make parallel HTTP requests**
3. **Processing and Transforming Data from the Previous Node**

## **1. Integration with Mongo DB Atlas**

```jsx
import { MongoClient } from 'mongodb';

export default async function run({execution_id, input, data}) {

    // MongoDB Connection String
    // Structure:
    // mongodb+srv://USERNAME:PASSWORD@CLUSTER_ADDRESS/DATABASE
    // USERNAME: User's name for authentication
    // PASSWORD: Password for authentication
    // CLUSTER_ADDRESS: Address to your MongoDB cluster
    // DATABASE: Default database to use (optional)
    const connectionString = 'mongodb+srv://USERNAME:PASSWORD@CLUSTER_ADDRESS/DATABASE';

    // Connecting to the MongoDB client
    const client = await MongoClient.connect(
      connectionString,
      { useNewUrlParser: true, useUnifiedTopology: true } // Options for the connection
    );

    // Selecting the 'parsing-m' database and 'apps' collection
    const coll = client.db('parsing-m').collection('apps');

    // Finding the last 3 records where processed is not equal to true
    const filter = {processed:{$ne: true}};
    // Sorting by the "sort" field in descending order (replace "sort" with the actual field name)
    const cursor = coll.find(filter).sort({"sort": -1}).limit(3);

    // Converting the cursor to an array to retrieve the result
    const result = await cursor.toArray();

    // Closing the connection to the MongoDB client
    await client.close();

    return result;
}
```

## 2. JS Node. Make parallel HTTP requests

You can make parallel HTTP requests using the [JavaScript](./javascript.mdx) node.

```jsx
/*
* This code is structured to handle multiple HTTP GET requests concurrently,
* using axios to perform the requests and Promise.all to manage them simultaneously.
*/

// Importing the axios library for making HTTP requests
import axios from "axios";

export default async function run({ execution_id, input, data }) {
  // Defining an array of URLs to make HTTP requests to
  const urls = ['https://dummyjson.com/carts', 'https://dummyjson.com/users', 'https://dummyjson.com/quotes'];

  try {
    // Using Promise.all to perform simultaneous HTTP requests to the URLs defined above
    // The map function applies 'httpRequest' to each URL in the 'urls' array
    const results = await Promise.all(urls.map(url => httpRequest(url)));

    // Returning the results of the HTTP requests
    // This is where you can handle the results as needed in your application
    return {
      res: results
    };
  } catch (error) {
    // Logging any errors to the console
    console.error(error);
    // Rethrowing the error to be handled by the caller of this function
    throw error;
  }

  // Defining an asynchronous function 'httpRequest' to handle individual HTTP requests
  async function httpRequest(rawURL) {
    try {
      // Making a GET request to the provided URL using axios
      const response = await axios({
        method: "GET",
        url: rawURL
      });
      // Returning the data part of the response
      // This can be modified according to the needs of the application
      return response.data;
    } catch (error) {
      // Logging any errors encountered during the HTTP request
      console.error(error);
      // Rethrowing the error to be handled by the caller of 'httpRequest'
      throw error;
    }
  }
}
```

## 3. Processing and Transforming Data from the Previous Node

```jsx
export default async function run({execution_id, input, data}) {
// const - is the syntax for creating a constant
// SurName - the name of the constant
// data["{{1.body.Surname}}"] - the value of the constant. The expression is added automatically when you click on "SurName" in the Data window.
const SurName = data["{{1.body.Surname}}"];
const Name = data["{{1.body.Name}}"];
const FullName = Name +' '+ SurName;
const Email = data["{{1.body.Email}}"];
const LastAction = data["{{1.body.LastAction}}"];
const message = `Hi, ${FullName}! The last time you visited Latenode ${LastAction}.`;

// JSON assembly
    const resultRawJSON = JSON.stringify({
      "from_email": "test@gmail.com",
      "to": Email,
      "subject": "Latenode",
      "text": message,
    });

//Returning values
    return {
      resultRawJSON
    }
}
```

# Custom JS Parameters

Custom parameters are necessary to "extract" certain parts from the code and fill them in special fields without editing the code directly.

For example, if an API key is used in the code, you can generate a separate field in the JavaScript node for entering this parameter and reference it in the code. This way, when the API key changes, you only need to update the value in the separate field, not the code.

## Parameter Description

To display input fields for parameters in the node interface:

1. Add parameter descriptions to the code.
2. Click the **Generate Parameters** button.

You can use the following template for parameter descriptions:

```jsx
/** @CustomParams
{
	"parameter1": {
	  "type": "string",                  // Type of the parameter, required
	  "title": "Name_parameter1",        // Name of the parameter, required
	  "required": true,                  // Parameter requirement, optional (but recommended to fill)
	  "description": "Enter parameter1", // Parameter description, optional
	  "options": {                       // Parameter options, optional
		  "minLength": 10
	  }
	},
	"parameter2": {
	  "type": "int",
	  "title": "Name_parameter2",
	  "required": true,
	  "description": "Enter parameter2",
	  "options": {
		  "minLength": 10
	  }
	}
}
*/
```

## Parameter Types and Options

### Connection (connection)

The connection type parameter is used for entering a connection by selecting it in the auxiliary window.

Template:

```javascript
/** @CustomParams
{
	"parameter": {
	  "type": "connection",
	  "title": "connection_parameter",
	  "required": false,
	  "description": "Enter parameter"
	}
}
*/

```

Below is an example code that adds a row to a Google Sheet. The data for the row, including the token for connection, is entered as parameters.

```jsx
/** @CustomParams
{
    "access_token": {
        "type": "connection",
        "required": true,
        "title": "Google Sheet Connection",
        "description": "Google sheet authorization. Use \"Authorization\" field"
    },
    "spreadsheetId": {
        "type": "string",
        "required": true,
        "title": "Spreadsheet ID"
    },
    "sheetName": {
        "type": "string",
        "required": true,
        "title": "Sheet Name"
    },
    "values": {
        "type": "string_array",
        "title": "Values"
    }
}
*/

import axios from 'axios';

export default async function run({execution_id, input, data, store}) {
    const accessToken = JSON.parse(data.access_token).access_token;
    const spreadsheetId = data.spreadsheetId;
    const sheetName = data.sheetName;
    const values = [data.values];

    const appendOptions = {
        range: sheetName,
        valueInputOption: 'USER_ENTERED',
        insertDataOption: 'INSERT_ROWS',
        includeValuesInResponse: true,
    };

    try {
        const response = await axios({
            method: 'post',
            url: `https://sheets.googleapis.com/v4/spreadsheets/${spreadsheetId}/values/${encodeURIComponent(sheetName)}:append`,
            params: appendOptions,
            headers: {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            },
            data: {
                values: values,
            },
        });

        return {
            appendedData: response.data,
        };
    } catch (error) {
        console.error('Error appending data to Google Sheet:', error);
        return {
            error: error.response?.data || error.message,
        };
    }
}
```

### String (string)

The string type parameter is used for entering text. You can use the minLength option to define the minimum number of characters required.

Template:

```jsx
/** @CustomParams
{
	"parameter": {
	  "type": "string",
	  "title": "string_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "minLength": 10
	  }
	}
}
*/
```

Below is an example code that counts the number of characters in the specified parameter.

```jsx
/** @CustomParams
{
	"parameter2": {
	  "type": "string",
	  "title": "string_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "minLength": 10
	  }
	}
}
*/

export default async function run({ execution_id, input, data, store }) {
    // The input string parameter is obtained from the data object
    const String = data.parameter2;

    // Ensure parameter2 is a string
    if (typeof String !== 'string') {
        throw new Error('Parameter "String" must be a string.');
    }

    // Count the number of characters in the string
    const characterCount = String.length;

    // Return the character count
    return {
        characterCount
    };
}
```

### Integer (int)

The integer type parameter is used for entering whole numbers. You can use the following options for this parameter:

* max: maximum number
* min: minimum number

Template:

```jsx
/** @CustomParams
{
	"parameter": {
	    "type": "int",
	    "title": "int_parameter",
		"required": true,
		"description": "Enter parameter",
	    "options": {
	        "max": 100,
	        "min": 50
	    }
	}
}
*/
```

Below is an example code that generates a random number not exceeding the value specified in the parameter.

```jsx
/** @CustomParams
{
	"parameter3": {
	    "type": "int",
	    "title": "int_parameter",
		"required": true,
		"description": "Enter parameter",
	    "options": {
	        "max": 100,
	        "min": 50
	    }
	}
}
*/

import { randomInt } from 'crypto';

export default async function run({ execution_id, input, data, store }) {
    // The input parameter MaxN is obtained from the data object.
    const MaxN = data.parameter3;

    // Ensure MaxN is a number.
    if (typeof MaxN !== 'number') {
        throw new Error('MaxN should be a number.');
    }

    // Generate a random number from 0 to MaxN (not including MaxN).
    const randomNumber = randomInt(MaxN);

    // Return the generated random number.
    return {
        randomNumber
    };
}
```

### String Array (string\_array)

A string array type parameter is used for entering a list of strings. You can use the maxCount option to define the maximum number of strings allowed.

Template:

```jsx
/** @CustomParams
{
	"parameter": {
	  "type": "string_array",
	  "title": "string_array_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "maxCount": 2
	  }
	}
}
*/
```

Below is an example that outputs the array specified in the parameter and the number of elements in it.

```jsx
/** @CustomParams
{
	"parameter4": {
	  "type": "string_array",
	  "title": "string_array_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "maxCount": 5
	  }
	}
}
*/

export default async function run({ execution_id, input, data, store }) {
    // The input array parameter is obtained from the data object.
    const array = data.parameter4;

	// Ensure parameter4 is an array.
    if (!Array.isArray(array)) {
        throw new Error('Parameter "parameter4" must be an array.');
    }

    // Count the number of strings in the array.
    const stringCount = array.length;

    // Return the count result.
    return {
        array,
		stringCount
    };
}
```

### Key-Value (string\_to\_string)

The key-value parameter type is used for entering a list of strings in a key-value format.

Template:

```jsx
/** @CustomParams
{
	"parameter": {
	  "type": "string_to_string",
	  "title": "string_to_string_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "maxCount": 2
	  }
	}
}
*/
```

Below is an example that identifies the highest value and its key from the list of values in the parameter.

```jsx
/** @CustomParams
{
	"parameter5": {
	  "type": "string_to_string",
	  "title": "string_to_string_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "maxCount": 2
	  }
	}
}
*/

export default async function run({execution_id, input, data}) {
    // Ensure parameter5 exists and is an object.
    if (typeof data.parameter5 !== 'object' || data.parameter5 === null) {
        throw new Error('parameter5 is missing or not an object');
    }

    // Initialize variables to store the maximum value and the corresponding key.
    let maxKey = null;
    let maxValue = -Infinity;

    // Iterate through all keys and values in the parameter5 object.
    for (const [key, value] of Object.entries(data.parameter5)) {
        // Convert the value to a number.
        const numericValue = parseFloat(value);

        // Check if the current value is the highest.
        if (numericValue > maxValue) {
            maxValue = numericValue;
            maxKey = key;
        }
    }

    // Return the maximum value and its key.
    return {
        maxKey,
        maxValue
    };
}
```

### Dropdown List (select)

The dropdown list parameter type is used to select a value from a predefined list of possible values. You can use the following options for this parameter:

* options: an array like `[{ "key": "SelectOptionKey1", "value": "SelectOptionValue1" }]`. (value is the value that will be displayed in the dropdown list, key is the key that will be used in the code).
* multiple: allows selecting multiple values.

Template:

```jsx
/** @CustomParams
{
	"parameter": {
	  "type": "select",
	  "title": "select_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "options": [{ "key": "SelectOptionKey1", "value": "SelectOptionValue1" }, { "key": "SelectOptionKey2", "value": "SelectOptionValue2" }],
      "multiple": false
	  }
	}
}
*/
```

Below is an example that outputs the selected value of the parameter.

```jsx
/** @CustomParams
{
	"parameter6": {
	  "type": "select",
	  "title": "select_parameter",
	  "required": false,
	  "description": "Enter parameter",
	  "options": {
		  "options": [{ "key": "1", "value": "100" }, { "key": "2", "value": "200" }],
      "multiple": false
	  }
	}
}
*/

export default async function run({ execution_id, input, data, store }) {
    // Create a mapping of keys to values for easy lookup.
    const optionsMapping = {
        "1": "100",
        "2": "200"
    };

    // Obtain the key selected by the user.
	const selectedKey = data.parameter6;

    // Find the corresponding value.
    const selectedValue = selectedKey ? optionsMapping[selectedKey] : undefined;

    if (selectedValue) {
        console.log('Selected value:', selectedValue);
        return { selectedValue };
    } else {
        console.log('Selected value not found.');
        return {};
    }
}
```

### Boolean (bool)

The boolean parameter type is used for entering a true/false value.

Template:

```jsx
/** @CustomParams
{
	"parameter": {
	  "type": "bool",
	  "title": "bool_parameter",
	  "required": false,
	  "description": "Enter parameter"
	}
}
*/
```

Below is an example code that outputs one value or another depending on whether the parameter is set to **`true`** or **`false`**.

```jsx
/** @CustomParams
{
	"parameter7": {
	  "type": "bool",
	  "title": "bool_parameter",
	  "required": false,
	  "description": "Enter parameter"
	}
}
*/

export default async function run({execution_id, input, data, store}) {

	const TrueFalse = data.parameter7

	 // Check the value and return "Yes" or "No" based on the condition.
    const result = TrueFalse === true ? "Yes" : "No";

    return {
        result
    };
}
```

# Headless browser

## **Node Description**

A **Headless browser** - an action-type node that is required to configure interaction with a web browser using JavaScript code.

  You can use our GPT Assistant for help with **Headless browser**:

  ?? [**Latenode Headless Browser Assistant**](https://chatgpt.com/g/g-697239177f3481919bd3991f1430539e-latenode-headless-browser-assistant)

  It can help you generate Puppeteer code, handle selectors, debug browser automation scripts, and solve common headless browser challenges.

## Basic Example - Get the body content of a web page

````````````````````````jsx
// Open web page and return the content of ```````````````````````<body>``````````````````````` element
await page.goto('https://latenode.com');
const bodyContent = await page.evaluate(() => document.body.innerHTML);
return { bodyContent };
````````````````````````

## Example #2 - Wait for an HTML element before retrieving a web page's body content

Some web pages load content dynamically using JavaScript. In these cases, you need to wait for a specific selector to appear before proceeding using �await page.waitForSelector�, as shown in the example below

````````````````````````jsx
/*
* Headless browser automation with Puppeteer
* Documentation: https://latenode.com/help/headless_browser
* AI assistant to write code for Headless Browser: https://latenode.com/help/headless_browser_assistant
*/

// Basic example: Open web page and return the content of ```````````````````````<body>``````````````````````` element
await page.goto('https://latenode.com');
await page.waitForSelector('#termly-consent-preferences');

// Wait for the body to load and extract its content
const bodyContent = await page.evaluate(() => document.body.innerHTML);

return {
    bodyContent
};
````````````````````````

You could get a selector here:

## **Node Configuration**

To configure the **Headless browser** node, you need to:

* Create the code in the **Code** window according to the requirements for interacting with the browser;
* If necessary, fill out the **Proxy** field block.

### **Proxy**

The configuration block with fields:

* **Enter proxy address** - a field for entering the proxy address through which the request needs to be forwarded.
* **Enter login** - a field for entering credentials for using the proxy.
* **Enter password** - a field for entering credentials for using the proxy.

These fields are filled out in case access to the required website is restricted to the local network only.

### **Data Processing Result**

The output of the **Headless Browser** can be a string, numerical value, JSON object, and so on. The data processing result from the **Headless Browser** node is accessible for configuring parameters of other nodes.

  It is recommended to wrap data in string format with quotation marks for further correct processing.

## Code

### **Libraries**

To interact with the browser using JavaScript, the [Puppeteer](https://pptr.dev/) library is used.

  In large JavaScript scripts, it may be necessary to install [Puppeteer](https://pptr.dev/) locally on your computer ([installation information](https://pptr.dev/#installation)). To install JavaScript libraries on your computer, you need to set up [NodeJS](https://nodejs.org/) and [NPM](https://www.npmjs.com/).

### Inital Function `run`

The original function of the **Headless browser** node looks like this:

```jsx
async function run({execution_id, input, data, page}) {
    return {

    }
}
```

The "page" parameter is the result of the call to [browser.newPage](https://pptr.dev/api/puppeteer.browsercontext.newpage/) [Puppeteer](https://pptr.dev/) library and has the corresponding [interface](https://pptr.dev/api/puppeteer.page/). All interactions with the browser page are performed using this parameter. There is **no** direct access to the [puppeteer](https://pptr.dev/) library or the browser from within this function.

  Almost all operations with the `page` object are asynchronous. For convenience, the original `run` function is declared with the `async` keyword, allowing you to write code using [`async/await`](https://learn.javascript.ru/async-await) for better handling of asynchronous operations.

### **Using the function** `callWebhook`

In the code of the **Headless Browser** node, there is no direct access to libraries like [axios](https://axios-http.com/) or [fetch](https://learn.javascript.ru/fetch).

To make asynchronous API calls, you can use the `callWebhook` function. It is based on the [axios](https://axios-http.com/) library but with slightly reduced functionality.

  With this function, you can make API requests **only to incoming Trigger on Webhook nodes created within the Latenode platform**. Requests to other domains will result in an error.

The interface of the `callWebhook(webhookUrl, options)` function is similar to the interface of [axios request](https://axios-http.com/docs/req_config) and consists of:

* `webhookUrl` - the URL of an incoming **Trigger on Webhook** within the [Latenode](https://app.latenode.com/) platform;
* `options` - an object with request options.

The response will be an object with an interface similar to [axios response](https://axios-http.com/docs/res_schema).

Here's an example of how to use the `callWebhook` function:

```jsx
async function run({execution_id, input, data, page}) {
  const response = await callWebhook("https://webhook.latenode.com/137/dev/db76895b-093b-4a6e-a3a1-57edcaa36a5c", {
    method: "POST",
    data: {
        "some": "data"
    }
  });
  console.log(response.data);
  return {

  }
}
```

As a result, the logs will display the object returned by the script, which was invoked via the `callWebhook` function for the respective **Trigger on Webhook**.

## **Examples**

### Google Search Query

```jsx
async function run({execution_id, input, data, page}) {
  await page.goto('https://google.com');
// Waiting for the appearance of the input field for entering the search query
  await page.waitForXPath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input');
  const searchInput =
      (await page.$x('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))[0];
// Entering the search query
  await searchInput.type('Hello world');

  const searchButton = (await page.$x('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]'))[0];
// Pressing the search button
  await searchButton.click();
// Waiting for the appearance of the results page.
// Here, any XPath to an element
// that reliably appears after a successful search can be used
  await page.waitForXPath('//*[@id="result-stats"]');

// Selecting all results
  const results = await page.$x('//*/a/h3[@class]');

  const responseArray = [];
// Building the final array
  for (let result of results) {
      responseArray.push(await page.evaluate(el => ({ title: el.textContent }), result))
  }

// Returning the data
  return {
      responseArray
  }
}
```

  An example script using the **Headless Browser** node can be found in the [Building Scenarios](../scenarios/building_scenarios.mdx) documentation.

## Possible problems

### UserAgent

Some websites may not open through a Headless Browser. In such cases, you should use the [page.setUserAgent](https://pptr.dev/api/puppeteer.page.setuseragent/) function.

```jsx
await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36');
```

### Can't find XPath

A Headless Browser opens the browser using the [puppeteer](https://pptr.dev/) library, which, in turn, opens a page with a specific `viewport`. Websites can have responsive designs, so there may be differences in layout between a local computer and the **Headless Browser**. You can change the page's `viewport` using the [page.setViewport](https://pptr.dev/api/puppeteer.page.setviewport/) function.

```jsx
await page.setViewport({
  width: 1440,
  height: 900,
});
```

# JavaScript

## **Node Description**

**JavaScript** - an action-type node that is essential for processing data used in a scenario using the JavaScript programming language.

## **Node Configuration**

### **Code Generation**

To configure a **JavaScript** node, you need to generate code within the **Code** window in accordance with the data processing requirements.

The available parameters from previous nodes are displayed in the **Data** window. For more information on using data from previous nodes, please refer to the documentation under [Passing Data](../javascript/passing_data.mdx).

### **Data Processing Result**

The output of the **JavaScript** operation can be a string, numerical value, JSON object, and so forth. The data processing result from the **JavaScript** node is accessible for configuring parameters of other nodes.

  It is recommended to wrap data in string format with quotation marks for further correct processing.

# Managing files on FTP using JS

With the code generated in the **JavaScript** node, file management on an FTP server is possible. For a specific directory on the designated FTP server, the following actions are available:

* Retrieving a list of files.
* Retrieving a file, including its content.
* Uploading a file.
* Deleting a file.

## **Retrieving files**

To ***retrieve*** a file using the **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the script with the following code:

```jsx
import FTP from 'promise-ftp';

export default async function run({ execution_id, input, data, store }) {
  const ftp = new FTP();
  try {
    await ftp.connect({
      host: 'You_host', // Replace with your FTP server's host
      user: 'You_login',        // Replace with your FTP username
      password: 'You_password'     // Replace with your FTP password
    });

   // Defining the path to the file.
   // The parameter can be obtained from the output parameters of the previous nodes
    const remoteFilePath = "/htdocs/index2.html";
    const stream = await ftp.get(remoteFilePath);

    // Read the stream and convert it to a string
    let fileContent = '';
    for await (const chunk of stream) {
      fileContent += chunk.toString();
    }

    // Disconnect from the FTP server
    await ftp.end();

    // Extract the filename and extension
    const filename = remoteFilePath.replace(/^.*[\\\/]/, ''); // Remove directory path if present
    const extension = filename.split('.').pop();

    return {
      content: fileContent,
      extension: extension,
      filename: filename
    };
  } catch (error) {
    // If there's an error, disconnect and throw the error
    await ftp.end();
    throw error; // The error will be handled by the platform
  }
}
```

This code contains a function to connect to the FTP server with specified credentials, retrieve the content of the file from the given path **`remoteFilePath`**, read the file, extract its name **`filename`**, and extension **`extension`**, and return this data. In case of an error, the code disconnects from the FTP server and passes the error for platform handling.

2. Run the **JavaScript** node once and wait for its execution;

3. Examine the **JavaScript** node's output data for file attributes, including its content:

## **Retrieving a list of files**

To ***retrieve a list*** of files using the **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the script with the following code:

```jsx
import FTP from 'promise-ftp';

export default async function run({execution_id, input, data, store}) {
    const ftp = new FTP();
    try {
        await ftp.connect({
      host: 'You_host', // Replace with your FTP server's host
      user: 'You_login',        // Replace with your FTP username
      password: 'You_password'     // Replace with your FTP password
        });

        // Change to the directory you want to list files from, if needed
        await ftp.cwd('/htdocs');

        // Get the list of files
        let fileList = await ftp.list();

        // Filter out hidden files and folders
        fileList = fileList.filter(file => !file.name.startsWith('.'));

        // Disconnect from the FTP server
        await ftp.end();

        // Return the file list
        return {
            fileList
        };
    } catch (error) {
        // If there's an error, disconnect and throw the error
        await ftp.end();
        throw error;
    }
}
```

This code connects to the FTP server, changes the working directory to **`/htdocs`** (if necessary), retrieves the list of files, excludes hidden files and folders, and then returns this list **`fileList`**. In case of an error, the code disconnects from the FTP server and passes the error for platform handling.

2. Run the **JavaScript** node once and wait for its execution;

3. Examine the **JavaScript** node's output data, an array of files, including parameters for each file:

```jsx
{
"type": "-",
"name": "index2.html",
"sticky": false,
"rights": {
"user": "rw",
"group": "r",
"other": "r"
},
"acl": false,
"owner": "0",
"group": "2",
"size": 2064,
"date": "2024-01-22T03:38:00.000Z"
}
```

## **Uploading a file**

To ***upload*** a file to an FTP server using the **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the script with the following code:

````````````````````````jsx
import FTP from 'promise-ftp';

export default async function uploadFile({ execution_id, input, data, store }) {
  const ftp = new FTP();
  try {
    await ftp.connect({
      host: 'You_host', // Replace with your FTP server's host
      user: 'You_login',        // Replace with your FTP username
      password: 'You_password'     // Replace with your FTP password
    });

    // Example: HTML content to upload
    const htmlContent = "```````````````````````"; // Replace this with your actual HTML content

    // Convert the HTML content to a buffer
    const buffer = Buffer.from(htmlContent, 'utf-8');

    // Defining the path to the file.
    // The parameter can be obtained from the output parameters of the previous nodes
    const remoteFilePath = '/htdocs/index3.html';

    // Upload the buffer to the FTP server
    await ftp.put(buffer, remoteFilePath);

    // Disconnect from the FTP server
    await ftp.end();

    return {
      message: `File uploaded successfully as ${remoteFilePath}`
    };
  } catch (error) {
    // If there's an error, disconnect and throw the error
    await ftp.end();
    throw error; // The error will be handled by the platform
  }
}
````````````````````````

This code is designed to connect to the FTP server, upload a file with HTML content **`htmlContent`**, and return a success message **`message`**. The file is created from HTML content and uploaded to the server at the specified path **`remoteFilePath`**. In case of an error during connection or upload, the connection to the server is closed, and the error is passed for platform handling.

2. Run the **JavaScript** node once and wait for its execution;

3. Examine the **JavaScript** node's output data for a successful upload message with the file location:

## **Deleting a file**

To ***delete*** a file from an FTP server using the **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the script with the following code:

```jsx
import FTP from 'promise-ftp';

export default async function deleteFile({ execution_id, input, data, store }) {
  const ftp = new FTP();
  try {
    await ftp.connect({
      host: 'You_host', // Replace with your FTP server's host
      user: 'You_login',        // Replace with your FTP username
      password: 'You_password'     // Replace with your FTP password
    });

    // Defining the path to the file.
    // The parameter can be obtained from the output parameters of the previous nodes
    const remoteFilePath = '/htdocs/index3.html';

    // Delete the file from the FTP server
    await ftp.delete(remoteFilePath);

    // Disconnect from the FTP server
    await ftp.end();

    return {
      message: `File ${remoteFilePath} deleted successfully`
    };
  } catch (error) {
    // If there's an error, disconnect and throw the error
    await ftp.end();
    throw error; // The error will be handled by the platform
  }
}
```

This code is designed to connect to an FTP server and delete a file located at the path specified in the variable **`remoteFilePath`**. After a successful connection, the code deletes the file from the server. If the file is successfully deleted, the function returns a `message` stating that the file has been removed. In case of an error during the connection or file deletion process, the server connection is closed, and the error is passed for handling by the platform.

2. Run the **JavaScript** node once and wait for its execution;

3. Examine the **JavaScript** node's output data for a successful file deletion message:

# Node.js

The [JavaScript](./javascript.mdx) node allows you to write and execute JavaScript code, import npm libraries, and handle various data processing tasks. This node provides robust support for integrating custom code into workflows, enhancing the flexibility and functionality of your scenarios.

## Adding Code to a Scenario

To add code to a scenario, follow these steps:

1. Click on one of the buttons to add a node.
2. In the application selection window, choose the [JavaScript](./javascript.mdx) node.

3. Open the added JavaScript node and make changes to the code template manually or with the help of the AI assistant.

## Data Exchange Between Nodes

### Using Data from Previous Nodes in Code

The code generated in the [JavaScript](./javascript.mdx) node can utilize the output data from previous nodes in the scenario. For example, in a JavaScript node, you can reference a parameter passed to the **Trigger on Webhook** node via an HTTP request. To do this, follow these steps:

* Write an expression to define a constant using `const =`.
* Select the necessary parameter from the previous nodes.

By doing so, you can seamlessly integrate and manipulate data across different nodes within your scenario.

  When adding data from other nodes, part of the expression may be wrapped in backticks. For example: `data["{{1.headers.Content-Type}}"]`, even if another node returned the property without them. It is not necessary to remove the backticks, as they will be ignored during code execution. Removing them manually may result in code execution errors.

### Passing Processed Data to Subsequent Nodes

The result of the [JavaScript](./javascript.mdx) node can be a string, numerical value, JSON object, etc. The output data from the **JavaScript** node can also be used in other nodes within the scenario. For example, a parameter generated in the **JavaScript** node can be recorded as a variable. To do this:

1. In the **SetVariables** node, click on the **Value** field.

2. In the auxiliary window, select the parameter generated in the **JavaScript** node.

This way, you can efficiently pass and utilize processed data between nodes in your workflow.

### Using Variables

Variables created within the scenario or global variables can also be used in the [JavaScript](./javascript.mdx) node.

  Variables created within the scenario or global variables can also be used in the [JavaScript](./javascript.mdx) node.

  Learn more about using variables in the JavaScript node [here](../variables/variables-in-javascript-node.mdx). Learn more about using global variables in the **JavaScript** node [here](../variables/global-variables-in-javascript-node.mdx).

### Processing Files or Arrays of Files

The [JavaScript](./javascript.mdx) node can process files or arrays of files. For example, to upload a single file, you can use the following code:

```jsx
async function run({execution_id, input, data, page}) {
  const file = data["{{2.body.files.[0].content}}"];
  const uploadForm = await page.$x('//*/input[@type="file"]'))[0].uploadFile(file);
}
```

To iterate through an array of files with a known length, for example, 5, write the following code:

```jsx
async function run({execution_id, input, data, page}) {
  const files = [
    data["{{2.body.files.[0].content}}"],
    data["{{2.body.files.[1].content}}"],
    data["{{2.body.files.[2].content}}"],
    data["{{2.body.files.[3].content}}"],
    data["{{2.body.files.[4].content}}"]
  ].filter(file => file && file !== 'null');

  const uploadForm = await page.$x('//*/input[@type="file"]')[0];
  for (let file of files) {
      await uploadForm.uploadFile(file);
  }
}
```

### Return files from JavaScript

In a JavaScript node, you can create and edit files in the filesystem using, for example, the fs package. To return files from the node, you can use the following functions:

* `file(filePath)` � returns a single file from the specified path. The filePath parameter must be a string.
* `files(filePaths)` � returns an array of files from the specified paths. The filePaths parameter must be an array of strings.

  **Important:** These functions only work at the first level of nesting in the returned data from the node.

Example code:

```jsx
import fs from 'fs';
export default async function run({execution_id, input, data, store, db}) {
    fs.writeFileSync('file1.txt', 'some file content 1');
    fs.writeFileSync('file2.txt', 'some file content 2');
    fs.writeFileSync('file3.txt', 'some file content 3');
    return {
        file: file('file1.txt'),
        files: files(['file2.txt', 'file3.txt'])
    }
}
```

This will **not** work (functions file/files are deeper than the first level of nesting):

```jsx
import fs from 'fs';
export default async function run({execution_id, input, data, store, db}) {
    fs.writeFileSync('file1.txt', 'some file content 1');
    fs.writeFileSync('file2.txt', 'some file content 2');
    fs.writeFileSync('file3.txt', 'some file content 3');
    return {
        object: {
            file: file('file1.txt'),
            files: files(['file2.txt', 'file3.txt'])
        }
    }
}
```

## Custom Parameters in JavaScript

Custom parameters in the [JavaScript](./javascript.mdx) node allow you to externalize certain parts of the code into special input fields, eliminating the need to edit the code itself.

For example, if your code uses an API key, you can generate a separate input field for this parameter in the JavaScript node. This way, you only need to change the value in the designated field rather than modifying the code directly when updating the API key.

  Learn more about all possible custom parameters [here](./custom-js-parameters.mdx).

## Logging

Logging in the [JavaScript](./javascript.mdx) node is available using the `console.log` command. Logged data will be displayed in the **Log** tab.

## Using NPM Packages

The [JavaScript](./javascript.mdx) node supports the import of **npm** libraries using the `import` statement. For example, importing and using the "lodash" library:

You can specify the version of the library you want to use with the `@` symbol. For example:

```jsx
import _ from 'lodash@4.16.6';
import _ from 'axios@^1.2.0';
```

After each scenario with a **JavaScript** node is saved, a check is performed to see if there are any library imports and changes to the list of libraries and their versions (if specified):

* If there are changes, the libraries are installed.
* If there are no changes, the saved libraries and versions are used.

  Library installation takes some time. If the user starts the node before the installation is complete, an error message will appear: "Dependency installation is not yet completed. Please try again in a few seconds." In this case, simply wait a short while before proceeding.

**Node Package Manager (NPM)** is a tool for developers working with Node.js, as it allows them to leverage a vast library of ready-made packages and easily manage project dependencies. Using the **axios** package enables developers to easily fetch data from external APIs or other web services without having to write extensive code for handling HTTP requests and responses.

An example of such a scenario is fetching a list of current GitHub repositories based on a selected programming language using the **axios** package:

```jsx
import axios from "axios";

export default async function run({ execution_id, input, data }) {
  const language = "Javascript";
  const url = `https://api.github.com/search/repositories?q=language:${encodeURIComponent(
    language
  )}&sort=stars&order=desc`;

  try {
    const response = await axios({
      method: "GET",
      url: url,
    });

    const repos = response.data.items.map((repo) => ({
      name: repo.name,
      owner: repo.owner.login,
      stars: repo.stargazers_count,
      url: repo.html_url,
    }));

    return {
      trending_repositories: repos,
    };
  } catch (error) {
    console.error(error);
    return {
      error: "An error occurred while fetching data from the GitHub API.",
    };
  }
}
```

Another example of using NPM packages is a scenario for calculating the time remaining until a deadline using the **Moment** package:

```jsx
import moment from "moment";

export default async function run({ execution_id, input, data }) {
  const deadline = "25.10.2024"; // Retrieve deadline from input
  const now = moment(); // Get current time
  const deadlineMoment = moment(deadline, "DD.MM.YYYY"); // Parse deadline string to Moment object using custom format
  const remainingTime = deadlineMoment.from(now); // Calculate remaining time

  return {
    remainingTime
  };
}
```

## JavaScript Node Limitations

The maximum execution time for the [JavaScript](./javascript.mdx) node is **2 minutes**.

  You can add multiple JavaScript nodes to a scenario for sequential execution to handle more complex tasks.

# Using AI to Generate Code (Ai Node)

An AI assistant is available inside the JavaScript node. It helps you generate, modify, and debug code directly inside your scenario ? just by describing what you want in natural language.

The assistant works contextually: it understands the current node, available data, and even connections to other blocks. You can ask it to build logic, create inputs, work with global variables, integrate with APIs, and more.

## Where the AI Assistant Is Available

You can launch AI Assistant in two ways:

**1.Via the "AI Node" button** at the bottom of the editor. This opens a dedicated chat window with assistant.

**2.Inside any JavaScript node**. Open the node and enter your message to start a conversation.

### Table of contents: What Assistant Can Do

1. **Create custom input parameters**
2. **Process data from other nodes**
3. **Work with global variables**
4. **Integrate with services like Telegram (example of creating custom api calls)**
5. **Debug and explain existing code**

* And more ? just describe your task!

## 1. Custom Parameters

Assistant can automatically create custom input parameters for your nodes.

Instead of hardcoding a value:

```
const message = "Hello world";
```

Copilot will rewrite it to:

```
const message = input.text_input;
```

And it will automatically add the `text_input` field to the node UI ? as shown in the screenshot above.

More info: [Custom JS Parameters](https://help.latenode.com/advanced-features/46DTZD5aggy7NR22L329Ge/custom-js-parameters/46DTZD5aggyL65Vhn4v8cA)

## 2. Request to process data from other nodes

> ? *Generate code to process data from the Trigger on Webhook node so that based on the Name and Count parameters, text is generated based on the following pattern: Hi, Name! Count of your scenarios has been executed in X on the Latenode platform! Instead of X, substitute the name of the current month.*

The assistant will provide the answer:

To generate the required text based on the parameters from the "Trigger on Webhook" node, you can follow these steps inside the provided?**`run`**?function. First, we'll extract the?**`Name`**?and?**`Count`**?values from the data provided by the webhook node with ID?**`4`**. Then, we'll use JavaScript's?**`Date`**?object to get the current month and format it as a name. Finally, we'll construct the message according to the pattern you've requested.

Here is how you can do it:

```jsx
export default async function run({execution_id, input, data, store}) {
    // Extracting Name and Count from the webhook data
    const name = data["{{4.`body`.`Name`}}"];
    const count = data["{{4.`body`.`Count`}}"];

    // Getting the current month as a name
    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const currentMonthName = monthNames[new Date().getMonth()];

    // Generating the message
    const message = `Hi, ${name}! ${count} of your scenarios has been executed in ${currentMonthName} on the Latenode platform!`;

    // Returning the generated message
    return {
        message
    };
}
```

Explanation:

* **`data["{{4.body.Name}}"]`**?and?**`data["{{4.body.Count}}"]`**?access the?**`Name`**?and?**`Count`**?values from the webhook's body.
* We use JavaScript's?**`Date`**?object to get the current month as an index (**`getMonth()`**?returns a zero-based index for the months), and then we use this index to get the month's name from the?**`monthNames`**?array.
* The message is constructed using template literals, embedding the?**`name`**,?**`count`**, and?**`currentMonthName`**?variables into the predefined text pattern.
* Finally, the function returns an object containing the generated message, which can be used by subsequent nodes in your scenario.

## 3. Request for processing global variables

> ?? It is assumed that global variables GlobalVar\_number1 and GlobalVar\_number2 exist in the account. See the section on global variables.

> ? *Generate code that adds up the values of two global variables GlobalVar\_number1 and GlobalVar\_number2 and return an array of the values: sum of variables, GlobalVar\_number1, GlobalVar\_number2. Get global variables using store.getGlobalVariable*

The assistant will provide the answer:

To accomplish the task you've described, we will use the?**`store.getGlobalVariable`**?method to retrieve the values of the global variables?**`GlobalVar_number1`**?and?**`GlobalVar_number2`**. Then, we'll add these values together, and return an array that includes the sum,?**`GlobalVar_number1`**, and?**`GlobalVar_number2`**?in that order. Here's how you can do it:

```jsx
export default async function run({execution_id, input, data, store}) {
    // Retrieve the values of the global variables
    const number1 = await store.getGlobalVariable('GlobalVar_number1');
    const number2 = await store.getGlobalVariable('GlobalVar_number2');

    // Convert the retrieved values to numbers, if they are not already
    const num1 = parseFloat(number1);
    const num2 = parseFloat(number2);

    // Calculate the sum of the two numbers
    const sum = num1 + num2;

    // Return an array with the sum, GlobalVar_number1, and GlobalVar_number2
    return {
        result: [sum, num1, num2]
    };
}
```

This code snippet does the following:

1. It uses?**`store.getGlobalVariable`**?to fetch the values of?**`GlobalVar_number1`**?and?**`GlobalVar_number2`**. These methods are asynchronous, so we use?**`await`**?to wait for the promises to resolve.
2. It then converts these values to numbers using?**`parseFloat`**?to ensure that arithmetic operations can be performed correctly. This is a safeguard in case the values are stored as strings.
3. It calculates the sum of the two numbers.
4. Finally, it returns an object with a?**`result`**?key that maps to an array containing the sum,?**`GlobalVar_number1`**, and?**`GlobalVar_number2`**.

Ensure that the global variables?**`GlobalVar_number1`**?and?**`GlobalVar_number2`**?are set and contain numeric values. If these variables contain non-numeric values,?**`parseFloat`**?will return?**`NaN`**, and the sum calculation will not work as expected.

## **4. Request to connect to Telegram to send messages (example of creating custom api calls)**

> ? *Generate a code with a Telegram connection to send a message to the desired chat room with a given ID*

The assistant will provide the answer:

To send a message to a Telegram chat room, you will need to use the Telegram Bot API. First, ensure you have created a bot and obtained your bot's API token from BotFather in Telegram. Then, you can use the?**`axios`**?library to make HTTP requests to the Telegram API. Here?s how you can do it:

1. **Install Axios**: Since your environment automatically installs npm packages, you just need to import it.
2. **Use the Telegram Bot API**: You'll need to use the?**`sendMessage`**?method of the Telegram Bot API to send a message to a chat.

Here's an example code snippet that sends a message to a specified chat ID using a Telegram bot:

```jsx
import axios from 'axios';

export default async function run({execution_id, input, data, store}) {
    // Your Telegram Bot Token
    const botToken = 'YOUR_BOT_TOKEN_HERE';

    // The chat ID you want to send a message to
    const chatId = 'YOUR_CHAT_ID_HERE';

    // The message you want to send
    const message = 'Hello, this is a message from my bot!';

    // Telegram API URL to send messages
    const apiUrl = `https://api.telegram.org/bot${botToken}/sendMessage`;

    try {
        // Making a POST request to the Telegram API to send the message
        const response = await axios.post(apiUrl, {
            chat_id: chatId,
            text: message,
        });

        // Returning the response from the Telegram API
        return {
            success: true,
            response: response.data,
        };
    } catch (error) {
        // Returning the error if the request failed
        return {
            success: false,
            error: error.message,
        };
    }
}
```

Replace?**`'YOUR_BOT_TOKEN_HERE'`**?with your actual Telegram bot token and?**`'YOUR_CHAT_ID_HERE'`**?with the chat ID you want to send a message to.

**Important Notes:**

* Ensure your bot is added to the chat room you want to send a message to.
* The chat ID can be a user ID, group ID, or channel username (prepend with?**`@`**?for channels).
* This function runs asynchronously, leveraging?**`axios`**?for HTTP requests.
* The code handles basic success and error cases, returning the API response or error message.

## 5. Debugging & Error Fixes

If the assistant generates code that doesn't work as expected ? no problem. Just send the **error message or the broken code back to the assistant**, and it will:

* Analyze what went wrong
* Suggest and generate a corrected version
* Explain what was fixed (if needed)

You don't need to debug manually ? just say something like:

> ?This code throws an error: Cannot read property 'xyz' of undefined ? fix it?

Or:

> ?This returns undefined, but I expect the message to be shown ? what's wrong??

The assistant is designed to **iteratively** improve the output, so feel free to go back and forth. It?s part of the workflow.

***

## Tips & Notes

* The assistant understands your context and node configuration.
* You can ask complex multi-step queries (e.g. "get data from webhook, filter it, and send to Telegram").
* If something goes wrong, try rephrasing your request ? the assistant will adapt.
* Responses include explanations ? great for learning and debugging.

# Write JS code on your AI IDE (Cursor, Windsurf, Github Copilot etc.)

You can use your favorite IDE (Cursor, Windsurf, GitHub Copilot, etc.) to write code and paste it into the JS node.

Here are markdown instructions to use in your IDE:

{/* prettier-ignore-start */}

{/* Docusaurus-ignore-start */}

````markdown
# AI Copilot Chat Instructions

Act as AI developer's copilot to assist writing in NodeJS. You are working with an online automation platform that allows users to connect and integrate various web applications. Each workflow is called a "scenario" or "workflow" and each web app used within a scenario is referred to as a "Node". Nodes could be chained with each other and could get data from previous node.

## NodeJS availability and code structure

Users can use a NodeJS node (aka Javascript) where they can write their own code, which can utilize data from other nodes.

Each JavaScript node has the following function:

```javascript
export default async function run({execution_id, input, data}) {
    return {

    }
}
```

"input" argument is unknown.

"run" function always should return object. If you don't need to return something, return empty object `{}`

## NodeJS limitations and specifications:

In javascript Node you cannot use "fetch" lib, use "axios" instead.

You can import any library from npm you need, they will be installed automatically, don't ask user to install them.

Do not use "require", use "import" instead.

## Accessing data from previous nodes:

In javascript you can access data from another nodes from "data" variable provided in "run" function.

For example:

```jsx
data["{{1.result.list}}"]
```

which means [get data from node with id "1" by path "result.list"].

Always wrap every key except first with "`" symbol.

You may be provided with nodes output structs. By these shemas you can build another node data access path. Every "data" argument value is a string.

### Example of nodes output structs:

```json
[{"node_type_name": "HTTP/Actions/Http request", "id": "1", "label": "", "children": [{"property":"ages","type":"array","children":[{"property":"[]","type":"numeric"}]},{"property":"meetings","type":"array","children":[{"property":"[]","type":"object","children":[{"property":"name","type":"string"}]}]},{"property":"meta","type":"object","children":[{"property":"content-type","type":"string"},{"property":"length","type":"numeric"}]},{"property":"names","type":"array","children":[{"property":"[]","type":"string"}]}]}]
```

### Example: user asked you to write code where you need to get meta length from Node with id=1:

By this schema, you can see that node has id=1. After that, find your data path. In this schema it is "meta.length". Result is:

```jsx
data["{{1.`meta`.`length`}}"]
```

### Example: user asked you to write code where you need to get first meeting from node with id=1:

Result is:

```jsx
data["{{1.`meetings`.[0]}}"]
```

### Example: user asked you to write code where you need to get all meetings from node with id=1:

Result is:

```jsx
data["{{1.`meetings`}}"]
```

You must parse "data" value if it has non "string" type in Node output structs. For example:

```jsx
JSON.parse(data["{{1.\`meetings\`}}"])
```

## Custom parameters

All values that user should fill you must describe as custom params block.
Custom params can be described at the top of code as a comment. For example:

```javascript
/** @CustomParams
{
	"custom_param": {
		"type": "string",
		"title": "Custom input param example",
		"description": "Just example field"
	}
}
*/
```

By doing this user will see input field above the code where he can write anything he wants. He can use data from previous steps or from variables and do not change the code.

In your javascript code you can access these fields by `data` argument directly by property name:

```javascript
/** @CustomParams
{
	"custom_param": {
		"type": "string",
		"title": "Custom input param example",
		"description": "Just example field"
	}
}
*/

export default async function run({execution_id, input, data, store}) {
	return {
		user_input: data.custom_param,
	}
}
```

Custom params must be started with `/** @CustomParams` at first line. And must be ended with `*/` at the last line.
Betwen these lines you can put an object where property name is internal var name, that you can access by `data` argument. And value describes type, title and description.

Available custom params type is only string! You must JSON.parse values if user should provide JSON data

## Common instructions

If you wasn't provided with nodes output structs - write code as you think.

Try to explain your code.

If you don't have a user code, ask user to provide it.

If you have to write code, write it only for current NodeJS node.

Act as assistant to write NodeJS code.

You will be provided with user's data that user can see.

User will ask you questions.

You should answer.
````

{/* Docusaurus-ignore-end */}

{/* prettier-ignore-end */}

```
```

# Handling Files

Latenode supports two ways of working with files in scenarios:

* **No-code nodes**: you pass a file reference from one node to another.
* **JavaScript node**: you read/modify/create a file in code and return it back as a file output.

## Passing files between no-code nodes

When a node outputs a file, it usually contains a `file` object with fields like `content` (internal path/reference), `filename`, `extension`, and more.

### Typical mapping in receiving nodes

Most nodes either accept the whole file object or ask for specific fields (for example, **File Path** and **Name**). Use the helper widget to insert the values from previous nodes.

| Receiving node field         | What to map         | Example                        |
| ---------------------------- | ------------------- | ------------------------------ |
| **File Path / File Content** | File reference/path | `{{$2.result.file.content}}`   |
| **Name**                     | File name           | `{{$2.result.file.filename}}`  |
| **Extension** (optional)     | File extension      | `{{$2.result.file.extension}}` |

## Working with files in the JavaScript node

If you need to **read**, **transform**, or **generate** a file in code, you must work with a file path and Node.js `fs`.

### Step 1: Get the temporary file path

Use the templated data accessor to pull the file path from a previous node (example: Node 2).

```js
const contentFilePath = data["{{2.result.file.content}}"];
```

### Step 2: Read/modify the file (Buffer)

Read the file from the path, perform your transformation, and build a new `Buffer` (or write bytes directly).

### Step 3: Write and return the file

Write the output file to the temporary filesystem and return it using the `file()` helper so other nodes can consume it.

  Do not return the raw path from `data[...]` as your final output. Always follow: get path > read > modify > write > return `file(...)`.

## Tip: Ask the AI agent to return a binary file

The AI agent inside the **JavaScript** node can generate code that returns **binary files** (images, PDFs, CSVs, videos, etc.) out of the box. You can explicitly ask it to:

* Read a file from a specific node output (for example, �Node 2�).
* Process it (convert, resize, compress, parse, etc.).
* **Return the result as a file output** using `file()` and a correct `fileType`.

Example prompt you can paste into the AI chat in the JavaScript node:

> Read the file from Node 2 output (`result.file.content`), convert it to PDF, and return it as a binary file output with the correct MIME type.

## Complete example: Read > Modify > Write > Return (CSV)

```js
import fs from 'fs';

export default async function run({ data }) {
  // 1) Get the temporary file path from Node 2 output
  const contentFilePath = data["{{2.result.file.content}}"];

  if (!contentFilePath) {
    throw new Error(
      'File path not found. Check that Node 2 outputs result.file.content and insert it via the helper widget.'
    );
  }

  // 2) Read file as a Buffer
  const contentFileBuffer = fs.readFileSync(contentFilePath);

  // 3) Modify (example: add ',"Processed"' column to each CSV row)
  const csvContent = contentFileBuffer.toString('utf8');
  const rows = csvContent.split('\n');

  const header = rows[0] ?? '';
  const processedRows = [header];

  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    if (!row || row.trim() === '') continue;
    processedRows.push(`${row.trim()},"Processed"`);
  }

  const processedCsvString = processedRows.join('\n');
  const processedFileBuffer = Buffer.from(processedCsvString, 'utf8');

  // 4) Write and return as a file output
  const newFileName = 'processed_data.csv';
  fs.writeFileSync(newFileName, processedFileBuffer);

  return {
    file: file(newFileName),
    fileType: 'text/csv',
  };
}
```

# Iterating

Iterating means processing a collection (an array or object) **one item at a time**: the same steps run for each item. In Latenode this is done with the [**Iterator**](/integrations/core-nodes/iterator) node: you give it data to iterate over and connect nodes that should run inside the loop.

## What is an Iterator

The **Iterator** is a node that processes selected data sequentially, one element at a time. You can pass a JSON array (iteration over array elements) or a JSON object (iteration over key–value pairs).

## Setup

### Data to Iterate field

In the node's single configuration field — **Data to Iterate** — specify the array or object to iterate over. This can come from previous nodes (e.g. `{{node.field}}`) or be a fixed value.

### Top connector (cycle)

Unlike regular nodes, **Iterator** has an extra connector on **top**. This is the cycle output: each iteration goes through it. Connect here the nodes that should run for every element — as many times as there are items in the data.

### Right connector (after all iterations)

The **right** connector runs **only after all iterations are done**. It's optional and is typically used for "when everything is processed" actions — for example, sending a webhook response that data was processed successfully.

  A node connected to the **right** Iterator connector runs once after the loop. Nodes connected to the **top** connector run on every iteration.

## Example

Common pattern: trigger → data → **Iterator** → connect a node (e.g. Set Variables or HTTP Request) to the top connector to process one item; connect **Webhook Response** to the right connector to send the response to the caller after all items are processed.

For more on the node's parameters and examples, see [Iterator](/integrations/core-nodes/iterator).

# Passing Data

To configure each node, you need to fill in its fields. The fields in scenario nodes can be populated with:

* Variables created within the scenario
* Global variables
* Output parameters from other nodes in the scenario

You can manually or automatically fill these node fields.

## Variables

Existing variables are displayed in a helper window for filling in node or route fields. To make a variable appear in the helper window, it must first be created:

* To create a "regular" variable for use in the scenario, add a [SetVariables](../../../integrations/core-nodes/setvariables.mdx) node and run it.
* To create a global variable, add a [SetGlobalVariables](../../../integrations/core-nodes/setglobalvariables.mdx) node (in the current or any other scenario) and run it. Another way to create global variables is to add them via a separate interface.

### Automatic Filling

To automatically fill a field with a variable:

* **(1)** Click on the node or route configuration field.
* **(2)** View the available parameters from previous nodes in the **Variables** window. The **Variables** tab displays both regular variables (added to the scenario using the [SetVariables](../../../integrations/core-nodes/setvariables.mdx) node) and global variables (added to the account using the [SetGlobalVariables](../../../integrations/core-nodes/setglobalvariables.mdx) node or manually).
* **(3)** Select the necessary regular or global variables.

### Manual Filling

To manually fill a node field with variable values, write the variable name in curly braces in the specified format:

* For regular variables, use the format - **`{{_.VariableName}}`**.

***Example:*** Variable "SetVar" - **`{{_.SetVar}}`**

* For global variables, use the format - **`{{%.VariableName}}`**.

***Example:*** Variable "dayTemp" - **`{{%.dayTemp}}` .**

## Node Data

The output of previous nodes is displayed in a helper window for filling in node or route fields.

### Automatic Filling

To automatically input a parameter:

* **(1)** Click on the node or route configuration field.
* **(2)** View the available parameters from previous nodes in the **Data** window.
* **(3)** Select the necessary parameters or entire nodes.

### Manual Filling

To manually fill a field with existing data, write the parameter name in curly braces in the specified format:

* **All data** from a node in the format - **`{{$NodeNumber}}`**.

***Example:*** Node 2 - **`{{$2}}`**

* **Specific parameter** in the format - **`{{$NodeNumber.ParameterPath.ParameterName}}`**.

***Example:*** Parameter “name” in node 2 - **`{{$2.name}}`**

## Variable templates

Substitutions in node and route fields must follow the platform format. Valid formats:

* **Node data** — **`{{$NodeNumber}}`** (all node data) or **`{{$NodeNumber.parameter}}`** (specific parameter). The node number is required: the platform needs to know which node to take data from. Example: field `value` from node 5 — **`{{$5.value}}`**, not just `{{value}}`.
* **Scenario variable** — **`{{_.VariableName}}`**
* **Global variable** — **`{{%.VariableName}}`**
* **Built-in operators** (e.g. **`{{timestamp}}`**) — no node number needed.

Common mistake: writing **`{{value}}`** or **`{{name}}`** without a node number. The platform then cannot determine which node the data comes from. Always specify the node: **`{{$5.value}}`**, **`{{$2.name}}`**, etc.

### How templates appear in fields

In input fields, substitutions are shown in different ways depending on whether the platform recognizes them and whether data exists at the given path.

**1. Unrecognized template (error)** — the substitution appears **hollow** with a **red outline** and a warning icon. The message **Unrecognized template** appears above the field. The expression does not match the platform format (e.g. `{{value}}` without a node number). Fix the syntax using the rules above.

**2. Syntax correct, path potentially possible** — the substitution appears **hollow** without a red outline (e.g. with a neutral or brown border). The syntax is valid, but at the time of typing there is no node in the scenario that provides data at this path. If a node with that data structure is added later, the substitution will work correctly.

**3. Fully recognized substitution** — the substitution looks **filled** with the color of the source node (e.g. brown fill for SetVariables). This means that when the substitution was added, the scenario already had a node with that number and data structure; the value actually exists and will be substituted at runtime.

### Unrecognized template

If a substitution is **red**, hollow, and the message **Unrecognized template** is shown, the expression does not match the platform format. Check: is the node number specified for node data (**`{{$number.field}}`**), are variable names correct (**`{{_.Name}}`**, **`{{%.Name}}`**) or operator names valid.

## JavaScript and Headless Browser

In both the **JavaScript** and **Headless Browser** nodes, you can select parameters from previous nodes or variables. For example, to easily create a constant in the **JavaScript** node:

* Write the expression to add the constant, such as `const =`.
* Select the necessary parameter from previous nodes.

  When adding data from other nodes, part of the expression might be wrapped in backticks, like this: `data["{{1.headers.Content-Type}}"]`, even though another node returned the property without them. You do not need to remove the backticks, as they will be ignored during code processing. Manually removing them may cause the code to fail.

## Arrays

Sometimes, the output parameters of a node may be arrays containing a set of elements. You can use the desired array element or the entire array in other nodes.

### Auto-Filling

For example, let's create a scenario where the trigger node activates when a new row is added to a Google Sheet and provides an array of cell values from the new row as output parameters. We'll specify the entire array and individual elements as variables. To create this scenario, add two nodes:

* **(1)** **New Row Added (Shared Drive, Instant)** - to trigger the scenario and provide data about the added row. Authorization and selection of the required table and sheet are necessary for this node.

* **(2)** **SetVariables** - to record variables Val1, Val2, and Val3.

Run the scenario once by clicking the **Run Once** button and add a row to the specified table. The output of the **New Row Added (Shared Drive, Instant)** node will include an array of cell values from the added row:

Set the variable values:

* Val1 - the entire array of values **`{{$1.data.newRow}}`**. Click on **`newRow[ ]`**.
* Val2 - the first element of the array **`{{$1.data.newRow.[`0`]}}`**. Click on **`[0]`**.
* Val3 - the second element of the array **`{{$1.data.newRow.[`1`]}}`**. Click on **`[0]`** and **manually replace 0 with 1.**

Run the **SetVariables** node once and check the recorded variable values. You can then use each of these variables to fill in the fields of other nodes in the Helper Widget.

## Using the “Select / Map” Toggle in the Settings

Some parameters, such as a dropdown list or toggle, by default do not have an input field that allows passing data from variables or previous nodes.

For such parameters, there is a special toggle:

When the toggle is set to **“Select”**, the parameter operates in **manual (static)** mode. In the case of a dropdown list, the item is selected manually and saved in the node settings.

For example, in Google Calendar, you can select rules for sending notifications about a new event:

This value will always stay the same unless changed manually. It cannot be influenced by other nodes or incoming data.

> Use Select when the value should always remain fixed during scenario execution.

***

In cases where the value needs to be set dynamically, switch the toggle to **“Map”** mode. This allows passing data from previous nodes:

```
$5.query.send_updates_notification_rule
```

The value will now update automatically on each run, based on scenario input — for example, from a webhook, user form, or database.

> Use Map when the value should react to dynamic input from other nodes.

***

### Why Map Mode Is More Powerful

Unlike **Select**, which is limited to predefined values, **Map** mode enables:

* ✅ **Boolean values** like `true` / `false`
* 🔧 **Dynamic formatting using [Operators](https://docs.latenode.com/docs/operators)**

**Example:**

```
{{ if(7.is_active = true; "Active"; "Inactive") }}
```

📢 **Explanation:**

* `7.is_active` — a variable from node 7, for example a boolean flag
* `= true` — condition that checks if the flag is active
* Returns `"Active"` if true, `"Inactive"` otherwise

  This logic is only available in Map mode.
  The **Select** mode does not support variables or expressions.

# Add a Node

If your scenario is new and doesn't contain any nodes yet, click **Add Node...** in the center of the canvas to add the first one.

If there are already nodes in the scenario, you can add a new node by:

* Clicking the **Add Node** button in the bottom part of the interface;

* Clicking on the right route point of an already added node.

After clicking **Add Node**, select the desired node from the list in the **Choose an app** window.

## Favorite nodes

To pin frequently used nodes to the top of the **Choose an app** window:

1. Mark the desired node with a "star";

2. Check for the presence of the node in the **Choose an app** window under the **Favorites** section.

If quick access to the node is no longer needed, you can remove the "star" by clicking on it again.

## Search by name

Use the search field at the top of the **Choose an app** window to find a node by name.

# Configure & Run a Node

## Node Configuration and Execution

After adding a node, you can modify the node's name (**1**) in the settings window and save the changes by clicking the **Save** button (**2**).

When configuring any node, you should:

1. Fill in the mandatory fields (**1**).

  The set of fields for configuration is unique to each node.

2. Save the settings and changes by clicking the **Save** button in the node's configuration window.

Each added and configured node is accessible for viewing on the scenario page and displays:

* (**1**) **Node Number** - a unique identifier within the scenario for the node;
* (**2**) **Node Type** - the system name of the node;
* (**3**) **Node Name** - the name entered by the user;
* (**4**) **Route Points** used to create new nodes or routes between nodes.

By right-clicking on a node, a node menu opens with the following buttons:

* (**1**) **Settings** - access the node's settings;
* (**2**) **Run Once** - manually run the node once. Running a node separately allows you to check its functionality without running the entire scenario;
* (**3**) **Copy** - copy the node or selected group of nodes. You can paste:
  * into external tools, such as Notepad;
  * into the interface for creating/editing an existing scenario.
* (**4**) **Ignore Errors** - error handling feature;
* (**5**) **Delete** - delete the node.

# Copy Scenarios & Nodes

## Copying Scenarios and Nodes

Existing scenarios and nodes can be copied:

* within one account, either within the same scenario or between different scenarios;
* between different accounts.

The result of copying nodes within one account is identical, whether nodes are copied within the same scenario or across multiple scenarios.

## Steps for copying a scenario or nodes

You can copy a single node or multiple nodes in two ways.

### Option 1: Copy from the node context menu

To copy a node or multiple nodes:

* Right-click on the node;
* Click the **Copy** button;
* Right-click on any empty space on the page of the current scenario or another scenario;
* Click the **Paste** button.

### Option 2: Select nodes, then paste

* Press **Shift**;
* Click and drag the mouse pointer across the screen to select a node or multiple nodes;
* Right-click on any empty space on the page of the current scenario or another scenario;
* Click the **Paste** button.

To copy a scenario, you need to:

* Go to the **Scenarios** page;
* Open the menu for the row of the desired scenario;
* Click the **Copy** button;
* Right-click on any empty space on the page of another scenario;
* Click the **Paste** button.

### Alternative: copy all nodes from the canvas

* Press **Shift**;
* While holding the left mouse button, select all nodes in the scenario;
* Right-click on any empty space on the page of another scenario;
* Click the **Paste** button.

## Rules for Copying Scenarios and Nodes

When copying an entire scenario or one/multiple nodes, the duplicated nodes retain their routes and settings.

The numbers of duplicated nodes depend on whether the copying and pasting occurred within the same scenario:

* If nodes are copied and pasted within the current scenario, node numbers are updated, and the settings of these nodes are automatically adjusted to the new numbers.
* If nodes are copied and pasted into another scenario, node numbers remain the same.

Authorizations of duplicated nodes are preserved if copying occurs within the same account and are **not** preserved if copying and pasting occurs between different accounts.

## Examples of Copying Scenarios/Nodes

**Example 1:**

* A scenario is created where node 2, **Webhook Response**, displays the value from node 1, **Trigger on Webhook**, in the **Body** field;

* Both nodes of the scenario are copied and pasted into the same scenario;
* Node 4, **Webhook Response**, displays the value from node 3, **Trigger on Webhook**, in the **Body** field. This means that node settings were preserved and updated according to the new node numbers.

  When copying, the **Trigger on Webhook** URL of the node is duplicated without changes. You need to manually adjust the address to ensure requests are sent to the correct **Trigger on Webhook**.

When attempting to save a scenario with a non-unique **Trigger on Webhook** node address, a corresponding notification is displayed.

**Example 2:**

* In account 1, a scenario with an **Upload File** node has been created, with an authorization to Google Drive configured;

* In account 2, an empty scenario has been created;
* All nodes from the scenario in account 1 have been copied and pasted into the empty scenario of account 2;
* In the scenario of account 2, an error is displayed in the **Upload File** node, and setting up a new authorization is required.

# AI tools

AI tools help you delegate parts of scenario configuration and decision-making to AI systems.

  You can use our GPT Assistant for help with **Latenode operators**:

  👉 [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

### Let AI Decide (one-click placeholders)

In most fields where AI Agent or MCP can provide values, you will see a **Let AI Decide** button.
It inserts the correct operator (`fromAIAgent` or `fromMCP`) into the field and auto-generates a suitable parameter name/description.

## fromAIAgent()

Use `fromAIAgent()` inside any editable field of a node that is **connected to an AI Agent**.
This marks the field as an argument the agent must provide during execution. The agent sees these placeholders as tool parameters and fills them automatically.

For full context, see: [AI Agent Node](../../ai-agents/ai-agent-node.mdx).

**Format:**

```plain
{{fromAIAgent("parameter_name"; "description")}}
```

**Example:**

```plain
{{fromAIAgent("Email Body"; "Include an email body as either plain text or HTML. If HTML, make sure to set the \"Body Type\" prop to html")}}
```

## fromMCP

`fromMCP` is used in MCP workflows to mark inputs and fields that an **MCP client** should decide and fill.
In many places you can also use **Let AI Decide** to insert the correct placeholder automatically.

For setup details, see: [MCP Nodes](../../mcp/mcp_nodes.mdx).

**MCP Trigger input parameters**

In **MCP Trigger → Tool configuration → Input parameters**, add parameters and set:

* **Key**: parameter name (e.g., `email`, `message`)
* **Type**: `fromMCP`
* **Description**: what the AI client should pass

**MCP Response**

By default, MCP returns the output of the last node. **MCP Response** lets you return exactly what the client needs — and you can use **Let AI Decide** to make the response MCP-fillable.

{/* Optional screenshot: MCP Response with Let AI Decide / fromMCP */}

## askAI()

The `askAI()` operator sends a request to the built-in AI and returns a text response.

In addition to text, the request can use existing variables or global variables or output parameters of previous nodes, enclosed in symbols according to the pattern **`"+Variable/Data+"`**.

Below are some examples of using `askAI()`.

  When using artificial intelligence (AI), follow these precautions. Provide clear and understandable instructions to AI to avoid misunderstandings and incorrect results. Verify the accuracy of the AI's responses, especially if they have serious consequences or are critical for decision-making. Remember that AI responses can vary based on input data, model training, and other factors. Be prepared for different outcomes.

### Text Generation

A user request can be a text prompt, such as asking to generate an invitation for an event as the value of the variable **Val**:

1. Add the **Trigger on Run once** and **setvariables** nodes to the scenario.

2. Add the variable **Val** and set its value to **`{{askAI("Generate a short invitation text for an event")}}`**.

3. Run the scenario once and review the node execution results to verify the presence of the new variable.

### User Feedback Monitoring

A request can involve identifying the tone or sentiment of incoming text. The text can be the output parameter of a previous node, such as an email or Telegram chat message. For simplicity, generate the text directly within the scenario by adding the following nodes:

1. **Trigger on Run once** node to trigger the scenario with the **Run once** button.

2. **setvariables** node to generate the **Text** variable, containing the product review text.

3. **Webhook response** node to return a response upon successful execution of the scenario. In the **Body** field of the **Webhook response** node, add the AI operator with a request using the variable from the **setvariables** node: **`{{askAI("Determine if the text \"" + _.Text + "\" is a negative review")}}`**

The result of this scenario is an AI response:

***Yes, the text "The packaging is damaged and the courier was late" can be considered a negative review.***

### Text Classification

A request can involve determining if the incoming text is a question. Using the AI operator in routes allows the scenario to follow different branches based on the AI's response.

  Since the condition for route execution is a boolean **TRUE** in the **Condition** field, you must configure this field correctly. For example, ask the AI to return "true" or "false" and compare the result to "true." The equality true=true will be **TRUE**, triggering the route.

For simplicity, generate the text directly within the scenario by adding the following nodes:

1. **Trigger on Run once** node to trigger the scenario with the **Run once** button.

2. **setvariables** node to generate the **Value** variable containing the text for classification.

3. **Question** route with the condition **`{{askAI("The text contains \"" + $2.Value + "\" is there a question? If so, return one word \"true\", otherwise return one word \"false\"") = "true"}}`**.

4. **Webhook response** node for the **Question** route with the response *The text contains a question* upon scenario execution.

5. **Not a question** route with the condition **`{{askAI("The text contains \"" + $2.Value + "\" is there a question? If not, return one word \"true\", otherwise return one word \"false\"") = "true"}}`**.

6. **Webhook response** node for the **Not a question** route with the response *The text does not contain a question* upon scenario execution.

The result of the scenario depends on the text in the **Value** variable:

* If the variable contains a question, such as *What is the deadline for completing the task?*, the scenario's result is *The text contains a question*.

* If the variable contains a statement, such as *Documentation is an important part of learning*, the scenario's result is *The text does not contain a question*.

# Array Functions

You can use our GPT Assistant for help with **Latenode operators**:

  ?? [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group provide the ability to perform operations on arrays and array elements.

  Elements of the array can be strings, numbers, or boolean values.

## Operators

### `add`

This operator adds a value to the specified variable to create an array.

* **Result of the expression:** Value in the array.

### `join`

It concatenates all the array elements into a string, adding the specified delimiter between each array element.

* **Execution Result:** text with the specified delimiter.
* **Example:** If `_.Array = [1,2,3,4,5]`, then the result is `"1.2.3.4.5"`.

### `slice`

Returns a modified array containing the specified elements from the provided array.

  The specified numbers are the ordinal numbers of the array elements. In the example below, it returns elements from the zeroth (exclusive) to the first (inclusive) element. The ending number may be omitted, in which case, it will return all elements of the array after the initial number.

* **Execution Result:** an array of values.
* **Example:** If `1.Body = [\{"Value": "Hi"\}, \{"Value": "Latenode"\}]`, then the result is `[\{"Value": "Hi"\}]`.

### `merge`

Merges two or more passed arrays into one array.

* **Execution Result:** an array of values.
* **Example:** If `1.Body[0] = [\{"Value": 5\}, \{"Value": 10\}]` and `1.Body[1] = [\{"Value": 15\}, \{"Value": 20\}]`, then the result is `[\{"Value": 5\}, \{"Value": 10\}, \{"Value": 15\}, \{"Value": 20\}]`.

### `map`

Returns an array containing the desired values of the given complex array. Can be used for filtering values.

* **Execution Result:** an array of found values.
* **Example:**

Input data:

```json
[
	{
		"Name": "Kate",
		"Address": "Tokyo",
		"Age": 25
	},
	{
		"Name": "Anna",
		"Address": "Seoul",
		"Age": 35
	},
	{
		"Name": "Lisa",
		"Address": "Beijing",
		"Age": 45
	}
]
```

Result:

```json
[
	25,
	35,
	45
]
```

### `sort`

Returns an array containing values of the given array sorted in the desired order. Sorting options available:

* **asc** - in ascending order;
* **desc** - in descending order;
* **asc ci** - in ascending order, case-insensitive;
* **desc ci** - in descending order, case-insensitive.

* **Execution result:** an array of sorted values.
* **Example:** If `1.Body = [\{ "Value": 5\}, \{"Value": 10\}, \{ "Value": 15\}, \{"Value": 20\}]`, then the result is `[\{ "Value": 20\}, \{"Value": 15\}, \{ "Value": 10\}, \{"Value": 5\}]`.

### `deduplicate`

Removes duplicate values from the given array and returns an array with unique values.

* **Execution result:** an array of unique values.

* **Example:**

Input data:

```json
[
	{
		"Name": "Kate",
		"Age": 45
	},
	{
		"Name": "Anna",
		"Age": 45
	},
	{
		"Name": "Lisa",
		"Age": 45
	},
	{
		"Name": "Lisa",
		"Age": 45
	},
	{
		"Name": "Anna",
		"Age": 25
	}
]
```

Result:

```json
[
	{
		"Age": 45,
		"Name": "Kate"
	},
	{
		"Age": 45,
		"Name": "Anna"
	},
	{
		"Age": 45,
		"Name": "Lisa"
	},
	{
		"Age": 25,
		"Name": "Anna"
	}
]
```

### `distinct`

Removes duplicates from the given array and returns an array with unique values. All duplicates are removed based on the specified key, except for the first found value.

* **Execution result:** an array of unique values.
* **Example 1:**

Input data:

```json
[
	{
		"Name": "Kate",
		"Age": 45
	},
	{
		"Name": "Anna",
		"Age": 45
	},
	{
		"Name": "Lisa",
		"Age": 45
	},
	{
		"Name": "Lisa",
		"Age": 45
	},
	{
		"Name": "Anna",
		"Age": 25
	}
]
```

Result:

```json
[
	{
		"Age": 45,
		"Name": "Kate"
	},
	{
		"Age": 25,
		"Name": "Anna"
	}
]
```

* **Example 2:**

Input data:

```json
[
	{
		"Name": "Kate",
		"Age": 45
	},
	{
		"Name": "Anna",
		"Age": 45
	},
	{
		"Name": "Lisa",
		"Age": 45
	},
	{
		"Name": "Lisa",
		"Age": 45
	},
	{
		"Name": "Anna",
		"Age": 25
	}
]
```

Result:

```json
[
	{
		"Age": 45,
		"Name": "Kate"
	},
	{
		"Age": 45,
		"Name": "Anna"
	},
	{
		"Age": 45,
		"Name": "Lisa"
	}
]
```

# Comparisons

You can use our GPT Assistant for help with **Latenode operators**:

  👉 [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group compare operands with each other. The operands can be:

* Numerical values - their mathematical relationship is determined during comparison;
* String values - comparison is done character by character. If the first characters of two strings are equal, the second characters are compared, and so on. Comparison determines the lexicographic order of characters, i.e., their order in the alphabet.

  An uppercase letter is considered different from its lowercase counterpart. When comparing, a lowercase letter is considered greater than the corresponding uppercase letter. The presence of a character is considered a greater value than the absence of a character.

## Result

The result of the expression is a Boolean value, either TRUE or FALSE.

## Examples

### Operator `<` (Less than)

* If the operand types are **numbers**, and for example, `3.ValueSV1 = 45` and `3.ValueSV2 = 100`, then it's **TRUE**.
* If the operand types are **numbers**, and for example, `3.ValueSV1 = 125` and `3.ValueSV2 = 125`, then it's **FALSE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = AA` and `3.ValueSV2 = AB`, then it's **TRUE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = AC` and `3.ValueSV2 = AB`, then it's **FALSE**.

### Operator `≤` (Less than or equal to)

* If the operand types are **numbers**, and for example, `3.ValueSV1 = 5` and `3.ValueSV2 = 5`, then it's **TRUE**.
* If the operand types are **numbers**, and for example, `3.ValueSV1 = 5` and `3.ValueSV2 = 1`, then it's **FALSE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = AB` and `3.ValueSV2 = AB`, then it's **TRUE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = AB` and `3.ValueSV2 = AA`, then it's **FALSE**.

### Operator `=` (Equal)

* If the operand types are **numbers**, and for example, `3.ValueSV1 = 15` and `3.ValueSV2 = 15`, then it's **TRUE**.
* If the operand types are **numbers**, and for example, `3.ValueSV1 = 15` and `3.ValueSV2 = 20`, then it's **FALSE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = ABC` and `3.ValueSV2 = ABC`, then it's **TRUE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = ABC` and `3.ValueSV2 = ABCD`, then it's **FALSE**.

### Operator `≠` (Not equal)

* If the operand types are **numbers**, and for example, `3.ValueSV1 = 50` and `3.ValueSV2 = 51`, then it's **TRUE**.
* If the operand types are **numbers**, and for example, `3.ValueSV1 = 50` and `3.ValueSV2 = 50`, then it's **FALSE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = AA` and `3.ValueSV2 = B`, then it's **TRUE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = BB` and `3.ValueSV2 = BB`, then it's **FALSE**.

### Operator `≥` (Greater than or equal to)

* If the operand types are **numbers**, and for example, `3.ValueSV1 = 125` and `3.ValueSV2 = 100`, then it's **TRUE**.
* If the operand types are **numbers**, and for example, `3.ValueSV1 = 45` and `3.ValueSV2 = 100`, then it's **FALSE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = BC` and `3.ValueSV2 = BC`, then it's **TRUE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = BA` and `3.ValueSV2 = BB`, then it's **FALSE**.

### Operator `>` (Greater than)

* If the operand types are **numbers**, and for example, `3.ValueSV1 = 125` and `3.ValueSV2 = 100`, then it's **TRUE**.
* If the operand types are **numbers**, and for example, `3.ValueSV1 = 45` and `3.ValueSV2 = 100`, then it's **FALSE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = BBA` and `3.ValueSV2 = BB`, then it's **TRUE**.
* If the operand types are **strings**, and for example, `3.ValueSV1 = BB` and `3.ValueSV2 = BC`, then it's **FALSE**.

### Operator `AND`

The AND operator evaluates all of its operands. If the result of the evaluation is FALSE for at least one operand, the expression's result is also FALSE.

* If `1.body.ValueWH = 71` AND `3.ValueSV = 100`, then **TRUE**;
* If `1.body.ValueWH = 70` AND `3.ValueSV = 100`, then **FALSE**.

### Operator `OR`

The OR operator evaluates all of its operands. If the result of the evaluation is TRUE for at least one operand, the expression's result is also TRUE.

* If `1.body.ValueWH = 70` OR `3.ValueSV = 100`, then **TRUE**;
* If `1.body.ValueWH = 70` OR `3.ValueSV = 99`, then **FALSE**.

# Functions (date, time)

You can use our GPT Assistant for help with **Latenode operators**:

  ?? [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group ensure the execution of logical operations with operands of the date/time type. The result of the operations is the date.

## Result

## addMinutes

This operator generates a new date value:

* adding the specified number of minutes to the current date value, if a positive value is specified;\
  **Example:** If 3.ValueSV = 2023-01-01T00:**00**:00Z, then 2023-01-01T00:0**5**:00Z.

* subtracting the specified number of minutes from the current date value, if a negative value is specified.\
  **Example:** If 3.ValueSV = 2023-01-01T00:**25**:00Z, then 2023-01-01T00:**20**:00Z.

## addHours

This operator generates a new date value:

* adding the specified number of hours to the current date value, if a positive value is specified;\
  **Example:** If 3.ValueSV = 2023-01-01T**00**:00:00Z, then 2023-01-01T**10**:00:00Z.

* subtracting the specified number of hours from the current date value, if a negative value is specified.\
  **Example:** If 3.ValueSV = 2023-01-01T**12**:00:00Z, then 2023-01-01T**04**:00:00Z.

## addDays

This operator generates a new date value:

* adding the specified number of days to the current date value, if a positive value is specified;\
  **Example:** If 3.ValueSV = 2023-01-**01**T00:00:00Z, then 2023-01-**02**T00:00:00Z.

* subtracting the specified number of days from the current date value, if a negative value is specified.\
  **Example:** If 3.ValueSV = **2023-01-01**T00:00:00Z, then **2022-12-29**T00:00:00Z.

## addMonths

This operator generates a new date value:

* adding the specified number of months to the current date value, if a positive value is specified.

**Example:** If 3.ValueSV = 2023-01-01T00:00:00Z, then 2023-**05**-01T00:00:00Z.

* subtracting the specified number of months from the current date value, if a negative value is specified.\
  **Example:** If 3.ValueSV = **2023-01-01**T00:00:00Z, then **2021-12-01**T00:00:00Z.

## setMinute

This operator generates a new date value by replacing the minutes of the current date with a specified value.

* **Example:** If 3.ValueSV = 2023-01-31T11:11:00Z, then 2023-01-31T11:**05**:00Z.

## setHour

This operator generates a new date value by replacing the hours of the current date with a specified value.

* **Example:** If 3.ValueSV = 2023-01-31T11:11:00Z, then 2023-01-31T**05**:11:00Z.

## setDay

This operator generates a new date value by replacing the day of the current date with the specified value. The new day value can be either a number or the name of the day in Latin.

  If the specified value is in the range from 1 to 7, the resulting date will fall within the current week (from Sunday to Saturday), and the new day will correspond to its ordinal number. If the specified value is outside the range from 1 to 7, the resulting date will belong to the previous or next week.

* **Example:** If 3.ValueSV = 2023-09-03T00:00:00Z, then 2023-09-**10**T00:00:00Z.

* **Example:** If 3.ValueSV = 2023-09-03T00:00:00Z, then 2023-09-04T00:00:00Z.

## formatDate

This operator returns the date in the requested format and in the specified time zone if provided.

  You can find the list of time zones [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).

* **Example:** If 3.ValueSV = 2023-09-03T00:00:00Z, then 03.09.2023 03:00

## parseDate

This operator converts a string into a date in the requested format.

* **Example:** If 3.ValueSV = 2023-09-03, then 2023-09-03T00:00:00Z.

## Combination of parseDate and formatDate

In cases where the initial date value is provided as a string, the combination of parseDate and formatDate can be used. This allows you to first convert the string into a date value and then format it into the desired format.

**Example:** If 3.ValueSV = "2030-03-14 08:45:12" (string), to convert it into the format DD.MM.YYYY HH:mm:ss, use the following construction:

Result: 14.03.2030 08:45:12.

**Tip:**

Use this combination if:

* The initial date value is provided as a string.
* You need to convert the string into a date value and format it into the required format.

# Functions 2

You can use our GPT Assistant for help with **Latenode operators**:

  ?? [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group ensure the execution of logical operations with operands and output the result. The outcome of these operations varies.

## Result

## encode URL

This operator ñonverts the text part of the string to an encoded URL.

* **Result of the expression:** URL.
* **Example:** If 3.ValueSV = '??????', then '%CE%94%CE%BF%CE%BA%CE%B9%CE%BC%CE%AE'.

## decode URL

This operator decodes a URL into the original text string.

* **Result of the expression:** Text.
* **Example:** If 3.ValueSV = '%CE%94%CE%BF%CE%BA%CE%B9%CE%BC%CE%AE', then '??????'.

## escape markdown

This operator escapes special characters in a string, such as the asterisk "\*", by adding a backslash before the character.

* **Result of the expression:** Text with escaping.
* **Example:** If 3.ValueSV = 'Latenode\*', then 'Latenode\*'.

## split

This operator splits a string into an array of substrings using a chosen delimiter.

  This function trims substrings (removes spaces from both ends of the substring), and if the trimmed substring becomes an empty string, it is excluded from the array by default.

* **Result of the expression:** Array of substrings.
* **Example:** If 3.ValueSV = 'Latenode.No', then \[ "Latenode", "No" ]

## md5

This operator converts a string or number into an encoded representation using the md5 algorithm.

* **Result of the expression:** Value in md5 encoding.
* **Example:** If 3.ValueSV = 'Latenode', then 'cda182c15952870f090372f4811abe7b'.

## sha1

This operator converts a string or number into an encoded representation using the sha1 algorithm.

* **Result of the expression:** Value in sha1 encoding.
* **Example:** If 3.ValueSV = 'Latenode', then '16fc251ab241e924273ad70315fc5887d641140e'.

## sha256

This operator converts a string or number into an encoded representation using the sha256 algorithm.

* **Result of the expression:** Value in sha256 encoding.
* **Example:** If 3.ValueSV = 'Latenode', then 'a10967ea390e513139a6a7e56dc0f0dc32dd50a10d677a3ac622adff351c9781'.

## sha512

This operator converts a string or number into an encoded representation using the sha512 algorithm.

* **Result of the expression:** Value in sha512 encoding.
* **Example:** If 3.ValueSV = 'Latenode', then '119c2aaa3245368e2d18d939702c270cb7beaa4627b97cd48a54661b6213a43238215e74b8cb445efb671324d371b479f50753082cd7a30d7e9d6706eca245b7'.

## base64

This operator converts a string or number into an encoded representation using the base64 algorithm.

* **Result of the expression:** Value in base64 encoding.
* **Example:** If 3.ValueSV = 'Latenode', then 'TGF0ZW5vZGU='.

# Functions

You can use our GPT Assistant for help with **Latenode operators**:

  👉 [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group ensure the execution of logical operations with operands and output the result. The outcome of these operations varies.

## Result

## If

It outputs a specified value when conditions are met or a different value if the conditions are not met.

* **Result of the expression:** Specified value.
* **Example:** If 3.ValueSV = 10, then true. If 3.ValueSV = 11, then false.

## ()

This operator provides logical and mathematical isolation for any expressions.

* **Result of the expression:** -.

## not

This operator provides logical negation of specified/received boolean values.

* **Result of the expression:** Negation of the value.
* **Example:** If 3.ValueSV is TRUE, then FALSE.

## if empty

It outputs a specified value if the operand is absent (null), and the value of the operand if it is present.

* **Result of the expression:** The value.
* **Example:** If 3.ValueSV is absent (null), then 5. If 3.ValueSV = 50, then 50.

## empty

This operator checks for the absence of values in the operand.

* **Result of the expression:** TRUE/FALSE.
* **Example:** If 3.ValueSV is absent (null), then TRUE. If 3.ValueSV = "May", then FALSE.

## contains

This operator checks for the presence of selected characters in a string, number, or array (including an array of boolean values), regardless of their location.

* **Result of the expression:** TRUE/FALSE.
* **Example:** If 3.ValueSV = "Hello Latenode", then TRUE. If 3.ValueSV = "Hi Latenode", then FALSE.

## starts with

This operator checks for the presence of selected characters at the beginning of a string or number.

* **Result of the expression:** TRUE/FALSE.
* **Example:** If 3.ValueSV = "June", then TRUE. If 3.ValueSV = "May", then FALSE. If 3.ValueSV = "1000", then FALSE.

## ends with

This operator checks for the presence of selected characters at the end of a string or number.

* **Result of the expression:** TRUE/FALSE.
* **Example:** If 3.ValueSV = "June", then TRUE. If 3.ValueSV = "May", then FALSE. If 3.ValueSV = "1000", then FALSE.

## matches pattern

This operator checks for a match between the operand and a regular expression.

* **Result of the expression:** TRUE/FALSE.
* **Example:** If 3.ValueSV = "Abc", then TRUE. If 3.ValueSV = 2000, then FALSE.

## to lower

This operator converts a string to lowercase.

* **Result of the expression:** Lowercase text.
* **Example:** If 3.ValueSV = 'TEST', then test.

## to upper

This operator converts a string to uppercase.

* **Result of the expression:** Uppercase text.
* **Example:** If 3.ValueSV = 'test', then TEST.

## length

This operator outputs the number of characters in a string or the number of values in an array.

* **Result of the expression:** A number.
* **Example:** If 3.ValueSV = 'test', then 4.

## get

This operator outputs a JSON parameter or an array element.

* **Result of the expression:** Parameter.
* **Example:** The value of the parameter ValueWH1 from the provided JSON. For example, if ValueWH1 = 15, then 15.

* **Example:** The value of the element in the provided array ValueWH with index 1. For instance, if ValueWH1 = 15, then 15.

## switch

This operator checks if the expression matches the selected operand and outputs a value when a match is found. The operand can be a boolean value, a string, or a number.

  The function operator returns the result corresponding to the first matching value.

* **Result of the expression:** Value.
* **Example:** If 3.ValueSV = 'A', then 1. If 3.ValueSV = 'Abc1000', then 2.

## replace

This operator replaces selected values in a string or number with specified values.

* **Result of the expression:** Text or number with character replacement.
* **Example:** If 3.ValueSV = 'Hi Latenode', then 'Test Latenode'.

## trim

This operator removes spaces at the beginning and end of a string.

* **Result of the expression:** Text without spaces.
* **Example:** If 3.ValueSV = ' Hi Latenode ', then 'Hi Latenode'.

## substring

This operator outputs a portion of a string or number from a selected starting position not inclusive to a chosen ending position, inclusive.

* **Result of the expression:** A portion of text.
* **Example:** If 3.ValueSV = 'Latenode', then 'a'.

## indexOf

This operator provides the position of the first occurrence of a search value in a string or number.

  This operator returns "-1" if the search value is not found.

* **Result of the expression:** A portion of text.
* **Example:** If 3.ValueSV = 'Latenode', then 4.

# Key Fields

You can use our GPT Assistant for help with **Latenode operators**:

  ?? [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group ensure the presence of certain values in a field, variable, or expression.

## Result

## true

The result of the execution is the presence of a boolean value **TRUE**.

## false

The result of the execution is the presence of a boolean value **FALSE**.

## null

The result of the execution is the presence of **null**.

## space

The result of the execution is the presence of a **space**.

* **Example:** If 3.ValueSV = "Hello" and 3.ValueSV = "Latenode", then "Hello Latenode".

# Mathematical

You can use our GPT Assistant for help with **Latenode operators**:

  👉 [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group ensure the execution of mathematical operations between operands and output the result. The result of performing the same operation may vary depending on the types of operands.

## Result

## +

The result of the operation can be addition of numbers, concatenation of multiple strings, or concatenation of a string and a number.

* If the operand types are **numbers**, and for example, **3.ValueSV1 = 5** and **3.ValueSV2 = 10**, then **15**;
* If the operand types are **strings**, and for example, **3.ValueSV1 = Test** and **3.ValueSV2 = Test**, then **TestTest;**
* If one of the operands is a **string** and the other is a **number**, and for example, **3.ValueSV1 = Test** and **3.ValueSV2 = 15**, then **Test15.**

## -

The result of the operation is the difference between numbers.

  The result of the operation can be the conversion of a positive number into a negative one if there is only one operand, and the operator is placed before it.

* If the operand types are **numbers**, and for example, **3.ValueSV1 = 20** and **3.ValueSV2 = 3**, then the result is **17.**

## /

The result of the operation is the division of numbers.

* If the operand types are **numbers**, and for example, **3.ValueSV1 = 20** and **3.ValueSV2 = 2**, then the result is **10.**

## \*

The result of the operation is the multiplication of the numbers by each other.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 10** and **3.ValueSV2 = 3**, then the result is **30.**

## mod

The result of the operation is obtaining the remainder from dividing the numbers.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 5** and **3.ValueSV2 = 2**, then the result is **1.**

## Average

The result of the operation is the average value of numerical values in a specific array or the average value of numerical values entered individually.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 5** and **3.ValueSV2 = 10**, then the result is **7,5;**

* If the operand type is an **array**, and, for example, **3.ValueSV1 = \[5, 10]**, then the result is **7,5.**

## Сeil

The result of the operation is the smallest integer greater than or equal to the specified number.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 3,7**, then the result is **4.**

## Floor

The result of the operation is the largest integer less than or equal to the specified number.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 3,7**, then the result is **3.**

## Max

The result of the operation is the largest number in the specified array or the largest number among individually entered numbers.

  The number of numerical operands is not limited and can be any.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 15 and 3.ValueSV2 = 20**, then the result is **20;**

* If the operand type is an **array**, and, for example, **3.ValueSV1 = \[15, 20]**, then the result is **20.**

## Min

The result of the operation is the smallest number in the specified array or the smallest number among individually entered numbers.

  The number of numerical operands is not limited and can be any.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 15** and **3.ValueSV2 = 20**, then the result is **15;**

* If the operand type is an **array**, and, for example, **3.ValueSV1 = \[15, 20]**, then the result is **15.**

## Round

The result of the operation is rounding the number to the nearest integer.

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 9.5**, then **10**.

## Sum

The result of the operation is the sum of values in the specified array or the sum of individually entered numbers.

  The number of numerical operands is not limited and can be any.

* If the operand types are **numbers**, and, for example, **3.ValueSV1 = 5** and **3.ValueSV2 = 63**, then **68;**

* If the operand type is an **array**, and, for example, **3.ValueSV1 = \[5, 10]**, then **15**.

## ParseNumber

The result is the syntactic parsing of the string and returning a numerical value.

  If the operand is a number, the result of the expression is also a number, and no errors occur. The string analysis is performed considering the specified separator between the integer and decimal parts of the number.

* If the operand type is **number**, and, for example, **3.ValueSV1 = 5**, then **5;**
* If the operand type is **string**, and, for example, **3.ValueSV1 = "5; 10"**, then **5,10.**

## FormatNumber

The result is the conversion of a numerical value and returning the value with the specified parameters:

  The separators for the decimal and thousands formats should be different, for example, a comma and a period.

* Format, for example, 4 (up to four decimal places);
* Decimal separator, default is ",";
* Thousands separator, default is ".".

* If the operand type is a **number**, and, for example, **3.ValueSV1 = 185.77**, then **185,7700.**

# Operators Basics

Operators in Latenode are like formulas in spreadsheets: they take input data and return a result.

## Using operators to modify data

You can use operators in almost any input field across nodes to transform data before sending it next:

* Build or modify text (replace ,concatenate, trim, case conversion)
* Do math and formatting
* Extract values from JSON/arrays
* Apply conditional logic (choose one value or another)

## Using operators in routes

Routes use operators for **filtering and branching**.
When operators are used in **Route > Condition**, the condition must evaluate to a boolean: **TRUE** or **FALSE**.

### The result of any route filter is TRUE or FALSE

* If the filter condition is **TRUE**, the scenario execution continues through that route.
* If the filter condition is **FALSE**, that route is not selected and execution does not go there.

### Fallback route

A fallback route triggers **only if none of the outgoing routes from the node evaluates to TRUE**.

Read more: [Fallback routes](../routes.mdx#fallback-routes)

### How to test and debug any filter

You can test any route filter by copying the same formula into a separate **Set Variables** node in a neighboring branch.

This makes debugging easier because you can see:

* the input values used by the expression
* the final result of the filter as **true/false** in the node output

**Example:** copy the route condition into Set Variables and store it into a variable (e.g. `test`) � then check the output.

# Variables

You can use our GPT Assistant for help with **Latenode operators**:

  👉 [**Latenode Operators Assistant**](https://chatgpt.com/g/g-67d704425c088191b741075e2b0f9815-latenode-operators-assistant)

  It can guide you on writing expressions, using variables, filters, and building logic inside your scenarios.

## Algorithm

Operators in this group provide the capability to return specific values.

## Result

## timestamp

This operator returns the number of seconds that have elapsed since midnight (00:00:00 UTC) on January 1, 1970 (Thursday), also known as the Unix epoch time.

* **Result of the expression:** Number (count of seconds).
* **Example:** If the function is executed at 2023-09-10T18:39:01Z, then **1694360344**.

## now

This operator returns the current date and time.

* **Result of the expression:** Date and time.
* **Example:** If the function is executed at 2023-09-10T15:40:28Z, then **2023-09-10T15:40:28Z.**

## getGlobalVar

This operator returns the value of the global variable whose name is specified as an operand.

* **Result of the expression:** Value of a global variable (string, number, boolean value).
* **Example:** If the **dayTemp** variable exists and its value is 283.500000, then **283.500000**.

# Integrations and API Errors

When using integration nodes (HTTP requests, apps, webhooks), the external service or API may return an error response. Below are typical codes in the **4xx** range (request or authorization error) and **5xx** range (server-side error). The exact message depends on the service; the node logs usually show the code and response body.

***

## 4xx — Client errors (request or access)

### 400 Bad Request

**What it means:** The server rejected the request because of invalid format or data (bad JSON, missing required field, wrong value type).

  Check the request body, headers, and parameters in the node settings. Refer to the service's API docs for required fields and format.

***

### 401 Unauthorized

**What it means:** The request is not authorized. Token is missing, expired, or invalid.

  Check the node's authorization settings (API key, Bearer token, OAuth). Refresh the token or re-authorize in [Authorizations](/visual-builder/authorizations).

***

### 403 Forbidden

**What it means:** Access to the resource is forbidden. Authorization may succeed but the account or app does not have permission (no access to the object, app limits, IP block, etc.).

  Check the account/app permissions in the service; ensure the token has the required scopes. If needed, create a new authorization with broader permissions.

***

### 404 Not Found

**What it means:** The resource at the given URL was not found (page, object, or API method removed, or the path is wrong).

  Check the URL in the node settings (typos, API version, correct path to the object). Ensure the resource exists in the service and has not been deleted.

***

### 408 Request Timeout

**What it means:** The server did not receive the full request within the allowed time and closed the connection.

  Increase the timeout in the node settings if available; simplify or reduce the request size; check if the external service is overloaded.

***

### 429 Too Many Requests

**What it means:** The API rate limit has been exceeded. The service temporarily rejects requests to reduce load.

  Reduce how often the scenario runs or how many requests go to the same API; add delays between requests or use pagination. For platform-side limits, see [Platform & Limits Errors](/visual-builder/possible-errors/platform-limits-errors#parallel-execution-limit).

***

## 5xx — Server errors (external service)

### 500 Internal Server Error

**What it means:** An internal error occurred on the external service. The request may be valid but the server could not process it.

  Retry the request later; check the service status (provider status page). If it persists, contact the service support or add [retry on error](/visual-builder/error-handling) to the scenario.

***

### 502 Bad Gateway

**What it means:** The server (or proxy) acted as a gateway and received an invalid response from the upstream server. Often due to overload or backend failure.

  Retry the request after a short time; if it continues, the issue is on the external service side.

***

### 503 Service Unavailable

**What it means:** The service is temporarily unavailable (maintenance, overload, outage). Usually asks to try again later.

  Run the scenario again later; enable retry on error in the node or scenario settings.

***

### 504 Gateway Timeout

**What it means:** The server (gateway) did not get a response from the upstream server in time. The request “hung” on the external service side.

  Retry the request; if 504 persists, the issue or limits are on the external API side (they need to increase timeout or you need to reduce request size).

# Platform & Limits Errors

Common errors related to platform limits, parallel runs, execution time, and compute resources (CPU/RAM). For more on limits, see [Platform limits](/visual-builder/scenarios/platform-limits).

***

## Plug and Play balance empty

The built-in AI credits for plug-and-play AI nodes have run out (separate from subscription credits).

**Message:** `AI Agent node error: 'plug and play balance is empty'`

**Cause:** Token limit for plug-and-play nodes on your account is exhausted.

  * Top up your **Plug and Play** balance in **Billing**.
  * Or add your own API key in the node's connection settings.

***

## Parallel execution limit

Too many scenario runs at once — plan's parallel execution limit exceeded (429).

**Messages:** `Webhook responded 429: exceed limit of parallel executions`, or that max simultaneous runs reached and requests are being rejected.

**Cause:** Multiple scenarios triggered at the same time and exceeded the plan limit.

  * Reduce trigger frequency.
  * Upgrade to a plan with a higher parallel execution limit.

***

## Execution time exceeded

The scenario ran longer than the platform's maximum allowed execution time.

**Message:** `Scenario execution time exceeded`

**Cause:** Scenario execution duration limit hit; often due to iterating over too much data, slow APIs, or heavy processing.

  * Split the array into smaller datasets; filter unneeded elements.
  * Optimize the scenario.
  * Use [enhanced compute resources (Engine Tier 1)](/visual-builder/scenarios/enhanced-compute-resources).

***

## CPU / RAM resource limits

The scenario needs more compute resources than the current engine tier allows.

**Messages:** `resource limits exceeded`, `Insufficient CPU/RAM resources — switch Memory and CPU Limits to Engine Tier 1`

**Cause:** JavaScript with large payloads in memory, Headless Browser on a low-resource tier, or large file/image processing.

  * Scenario settings → **Memory and CPU Limits** → **Engine Tier 1** or higher. See [Enhanced compute resources](/visual-builder/scenarios/enhanced-compute-resources).
  * Avoid loading large arrays into memory at once; split heavy work into separate scenarios.

***

## Scenario deployment limits

Unable to deploy or activate — node count or active scenario limit reached for your plan.

**Messages:** `node count limit reached`, `Maximum active scenarios reached — cannot activate new scenario`

**Cause:** Plan limits the number of active scenarios or nodes; too many scenarios are active at once.

  * Deactivate unused scenarios.
  * Simplify large scenarios (split into sub-scenarios).
  * Upgrade to a plan with higher limits.

# Scenario Building Errors

Below are common errors that occur when configuring nodes, using variable substitutions, and running scenarios. Variable format is described in [Variable templates](/visual-builder/data-flow/passing-data#variable-templates).

***

## Variable syntax errors

The correct variable format and placeholders are described on [Passing data](/visual-builder/data-flow/passing-data). The platform uses its own variable format. Plain names like `{{first_name}}`, non-Latin characters, or bare operators inside `{{ }}` are not valid.

**Messages:** `Unexpected symbol: f — invalid variable format {{first_name}}`, `Unexpected symbol: 乙 — non-Latin character`, `Unexpected symbol: & — expression {{&&}} contains invalid operator`

**Cause:** plain name `{{first_name}}` used; non-Latin characters in the name; or operator (`&&`, `||`) used directly inside `{{ }}`.

  * Node output: **`{{$nodeNumber.field}}`**, e.g. `{{$11.first_name}}`.
  * Scenario variable: **`{{_.variableName}}`**, global: **`{{%.name}}`**.
  * Insert substitutions via the variable helper widget or see [Variable templates](/visual-builder/data-flow/passing-data#variable-templates).

***

## Expression parsing errors

The expression engine cannot parse a formula, condition, or function call.

**Messages:** `Expression parsing error: unsupported expression`, `Expression error: split() called with three arguments`, `invalid syntax near '&&'`

**Cause:** calling functions like `randomString()` or `split()` with unsupported syntax; using `&&` / `||` directly inside `{{ }}`; unmatched brackets or quotes.

  * Move complex logic to a [JavaScript](/visual-builder/code-tools/node-js) node.
  * For conditions, use a route filter or an IF-style node.
  * Validate the expression in the editor before saving.

***

## Empty required fields

A mandatory node parameter has no value at execution time.

**Messages:** `required field "Message ID" is empty`, `required field "Chat ID" is empty`, `required field "Search Value" is empty`

**Cause:** field left blank or set to a non-existent variable `{{xxx}}`; previous node returned no data; variable path does not match the node output.

  * Map the field to previous node output: **`{{$nodeNumber.field}}`**, e.g. `{{$11.id}}`.
  * Check the previous node output in [execution history](/visual-builder/scenarios/execution-history).
  * Add a condition to verify the value exists before passing it.

***

## Undefined / null values

The node tries to access a property on a value that does not exist.

**Messages:** `Cannot read properties of undefined (reading "0")`, `Cannot read properties of null (reading 'access_token')`, `undefined is not an array or an array-like object`

**Cause:** previous node returned empty or unexpected data; variable path points to a non-existent field; auth token missing or expired.

  * Log the previous node output to verify its structure.
  * In a JavaScript node use optional chaining: `data?.field ?? ''`.
  * Add a condition to check the value exists before using it.

***

## JSON parse errors

The JSON Parse node receives input that is not valid JSON.

**Messages:** `SyntaxError: invalid or unexpected token`, `Unexpected token 'R' — input is plain text`, `Bad control character in string literal`, `Parameter "..." is invalid JSON`

**Cause:** previous node returned plain text, HTML, or error message; AI node output wrapped in markdown fences \`\`\`json; unescaped newlines in JSON; input is CSV, XML, or other non-JSON format.

  * Log the raw output before the JSON Parse node to inspect it.
  * Use a JS node to strip markdown fences if needed.
  * In AI node prompts, add "respond only in valid JSON, no markdown".

***

## Not iterable / empty output

A node expects an array but receives a single object, null, or nothing.

**Messages:** `rows_input is not iterable`, `undefined is not an array or an array-like object`, `get last records empty list`

**Cause:** passing a single object where an array is expected; previous node returned empty results; wrong data structure from upstream node.

  * Wrap single objects in an array in a JS node: `[data]`.
  * Add a condition to handle empty arrays before iterating.
  * Ensure the source returns an array before the node that expects it.

***

## Execution timeout

Scenario or node exceeds allowed execution time.

**Messages:** `Scenario execution time exceeded`, `TimeoutError: Waiting for selector failed: 60000ms exceeded`, `524 timeout — webhook scenario marked Canceled`

**Cause:** processing too many records in one run; inefficient loop or missing filters; Headless Browser waiting for a selector that never appears; webhook needs response in \<3s but scenario is too slow.

  * Split large batches using an [Iterator](/visual-builder/data-flow/iterating).
  * Add filters to reduce data volume before heavy operations.
  * For fast webhook response: return 200 immediately, process asynchronously.
  * Use [enhanced compute (Engine Tier 1)](/visual-builder/scenarios/enhanced-compute-resources) for heavy scenarios.

***

## HTTP Request node errors

Error in the HTTP Request node: invalid or empty URL, unsupported protocol, or control characters in the URL field.

**Messages:** `unsupported protocol scheme ""`, `URL missing http:// or https://`, `invalid control character in URL`, `Invalid URL — empty or malformed URL`

**Cause:** variable for URL resolved to null (URL becomes `https://null`); URL built by concatenation with missing base; hidden newline or carriage return in the URL field.

  * Log the URL variable value before the HTTP Request node.
  * Add a condition so the request runs only if URL is not null or empty.
  * Use a JS node to trim and validate the URL: `url.trim()`.

# Building Scenarios

## Saving a Scenario

After adding a scenario, rename it (if needed), add a description, and click **Save**.

  The **Save** button becomes active as soon as you make changes to the scenario or its nodes. To avoid losing changes, save your work regularly.

***

## Running a Scenario

### One-time Execution

  Before running a scenario, you need to configure it. If you're just starting out, see [Building Your First Scenario](../../get-started/quickstarts/building-first-scenario).

Click **Run Once** to execute the scenario once. This is useful for testing and debugging.

Depending on the trigger node:

* If the trigger node is an app node, create an event in the external application to trigger the scenario.
* If the trigger node is **Trigger on Webhook**, send an HTTP request to the node's URL.
* If the trigger node is **Trigger on Schedule** or **Trigger on Run once**, no additional actions are required.

After the scenario executes:

* Status icons (success / error) appear in the upper right corner of the nodes. Click on them to view details.

* A new entry appears in **Execution History**.

* The **Data** tab shows data from previous nodes.

* The **Variables** tab shows variable data (if variables were created).

You can stop a one-time execution by clicking **Stop**.

### Automatic Execution and Activation

To enable automatic execution of the scenario, activate the scenario using the **Active** toggle at the bottom of the scenario page. When the scenario is active, it runs automatically in response to configured triggers (webhooks, schedules, or app events).

  Notifications about scenario execution results are displayed only when running the scenario manually.

***

## Deployment and Scenario Branches

Scenarios have two branches:

* **Development**: for testing configuration and data processing results
* **Production**: for the production version of the scenario

Development and Production can be edited and executed independently.

To create a new Development version and publish it to Production:

1. Click **Save** to create a new version.

2. Ensure that the next Development version appears in the version list.

3. Click **Deploy**.

4. Ensure that the Production branch appears in the version list.

  **Selected** indicates the currently selected scenario version. **Production** indicates the Production branch.

If needed, you can roll back the Production branch:

1. Select a previous version.

2. Click **Deploy** to publish it to Production.

3. Check the **Selected** and **Production** labels on the published version.

***

## Triggers and Scenario Branches

Each scenario has a trigger node that starts the scenario. The behavior of some triggers depends on whether the scenario is deployed and whether it is active.

### Trigger on Webhook

The [**Trigger on Webhook**](../../../integrations/core-nodes/trigger-on-webhook.mdx) node starts the scenario when an HTTP request is sent to one of the node's URLs (Production or Development).

* The Production branch is triggered by requests to the Production URL. Deploy the scenario and ensure it is active.

* The Development branch is triggered by requests to the Development URL. For requests to be accepted, either run the scenario once or activate it with the **Active** toggle.

### Trigger on Schedule

The [**Trigger on Schedule**](../../../integrations/core-nodes/trigger-on-schedule.mdx) node triggers the Production branch according to the configured schedule (while the scenario is active).

The Development branch is not triggered on schedule, but you can run it manually with **Run once**.

### Trigger on Run once

The [**Trigger on Run once**](../../../integrations/core-nodes/trigger-on-run-once.mdx) node triggers the Development branch when **Run once** is clicked. The Production branch is not triggered when **Run once** is clicked.

  You can have multiple trigger nodes in a single scenario. For example, use **Trigger on Run once** for testing and **Trigger on Webhook** for end-to-end testing with incoming external data.

### App Triggers

App trigger nodes behave differently depending on the branch:

* The Production branch is triggered at regular intervals (depending on your plan) if the triggering event in the app has occurred.

  On **Starter**, triggers run every 10 minutes. On **Grow**, every 5 minutes. On **Prime**, every 2 minutes.

  Nodes with the word "Instant" in their name are an exception: they trigger immediately after the triggering event occurs in the external application.

* The Development branch is not triggered by the app trigger node. After manual **Run once**, it will execute if the triggering event occurs in the app.

***

## Other Settings

### Aligning Nodes

At the bottom of the scenario page, use **Align Nodes** to horizontally align the scenario chain (when nodes are connected by links).

  If scenario nodes are not connected, unconnected nodes are aligned vertically.

### Stickers

Use **Add Sticker** to add notes to the scenario. Stickers are optional but can be used for comments, links, and code snippets.

You can resize a sticker by dragging its edges. Right-click on a sticker to:

* **Copy** — copy it to duplicate in the current or another scenario
* **Delete** — delete it

# Enhanced Compute Resources (Engine Tier 1)

## What is this?

We've added the ability to run scenarios using an `engine` with increased compute resources. This can be useful in situations where the standard resource allocation is insufficient for successful scenario execution.

***

## Why is this needed?

By default, scenarios execute in a standard environment (**Default**), which is suitable for most use cases.

However, in some cases, the following problem may occur:

> Your scenario doesn't have enough resources, specifically RAM.

Using **Engine Tier 1** allows you to run such scenarios in an environment with enhanced resources.

***

## How does it work?

When running a scenario, you can specify the `engine_type` parameter to select the desired configuration:

* **Default** � standard engine (used by default)
* **Engine tier 1** � engine with increased compute resources

***

## How much does it cost?

Using **Engine Tier 1** is billed separately.

  **Engine Tier 1 doubles the cost of scenario execution. In other words, running a scenario with Engine Tier 1 will cost twice as much as running it in Default mode.**

This is because the system allocates additional infrastructure resources to support such executions.

***

## When should you use Engine Tier 1?

We recommend using **Engine Tier 1** if:

* your scenario is unstable in the standard environment;
* you see errors related to resource limits (e.g., Out of Memory);
* you know your scenario requires more RAM or CPU than usual;
* you're willing to pay for increased resource consumption.

***

## Frequently Asked Questions

**What resources are allocated for Engine Tier 1?**

We don't disclose specific technical parameters, as configurations may change. The main goal is to ensure successful execution of scenarios that exceed standard resource limits.

**Can I choose the engine type for each scenario?**

Yes. You can select the engine mode for each scenario by setting the appropriate value in the `engine_type` parameter.

***

## Troubleshooting

If your scenario fails with an error like:

> Scenario execution needs more CPU/RAM resources. Try switching Memory and CPU Limits to Tier-1.

try restarting it with **Engine Tier 1**.

In most cases, such errors are caused by resource exhaustion (e.g., memory or CPU limits). Switching to an engine with enhanced resources typically resolves the issue.

  Engine Tier 1 increases all available resources, **except for the 32 MB file size limit**, which remains unchanged. If you need to work with larger files, we recommend providing them via public URLs (e.g., file sharing services) instead of direct upload.

# Execution History

If the history table is empty, you need to run the scenario. For more on running a scenario once, see [One-time Scenario Execution](../../../integrations/core-nodes/trigger-on-run-once.mdx).

Each scenario run (successful or unsuccessful) is recorded in history. The history table is accessible by clicking the **History** button. The table displays key information about the scenario:

* **(1)** **Time** the scenario started;
* **(2)** **Branch** (Development or Production) of the executed scenario, including the version, e.g., v.13 Dev;
* **(3)** **Status** of scenario execution:

**Success** — if the scenario completed fully
**Error** — if errors occurred during the scenario
**Paused** — if the scenario is at the Wait node execution stage
**New** — if the scenario was stopped by clicking the **Stop** button

* **(4)** **Duration** of scenario execution in seconds;
* **(5)** Number of **credits** consumed by the scenario;
* **(6)** Number of **operations** performed in the scenario.

### Viewing the Scenario

Each scenario run record has a **View** button. Clicking the **View** button **(1)** displays the nodes **(2)** and their notifications **(3)** for the selected scenario version. If the scenario failed with an error, error information is displayed **(4)**.

### Restarting the Scenario

Each scenario run record has a **Restart** button. Clicking the **Restart** button:

* Initiates a re-run identical to the selected scenario version and input data
* Creates a new entry in history

  You can also copy a scenario execution from history.

# Import and Export

## Export

### Export Scenario

Next to each scenario, open the context menu (**?**) and select **Export scenario**. This will download the scenario as a JSON file.

### Export Folder

In the context menu next to any folder, select **Export folder** to export the entire folder as an archive. The archive includes all nested folders and scenarios.

***

## Import

### Import to a Specific Folder

In the context menu of any folder, select **Import a folder or scenario** to upload previously exported files directly into that folder.

### Import from Top Menu

You can also use **Import a folder or scenario** in the top toolbar to import files into the root directory or the currently selected folder.

***

## Migrating All Scenarios Between Accounts

To transfer **all your scenarios** from one account to another:

1. Move all scenarios into a single folder.
2. Use **Export folder** to export the folder as an archive.
3. Log in to the target account and use **Import a folder or scenario** to upload the archive.
4. Recreate and reconnect all **authorizations** (tokens, API keys, etc.) manually � they are not transferred with the scenarios.

# Platform Limits

The Latenode platform sets the following time limits for scenario or node execution:

* Maximum execution time for a [JavaScript](/visual-builder/code-tools/javascript) node is **2 minutes**.
* Maximum execution time for all nodes in any scenario is **30 minutes**.
  (the [Wait](/integrations/core-nodes/wait) node is not counted when calculating the total scenario execution time limit)
* Maximum number of nodes executed in a single scenario should not exceed **1000**
* Maximum size of data transferred between nodes in JSON format should not exceed **32 MB**

# Publishing Scenarios

Publishing means moving a scenario version from the **Development** branch to the **Production** branch. Production is the live version that runs on schedule, webhooks, or app events. To make that version run, click **Deploy**, then turn the scenario on with the **Active** toggle.

## Before you publish

Save the scenario with **Save** — that adds a new version to [version history](/visual-builder/scenarios/version-history). The version that gets published is the one currently **selected** in the version list (**Selected**). To publish a different version, select it in the list first, then click **Deploy**.

## How to publish (Deploy button)

1. Make sure the version you want is selected in the version list (Selected).
2. Click **Deploy**.
3. In the version list, that version will show the **Production** label — it’s now deployed to the live branch.

For a step-by-step guide with screenshots, see [Deployment and scenario branches](/visual-builder/scenarios/building-scenarios#deployment-and-scenario-branches) on the [Building scenarios](/visual-builder/scenarios/building-scenarios) page.

## Making the Production version run

After publishing, the scenario in Production will only run on triggers if it’s **on**. Turn it on with the **Active** toggle at the bottom of the scenario page. While **Active** is off, triggers (webhook, schedule, apps) won’t run the Production branch.

  Before turning **Active** on, make sure the scenario is tested (e.g. with **Run once** in Development) and ready for live runs.

## Rolling back Production

To roll Production back to an earlier version, select that version in the version list and click **Deploy** again — it becomes the new Production. For more, see [Version History](/visual-builder/scenarios/version-history).

## What's next

* [Building scenarios](/visual-builder/scenarios/building-scenarios) — saving, running, deployment, and triggers by branch
* [Version History](/visual-builder/scenarios/version-history) — version list, Selected and Production labels
* [Execution History](/visual-builder/scenarios/execution-history) — viewing past runs

# Version History

Version history is the list of saved states of a scenario. Each save creates a new version in the **Development** branch. One of the versions can be published to the **Production** branch for live runs. The version list lets you switch between scenario states and, if needed, roll back Production to an earlier version.

## Where the version list is

The version list appears on the scenario page (a dropdown with versions). It lists Development versions and marks which one is deployed to Production.

* **Selected** — the version currently selected (the one you are viewing or editing).
* **Production** — the version deployed to the Production branch (the one that runs in production when triggers fire).

## Creating versions, deploying, and rollback

A new version is added when you click **Save**; publishing to Production and rolling back to an earlier version are done via **Deploy**. For step-by-step instructions with screenshots, see [Deployment and scenario branches](/visual-builder/scenarios/building-scenarios#deployment-and-scenario-branches) on the [Building scenarios](/visual-builder/scenarios/building-scenarios) page.

## What's next

* [Building scenarios](/visual-builder/scenarios/building-scenarios) — saving, running, deployment, and branches
* [Execution History](/visual-builder/scenarios/execution-history) — viewing past scenario runs

# Creating and Editing Variables

## Creating a global variable

To add a new global variable, click the **New Variable** button on the page listing global variables.

After clicking the add button, a window for creating a global variable opens on the same page.

To create a variable, choose the variable type from the mandatory drop-down field **Select the type of variable** in the new variable window. The available values for selection are: string, number, JSON, and boolean.

### Variable Type - String, Number, JSON

If a variable of type string, number, or JSON is created, fill in the mandatory fields before clicking the **Save (4)** button:

* Variable name in the **Name (1)** field;
* Variable value (up to 32Mb for strings and JSON) in the **Value (2)** field;
* Indication of whether the variable can be edited from the scenario **(3)** (default - yes).

### Variable Type - Boolean

If the created variable is of boolean type, fill in the mandatory fields before clicking the **Save (4)** button:

* Variable name in the **Name (1)** field;
* One of the two possible values, true or false, for the variable in the **Value (2)** field;
* Indication of whether the variable can be edited from the script **(3)** (default - yes).

## Editing a global variable

To modify a global variable, click the **Edit (2)** button in the menu of the variable's row **(1)** in the global variables table.

After clicking the edit button, a window for changing the selected global variable opens on the same page. The variable parameters are filled in the corresponding fields and are available for modification.

## All Global Variables

Existing global variables are accessible for review on the **Global Variables** page in the corresponding table.

* (**1**) The name of the global variable is in the **Name** column;
* (**2**) The value of the global variable is in the **Value** column. The maximum size of the variable's value (string or JSON) is **32MB;**
* (**3**) The variable type is in the **Type of variable** column. Variables can be a string, number, JSON, or a boolean value (true/false);
* (**4**) The creation date of the global variable is in the **Creation Date** column. Using the gear icon, the column can be reconfigured to display the modification date instead of the creation date;

* Menu (**5**) available for each row allowing:

**Edit** the global variable;\
**Delete** the global variable.

  Upon clicking the **Delete** button and confirming the action in the modal window, the variable will be permanently deleted.

For ease of viewing and managing variables, a filter is available at the top of the global variables page. The test filter allows entering the desired variable name value.

# Global Variables in JavaScript Node

## �reate Global Variables

To ***create*** a global variable using the **JavaScript** node, you need to:

1. Add a **JavaScript** node to the scenario with the following code:

```jsx
export default async function run({ execution_id, input, data, store }) {
 // Set Global vars directly from JS
 // String, Obj and Number are available
 const gv_str = await store.setGlobalVariable("GlobalVarFromJs_string", "global var string value");
 const gv_obj = await store.setGlobalVariable("GlobalVarFromJs_obj", {"key":"global var object value"});
 const gv_num = await store.setGlobalVariable("GlobalVarFromJs_number", 100);

 return {
 }
}
```

This code represents an asynchronous function **`run`**. This function is intended for execution in a web automation scenario and uses objects **`execution_id`**, **`input`**, **`data`**, and **`store`**.

The function defines global variables **`GlobalVarFromJs_string`**, **`GlobalVarFromJs_obj`**, **`GlobalVarFromJs_number`** and saves them using the **`store.setGlobalVariable`** method. These global variables can be used later in other nodes of the scenario.

2. Run the **JavaScript** node once and wait for its execution.
3. View the globally created variables **`GlobalVarFromJs_string`**, **`GlobalVarFromJs_obj`**, **`GlobalVarFromJs_number`** on the **Global variables** interface.

4. Check for the presence of new global variables when filling in the parameters of any other node:

## Getting Global Variables

To ***get*** a global variable using a **JavaScript** node, you need to:

1. Add a **JavaScript** node to the scenario with the following code:

```jsx
export default async function run({ execution_id, input, data, store }) {

 // Get Global Vars
 const res_gv_str = await store.getGlobalVariable("GlobalVarFromJs_string")
 const res_gv_obj = await store.getGlobalVariable("GlobalVarFromJs_obj")
 const res_gv_num = await store.getGlobalVariable("GlobalVarFromJs_number")

 return {
  res_gv_str, res_gv_obj, res_gv_num
 }
}
```

This code represents an asynchronous function **`run`**. This function is designed to be executed in a web automation scenario and utilizes objects **`execution_id`**, **`input`**, **`data`**, and **`store`**. The code retrieves values of global variables using the **`store.getGlobalVariable`** method. This method returns values of previously set global variables.

2. Run the **JavaScript** node once and wait for its execution to complete.
3. Check the output data of the **JavaScript** node for the values of global variables:

## Removing Global Variables

Added global variables can be deleted.
To ***delete*** a global variable using a **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the scenario with the following code:

```jsx
export default async function run({ execution_id, input, data, store }) {
 // Del Global vars directly from JS

await store.deleteGlobalVariable("GlobalVarFromJs_string")
await store.deleteGlobalVariable("GlobalVarFromJs_obj")
await store.deleteGlobalVariable("GlobalVarFromJs_number")

 return {
 }
}
```

The code represents an asynchronous function **`run`** designed to be executed in a web automation scenario, utilizing the objects **`execution_id`**, **`input`**, **`data`**, and **`store`**. The function deletes existing global variables **`GlobalVarFromJs_string`**, **`GlobalVarFromJs_obj`**, **`GlobalVarFromJs_number`** using the **`store.deleteGlobalVariable`** method. Global variables are permanently deleted and cannot be used by other scenarios.

2. Run the **JavaScript** node once and wait for its execution.

3. Check for the absence of global variables **`GlobalVarFromJs_string`**, **`GlobalVarFromJs_obj`**, **`GlobalVarFromJs_number`** on the Global Variables interface.

## Getting a list of global variables

To ***get a list*** of global variables using a **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the scenario with the following code:

```jsx
export default async function run({ execution_id, input, data, store }) {
 // List Global vars directly from JS

const List = await store.listGlobalVariables()

 return {
List
 }
}
```

The code represents an asynchronous function **`run`** designed to be executed in a web automation scenario, utilizing the objects **`execution_id`**, **`input`**, **`data`**, and **`store`**. The function allows obtaining a list of all existing global variables using the **`store.listGlobalVariables`** method.

2. Run the **JavaScript** node once and wait for its execution.
3. Examine the output data of the **JavaScript** node, which will contain an array of global variables. Attributes are provided for each global variable:

* Name "key";
* Type "type";
* Editability indicator "editable";
* Creation date "created\_at";
* Last modification date "last\_modified\_at".

# Variables in JavaScript Node

With the JavaScript node, it is possible to manage local variables.

## Сreate Variables

To create a variable using the **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the scenario with the following code:

```jsx
export default async function run({ execution_id, input, data, store }) {
 // Set Vars directly from JS
 // String are available
 const v_str = await store.setVariable("VarFromJs", "var value");

 return {
 }
}
```

This code represents an asynchronous function **`run`**. This function is designed to be executed in a web automation scenario and utilizes objects **`execution_id`**, **`input`**, **`data`**, and **`store`**.

The function defines the variable **`VarFromJs`** and saves it using the **`store.setVariable`** method. This variable can only be used within the current scenario.

2. Run the **JavaScript** node once and wait for its execution.
3. Check for the existence of the new variable when populating parameters for any other node.

## Getting Variables

To ***get*** a variable using the **JavaScript** node, follow these steps:

1. Add a **JavaScript** node to the scenario with the following code:

```jsx
export default async function run({ execution_id, input, data, store }) {

 // Get Vars
 const res_v_str = await store.getVariable("VarFromJs")

 return {
  res_v_str
 }
}
```

This code represents an asynchronous function **`run`**. This function is designed to be executed in a web automation scenario and utilizes objects **`execution_id`**, **`input`**, **`data`**, and **`store`**.

The code extracts the values of the variable using the **`store.getVariable`** method. This method returns the value of a previously set variable.

2. Run the **JavaScript** node once and wait for its execution.
3. Check the output data of the **JavaScript** node for the variable values:

# Troubleshooting

Personal accounts are not intended for mass messaging. Use a separate number and minimal load.

  New accounts require "warming up" — you cannot send many messages immediately. Gradually increase volumes, otherwise WhatsApp will block the account.

## Common Errors

### Error 401 Unauthorized

```json
{
  "status": 401,
  "title": "Unauthorized",
  "message": "This account has been disconnected. To proceed using your account, please re-authorize your connection in the Authorizations section"
}
```

**What to do:**

1. Open the Authorizations section
2. Click **Reconnect / Reauthorize**
3. Scan the QR code in WhatsApp on your phone
4. Make sure your phone is online and WhatsApp is open

  Reauthorization is free if the connection was not deleted and the current period is still paid.

***

### Frequent Disconnections

The connection may break for various reasons:

**On your side:**

* Phone is offline or WhatsApp is unloaded from memory
* WhatsApp Web is open in another service or browser
* VPN or frequent IP changes

**On WhatsApp's side:**

* Inactivity for more than 14 days — session closes automatically
* WhatsApp reinstallation, phone change, or restore from backup — all connected devices are disconnected
* Phone number change or two-factor authentication PIN change
* Suspicious activity (unusual IP, frequent reconnections)
* Issues due to browser cache clearing or system updates

***

## Best Practices

To reduce the risk of blocking:

* Use random intervals between messages
* Limit the number of recipients
* Add variation to texts — don't send identical messages
* Monitor complaints from recipients
* Avoid words that WhatsApp may consider spam

# Bitrix24

To use Bitrix24 nodes, you need to generate an incoming webhook in the application and get its address.

## Obtaining a webhook address

To get the address of a webhook you need to:

1. Register in the Bitrix24 application and go to the application. On the **Developer resources** page, select **Other**:

2. On the Other page, select **Inbound webhook**;

3. On the **Inbound webhook** page:

* **(1)** Copy the automatically generated webhook address;
* **(2)** Select the desired webhook method and, if necessary, configure the parameters;
* **(3)** Configure the necessary permissions (the parameter can be filled in automatically).

4. Add the name of the inbound webhook **(1)** and save the changes **(2)**.

The list of created webhooks is available on the Integrations tab:

# Discord

For **Discord bot** group nodes to work, you need to get a token and perform authorization.

## Receiving a token

To obtain a token you need to:

1. Go to [Discord Developer Portal](https://discord.com/developers/applications) and create an application by clicking on the **New Application** button;

2. Fill in the name of the application, agree to the terms and policies, and then click **Create**;

3. On the opened application page, click the tab **Bot**;

4. Check the privileges available for the bot (it is recommended to check MESSAGE CONTENT INTENT to display message content);

5. Mark bot permissions and save the changes;

6. On the **OAuth2** tab, check the **bot** checkboxes and the permissions available to it;

7. Copy the generated URL and navigate to the address in a new browser tab;

8. Select the server to which you want to add the bot and click **Continue**;

9. Confirm the bot's rights and click on the **Authorize** button. After authorization the bot will be added to the selected server;

10. Click the **Reset Token** button;

11. Copy the generated token and save it for later use.

# Facebook

## Receiving a token

  Before following the instructions, you need to sign up for **Facebook**.

For nodes of the **Facebook** group to work, it is necessary to get a token.

To obtain a token you need to:

1. Follow the [link](https://developers.facebook.com/apps) and click the **Create application** button;

2. On the **Create an app** page, select **The other** option and click **Read more**;

3. Fill in the application name, email address, and click the **Application creation** button;

4. On **The Panel** (1) application settings page, select **The messenger** and click **Configure** (2);

5. On the **Settings of Messenger API** (1) page, go to section 2.2 and click the **To connect** button (2). In the dialog box that opens, choose the pages you want your app to access and click Continue and Save.

6. On the **Settings of Messenger API** (1) page, in section 2.2, click the **Generate** button (2);

7. In the **Token Generated** dialog box, confirm that you understand and then copy the token.

# Fauna

To use **Fauna** group nodes it is necessary to get a key (token) and perform authorization.

## Receiving a token

  The received key (token) must be saved after copying, as it is displayed only when created.

To obtain a token you need to:

1. Register in the **Fauna** app and go to the main [page](https://dashboard.fauna.com/resources/home);

2. Click on the **Create Database** button;

3. Configure the database and click the Create button;

4. Select the required row in the list of databases in the **Databases** table;

5. Place the cursor over the name of the desired database and click the **Manage Keys** icon;

6. Click the **Create Key** button;

7. Configure the key parameters and click the **Save** button;

8. Copy the created key and save it.

## Configuring authorization in nodes

When configuring a node in the **Fauna** group, authorization is required. To do this, you need to:

1. Select the required node from the **Fauna** group;

2. Click the **Create Authorization** button;

3. Click the **New Authorization** button and select **Access Token**;

4. In the **access\_token** field enter the token you received earlier and click the **Authorize** button;

5. View whether the node has authorization and fill in the remaining node configuration fields.

You can view the result of the node execution when you run the scenario or by clicking on the node's **Run Once** button.

# Fireflies.ai

Use the Fireflies.ai nodes in Latenode to automate your workflows. You can retrieve meeting transcripts, run GraphQL queries, and list all available transcripts.

## Prerequisites

* A Fireflies.ai account ([Sign up here](https://fireflies.ai/))
* A Latenode account ([Sign up here](https://latenode.com/))
* Your Fireflies.ai API key (Navigate to the Integrations section → Click on Fireflies API → Copy and store your API key securely)

## Steps to Connect and Configure Fireflies.ai

### 1. Log in to Latenode

Go to [https://app.latenode.com/](https://app.latenode.com/) and log in.

### 2. Create a New Authorization

* Go to Connections: [https://app.latenode.com/connections](https://app.latenode.com/connections)
* Click **New Authorization**
* Search for **Fireflies.ai (API Key)**
* Paste your API key
* Save the connection

### 3. Create and Configure a Scenario

* Go to Scenarios: [https://app.latenode.com/scenarios](https://app.latenode.com/scenarios)
* Click **Create New Scenario**
* In the scenario canvas, add a new node.
* In the search bar, find and select a Fireflies.ai node (e.g., Get Transcript, Execute GraphQL Query, List Transcripts).

### 4. Configure the Get Transcript Node

* Click the node to open settings
* Under **Authorization**, choose the Fireflies.ai connection you created
* Fill in the required parameters depending on the method

### 5. Test the Connection

* Click **Run Node Once** to check that the API key works and the node returns data.

# Flutterflow

The Latenode platform facilitates interaction with apps created using the Flutterflow service through the Trigger on Webhook node.

Flutterflow provides intuitive tools for designing mobile app interfaces, enabling quick and efficient frontend development with minimal effort. Latenode can manage the backend logic.

**Example Scenario: Generating Random Numbers for Display in Flutterflow**

  You can watch a training video here.

## Creating a Latenode Scenario

* **Trigger on Webhook**: Start the scenario with this node and save its URL for later use in Flutterflow.

* **JavaScript**: Add a node with code to generate a random number.

```jsx
export default async function run({execution_id, input, data, store}) {
    let randomNumber = Math.floor(Math.random() * 101);

    return {
        random_number: randomNumber
    }
}
```

* **Webhook Response**: Use this node to send the scenario's result to Flutterflow.

## Building the Form in Flutterflow

**Sign Up**: Register on Flutterflow.

### Create Project

* Go to the Projects page and click Create new.

* Name the new project and select Create Blank.

### Interface Design

* In the Widget Tree (1) tab, view interface elements and update the text element (2) at the top.

* Add a TextField (2) to the Column (1) element.

* Add a Button to the Column.

* Customize settings, align fields, and rename buttons as desired.

### API Setup

* In the API Calls (1) tab, select Create API Call (2).

* Name the call (1), add the Trigger on Webhook (2) node address, and click Add Call (3).

### Testing

* Run once the scenario on Latenode.

* In the Response & Test tab, click "Test API Call" and view the results. For the output parameter `number`, click Add JSON Path, name it (1), and save (2).

* Return to the Widget Tree (1) tab and click Add parameter (2).

* Add a string parameter `number` and click Confirm.

* For the TextField (1) element, set the Initial Value (2) to the `number` (3).

* For the Button (1) element, go to the Action section (2).

* Open the Action Flow Editor and add an action to call the configured API, so the request is sent to Latenode when the button is clicked. Change the output parameter name of the first action as needed.

* Add an action to pass the response to the `number` parameter.

## Testing the Created Scenario and Flutterflow Form

* Click the application launch button.

* Run once the scenario on the Latenode platform.

* Click the Generate button and view the random number generated by Latenode.

# Framer

The **Latenode** platform allows interaction with websites created using the **Framer** service. For interaction, only the **Trigger on Webhook** node is needed.

Let's create a scenario that records the email address entered in a website form into a Google Sheet. First, use the Framer service to create the registration form with a field for entering the email address and a confirmation button.

## Creating a Framer Form

1. In the Framer workspace, choose the method to add a **Code** element. In the **Create Code File** window, enter any name and select the **New component** option.

2. Click the **Create** button.

3. On the opened page, add the code below and save the changes by pressing Ctrl + S. The form with an email input field and a **Signup** button will appear on the right side of the interface.

```jsx
import React, { useState } from "react"
import Example from "https://framer.com/m/framer/Example.js@^1.0.0"

export default function AuthorizationForm(props) {
    // Update this with your Trigger on Webhook URL
    const formUrl = "Your_URL"

    const [email, setEmail] = useState("")
    const [formStatus, setFormStatus] = useState("unsubmitted")

    const onSubmit = async (event) => {
        event.preventDefault()

        try {
            const response = await fetch(formUrl, {
                method: "POST",
                body: JSON.stringify({ email }),
                headers: {
                    "Content-type": "application/json",
                },
            })

            if (!response.ok) {
                throw new Error("Network response was not ok")
            }

            setFormStatus("submitted")
        } catch (error) {
            console.error("Error during form submission: ", error)
            setFormStatus("error")
        }
    }

    const handleEmailChange = (event) => {
        setEmail(event.target.value)
    }

    if (formStatus === "submitted") {
        return (

        )
    }

    if (formStatus === "error") {
        return
    }

    return (
        <>


        </>
    )
}

const containerStyle = {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "0.5rem",
    borderRadius: "4px",
    maxWidth: "500px",
    margin: "auto",
}

const inputStyle = {
    flex: "1",
    fontSize: "16px",
    padding: "0.75rem",
    margin: "0",
    backgroundColor: "#18181B",
    border: "1px solid #333",
    borderRadius: "12px",
    color: "#FFF",
    marginRight: "0.5rem",
}

const submitButtonStyle = {
    fontSize: "16px",
    padding: "0.75rem 1.5rem",
    backgroundColor: "#2C91ED",
    color: "#FFF",
    border: "none",
    borderRadius: "12px",
    cursor: "pointer",
    fontWeight: "bold",
}

const responseText = {
    textAlign: "center",
    color: "#5FCEAE",
    fontSize: "16px",
    marginTop: "1rem",
}

const labelStyle = {
    textAlign: "center",
    color: "#FFF",
    fontSize: "16px",
    marginBottom: "1rem",
}
```

## Setting Up the Latenode Scenario and Sending Email

1. In the scenario created on the platform, add a **Trigger on Webhook** node. After adding, copy the URL address. You can run the node once to view the output data.

2. Replace `Your_URL` in the Framer form code with the URL address of the **Trigger on Webhook** node.

  Remember, the **Production-branch** of the scenario is initiated by a request sent to the Production-version URL of the **Trigger on Webhook** node. The **Development-branch** of the scenario is initiated by a request sent to the Development-version URL of the **Trigger on Webhook** node.

3. After adding the URL address, fill in the field with a test email address and click the **Signup** button.

4. Once you click the **Signup** button, the **Trigger on Webhook** node will execute, and the output data will include the provided email address.

5. To record the received email address in a Google Sheet, add an **Add Single Row** node and configure it:

* Create or select an existing authorization.
* Choose the desired Google Sheet and sheet tab.
* Select the parameter from the previous node for the **Values** field in the auxiliary window.

The result of the scenario execution is that the email address entered in the **Framer** form is recorded in a cell of the **Google** Sheet.

# Front

Use the Latenode Front nodes to automate your customer communication. Manage conversations, messages, contacts, and more directly from your workflows.

## Prerequisites

* A Front account ([Sign up here](https://frontapp.com/signup))
* A Latenode account ([Sign up here](https://app.latenode.com/))

## Steps to Connect and Configure Front

### 1. Log in to Latenode

Navigate to [https://app.latenode.com/](https://app.latenode.com/) and log in with your credentials.

### 2. Create a New Authorization

* Go to the **Connections** section: [https://app.latenode.com/connections](https://app.latenode.com/connections)
* Click **New Authorization**
* Search for and select **Front** (Front OAuth 2.0)
* Follow the OAuth 2.0 prompts to authenticate and connect your Front account

### 3. Create and Configure a Scenario

* Navigate to the **Scenarios** section: [https://app.latenode.com/scenarios](https://app.latenode.com/scenarios)
* Click **Create New Scenario**
* In the scenario canvas, add a new node. In the search bar, find and select a **Front** node (e.g., "Create Message", "Create Contact")

### 4. Configure the Node

* Click on the newly added Front node to open its configuration
* Under **Authorization**, select the Front connection you created in Step 2
* Fill in all the required parameters for the action (e.g., Contact details, Message content)

### 5. Test the Connection

* Click **Run Node Once** to test the configuration and ensure it works correctly.

# Google Cloud Storage and Google Cloud Pub/Sub

To use nodes from the **Google Cloud Storage** and **Google Cloud Pub/Sub** groups, you need to obtain a key (token) and authorize access.

## Obtaining a Token

To get a key (token), follow these steps:

1. Create a Google account and visit [this link](https://cloud.google.com/iam/docs/creating-managing-service-accounts).

2. On the **Create service accounts** page, click **Enable the API**.

3. On the **Enable API wizard** page, click **CREATE PROJECT**.

4. Configure the project and click **CREATE**.

5. Confirm the project and allow API usage.

6. Go to [this link](https://cloud.google.com/iam/docs/creating-managing-service-accounts) and scroll down. Click **Go to Create a service account**.

7. Select the project created in step 4.

8. Configure the account details (only the name is mandatory, but defining access rights is recommended) and click **DONE**.

9. Go to [this link](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and scroll down. Click **Go to Service accounts**.

10. Select the project created in step 4.

11. Select the account address for which you need to create a key.

12. Go to the **KEYS** tab and click the **ADD KEY** dropdown.

13. Choose **Create new key**.

14. Select the JSON key type and click **CREATE**.

15. View the downloaded key in JSON format. Open the file in any text editor and copy its contents.

16. Go to [this link](https://console.cloud.google.com/apis/library) and select the project created in step 4.

17. Search for the desired API and choose either **Cloud Storage API** or **Cloud Pub/Sub API**.

18. Enable the API by clicking **ENABLE**.

## Authorization Setup in Nodes

When configuring nodes in the **Google Cloud Storage** and **Google Cloud Pub/Sub** groups, you need to authorize access. To do this:

1. Select the desired node, for example, from the **Google Cloud Pub/Sub** group.

2. Click the **Create an authorization** button.

3. Click **New authorization** and choose **Cloud Pub/Sub**.

4. In the **service\_json** field, enter the previously obtained key in JSON format and click **Authorize**.

5. Verify the authorization in the node and complete the remaining node configuration fields.

You can view the node's execution result by running the scenario or clicking the **Run once** button on the node.

# Google Services (Personal Account)

## Create and configure a Google Cloud Platform project for Google Personal OAuth

  You need to follow this procedure if you use an email address that ends with `@gmail` or `@googlemail`.
  To create a new project or work in the existing one, you need to have the `serviceusage.services.enable` permission. If you don't have this permission, ask the Google Cloud Platform Project Owner or Project IAM Admin to grant it to you.

To connect to Latenode using your own client credentials, you can create and configure a project in the Google Cloud Platform.

## Create a Google Cloud Platform project for Google Drive

To create a Google Cloud Platform project:

1. Log in to the Google Cloud Platform using your Google credentials.
2. On the welcome page, click **Create or select a project** > **New project**. If you already have a project, proceed to step 5.

3. Enter a **Project name** and select the **Location** for your project.
4. Click **Create**.
5. In the top menu, check if your new project is selected in the **Select a project** dropdown. If not, select the project you just created.

## Enable the required API

1. Open the left navigation menu and go to **APIs & Services** > **Library**.
2. Search for the following required APIs: e.g **Google Drive API**.
3. Click **Google Drive API** (or any other service API you need), then click **Enable**. If you see the **Manage** button instead of the **Enable** button, you can proceed to the next step: the API is already enabled.

## Configure your OAuth consent screen for Google Drive

To configure your OAuth consent screen:

1. In the left sidebar, click **Google Auth Platform**.
2. Click **Get Started**.
3. In the **Overview** section, under **App information**, enter **Latenode** as the app name and provide your Gmail address. Click **Next**.
4. Under **Audience**, select **External**. Click **Next**.

  For more information regarding user types, refer to [Google's Exceptions to verification requirements documentation](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts).

5. Under **Contact Information**, enter your Gmail address. Click **Next**.
6. Under **Finish**, agree to the Google User Data Policy.
7. Click **Continue** > **Create**.
8. Click **Create OAuth Client**.
9. In the **Branding** section, under **Authorized domains**, add `app.latenode.com`. Click **Save**.
10. Optional: In the **Audience** section, add your Gmail address on the **Test users** page, then click **Save and continue** if you want the project to remain in the **Testing** publishing status.
11. In the **Data Access** section, click **Add or remove scopes**, add the following scopes (please find table below with service reference).

You can add scopes using:

* A table with filters:

* A window to manually enter scopes:

12. Click **Update**.
13. Click **Save**.

## Create your Google OAuth client credentials

To create your client credentials:

1. In Google Auth Platform, click **Clients**.
2. Click **+ Create Client**.
3. In the **Application type** dropdown, select **Web application**.
4. Update the **Name** of your OAuth client. This will help you identify it in the platform.
5. In the **Authorized redirect URIs** section, click **+ Add URI** and enter the following redirect URI: `https://app.latenode.com/redirected/index.html`
6. Click **Create**.
7. Click the OAuth 2.0 Client you created, copy your **Client ID** and **Client secret** values, and store them in a safe place.

You will use these values in the **Client ID** and **Client Secret** fields in Latenode.

## Establish the connection in Latenode

1. Log in to your Latenode account, add a nodule to your scenario, and click **Create an authorization > New authorization > Personal App Google \<Service> Oauth 2.0**
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Enter your Client ID and Client secret that you created in the previous section.
4. Click **Sign in with Google**.
5. If prompted, authenticate your account, grant all requested permissions, and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Google nodules.

## Required scopes for your connection

| Google OAuth                               | Scopes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gmail                                      | `https://www.googleapis.com/auth/userinfo.email` `https://mail.google.com/`                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Google Calendar                            | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/calendar` `https://www.googleapis.com/auth/calendar.readonly` `https://www.googleapis.com/auth/calendar.events.owned` `https://www.googleapis.com/auth/calendar.settings.readonly`                                                                                                                                                                                                                                                                                      |
| Google Analytics                           | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/cloud-platform` `https://www.googleapis.com/auth/cloud-platform.read-only` `https://www.googleapis.com/auth/analytics` `https://www.googleapis.com/auth/analytics.edit` `https://www.googleapis.com/auth/analytics.manage.users` `https://www.googleapis.com/auth/analytics.manage.users.readonly` `https://www.googleapis.com/auth/analytics.provision` `https://www.googleapis.com/auth/analytics.readonly` `https://www.googleapis.com/auth/analytics.user.deletion` |
| Google Ads                                 | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/adwords`                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Google BigQuery                            | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/bigquery` `https://www.googleapis.com/auth/bigquery.insertdata` `https://www.googleapis.com/auth/bigquery.readonly` `https://www.googleapis.com/auth/cloud-platform` `https://www.googleapis.com/auth/cloud-platform.read-only`                                                                                                                                                                                                                                         |
| Google Cloud Dialogflow                    | `https://www.googleapis.com/auth/cloud-platform.read-only` `https://www.googleapis.com/auth/cloud-platform` `https://www.googleapis.com/auth/dialogflow`                                                                                                                                                                                                                                                                                                                                                                                                  |
| Google Cloud Firestore                     | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/cloud-platform` `https://www.googleapis.com/auth/datastore`                                                                                                                                                                                                                                                                                                                                                                                                             |
| Google Cloud Speech-to-Text/Text-to-Speech | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/cloud-platform`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Google Cloud Translate                     | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/cloud-translation` `https://www.googleapis.com/auth/cloud-platform`                                                                                                                                                                                                                                                                                                                                                                                                     |
| Google Contacts                            | `https://www.googleapis.com/auth/contacts.other.readonly` `https://www.googleapis.com/auth/contacts.readonly` `https://www.googleapis.com/auth/contacts` `openid` `https://www.googleapis.com/auth/userinfo.profile` `https://www.googleapis.com/auth/userinfo.email`                                                                                                                                                                                                                                                                                     |
| Google Docs                                | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/drive` `https://www.googleapis.com/auth/drive.readonly` `https://www.googleapis.com/auth/docs` `https://www.googleapis.com/auth/drive.file`                                                                                                                                                                                                                                                                                                                             |
| Google Drive                               | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/drive` `https://www.googleapis.com/auth/drive.readonly`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Google Forms                               | `https://www.googleapis.com/auth/forms.body` `https://www.googleapis.com/auth/forms.body.readonly` `https://www.googleapis.com/auth/forms.responses.readonly` `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/drive`                                                                                                                                                                                                                                                                                                    |
| Google Groups                              | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/admin.directory.group` `https://www.googleapis.com/auth/admin.directory.domain`                                                                                                                                                                                                                                                                                                                                                                                         |
| Google Business Profile                    | `email` `https://www.googleapis.com/auth/business.manage`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Google Sheets                              | `https://www.googleapis.com/auth/drive` `https://www.googleapis.com/auth/drive.readonly` `https://www.googleapis.com/auth/spreadsheets` `https://www.googleapis.com/auth/user.emails.read` `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/userinfo.profile`                                                                                                                                                                                                                                                            |
| Google Slides                              | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/drive` `https://www.googleapis.com/auth/drive.file` `https://www.googleapis.com/auth/drive.readonly` `https://www.googleapis.com/auth/presentations` `https://www.googleapis.com/auth/presentations.readonly` `https://www.googleapis.com/auth/spreadsheets` `https://www.googleapis.com/auth/spreadsheets.readonly`                                                                                                                                                    |
| Google Tasks                               | `https://www.googleapis.com/auth/userinfo.email` `https://www.googleapis.com/auth/tasks` `https://www.googleapis.com/auth/tasks.readonly`                                                                                                                                                                                                                                                                                                                                                                                                                 |

# Instagram for Business (Personal Account)

## Overview

Instagram for Business provides powerful tools including analytics, advertising options, and shopping capabilities to help companies showcase products, engage customers, and grow their brand online. With the Instagram for Business (Personal Account) integration on Latenode, you can automate workflows involving events, insights, media, users, comments, and stories from your Instagram Business account.

## Requirements

Before connecting Instagram for Business to Latenode, ensure you have:

1. A Facebook account with admin-level access to a Facebook Page connected to your Instagram account
2. An Instagram Business account (not a Creator account)

If you have a regular Instagram account, convert it to a Business account using [Instagram's guide](https://help.instagram.com/502981923235522)

## Creating a Facebook Developer App

1. Go to the [Facebook Developer Portal](https://developers.facebook.com/)
2. Click "My Apps" in the upper right corner and select "Create an app."
3. Click the admin app you created

4. On the main "Dashboard" page, find Instagram under "My Products" and click the "Settings" button.

5. On the "Set up Instagram Business Login API" page, copy the Instagram App ID and App Secret values.

## Connecting to Latenode

1. Log in to your Latenode account
2. Create a new scenario or open an existing one
3. Add an Instagram for Business action or trigger to your scenario
4. Click "Create an authorization" and click "New authorization"

5. Click **Personal App Instagram Oauth 2.0**
6. Enter your Client ID and Client secret that you created in the previous section
7. Configure the added action or trigger
8. Click "Save" or "Save & Run"

## Troubleshooting Connection Issues

If no Instagram pages appear in the dropdown:

1. Verify your Facebook account has admin access to the connected Facebook Page
2. Confirm your Instagram account is a Business account (not Creator)
3. Ensure proper connection between Facebook Page and Instagram account via Meta Business Suite

## Available Nodes

After connecting, you can use these nodes:

### Actions

* **Create Carousel Post** � Create multi-image carousel posts
* **Create Photo Post** � Publish single image posts
* **Download Media** � Download media content from your account
* **Get Media Insights** � Retrieve analytics for specific media items
* **Get User Insights** � Access detailed user analytics
* **List Album Media** � View all media in an album
* **List Media Comments** � Retrieve comments on specific media
* **List Stories** � Get a list of all active stories

### Triggers

* **New Media Posted in My Account** � Detects when new photos, videos, or carousels are published on your Instagram Business account.

## Additional Resources

* [Instagram API with Facebook Login documentation](https://developers.facebook.com/docs/instagram-api)
* [Instagram for Business Help Center](https://help.instagram.com/)

# Intercom

## How to Work with Intercom Authorization and Nodes on Latenode

1. Navigate to [https://app.latenode.com/](https://app.latenode.com/) and log in using your Latenode credentials or Google OAuth.
2. Go to the Authorization section: [https://app.latenode.com/connections](https://app.latenode.com/connections)
3. Click **New Authorization**
4. In the menu, find **Intercom** → **Intercom Authorization** and click it to authorize.
5. Follow the Intercom OAuth 2.0 flow to complete the authorization.
6. Navigate to the Scenarios section: [https://app.latenode.com/scenarios](https://app.latenode.com/scenarios)
7. Click the **Create New Scenario** button.
8. Click on the new node.
9. In the **Actions** section, find any Intercom node.
10. Select any node from the list.
11. Click on the created node.
12. Click **Create Authorization**.
13. Click on the created authorization.
14. Fill in the required parameters in the node.
15. Click **Run Node Once**.

## Notes

* You can delete any of your authorizations in the Authorization section by clicking on the respective authorization options and selecting the **Delete** button. It won't be archived or stored. You will need to create a new authorization if necessary.
* You can delete scenarios with history at any time by clicking on the respective scenario options and selecting the **Delete** button. It won't be archived or stored. You will need to create a new scenario and nodes if required. It will be a completely new scenario with an empty history.

# MongoDB

To use nodes in the **MongoDB** group, you must obtain authorization credentials.

## Obtaining credentials

To obtain a host, login credentials, and password, you must:

1. Register in the **MongoDB** application and start the cluster creation process. In the **Deploy your database** section, you can select the free plan and leave the default settings (cluster name in the **Name** field, etc.);

2. Click the **Create Deployment** button;

3. Add a user with access to the database by defining their login (**Username**) and password (**Password**). The data can be copied;

4. Click the **Create Database User** button;

5. Click the **Choose a connection method** button;

6. Select **Drivers**;

7. Leave the default settings and view the string generated in step 3. **Copy the part of the string after the @ and before the ?** In the example: `cluster0.piecrrs.mongodb.net/`. Click the **Review setup steps** button.

8. View the string to connect in the next setup window (you can copy part of the string if not done in the previous step). Click the **Done** button.

9. View the created cluster on the **Database** tab;

10. Go to the **Network Access** tab and click on the **Add IP Address** button;

11. Click the **Allow access from anywhere** button (no special access settings are needed to test authorization). Click the **Confirm** button.

12. View access availability on the **Network Access** tab.

  For authorization you will need: **login and password from step 3 and a part of the string from step 7.**

## Configuring authorization in nodes

When configuring a node in the **MongoDB** group, authorization is required. To do this, you need to:

1. Select the required node from the **MongoDB** group;

2. Click the **Create an authorization** button;

3. Click on **New Authorization** and select **MongoDB API Key**;

4. In the fields for credentials enter the host (part of the string from step 7 of the instructions above), login and password (from step 3 of the instructions above). Click the **Authorize** button;

5. View whether the node is authorized and fill in the remaining node configuration fields.

You can view the result of the node execution when you run the scenario or by clicking on the node's **Run Once** button.

# Notion

To use the nodes in the **Notion** group, you need to create an authorization. Here's how to do it:

1. Go to the **Authorizations** page and click on the **New authorization** button;

2. In the **Choose a service** window, select **Notion**;

3. In the **Notion** authorization group, choose **OAuth2**;

4. Select the required workspace and click on the **Select Pages** button;

5. Choose the necessary pages within the workspace and click on the **Allow Access** button.

# PagerDuty

## How to Connect PagerDuty to Latenode

1. Navigate to [https://app.latenode.com/](https://app.latenode.com/) and log in with your credentials.
2. Navigate to Authorization Section: [https://app.latenode.com/connections](https://app.latenode.com/connections)
3. Click **New Authorization**
4. In a menu find **PagerDuty** → **PagerDuty Authorization**. Click it to authorize.
5. Proceed with PagerDuty OAuth 2.0 flow to complete the Authorization.
6. Navigate to Scenarios Section: [https://app.latenode.com/scenarios](https://app.latenode.com/scenarios)
7. Click **Create New Scenario** button
8. Click on new node
9. Find any PagerDuty Node in Actions Section
10. Pick any node from list
11. Click on created Node
12. Click on **Create Authorization**
13. Click on created Authorization
14. Fill needed parameters in a node
15. Click **Run Node Once**

# Salesforce

To connect your **Salesforce** account to **Latenode**, you need to create a **custom app** in Salesforce. This is necessary to get the **Consumer Key**, **Consumer Secret**, and **Subdomain**.

Here's a quick overview of the steps:

1. **Log in to Salesforce** and go to **Setup** (click the gear icon in the top right).
2. In the left sidebar, search for **"App Manager"** and open it.
3. Click **"New Connected App"** in the top right corner.
4. Fill in the basic information like app name, API name, and email.
5. Click **"Enable OAuth Settings"**, then scroll down and **open "Advanced Settings"** to reveal additional options.
6. Set the **Callback URL** to any valid URL (e.g. `https://example.com` — Latenode doesn't use it directly).
7. Add the following **OAuth Scopes**:
   * `Full access (full)`
   * `Perform requests on your behalf at any time (refresh_token, offline_access)`
8. Save the app and wait a few minutes for it to become active.
9. After it's active, go back to the app detail page — there you'll find your **Consumer Key** and **Consumer Secret**.

## Subdomain

Take the first part of your Salesforce URL.

For example, if your login URL is:

```
https://yourcompany.my.salesforce.com
```

Then your subdomain is: `yourcompany`

Once you have these three values, enter them into Latenode like this:

# Shopify

## Instructions for Authorization in Shopify

To complete authorization, you need to obtain the **Admin API Access Token** and the **Shop ID**. Here's how to do it:

***

## 1. Admin API Access Token

1. Navigate to your [Shopify Admin](https://admin.shopify.com/).

2. Go to **Settings** > [Apps and Sales Channels](https://admin.shopify.com/settings/apps) > Click **Develop apps**.

3. Click **Create a new app** or select an existing app.

4. Provide a name for the app and assign an app administrator.

5. Proceed to the app setup screen.

6. Select the necessary scopes (permissions) and save your changes (the **Save** button is at the bottom of the page).

7. Go to the **API Credentials** section, click **Install App**, and agree to the prompt.

8. Once installed, your Admin API Access Token will be available. Copy it for later use.

***

## 2. Shop ID

The Shop ID can always be found in the URL of your admin panel in your browser.

***

## 3. Authorization on Latenode

1. Add the required node in Latenode and click **New Authorization**.

2. Enter the obtained credentials (Admin API Access Token and Shop ID).

3. That's it! You're authorized. Perform a test run to check the results.

***

This process ensures that your Shopify and Latenode integration is set up correctly for seamless functionality.

# Slack Bot

## Receiving a token

  Before following the instructions, you need to sign up for **Slack** and create a workspace.

For nodes of the **Slack bot** group to work, it is necessary to get a token and perform authorization.

To obtain a token you need to:

1. Go to [Slack API](https://api.slack.com/apps) and create an app by clicking on **Create New App**;

2. In the **Create an app** window, select the **From scratch** option;

3. Customize the app - fill in the name and select the desired **Slack** space. Click the **Create App** button;

4. On the application settings page, click the **OAuth & Permissions** tab;

5. In the **Scopes** block, define the permissions available to the **Slack** bot;

6. In the **OAuth Tokens for Your Workspace** block, click the **Install to Workspace** button.

7. Confirm accesses by pressing the **Allow** button;

8. In the **OAuth Tokens for Your Workspace** block, view and copy the **Bot User OAuth Token**;

9. Add a bot to the required channel by sending the message `/invite @<botname>` to this channel, where `<botname>` is the name of the bot (corresponds to the name of the application that was created in the above step);

10. View the availability of a bot added to the channel;

## Configuring authorization in nodes

When configuring a node in the **Slack bot** group, authorization is required. To do this, you need to:

1. Select the required node from the **Slack bot** group;

2. Click the **Create an authorization** button;

3. Click on **New authorization** (1) and select **Access Token** (2);

4. In the **access\_token** field enter the token received in item 8 of the instructions above. Press the **Authorize** button;

5. View the presence of authorization in the node;

6. Fill in the required fields of the node settings.

You can view the result of the node execution when you run the scenario or by clicking on the node's **Run Once** button. You can also see the message sent to the specified Slack channel.

# Supabase

## Using Trigger on Webhook node

To work with **Supabase** service you can use URL of [Trigger on Webhook](/integrations/core-nodes/trigger-on-webhook) nodes of **Latenode** platform. After registration in the **Supabase** application it is necessary to:

1. Click on the **New Project** button to create a new project;

2. Create a new organization by clicking the **Create organization** button;

3. Create a new project by clicking the **Create new project** button;

4. After creating the organization and project on the **Tables** tab, click on the **New table** button;

5. Create a new table in the **Create a new table under `public`** window, filling in the table name. If necessary, the required columns can be added to the table;

6. View the row with the new table on the **Tables** tab in the **Database Tables** block;

7. To view the table, click on the menu in the row and select **View table**;

8. Press **Insert row** to add a row to the created table;

9. View the added row on the **Table Editor** tab;

10. Go to the **Database** page and open the **Webhooks** tab. Click the **Enable webhooks** button;

11. Click the **Create a new hook** button to create a new webhook;

12. Configure the webhook in the **Create a new database webhook** window by adding its name (**Name**), defining the table (**Table**) and the events at which the query should be sent (**Events**).

Select HTTP Request (**Type of webhook**) as the type of webhook, POST (**Method**) as the method, and the address of the [Trigger on Webhook](/integrations/core-nodes/trigger-on-webhook) node of the **Latenode** platform (**URL**) as the address. After selecting all the parameters, click on the **Create Webhook** button;

  To get the URL of the Trigger on Webhook node, you need to create a scenario and add this node to it. Clicking on the node will open its configuration window, where you can copy the URL.

13. View the created webhooks in the **Database Webhooks** table;

14. Go to the scenario page with the **Trigger on Webhook** (1) node whose URL was used to create the webhook in the **Supabase** application. Expand the scenario (2) and view its active status (3).

15. Add a row (id = 2) to the **Supabase** table;

16. View the results of the scenario (1) in the history, including the output parameters of the Trigger on Webhook node (2).

The output parameters of the Trigger on Webhook node are the added string data:

```json
{
  "body": {
    "old_record": null,
    "record": {
      "created_at": "2024-04-25T18:13:57+00:00",
      "id": 2,
      "name": "Kate"
    },
    "schema": "public",
    "table": "TestTest",
    "type": "INSERT"
  },
  "client_ip": "",
  "headers": {
    "Accept": "*/*",
    "Content-Length": "159",
    "Content-Type": "application/json",
    "User-Agent": "pg_net/0.8.0"
  },
  "method": "POST",
  "query": {},
  "url": "http://"
}
```

# Twitter (X)

## 1. Creating an App

Go to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)

In the **Projects** section, select the **Default project** (it is created automatically)

Click **Add App**

Enter a name for your app and click **Next**

The app is now created � but don't save the keys yet.

We'll return here later to get the necessary data.

***

## 2. Setting Permissions

Go to **User authentication settings**

Set the necessary permissions (e.g., **Read and Write**)

In the **Type of App** section, select:

? **Native App** � Public client

In the **App info** block, make sure to enter the following values exactly:

?? **Callback URL / Redirect URL**:

`https://app.latenode.com/redirected/index.html`

?? **Website URL**:

`https://app.latenode.com/connections`

  **Important**: These fields must be entered exactly as shown � otherwise, the authorization won't work.

***

After this, you'll receive the **Client ID** and **Client Secret**.

These are the values you need to paste into the authorization form in **Latenode**, then confirm login.

# Zoom

## How to Work with Zoom Authorization and Nodes on Latenode

1. Navigate to [https://app.latenode.com/](https://app.latenode.com/) and log in using your Latenode credentials or Google OAuth.
2. Go to the Authorization section: [https://app.latenode.com/connections](https://app.latenode.com/connections)
3. Click **New Authorization**
4. In the menu, find **Zoom** → **Zoom Authorization** and click it to authorize.
5. Follow the Zoom OAuth 2.0 flow to complete the authorization.
6. Navigate to the Scenarios section: [https://app.latenode.com/scenarios](https://app.latenode.com/scenarios)
7. Click the **Create New Scenario** button.
8. Click on the new node.
9. In the **Actions** section, find any Zoom node.
10. Select any node from the list.
11. Click on the created node.
12. Click **Create Authorization**.
13. Click on the created authorization.
14. Fill in the required parameters in the node.
15. Click **Run Node Once**.

## Notes

* You can delete any of your authorizations in the Authorization section by clicking on the respective authorization options and selecting the **Delete** button. It won't be archived or stored. You will need to create a new authorization if necessary.
* You can delete scenarios with history at any time by clicking on the respective scenario options and selecting the **Delete** button. It won't be archived or stored. You will need to create a new scenario and nodes if required. It will be a completely new scenario with an empty history.