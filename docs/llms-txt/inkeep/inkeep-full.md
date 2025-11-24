# Inkeep Documentation

Source: https://docs.inkeep.com/llms-full.txt

---

# API Key Management
URL: /api-keys

Secure API key management for agent authentication

***

title: API Key Management
description: Secure API key management for agent authentication
---------------------------------------------------------------

# API Key Management

The Inkeep Agent Framework provides a comprehensive API key management system for authenticating access to agents. API keys are securely hashed and stored, with support for expiration and revocation.

## Overview

API keys provide a secure way to authenticate programmatic access to your agents. Each API key is:

* **Securely hashed** using scrypt algorithm before storage
* **Scoped to a specific tenant and agent**
* **Revocable** at any time
* **Expirable** with optional expiration dates

## Usage

### Creating an API Key

```typescript
import { createApiKey } from '@inkeep/agents-core';

const result = await createApiKey({
  tenantId: 'your-tenant-id',
  agentId: 'your-agent-id',
  expiresAt: '2025-12-31T23:59:59Z', // Optional expiration
});

// IMPORTANT: Show this key to the user only once!
console.log('Your API Key:', result.key);
// Example: sk_live_abc123def456...

// The API key record (without the actual key)
console.log('Key Details:', result.apiKey);
```


# Core concepts
URL: /concepts

Learn about the key building blocks of Inkeep - Agents, Sub Agents, tools, data components, and more.

***

title: Core concepts
sidebarTitle: Concepts
description: Learn about the key building blocks of Inkeep - Agents, Sub Agents, tools, data components, and more.
icon: "LuBoxes"
---------------

## Agents

In Inkeep, an **Agent** is the top-level entity you can interface with via conversational experiences (chat) or trigger programmatically (via API).

Under the hood, an Agent is made up of one or more **Sub Agents** that work together to respond to a user or complete a task.

## Tools

When you send a message to an Agent, it is first received by a **Default Sub Agent** that decides what to do next.

In a simple Agent, there may be only one Sub Agent with a few tools available to it.

**Tools** are actions that a Sub Agent can take, like looking up information or performing a task on apps and APIs.

In Inkeep, tools can be added to Sub Agents as:

* **MCP Servers**: Connect to external services and APIs via the Model Context Protocol. You can:

  * **Connect to Native MCP servers** provided directly by SaaS vendors (no building required)
  * **Access Composio's platform** for 10,000+ out-of-box MCP servers for popular services (no building required)
  * **Use Gram** to convert OpenAPI specs into MCP servers
  * **Build and deploy Custom servers** for your own APIs and business logic

  Register any of these with their associated **Credentials** for your Agents to use.
* **Function Tools**: Custom JavaScript functions that Agents can execute directly without the need for standing up an MCP server.

Typically, you want a Sub Agent to handle narrow, well-defined tasks. As a general rule of thumb, keep Sub Agents to be using 5-7 related tools at a time.

## Sub Agent relationships

When your scenario gets complex, it can be useful to break up your logic into multiple Sub Agents that are specialized in specific parts of your task or workflow. This is often referred to as a "Multi-agent" system.

A Sub Agent can be configured to:

* **Transfer** control of the chat to another Sub Agent. When a transfer happens, the receiving Sub Agent becomes the primary driver of the thread and can respond to the user directly.
* **Delegate** a subtask for another ('child') Sub Agent to do and wait for its response before proceeding with the next step. A child Sub Agent *cannot* respond directly to a user.

## Sub Agent 'turn'

When it's a Sub Agent's turn, it can choose to:

1. Send an update message to the user
2. Call a tool to collect information or take an action
3. Transfer or delegate to another Sub Agent

An Agent's execution stays in this loop until one of the Sub Agents chooses to respond to the user with a final result.

<Note>
  Sub Agents in Inkeep are designed to respond to the user as a single, cohesive unit by default.
</Note>

## Chatting with an Agent

<>
  You can talk to an Inkeep Agent in a few ways, including:

  * **UI Chat Components**: Drop-in React components for chat UIs with built-in streaming and rich UI customization. See [`agents-ui`](/talk-to-your-agents/react/chat-button).
  * **As an MCP server**: Use your Inkeep Agent as if was an MCP Server. Allows you to connect it to any MCP client, like Claude, ChatGPT, Claude and other Agents. See [MCP server](/talk-to-your-agents/mcp-server).
  * **Via API (Vercel format)**: An API that streams responses over server-side events (SSE). Use from any language/runtime, including the Vercel's `useChat` and AI Element primitives for custom UIs. See [API (Vercel format)](/talk-to-your-agents/api).
  * **Via API (A2A format)**: An API that follows the Agent-to-Agent ('A2A') JSON-RPC protocol. Great for when combining Inkeep with different Agent frameworks that support the A2A format. See [A2A protocol](/talk-to-your-agents/a2a).

  <Cards>
    <Card title="React UI" icon="LuMessageSquare" href="/talk-to-your-agents/react/chat-button">
      Drop-in chat components for React apps with streaming and rich UI.
    </Card>

    <Card title="API (Vercel format)" icon="LuNetwork" href="/talk-to-your-agents/api">
      POST /api/chat, SSE (text/event-stream), x-vercel-ai-data-stream: v2.
    </Card>

    <Card title="A2A protocol" icon="LuNetwork" href="/talk-to-your-agents/a2a">
      JSON-RPC messages at /agents/a2a with blocking and streaming modes.
    </Card>

    <Card title="MCP server" icon="LuServer" href="/talk-to-your-agents/mcp-server">
      HTTP JSON-RPC endpoint at /v1/mcp with session header management.
    </Card>
  </Cards>
</>

## Authentication & API Keys

You can authenticate with your Agent using:

* **API Keys**: Securely hashed keys that are scoped to specific Agents
* **Development Mode**: No API key required, perfect for local development and testing
* **Bypass Secrets**: For internal services and infrastructure that need direct access

API keys are the recommended approach for production use, providing secure, scoped access to your Agents.

## Agent replies with Structured Data

Sometimes, you want your Agent to reply not in plain text but with specific types of well-defined information, often called 'Structured Outputs' (JSON).

With Inkeep, there are a few ways to do this:

* **Data Components**: Structured Outputs that Sub Agents can output in their messages so they can render rich, interactive UIs (lists, buttons, forms, etc.) or convey structured information.
* **Artifacts**: A Sub Agent can save information from a **tool call result** as an artifact in order to make it available to others. For example, a Sub Agent that did a web search can save the contents of a webpage it looked at as an artifact. Once saved, a Sub Agent can cite or reference artifacts in its response, and other Sub Agents or users can fetch the full artifacts if they'd like.
* **Status Updates**: Real-time progress updates that can be plain text or Structured Outputs that can be used to keep users informed about what the Sub Agent is doing during longer operations.

## Passing context to Sub Agents

Beyond using Tools to fetch information, Sub Agents also receive information via:

* **Headers**: In the API request to an Agent, the calling application can include headers for a Sub Agent. Learn more [here](/typescript-sdk/headers).
* **Context Fetchers**: Can be configured for an Agent so that at the beginning of a conversation, an API call is automatically made to an external service to get information that is then made available to any Sub Agent. For example, your Headers may include a `user-id`, which can be used to auto-fetch information from a CRM about the user for any Sub Agent to use.

Headers and fetched context can then be referenced explicitly as `{{variables}}` in Sub Agent prompts. Learn more [here](/typescript-sdk/headers).

## Ways to build

Quick reference to the key docs for building with the Visual Builder or the TypeScript SDK.

<Tabs>
  <Tab title="Visual Builder">
    <Cards>
      <Card title="MCP Servers" icon="LuServer" href="/visual-builder/tools/mcp-servers">
        Configure and manage MCP servers for your Sub Agents.
      </Card>

      <Card title="Agents" icon="LuSpline" href="/visual-builder/sub-agents">
        Create and manage Agents visually.
      </Card>

      <Card title="Data Components" icon="LuBlocks" href="/visual-builder/structured-outputs/data-components">
        Build rich UI elements Sub Agents can render in conversations.
      </Card>

      <Card title="Artifact Components" icon="TbInputSpark" href="/visual-builder/structured-outputs/artifact-components">
        Define structured outputs generated by tools or Sub Agents.
      </Card>

      <Card title="Status Components" icon="LuClock" href="/visual-builder/structured-outputs/status-components">
        Show progress updates during longer operations.
      </Card>

      <Card title="Credentials" icon="LuKey" href="/visual-builder/tools/credentials">
        Manage secrets and auth for MCP servers.
      </Card>

      <Card title="Project Management" icon="LuFolder" href="/visual-builder/project-management">
        Organize agents, MCP Servers, and other entities in Projects.
      </Card>
    </Cards>
  </Tab>

  <Tab title="TypeScript SDK">
    <Cards>
      <Card title="Sub Agent Settings" icon="LuUser" href="/typescript-sdk/agent-settings">
        Configure Sub Agents with prompts, tools, and data components.
      </Card>

      <Card title="MCP Servers" icon="LuHammer" href="/typescript-sdk/tools/mcp-servers">
        Add tools as MCP servers.
      </Card>

      <Card title="Function Tools" icon="LuCode" href="/typescript-sdk/tools/function-tools">
        Create custom JavaScript functions that run in secure sandboxes.
      </Card>

      <Card title="Sub Agent Relationships" icon="LuUsers" href="/typescript-sdk/agent-relationships">
        Define how Sub Agents transfer and delegate tasks.
      </Card>

      <Card title="Data Components" icon="LuBlocks" href="/typescript-sdk/structured-outputs/data-components">
        Build custom UI elements Sub Agents can render.
      </Card>

      <Card title="Artifact Components" icon="TbInputSpark" href="/typescript-sdk/structured-outputs/artifact-components">
        Create structured outputs from tools or Sub Agents.
      </Card>

      <Card title="Status Updates" icon="LuClock" href="/typescript-sdk/structured-outputs/status-updates">
        Provide real-time progress updates.
      </Card>

      <Card title="Context Fetchers" icon="LuCirclePlus" href="/typescript-sdk/context-fetchers">
        Dynamically fetch and cache external context.
      </Card>

      <Card title="Credentials" icon="LuKey" href="/typescript-sdk/tools/credentials">
        Store and retrieve credentials for MCP tools.
      </Card>
    </Cards>
  </Tab>
</Tabs>

The Visual Builder and TypeScript SDK work seamlessly together—define your Sub Agents in code, push them to the Visual Builder, and iterate visually.

## Projects

You can organize your related MCP Servers, Credentials, Agents, and more into **Projects**. A Project is generally used to represent a set of related scenarios.

For example, you may create one Project for your support team that has all the MCP servers and Agents related to customer support.

## CLI: Push and pull

The Inkeep CLI bridges your TypeScript SDK project and the Visual Builder.

Run the following from your project (the folder that contains your `inkeep.config.ts`) which has an `index.ts` file that exports a project.

* **Push (code → Builder)**: Sync locally defined agents, Sub Agents, tools, and settings from your SDK project into the Visual Builder.

```bash
inkeep push
```

* **Pull (Builder → code)**: Fetch your project from the Visual Builder back into your SDK project. By default, the CLI will LLM-assist in updating your local TypeScript files to reflect Builder changes.

```bash
inkeep pull
```

<Note>
  Push and pull operate at the project level (not individual agents). Define agents in your project and push/pull the whole project.
</Note>

See the [CLI Reference](/typescript-sdk/cli-reference) for full command details.

## Deployment

Once you've built your Agents, you can deploy them using:

<Cards>
  <Card title="Deploy with Docker" icon="LuContainer" href="/self-hosting/docker">
    Self-host your Agents using Docker for full control and flexibility.
  </Card>

  <Card title="Deploy to Vercel" icon="LuRocket" href="/self-hosting/vercel">
    Deploy your Agents to Vercel for easy serverless hosting.
  </Card>
</Cards>

## Architecture

The Inkeep Agent framework is composed of several key services and libraries that work together:

* **agents-manage-api**: An API that handles configuration of Agents, Sub Agents, MCP Servers, Credentials, and Projects with a REST API.
* **agents-manage-ui**: Visual Builder web interface for creating and managing Agents. Writes to the `agents-manage-api`.
* **agents-sdk**: TypeScript SDK (`@inkeep/agents-sdk`) for declaratively defining Agents and custom tools in code. Writes to `agents-manage-api`.
* **agents-cli**: Includes various handy utilities, including `inkeep push` and `inkeep pull` which sync your TypeScript SDK code with the Visual Builder.
* **agents-run-api**: The Runtime API that exposes Agents as APIs and executes Agent conversations. Keeps conversation state and emits OTEL traces.
* **agents-ui**: A UI component library of chat interfaces for embedding rich, dynamic conversational AI experiences in web apps.


# The No-Code + Code Agent Builder
URL: /overview

Inkeep is a platform for building Agent Chat Assistants and AI Workflows.

***

title: The No-Code + Code Agent Builder
sidebarTitle: Overview
icon: "LuBookOpen"
description: Inkeep is a platform for building Agent Chat Assistants and AI Workflows.
--------------------------------------------------------------------------------------

With Inkeep, you can build AI Agents with a **No-Code Visual Builder** and **Developer SDK**. Agents can be edited in either with **full 2-way sync**, so technical and non-technical teams can create and manage their Agents in one platform.

## Two ways to build

### No-Code Visual Builder

A drag-and-drop canvas so any team can create and own the Agents they care about.

<Image src="/gifs/drag-n-drop.gif" alt="No-Code Agent Builder demo" />

### TypeScript Agents SDK

A code-first framework so engineering teams can build with the tools they expect.

```typescript
import { agent, subAgent } from "@inkeep/agents-sdk";
import { consoleMcp } from "./mcp";

const helloAgent = subAgent({
  id: "hello-agent",
  name: "Hello Agent",
  description: "Says hello",
  canUse: () => [consoleMcp], 
  prompt: `Reply to the user and console log "hello world" with fun variations like h3llo world`,
});

export const basicAgent = agent({
  id: "basic-agent",
  name: "Basic Agent",
  description: "A basic agent",
  defaultSubAgent: helloAgent,
  subAgents: () => [helloAgent],
});
```

The **Visual Builder and TypeScript SDK are fully interoperable**: your technical and non-technical teams can edit and manage Agents in either format and switch or collaborate with others at any time.

## Use cases

Inkeep Agents can operate as **Agentic AI Chat Assistants**, for example:

* a customer experience agent for help centers, technical docs, or in-app experiences
* an internal copilot to assist your support, sales, marketing, ops, and other teams

Agents can also be used for **Agentic Workflow Automation** like:

* Creating and updating knowledge bases, documentation, and blogs
* Updating CRMs, triaging helpdesk tickets, and tackling repetitive tasks

## Platform Overview

**Inkeep Open Source** includes:

* A Visual Builder & TypeScript SDK with 2-way sync
* Multi-agent architecture to support teams of agents
* MCP Tools with credentials management
* A UI component library for dynamic chat experiences
* Triggering Agents via MCP, A2A, & Vercel SDK APIs
* Observability via a Traces UI & OpenTelemetry
* Easy deployment to Vercel and using Docker

Interested in a managed platform? Sign up for the [Inkeep Cloud waitlist](https://inkeep.com/cloud-waitlist) or learn about [Inkeep Enterprise](https://inkeep.com/enterprise).

## Our Approach

Inkeep is designed to be extensible and open: you can use the LLM provider of your choice, use Agents via open protocols, and with a [fair-code](/community/license) license and great devex, easily deploy and self-host Agents in your own infra.

[Join our community](https://docs.inkeep.com/community/inkeep-community) to get support, stay up to date, and share feedback.

## Next Steps

<Cards>
  <Card title="Follow the <1min Quick Start" icon="LuZap" href="/get-started/quick-start">
    Get started with the Visual Builder and TypeScript SDK in under 5 minutes.
  </Card>

  <Card title="Conceptual Overview" icon="LuLightbulb" href="/concepts">
    Learn about the key concepts of building Agents with Inkeep.
  </Card>
</Cards>


# Pricing
URL: /pricing

Learn about Inkeep's pricing plans and features

***

title: Pricing
description: Learn about Inkeep's pricing plans and features
icon: "LuCreditCard"
--------------------

Inkeep offers two ways to get started: **Open Source** (free forever) and **Enterprise** (managed platform with dedicated support).

***

## Open Source (Free)

Everything you need to create agentic assistants, copilots, and workflows that help your customers and your team.

Includes:

* No-Code Visual Builder
* TypeScript Agents SDK
* MCP Servers and Custom Tools
* Observability via UI & OpenTelemetry
* UI Component Library
* Use with Claude, ChatGPT, & Cursor

[Follow the \<1min Quick Start →](/get-started/quick-start)

***

## Enterprise

Managed platform and a trusted partner to accelerate AI agent adoption and deployment.

Everything in Open Source, plus:

* Unified AI Search (Managed RAG)
* Use from Slack & Support Platforms
* PII removal and data controls
* Cloud Hosting & User Management
* Trainings, enablement, and support
* Dedicated forward deployed engineer

[Schedule a Demo →](https://inkeep.com/demo)

***

## Feature Comparison

### Building Agents

| Feature                          | Open Source | Enterprise |
| -------------------------------- | ----------- | ---------- |
| No-Code Visual Builder           | ✓           | ✓          |
| Agent Developer SDK (TypeScript) | ✓           | ✓          |
| 2-way Sync: Edit in Code or UI   | ✓           | ✓          |

### Core Framework

| Feature                                                | Open Source | Enterprise |
| ------------------------------------------------------ | ----------- | ---------- |
| Take actions on any MCP Server, App, or API            | ✓           | ✓          |
| Multi-agent Architecture (Teams of Agents)             | ✓           | ✓          |
| Agent Credential and Permissions Management            | ✓           | ✓          |
| Agent Traces available in UI and OTEL                  | ✓           | ✓          |
| Talk to Agents via A2A, MCP, and Vercel AI SDK formats | ✓           | ✓          |

### Talk to Your Agents (Out of the Box)

| Feature                                            | Open Source | Enterprise |
| -------------------------------------------------- | ----------- | ---------- |
| With Claude, ChatGPT, and Cursor                   | ✓           | ✓          |
| With Slack, Discord, and Teams integrations        | —           | ✓          |
| With Zendesk, Salesforce, and support integrations | —           | ✓          |

### Building Agent UIs

| Feature                                             | Open Source | Enterprise |
| --------------------------------------------------- | ----------- | ---------- |
| Agent Messages with Custom UIs (forms, cards, etc.) | ✓           | ✓          |
| Custom UIs using Vercel AI SDK format               | ✓           | ✓          |
| Out-of-box Chat Components (React)                  | ✓           | ✓          |
| Out-of-box Chat Components (JavaScript)             | —           | ✓          |
| Answers with Inline Citations                       | ✓           | ✓          |

### Unified AI Search (Managed RAG)

| Feature                                                           | Open Source | Enterprise |
| ----------------------------------------------------------------- | ----------- | ---------- |
| Real-time fetch from databases, APIs, and the web                 | ✓           | ✓          |
| Automated Ingestion of public sources (docs, help center, etc.)   | —           | ✓          |
| Automated Ingestion of private sources (Notion, Confluence, etc.) | —           | ✓          |
| Optimized Retrieval and Search (Managed RAG)                      | —           | ✓          |
| Semantic Search                                                   | —           | ✓          |

### Insights & Analytics

| Feature                            | Open Source | Enterprise |
| ---------------------------------- | ----------- | ---------- |
| AI Reports on Knowledge Gaps       | —           | ✓          |
| AI Reports on Product Feature Gaps | —           | ✓          |

### Authentication and Authorization

| Feature                   | Open Source | Enterprise |
| ------------------------- | ----------- | ---------- |
| Single Sign-on            | —           | ✓          |
| Role-Based Access Control | —           | ✓          |
| Audit Logs                | —           | ✓          |

### Security

| Feature                               | Open Source | Enterprise |
| ------------------------------------- | ----------- | ---------- |
| PII Removal                           | —           | ✓          |
| Uptime and Support SLAs               | —           | ✓          |
| SOC II Type II and Pentest Reports    | —           | ✓          |
| GDPR, HIPAA, DPA, and Infosec Reviews | —           | ✓          |

### Deployment

| Feature       | Open Source | Enterprise                    |
| ------------- | ----------- | ----------------------------- |
| Hosting Types | Self-hosted | Cloud, Hybrid, or Self-Hosted |
| Support Type  | Community   | Dedicated Engineering Team    |

### Forward Deployed Engineer Program

| Feature                                    | Open Source | Enterprise |
| ------------------------------------------ | ----------- | ---------- |
| Dedicated Architect and AI Agents Engineer | —           | ✓          |
| 1:1 Office Hours and Trainings             | —           | ✓          |
| Structured Pilot                           | —           | ✓          |


# Troubleshooting Guide
URL: /troubleshooting

Learn how to diagnose and resolve issues when something breaks in your Inkeep agent system.

***

title: Troubleshooting Guide
sidebarTitle: Troubleshooting
description: Learn how to diagnose and resolve issues when something breaks in your Inkeep agent system.
icon: LuWrench
keywords: troubleshooting, debugging, errors, timeline, signoz, widget implementation
-------------------------------------------------------------------------------------

## Overview

This guide provides a structured methodology for debugging problems across different components of your agent system.

## Step 1: Check the Timeline

The timeline is your first stop for understanding what happened during a conversation or agent execution. Navigate to the **Traces** sections to view in depth details per conversation. Within each conversation, you'll find an **error card** that is clickable whenever something goes wrong during agent execution.

### What to Look For

* **Execution flow**: Review the sequence of agent actions and tool calls
* **Timing**: Check for delays or bottlenecks in the execution
* **Agent transitions**: Verify that transfers and delegations happened as expected
* **Tool usage**: Confirm that tools were called correctly and returned expected results
* **Error cards**: Look for red error indicators in the timeline and click to view detailed error information

### Error Cards in the Timeline

Clicking on this error card reveals:

* **Error type**: The specific category of error (e.g., "Agent Generation Error")
* **Exception stacktrace**: The complete stack trace showing exactly where the error occurred in the code

This detailed error information helps you pinpoint exactly what went wrong and where in your agent's execution chain.

<>
  ### Copy Trace for Debugging

  The `Copy Trace` button in the timeline view allows you to export the entire conversation trace as JSON. This is particularly useful for offline analysis and debugging complex flows.

  <Image src="/images/copy-trace.png" alt="Copy Trace button in the timeline view for exporting conversation traces" />

  #### What's Included in the Trace Export

  When you click `Copy Trace`, the system exports a JSON object containing:

  ```json
  {
    "metadata": {
      "conversationId": "unique-conversation-id",
      "traceId": "distributed-trace-id",
      "agentId": "agent-identifier",
      "agentName": "Agent Name",
      "exportedAt": "2025-10-14T12:00:00.000Z"
    },
    "timing": {
      "startTime": "2025-10-14T11:59:00.000Z",
      "endTime": "2025-10-14T12:00:00.000Z",
      "durationMs": 60000
    },
    "timeline": [
      // Array of all activities with complete details:
      // - Agent messages and responses
      // - Tool calls and results
      // - Agent transfers
      // - Artifact information
      // - Execution context
    ]
  }
  ```

  #### How to Use Copy Trace

  1. Navigate to the **Traces** section in the management UI
  2. Open the conversation you want to debug
  3. Click the **Copy Trace** button at the top of the timeline
  4. The complete trace JSON is copied to your clipboard
  5. Paste it into your preferred tool for analysis

  This exported trace contains all the activities shown in the timeline, making it easy to share complete execution context with team members or support.
</>

## Step 2: Check SigNoz

SigNoz provides distributed tracing and observability for your agent system, offering deeper insights when the built-in timeline isn't sufficient.

### Accessing SigNoz from the Timeline

You can easily access SigNoz directly from the timeline view. In the **Traces** section, click on any activity in the conversation timeline to view its details. Within the activity details, you'll find a **"View in SigNoz"** button that takes you directly to the corresponding span in SigNoz for deeper analysis.

### What SigNoz Shows

* **Distributed traces**: End-to-end request flows across services
* **Performance metrics**: Response times, throughput, and error rates

### Key Metrics to Monitor

* **Agent response times**: How long each agent takes to process requests
* **Tool execution times**: Performance of MCP servers and external APIs
* **Error rates**: Frequency and types of failures

## Agent Stopped Unexpectedly

### StopWhen Limits Reached

If your agent stops mid-conversation, it may have hit a configured stopWhen limit:

* **Transfer limit reached**: Check `transferCountIs` on your Agent or Project - agent stops after this many transfers between Sub Agents
* **Step limit reached**: Check `stepCountIs` on your Sub Agent or Project - execution stops after this many tool calls + LLM responses

**How to diagnose:**

* Check the timeline for the last activity before stopping
* Look for messages indicating limits were reached
* Review your stopWhen configuration in Agent/Project settings

**How to fix:**

* Increase the limits if legitimate use case requires more steps/transfers
* Optimize your agent flow to use fewer transfers
* Investigate if agent is stuck in a loop (limits working as intended)

See [Configuring StopWhen](/typescript-sdk/agent-settings#configuring-stopwhen) for more details.

## Check service logs (local development)

When running `pnpm dev` from your [quickstart workspace](/quick-start/start-development), you will see an interactive terminal interface. This interface allows you to inspect the logs of each [running service](/quick-start/start-development#service-ports). You can navigate between services using the up and down arrow keys.

![Service logs in local development](/images/agents-quickstart-pnpm-dev.png)

* The `service-info` tab displays the health of each running service.
* The `manage-api` tab contains logs for all database operations. This is useful primarily for debugging issues with [`inkeep push`](/typescript-sdk/push-pull-workflows).
* The `run-api` tab contains logs for all agent execution and tool calls. This is useful for debugging issues with your agent's behavior.
* The `mcp` tab contains logs for your [custom MCP servers](/tutorials/how-to-create-mcp-servers/inkeep).
* The `dashboard` tab displays logs for the [Visual Builder](/visual-builder/overview) dashboard.

To terminate the running services, click press `q` or `esc` in the terminal.

## Common Configuration Issues

### General Configuration Issues

* **Missing environment variables**: Ensure all required env vars are set
* **Incorrect API endpoints**: Verify you're using the right URLs
* **Network connectivity**: Check firewall and proxy settings
* **Version mismatches**: Ensure all packages are compatible

### MCP Server Connection Issues

* **MCP not able to connect**:
  * Check that the MCP server is running and accessible
* **401 Unauthorized errors**:
  * Verify that credentials are properly configured and valid
* **Connection timeouts**:
  * Ensure network connectivity and firewall settings allow connections

### AI Provider Configuration Problems

* **AI Provider key not defined or invalid**:
  * Ensure you have one of these environment variables set: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_GENERATIVE_AI_API_KEY`
  * Verify the API key is valid and has sufficient credits
  * Check that the key hasn't expired or been revoked

* **GPT-5 access issues**:
  * Individual users cannot access GPT-5 as it requires organization verification
  * Use GPT-4 or other available models instead
  * Contact OpenAI support if you need GPT-5 access for your organization

### Credit and Rate Limiting Issues

* **Running out of credits**:
  * Monitor your OpenAI usage and billing
  * Set up usage alerts to prevent unexpected charges

* **Rate limiting by AI providers**:
  * Especially common with high-frequency operations like summarizers
  * Monitor your API usage patterns and adjust accordingly

### Context Fetcher Issues

* **Context fetcher timeouts**:
  * Check that external services are responding within expected timeframes


# Inkeep Agents Manage API
URL: /api-reference

undefined

***

title: Inkeep Agents Manage API
full: true
\_openapi:
toc:

* depth: 2
  title: List Projects
  url: '#list-projects'
* depth: 2
  title: Create Project
  url: '#create-project'
* depth: 2
  title: Get Project
  url: '#get-project'
* depth: 2
  title: Update Project
  url: '#update-project'
* depth: 2
  title: Delete Project
  url: '#delete-project'
* depth: 2
  title: List SubAgents
  url: '#list-subagents'
* depth: 2
  title: Create SubAgent
  url: '#create-subagent'
* depth: 2
  title: Get SubAgent
  url: '#get-subagent'
* depth: 2
  title: Delete SubAgent
  url: '#delete-subagent'
* depth: 2
  title: Update SubAgent
  url: '#update-subagent'
* depth: 2
  title: List Agent Relations
  url: '#list-agent-relations'
* depth: 2
  title: Create Agent Relation
  url: '#create-agent-relation'
* depth: 2
  title: Get Agent Relation
  url: '#get-agent-relation'
* depth: 2
  title: Delete Agent Relation
  url: '#delete-agent-relation'
* depth: 2
  title: Update Agent Relation
  url: '#update-agent-relation'
* depth: 2
  title: List Agent Agent
  url: '#list-agent-agent'
* depth: 2
  title: Create Agent Agent
  url: '#create-agent-agent'
* depth: 2
  title: Get Agent Agent
  url: '#get-agent-agent'
* depth: 2
  title: Delete Agent Agent
  url: '#delete-agent-agent'
* depth: 2
  title: Update Agent Agent
  url: '#update-agent-agent'
* depth: 2
  title: Get Related Agent Infos
  url: '#get-related-agent-infos'
* depth: 2
  title: Get Full Agent Definition
  url: '#get-full-agent-definition'
* depth: 2
  title: List SubAgent Tool Relations
  url: '#list-subagent-tool-relations'
* depth: 2
  title: Create SubAgent Tool Relation
  url: '#create-subagent-tool-relation'
* depth: 2
  title: Get SubAgent Tool Relation
  url: '#get-subagent-tool-relation'
* depth: 2
  title: Delete SubAgent Tool Relation
  url: '#delete-subagent-tool-relation'
* depth: 2
  title: Update SubAgent Tool Relation
  url: '#update-subagent-tool-relation'
* depth: 2
  title: Get SubAgents for Tool
  url: '#get-subagents-for-tool'
* depth: 2
  title: Get Artifact Components for Agent
  url: '#get-artifact-components-for-agent'
* depth: 2
  title: Get Agents Using Artifact Component
  url: '#get-agents-using-artifact-component'
* depth: 2
  title: Associate Artifact Component with Agent
  url: '#associate-artifact-component-with-agent'
* depth: 2
  title: Remove Artifact Component from Agent
  url: '#remove-artifact-component-from-agent'
* depth: 2
  title: Check if Artifact Component is Associated with Agent
  url: '#check-if-artifact-component-is-associated-with-agent'
* depth: 2
  title: Get Data Components for Agent
  url: '#get-data-components-for-agent'
* depth: 2
  title: Get Agents Using Data Component
  url: '#get-agents-using-data-component'
* depth: 2
  title: Associate Data Component with Agent
  url: '#associate-data-component-with-agent'
* depth: 2
  title: Remove Data Component from Agent
  url: '#remove-data-component-from-agent'
* depth: 2
  title: Check if Data Component is Associated with Agent
  url: '#check-if-data-component-is-associated-with-agent'
* depth: 2
  title: List Artifact Components
  url: '#list-artifact-components'
* depth: 2
  title: Create Artifact Component
  url: '#create-artifact-component'
* depth: 2
  title: Get Artifact Component
  url: '#get-artifact-component'
* depth: 2
  title: Delete Artifact Component
  url: '#delete-artifact-component'
* depth: 2
  title: Update Artifact Component
  url: '#update-artifact-component'
* depth: 2
  title: List Context Configurations
  url: '#list-context-configurations'
* depth: 2
  title: Create Context Configuration
  url: '#create-context-configuration'
* depth: 2
  title: Get Context Configuration
  url: '#get-context-configuration'
* depth: 2
  title: Delete Context Configuration
  url: '#delete-context-configuration'
* depth: 2
  title: Update Context Configuration
  url: '#update-context-configuration'
* depth: 2
  title: List Credentials
  url: '#list-credentials'
* depth: 2
  title: Create Credential
  url: '#create-credential'
* depth: 2
  title: Get Credential
  url: '#get-credential'
* depth: 2
  title: Delete Credential
  url: '#delete-credential'
* depth: 2
  title: Update Credential
  url: '#update-credential'
* depth: 2
  title: List Data Components
  url: '#list-data-components'
* depth: 2
  title: Create Data Component
  url: '#create-data-component'
* depth: 2
  title: Get Data Component
  url: '#get-data-component'
* depth: 2
  title: Delete Data Component
  url: '#delete-data-component'
* depth: 2
  title: Update Data Component
  url: '#update-data-component'
* depth: 2
  title: List External Agents
  url: '#list-external-agents'
* depth: 2
  title: Create External Agent
  url: '#create-external-agent'
* depth: 2
  title: Get External Agent
  url: '#get-external-agent'
* depth: 2
  title: Delete External Agent
  url: '#delete-external-agent'
* depth: 2
  title: Update External Agent
  url: '#update-external-agent'
* depth: 2
  title: List Function Tools
  url: '#list-function-tools'
* depth: 2
  title: Create Function Tool
  url: '#create-function-tool'
* depth: 2
  title: Get Function Tool by ID
  url: '#get-function-tool-by-id'
* depth: 2
  title: Delete Function Tool
  url: '#delete-function-tool'
* depth: 2
  title: Update Function Tool
  url: '#update-function-tool'
* depth: 2
  title: List Functions
  url: '#list-functions'
* depth: 2
  title: Create Function
  url: '#create-function'
* depth: 2
  title: Get Function by ID
  url: '#get-function-by-id'
* depth: 2
  title: Delete Function
  url: '#delete-function'
* depth: 2
  title: Update Function
  url: '#update-function'
* depth: 2
  title: List Tools
  url: '#list-tools'
* depth: 2
  title: Create Tool
  url: '#create-tool'
* depth: 2
  title: Get Tool
  url: '#get-tool'
* depth: 2
  title: Delete Tool
  url: '#delete-tool'
* depth: 2
  title: Update Tool
  url: '#update-tool'
* depth: 2
  title: List API Keys
  url: '#list-api-keys'
* depth: 2
  title: Create API Key
  url: '#create-api-key'
* depth: 2
  title: Get API Key
  url: '#get-api-key'
* depth: 2
  title: Delete API Key
  url: '#delete-api-key'
* depth: 2
  title: Update API Key
  url: '#update-api-key'
* depth: 2
  title: Create Full Agent
  url: '#create-full-agent'
* depth: 2
  title: Get Full Agent
  url: '#get-full-agent'
* depth: 2
  title: Delete Full Agent
  url: '#delete-full-agent'
* depth: 2
  title: Update Full Agent
  url: '#update-full-agent'
* depth: 2
  title: Create Full Project
  url: '#create-full-project'
* depth: 2
  title: Get Full Project
  url: '#get-full-project'
* depth: 2
  title: Delete Full Project
  url: '#delete-full-project'
* depth: 2
  title: Update Full Project
  url: '#update-full-project'
* depth: 2
  title: Initiate OAuth login for MCP tool
  url: '#initiate-oauth-login-for-mcp-tool'
* depth: 2
  title: OAuth authorization callback
  url: '#oauth-authorization-callback'
  structuredData:
  headings:
  * content: List Projects
    id: list-projects
  * content: Create Project
    id: create-project
  * content: Get Project
    id: get-project
  * content: Update Project
    id: update-project
  * content: Delete Project
    id: delete-project
  * content: List SubAgents
    id: list-subagents
  * content: Create SubAgent
    id: create-subagent
  * content: Get SubAgent
    id: get-subagent
  * content: Delete SubAgent
    id: delete-subagent
  * content: Update SubAgent
    id: update-subagent
  * content: List Agent Relations
    id: list-agent-relations
  * content: Create Agent Relation
    id: create-agent-relation
  * content: Get Agent Relation
    id: get-agent-relation
  * content: Delete Agent Relation
    id: delete-agent-relation
  * content: Update Agent Relation
    id: update-agent-relation
  * content: List Agent Agent
    id: list-agent-agent
  * content: Create Agent Agent
    id: create-agent-agent
  * content: Get Agent Agent
    id: get-agent-agent
  * content: Delete Agent Agent
    id: delete-agent-agent
  * content: Update Agent Agent
    id: update-agent-agent
  * content: Get Related Agent Infos
    id: get-related-agent-infos
  * content: Get Full Agent Definition
    id: get-full-agent-definition
  * content: List SubAgent Tool Relations
    id: list-subagent-tool-relations
  * content: Create SubAgent Tool Relation
    id: create-subagent-tool-relation
  * content: Get SubAgent Tool Relation
    id: get-subagent-tool-relation
  * content: Delete SubAgent Tool Relation
    id: delete-subagent-tool-relation
  * content: Update SubAgent Tool Relation
    id: update-subagent-tool-relation
  * content: Get SubAgents for Tool
    id: get-subagents-for-tool
  * content: Get Artifact Components for Agent
    id: get-artifact-components-for-agent
  * content: Get Agents Using Artifact Component
    id: get-agents-using-artifact-component
  * content: Associate Artifact Component with Agent
    id: associate-artifact-component-with-agent
  * content: Remove Artifact Component from Agent
    id: remove-artifact-component-from-agent
  * content: Check if Artifact Component is Associated with Agent
    id: check-if-artifact-component-is-associated-with-agent
  * content: Get Data Components for Agent
    id: get-data-components-for-agent
  * content: Get Agents Using Data Component
    id: get-agents-using-data-component
  * content: Associate Data Component with Agent
    id: associate-data-component-with-agent
  * content: Remove Data Component from Agent
    id: remove-data-component-from-agent
  * content: Check if Data Component is Associated with Agent
    id: check-if-data-component-is-associated-with-agent
  * content: List Artifact Components
    id: list-artifact-components
  * content: Create Artifact Component
    id: create-artifact-component
  * content: Get Artifact Component
    id: get-artifact-component
  * content: Delete Artifact Component
    id: delete-artifact-component
  * content: Update Artifact Component
    id: update-artifact-component
  * content: List Context Configurations
    id: list-context-configurations
  * content: Create Context Configuration
    id: create-context-configuration
  * content: Get Context Configuration
    id: get-context-configuration
  * content: Delete Context Configuration
    id: delete-context-configuration
  * content: Update Context Configuration
    id: update-context-configuration
  * content: List Credentials
    id: list-credentials
  * content: Create Credential
    id: create-credential
  * content: Get Credential
    id: get-credential
  * content: Delete Credential
    id: delete-credential
  * content: Update Credential
    id: update-credential
  * content: List Data Components
    id: list-data-components
  * content: Create Data Component
    id: create-data-component
  * content: Get Data Component
    id: get-data-component
  * content: Delete Data Component
    id: delete-data-component
  * content: Update Data Component
    id: update-data-component
  * content: List External Agents
    id: list-external-agents
  * content: Create External Agent
    id: create-external-agent
  * content: Get External Agent
    id: get-external-agent
  * content: Delete External Agent
    id: delete-external-agent
  * content: Update External Agent
    id: update-external-agent
  * content: List Function Tools
    id: list-function-tools
  * content: Create Function Tool
    id: create-function-tool
  * content: Get Function Tool by ID
    id: get-function-tool-by-id
  * content: Delete Function Tool
    id: delete-function-tool
  * content: Update Function Tool
    id: update-function-tool
  * content: List Functions
    id: list-functions
  * content: Create Function
    id: create-function
  * content: Get Function by ID
    id: get-function-by-id
  * content: Delete Function
    id: delete-function
  * content: Update Function
    id: update-function
  * content: List Tools
    id: list-tools
  * content: Create Tool
    id: create-tool
  * content: Get Tool
    id: get-tool
  * content: Delete Tool
    id: delete-tool
  * content: Update Tool
    id: update-tool
  * content: List API Keys
    id: list-api-keys
  * content: Create API Key
    id: create-api-key
  * content: Get API Key
    id: get-api-key
  * content: Delete API Key
    id: delete-api-key
  * content: Update API Key
    id: update-api-key
  * content: Create Full Agent
    id: create-full-agent
  * content: Get Full Agent
    id: get-full-agent
  * content: Delete Full Agent
    id: delete-full-agent
  * content: Update Full Agent
    id: update-full-agent
  * content: Create Full Project
    id: create-full-project
  * content: Get Full Project
    id: get-full-project
  * content: Delete Full Project
    id: delete-full-project
  * content: Update Full Project
    id: update-full-project
  * content: Initiate OAuth login for MCP tool
    id: initiate-oauth-login-for-mcp-tool
  * content: OAuth authorization callback
    id: oauth-authorization-callback
    contents:
  * content: Check if the management service is healthy
  * content: List all projects within a tenant with pagination
    heading: list-projects
  * content: Create a new project
    heading: create-project
  * content: Get a single project by ID
    heading: get-project
  * content: Update an existing project
    heading: update-project
  * content: Delete a project. Will fail if the project has existing resources.
    heading: delete-project
  * content: List all API keys for a tenant with optional pagination
    heading: list-api-keys
  * content: >-
    Create a new API key for an agent. Returns the full key (shown only
    once).
    heading: create-api-key
  * content: Get a specific API key by ID (does not return the actual key)
    heading: get-api-key
  * content: Delete an API key permanently
    heading: delete-api-key
  * content: Update an API key (currently only expiration date can be changed)
    heading: update-api-key
  * content: >-
    Create a complete agent with all agents, tools, and relationships from
    JSON definition
    heading: create-full-agent
  * content: >-
    Retrieve a complete agent definition with all agents, tools, and
    relationships
    heading: get-full-agent
  * content: >-
    Delete a complete agent and cascade to all related entities
    (relationships, not other agents/tools)
    heading: delete-full-agent
  * content: >-
    Update or create a complete agent with all agents, tools, and
    relationships from JSON definition
    heading: update-full-agent
  * content: >-
    Create a complete project with all Agents, Sub Agents, tools, and
    relationships from JSON definition
    heading: create-full-project
  * content: >-
    Retrieve a complete project definition with all Agents, Sub Agents,
    tools, and relationships
    heading: get-full-project
  * content: >-
    Delete a complete project and cascade to all related entities (Agents,
    Sub Agents, tools, relationships)
    heading: delete-full-project
  * content: >-
    Update or create a complete project with all Agents, Sub Agents,
    tools, and relationships from JSON definition
    heading: update-full-project
  * content: >-
    Detects OAuth requirements and redirects to authorization server
    (public endpoint)
    heading: initiate-oauth-login-for-mcp-tool
  * content: >-
    Handles OAuth authorization codes and completes the authentication
    flow
    heading: oauth-authorization-callback
    icon: LuDatabaseZap

***

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

REST API for the management of the Inkeep Agent Framework.

<APIPage document={"./src/lib/index.json"} operations={[{"path":"/health","method":"get"},{"path":"/tenants/{tenantId}/projects","method":"get"},{"path":"/tenants/{tenantId}/projects","method":"post"},{"path":"/tenants/{tenantId}/projects/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{id}","method":"patch"},{"path":"/tenants/{tenantId}/projects/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agents","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agents","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agents/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agents/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agents/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-relations","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-relations","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-relations/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-relations/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-relations/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agents/{subAgentId}/related","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/full","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-tool-relations","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-tool-relations","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-tool-relations/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-tool-relations/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-tool-relations/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-tool-relations/tool/{toolId}/sub-agents","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-artifact-components/agent/:subAgentId","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-artifact-components/component/:artifactComponentId/agents","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-artifact-components","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-artifact-components/agent/:subAgentId/component/:artifactComponentId","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-artifact-components/agent/:subAgentId/component/:artifactComponentId/exists","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-data-components/agent/:subAgentId","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-data-components/component/:dataComponentId/agents","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-data-components","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-data-components/agent/:subAgentId/component/:dataComponentId","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/sub-agent-data-components/agent/:subAgentId/component/:dataComponentId/exists","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/artifact-components","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/artifact-components","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/artifact-components/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/artifact-components/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/artifact-components/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/context-configs","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/context-configs","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/context-configs/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/context-configs/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/context-configs/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/credentials","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/credentials","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/credentials/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/credentials/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/credentials/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/data-components","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/data-components","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/data-components/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/data-components/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/data-components/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/external-agents","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/external-agents","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/external-agents/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/external-agents/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/external-agents/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/function-tools","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/function-tools","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/function-tools/:id","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/function-tools/:id","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agents/{agentId}/function-tools/:id","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/functions","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/functions","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/functions/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/functions/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/functions/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/tools","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/tools","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/tools/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/tools/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/tools/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/api-keys","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/api-keys","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/api-keys/{id}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/api-keys/{id}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/api-keys/{id}","method":"put"},{"path":"/tenants/{tenantId}/projects/{projectId}/agent","method":"post"},{"path":"/tenants/{tenantId}/projects/{projectId}/agent/{agentId}","method":"get"},{"path":"/tenants/{tenantId}/projects/{projectId}/agent/{agentId}","method":"delete"},{"path":"/tenants/{tenantId}/projects/{projectId}/agent/{agentId}","method":"put"},{"path":"/tenants/{tenantId}/project-full","method":"post"},{"path":"/tenants/{tenantId}/project-full/{projectId}","method":"get"},{"path":"/tenants/{tenantId}/project-full/{projectId}","method":"delete"},{"path":"/tenants/{tenantId}/project-full/{projectId}","method":"put"},{"path":"/oauth/login","method":"get"},{"path":"/oauth/callback","method":"get"}]} webhooks={[]} hasHead={true} />


# Join & Follow
URL: /community/inkeep-community

undefined

***

title: Join & Follow
icon: "LuUsers"
---------------

To get help, share ideas, and provide feedback, join our community:

<Cards>
  <Card title="Slack" icon="LuSlack" href="https://inkeep-ai.slack.com/ssb/redirect">
    Get support, share ideas, and connect with other builders.
  </Card>
</Cards>

You can also find us on:

<Cards>
  <Card title="𝕏 (Twitter)" icon="LuTwitter" href="https://x.com/inkeep">
    Updates, tips, and shout‑outs for builders.
  </Card>

  <Card title="GitHub" icon="LuGithub" href="https://github.com/inkeep/agents">
    Star the repo, open issues, and contribute.
  </Card>

  <Card title="YouTube" icon="LuYoutube" href="https://www.youtube.com/@inkeep-ai">
    Practical demos, tutorials, and deep dives.
  </Card>

  <Card title="LinkedIn" icon="LuLinkedin" href="https://www.linkedin.com/company/inkeep/">
    Company updates, launches, and hiring news.
  </Card>
</Cards>

Feel free to tag us as `@inkeep` on 𝕏 or `@Inkeep` on LinkedIn with a video of what you're building — we like to highlight neat Agent use cases from the community where possible. Also feel free to submit a PR to our [template library](https://github.com/inkeep/agents/tree/main/agents-cookbook/template-projects).

To keep up to date with all news related to AI Agents, sign up for the Agents Newsletter:

<Cards>
  <Card title="Agents Newsletter" icon="LuMail" href="https://inkeep.com/agents-newsletter">
    Get the latest AI Agents news, tips, and updates delivered to your inbox.
  </Card>
</Cards>


# License
URL: /community/license

License for the Inkeep Agent Framework

***

title: License
description: License for the Inkeep Agent Framework
icon: "LuFileText"
------------------

The Inkeep Agent Framework is licensed under the **Elastic License 2.0** ([ELv2](https://www.elastic.co/licensing/elastic-license)) subject to **Inkeep's Supplemental Terms** ([SUPPLEMENTAL\_TERMS.md](https://github.com/inkeep/agents/blob/main/SUPPLEMENTAL_TERMS.md)). This is a [fair-code](https://faircode.io/), source-available license that allows broad usage while protecting against certain competitive uses.


# Push / Pull
URL: /get-started/push-pull

Push and pull your agents to and from the Visual Builder

***

title: Push / Pull
description: Push and pull your agents to and from the Visual Builder
icon: "LuArrowLeftRight"
------------------------

## Push code to visual

With Inkeep, you can define your agents in code, push them to the Visual Builder, and continue developing with the intuitive drag-and-drop interface. You can switch back to code any time.

Let's walk through the process.

<Video src="https://www.youtube.com/watch?v=2-j4LuabeHQ&t=3s" title="Using Inkeep push" />

### Step 1: Install the Inkeep CLI

```bash
pnpm install -g @inkeep/agents-cli
```

### Step 2: Download a template project

Navigate to the `src/projects` directory.

```bash
cd src/projects
```

Add the docs assistant agent using `inkeep add`.

```bash
inkeep add --project docs-assistant
```

Find the downloaded code in `src/projects/docs-assistant`.

<Note>
  `inkeep add` imports a template project from our [cookbook library](https://github.com/inkeep/agents/tree/main/agents-cookbook/template-projects) into your src/projects directory.
</Note>

### Step 3: Push code to visual

Navigate to your docs assistant project.

```bash
cd docs-assistant
```

Use `inkeep push` to push the code to the Visual Builder.

```bash
inkeep push
```

### Step 4: Chat with your agent

Refresh [http://localhost:3000](http://localhost:3000), switch to the **Docs Assistant** project (in the bottom left).

Under **Agents**, click on the Docs Assistant agent and press **Try it**. Ask a question about Inkeep.

<Image src="/gifs/docs-assistant.gif" alt="Chat with your agent" />

## Run `inkeep pull`

Make some changes, like changing a prompt, and let's walk through `inkeep pull`.

### Requirements

The `inkeep pull` command in-part leverages AI to sync your TypeScript files to the state of your Visual Builder, so **at least one** of the below environment variables to be defined:

```txt .env
# Choose one:
ANTHROPIC_API_KEY=your_api_key_here
# or
OPENAI_API_KEY=your_api_key_here
# or
GOOGLE_GENERATIVE_AI_API_KEY=your_api_key_here
```

The CLI prioritizes Anthropic → OpenAI → Google.

Here are the models used:

| Provider  | Model(s)                              | Where to Get API Key                                |
| --------- | ------------------------------------- | --------------------------------------------------- |
| Anthropic | Claude Sonnet 4.5 (extended thinking) | [Anthropic Console](https://console.anthropic.com/) |
| OpenAI    | GPT-5.1                               | [OpenAI Platform](https://platform.openai.com/)     |
| Google    | Gemini 2.5 Flash                      | [Google AI Studio](https://ai.google.dev/)          |

### Step 1: Make an edit visually

Make an edit to the docs assistant agent in the UI, such as changing the prompt of the agent.

### Step 2: Pull code from visual

Navigate to your docs assistant project.

```bash
cd src/projects/docs-assistant
```

Use `inkeep pull` to pull the code from the Visual Builder to your local project.

```bash
inkeep pull
```

### Step 3: Verify the code was pulled

Check the `src/projects/docs-assistant/agents/docs-assistant.ts` file for the updated prompt.

```bash
cat src/projects/docs-assistant/agents/docs-assistant.ts
```

## Next steps

Next, we recommend setting up observability to see live traces of your agent. See [Traces](/get-started/traces) to get started.

<Cards>
  <Card title="Traces" icon="LuActivity" href="/get-started/traces">
    Set up SigNoz to enable live debugging capabilities for your agents
  </Card>
</Cards>


# Quick Start
URL: /get-started/quick-start

Get started with Inkeep Agents in &lt;1min

***

title: Quick Start
description: Get started with Inkeep Agents in \<1min
icon: "LuRocket"
----------------

## Launch your first agent

### Prerequisites

Before getting started, ensure you have the following installed on your system:

* [Node.js](https://nodejs.org/en/download/) version 22 or higher
* [Docker](https://docs.docker.com/get-docker/)
* [pnpm](https://pnpm.io/installation) version 10 or higher

You can verify by running:

```bash
node --version
pnpm --version
docker --version
```

### Step 1: Create a new agents project

Run the quickstart script on a target folder:

```bash
npx @inkeep/create-agents my-agents
```

Navigate to the folder

```bash
cd my-agents
```

Open the folder using your favorite coding editor. To open with Cursor, you can run `cursor .`

### Step 2: Run the setup script

Ensure Docker Desktop (or Docker daemon) is running before running the setup script.

```bash
pnpm setup-dev
```

### Step 3: Launch the dev environment

```bash
pnpm dev
```

The Visual Builder will auto-open at [http://localhost:3000](http://localhost:3000).

### Step 4: Chat with your agent

Navigate to the **Activities Planner** agent at [http://localhost:3000](http://localhost:3000), click **Try it**, and ask about fun activities at a location of your choice:

<Image src="/gifs/activities-planner.gif" alt="Chat with your agent" />

### Step 5: Install Inkeep MCP (optional)

To help "vibe code" agents with Inkeep, add the `Inkeep Agents MCP` to your preferred IDE.

<div
  style={{
  display: "flex",
  flexDirection: "row",
  alignItems: "center",
  gap: "16px",
}}
>
  <a href="cursor://anysphere.cursor-deeplink/mcp/install?name=inkeep-agents&config=eyJ1cmwiOiJodHRwczovL2FnZW50cy5pbmtlZXAuY29tL21jcCJ9">
    <Image src="https://cursor.com/deeplink/mcp-install-dark.png" alt="Add to Cursor" style={{ height: "32px", verticalAlign: "middle" }} />
  </a>

  <a href="vscode:mcp/install?%7B%22name%22%3A%22inkeep-agents-mcp%22%2C%22type%22%3A%22sse%22%2C%22url%22%3A%22https%3A%2F%2Fagents.inkeep.com%2Fmcp%22%7D">
    <Image src="https://img.shields.io/badge/VS_Code-Install_Inkeep_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=ffffff" alt="Install in VS Code" style={{ height: "22px", verticalAlign: "middle" }} />
  </a>
</div>

To add to **Claude Code**, run this in your terminal:

```bash
claude mcp add --transport http inkeep-agents https://agents.inkeep.com/mcp --scope project
```

Or manually add `https://agents.inkeep.com/mcp` as an MCP Server to any MCP client.

### Next steps

Next, we recommend learning about `inkeep push` and `inkeep pull` so you can go from `SDK -> Visual Builder` and `Visual Builder -> SDK`. See the [Push / Pull](/get-started/push-pull) guide for a quick example.

<Cards>
  <Card title="Push / Pull" icon="LuArrowLeftRight" href="/get-started/push-pull">
    Use our cookbook to learn about push and pull.
  </Card>
</Cards>


# Live Debugger, Traces, and OTEL Telemetry
URL: /get-started/traces

Set up SigNoz to enable full observability with traces and live debugging capabilities for your agents.

***

title: Live Debugger, Traces, and OTEL Telemetry
sidebarTitle: Traces
description: Set up SigNoz to enable full observability with traces and live debugging capabilities for your agents.
icon: "LuActivity"
keywords: SigNoz, traces, live debugger, observability, OpenTelemetry, monitoring, distributed tracing, debugging, copy trace, export trace, JSON export
--------------------------------------------------------------------------------------------------------------------------------------------------------

## Overview

The Inkeep Agent Framework provides powerful **traces** and **live debugging** capabilities powered by SigNoz. Setting up SigNoz gives you:

* **Real-time trace visualization** - See exactly how your agents execute step-by-step
* **Live debugging** - Debug agent conversations as they happen
* **Export traces as JSON** - Copy complete traces for offline analysis and debugging
* **Full observability** - Complete OpenTelemetry instrumentation for monitoring
* **Performance insights** - Identify bottlenecks and optimize agent performance

<Image src="/images/live-traces.png" alt="Live traces interface showing real-time agent execution" />

## Setup Options

You can set up SigNoz in two ways:

1. **Cloud Setup**: Use SigNoz Cloud
2. **Local Setup**: Run SigNoz locally using Docker

## Option 1: SigNoz Cloud Setup

<Video src="https://www.youtube.com/watch?v=F8n6427hjUE&t=3s" title="SigNoz Cloud Setup steps" />

### Step 1: Create a SigNoz Cloud Project

1. Sign up at [SigNoz](https://signoz.io/teams/)
2. Create a new project or use an existing one

### Step 2: Save Your SigNoz Credentials

You'll need to collect three pieces of information from your SigNoz dashboard:

1. **API Key**:

   * Navigate to Settings → Workspace Settings → API Keys → New Key
   * Choose any role (Admin, Editor, or Viewer) - Viewer is sufficient for observability
   * Set the expiration field to "No Expiry" to prevent the key from expiring
   * Copy the generated API key

2. **Ingestion Key**:

   * Navigate to Settings → Workspace Settings → Ingestion
   * Set the expiration field to "No Expiry" to prevent the key from expiring
   * Copy the ingestion key

3. **SigNoz URL**:
   * Copy the URL from your browser's address bar
   * It will look like: `https://<your-organization>.signoz.cloud`

### Step 3: Configure Your Root `.env` File

```bash
# SigNoz
SIGNOZ_URL=https://<your-organization>.signoz.cloud
SIGNOZ_API_KEY=<your-api-key>

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://ingest.us.signoz.cloud:443/v1/traces
OTEL_EXPORTER_OTLP_TRACES_HEADERS="signoz-ingestion-key=<your-ingestion-key>"
```

### Step 4: Verify Cloud Setup

1. Restart your development environment:

   ```bash
   pnpm dev
   ```

2. Generate some traces by interacting with your agents

3. Open your SigNoz cloud dashboard and navigate to "Traces" to see your agent traces

## Option 2: Local SigNoz Setup

<Video src="https://www.youtube.com/watch?v=DWuL4AeRzAA&t=3s" title="Local SigNoz Setup steps" />

### Prerequisites

* Docker installed on your machine

### Step 1: Clone the Optional Services Repository

Clone the Inkeep optional local development services repository:

```bash
git clone https://github.com/inkeep/agents-optional-local-dev
cd agents-optional-local-dev
```

### Step 2: Start SigNoz Services

Run the following command to start SigNoz and related services:

```bash
docker-compose --profile signoz up -d
```

This will start:

* SigNoz frontend (accessible at `http://localhost:3080`)
* SigNoz query service
* SigNoz OTEL collector
* ClickHouse database

When you visit `http://localhost:3080`, you can sign up with your desired credentials.

### Step 3: Configure Environment Variables

In your **root project directory** (e.g., `my-agents`), update your `.env` file:

```bash
# SigNoz Configuration
SIGNOZ_URL=http://localhost:3080
SIGNOZ_API_KEY=your-signoz-api-key

# IMPORTANT: Comment out the OTEL Configuration
# OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://ingest.us.signoz.cloud:443/v1/traces
# OTEL_EXPORTER_OTLP_TRACES_HEADERS="signoz-ingestion-key=<your-ingestion-key>"
```

To get your SigNoz API key:

1. Open SigNoz at `http://localhost:3080`
2. Navigate to Settings → Account Settings → API Keys → New Key
3. Create a new API key or copy an existing one.
   * Choose any role (Admin, Editor, or Viewer) - Viewer is sufficient for observability
   * Set the expiration field to "No Expiry" to prevent the key from expiring

### Step 4: Verify Setup

1. Restart your Inkeep agents:

   ```bash
   pnpm dev
   ```

2. Make some requests to your agents to generate traces

3. Open SigNoz at `http://localhost:3080` and navigate to the "Traces" section to see your agent traces

## Viewing Traces and Using the Live Debugger

Once SigNoz is set up, you can access traces and live debugging in two ways:

### 1. Visual Builder Traces Interface

If you're using the Visual Builder:

1. Open your agent project in the Visual Builder
2. Navigate to the **Traces** section
3. You'll see real-time traces of your agent executions
4. Click on any trace to see detailed execution flow and timing

The traces overview shows conversation metrics and recent activity:

<Image src="/images/trace-overview.png" alt="Traces overview dashboard showing conversation metrics and recent activity" />

Click on any conversation to see detailed execution flow:

<Image src="/images/trace-detail.png" alt="Detailed conversation trace showing step-by-step execution and timing" />

<>
  ### Copy Trace for Debugging

  The `Copy Trace` button in the timeline view allows you to export the entire conversation trace as JSON. This is particularly useful for offline analysis and debugging complex flows.

  <Image src="/images/copy-trace.png" alt="Copy Trace button in the timeline view for exporting conversation traces" />

  #### What's Included in the Trace Export

  When you click `Copy Trace`, the system exports a JSON object containing:

  ```json
  {
    "metadata": {
      "conversationId": "unique-conversation-id",
      "traceId": "distributed-trace-id",
      "agentId": "agent-identifier",
      "agentName": "Agent Name",
      "exportedAt": "2025-10-14T12:00:00.000Z"
    },
    "timing": {
      "startTime": "2025-10-14T11:59:00.000Z",
      "endTime": "2025-10-14T12:00:00.000Z",
      "durationMs": 60000
    },
    "timeline": [
      // Array of all activities with complete details:
      // - Agent messages and responses
      // - Tool calls and results
      // - Agent transfers
      // - Artifact information
      // - Execution context
    ]
  }
  ```

  #### How to Use Copy Trace

  1. Navigate to the **Traces** section in the management UI
  2. Open the conversation you want to debug
  3. Click the **Copy Trace** button at the top of the timeline
  4. The complete trace JSON is copied to your clipboard
  5. Paste it into your preferred tool for analysis

  This exported trace contains all the activities shown in the timeline, making it easy to share complete execution context with team members or support.
</>

### 2. SigNoz Dashboard

For detailed analysis and further debugging:

1. Open your SigNoz dashboard (cloud or local)
2. Navigate to **Traces** to see all agent executions
3. Use filters to find specific conversations or agents
4. Click on traces to see:
   * Step-by-step execution details
   * Performance metrics
   * Error information
   * Agent-to-agent communication flows

For more detailed information on using traces, see the [SigNoz Usage guide](/typescript-sdk/signoz-usage).

## Additional Observability and Evals

👉 For additional observability or a dedicated Evals platform, you can connect to any OTEL-based provider. For example, check out the [Langfuse Usage guide](/typescript-sdk/langfuse-usage) for end-to-end instructions.

## Next steps

Next, we recommend setting up the Nango credential store for production-ready credential management. See [Credentials](/typescript-sdk/credentials/overview) to get started.


# Quick Start
URL: /quick-start/start-development

Start developing your agents with the Inkeep Agent Platform

***

title: Quick Start
description: Start developing your agents with the Inkeep Agent Platform
icon: "LuRocket"
----------------

### Prerequisites

* Node.js 22+
* Docker (installation instructions [here](https://docs.docker.com/engine/install))
* pnpm 10+ (installation instructions [here](https://pnpm.io/installation))

### Step 1: Create a new agents project

```bash
npx @inkeep/create-agents my-agents 
cd my-agents
```

### Step 2: Run the setup script

```bash
pnpm setup-dev
```

### Step 3: Launch the development environment

```bash
pnpm dev
```

The Visual Builder will open automatically at [http://localhost:3000](http://localhost:3000).

#### Service Ports

The development environment starts multiple services on different ports:

| Service            | Port | URL                                            | Description                                            |
| ------------------ | ---- | ---------------------------------------------- | ------------------------------------------------------ |
| **Visual Builder** | 3000 | [http://localhost:3000](http://localhost:3000) | Web interface for building and managing agents         |
| **Manage API**     | 3002 | [http://localhost:3002](http://localhost:3002) | API for managing agent configurations and projects     |
| **Run API**        | 3003 | [http://localhost:3003](http://localhost:3003) | API for executing agent conversations with your agents |

<Note>
  Make sure these ports are available before starting the development environment. If any port is in use, you'll need to free it up first.
</Note>

### Step 3: Install the Inkeep CLI

```bash
npm install -g @inkeep/agents-cli
```

### Step 4: Push your project

Running this command will push the code you defined your agents and tools with to the Visual Builder.

```bash
cd src/weather-project
inkeep push
```

### Step 5: Chat with your agent

Open the Visual Builder at [http://localhost:3000](http://localhost:3000), click into the weather graph, and then click the "Try It" button to start chatting with the agent.

Next, we recommend setting up observability to see live traces of your agent. See [Traces](/quick-start/traces) for more information.


# Deploy to AWS EC2
URL: /self-hosting/aws-ec2

Deploy to AWS EC2 with Docker Compose

***

title: Deploy to AWS EC2
sidebarTitle: AWS EC2
description: Deploy to AWS EC2 with Docker Compose
icon: "LuServerCog"
-------------------

## Create a VM Instance

* Go to [Compute Engine](https://console.aws.amazon.com/ec2/v2/home).
* Launch an instance
* Select Amazon Machine Image (AMI)
* Recommended size is at least `t2.large` (2 vCPU, 8 GiB Memory).
* Click "Edit" in the "Network settings" section. Set up an Inbound Security Group Rules for (TCP, 3000, 0.0.0.0/0), (TCP, 3002-3003, 0.0.0.0/0), (TCP, 3050-3051, 0.0.0.0/0), and (TCP, 3080, 0.0.0.0/0). These are the ports exposed by the Inkeep services.
* Auto-assign public IP
* Increase the size of storage to 30 GiB.

## Install Docker Compose

1. SSH into the EC2 Instance

2. Install packages

```bash
sudo dnf update
sudo dnf install -y git
sudo dnf install -y docker
```

```bash
sudo mkdir -p /usr/libexec/docker/cli-plugins
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-$(uname -m) -o /usr/libexec/docker/cli-plugins/docker-compose
sudo chmod +x /usr/libexec/docker/cli-plugins/docker-compose
```

## Deploy SigNoz and Nango

Clone this repo, which includes Docker files with SigNoz and Nango:

```bash
git clone https://github.com/inkeep/agents-optional-local-dev inkeep-external-services
cd inkeep-external-services
```

Run this command to autogenerate a `.env` file:

```bash
cp .env.example .env && \
  encryption_key=$(openssl rand -base64 32) && \
  tmp_file=$(mktemp) && \
  sed "s|<REPLACE_WITH_BASE64_256BIT_ENCRYPTION_KEY>|$encryption_key|" .env > "$tmp_file" && \
  mv "$tmp_file" .env && \
  echo "Docker environment file created with auto-generated encryption key"
```

Nango requires a `NANGO_ENCRYPTION_KEY`. Once you create this, it cannot be edited.

Here's an overview of the important environment variables when deploying to production. Make sure to replace all of these in the `.env` file.

```bash
NANGO_ENCRYPTION_KEY=<nango_encryption_key>

# Replace these with your <vm_external_ip> in production!
NANGO_SERVER_URL=http://<vm_external_ip>:3050
NANGO_PUBLIC_CONNECT_URL=http://<vm_external_ip>:3051

# Modify these in production environments!
NANGO_DASHBOARD_USERNAME=admin@example.com
NANGO_DASHBOARD_PASSWORD=adminADMIN!@12
```

Build and deploy SigNoz, Nango, OTEL Collector, and Jaeger:

```bash
docker compose up -d
```

This may take up to 5 minutes to start.

### Retrieve your SigNoz and Nango API Keys

To get your SigNoz API key `SIGNOZ_API_KEY`:

* Open SigNoz in a browser at `http://<vm_external_ip>:3080`
* Navigate to Settings → Account Settings → API Keys → New Key
* Choose a role, Viewer is sufficient for observability
* Set the expiration field to "No Expiry" to prevent the key from expiring

To get your Nango secret key `NANGO_SECRET_KEY`:

* Open Nango in a browser at `http://<vm_external_ip>:3050`
* Nango auto-creates two environments, Prod and Dev. Select the one you will use.
* Navigate to Environment Settings to find the secret key

## Deploy the Inkeep Agent Framework

From the root directory, create a new project directory for the Docker Compose setup for the Inkeep Agent Framework

```bash
mkdir inkeep && cd inkeep
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/docker-compose.yml
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/.env.docker.example
```

Generate a `.env` file from the example:

```bash
cp .env.docker.example .env
```

Here's an overview of the important environment variables when deploying to production. Make sure to replace all of these in the `.env` file.

```bash
# Change to "production" if deploying to production
ENVIRONMENT=production

# AI Provider Keys (you need at least one)
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GOOGLE_GENERATIVE_AI_API_KEY=

# Nango
NANGO_SECRET_KEY=

# SigNoz
SIGNOZ_API_KEY=

# Uncomment and set each of these with (openssl rand -hex 32)
INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET=
INKEEP_AGENTS_RUN_API_BYPASS_SECRET=
INKEEP_AGENTS_JWT_SIGNING_SECRET=

# Uncomment and set these for the Manage UI at http://<vm_external_ip>:3000
PUBLIC_INKEEP_AGENTS_MANAGE_API_URL=http://<vm_external_ip>:3002
PUBLIC_INKEEP_AGENTS_RUN_API_URL=http://<vm_external_ip>:3003
PUBLIC_INKEEP_AGENTS_RUN_API_BYPASS_SECRET=<copy INKEEP_AGENTS_RUN_API_BYPASS_SECRET>
PUBLIC_NANGO_SERVER_URL=http://<vm_external_ip>:3050
PUBLIC_NANGO_CONNECT_BASE_URL=http://<vm_external_ip>:3051
PUBLIC_SIGNOZ_URL=http://<vm_external_ip>:3080

# Uncomment and set these to access Manage UI at http://<vm_external_ip>:3000
INKEEP_AGENTS_MANAGE_UI_USERNAME=admin@example.com
INKEEP_AGENTS_MANAGE_UI_PASSWORD=adminADMIN!@12
```

<>
  :::tip Advanced Configuration

  For long-running agents or custom deployment requirements, you can override runtime limits like execution timeouts, maximum transfers, and generation steps. See [Configure Runtime Limits](/docs/self-hosting/configure-runtime-limits) for examples and the complete list of overridable settings.

  :::
</>

Run with Docker:

```bash
docker compose up -d
```

Then open `http://<vm_external_ip>:3000` in a browser!


# Configure Runtime Limits
URL: /self-hosting/configure-runtime-limits

Customize execution limits, timeouts, and constraints for your deployment

***

title: Configure Runtime Limits
description: Customize execution limits, timeouts, and constraints for your deployment
icon: "LuSettings2"
-------------------

# Configure Runtime Limits

## Overview

The Inkeep Agent Framework includes sensible defaults for execution limits, timeouts, and constraints. However, certain use cases—like long-running orchestration agents—may require different configurations.

## How Runtime Configuration Works

### Two Types of Limits

**1. API-Configurable Limits** (set per agent/sub-agent via manage-api)

* Configured in your agent definitions using `stopWhen`
* Controls agent-specific behavior
* See [Agent Settings - StopWhen](/docs/typescript-sdk/agent-settings#configuring-stopwhen)

**2. Runtime Environment Limits** (set via environment variables)

* System-wide defaults and maximum allowed values
* Controls infrastructure-level constraints
* Documented in this guide

### Configuration Hierarchy

When an agent executes:

1. Uses agent-specific `stopWhen` settings if configured
2. Falls back to runtime environment defaults
3. Cannot exceed runtime environment maximums

### Understanding the Constants Architecture

The runtime environment limits are defined as TypeScript constants in the `@inkeep/agents-core` package. These constants are organized into two categories based on their purpose:

**1. Schema Validation Constants** (`packages/agents-core/src/constants/schema-validation/defaults.ts`)

* Define **API-level validation limits** (min, max, default values)
* Control what values users can configure via the manage-api
* Used in Zod schemas to validate agent configuration requests
* Examples: Transfer count limits, generation step limits, prompt character limits

**2. Runtime Execution Constants - Shared** (`packages/agents-core/src/constants/execution-limits-shared/defaults.ts`)

* Define **internal runtime behavior** limits
* Control infrastructure-level timeouts, retries, and constraints
* Shared across both manage-api and run-api services
* Examples: MCP connection timeouts, conversation history token limits

**3. Runtime Execution Constants - Run-API** (`packages/agents-run-api/src/constants/execution-limits/defaults.ts`)

* Define **run-api specific runtime behavior** limits
* Control execution engine timeouts, retries, and resource constraints
* Only used by the run-api service (not shared with manage-api)
* Examples: LLM generation timeouts, function tool sandbox limits, streaming buffer sizes

Each constant includes detailed inline documentation explaining its purpose, behavior, and impact on the runtime. **The TypeScript constant files are the source of truth** for default values and available overrides—not `.env.example`.

All constants can be overridden via environment variables prefixed with `AGENTS_`. For example:

```bash
# Override a schema validation constant
AGENTS_AGENT_EXECUTION_TRANSFER_COUNT_DEFAULT=50

# Override a runtime execution constant
AGENTS_MCP_TOOL_CONNECTION_TIMEOUT_MS=5000
```

## Use Case: Long-Running Orchestration Agents

For agents that orchestrate complex workflows (like coding agents that run for hours), you'll want to increase various limits and timeouts.

### Recommended Configuration

Add these to your `.env` file:

```bash
# Agent Execution - Allow more sub-agent transfers for complex orchestration
AGENTS_EXECUTION_TRANSFER_COUNT_DEFAULT=50  # Default: 10
AGENTS_EXECUTION_TRANSFER_COUNT_MAX=2000    # Default: 1000

# Sub-Agent Turns - Allow more LLM generation steps per turn
AGENTS_SUB_AGENT_TURN_GENERATION_STEPS_DEFAULT=30  # Default: 12
AGENTS_SUB_AGENT_TURN_GENERATION_STEPS_MAX=2000    # Default: 1000

# LLM Timeouts - Increase for longer-running operations
AGENTS_LLM_GENERATION_FIRST_CALL_TIMEOUT_MS_STREAMING=600000   # 10min, Default: 4.5min
AGENTS_LLM_GENERATION_SUBSEQUENT_CALL_TIMEOUT_MS=180000        # 3min, Default: 1.5min

# Function Tools - Allow longer execution for complex operations
AGENTS_FUNCTION_TOOL_EXECUTION_TIMEOUT_MS_DEFAULT=120000  # 2min, Default: 30sec

# MCP Tools - Increase timeout for external tool operations
AGENTS_MCP_TOOL_REQUEST_TIMEOUT_MS_DEFAULT=180000  # 3min, Default: 1min

# Session Management - Keep tool results cached longer
AGENTS_SESSION_TOOL_RESULT_CACHE_TIMEOUT_MS=1800000  # 30min, Default: 5min

# Streaming - Allow streams to run longer
AGENTS_STREAM_MAX_LIFETIME_MS=1800000  # 30min, Default: 10min
```

### Why These Settings?

* **Transfer Count**: Coding orchestration often involves many handoffs between specialist agents (planning → implementation → testing → refinement)
* **Generation Steps**: Each coding operation may require multiple tool calls (read files, analyze, write code, run tests)
* **Timeouts**: Code generation and analysis can take time, especially for large files or complex refactoring
* **Cache Duration**: Keeps tool results available throughout long sessions for artifact processing

## Setting Variables by Deployment Type

### Local Development (Docker Compose)

```bash
# Edit .env file
vim .env

# Add your overrides
AGENTS_EXECUTION_TRANSFER_COUNT_DEFAULT=50
# ... other settings

# Restart services
docker compose down && docker compose up -d
```

### Production Deployments

#### AWS EC2, GCP, Hetzner

Add variables to your `.env` file before running `docker compose up`:

```bash
cp .env.docker.example .env
# Edit .env with your overrides
vim .env
docker compose up -d
```

#### Vercel, Cloud Run, etc.

Set environment variables in your platform's environment configuration UI.

## All Available Configuration Variables

All runtime configuration variables are defined as TypeScript constants. To explore available overrides and their detailed documentation:

1. **View the constant files** (source of truth):
   * Schema validation constants: `packages/agents-core/src/constants/schema-validation/defaults.ts`
   * Runtime execution constants (shared): `packages/agents-core/src/constants/execution-limits-shared/defaults.ts`
   * Runtime execution constants (run-api): `packages/agents-run-api/src/constants/execution-limits/defaults.ts`
2. Each constant includes inline documentation explaining its purpose, behavior, and impact
3. Convert constant names to environment variables by prefixing with `AGENTS_`

### Configuration Categories

The runtime configuration is organized into functional categories:

**Schema Validation Constants** (API-level limits):

* **Agent Execution Transfer Count**: Limits transfers between sub-agents in a turn
* **Sub-Agent Turn Generation Steps**: LLM generation steps within a single sub-agent activation
* **Status Update Thresholds**: Event and time-based triggers for status updates
* **Prompt Validation**: Character limits for agent and sub-agent system prompts
* **Context Fetchers**: HTTP timeouts for external data fetching (CRM lookups, API calls)

**Runtime Execution Constants - Shared** (infrastructure-level limits):

* **MCP Tool Connection & Retry**: Connection timeouts and exponential backoff for MCP tools
* **Conversation History**: Token limits for conversation context windows

**Runtime Execution Constants - Run-API** (run-api service-specific limits):

* **LLM Generation Timeouts**: Timeout behavior for AI model calls
* **Function Tool Sandbox**: Execution limits for function tools in isolated sandboxes
* **Delegation & A2A**: Inter-agent communication settings
* **Artifact Processing**: UI component generation with retry mechanisms
* **Session Management**: Tool result caching and cleanup
* **Streaming**: Frequency, batching, and lifetime limits for streams

## Related Documentation

* [Agent Settings - StopWhen](/docs/typescript-sdk/agent-settings#configuring-stopwhen) - Configure per-agent limits
* [Environment Configuration](/docs/community/contributing/environment-configuration) - Development environment setup
* [Configuration Management](/docs/typescript-sdk/configuration) - Workspace configuration


# Build a Custom Docker Image
URL: /self-hosting/docker-build

How to build your own Docker images

***

title: Build a Custom Docker Image
sidebarTitle: Custom Image
description: How to build your own Docker images
icon: "LuWrench"
----------------

If you created a project from the quick start, the template includes a set of Dockerfiles and `docker-compose.yml` files.

To build and run locally:

```
docker compose build
docker compose up -d
```


# Deploy using Docker (Local Development)
URL: /self-hosting/docker-local

undefined

***

title: Deploy using Docker (Local Development)
sidebarTitle: Local Development
icon: "LuLaptop"
----------------

## Install Docker

* [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Deploy SigNoz and Nango

For full functionality, the **Inkeep Agent Framework** requires [**SigNoz**](https://signoz.io/) and [**Nango**](https://www.nango.dev/). You can sign up for a cloud hosted account with them directly, or you can self host them. Follow these instructions to self-host both SigNoz and Nango.

Clone this repo, which includes docker files with SigNoz and Nango:

```bash
git clone https://github.com/inkeep/agents-optional-local-dev inkeep-external-services
cd inkeep-external-services
```

Run this command to autogenerate a `.env` file:

```bash
cp .env.example .env && \
  encryption_key=$(openssl rand -base64 32) && \
  tmp_file=$(mktemp) && \
  sed "s|<REPLACE_WITH_BASE64_256BIT_ENCRYPTION_KEY>|$encryption_key|" .env > "$tmp_file" && \
  mv "$tmp_file" .env && \
  echo "Docker environment file created with auto-generated encryption key"
```

Nango requires a `NANGO_ENCRYPTION_KEY`. Once you create this, it cannot be edited.

Build and deploy SigNoz, Nango, OTEL Collector, and Jaeger:

```bash
docker compose up -d
```

This may take up to 5 minutes to start.

### Retrieve your SigNoz and Nango API Keys

To get your SigNoz API key `SIGNOZ_API_KEY`:

* Open SigNoz in a browser at `http://localhost:3080`
* Navigate to Settings → Account Settings → API Keys → New Key
* Choose a role, Viewer is sufficient for observability
* Set the expiration field to "No Expiry" to prevent the key from expiring

To get your Nango secret key `NANGO_SECRET_KEY`:

* Open Nango in a browser at `http://localhost:3050`
* Nango autocreates two environments Prod and Dev, select the one you will use
* Navigate to Environment Settings to find the secret key

## Deploy the Inkeep Agent Framework

From the root directory, create a new project directory for the docker compose setup for Inkeep Agent Framework

```bash
mkdir inkeep && cd inkeep
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/docker-compose.yml
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/.env.docker.example
```

Generate a `.env` file from the example:

```bash
cp .env.docker.example .env
```

Here's an overview of the important environment variables when deploying. Make sure to replace all of these in the `.env` file.

```bash
ENVIRONMENT=development

# AI Provider Keys (you need at least one)
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GOOGLE_GENERATIVE_AI_API_KEY=

# Nango
NANGO_SECRET_KEY=

# SigNoz
SIGNOZ_API_KEY=

# Default username and password for Manage UI (http://localhost:3000)
# INKEEP_AGENTS_MANAGE_UI_USERNAME=admin@example.com
# INKEEP_AGENTS_MANAGE_UI_PASSWORD=adminADMIN!@12
```

<>
  :::tip Advanced Configuration

  For long-running agents or custom deployment requirements, you can override runtime limits like execution timeouts, maximum transfers, and generation steps. See [Configure Runtime Limits](/docs/self-hosting/configure-runtime-limits) for examples and the complete list of overridable settings.

  :::
</>

Run with docker:

```bash
docker compose up -d
```

Then open [http://localhost:3000](http://localhost:3000) in a browser!

* Manage UI ([http://localhost:3000](http://localhost:3000))
* Manage API Docs ([http://localhost:3002/docs](http://localhost:3002/docs))
* Run API Docs ([http://localhost:3003/docs](http://localhost:3003/docs))
* Nango Dashboard ([http://localhost:3050](http://localhost:3050))
* SigNoz Dashboard ([http://localhost:3080](http://localhost:3080))


# Deploy to GCP Cloud Run
URL: /self-hosting/gcp-cloud-run

Deploy to GCP Cloud Run with Docker Containers

***

title: Deploy to GCP Cloud Run
sidebarTitle: GCP Cloud Run
description: Deploy to GCP Cloud Run with Docker Containers
icon: "LuCloudLightning"
------------------------

## Coming soon


# Deploy to GCP Compute Engine
URL: /self-hosting/gcp-compute-engine

Deploy to GCP Compute Engine with Docker Compose

***

title: Deploy to GCP Compute Engine
sidebarTitle: GCP Compute Engine
description: Deploy to GCP Compute Engine with Docker Compose
icon: "LuCloudSun"
------------------

## Create a VM Instance

* Go to [Compute Engine](https://console.cloud.google.com/compute/instances) in your GCP project.
* Create an instance; a recommended size is at least `e2-standard-2` (2 vCPU, 1 core, 8 GB memory).
* Use Debian GNU/Linux 12 (bookworm)
* Increase the size of the boot disk to 30 GB.
* Allow HTTP traffic.
* Allow ingress traffic from source IPv4 ranges `0.0.0.0/0` to TCP ports: `3000, 3002, 3003, 3050, 3051, 3080`. These are the ports exposed by the Inkeep services.
* Retrieve an external IP address (if applicable, set up a static IP or set up a load balancer).

## Install Docker Compose

1. [SSH into the VM](https://cloud.google.com/compute/docs/connect/standard-ssh)

2. [Set up Docker's apt repository](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3. Install the Docker packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

4. Grant permissions

```
sudo usermod -aG docker $USER
newgrp docker
```

## Deploy SigNoz and Nango

Clone this repo, which includes Docker files with SigNoz and Nango:

```bash
git clone https://github.com/inkeep/agents-optional-local-dev inkeep-external-services
cd inkeep-external-services
```

Run this command to autogenerate a `.env` file:

```bash
cp .env.example .env && \
  encryption_key=$(openssl rand -base64 32) && \
  tmp_file=$(mktemp) && \
  sed "s|<REPLACE_WITH_BASE64_256BIT_ENCRYPTION_KEY>|$encryption_key|" .env > "$tmp_file" && \
  mv "$tmp_file" .env && \
  echo "Docker environment file created with auto-generated encryption key"
```

Nango requires a `NANGO_ENCRYPTION_KEY`. Once you create this, it cannot be edited.

Here's an overview of the important environment variables when deploying to production. Make sure to replace all of these in the `.env` file.

```bash
NANGO_ENCRYPTION_KEY=<nango_encryption_key>

# Replace these with your <vm_external_ip> in production!
NANGO_SERVER_URL=http://<vm_external_ip>:3050
NANGO_PUBLIC_CONNECT_URL=http://<vm_external_ip>:3051

# Modify these in production environments!
NANGO_DASHBOARD_USERNAME=admin@example.com
NANGO_DASHBOARD_PASSWORD=adminADMIN!@12
```

Build and deploy SigNoz, Nango, OTEL Collector, and Jaeger:

```bash
docker compose up -d
```

This may take up to 5 minutes to start.

### Retrieve your SigNoz and Nango API Keys

To get your SigNoz API key `SIGNOZ_API_KEY`:

* Open SigNoz in a browser at `http://<vm_external_ip>:3080`
* Navigate to Settings → Account Settings → API Keys → New Key
* Choose a role, Viewer is sufficient for observability
* Set the expiration field to "No Expiry" to prevent the key from expiring

To get your Nango secret key `NANGO_SECRET_KEY`:

* Open Nango in a browser at `http://<vm_external_ip>:3050`
* Nango auto-creates two environments, Prod and Dev. Select the one you will use.
* Navigate to Environment Settings to find the secret key

## Deploy the Inkeep Agent Framework

From the root directory, create a new project directory for the Docker Compose setup for the Inkeep Agent Framework

```bash
mkdir inkeep && cd inkeep
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/docker-compose.yml
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/.env.docker.example
```

Generate a `.env` file from the example:

```bash
cp .env.docker.example .env
```

Here's an overview of the important environment variables when deploying to production. Make sure to replace all of these in the `.env` file.

```bash
# Change to "production" if deploying to production
ENVIRONMENT=production

# AI Provider Keys (you need at least one)
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GOOGLE_GENERATIVE_AI_API_KEY=

# Nango
NANGO_SECRET_KEY=

# SigNoz
SIGNOZ_API_KEY=

# Uncomment and set each of these with (openssl rand -hex 32)
INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET=
INKEEP_AGENTS_RUN_API_BYPASS_SECRET=
INKEEP_AGENTS_JWT_SIGNING_SECRET=

# Uncomment and set these for the Manage UI at http://<vm_external_ip>:3000
PUBLIC_INKEEP_AGENTS_MANAGE_API_URL=http://<vm_external_ip>:3002
PUBLIC_INKEEP_AGENTS_RUN_API_URL=http://<vm_external_ip>:3003
PUBLIC_INKEEP_AGENTS_RUN_API_BYPASS_SECRET=<copy INKEEP_AGENTS_RUN_API_BYPASS_SECRET>
PUBLIC_NANGO_SERVER_URL=http://<vm_external_ip>:3050
PUBLIC_NANGO_CONNECT_BASE_URL=http://<vm_external_ip>:3051
PUBLIC_SIGNOZ_URL=http://<vm_external_ip>:3080

# Uncomment and set these to access Manage UI at http://<vm_external_ip>:3000
INKEEP_AGENTS_MANAGE_UI_USERNAME=admin@example.com
INKEEP_AGENTS_MANAGE_UI_PASSWORD=adminADMIN!@12
```

<>
  :::tip Advanced Configuration

  For long-running agents or custom deployment requirements, you can override runtime limits like execution timeouts, maximum transfers, and generation steps. See [Configure Runtime Limits](/docs/self-hosting/configure-runtime-limits) for examples and the complete list of overridable settings.

  :::
</>

Run with Docker:

```bash
docker compose up -d
```

Then open `http://<vm_external_ip>:3000` in a browser!


# Deploy to Hetzner
URL: /self-hosting/hetzner

Deploy to Hetzner with Docker Compose

***

title: Deploy to Hetzner
sidebarTitle: Hetzner
description: Deploy to Hetzner with Docker Compose
icon: "LuServerCog"
-------------------

## Create a server

* Create a server, recommended size is at least CPX32 (4 VCPUS, 8 GB RAM, >30 GB Storage)
* Select Ubuntu 24.04 Image
* Create an inbound firewall rule to allow TCP ports: 3000, 3002, 3003, 3050, 3051, and 3080. These are the ports exposed by the Inkeep services.

## Install Docker Compose

1. SSH into the server as root

2. [Set up Docker's apt repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3. Install the Docker packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Deploy SigNoz and Nango

Clone this repo, which includes Docker files with SigNoz and Nango:

```bash
git clone https://github.com/inkeep/agents-optional-local-dev inkeep-external-services
cd inkeep-external-services
```

Run this command to autogenerate a `.env` file:

```bash
cp .env.example .env && \
  encryption_key=$(openssl rand -base64 32) && \
  tmp_file=$(mktemp) && \
  sed "s|<REPLACE_WITH_BASE64_256BIT_ENCRYPTION_KEY>|$encryption_key|" .env > "$tmp_file" && \
  mv "$tmp_file" .env && \
  echo "Docker environment file created with auto-generated encryption key"
```

Nango requires a `NANGO_ENCRYPTION_KEY`. Once you create this, it cannot be edited.

Here's an overview of the important environment variables when deploying to production. Make sure to replace all of these in the `.env` file.

```bash
NANGO_ENCRYPTION_KEY=<nango_encryption_key>

# Replace these with your <vm_external_ip> in production!
NANGO_SERVER_URL=http://<vm_external_ip>:3050
NANGO_PUBLIC_CONNECT_URL=http://<vm_external_ip>:3051

# Modify these in production environments!
NANGO_DASHBOARD_USERNAME=admin@example.com
NANGO_DASHBOARD_PASSWORD=adminADMIN!@12
```

Build and deploy SigNoz, Nango, OTEL Collector, and Jaeger:

```bash
docker compose up -d
```

This may take up to 5 minutes to start.

### Retrieve your SigNoz and Nango API Keys

To get your SigNoz API key `SIGNOZ_API_KEY`:

* Open SigNoz in a browser at `http://<vm_external_ip>:3080`
* Navigate to Settings → Account Settings → API Keys → New Key
* Choose a role, Viewer is sufficient for observability
* Set the expiration field to "No Expiry" to prevent the key from expiring

To get your Nango secret key `NANGO_SECRET_KEY`:

* Open Nango in a browser at `http://<vm_external_ip>:3050`
* Nango auto-creates two environments, Prod and Dev. Select the one you will use.
* Navigate to Environment Settings to find the secret key

## Deploy the Inkeep Agent Framework

From the root directory, create a new project directory for the Docker Compose setup for the Inkeep Agent Framework

```bash
mkdir inkeep && cd inkeep
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/docker-compose.yml
wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/.env.docker.example
```

Generate a `.env` file from the example:

```bash
cp .env.docker.example .env
```

Here's an overview of the important environment variables when deploying to production. Make sure to replace all of these in the `.env` file.

```bash
# Change to "production" if deploying to production
ENVIRONMENT=production

# AI Provider Keys (you need at least one)
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GOOGLE_GENERATIVE_AI_API_KEY=

# Nango
NANGO_SECRET_KEY=

# SigNoz
SIGNOZ_API_KEY=

# Uncomment and set each of these with (openssl rand -hex 32)
INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET=
INKEEP_AGENTS_RUN_API_BYPASS_SECRET=
INKEEP_AGENTS_JWT_SIGNING_SECRET=

# Uncomment and set these for the Manage UI at http://<vm_external_ip>:3000
PUBLIC_INKEEP_AGENTS_MANAGE_API_URL=http://<vm_external_ip>:3002
PUBLIC_INKEEP_AGENTS_RUN_API_URL=http://<vm_external_ip>:3003
PUBLIC_INKEEP_AGENTS_RUN_API_BYPASS_SECRET=<copy INKEEP_AGENTS_RUN_API_BYPASS_SECRET>
PUBLIC_NANGO_SERVER_URL=http://<vm_external_ip>:3050
PUBLIC_NANGO_CONNECT_BASE_URL=http://<vm_external_ip>:3051
PUBLIC_SIGNOZ_URL=http://<vm_external_ip>:3080

# Uncomment and set these to access Manage UI at http://<vm_external_ip>:3000
INKEEP_AGENTS_MANAGE_UI_USERNAME=admin@example.com
INKEEP_AGENTS_MANAGE_UI_PASSWORD=adminADMIN!@12
```

<>
  :::tip Advanced Configuration

  For long-running agents or custom deployment requirements, you can override runtime limits like execution timeouts, maximum transfers, and generation steps. See [Configure Runtime Limits](/docs/self-hosting/configure-runtime-limits) for examples and the complete list of overridable settings.

  :::
</>

Run with Docker:

```bash
docker compose up -d
```

Then open `http://<vm_external_ip>:3000` in a browser!


# Deploy to Vercel
URL: /self-hosting/vercel

Deploy the Inkeep Agent Framework to Vercel

***

title: Deploy to Vercel
description: Deploy the Inkeep Agent Framework to Vercel
icon: "brand/VercelIcon"
------------------------

## Deploy to Vercel

### Step 1: Create a GitHub repository for your project

If you do not have an Inkeep project already, [follow these steps](/get-started/quick-start) to create one. Then push your project to a repository on GitHub.

### Step 2: Create a Postgres Database

Create a Postgres database on the [**Vercel Marketplace**](https://vercel.com/marketplace/neon) or directly at [**Neon**](https://neon.tech/).

### Step 3: Configure Database Connection

Set your database connection string as an environment variable:

```
DATABASE_URL=
```

### Step 4: Create a Vercel account

Sign up for a Vercel account [here](https://vercel.com/signup).

### Step 5: Create a Vercel project for Manage API

![Vercel New Project - Manage API](/images/vercel-new-project-manage-api-hono.png)

<Note>
  The Framework Preset should be "Hono" and the Root Directory should be
  `apps/manage-api`.
</Note>

Required environment variables for Manage API:

```
ENVIRONMENT=production

INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET=

DATABASE_URL=

NANGO_SECRET_KEY=
NANGO_SERVER_URL=https://api.nango.dev
```

| Environment Variable                     | Value                                                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ENVIRONMENT`                            | `production`                                                                                                                                                       |
| `INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET` | Run `openssl rand -hex 32` in your terminal to generate this value. Save this value for `INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET` in Step 7.                        |
| `DATABASE_URL`                           | Postgres connection string from Step 3 (e.g., `postgresql://user:password@host:5432/database`)                                                                     |
| `NANGO_SECRET_KEY`                       | Nango secret key from your [Nango Cloud account](/get-started/credentials#option-1-nango-cloud-setup). Note: Local Nango setup won't work with Vercel deployments. |
| `NANGO_SERVER_URL`                       | `https://api.nango.dev`                                                                                                                                            |

### Step 6: Create a Vercel project for Run API

![Vercel New Project - Run API](/images/vercel-new-project-run-api-hono.png)

<Note>
  The Framework Preset should be "Hono" and the Root Directory should be
  `apps/run-api`.
</Note>

Required environment variables for Run API:

```
ENVIRONMENT=production

ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GOOGLE_GENERATIVE_AI_API_KEY=

INKEEP_AGENTS_RUN_API_BYPASS_SECRET=

DATABASE_URL=

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://ingest.us.signoz.cloud:443/v1/traces
OTEL_EXPORTER_OTLP_TRACES_HEADERS=signoz-ingestion-key=<your-ingestion-key>

NANGO_SECRET_KEY=
NANGO_SERVER_URL=https://api.nango.dev

INKEEP_AGENTS_JWT_SIGNING_SECRET=
```

| Environment Variable                  | Value                                                                                                                                                                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ENVIRONMENT`                         | `production`                                                                                                                                                                                                                               |
| `ANTHROPIC_API_KEY`                   | Your Anthropic API key                                                                                                                                                                                                                     |
| `OPENAI_API_KEY`                      | Your OpenAI API key                                                                                                                                                                                                                        |
| `GOOGLE_GENERATIVE_AI_API_KEY`        | Your Google Gemini API key                                                                                                                                                                                                                 |
| `INKEEP_AGENTS_RUN_API_BYPASS_SECRET` | Run `openssl rand -hex 32` in your terminal to generate this value. Save this value for `INKEEP_AGENTS_RUN_API_BYPASS_SECRET` in Step 7.                                                                                                   |
| `DATABASE_URL`                        | Postgres connection string from Step 3 (e.g., `postgresql://user:password@host:5432/database`)                                                                                                                                             |
| `NANGO_SECRET_KEY`                    | Nango secret key from your [Nango Cloud account](/get-started/credentials#option-1-nango-cloud-setup). Note: Local Nango setup won't work with Vercel deployments.                                                                         |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`  | `https://ingest.us.signoz.cloud:443/v1/traces`                                                                                                                                                                                             |
| `OTEL_EXPORTER_OTLP_TRACES_HEADERS`   | `signoz-ingestion-key=<your-ingestion-key>`. Use the instructions from [SigNoz Cloud Setup](/get-started/traces#option-1-signoz-cloud-setup) to configure your ingestion key. Note: Local SigNoz setup won't work with Vercel deployments. |
| `NANGO_SERVER_URL`                    | `https://api.nango.dev`                                                                                                                                                                                                                    |
| `INKEEP_AGENTS_JWT_SIGNING_SECRET`    | Run `openssl rand -hex 32` in your terminal to generate this value. Save this value for `INKEEP_AGENTS_JWT_SIGNING_SECRET` in Step 7.                                                                                                      |

### Step 7: Create a Vercel project for Manage UI

![Vercel New Project - Manage UI](/images/vercel-new-project-manage-ui-nextjs.png)

<Note>
  The Framework Preset should be "Next.js" and the Root Directory should be
  `apps/manage-ui`.
</Note>

Required environment variables for Manage UI:

```
ENVIRONMENT=production

PUBLIC_INKEEP_AGENTS_RUN_API_URL=
PUBLIC_INKEEP_AGENTS_RUN_API_BYPASS_SECRET=

PUBLIC_INKEEP_AGENTS_MANAGE_API_URL=
INKEEP_AGENTS_MANAGE_API_URL=
INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET=

PUBLIC_SIGNOZ_URL=https://<your-organization>.signoz.cloud
SIGNOZ_API_KEY=

PUBLIC_NANGO_SERVER_URL=https://api.nango.dev
PUBLIC_NANGO_CONNECT_BASE_URL=https://connect.nango.dev
NANGO_SECRET_KEY=
```

| Environment Variable                         | Value                                                                                                                                                                                          |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ENVIRONMENT`                                | `production`                                                                                                                                                                                   |
| `PUBLIC_INKEEP_AGENTS_RUN_API_URL`           | Your Vercel deployment URL for Run API                                                                                                                                                         |
| `PUBLIC_INKEEP_AGENTS_RUN_API_BYPASS_SECRET` | Your generated Run API bypass secret from Step 6                                                                                                                                               |
| `PUBLIC_INKEEP_AGENTS_MANAGE_API_URL`        | Your Vercel deployment URL for Manage API (skip if same as `INKEEP_AGENTS_MANAGE_API_URL`)                                                                                                     |
| `INKEEP_AGENTS_MANAGE_API_URL`               | Your Vercel deployment URL for Manage API                                                                                                                                                      |
| `INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET`     | Your generated Manage API bypass secret from Step 5                                                                                                                                            |
| `PUBLIC_SIGNOZ_URL`                          | Use the instructions from [SigNoz Cloud Setup](/get-started/traces#option-1-signoz-cloud-setup) to configure your SigNoz URL. Note: Local SigNoz setup won't work with Vercel deployments.     |
| `SIGNOZ_API_KEY`                             | Use the instructions from [SigNoz Cloud Setup](/get-started/traces#option-1-signoz-cloud-setup) to configure your SigNoz API key. Note: Local SigNoz setup won't work with Vercel deployments. |
| `NANGO_SECRET_KEY`                           | Nango secret key from your [Nango Cloud account](/get-started/credentials#option-1-nango-cloud-setup). Note: Local Nango setup won't work with Vercel deployments.                             |
| `PUBLIC_NANGO_SERVER_URL`                    | `https://api.nango.dev`                                                                                                                                                                        |
| `PUBLIC_NANGO_CONNECT_BASE_URL`              | `https://connect.nango.dev`                                                                                                                                                                    |

### Step 8: Enable Vercel Authentication

To prevent anyone from being able to access the UI, we recommend enabling Vercel authentication for all deployments: **Settings > Deployment Protection > Vercel Authentication > All Deployments**.

### Step 9: Create a Vercel project for your MCP server (optional)

![Vercel New Project - MCP Server](/images/vercel-new-project-mcp.png)

<Note>
  The Framework Preset should be "Next.js" and the Root Directory should be
  `apps/mcp`.
</Note>

For more information on how to add MCP servers to your project, see [Create MCP Servers](/typescript-sdk/cli-reference#inkeep-add).

## Push your Agent

### Step 1: Configure your root .env file

```
INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET=
INKEEP_AGENTS_RUN_API_BYPASS_SECRET=
```

### Step 2: Create a cloud configuration file

Create a new configuration file named `inkeep-cloud.config.ts` in your project's `src` directory, alongside your existing configuration file.

```typescript
import { defineConfig } from "@inkeep/agents-cli/config";

const config = defineConfig({
  tenantId: "default",
  agentsManageApi: {
    url: "https://<your-manage-api-url>",
    apiKey: process.env.INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET,
  },
  agentsRunApi: {
    url: "https://<your-run-api-url>",
    apiKey: process.env.INKEEP_AGENTS_RUN_API_BYPASS_SECRET,
  },
});

export default config;
```

### Step 3: Push your Agent

```bash
cd /src/<your-project-directory>
inkeep push --config ../inkeep-cloud.config.ts
```

## Pull your Agent

```bash
cd /src
inkeep pull --config inkeep-cloud.config.ts
```

## Function Tools with Vercel Sandbox

When deploying to serverless environments like Vercel, you can configure [function tools](/typescript-sdk/tools/function-tools) to execute in [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) MicroVMs instead of your Agent's runtime service. This is **required** for serverless platforms since child process spawning is restricted.

### Why Use Vercel Sandbox?

**When to use each provider:**

* **Native** - Use for traditional cloud deployments (VMs, Docker, Kubernetes), self-hosted servers, or local development
* **Vercel Sandbox** - Required for serverless platforms (Vercel, AWS Lambda, etc.) or if you'd like to isolate tool executions

### Setting Up Vercel Sandbox

#### Step 1: Get Vercel Credentials

You'll need three credentials from your Vercel account:

1. **Vercel Token** - Create an access token at [vercel.com/account/tokens](https://vercel.com/account/tokens)
2. **Team ID** - Find in your team settings at [vercel.com/teams](https://vercel.com/teams)
3. **Project ID** - Find in your Vercel project settings

#### Step 2: Configure Sandbox in Your Application

Update your Run API to use Vercel Sandbox.

In the `apps/run-api/src` folder, create a `sandbox.ts` file:

```typescript sandbox.ts
const isProduction = process.env.ENVIRONMENT === "production";

export const sandboxConfig = isProduction
  ? {
      provider: "vercel",
      runtime: "node22", // or 'typescript'
      timeout: 60000, // 60 second timeout
      vcpus: 4, // Allocate 4 vCPUs
      teamId: process.env.SANDBOX_VERCEL_TEAM_ID!,
      projectId: process.env.SANDBOX_VERCEL_PROJECT_ID!,
      token: process.env.SANDBOX_VERCEL_TOKEN!,
    }
  : {
      provider: "native",
      runtime: "node22",
      timeout: 30000,
      vcpus: 2,
    };
```

Import it into your `index.ts` file:

```typescript index.ts
import { sandboxConfig } from "./sandbox.ts";
// ...
const app: Hono = createExecutionApp({
  // ...
  sandboxConfig, // NEW
});
```

#### Step 3: Add Environment Variables to Run API

Add these [environment variables in your Vercel project](https://vercel.com/docs/environment-variables/managing-environment-variables#declare-an-environment-variable) to your **Run API** app:

```bash
SANDBOX_VERCEL_TOKEN=your_vercel_access_token
SANDBOX_VERCEL_TEAM_ID=team_xxxxxxxxxx
SANDBOX_VERCEL_PROJECT_ID=prj_xxxxxxxxxx
```

<Accordions>
  <Accordion title="Troubleshooting Functions">
    <strong>"Failed to refresh OIDC token" error:</strong>

    <ul>
      <li>This occurs when you're not in a Vercel environment or you don't provide a Vercel access token</li>

      <li>
        Solution: Use a Vercel access token from
        <a href="https://vercel.com/account/tokens" target="_blank" rel="noopener noreferrer">vercel.com/account/tokens</a>
      </li>
    </ul>

    <strong>Function execution timeouts:</strong>

    <ul>
      <li>Increase the <code>timeout</code> value in sandbox configuration</li>
      <li>Consider allocating more <code>vcpus</code> for resource-intensive functions</li>
      <li>Check Vercel Sandbox limits for your plan</li>
    </ul>

    <strong>Dependency installation failures:</strong>

    <ul>
      <li>Ensure dependencies are compatible with Node.js 22</li>
      <li>Check that package versions are specified correctly</li>
      <li>Verify network access to npm registry</li>
    </ul>

    <strong>High costs:</strong>

    <ul>
      <li>Reduce <code>vcpus</code> allocation if functions don't need maximum resources</li>
      <li>Optimize function code to execute faster</li>
      <li>Consider caching results when possible</li>
    </ul>
  </Accordion>

  <Accordion title="Best Practices">
    <ol>
      <li><strong>Use environment variables</strong> – Never hardcode credentials</li>
      <li><strong>Start with fewer vCPUs</strong> – Scale up only if needed</li>
      <li><strong>Set reasonable timeouts</strong> – Prevent runaway executions</li>
      <li><strong>Monitor usage</strong> – Track sandbox execution metrics in Vercel dashboard</li>
      <li><strong>Test thoroughly</strong> – Verify functions work in sandbox environment before deploying</li>
      <li><strong>Choose the right provider</strong> – Use native for VMs/Docker/K8s, Vercel Sandbox for serverless only</li>
    </ol>

    <p>For more information on function tools, see:</p>

    <ul>
      <li>
        <a href="/typescript-sdk/tools/function-tools">Function Tools (TypeScript SDK)</a>
      </li>

      <li>
        <a href="/visual-builder/tools/function-tools">Function Tools (Visual Builder)</a>
      </li>

      <li>
        <a href="https://vercel.com/docs/vercel-sandbox" target="_blank" rel="noopener noreferrer">Vercel Sandbox Documentation</a>
      </li>
    </ul>
  </Accordion>
</Accordions>


# Talk to your agent via A2A (JSON-RPC)
URL: /talk-to-your-agents/a2a

Use the Agent2Agent JSON-RPC protocol to send messages to your agent and receive results, with optional streaming.

***

title: Talk to your agent via A2A (JSON-RPC)
sidebarTitle: Agent2Agent API
description: Use the Agent2Agent JSON-RPC protocol to send messages to your agent and receive results, with optional streaming.
icon: "LuNetwork"
-----------------

The A2A (Agent-to-Agent) endpoint lets third-party agents, agent platforms, or agent workspaces interact with your Inkeep Agent using a standard agent protocol.

Here are some example platforms that you can add Inkeep Agents to:

| Platform                                                                                                                                                                                                       | Description                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **[Google Gemini Enterprise](https://cloud.google.com/gemini-enterprise/faq)**                                                                                                                                 | Bring‑your‑own A2A agents into an enterprise agentspace and orchestrate alongside Google/vendor agents. |
| **[Microsoft Copilot Studio / Azure AI Foundry](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/06-multi-remote-agents-with-a2a.html)**                                                     | Copilots can invoke external A2A agents as peer services in multi‑agent flows.                          |
| **[Salesforce Agentforce](https://architect.salesforce.com/fundamentals/agentic-patterns)**                                                                                                                    | Add third‑party A2A agents (e.g., via AgentExchange) and compose them in CRM workflows.                 |
| **[SAP Joule](https://learning.sap.com/courses/boosting-ai-driven-business-transformation-with-joule-agents/enabling-interoperability-for-ai-agents)**                                                         | Federate non‑SAP A2A agents into SAP’s business agent fabric.                                           |
| **[ServiceNow AI Agent Fabric](https://www.servicenow.com/community/now-assist-articles/introducing-ai-agent-fabric-enable-mcp-and-a2a-for-your-agentic/ta-p/3373907)**                                        | Discover and call external A2A agents within IT/business automations.                                   |
| **[Atlassian Rovo](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/)**                                                                       | Configure Rovo to call external A2A agents for cross‑tool tasks.                                        |
| **[Workday AI (Agent Gateway / ASOR)](https://investor.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)** | Register external customer/partner A2A agents alongside Workday agents.                                 |

<>
  ## Authentication

  Choose the authentication method:

  <Tabs>
    <Tab title="Using an API Key">
      **Create an API Key:**

      1. Open the Visual Builder Dashboard
      2. Go to your Project → **API Keys**
      3. Click **Create**, select the target agent
      4. Copy the API key (it will be shown once) and store it securely

      **Request Header:**

      ```http
      Authorization: Bearer <api_key>
      ```
    </Tab>

    <Tab title="Without API key">
      When running the API server locally with `pnpm dev`, authentication is automatically bypassed. You can use headers in the request instead:

      **Request Headers:**

      ```http
      x-inkeep-tenant-id: <tenant-id>
      x-inkeep-project-id: <project-id>
      x-inkeep-agent-id: <agent-id>
      ```

      <Warning>
        This mode is for development only. Never use in production as it bypasses all security checks.
      </Warning>
    </Tab>
  </Tabs>

  See [Authentication → Run API](/api-reference/authentication/run-api) for more details.
</>

## Endpoints

* **Agent card discovery (agent or sub-agent-level):** `GET <INKEEP_AGENTS_RUN_API_URL>/agents/.well-known/agent.json`
* **A2A protocol (agent or sub-agent-level):** `POST <INKEEP_AGENTS_RUN_API_URL>/agents/.well-known/agent.json`

Notes:

* If you supply `x-inkeep-sub-agent-id` in headers, requests target that specific Sub Agent. This is supported in development (or when using the bypass secret). With production API keys, requests always use the Agent's default Sub Agent.

## Message Send (Blocking)

* **Path:** `POST  <INKEEP_AGENTS_RUN_API_URL>/agents/a2a`
* **Headers:** Per Authentication section (Standard API Key recommended)
* **Body (JSON-RPC 2.0):**

```json
{
  "jsonrpc": "2.0",
  "method": "message/send",
  "id": 1,
  "params": {
    "message": {
      "messageId": "msg-123",
      "role": "user",
      "parts": [
        { "kind": "text", "text": "Hello!" }
      ],
      "contextId": "conv-123",
      "kind": "message"
    },
    "configuration": {
      "acceptedOutputModes": ["text", "text/plain"],
      "blocking": true
    }
  }
}
```

* **Success Response (Message):**

```json
{
  "jsonrpc": "2.0",
  "result": {
    "kind": "message",
    "messageId": "auto-generated",
    "role": "agent",
    "parts": [ { "kind": "text", "text": "..." } ],
    "taskId": "task-...",
    "contextId": "conv-123"
  },
  "id": 1
}
```

* **Transfer Case:** if the agent decides to transfer, the response contains a `task` with a transfer artifact:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "kind": "task",
    "id": "task-...",
    "contextId": "conv-123",
    "status": { "state": "completed", "timestamp": "..." },
    "artifacts": [
      {
        "artifactId": "...",
        "parts": [
          { "kind": "data", "data": { "type": "transfer", "targetSubAgentId": "other-agent-id" } },
          { "kind": "text", "text": "Transfer reason text" }
        ]
      }
    ]
  },
  "id": 1
}
```

## Message Send (Non-blocking)

Set `configuration.blocking` to `false`. The server immediately returns a `task`, and you can poll or stream updates.

* **Request:** same as above, with `"blocking": false`
* **Response (Task):**

```json
{
  "jsonrpc": "2.0",
  "result": {
    "kind": "task",
    "id": "task-...",
    "contextId": "conv-123",
    "status": { "state": "completed", "timestamp": "..." },
    "artifacts": [ { "artifactId": "...", "parts": [ { "kind": "text", "text": "..." } ] } ]
  },
  "id": 1
}
```

## Streaming Messages (SSE)

* **Path:** `POST /agents/a2a`
* **Headers:** include `Accept: text/event-stream` plus Authentication headers
* **Body (JSON-RPC 2.0):** same as blocking, but method `"message/stream"`

```json
{
  "jsonrpc": "2.0",
  "method": "message/stream",
  "id": 2,
  "params": {
    "message": {
      "messageId": "msg-456",
      "role": "user",
      "parts": [ { "kind": "text", "text": "Stream please" } ],
      "contextId": "conv-123",
      "kind": "message"
    },
    "configuration": {
      "acceptedOutputModes": ["text", "text/plain"],
      "blocking": false
    }
  }
}
```

* **SSE Events (each line is an SSE `data:` payload containing JSON-RPC):**

```text
: keep-alive

data: {"jsonrpc":"2.0","result":{"kind":"task","id":"task-...","contextId":"conv-123","status":{"state":"working","timestamp":"..."},"artifacts":[]},"id":2}

data: {"jsonrpc":"2.0","result":{"kind":"message","messageId":"...","role":"agent","parts":[{"kind":"text","text":"..."}],"taskId":"task-...","contextId":"conv-123"},"id":2}

data: {"jsonrpc":"2.0","result":{"kind":"task","id":"task-...","contextId":"conv-123","status":{"state":"completed","timestamp":"..."},"artifacts":[{"artifactId":"...","parts":[{"kind":"text","text":"..."}]}]},"id":2}
```

* **Transfer (streaming):** if a transfer is triggered, an SSE event with a JSON-RPC `result` of transfer details is sent, then the stream ends.

## Task APIs

* **Get task:** `POST /agents/a2a` with method `"tasks/get"` and params `{ "id": "task-..." }` → returns the `task`
* **Cancel task:** `POST /agents/a2a` with method `"tasks/cancel"` and params `{ "id": "task-..." }` → returns `{ "success": true }`
* **Resubscribe (SSE, mock):** `POST /agents/a2a` with method `"tasks/resubscribe"` and params `{ "taskId": "task-..." }` → SSE with a task event

<Note>
  Currently, `tasks/get` and `tasks/cancel` return stubbed responses, and `tasks/resubscribe` returns a mock SSE event. For live progress updates, use `message/stream`.
</Note>

## Agent Card Discovery

* **Agent-level:** `GET /agents/.well-known/agent.json` (uses Agent's default Sub Agent)
* **Agent-level (dev/bypass only):** Provide `x-inkeep-sub-agent-id` in headers to target a specific agent for discovery

## Notes & Behavior

* **contextId resolution:** The server first tries `task.context.conversationId` (derived from the request), then `params.message.metadata.conversationId`. Final fallback is `'default'`.
* **Artifacts in responses:** Message/Task responses may include `artifacts[0].parts` as the agent's output parts.
* **Errors (JSON-RPC):** Standard JSON-RPC error codes: `-32600`, `-32601`, `-32602`, `-32603`, `-32700`, plus A2A-specific `-3200x` codes.

## Development Notes

* **Base URL (local):** `http://localhost:3003`
* **Route Mounting:** A2A routes are mounted under `/agents`; use `/agents/a2a` for RPC and `/agents/.well-known/agent.json` for discovery
* **Streaming support:** Requires agent capabilities `streaming: true` in the agent card


# How to call your AI Agent using the Chat API
URL: /talk-to-your-agents/chat-api

Learn about details of the Vercel AI SDK data stream protocol that powers the `/chat` API endpoint.

***

title: How to call your AI Agent using the Chat API
sidebarTitle: Chat API
description: Learn about details of the Vercel AI SDK data stream protocol that powers the `/chat` API endpoint.
icon: LuMessagesSquare
keywords: API, Vercel AI SDK, streaming, SSE, data stream, agents, chat
-----------------------------------------------------------------------

## Overview

This guide shows how to call your agent directly over HTTP and stream responses using the Vercel AI SDK data stream format. It covers the exact endpoint, headers, request body, and the event stream response you should expect.

<Tip>
  If you are building a React UI, consider our prebuilt components under [React UI Components](/talk-to-your-agents/react/chat-button) or [Vercel AI Elements](/talk-to-your-agents/vercel-ai-sdk/ai-elements) headless primatives. This page is for the low-level streaming API.
</Tip>

## Endpoint

* **Path (mounted by the Run API):** `/api/chat`
* **Method:** `POST`
* **Protocol:** Server-Sent Events (SSE) encoded JSON, using Vercel AI SDK data-stream v2
* **Content-Type (response):** `text/event-stream`
* **Response Header:** `x-vercel-ai-data-stream: v2`

<>
  ## Authentication

  Choose the authentication method:

  <Tabs>
    <Tab title="Using an API Key">
      **Create an API Key:**

      1. Open the Visual Builder Dashboard
      2. Go to your Project → **API Keys**
      3. Click **Create**, select the target agent
      4. Copy the API key (it will be shown once) and store it securely

      **Request Header:**

      ```http
      Authorization: Bearer <api_key>
      ```
    </Tab>

    <Tab title="Without API key">
      When running the API server locally with `pnpm dev`, authentication is automatically bypassed. You can use headers in the request instead:

      **Request Headers:**

      ```http
      x-inkeep-tenant-id: <tenant-id>
      x-inkeep-project-id: <project-id>
      x-inkeep-agent-id: <agent-id>
      ```

      <Warning>
        This mode is for development only. Never use in production as it bypasses all security checks.
      </Warning>
    </Tab>
  </Tabs>

  See [Authentication → Run API](/api-reference/authentication/run-api) for more details.
</>

## Request Body Schema

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello!"
    }
  ],
  "conversationId": "optional-conversation-id"
}
```

**Field Notes:**

* **`messages`** — Must include at least one `user` message
* **`content`** — Can be a string or an object with `parts` for multi-part content
* **`conversationId`** — Optional; server generates one if omitted

### Optional Headers

* **`x-emit-operations`** — Set to `true` to include detailed data operations in the response stream. Useful for debugging and monitoring agent behavior. See [Data Operations](/typescript-sdk/data-operations) for details.

### Example cURL

When using an API key for auth:

```bash
curl -N \
  -X POST "http://localhost:3003/api/chat" \
  -H "Authorization: Bearer $INKEEP_API_KEY" \
  -H "Content-Type: application/json" \
  -H "x-emit-operations: true" \
  -d '{
    "messages": [
      { "role": "user", "content": "What can you do?" }
    ],
    "conversationId": "chat-1234"
  }'
```

## Response: Vercel AI SDK Data Stream (v2)

The response is an SSE stream of JSON events compatible with the Vercel AI SDK UI message stream. The server sets `x-vercel-ai-data-stream: v2`.

### Event Types

#### Text Streaming Events

* **`text-start`** — Indicates a new text segment is starting
* **`text-delta`** — Carries the text content delta for the current segment
* **`text-end`** — Marks the end of the current text segment

#### Data Events

* **`data-component`** — Structured UI data emitted by the agent (for rich UIs)
* **`data-artifact`** — Artifact data emitted by tools/agents (documents, files, saved results)
* **`data-operation`** — Low-level operational events (agent lifecycle, completion, errors)
* **`data-summary`** — AI-generated status updates with user-friendly labels and contextual details

### Example Stream (abbreviated)

```text
: keep-alive

data: {"type":"text-start","id":"1726247200-abc123"}

data: {"type":"text-delta","id":"1726247200-abc123","delta":"Hello! I can help with..."}

data: {"type":"data-summary","data":{"label":"Searching documentation","details":{"summary":"Looking for relevant information","progress":"25%"}}}

data: {"type":"text-delta","id":"1726247200-abc123","delta":" analyzing your query..."}

data: {"type":"text-end","id":"1726247200-abc123"}

data: {"type":"data-operation","data":{"type":"completion","ctx":{"agent":"search-agent","iteration":1}}}

data: {"type":"data-component","id":"1726247200-abc123-0","data":{"type":"customer-info","name":"Ada","email":"ada@example.com"}}

data: {"type":"data-artifact","data":{"artifact_id":"art_abc","task_id":"task_xyz","summary":{"title":"Search Results"}}}
```

### Data Event Details

#### `data-operation` Events

Low-level operational events with technical context. Common types include:

* **`agent_initializing`** — The agent runtime is starting
* **`agent_ready`** — Agent is ready and processing
* **`completion`** — The agent completed the task (includes agent ID and iteration count)
* **`error`** — Error information (also emitted as a top-level `error` event)

```json
{"type":"data-operation","data":{"type":"completion","ctx":{"agent":"search-agent","iteration":1}}}
```

#### `data-summary` Events

AI-generated status updates designed for end-user consumption. Structure:

* **`label`** — User-friendly description (required)
* **`details`** — Optional structured/unstructured context data

```json
{"type":"data-summary","data":{"label":"Processing search results","details":{"summary":"Found 12 relevant documents","itemsProcessed":12,"status":"analyzing"}}}
```

#### `data-artifact` Events

Saved documents, files, or structured results from tool executions:

```json
{"type":"data-artifact","data":{"artifact_id":"art_123","task_id":"task_456","summary":{"title":"Weather Report","type":"document"}}}
```

#### `data-component` Events

Structured UI data for rich interface components:

```json
{"type":"data-component","id":"comp_123","data":{"type":"chart","title":"Sales Data","chartData":[1,2,3]}}
```

### Text Streaming Behavior

* For each text segment, the server emits `text-start` → `text-delta` → `text-end`
* The server avoids splitting content word-by-word; a segment is usually a coherent chunk
* Operational events are queued during active text emission and flushed shortly after to preserve ordering and readability

## Error Responses

### Streamed Errors

Errors are now delivered as `data-operation` events with unified structure:

```json
{
  "type": "data-operation",
  "data": {
    "type": "error",
    "message": "Error description",
    "agent": "agent-id",
    "severity": "error",
    "code": "optional-error-code",
    "timestamp": 1640995200000
  }
}
```

### Non-Streaming Errors

Validation failures and other errors return JSON with an appropriate HTTP status code.

## HTTP Status Codes

* **`200`** — Stream opened successfully
* **`401`** — Missing/invalid authentication
* **`404`** — Agent not found
* **`400`** — Invalid request body/context
* **`500`** — Internal server error

## Development Notes

* **Default local base URL:** `http://localhost:3003`
* **Endpoint mounting in the server:**
  * `/api/chat` → Vercel data stream (this page)
  * `/v1/mcp` → MCP JSON-RPC endpoint

<Note>
  To test quickly without a UI, use `curl -N` or a tool that supports Server-Sent Events.
</Note>


# MCP Server
URL: /talk-to-your-agents/mcp-server

Learn how to use the MCP server to talk to your agents

***

title: MCP Server
description: Learn how to use the MCP server to talk to your agents
icon: "LuServer"
----------------

The MCP server allows you to talk to your agents through the Model Context Protocol.

<>
  ## Authentication

  Choose the authentication method:

  <Tabs>
    <Tab title="Using an API Key">
      **Create an API Key:**

      1. Open the Visual Builder Dashboard
      2. Go to your Project → **API Keys**
      3. Click **Create**, select the target agent
      4. Copy the API key (it will be shown once) and store it securely

      **Request Header:**

      ```http
      Authorization: Bearer <api_key>
      ```
    </Tab>

    <Tab title="Without API key">
      When running the API server locally with `pnpm dev`, authentication is automatically bypassed. You can use headers in the request instead:

      **Request Headers:**

      ```http
      x-inkeep-tenant-id: <tenant-id>
      x-inkeep-project-id: <project-id>
      x-inkeep-agent-id: <agent-id>
      ```

      <Warning>
        This mode is for development only. Never use in production as it bypasses all security checks.
      </Warning>
    </Tab>
  </Tabs>

  See [Authentication → Run API](/api-reference/authentication/run-api) for more details.
</>

## MCP Server Implementation

The MCP server is implemented in the `@inkeep/agents-run-api` library and provides a standard interface for agent communication.

## Available Tools

The MCP server exposes one core tool:

### send-query-to-agent

Sends a query to your agent's default sub-agent. This tool:

* **Name**: `send-query-to-agent`
* **Description**: Dynamically generated based on your agent's name and description
* **Parameters**:
  * `query` (string): The query to send to the agent
* **Returns**: The agent's response as text content

**Example usage in Cursor:**
When the MCP server is configured, Cursor will automatically discover this tool and you can use it by asking questions. The tool will route your query to the appropriate sub-agent in your agent and return the response.

The tool handles:

* Message creation and conversation management
* Sub-agent execution with your configured tools and capabilities
* Context resolution if your agent has context configuration
* Error handling and response formatting

## Using with Cursor

### Quick Install (Inkeep Hosted Docs MCP)

Install the Inkeep Agents documentation MCP server with one click:

<div
  style={{
  display: "flex",
  gap: "10px",
  marginBottom: "16px",
  flexWrap: "wrap",
}}
>
  <a href="cursor://anysphere.cursor-deeplink/mcp/install?name=inkeep-agents&config=eyJ1cmwiOiJodHRwczovL2FnZW50cy5pbmtlZXAuY29tL21jcCJ9">
    <Image src="https://cursor.com/deeplink/mcp-install-dark.png" alt="Add to Cursor" style={{ height: "40px" }} />
  </a>

  <a href="vscode:mcp/install?%7B%22name%22%3A%22inkeep-agents%22%2C%22type%22%3A%22sse%22%2C%22url%22%3A%22https%3A%2F%2Fagents.inkeep.com%2Fmcp%22%7D">
    <Image src="https://img.shields.io/badge/VS_Code-Install_Inkeep_Agents-0098FF?style=flat-square&logo=visualstudiocode&logoColor=ffffff" alt="Install in VS Code" />
  </a>
</div>

### Manual Configuration

Add the following configuration to your Cursor MCP settings.

#### Example

Example when using an API key for auth:

```json
{
  "AgentName": {
    "type": "mcp",
    "url": "http://<your-run-api-url>/v1/mcp",
    "headers": {
      "Authorization": "Bearer <agent_api_key>"
    }
  }
}
```

## Session Management (Required by MCP HTTP Transport)

* Initialize a session by sending an `initialize` JSON-RPC request to `/v1/mcp`.
* The server will respond and set `Mcp-Session-Id` in response headers.
* For all subsequent JSON-RPC requests in that session, include `Mcp-Session-Id` header with the value from initialization.

<Note>
  Session management is required by MCP’s HTTP transport. If `Mcp-Session-Id` is
  missing or invalid on follow-up requests, the server will return a JSON-RPC
  error (e.g., "Session not found").
</Note>

## Configuration Notes

* **URL**: Point to your `agents-run-api` instance (default: `http://localhost:3003`)
* **Headers**: Use the appropriate authentication mode per the section above
* **Authorization**: Only required outside development mode


# Overview
URL: /talk-to-your-agents/overview

Learn how to talk to your agents

***

title: Overview
description: Learn how to talk to your agents
icon: "LuMessageSquare"
-----------------------

<>
  You can talk to an Inkeep Agent in a few ways, including:

  * **UI Chat Components**: Drop-in React components for chat UIs with built-in streaming and rich UI customization. See [`agents-ui`](/talk-to-your-agents/react/chat-button).
  * **As an MCP server**: Use your Inkeep Agent as if was an MCP Server. Allows you to connect it to any MCP client, like Claude, ChatGPT, Claude and other Agents. See [MCP server](/talk-to-your-agents/mcp-server).
  * **Via API (Vercel format)**: An API that streams responses over server-side events (SSE). Use from any language/runtime, including the Vercel's `useChat` and AI Element primitives for custom UIs. See [API (Vercel format)](/talk-to-your-agents/api).
  * **Via API (A2A format)**: An API that follows the Agent-to-Agent ('A2A') JSON-RPC protocol. Great for when combining Inkeep with different Agent frameworks that support the A2A format. See [A2A protocol](/talk-to-your-agents/a2a).

  <Cards>
    <Card title="React UI" icon="LuMessageSquare" href="/talk-to-your-agents/react/chat-button">
      Drop-in chat components for React apps with streaming and rich UI.
    </Card>

    <Card title="API (Vercel format)" icon="LuNetwork" href="/talk-to-your-agents/api">
      POST /api/chat, SSE (text/event-stream), x-vercel-ai-data-stream: v2.
    </Card>

    <Card title="A2A protocol" icon="LuNetwork" href="/talk-to-your-agents/a2a">
      JSON-RPC messages at /agents/a2a with blocking and streaming modes.
    </Card>

    <Card title="MCP server" icon="LuServer" href="/talk-to-your-agents/mcp-server">
      HTTP JSON-RPC endpoint at /v1/mcp with session header management.
    </Card>
  </Cards>
</>


# Upgrading your Inkeep version
URL: /tutorials/upgrading

Upgrade the packages that make up the Inkeep Agent Framework

***

title: Upgrading your Inkeep version
sidebarTitle: Upgrading
description: Upgrade the packages that make up the Inkeep Agent Framework
icon: "LuPackage"
-----------------

## Overview

The Inkeep Agent Framework is composed of several npm packages:

* [`@inkeep/agents-manage-api`](https://www.npmjs.com/package/@inkeep/agents-manage-api): The API for managing projects and agent configurations.
* [`@inkeep/agents-run-api`](https://www.npmjs.com/package/@inkeep/agents-run-api): The API for executing conversations with your agents.
* [`@inkeep/agents-manage-ui`](https://www.npmjs.com/package/@inkeep/agents-manage-ui): The UI for the visual builder and dashboard.
* [`@inkeep/agents-core`](https://www.npmjs.com/package/@inkeep/agents-core): The core shared functionality of the agent framework.
* [`@inkeep/agents-sdk`](https://www.npmjs.com/package/@inkeep/agents-sdk): The TypeScript SDK for building multi-agent systems.
* [`@inkeep/agents-cli`](https://www.npmjs.com/package/@inkeep/agents-cli): The CLI for managing and interacting with the agent framework.
* [`@inkeep/agents-ui`](https://www.npmjs.com/package/@inkeep/agents-ui): The UI library containing chat widget components.

## Upgrading the quickstart template

If you used the `npx @inkeep/create-agents` CLI command to create your workspace, run the following command from the workspace root:

```bash
pnpm upgrade-agents
```

This will update all the packages to the latest version and migrate your database schema to the latest version.

## Upgrading the Agent CLI

If you installed the `@inkeep/agents-cli` package globally, you can upgrade it to the latest version by running the following command:

```bash
inkeep update
```


# Sub Agent Relationships
URL: /typescript-sdk/agent-relationships

Learn how to add Sub Agent relationships to your agent

***

title: Sub Agent Relationships
description: Learn how to add Sub Agent relationships to your agent
icon: "LuUsers"
---------------

Sub Agent relationships are used to coordinate specialized Sub Agents for complex workflows. This framework implements Sub Agent relationships through using `canDelegateTo()` and `canTransferTo()`, allowing a parent Sub Agent to automatically coordinate specialized Sub Agents for complex workflows.

## Understanding Sub Agent Relationships

The framework supports two types of Sub Agent relationships:

### Transfer Relationships

Transfer relationships **completely relinquish control** from one Sub Agent to another. When a Sub Agent hands off to another:

* The source Sub Agent stops processing
* The target Sub Agent takes full control of the conversation
* Control is permanently transferred until the target Sub Agent hands back

```typescript
import { subAgent, agent } from "agent-sdk";

// Create specialized Sub Agents first
const qaSubAgent = subAgent({
  id: "qa-agent",
  name: "QA Sub Agent",
  description: "Answers product and service questions",
  prompt: "Provide accurate information using available tools. Hand back to router if unable to help.",
  canUse: () => [knowledgeBaseTool],
  canTransferTo: () => [routerSubAgent],
});

const orderSubAgent = subAgent({
  id: "order-agent",
  name: "Order Sub Agent",
  description: "Handles order-related inquiries and actions",
  prompt: "Assist with order tracking, modifications, and management.",
  canUse: () => [orderSystemTool],
  canTransferTo: () => [routerSubAgent],
});

// Create router Sub Agent that coordinates other Sub Agents
const routerSubAgent = subAgent({
  id: "router-agent",
  name: "Router Sub Agent",
  description: "Routes customer inquiries to specialized Sub Agents",
  prompt: `Analyze customer inquiries and route them appropriately:
    - Product questions → Hand off to QA Sub Agent
    - Order issues → Hand off to Order Sub Agent
    - Complex issues → Handle directly or escalate`,
  canTransferTo: () => [qaSubAgent, orderSubAgent],
});

// Create the agent with router as default entry point
const supportAgent = agent({
  id: "customer-support-agent",
  defaultSubAgent: routerSubAgent,
  subAgents: () => [routerSubAgent, qaSubAgent, orderSubAgent],
  models: {
    base: {
      model: "anthropic/claude-sonnet-4-5",
      providerOptions: {
        temperature: 0.5,
      },
    },
    structuredOutput: {
      model: "openai/gpt-4.1-mini",
    },
  },
});
```

### Delegation Relationships

Delegation relationships are used to **pass a task** from one Sub Agent to another while maintaining oversight:

* The source Sub Agent remains in control
* The target Sub Agent executes a specific task
* Results are returned to the source Sub Agent
* The source Sub Agent continues processing

```typescript
// Sub Agents for specific tasks
const numberProducerA = subAgent({
  id: "number-producer-a",
  name: "Number Producer A",
  description: "Produces low-range numbers (0-50)",
  prompt: "Generate numbers between 0 and 50. Respond with a single integer.",
});

const numberProducerB = subAgent({
  id: "number-producer-b",
  name: "Number Producer B",
  description: "Produces high-range numbers (50-100)",
  prompt: "Generate numbers between 50 and 100. Respond with a single integer.",
});

// Coordinating Sub Agent that delegates tasks
const mathSupervisor = subAgent({
  id: "math-supervisor",
  name: "Math Supervisor",
  description: "Coordinates mathematical operations",
  prompt: `When given a math task:
    1. Delegate to Number Producer A for a low number
    2. Delegate to Number Producer B for a high number
    3. Add the results together and provide the final answer`,
  canDelegateTo: () => [numberProducerA, numberProducerB],
});

const mathAgent = agent({
  id: "math-delegation-agent",
  defaultSubAgent: mathSupervisor,
  subAgents: () => [mathSupervisor, numberProducerA, numberProducerB],
  models: {
    base: {
      model: "anthropic/claude-haiku-4-5",
      providerOptions: {
        temperature: 0.1,
      }
    }
  },
});
```

## When to Use Each Relationship

### Use Transfers for Complex Tasks

Use `canTransferTo` when the task is complex and the user will likely want to ask follow-up questions to the specialized Sub Agent:

* **Customer support conversations** - User may have multiple related questions
* **Technical troubleshooting** - Requires back-and-forth interaction
* **Order management** - User might want to modify, track, or ask about multiple aspects
* **Product consultations** - Users often have follow-up questions

### Use Delegation for Simple Tasks

Use `canDelegateTo` when the task is simple and self-contained:

* **Data retrieval** - Get a specific piece of information and return it
* **Calculations** - Perform a computation and return the result
* **Single API calls** - Make one external request and return the data
* **Simple transformations** - Convert data from one format to another

```typescript
// TRANSFER: User will likely have follow-up questions about their order
const routerSubAgent = subAgent({
  id: "router",
  prompt: "For order inquiries, transfer to order specialist",
  canTransferTo: () => [orderSubAgent],
});

// DELEGATION: Just need a quick calculation, then continue
const mathSupervisor = subAgent({
  id: "supervisor",
  prompt: "Delegate to number producers, then add results together",
  canDelegateTo: () => [numberProducerA, numberProducerB],
});
```

## Types of Delegation Relationships

### Sub Agent Delegation

Sub agent delegation is used to delegate a task to a sub agent as seen above.

### External Agent Delegation

External agent delegation is used to delegate a task to an [external agent](/typescript-sdk/external-agents).

```typescript
import { myExternalAgent } from "./external-agents/external-agent-example";

const mathSupervisor = subAgent({
  id: "supervisor",
  prompt: "Delegate to the external agent to calculate the answer to the question",
  canDelegateTo: () => [myExternalAgent],
});
```

You can also specify headers to include with every request to the external agent.

```typescript
const mathSupervisor = subAgent({
  id: "supervisor",
  prompt: "Delegate to the external agent to calculate the answer to the question",
  canDelegateTo: () => [myExternalAgent.with({ headers: { "authorization": "my-api-key" } })],
});
```

### Team Agent Delegation

Team agent delegation is used to delegate a task to another agent in the same project.

```typescript
import { myAgent } from "./agents/my-team-agent";

const mathSupervisor = subAgent({
  id: "supervisor",
  prompt: "Delegate to the team agent to calculate the answer to the question",
  canDelegateTo: () => [myAgent],
});
```

You can also specify headers to include with every request to the team agent.

```typescript
const mathSupervisor = subAgent({
  id: "supervisor",
  prompt: "Delegate to the team agent to calculate the answer to the question",
  canDelegateTo: () => [myAgent.with({ headers: { "authorization": "my-api-key" } })],
});
```


# Agents & Sub Agents
URL: /typescript-sdk/agent-settings

Learn how to customize your Agents.

***

title: Agents & Sub Agents
description: Learn how to customize your Agents.
icon: "LuUser"
--------------

Agents and Sub Agents are the core building blocks of the Inkeep Agent framework.

An Agent is made up of one or more Sub Agents that can delegate or transfer control with each other, share context, use tools to respond to a user or complete a task.

## Creating an Agent

An Agent is your top-level entity that you as a user interact with or can trigger programmatically.

An Agent is made up of sub-agents, like so:

```typescript
// Agent-level prompt that gets added to all Sub Agents
const customerSupportAgent = agent({
  id: "support-agent",
  prompt: `You work for Acme Corp. Always be professional and helpful.
Follow company policies and escalate complex issues appropriately.`,
  subAgents: () => [supportAgent, escalationAgent],
});
```

**The `prompt` is automatically put into context and added into each Sub Agent's system prompt.** This provides consistent behavior and tone to all Sub Agents so they can act and respond as one cohesive unit to the end-user.

## Creating a Sub Agent

Like an Agent, a Sub Agent needs an id, name, and clear prompt that define its behavior:

```typescript
import { subAgent } from "@inkeep/agents-sdk";

const supportAgent = subAgent({
  id: "customer-support",
  name: "Customer Support Agent",
  prompt: `You are a customer support specialist. Always be helpful, professional, and empathetic.`,
});
```

## Configuring Models

Configure AI models for your agents. See [Model Configuration](/typescript-sdk/models) for detailed information about supported providers, configuration options, and examples.

## Configuring StopWhen

Control stopping conditions to prevent infinite loops:

```typescript
// Agent level - limit transfers between Sub Agents
agent({
  id: "support-agent",
  stopWhen: {
    transferCountIs: 5  // Max transfers in one conversation
  },
});

// Sub Agent level - limit generation steps
subAgent({
  id: "my-sub-agent",
  stopWhen: {
    stepCountIs: 20  // Max tool calls + LLM responses
  },
});
```

**Configuration levels:**

* `transferCountIs`: Project or Agent level
* `stepCountIs`: Project or Sub Agent level

Settings inherit from Project → Agent → Sub Agent.

## Sub Agent overview

Beyond model configuration, Sub Agents define tools, structured outputs, and agent-to-agent relationships available to the Sub Agent.

| Parameter            | Type     | Required | Description                                                                                                                                                         |
| -------------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                 | string   | Yes      | Stable Sub Agent identifier used for consistency and persistence                                                                                                    |
| `name`               | string   | Yes      | Human-readable name for the Sub Agent                                                                                                                               |
| `prompt`             | string   | Yes      | Detailed behavior guidelines and system prompt for the Sub Agent                                                                                                    |
| `description`        | string   | No       | Brief description of the Sub Agent's purpose and capabilities                                                                                                       |
| `models`             | object   | No       | Model configuration for this Sub Agent. See [Model Configuration](/typescript-sdk/models)                                                                           |
| `stopWhen`           | object   | No       | Stop conditions (`stepCountIs`). See [Configuring StopWhen](#configuring-stopwhen)                                                                                  |
| `canUse`             | function | No       | Returns the list of MCP/tools the Sub Agent can use. See [MCP Servers](/tutorials/mcp-servers/overview) for how to find or build MCP servers                        |
| `dataComponents`     | array    | No       | Structured output components for rich, interactive responses. See [Data Components](/typescript-sdk/structured-outputs/data-components)                             |
| `artifactComponents` | array    | No       | Components for handling tool or Sub Agent outputs. See [Artifact Components](/typescript-sdk/structured-outputs/artifact-components)                                |
| `canTransferTo`      | function | No       | Function returning array of Sub Agents this Sub Agent can transfer to. See [Transfer Relationships](/typescript-sdk/agent-relationships#transfer-relationships)     |
| `canDelegateTo`      | function | No       | Function returning array of Sub Agents this Sub Agent can delegate to. See [Delegation Relationships](/typescript-sdk/agent-relationships#delegation-relationships) |

### Tools & MCPs

Enable tools for a Sub Agent to perform actions like looking up information or calling external APIs.

Tools can be:

* **[MCP Servers](/typescript-sdk/tools/mcp-servers)** - Connect to external services and APIs using the Model Context Protocol
* **[Function Tools](/typescript-sdk/tools/function-tools)** - Custom JavaScript functions that execute directly in secure sandboxes

```typescript
import { subAgent, functionTool, mcpTool } from "@inkeep/agents-sdk";

const mySubAgent = subAgent({
  id: "my-agent-id",
  name: "My Sub Agent",
  prompt: "Detailed behavior guidelines",
  canUse: () => [
    functionTool({
      name: "get-current-time",
      description: "Get the current time",
      execute: async () => ({ time: new Date().toISOString() }),
    }),
    mcpTool({
      id: "inkeep-kb-rag",
      name: "Knowledge Base Search",
      description: "Search the company knowledge base.",
      serverUrl: "https://rag.inkeep.com/mcp",
    }),
  ],
});
```

### Data components

Structured output components for rich, interactive responses. See [Data Components](/typescript-sdk/structured-outputs/data-components).

```typescript
import { z } from 'zod';

const mySubAgent = subAgent({
  id: "my-agent-id",
  name: "My Sub Agent",
  prompt: "Detailed behavior guidelines",
  dataComponents: [
    {
      id: "customer-info",
      name: "CustomerInfo",
      description: "Customer information display component",
      props: z.object({
        name: z.string().describe("Customer name"),
        email: z.string().describe("Customer email"),
        issue: z.string().describe("Customer issue description"),
      }),
    },
  ],
});
```

### Artifact components

Components for handling tool or Sub Agent outputs. See [Artifact Components](/typescript-sdk/structured-outputs/artifact-components).

```typescript
import { z } from 'zod';
import { preview } from '@inkeep/agents-core';

const mySubAgent = subAgent({
  id: "my-agent-id",
  name: "My Sub Agent",
  prompt: "Detailed behavior guidelines",
  artifactComponents: [
    {
      id: "customer-info",
      name: "CustomerInfo",
      description: "Customer information display component",
      props: z.object({
        name: preview(z.string().describe("Customer name")),
        customer_info: z.string().describe("Customer information"),
      }),
    },
  ],
});
```

### Sub Agent relationships

Define other Sub Agents this Sub Agent can transfer control to or delegate tasks to.

```typescript
const mySubAgent = subAgent({
  // ...
  canTransferTo: () => [subAgent1],
  canDelegateTo: () => [subAgent2],
});
```

As a next step, see [Sub Agent Relationships](/typescript-sdk/agent-relationships) to learn how to design transfer and delegation relationships between Sub Agents.


# CLI Observability with Langfuse
URL: /typescript-sdk/cli-observability

Track LLM operations during pull command with Langfuse

***

title: CLI Observability with Langfuse
description: Track LLM operations during pull command with Langfuse
-------------------------------------------------------------------

The Inkeep CLI includes built-in observability for tracking LLM operations during the `pull` command. This allows you to monitor costs, latency, and quality of AI-generated code across different LLM providers.

## Overview

When you run `inkeep pull`, the CLI uses LLMs to generate TypeScript files for your agents, tools, and components. With Langfuse integration enabled, you can:

* **Track token usage and costs** across Anthropic, OpenAI, and Google models
* **Monitor generation latency** to identify slow operations
* **View complete traces** of multi-file code generation
* **Analyze placeholder optimization** impact on token savings
* **Debug failed generations** with full context

## Setup

### 1. Create a Langfuse Account

Sign up for a free account at [cloud.langfuse.com](https://cloud.langfuse.com) (EU region) or [us.cloud.langfuse.com](https://us.cloud.langfuse.com) (US region).

### 2. Get API Keys

From your Langfuse dashboard:

1. Navigate to **Settings** → **API Keys**
2. Create a new API key pair
3. Copy both the **Secret Key** (`sk-lf-...`) and **Public Key** (`pk-lf-...`)

### 3. Configure Environment Variables

Add these variables to your `.env` file in your project root:

```bash
# Enable Langfuse tracing
LANGFUSE_ENABLED=true

# Your Langfuse credentials
LANGFUSE_SECRET_KEY=sk-lf-your-secret-key-here
LANGFUSE_PUBLIC_KEY=pk-lf-your-public-key-here

# Langfuse API URL (defaults to EU cloud)
LANGFUSE_BASEURL=https://cloud.langfuse.com  # or https://us.cloud.langfuse.com for US

# Your LLM provider API keys (at least one required)
ANTHROPIC_API_KEY=your-anthropic-key
OPENAI_API_KEY=your-openai-key
GOOGLE_GENERATIVE_AI_API_KEY=your-google-key
```

### 4. Run Pull Command

Now when you run `inkeep pull`, all LLM operations will be traced to Langfuse:

```bash
inkeep pull --project my-agent-project
```

## Viewing Traces

### In Langfuse Dashboard

1. Go to your [Langfuse dashboard](https://cloud.langfuse.com)
2. Navigate to **Traces**
3. You'll see traces for each file generation operation

### Trace Metadata

Each trace includes rich metadata:

| Field              | Description                  | Example                           |
| ------------------ | ---------------------------- | --------------------------------- |
| `fileType`         | Type of file being generated | `agent`, `tool`, `data_component` |
| `placeholderCount` | Number of placeholders used  | `5`                               |
| `promptSize`       | Size of prompt in characters | `15234`                           |
| `model`            | LLM model used               | `claude-sonnet-4-5`               |

### Example Trace Structure

```
Service: inkeep-agents-cli
├── generate-agent-file
│   ├── Model: claude-sonnet-4-5
│   ├── Tokens: 12,543 input / 3,421 output
│   ├── Duration: 8.3s
│   └── Metadata:
│       ├── fileType: agent
│       ├── placeholderCount: 12
│       └── promptSize: 25,891 chars
```

## Monitoring Strategies

### Track Costs by Provider

Compare costs across different LLM providers:

1. Filter traces by model in Langfuse
2. View cumulative costs in the **Usage** dashboard
3. Identify cost-saving opportunities

### Optimize Generation Time

Find slow generation steps:

1. Sort traces by duration
2. Check if complex agents need longer timeouts
3. Consider using faster models for simpler files

### Analyze Token Savings

Monitor placeholder optimization impact:

1. Look at `placeholderCount` metadata
2. Higher counts = more token savings
3. Useful for understanding efficiency gains

## Troubleshooting

### Traces Not Appearing

**Check if Langfuse is enabled:**

```bash
# Should output: true
echo $LANGFUSE_ENABLED
```

**Verify API keys are set:**

```bash
# Should show your keys (without exposing them)
env | grep LANGFUSE
```

**Check for errors:**

```bash
# Run with debug logging
DEBUG=* inkeep pull --project my-project
```

### Missing Metadata

If traces appear but lack metadata:

1. Ensure you're using the latest CLI version
2. Check that file type context is being passed correctly
3. Report issues on [GitHub](https://github.com/anthropics/claude-code/issues)

## Privacy Considerations

### What Data is Sent to Langfuse

* **Prompt content**: The full prompts sent to LLMs (includes your project data)
* **Generated code**: The TypeScript code generated by LLMs
* **Model metadata**: Model names, token counts, timings
* **File metadata**: File types, sizes, placeholder counts

### What is NOT Sent

* **Your API keys**: LLM provider keys are never sent to Langfuse
* **Other environment variables**: Only Langfuse-specific vars are used

### Self-Hosted Option

For complete control over your data, you can self-host Langfuse:

```bash
# Use your self-hosted instance
LANGFUSE_BASEURL=https://langfuse.your-domain.com
```

See [Langfuse self-hosting docs](https://langfuse.com/docs/deployment/self-host) for details.

## Best Practices

1. **Enable for development**: Keep tracing on during development to catch issues early
2. **Disable in CI/CD**: Turn off for automated builds to avoid unnecessary traces
3. **Review weekly**: Check Langfuse dashboard weekly to monitor costs and performance
4. **Set budgets**: Configure spending alerts in your LLM provider dashboards

## Related Documentation

* [SignOz Usage](/typescript-sdk/signoz-usage) - OpenTelemetry tracing for runtime operations
* [Langfuse Usage](/typescript-sdk/langfuse-usage) - Langfuse integration for agent runtime
* [CLI Reference](/typescript-sdk/cli-reference) - Complete CLI command reference


# CLI Reference
URL: /typescript-sdk/cli-reference

Complete reference for the Inkeep CLI commands

***

title: CLI Reference
description: Complete reference for the Inkeep CLI commands
icon: "LuTerminal"
------------------

## Overview

The Inkeep CLI is the primary tool for interacting with the Inkeep Agent Framework. It allows you to push Agent configurations and interact with your multi-agent system.

## Installation

```bash
# Install the CLI globally
npm install -g @inkeep/agents-cli

# Install the dashboard package (for visual agents orchestration)
npm install @inkeep/agents-manage-ui
```

## Global Options

All commands support the following global options:

* `--version` - Display CLI version
* `--help` - Display help for a command

## Commands

### `inkeep init`

Initialize a new Inkeep configuration file in your project.

```bash
inkeep init [path]
```

**Options:**

* `--no-interactive` - Skip interactive path selection
* `--config <path>` - Path to use as template for new configuration

**Examples:**

```bash
# Interactive initialization
inkeep init

# Initialize in specific directory
inkeep init ./my-project

# Non-interactive mode
inkeep init --no-interactive

# Use specific config as template
inkeep init --config ./template-config.ts
```

### `inkeep push`

**Primary use case:** Push a project containing Agent configurations to your server. This command deploys your entire multi-agent project, including all Agents, Sub Agents, and tools.

```bash
inkeep push
```

**Options:**

* `--project <project-id>` - Project ID or path to project directory
* `--env <environment>` - Load environment-specific credentials from `environments/<environment>.env.ts`
* `--config <path>` - Override config file path (bypasses automatic config discovery)
* `--tenant-id <id>` - Override tenant ID
* `--agents-manage-api-url <url>` - Override the management API URL from config
* `--agents-run-api-url <url>` - Override agents run API URL
* `--json` - Generate project data as JSON file instead of pushing to server

**Examples:**

```bash
# Push project from current directory
inkeep push

# Push specific project directory
inkeep push --project ./my-project

# Push with development environment credentials
inkeep push --env development

# Generate project JSON without pushing
inkeep push --json

# Override tenant ID
inkeep push --tenant-id my-tenant

# Override API URLs
inkeep push --agents-manage-api-url https://api.example.com
inkeep push --agents-run-api-url https://run.example.com

# Use specific config file
inkeep push --config ./custom-config/inkeep.config.ts
```

**Environment Credentials:**

The `--env` flag loads environment-specific credentials when pushing your project. This will look for files like `environments/development.env.ts` or `environments/production.env.ts` in your project directory and load the credential configurations defined there.

**Example environment file:**

```typescript
// environments/development.env.ts
import { CredentialStoreType } from "@inkeep/agents-core";
import { registerEnvironmentSettings } from "@inkeep/agents-sdk";

export const development = registerEnvironmentSettings({
  credentials: {
    "api-key-dev": {
      id: "api-key-dev",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "API_KEY_DEV",
      },
    },
  },
});
```

#### Project Discovery and Structure

The `inkeep push` command follows this discovery process:

1. **Config File Discovery**: Searches for `inkeep.config.ts` using this pattern:

   * Starts from current working directory
   * Traverses **upward** through parent directories until found
   * Can be overridden by providing a path to the config file with the `--config` flag

2. **Workspace Structure**: Expects this directory layout:

   ```
   workspace-root/
   ├── package.json              # Workspace package.json
   ├── tsconfig.json             # Workspace TypeScript config
   ├── inkeep.config.ts          # Inkeep configuration file
   ├── my-project/               # Individual project directory
   │   ├── index.ts              # Project entry point
   │   ├── agents/               # Agent definitions
   │   │   └── *.ts
   │   ├── tools/                # Tool definitions
   │   │   └── *.ts
   │   ├── data-components/      # Data component definitions
   │   │   └── *.ts
   │   └── environments/         # Environment-specific configs
   │       ├── development.env.ts
   │       └── production.env.ts
   └── another-project/          # Additional projects
       └── index.ts
   ```

3. **Resource Compilation**: Automatically discovers and compiles:
   * All project directories containing `index.ts`
   * All TypeScript files within each project directory
   * Categorizes files by type (agents, Sub Agents, tools, data components)
   * Resolves dependencies and relationships within each project

#### Push Behavior

When pushing, the CLI:

* Finds and loads configuration from `inkeep.config.ts` at workspace root
* Discovers all project directories containing `index.ts`
* Applies environment-specific settings if `--env` is specified
* Compiles all project resources defined in each project's `index.ts`
* Validates Sub Agent relationships and tool configurations across all projects
* Deploys all projects to the management API
* Prints deployment summary with resource counts per project

### `inkeep pull`

Pull project configuration from the server and update all TypeScript files in your local project using LLM generation.

```bash
inkeep pull
```

**Options:**

* `--project <project-id>` - Project ID to pull (or path to project directory). If in project directory, validates against local project ID.
* `--config <path>` - Path to configuration file
* `--env <environment>` - Environment file to generate (development, staging, production). Defaults to development
* `--json` - Output project data as JSON instead of generating files
* `--debug` - Enable debug logging
* `--verbose` - Enable verbose logging
* `--force` - Force regeneration even if no changes detected
* `--introspect` - Completely regenerate all files from scratch (no comparison needed)

**Smart Project Detection:**

The pull command intelligently handles different scenarios:

1. **Project Directory Detection**: If your current directory contains an `index.ts` file that exports a project, the command automatically uses that project's ID
2. **Project ID Validation**: If you specify `--project` while in a project directory, it validates that the ID matches your local project
3. **Subdirectory Creation**: When not in a project directory, creates a new subdirectory named after the project ID

**`--project` Flag Behavior:**

The `--project` flag has dual functionality:

* **Directory Path**: If the value points to a directory containing `index.ts`, it uses that directory
* **Project ID**: If the value doesn't match a valid directory path, it treats it as a project ID

**Pull Modes:**

| Scenario                 | Command                                | Behavior                                                         |
| ------------------------ | -------------------------------------- | ---------------------------------------------------------------- |
| In project directory     | `inkeep pull`                          | ✅ Automatically detects project, pulls to current directory      |
| In project directory     | `inkeep pull --project <matching-id>`  | ✅ Validates ID matches local project, pulls to current directory |
| In project directory     | `inkeep pull --project <different-id>` | ❌ Error: Project ID doesn't match local project                  |
| Not in project directory | `inkeep pull`                          | ❌ Error: Requires --project flag                                 |
| Not in project directory | `inkeep pull --project <id>`           | ✅ Creates `<id>/` subdirectory with project files                |

**How it Works:**

The pull command discovers and updates all TypeScript files in your project based on the latest configuration from the server:

1. **File Discovery**: Recursively finds all `.ts` files in your project (excluding `environments/` and `node_modules/`)
2. **Smart Categorization**: Categorizes files as index, agents, Sub Agents, tools, or other files
3. **Context-Aware Updates**: Updates each file with relevant context from the server:
   * **Agent files**: Updated with specific agent data
   * **Sub Agent files**: Updated with specific Sub Agent configurations
   * **Tool files**: Updated with specific tool definitions
   * **Other files**: Updated with full project context
4. **LLM Generation**: Uses AI to maintain code structure while updating with latest data

#### TypeScript Updates (Default)

By default, the pull command updates your existing TypeScript files using LLM generation:

1. **Context Preservation**: Maintains your existing code structure and patterns
2. **Selective Updates**: Only updates relevant parts based on server configuration changes
3. **File-Specific Context**: Each file type receives appropriate context (Agents get Agent data, Sub Agents get Sub Agent data, etc.)

**Examples:**

```bash
# Directory-aware pull: Automatically detects project from current directory
cd my-project  # Directory contains index.ts with project export
inkeep pull    # Pulls to current directory, no subdirectory created

# Validate project ID while in project directory
cd my-project  # Directory contains index.ts
inkeep pull --project my-project  # Validates ID matches, pulls to current directory

# Error case: Wrong project ID in project directory
cd my-project  # Directory contains index.ts with different project ID
inkeep pull --project different-project  # ERROR: Project ID mismatch

# Pull when NOT in a project directory (requires --project)
cd ~/projects
inkeep pull  # ERROR: Requires --project flag

# Pull specific project to new subdirectory
cd ~/projects
inkeep pull --project my-project  # Creates ./my-project/ subdirectory

# Save project data as JSON file instead of updating files
inkeep pull --json

# Enable debug logging
inkeep pull --debug

# Enable verbose logging  
inkeep pull --verbose

# Force regeneration even if no changes detected
inkeep pull --force

# Completely regenerate all files from scratch
inkeep pull --introspect

# Generate environment-specific credentials
inkeep pull --env production

# Use specific config file
inkeep pull --config ./custom-config/inkeep.config.ts
```

#### Model Configuration

The `inkeep pull` command automatically selects the best available model for LLM generation based on your API keys:

1. **Anthropic Claude** (if `ANTHROPIC_API_KEY` is set): `claude-sonnet-4-5`
2. **OpenAI GPT** (if `OPENAI_API_KEY` is set): `gpt-5.1`
3. **Google Gemini** (if `GOOGLE_GENERATIVE_AI_API_KEY` is set): `gemini-2.5-flash`

The models are used for intelligent content merging when updating modified components, ensuring your local customizations are preserved while incorporating upstream changes.

#### Validation Process

The `inkeep pull` command includes a two-stage validation process to ensure generated TypeScript files accurately represent your backend configuration:

**1. Basic File Verification**

* Checks that all expected files exist (index.ts, agent files, tool files, component files)
* Verifies file naming conventions match (kebab-case)
* Ensures project export is present in index.ts

**2. Round-Trip Validation** *(New in v0.24.0)*

* Loads the generated TypeScript using the same logic as `inkeep push`
* Serializes it back to JSON format
* Compares the serialized JSON with the original backend data
* Reports any differences found

This round-trip validation ensures:

* ✅ Generated TypeScript can be successfully loaded and imported
* ✅ The serialization logic (TS → JSON) works correctly
* ✅ Generated files will work with `inkeep push` without errors
* ✅ No data loss or corruption during the pull process

**Validation Output:**

```bash
✓ Basic file verification passed
✓ Round-trip validation passed - generated TS matches backend data
```

**If validation fails:**

The CLI will display specific differences between the generated and expected data:

```bash
✗ Round-trip validation failed

❌ Round-trip validation errors:
   The generated TypeScript does not serialize back to match the original backend data.
  • Value mismatch at agents.my-agent.name: "Original Name" vs "Generated Name"
  • Missing tool in generated: tool-id

⚠️  This indicates an issue with LLM generation or schema mappings.
The generated files may not work correctly with `inkeep push`.
```

**TypeScript generation fails:**

* Ensure your network connectivity and API endpoints are correct
* Check that your model provider credentials (if required by backend) are set up
* Try using `--json` flag as a fallback to get the raw project data

**Validation errors during pull:**

* The generated TypeScript may have syntax errors or missing dependencies
* Check the generated file manually for obvious issues
* Try pulling as JSON first to verify the source data: `inkeep pull --json`
* If round-trip validation fails, report the issue with the error details

### `inkeep list-agents`

List all available agents for a specific project.

```bash
inkeep list-agents --project <project-id>
```

**Options:**

* `--project <project-id>` - **Required.** Project ID to list agents for
* `--tenant-id <tenant-id>` - Tenant ID
* `--agents-manage-api-url <url>` - Agents manage API URL
* `--config <path>` - Path to configuration file
* `--config-file-path <path>` - Path to configuration file (deprecated, use --config)

**Examples:**

```bash
# List agents for a specific project
inkeep list-agents --project my-project

# List agents using a specific config file
inkeep list-agents --project my-project --config ./inkeep.config.ts

# Override tenant and API URL
inkeep list-agents --project my-project --tenant-id my-tenant --agents-manage-api-url https://api.example.com
```

### `inkeep dev`

Start the Inkeep dashboard server, build for production, or export the Next.js project.

> **Note:** This command requires `@inkeep/agents-manage-ui` to be installed for visual agents orchestration.

```bash
inkeep dev
```

**Options:**

* `--port <port>` - Port to run the server on (default: 3000)
* `--host <host>` - Host to bind the server to (default: localhost)
* `--build` - Build the Dashboard UI for production (packages standalone build)
* `--export` - Export the Next.js project source files
* `--output-dir <dir>` - Output directory for build files (default: ./inkeep-dev)
* `--path` - Output the path to the Dashboard UI

**Examples:**

```bash
# Start development server
inkeep dev

# Start on custom port and host
inkeep dev --port 3001 --host 0.0.0.0

# Build for production (packages standalone build)
inkeep dev --build --output-dir ./build

# Export Next.js project source files
inkeep dev --export --output-dir ./my-dashboard

# Get dashboard path for deployment
DASHBOARD_PATH=$(inkeep dev --path)
echo "Dashboard built at: $DASHBOARD_PATH"

# Use with Vercel
vercel --cwd $(inkeep dev --path) -Q .vercel build

# Use with Docker
docker build -t inkeep-dashboard $(inkeep dev --path)

# Use with other deployment tools
rsync -av $(inkeep dev --path)/ user@server:/var/www/dashboard/
```

### `inkeep config`

Manage Inkeep configuration values.

**Subcommands:**

#### `inkeep config get [key]`

Get configuration value(s).

```bash
inkeep config get [key]
```

**Options:**

* `--config <path>` - Path to configuration file
* `--config-file-path <path>` - Path to configuration file (deprecated, use --config)

**Examples:**

```bash
# Get all config values
inkeep config get

# Get specific value
inkeep config get tenantId
```

#### `inkeep config set <key> <value>`

Set a configuration value.

```bash
inkeep config set <key> <value>
```

**Options:**

* `--config <path>` - Path to configuration file
* `--config-file-path <path>` - Path to configuration file (deprecated, use --config)

**Examples:**

```bash
inkeep config set tenantId my-tenant-id
inkeep config set apiUrl http://localhost:3002
```

#### `inkeep config list`

List all configuration values.

```bash
inkeep config list
```

**Options:**

* `--config <path>` - Path to configuration file
* `--config-file-path <path>` - Path to configuration file (deprecated, use --config)

### `inkeep add`

Pull a template project or MCP from the [Inkeep Agents Cookbook](https://github.com/inkeep/agents/tree/main/agents-cookbook).

```bash
inkeep add [options]
```

**Options:**

* `--project <name>` - Add a project template
* `--mcp <name>` - Add a custom MCP server template for common use cases (adds server code to your project)
* `--target-path <path>` - Target path to add the template to
* `--config <path>` - Path to configuration file

**Examples:**

```bash
# List available templates (both project and MCP)
inkeep add

# Add a project template
inkeep add --project activities-planner

# Add project template to specific path
inkeep add --project activities-planner --target-path ./examples

# Add a custom MCP server template (auto-detects apps/mcp/app directory)
inkeep add --mcp zendesk

# Add MCP server template to specific path
inkeep add --mcp zendesk --target-path ./apps/mcp/app

# Using specific config file
inkeep add --project activities-planner --config ./my-config.ts
```

**Behavior:**

* When adding an MCP server template without `--target-path`, the CLI automatically searches for an `apps/mcp/app` directory in your project
* If no app directory is found, you'll be prompted to confirm whether to add to the current directory
* Project templates are added to the current directory or specified `--target-path`
* Model configurations are automatically injected based on available API keys in your environment (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_GENERATIVE_AI_API_KEY`)

### `inkeep update`

Update the Inkeep CLI to the latest version from npm.

```bash
inkeep update
```

**Options:**

* `--check` - Check for updates without installing
* `--force` - Force update even if already on latest version

**How it Works:**

The update command automatically:

1. **Detects Package Manager**: Identifies which package manager (npm, pnpm, bun, or yarn) was used to install the CLI globally
2. **Checks Version**: Compares your current version with the latest available on npm
3. **Updates CLI**: Executes the appropriate update command for your package manager
4. **Displays Changelog**: Shows a link to the changelog for release notes

**Examples:**

```bash
# Check if an update is available (no installation)
inkeep update --check

# Update to latest version (with confirmation prompt)
inkeep update

# Force reinstall current version
inkeep update --force

# Skip confirmation prompt (useful for CI/CD)
inkeep update --force
```

**Output Example:**

```
📦 Version Information:
  • Current version: 0.22.3
  • Latest version:  0.23.0

📖 Changelog:
  • https://github.com/inkeep/agents/blob/main/agents-cli/CHANGELOG.md

🔍 Detected package manager: pnpm

✅ Updated to version 0.23.0
```

**Troubleshooting:**

If you encounter permission errors, try running with elevated permissions:

```bash
# For npm, pnpm, yarn
sudo inkeep update

# For bun
sudo -E bun add -g @inkeep/agents-cli@latest
```

**Package Manager Detection:**

The CLI automatically detects which package manager you used by checking global package installations:

* npm: Checks `npm list -g @inkeep/agents-cli`
* pnpm: Checks `pnpm list -g @inkeep/agents-cli`
* bun: Checks `bun pm ls -g`
* yarn: Checks `yarn global list`

If automatic detection fails, the CLI will prompt you to select your package manager.

## Configuration File

The CLI uses a configuration file (typically `inkeep.config.ts`) to store settings:

```typescript
import { defineConfig } from "@inkeep/agents-cli/config";

export default defineConfig({
  tenantId: "your-tenant-id",
  agentsManageApiUrl: "http://localhost:3002",
  agentsRunApiUrl: "http://localhost:3003",
});
```

### Configuration Priority

Effective resolution order:

1. Command-line flags (highest)
2. Environment variables (override config values)
3. `inkeep.config.ts` values

## Environment Variables

The CLI and SDK respect the following environment variables:

* `INKEEP_TENANT_ID` - Tenant identifier
* `INKEEP_AGENTS_MANAGE_API_URL` - Management API base URL
* `INKEEP_AGENTS_RUN_API_URL` - Run API base URL
* `INKEEP_ENV` - Environment name for credentials loading during `inkeep push`
* `INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET` - Optional bearer for Manage API (advanced)
* `INKEEP_AGENTS_RUN_API_BYPASS_SECRET` - Optional bearer for Run API (advanced)

## Troubleshooting

**Project Not Found:**

* Projects are automatically managed based on your tenantId
* `inkeep push` will create resources as needed

### Getting Help

For additional help with any command:

```bash
inkeep [command] --help
```

For issues or feature requests, visit: [GitHub Issues](https://github.com/inkeep/agents/issues)


# Configuration Management
URL: /typescript-sdk/configuration

Configure your Inkeep Agent workspace with inkeep.config.ts - workspace-level settings for all agents and CLI commands

***

title: Configuration Management
description: Configure your Inkeep Agent workspace with inkeep.config.ts - workspace-level settings for all agents and CLI commands
icon: "LuSettings"
------------------

## Overview

Inkeep Agent projects use a hierarchical configuration system that combines file-based configuration, environment variables, and command-line overrides. This flexible approach supports different deployment environments while maintaining developer-friendly defaults.

## Configuration File Format

### `inkeep.config.ts`

The **workspace-level** configuration file for your Inkeep project. This file defines settings that apply to your entire workspace, including:

* **Tenant and project identification** for organizing your agents
* **API endpoints** for the Management and Runtime APIs
* **Authentication credentials** for secure API access
* **Model configuration** for AI models (required at least base model)
* **Output directories** for generated files

:::tip
`inkeep.config.ts` is typically placed at the **root of your workspace** (not within individual packages or subdirectories). All CLI commands in the workspace will discover and use this configuration automatically.
:::

The configuration file supports both nested (recommended) and flat configuration formats:

#### Nested Format (Recommended)

```typescript
import { defineConfig } from '@inkeep/agents-cli/config';
import 'dotenv/config';

export default defineConfig({
  // Required: Your tenant identifier
  tenantId: 'my-company',

  // Management API configuration
  agentsManageApi: {
    url: 'http://localhost:3002',
    apiKey: process.env.MANAGE_API_KEY, // Optional: API key for authentication
  },

  // Runtime API configuration
  agentsRunApi: {
    url: 'http://localhost:3003',
    apiKey: process.env.RUN_API_KEY, // Optional: API key for authentication
  },

  // Required: Model configuration (at least base model)
  models: {
    base: {
      model: 'anthropic/claude-sonnet-4-5',
      providerOptions: {
        temperature: 0.7,
        maxOutputTokens: 2048
      }
    }
  },

  // Optional: Output directory for generated files
  outputDirectory: './output',
});
```

#### Flat Format (Deprecated - Legacy Only)

:::warning
**Deprecated:** The flat configuration format is maintained for backward compatibility only. New projects should use the nested format above.
:::

```typescript
import { defineConfig } from '@inkeep/agents-cli/config';

export default defineConfig({
  // Required: Your tenant identifier
  tenantId: 'my-company',

  // API endpoints (legacy format - DEPRECATED)
  agentsManageApiUrl: 'http://localhost:3002', // ⚠️ Use agentsManageApi.url instead
  agentsRunApiUrl: 'http://localhost:3003',     // ⚠️ Use agentsRunApi.url instead
});
```

### Configuration Options

#### Nested Format Options

| Option                   | Type     | Description                                        | Default                   |
| ------------------------ | -------- | -------------------------------------------------- | ------------------------- |
| `tenantId`               | `string` | **Required.** Unique identifier for your tenant    | -                         |
| `agentsManageApi`        | `object` | Management API configuration                       | -                         |
| `agentsManageApi.url`    | `string` | Management API endpoint URL                        | `'http://localhost:3002'` |
| `agentsManageApi.apiKey` | `string` | Optional API key for Management API authentication | -                         |
| `agentsRunApi`           | `object` | Runtime API configuration                          | -                         |
| `agentsRunApi.url`       | `string` | Runtime API endpoint URL                           | `'http://localhost:3003'` |
| `agentsRunApi.apiKey`    | `string` | Optional API key for Runtime API authentication    | -                         |
| `outputDirectory`        | `string` | Output directory for generated files               | -                         |
| `manageUiUrl`            | `string` | Optional Management UI URL                         | `'http://localhost:3000'` |

#### Flat Format Options (Deprecated - Legacy)

| Option               | Type     | Description                                                                   | Default                   |
| -------------------- | -------- | ----------------------------------------------------------------------------- | ------------------------- |
| `tenantId`           | `string` | **Required.** Unique identifier for your tenant                               | -                         |
| `agentsManageApiUrl` | `string` | **⚠️ Deprecated.** Management API endpoint. Use `agentsManageApi.url` instead | `'http://localhost:3002'` |
| `agentsRunApiUrl`    | `string` | **⚠️ Deprecated.** Runtime API endpoint. Use `agentsRunApi.url` instead       | `'http://localhost:3003'` |
| `outputDirectory`    | `string` | Output directory for generated files                                          | -                         |
| `manageUiUrl`        | `string` | Optional Management UI URL                                                    | `'http://localhost:3000'` |

**Note:** API keys should be provided via the config file (using environment variables) rather than using legacy `INKEEP_AGENTS_*_BYPASS_SECRET` environment variables.

## Workspace Structure

The `inkeep.config.ts` file is a **workspace-level configuration** that applies to all agent definitions and CLI commands within your project. Here's a typical workspace structure:

```
my-agent-workspace/
├── inkeep.config.ts          # Workspace configuration (shared)
├── .env                       # Environment variables
├── package.json
├── agents/                    # Your agent definitions
│   ├── qa-agent.ts
│   ├── support-agent.ts
│   └── router.ts
└── tools/                     # Custom tools (optional)
    └── search-tool.ts
```

**Key points:**

* **Single config per workspace**: One `inkeep.config.ts` at the workspace root
* **Shared settings**: All agent files use the same tenant, API endpoints, and credentials
* **CLI discovery**: Commands run from any subdirectory will find the root config
* **Monorepo support**: In monorepos, place config at the root or use `--config` flag

## Config File Discovery

The CLI uses a sophisticated discovery mechanism to locate your configuration:

```mermaid
graph TD
    A[CLI Command] --> B{--config flag provided?}
    B -->|Yes| C[Use specified config file]
    B -->|No| D[Start in current directory]
    D --> E{inkeep.config.ts exists?}
    E -->|Yes| F[Use found config]
    E -->|No| G[Check parent directory]
    G --> H{At filesystem root?}
    H -->|No| E
    H -->|Yes| I[Error: Config not found]
    C --> J[Load and validate config]
    F --> J
    J --> K[Apply environment overrides]
    K --> L[Apply CLI flag overrides]
    L --> M[Final configuration]
```

### Search Pattern

1. **Explicit Path**: If `--config` flag is provided, use that file directly
2. **Upward Search**: Starting from current working directory:
   * Look for `inkeep.config.ts` in current directory
   * If not found, move to parent directory
   * Repeat until found or reach filesystem root
   * Config file should be at the same level as `package.json`/`tsconfig.json`
3. **Error Handling**: If no config found, provide helpful error message

### Example Discovery

```bash
# Directory structure (workspace root)
/home/user/workspace/
├── package.json              # Workspace package.json
├── tsconfig.json             # Workspace TypeScript config
├── inkeep.config.ts          # ✅ Config file at workspace root
├── my-agents/                # Project directory
│   ├── index.ts              # Project entry point
│   └── subfolder/
│       └── current-location/ # CLI run from here
└── other-project/

# CLI searches: current-location → subfolder → my-agents → workspace → FOUND!
```

## Configuration Priority

Settings are resolved in this order (highest to lowest priority):

```mermaid
graph LR
    A[CLI Flags] --> B[Environment Variables]
    B --> C[Config File Values]
    C --> D[Built-in Defaults]

    style A fill:#ff6b6b
    style B fill:#ffa500
    style C fill:#4ecdc4
    style D fill:#95e1d3
```

### 1. CLI Flags (Highest Priority)

Command-line flags override all other settings:

```bash
# Override API URL
inkeep push --agents-manage-api-url https://api.production.com

# Override config file location
inkeep pull --config /path/to/custom.config.ts

# Override environment
inkeep push --env production
```

### 2. Environment Variables

Environment variables override config file values:

```bash
# Set via environment
export INKEEP_AGENTS_MANAGE_API_URL=https://api.staging.com
export INKEEP_TENANT_ID=staging-tenant
export INKEEP_ENV=staging

# Now CLI commands use these values
inkeep push
```

**Supported Environment Variables:**

| Variable                       | Config Equivalent    | Description                             |
| ------------------------------ | -------------------- | --------------------------------------- |
| `INKEEP_TENANT_ID`             | `tenantId`           | Tenant identifier                       |
| `INKEEP_AGENTS_MANAGE_API_URL` | `agentsManageApiUrl` | Management API URL                      |
| `INKEEP_AGENTS_RUN_API_URL`    | `agentsRunApiUrl`    | Runtime API URL                         |
| `INKEEP_ENV`                   | -                    | Environment name for credential loading |

### 3. Config File Values

Values explicitly set in your `inkeep.config.ts`:

```typescript
export default defineConfig({
  tenantId: 'my-tenant',
  agentsManageApiUrl: 'http://localhost:3002',
  // These values used unless overridden
});
```

### 4. Built-in Defaults (Lowest Priority)

Default values used when not specified elsewhere:

```typescript
const defaults = {
  agentsManageApiUrl: 'http://localhost:3002',
  agentsRunApiUrl: 'http://localhost:3003',
  apiTimeout: 30000,
  retryAttempts: 3,
};
```

## Advanced Configuration

### TypeScript Support

The config system is fully typed, providing IntelliSense and validation:

```typescript
import { defineConfig, ConfigOptions } from '@inkeep/agents-cli/config';

// Get full type safety
const config: ConfigOptions = {
  tenantId: 'my-tenant', // ✓ Required
  invalidOption: true,   // ✗ TypeScript error
};

export default defineConfig(config);
```

### Dynamic Configuration

You can use environment-based logic in your workspace config:

```typescript
// inkeep.config.ts at workspace root
import { defineConfig } from '@inkeep/agents-cli/config';

const isDevelopment = process.env.NODE_ENV === 'development';

export default defineConfig({
  tenantId: process.env.TENANT_ID || 'default-tenant',
  agentsManageApiUrl: isDevelopment
    ? 'http://localhost:3002'
    : 'https://api.production.com',
  apiTimeout: isDevelopment ? 60000 : 30000,
});
```

**Note**: This single config file manages all projects within the workspace.

### Multiple Configurations

For workspaces requiring different configurations:

```typescript
// inkeep.config.ts (main config at workspace root)
export default defineConfig({
  tenantId: 'production-tenant',
  agentsManageApiUrl: 'https://api.production.com',
});
```

```typescript
// inkeep.dev.config.ts (development config at workspace root)
export default defineConfig({
  tenantId: 'dev-tenant',
  agentsManageApiUrl: 'http://localhost:3002',
});
```

```bash
# Use development config (specify from any project directory)
inkeep push --config ../inkeep.dev.config.ts
# or with absolute path
inkeep push --config /path/to/workspace/inkeep.dev.config.ts
```

## Configuration Validation

The CLI validates configuration at runtime:

### Required Fields

```typescript
export default defineConfig({
  // ✗ Error: tenantId is required
});
```

### URL Validation

```typescript
export default defineConfig({
  tenantId: 'my-tenant',
  agentsManageApiUrl: 'invalid-url', // ✗ Error: Invalid URL format
});
```

### Type Validation

```typescript
export default defineConfig({
  tenantId: 'my-tenant',
  apiTimeout: 'thirty seconds', // ✗ Error: Expected number
});
```

## Debugging Configuration

### View Current Configuration

```bash
# View all configuration values
inkeep config get

# View specific value
inkeep config get tenantId

# View with specific config file
inkeep config get --config ./custom.config.ts
```

### Configuration Sources

The CLI shows where each setting comes from:

```bash
inkeep config get tenantId
# Output: my-tenant (from environment variable)

inkeep config get agentsManageApiUrl
# Output: http://localhost:3002 (from config file)
```

## Best Practices

### 1. Environment-Specific Configs

Use different configs for different environments:

```bash
# Development
inkeep.config.ts          # Local development settings

# Staging
inkeep.staging.config.ts  # Staging environment settings

# Production
inkeep.prod.config.ts     # Production environment settings
```

### 2. Secret Management

Never commit secrets to config files:

```typescript
// ✗ Bad: Hardcoded secrets
export default defineConfig({
  tenantId: 'my-tenant',
  apiKey: 'sk-secret-key', // Don't do this!
});

// ✓ Good: Use environment variables
export default defineConfig({
  tenantId: 'my-tenant',
  // API keys handled via environment-specific credential configs
});
```

### 3. Documentation

Document your configuration options:

```typescript
export default defineConfig({
  // Production tenant for main application
  tenantId: 'acme-corp-prod',

  // Use staging API for development
  agentsManageApi: {
    url: process.env.NODE_ENV === 'development'
      ? 'https://api-staging.acme.com'
      : 'https://api.acme.com',
    apiKey: process.env.MANAGE_API_KEY,
  },

  agentsRunApi: {
    url: process.env.NODE_ENV === 'development'
      ? 'https://run-staging.acme.com'
      : 'https://run.acme.com',
    apiKey: process.env.RUN_API_KEY,
  },
});
```

## Migration Guide

### Migrating from Flat to Nested Format

If you're using the legacy flat format, here's how to migrate to the new nested format:

**Before (Flat Format):**

```typescript
import { defineConfig } from '@inkeep/agents-cli/config';

export default defineConfig({
  tenantId: 'my-tenant',
  agentsManageApiUrl: 'http://localhost:3002',
  agentsRunApiUrl: 'http://localhost:3003',
});
```

**After (Nested Format):**

```typescript
import { defineConfig } from '@inkeep/agents-cli/config';
import 'dotenv/config';

export default defineConfig({
  tenantId: 'my-tenant',
  agentsManageApi: {
    url: 'http://localhost:3002',
    // Optional: Add API key for authentication
    apiKey: process.env.MANAGE_API_KEY,
  },
  agentsRunApi: {
    url: 'http://localhost:3003',
    // Optional: Add API key for authentication
    apiKey: process.env.RUN_API_KEY,
  },
});
```

**Benefits of the Nested Format:**

* **Explicit API Key Management**: Store API keys directly in config (via environment variables) with clear, organized structure
* **Better Organization**: Related configuration grouped together
* **Type Safety**: Improved IntelliSense and type checking
* **Future-Proof**: New API configuration options can be added without cluttering the top-level config
* **Cleaner Environment**: No need for legacy `INKEEP_AGENTS_*_BYPASS_SECRET` environment variables

**Backward Compatibility:**
The CLI fully supports both formats. You can continue using the flat format without any changes, or migrate at your convenience.

## Troubleshooting

### Config Not Found

```bash
Error: Could not find inkeep.config.ts
```

**Solutions:**

* Ensure `inkeep.config.ts` exists at **workspace root** (same level as `package.json`)
* CLI searches upward - make sure you're running from within the workspace
* Use `--config` flag to specify absolute or relative path to config file
* Check file name (must be exactly `inkeep.config.ts`)
* Verify you're not running from a completely separate directory tree

### Invalid Configuration

```bash
Error: Invalid configuration: tenantId is required
```

**Solutions:**

* Add required `tenantId` field
* Check for typos in field names
* Verify TypeScript compilation

### Environment Issues

```bash
Warning: INKEEP_TENANT_ID environment variable overrides config
```

**Solutions:**

* Unset environment variable: `unset INKEEP_TENANT_ID`
* Use `--config` to override with specific file
* Check `.env` files for conflicting values

The configuration system provides the flexibility to adapt your Inkeep Agent projects to different environments while maintaining consistency and type safety across your development workflow.


# Context Fetchers
URL: /typescript-sdk/context-fetchers

Learn how to use context fetchers to fetch data from external sources and make it available to your agents

***

title: Context Fetchers
description: Learn how to use context fetchers to fetch data from external sources and make it available to your agents
icon: "LuCirclePlus"
--------------------

## Overview

Context fetchers allow you to embed real-time data from external APIs into your agent prompts. Instead of hardcoding information in your agent prompt, context fetchers dynamically retrieve fresh data for each conversation.

## Key Features

* **Dynamic data retrieval**: Fetch real-time data from APIs.
* **Dynamic Prompting**: Use dynamic data in your agent prompts
* **Headers integration**: Use request-specific parameters to customize data fetching.
* **Data transformation**: Transform API responses into the exact format your agent needs.

## Context Fetchers vs Tools

* **Context Fetchers**: Pre-populate agent prompts with dynamic data
  * Run automatically before/during conversation startup
  * Data becomes part of the agent's system prompt
  * Perfect for: Personalized agent personas, dynamic agent guardrails
  * Example Prompt: `You are an assistant for ${userContext.toTemplate('user.name')} and you work for ${userContext.toTemplate('user.organization')}`

* **Tools**: Enable agents to take actions or fetch data during conversations
  * Called by the agent when needed during the conversation
  * Agent decides when and how to use them
  * Example Tool Usage: Agent calls a "send\_email" tool or "search\_database" tool

## Basic Usage

Let's create a simple context fetcher that retrieves user information:

```typescript
import { agent, subAgent } from "@inkeep/agents-sdk";
import { contextConfig, fetchDefinition, headers } from "@inkeep/agents-core";
import { z } from "zod";

// 1. Define a schema for headers validation. All header keys are converted to lowercase.
// In this example all incoming headers will be validated to make sure they include user_id and api_key.
const personalAgentHeaders = headers({
  schema: z.object({
    user_id: z.string(),
    api_key: z.string(),
  })
});

// 2. Create the fetcher with
const userFetcher = fetchDefinition({
  id: "user-info",
  name: "User Information",
  trigger: "initialization", // Fetch only once when a conversation is started with the Agent. When set to "invocation", the fetch will be executed every time a request is made to the Agent.
  fetchConfig: {
    url: `https://api.example.com/users/${personalAgentHeaders.toTemplate('user_id')}`,
    method: "GET",
    headers: {
      Authorization: `Bearer ${personalAgentHeaders.toTemplate('api_key')}`,
    },
    transform: "user", // Extract user from response, for example if the response is { "user": { "name": "John Doe", "email": "john.doe@example.com" } }, the transform will return the user object
  },
  responseSchema: z.object({
    user: z.object({
      name: z.string(),
      email: z.string(),
    }),
  }), // Used to validate the result of the transformed api response.
  defaultValue: "Unable to fetch user information",
});

// 3. Configure context
const personalAgentContext = contextConfig({
  headers: personalAgentHeaders,
  contextVariables: {
    user: userFetcher,
  },
});

// 4. Create and use the Sub Agent
const personalAssistant = subAgent({
  id: "personal-assistant",
  name: "Personal Assistant",
  description: "A personalized AI assistant",
  prompt: `Hello ${personalAgentContext.toTemplate('user.name')}! I'm your personal assistant.`,
});

// Initialize the Agent
export const myAgent = agent({
  id: "personal-agent",
  name: "Personal Assistant Agent",
  defaultSubAgent: personalAssistant,
  subAgents: () => [personalAssistant],
  contextConfig: personalAgentContext,
});
```

## Using Context Variables

Context variables can be used in your agent prompts using JSONPath template syntax `{{contextVariableKey.field_name}}`.
Use the context config's `toTemplate()` method for type-safe templating with autocomplete and validation.

```typescript
const personalGraphContext = contextConfig({
  headers: personalGraphHeaders,
  contextVariables: {
    user: userFetcher,
  },
});

const personalAgent = subAgent({
  id: "personal-agent",
  name: "Personal Assistant",
  description: "A personalized AI assistant",
  prompt: `Hello ${personalGraphContext.toTemplate('user.name')}! I'm your personal assistant.`,
});
```

Context variables are resolved using [JSONPath notation](https://jsonpath.com).

## Data transformation

The `transform` property on fetch definitions lets you extract exactly what you need from API responses using JSONPath notation:

```typescript
// API returns: { "user": { "profile": { "displayName": "John Doe" } } }
transform: "user.profile.displayName"; // Result: "John Doe"

// API returns: { "items": [{ "name": "First Item" }, { "name": "Second Item" }] }
transform: "items[0].name"; // Result: "First Item"
```

## Best Practices

1. **Use Appropriate Triggers**

   * `initialization`: Use when data rarely changes
   * `invocation`: Use for frequently changing data

2. **Handle Errors Gracefully**

   * Always provide a `defaultValue`
   * Use appropriate response schemas

## Related documentation

* [Headers](/typescript-sdk/headers) - Learn how to pass dynamic context to your agents via HTTP headers


# Data Operations
URL: /typescript-sdk/data-operations

Learn about data operations emitted by agents and how to use the x-emit-operations header to control their visibility.

***

title: Data Operations
sidebarTitle: Data Operations
description: Learn about data operations emitted by agents and how to use the x-emit-operations header to control their visibility.
icon: LuActivity
keywords: data operations, emit operations, debugging, agent events, x-emit-operations header, agent monitoring
---------------------------------------------------------------------------------------------------------------

## Overview

Data operations are detailed, real-time events that provide visibility into what agents are doing during execution. They include agent reasoning, tool executions, transfers, delegations, and artifact creation. By default, these operations are hidden from end users to keep the interface clean, but they can be enabled for debugging and monitoring purposes.

## The x-emit-operations Header

The `x-emit-operations` header controls whether data operations are included in the response stream. When set to `true`, the system will emit detailed operational events alongside the regular response content.

### Usage

```bash
curl -N \
  -X POST "http://localhost:3003/api/chat" \
  -H "Authorization: Bearer $INKEEP_API_KEY" \
  -H "Content-Type: application/json" \
  -H "x-emit-operations: true" \
  -d '{
    "messages": [
      { "role": "user", "content": "What can you do?" }
    ],
    "conversationId": "chat-1234"
  }'
```

### CLI Usage

In the CLI, you can toggle data operations using the `operations` command:

```bash
# Start a chat session
inkeep chat

# Toggle data operations on/off
> operations
🔧 Emit operations: ON
Data operations will be shown during responses.

> operations  
🔧 Emit operations: OFF
Data operations are hidden.
```

## Data Operation Types

### Agent Events

#### `agent_generate`

Emitted when an agent generates content (text or structured data).

```json
{
  "type": "data-operation",
  "data": {
    "type": "agent_generate",
    "label": "Agent search-agent generating response",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "parts": [
          {
            "type": "text",
            "content": "I found 5 relevant documents..."
          }
        ],
        "generationType": "text_generation"
      }
    }
  }
}
```

#### `agent_reasoning`

Emitted when an agent is reasoning through a request or planning its approach.

```json
{
  "type": "data-operation",
  "data": {
    "type": "agent_reasoning",
    "label": "Agent search-agent reasoning through request",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "parts": [
          {
            "type": "text",
            "content": "I need to search for information about..."
          }
        ]
      }
    }
  }
}
```

### Tool Execution Events

#### `tool_call`

Emitted when an agent starts calling a tool or function.

```json
{
  "type": "data-operation",
  "data": {
    "type": "tool_call",
    "label": "Tool call: search_documents",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "toolName": "search_documents",
        "args": {
          "query": "machine learning best practices",
          "limit": 10
        },
        "toolCallId": "call_abc123",
        "toolId": "tool_xyz789"
      }
    }
  }
}
```

#### `tool_result`

Emitted when a tool execution completes (success or failure).

```json
{
  "type": "data-operation",
  "data": {
    "type": "tool_result",
    "label": "Tool result: search_documents",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "toolName": "search_documents",
        "result": {
          "documents": [
            {
              "title": "ML Best Practices Guide",
              "url": "/docs/ml-guide",
              "relevance": 0.95
            }
          ]
        },
        "toolCallId": "call_abc123",
        "toolId": "tool_xyz789",
        "duration": 1250
      }
    }
  }
}
```

**Error Example:**

```json
{
  "type": "data-operation",
  "data": {
    "type": "tool_result",
    "label": "Tool error: search_documents",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "toolName": "search_documents",
        "result": null,
        "toolCallId": "call_abc123",
        "toolId": "tool_xyz789",
        "duration": 500,
        "error": "API rate limit exceeded"
      }
    }
  }
}
```

### Agent Interaction Events

#### `transfer`

Emitted when control is transferred from one agent to another.

```json
{
  "type": "data-operation",
  "data": {
    "type": "transfer",
    "label": "Agent transfer: search-agent → analysis-agent",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "fromSubAgent": "search-agent",
        "targetAgent": "analysis-agent",
        "reason": "Specialized analysis required",
        "context": {
          "searchResults": "...",
          "userQuery": "..."
        }
      }
    }
  }
}
```

#### `delegation_sent`

Emitted when an agent delegates a task to another agent.

```json
{
  "type": "data-operation",
  "data": {
    "type": "delegation_sent",
    "label": "Task delegated: coordinator-agent → search-agent",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "coordinator-agent",
      "data": {
        "delegationId": "deleg_xyz789",
        "fromSubAgent": "coordinator-agent",
        "targetAgent": "search-agent",
        "taskDescription": "Search for information about machine learning",
        "context": {
          "priority": "high",
          "deadline": "2024-01-15T10:00:00Z"
        }
      }
    }
  }
}
```

#### `delegation_returned`

Emitted when a delegated task is completed and returned.

```json
{
  "type": "data-operation",
  "data": {
    "type": "delegation_returned",
    "label": "Task completed: search-agent → coordinator-agent",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "search-agent",
      "data": {
        "delegationId": "deleg_xyz789",
        "fromSubAgent": "search-agent",
        "targetAgent": "coordinator-agent",
        "result": {
          "status": "completed",
          "documents": [...],
          "summary": "Found 5 relevant documents"
        }
      }
    }
  }
}
```

### Artifact Events

#### `artifact_saved`

Emitted when an agent creates or saves an artifact (document, chart, file, etc.).

```json
{
  "type": "data-operation",
  "data": {
    "type": "artifact_saved",
    "label": "Artifact saved: chart",
    "details": {
      "timestamp": 1726247200000,
      "agentId": "analysis-agent",
      "data": {
        "artifactId": "art_123456",
        "taskId": "task_789",
        "toolCallId": "tool_abc123",
        "artifactType": "chart",
        "summaryData": {
          "title": "Sales Performance Q4 2023",
          "type": "bar_chart"
        },
        "fullData": {
          "chartData": [...],
          "config": {...}
        },
        "metadata": {
          "createdBy": "analysis-agent",
          "version": "1.0"
        }
      }
    }
  }
}
```

## System Events

### `agent_initializing`

Emitted when the agent runtime is starting up.

```json
{
  "type": "data-operation",
  "data": {
    "type": "agent_initializing",
    "details": {
      "sessionId": "session_abc123",
      "agentId": "graph_xyz789"
    }
  }
}
```

### `completion`

Emitted when an agent completes its task.

```json
{
  "type": "data-operation",
  "data": {
    "type": "completion",
    "details": {
      "agent": "search-agent",
      "iteration": 1
    }
  }
}
```

### `error`

Emitted when an error occurs during execution.

```json
{
  "type": "data-operation",
  "data": {
    "type": "error",
    "message": "Tool execution failed: API rate limit exceeded",
    "agent": "search-agent",
    "severity": "error",
    "code": "RATE_LIMIT_EXCEEDED",
    "timestamp": 1726247200000
  }
}
```

## Example: Complete Request with Data Operations

Here's a complete example showing a request with data operations enabled:

```bash
curl -N \
  -X POST "http://localhost:3003/api/chat" \
  -H "Authorization: Bearer $INKEEP_API_KEY" \
  -H "Content-Type: application/json" \
  -H "x-emit-operations: true" \
  -d '{
    "messages": [
      { "role": "user", "content": "Create a sales report for Q4" }
    ],
    "conversationId": "chat-1234"
  }'
```

**Response Stream:**

```text
data: {"type":"agent_initializing","details":{"sessionId":"session_abc123","agentId":"graph_xyz789"}}

data: {"type":"data-operation","data":{"type":"agent_reasoning","label":"Agent coordinator-agent reasoning through request","details":{"timestamp":1726247200000,"agentId":"coordinator-agent","data":{"parts":[{"type":"text","content":"I need to create a sales report for Q4. This will require gathering data and generating a chart."}]}}}}

data: {"type":"data-operation","data":{"type":"tool_call","label":"Tool call: get_sales_data","details":{"timestamp":1726247200000,"agentId":"coordinator-agent","data":{"toolName":"get_sales_data","args":{"quarter":"Q4","year":"2023"},"toolCallId":"call_abc123","toolId":"tool_xyz789"}}}}

data: {"type":"data-operation","data":{"type":"tool_result","label":"Tool result: get_sales_data","details":{"timestamp":1726247200000,"agentId":"coordinator-agent","data":{"toolName":"get_sales_data","result":{"sales":[...]},"toolCallId":"call_abc123","toolId":"tool_xyz789","duration":850}}}}

data: {"type":"data-artifact","data":{ ... }}

data: {"type":"data-operation","data":{"type":"artifact_saved","label":"Artifact saved: chart","details":{"timestamp":1726247200000,"agentId":"coordinator-agent","data":{"artifactId":"art_123456","artifactType":"chart","summaryData":{"title":"Q4 Sales Report"}}}}}

data: {"type":"text-start","id":"1726247200-abc123"}

data: {"type":"text-delta","id":"1726247200-abc123","delta":"I've created a comprehensive Q4 sales report..."}

data: {"type":"text-end","id":"1726247200-abc123"}

data: {"type":"completion","details":{"agent":"coordinator-agent","iteration":1}}
```

This provides complete visibility into the agent's execution process, from initialization through reasoning, tool execution, artifact creation, and final response generation.


# Environment Management
URL: /typescript-sdk/environments

Manage different deployment environments with environment-specific configurations and credential management

***

title: Environment Management
description: Manage different deployment environments with environment-specific configurations and credential management
icon: "LuLayers"
----------------

## Overview

Environment management in Inkeep Agent projects enables you to maintain different configurations for development, staging, and production deployments. The `--env` flag system provides secure credential management and environment-specific settings without duplicating your core project configuration.

## Environment Structure

### Directory Layout

```
workspace-root/
├── package.json              # Workspace package.json
├── inkeep.config.ts          # Base configuration (at workspace root)
└── my-project/               # Individual project directory
    ├── index.ts              # Project entry point
    ├── environments/         # Environment-specific configs
    │   ├── index.ts          # Environment exports
    │   ├── development.env.ts # Development settings
    │   ├── staging.env.ts    # Staging settings
    │   └── production.env.ts # Production settings
    └── ...
```

### Environment File Format

```typescript
// environments/development.env.ts
import { registerEnvironmentSettings } from '@inkeep/agents-sdk';
import { CredentialStoreType } from '@inkeep/agents-core';

export const development = registerEnvironmentSettings({
  credentials: {
    "openai-dev": {
      id: "openai-dev",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "OPENAI_API_KEY_DEV",
      },
    },
    "anthropic-dev": {
      id: "anthropic-dev",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "ANTHROPIC_API_KEY_DEV",
      },
    },
  },
});
```

## How Environments Work

### Environment Selection Flow

```mermaid
graph TD
    A[inkeep push] --> B{--env flag provided?}
    B -->|Yes| C[Load environments/<env>.env.ts]
    B -->|No| D[Use base configuration only]
    C --> E{Environment file exists?}
    E -->|Yes| F[Merge with base config]
    E -->|No| G[Error: Environment not found]
    F --> H[Apply environment credentials]
    D --> I[Deploy with base config]
    H --> I
    G --> J[Exit with error]
```

### Usage Examples

```bash
# Push with development environment
inkeep push --env development

# Push with production credentials
inkeep push --env production

# Push without environment (base config only)
inkeep push
```

## Environment Configuration

### Credential Management

Environments primarily manage credentials for different deployment stages:

```typescript
// environments/production.env.ts
import { registerEnvironmentSettings } from '@inkeep/agents-sdk';
import { CredentialStoreType } from '@inkeep/agents-core';

export const production = registerEnvironmentSettings({
  credentials: {
    // Production OpenAI credentials
    "openai-prod": {
      id: "openai-prod",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "OPENAI_API_KEY_PROD",
      },
    },
    // Production database credentials
    "database-prod": {
      id: "database-prod",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "DATABASE_URL_PROD",
      },
    },
    // External API credentials
    "external-api-prod": {
      id: "external-api-prod",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "EXTERNAL_API_SECRET_PROD",
      },
    },
  },
});
```

### MCP Server Management

Environments can also manage MCP servers for different deployment stages. If your MCP server requires credentials, you can define them inline on the MCP server definition:

```typescript
// environments/development.env.ts
export const development = registerEnvironmentSettings({
  mcpServers: {
    "my-mcp-server": {
      id: "my-mcp-server",
      type: CredentialStoreType.memory,
      serverUrl: "http://localhost:3000/mcp",
      credential: {
        id: "my-mcp-server-credential",
        type: CredentialStoreType.memory,
        credentialStoreId: "memory-default",
        retrievalParams: {
          key: "MY_MCP_SERVER_KEY_DEV",
        },
     },
    },
  },
});
```

```typescript
// environments/production.env.ts
export const production = registerEnvironmentSettings({
  mcpServers: {
    "my-mcp-server": {
      id: "my-mcp-server",
      type: CredentialStoreType.memory,
      serverUrl: "https://my-mcp-server-prod.com/mcp",
      credential: {
        id: "my-mcp-server-credential",
        type: CredentialStoreType.memory,
        credentialStoreId: "memory-default",
        retrievalParams: {
          key: "MY_MCP_SERVER_KEY_PROD",
        },
     },
    },
  },
});
```

### Environment Index File

Export all environments from the index file:

```typescript
// environments/index.ts
import { createEnvironmentSettings } from '@inkeep/agents-sdk';
import { development } from './development.env';
import { staging } from './staging.env';
import { production } from './production.env';

export const envSettings = createEnvironmentSettings({
  development,
  staging,
  production,
});
```

## Credential Store Types

### Memory Store

Loads credentials from environment variables at runtime:

```typescript
{
  type: CredentialStoreType.memory,
  credentialStoreId: "memory-default",
  retrievalParams: {
    key: "API_KEY_ENV_VAR",
  },
}
```

### File Store

Loads credentials from secure files:

```typescript
{
  type: CredentialStoreType.file,
  credentialStoreId: "file-store",
  retrievalParams: {
    filePath: "/secure/path/to/credentials.json",
    key: "apiKey",
  },
}
```

### External Store

Integrates with external credential management systems:

```typescript
{
  type: CredentialStoreType.external,
  credentialStoreId: "vault-store",
  retrievalParams: {
    endpoint: "https://vault.company.com",
    path: "secret/api-keys",
  },
}
```

## Environment Workflows

### Development Environment

```typescript
// environments/development.env.ts
export const development = registerEnvironmentSettings({
  credentials: {
    "openai-dev": {
      id: "openai-dev",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "OPENAI_API_KEY_DEV", // Uses dev API key
      },
    },
  },
  mcpServers: {
    "my-mcp-server": {
      id: "my-mcp-server",
      type: CredentialStoreType.memory,
      serverUrl: "http://localhost:3000/mcp",
      credential: {
        id: "my-mcp-server-credential",
        type: CredentialStoreType.memory,
        credentialStoreId: "memory-default",
        retrievalParams: {
          key: "MY_MCP_SERVER_KEY_DEV",
        },
     },
    },
  },
});
```

```bash
# Set development environment variables
export OPENAI_API_KEY_DEV=sk-dev-key...
export ANTHROPIC_API_KEY_DEV=sk-ant-dev...

# Deploy to development
inkeep push --env development
```

### Staging Environment

```typescript
// environments/staging.env.ts
export const staging = registerEnvironmentSettings({
  credentials: {
    "openai-staging": {
      id: "openai-staging",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "OPENAI_API_KEY_STAGING",
      },
    },
  },
  mcpServers: {
    "my-mcp-server": {
      id: "my-mcp-server",
      type: CredentialStoreType.memory,
      serverUrl: "https://my-mcp-server-staging.com/mcp",
      credential: {
        id: "my-mcp-server-credential",
        type: CredentialStoreType.memory,
        credentialStoreId: "memory-default",
        retrievalParams: {
          key: "MY_MCP_SERVER_KEY_STAGING",
        },
     },
    },
  },
});
```

### Production Environment

```typescript
// environments/production.env.ts
export const production = registerEnvironmentSettings({
  credentials: {
    "openai-prod": {
      id: "openai-prod",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "OPENAI_API_KEY_PROD",
      },
    },
  },
  mcpServers: {
    "my-mcp-server": {
      id: "my-mcp-server",
      type: CredentialStoreType.memory,
      serverUrl: "https://my-mcp-server-prod.com/mcp",
      credential: {
        id: "my-mcp-server-credential",
        type: CredentialStoreType.memory,
        credentialStoreId: "memory-default",
        retrievalParams: {
          key: "MY_MCP_SERVER_KEY_PROD",
        },
     },
    },
  },
});
```

## Advanced Environment Features

### Environment-Specific Overrides

While environments primarily manage credentials and MCP servers, they can include other settings:

```typescript
// environments/development.env.ts
export const development = registerEnvironmentSettings({
  // Credential configuration
  credentials: {
    // ... credential definitions
  },

  // Development-specific settings
  settings: {
    logLevel: 'debug',
    apiTimeout: 60000, // Longer timeout for debugging
  },
});
```

### Conditional Environments

Create environments that adapt to runtime conditions:

```typescript
// environments/dynamic.env.ts
const isDevelopment = process.env.NODE_ENV === 'development';

export const dynamic = registerEnvironmentSettings({
  credentials: {
    "api-key": {
      id: "api-key",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: isDevelopment ? "API_KEY_DEV" : "API_KEY_PROD",
      },
    },
  },
});
```

## Environment Variables Integration

### CLI Environment Variables

The CLI respects these environment variables when using the `--env` flag:

```bash
# Set environment name via environment variable
export INKEEP_ENV=production
inkeep push  # Uses production environment automatically

# Override via CLI (takes precedence)
inkeep push --env development  # Uses development instead
```

### Credential Environment Variables

Environment files reference environment variables for actual credential values:

```bash
# Development
export OPENAI_API_KEY_DEV=sk-dev-...
export DATABASE_URL_DEV=postgresql://dev...

# Production
export OPENAI_API_KEY_PROD=sk-prod-...
export DATABASE_URL_PROD=postgresql://prod...
```

## Best Practices

### 1. Credential Isolation

Keep credentials completely separate between environments:

```typescript
// ✓ Good: Environment-specific credential IDs
const development = registerEnvironmentSettings({
  credentials: {
    "openai-dev": { /* dev credentials */ },
    "database-dev": { /* dev database */ },
  },
});

const production = registerEnvironmentSettings({
  credentials: {
    "openai-prod": { /* prod credentials */ },
    "database-prod": { /* prod database */ },
  },
});
```

### 2. Secure Secret Management

Never commit secrets to environment files:

```typescript
// ✗ Bad: Hardcoded secrets
export const production = registerEnvironmentSettings({
  credentials: {
    "api-key": {
      value: "sk-secret-key", // Don't do this!
    },
  },
});

// ✓ Good: Reference environment variables
export const production = registerEnvironmentSettings({
  credentials: {
    "api-key": {
      type: CredentialStoreType.memory,
      retrievalParams: {
        key: "API_KEY_PROD", // Loaded from environment
      },
    },
  },
});
```

### 3. Environment Naming

Use consistent, descriptive environment names:

```bash
# ✓ Good: Clear, standard names
environments/
├── development.env.ts
├── staging.env.ts
└── production.env.ts

# ✗ Avoid: Ambiguous names
environments/
├── dev.env.ts      # Too abbreviated
├── test.env.ts     # Confusing (test vs staging?)
└── live.env.ts     # Unclear (live vs production?)
```

### 4. Environment Documentation

Document what each environment is for:

```typescript
/**
 * Development environment configuration
 * - Uses development API keys
 * - Connects to local development services
 * - Enables debug logging
 */
export const development = registerEnvironmentSettings({
  credentials: {
    // Development-specific credentials...
  },
});
```

## Troubleshooting

### Environment Not Found

```bash
Error: Environment file 'environments/staging.env.ts' not found
```

**Solutions:**

* Check file exists in `/environments/` directory
* Verify file name matches `--env` parameter exactly
* Ensure file exports environment with correct name

### Credential Loading Issues

```bash
Error: Environment variable 'OPENAI_API_KEY_PROD' not set
```

**Solutions:**

* Set required environment variables before push
* Check environment variable names in credential config
* Verify credential store configuration

### Environment Override Issues

```bash
Warning: No credentials found for environment 'production'
```

**Solutions:**

* Check environment file exports credentials object
* Verify credential IDs match agent requirements
* Test environment file syntax with TypeScript compiler

## CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy Agents

on:
  push:
    branches: [main]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
      - name: Install CLI
        run: npm install -g @inkeep/agents-cli
      - name: Deploy to Staging
        env:
          OPENAI_API_KEY_STAGING: ${{ secrets.OPENAI_API_KEY_STAGING }}
          ANTHROPIC_API_KEY_STAGING: ${{ secrets.ANTHROPIC_API_KEY_STAGING }}
        run: inkeep push --env staging

  deploy-production:
    runs-on: ubuntu-latest
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Production
        env:
          OPENAI_API_KEY_PROD: ${{ secrets.OPENAI_API_KEY_PROD }}
          ANTHROPIC_API_KEY_PROD: ${{ secrets.ANTHROPIC_API_KEY_PROD }}
        run: inkeep push --env production
```

### Docker Integration

```dockerfile
# Dockerfile
FROM node:18

# Install CLI
RUN npm install -g @inkeep/agents-cli

# Copy project
COPY . /app
WORKDIR /app

# Set environment and deploy
ARG ENVIRONMENT=production
ENV INKEEP_ENV=${ENVIRONMENT}

CMD ["inkeep", "push"]
```

Environment management provides the foundation for secure, scalable deployment of your Inkeep Agent projects across different stages of your development lifecycle.


# Add External Agents to your Agent
URL: /typescript-sdk/external-agents

Learn how to configure and use external agents using the A2A protocol

***

title: Add External Agents to your Agent
sidebarTitle: External Agents
description: Learn how to configure and use external agents using the A2A protocol
icon: "LuGlobe"
---------------

External agents let you integrate agents built outside of Inkeep (using other frameworks or platforms) into your Agent. They communicate over the A2A (Agent‑to‑Agent) protocol so your Inkeep sub-agents can delegate tasks to them as if they were native. Note that Inkeep Agents are available via an [A2A endpoint](/talk-to-your-agents/a2a) themselves and used from other platforms.

Learn more about A2A:

* A2A overview on the Google Developers Blog: [A2A — a new era of agent interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
* A2A protocol site: [a2a.how](https://a2a.how/)

Examples platforms that expose Agents in A2A-format:

| Platform                                                                                                                      | Type         | Description                                                         |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------- |
| [LangGraph](https://docs.langchain.com/langgraph-platform/server-a2a)                                                         | Native       | Built-in A2A endpoint & Agent Card for graph agents.                |
| [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/a2a/)                                                  | Native       | Official guide to build agents that expose/consume A2A.             |
| [Microsoft Semantic Kernel](https://devblogs.microsoft.com/foundry/semantic-kernel-a2a-integration/)                          | Native       | “SK now speaks A2A” with sample to expose compliant agents.         |
| [Pydantic AI](https://ai.pydantic.dev/a2a/)                                                                                   | Native       | Convenience method to publish a Pydantic AI agent as an A2A server. |
| [AWS Strands Agents SDK](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/agent-to-agent/) | Native       | A2A support in Strands for cross‑platform agent communication.      |
| [CrewAI](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge)                                               | With Adapter | Use the A2A Python SDK to serve a CrewAI agent over A2A.            |
| [LlamaIndex](https://a2aprotocol.ai/blog/a2a-samples-llama-index-file-chat-openrouter)                                        | With Adapter | Example Workflows app exposed via A2A (agent + card).               |

<Note>
  Any agent that exposes an A2A‑compatible HTTP endpoint can be integrated by providing its `baseUrl` plus headers/auth (static or dynamic).
</Note>

## Creating an External Agent

Every external agent needs a unique identifier, name, description, base URL for A2A communication, and optional authentication configuration:

```typescript
import { externalAgent } from "@inkeep/agents-sdk";

const technicalSupportAgent = externalAgent({
  id: "technical-support-agent",
  name: "Technical Support Team",
  description: "External technical support specialists for complex issues",
  baseUrl: "https://api.example.com/agents/technical-support", // A2A endpoint
});
```

## External Agent Relationships

Agents can be configured to delegate tasks to external agents.

```typescript
import { subAgent, agent } from "@inkeep/agents-sdk";
import { myExternalAgent } from "./external-agents/exernal-agent-example";

// Define the customer support sub-agent with delegation capabilities
const supportSubAgent = subAgent({
  id: "support-agent",
  name: "Customer Support Sub-Agent",
  description: "Handles customer inquiries and escalates technical issues",
  prompt: `You are a customer support sub-agent that handles general customer inquiries.`,
  canDelegateTo: () => [myExternalAgent],
});

// Create the customer support agent with external agent capabilities
export const supportAgent = agent({
  id: "customer-support-agent",
  name: "Customer Support System",
  description: "Handles customer inquiries and escalates to technical teams when needed",
  defaultSubAgent: supportSubAgent,
  subAgents: () => [supportSubAgent],
});
```

## External Agent Options

Configure authentication by providing a [credential reference](/typescript-sdk/tools/credentials).

```typescript
const myExternalAgent = externalAgent({
  // Required
  id: "external-support-agent",
  name: "External Support Agent", // Human-readable agent name
  description: "External AI agent for specialized support", // Agent's purpose
  baseUrl: "https://api.example.com/agents/support", // A2A endpoint URL
  // Optional - Credential Reference
  credentialReference: myCredentialReference,
});
```

When delegating to an external agent, you can specify headers to include with every request to the external agent.
These headers can be dynamic variables that are [resolved at runtime](/typescript-sdk/headers).

```typescript
const supportSubAgent = subAgent({
  id: "support-agent",
  name: "Customer Support Sub-Agent",
  description: "Handles customer inquiries and escalates technical issues",
  prompt: `You are a customer support sub-agent that handles general customer inquiries.`,
  canDelegateTo: () => [myExternalAgent.with({ headers: { Authorization: "Bearer {{headers.Authorization}}" } })],
});
```

| Parameter             | Type                | Required | Description                                                                                                           |
| --------------------- | ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| `id`                  | string              | Yes      | Stable agent identifier used for consistency and persistence                                                          |
| `name`                | string              | Yes      | Human-readable name for the external agent                                                                            |
| `description`         | string              | Yes      | Brief description of the agent's purpose and capabilities                                                             |
| `baseUrl`             | string              | Yes      | The A2A endpoint URL where the external agent can be reached                                                          |
| `credentialReference` | CredentialReference | No       | Reference to dynamic credentials for authentication. See [Credentials](/typescript-sdk/tools/credentials) for details |


# Headers
URL: /typescript-sdk/headers

Pass dynamic context to your Agents via HTTP headers for personalized interactions

***

title: Headers
sidebarTitle: Headers
description: Pass dynamic context to your Agents via HTTP headers for personalized interactions
icon: LuBoxes
keywords: headers, context fetchers, prompt variables, personalization
----------------------------------------------------------------------

## Overview

Headers allow you to pass request-specific values (like user IDs, authentication tokens, or organization metadata) to your Agent at runtime via HTTP headers. These values are validated, cached per conversation, and made available throughout your Agent system for:

* **Context Fetchers**: Dynamic data retrieval based on request values
* **External Tools**: Authentication and personalization for API calls
* **Agent Prompts**: Personalized responses using context variables

## Passing context via headers

Include context values as HTTP headers when calling your agent API. These headers are validated against your configured schema and cached for the conversation.

```bash
curl -N \
  -X POST "http://localhost:3003/api/chat" \
  -H "Authorization: Bearer $INKEEP_API_KEY" \
  -H "user_id: u_123" \
  -H "auth_token: t_abc" \
  -H "org_name: Acme Corp" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [ { "role": "user", "content": "What can you help me with?" } ],
    "conversationId": "conv-123"
  }'
```

<Note>
  Header keys are normalized to lowercase. Define them as lowercase in your schema and reference them as lowercase in templates.
</Note>

## Configuring headers

Define a schema for your headers and configure how it's used in your agent.
You must include the headers schema in your context config.

```typescript
import { z } from "zod";
import { agent, subAgent } from "@inkeep/agents-sdk";
import { contextConfig, fetchDefinition, headers } from '@inkeep/agents-core';


// Define schema for expected headers (use lowercase keys)
const personalAgentHeaders = headers({
  schema: z.object({
    user_id: z.string(),
    auth_token: z.string(),
    org_name: z.string().optional()
  });
});

// Create a context fetcher that uses header values with type-safe templating
const userFetcher = fetchDefinition({
  id: "user-info",
  name: "User Information",
  trigger: "initialization",
  fetchConfig: {
    url: `https://api.example.com/users/${personalAgentHeaders.toTemplate('user_id')}`,
    method: "GET",
    headers: {
      Authorization: `Bearer ${personalAgentHeaders.toTemplate('auth_token')}`,
    },
    transform: "user", // Extract user from response, for example if the response is { "user": { "name": "John Doe", "email": "john.doe@example.com" } }, the transform will return the user object
  },
  responseSchema: z.object({
    user: z.object({
      name: z.string(),
      email: z.string(),
    }),
  }),
  defaultValue: "Guest User"
});

// Configure context for your agent
const personalAgentContext = contextConfig({
  headers: personalAgentHeaders,
  contextVariables: {
    user: userFetcher,
  },
});

// Create a Sub Agent that uses context variables
const personalAssistant = subAgent({
  id: "personal-assistant",
  name: "Personal Assistant",
  description: "Personalized AI assistant",
  prompt: `You are a helpful assistant for ${personalAgentContext.toTemplate('user.name')} from ${personalAgentHeaders.toTemplate('org_name')}.

  User ID: ${personalAgentHeaders.toTemplate('user_id')}

  Provide personalized assistance based on their context.`,
});

// Attach context to your Agent
const myAgent = agent({
  id: "personal-agent",
  name: "Personal Assistant Agent",
  defaultSubAgent: personalAssistant,
  subAgents: () => [personalAssistant],
  contextConfig: personalAgentContext,
});
```

## How it works

<Steps>
  <Step>
    **Validation**: Headers are validated against your configured schema when a request arrives
  </Step>

  <Step>
    **Caching**: Validated context is cached per conversation for reuse across multiple interactions
  </Step>

  <Step>
    **Reuse**: Subsequent requests with the same `conversationId` automatically use cached context values
  </Step>

  <Step>
    **Updates**: Provide new header values to update the context for an ongoing conversation
  </Step>
</Steps>

<Tip>
  Context values persist across conversation turns. To update them, send new header values with the same conversation ID.
</Tip>

## Using headers in your agents

Header values can be used in your agent prompts and fetch definitions using JSONPath template syntax `{{headers.field_name}}`.
You can use the headers schema's `toTemplate()` method for type-safe templating with autocomplete and validation.

### In Context Fetchers

Use header values to fetch dynamic data from external APIs:

```typescript
// Define schema for expected headers (use lowercase keys)
const personalAgentHeaders = headers({
  schema: z.object({
    user_id: z.string(),
    auth_token: z.string(),
    org_name: z.string().optional()
  });
});


const userDataFetcher = fetchDefinition({
  id: "user-data",
  name: "User Data",
  fetchConfig: {
    url: `https://api.example.com/users/${personalAgentHeaders.toTemplate('user_id')}/profile`,
    headers: {
      Authorization: `Bearer ${personalAgentHeaders.toTemplate('auth_token')}`,
      "X-Organization": personalAgentHeaders.toTemplate('org_name')
    },
    body: {
      includePreferences: true,
      userId: personalAgentHeaders.toTemplate('user_id')
    }
  },
  responseSchema: z.object({
    name: z.string(),
    preferences: z.record(z.unknown())
  })
});

// Configure context for your Agent
// You must include the headers schema and fetchers in your context config.
const personalAgentContext = contextConfig({
  headers: personalAgentHeaders,
  contextVariables: {
    user: userFetcher,
  },
});
```

### In Agent Prompts

Reference context directly in agent prompts for personalization using the context config's template method:

```typescript
// Create context config with both headers and fetchers
const userContext = contextConfig({
  headers: requestHeaders,
  contextVariables: {
    userName: userDataFetcher,
  },
});

const assistantAgent = subAgent({
  prompt: `You are an assistant for ${userContext.toTemplate('userName')} from ${requestHeaders.toTemplate('org_name')}.

  User context:
  - ID: ${requestHeaders.toTemplate('user_id')}
  - Organization: ${requestHeaders.toTemplate('org_name')}

  Provide help tailored to their organization's needs.`
});
```

### In External Tools

Configure external agents or MCP servers with dynamic headers using the headers schema:

```typescript
// Define schema for expected headers (use lowercase keys)
const personalAgentHeaders = headers({
  schema: z.object({
    user_id: z.string(),
    auth_token: z.string(),
    org_name: z.string().optional()
  });
});

// Configure external agent
const externalAgent = externalAgent({
  id: "external-service",
  baseUrl: "https://external.api.com",
  headers: {
    Authorization: `Bearer ${personalAgentHeaders.toTemplate('auth_token')}`,
    "X-User-Context": personalAgentHeaders.toTemplate('user_id'),
    "X-Org": personalAgentHeaders.toTemplate('org_name')
  }
});

// Configure context for your Agent with your headers schema.
const personalAgentContext = contextConfig({
  headers: personalAgentHeaders,
});
```

## Best practices

* **Use lowercase keys**: Always define schema properties in lowercase and reference them as lowercase in templates
* **Validate early**: Test your schema configuration with sample headers before deploying
* **Cache wisely**: Remember that context persists per conversation - design accordingly
* **Secure sensitive data**: For long-lived secrets, use the [Credentials](/typescript-sdk/tools/credentials) system instead of headers
* **Keep it minimal**: Only include context values that are actually needed by your agents

## Common use cases

### Multi-tenant applications

Pass tenant-specific configuration to customize agent behavior per customer:

```typescript
// Headers
"tenant_id: acme-corp"
"tenant_plan: enterprise"
"tenant_features: advanced-analytics,custom-branding"
```

### User authentication

Provide user identity and session information for personalized interactions:

```typescript
// Headers
"user_id: user_123"
"user_role: admin"
"session_token: sk_live_..."
```

### API gateway integration

Forward headers from your API gateway for consistent authentication:

```typescript
// Headers
"x-api-key: your-api-key"
"x-request-id: req_abc123"
"x-client-version: 2.0.0"
```

## Troubleshooting

### Invalid headers errors

If you receive a 400 error about invalid headers:

1. Verify your schema matches the headers you're sending
2. Ensure all header keys are lowercase
3. Check that required fields are present
4. Validate the data types match your schema

### Context not persisting

If context values aren't available in subsequent requests:

1. Ensure you're using the same `conversationId` across requests
2. Verify headers are being sent correctly
3. Check that your context config is properly attached to the Agent

## Related documentation

* [Context Fetchers](/typescript-sdk/context-fetchers) - Learn about fetching and caching external data
* [External Agents](/typescript-sdk/external-agents) - Configure external agent integrations
* [Credentials](/typescript-sdk/tools/credentials) - Manage secure credentials for your Agents


# Using Langfuse for LLM Observability
URL: /typescript-sdk/langfuse-usage

Complete guide to using Langfuse for LLM observability, tracing, and analytics in the Inkeep Agent Framework

***

title: Using Langfuse for LLM Observability
sidebarTitle: Langfuse Usage
description: Complete guide to using Langfuse for LLM observability, tracing, and analytics in the Inkeep Agent Framework
keywords: Langfuse, LLM observability, tracing, OpenTelemetry, AI monitoring, token usage, model analytics
icon: "brand/Langfuse"
----------------------

Langfuse is an open-source LLM engineering platform that provides specialized observability for AI applications, including token usage tracking, model performance analytics, and detailed LLM interaction tracing.

## Quick Start

### 1. Setup Langfuse Account

First, create a Langfuse account and get your API keys:

1. **Sign up** at [Langfuse Cloud](https://cloud.langfuse.com)
2. **Create a new project** in your Langfuse dashboard
3. **Get your API keys** from the project settings:
   * Public Key: `pk-lf-xxxxxxxxxx`
   * Secret Key: `sk-lf-xxxxxxxxxx`

### 2. Configure Langfuse

To integrate Langfuse with your Inkeep Agent Framework instrumentation, you need to modify your instrumentation file to include the Langfuse span processor.

Replace the default setup with a custom NodeSDK configuration:

Set your environment variables:

```bash
LANGFUSE_PUBLIC_KEY=pk-lf-xxxxxxxxxx
LANGFUSE_SECRET_KEY=sk-lf-xxxxxxxxxx
LANGFUSE_BASE_URL=https://us.cloud.langfuse.com
```

Update your instrumentation file:

```typescript
import {
  defaultSpanProcessors,
  defaultContextManager,
  defaultResource,
  defaultTextMapPropagator,
  defaultInstrumentations,
} from "@inkeep/agents-run-api/instrumentation";
import { NodeSDK } from "@opentelemetry/sdk-node";
import { LangfuseSpanProcessor } from "@langfuse/otel";

export const defaultSDK = new NodeSDK({
  resource: defaultResource,
  contextManager: defaultContextManager,
  textMapPropagator: defaultTextMapPropagator,
  spanProcessors: [...defaultSpanProcessors, new LangfuseSpanProcessor()],
  instrumentations: defaultInstrumentations,
});

defaultSDK.start();
```

<Note>
  Make sure to install the required dependencies in your run API directory:
  `bash cd apps/run-api pnpm add @opentelemetry/sdk-node @langfuse/otel `
</Note>

#### What This Configuration Does

* **Preserves all default instrumentation**: Uses the same resource, context manager, propagator, and instrumentations as the default setup
* **Adds Langfuse span processor**: Extends the default span processors with Langfuse's processor for specialized LLM observability
* **Maintains compatibility**: Your existing traces will continue to work while adding Langfuse-specific features

## Dataset setup and execution

Use the [Inkeep Agent Cookbook](https://github.com/inkeep/agents/tree/main/agents-cookbook) which provides ready-to-use scripts for creating and running Langfuse dataset evaluations programmatically.

#### 1. Clone the Agents Repository

```bash
git clone https://github.com/inkeep/agents.git
cd agents/agents-cookbook/evals/langfuse-dataset-example
```

**Set up environment variables in a `.env` file:**

```bash
# Langfuse configuration (required for both scripts)
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_BASE_URL=https://cloud.langfuse.com

# Chat API configuration (for dataset runner)
INKEEP_AGENTS_RUN_API_KEY=your_api_key
INKEEP_AGENTS_RUN_API_URL=your_chat_api_base_url

# Execution context (for dataset runner)
INKEEP_TENANT_ID=your_tenant_id
INKEEP_PROJECT_ID=your_project_id
INKEEP_AGENT_ID=your_agent_id
```

#### 2. Initialize Dataset with Sample Data

Run the basic Langfuse example to initialize a dataset with sample user messages:

```bash
pnpm run langfuse-init-example
```

This script will:

* Connect to your Langfuse project
* Create a new dataset called "inkeep-weather-example-dataset" with sample dataset items

#### 3. Run Dataset Items to Generate Traces

Run dataset items to generate traces that can be evaluated:

```bash
pnpm run langfuse-run-dataset
```

This script will:

* Read items from your Langfuse dataset
* Execute each item against your weather agent
* Generate the data needed for evaluation

## Running LLM Evaluations in Langfuse Dashboard

Langfuse provides a powerful web interface for running LLM evaluations without writing code. You can create datasets, set up evaluators, and run evaluations directly in the dashboard.

### Accessing the Evaluation Features

1. **Log into your Langfuse dashboard**: [https://cloud.langfuse.com](https://cloud.langfuse.com)
2. **Navigate to your project** where your agent traces are being collected
3. **Click "Evaluations"** in the left sidebar
4. **Click "Set up evaluator"** to begin creating evaluations

### Setting Up LLM-as-a-Judge Evaluators

#### Set Up Default Evaluation Model

Before creating evaluators, you need to configure a default LLM connection for evaluations:

<Image src="/images/langfuse-llm-connection.png" alt="Langfuse LLM Connection setup showing OpenAI provider configuration with API key field and advanced settings" style={{ border: "1px solid #e1e5e9" }} />

**Setting up the LLM Connection:**

1. **Navigate to "Evaluator Library"** in your Langfuse dashboard
2. **Click "Set up"** next to "Default Evaluation Model"
3. **Configure the LLM connection**:
   * **LLM Adapter**: Select your preferred provider
   * **Provider Name**: Give it a descriptive name (e.g., "openai")
   * **API Key**: Enter your OpenAI API key (stored encrypted)
   * **Advanced Settings**: Configure base URL, model parameters if needed
4. **Click "Create connection"** to save

#### Navigate to Evaluator Setup

1. **Go to "Evaluations"** → **"Running Evaluators"**
2. **Click "Set up evaluator"** button
3. **You'll see two main steps**: "1. Select Evaluator" and "2. Run Evaluator"

#### Choose Your Evaluator Type

You have two main options:

## Option A: Langfuse Managed Evaluators

Langfuse provides a comprehensive catalog of **pre-built evaluators**

**To use a managed evaluator:**

1. **Browse the evaluator list** and find one that matches your needs
2. **Click on the evaluator** to see its description and criteria
3. **Click "Use Selected Evaluator"** button

#### Customizing Managed Evaluators for Dataset Runs

Once you've selected a managed evaluator, you can **edit it to target your dataset runs**. This is particularly useful for evaluating agent performance against known test cases.

### Example: Customizing a Helpfulness Evaluator

1. **Select the "Helpfulness" evaluator** from the managed list
2. Under **Target** select dataset runs
3. **Configure variable mapping**
   * **{`{{input}}`}** → **Object**: Trace, **Object Variable**: Input
   * **{`{{generation}}`}** → **Object**: Trace, **Object Variable**: Output

<Image
  src="/images/langfuse-helpfulness-setup.png"
  style={{
  border: "1px solid #e1e5e9",
  maxWidth: "1600px",
  height: "auto",
  minHeight: "300px",
}}
/>

## Option B: Create Custom Evaluator

1. **Click "+ Create Custom Evaluator"** button
2. **Fill in evaluator details**:

   * **Name**: Choose a descriptive name (e.g., "weather\_tool\_used")
   * **Description**: Explain what this evaluator measures
   * **Model**: Select evaluation model
   * **Prompt**: Configure a custom prompt

### Example: Customizing a Weather Tool Evaluator

1. **Prompt**

```
You are an expert evaluator for an AI agent system.
Your task is to rate the correctness of tool usage on a scale from 0.0 to 1.0.

Instructions:

If the user’s question is not weather-related and the tool used is not get_weather_forecast, return 1.0.

If the user’s question is not weather-related and the tool is get_weather_forecast, return 0.0.

If the user’s question is weather-related, return 1.0 only if the tool used is get_weather_forecast; otherwise return 0.0.

Input:
User Question: {`{{input}}`}
Tool Used: {`{{tool_used}}`}
```

<Image
  src="/images/custom-eval.png"
  width="80%"
  style={{
  border: "1px solid #e1e5e9",
  maxWidth: "800px",
  height: "auto",
}}
/>

2. **Configure variable mapping**:
   * **{`{{input}}`}** → **Object**: Trace, **Object Variable**: Input
   * **{`{{tool_used}}`}** → **Object**: Span, **Object Name**: weather-forecaster.ai.toolCall, **Object Variable**: Metadata, **JsonPath**: $.attributes\["ai.toolCall.name"]

<Image
  src="/images/custom-variable-mapping.png"
  alt="Langfuse helpfulness evaluator setup screen showing evaluator configuration with variable mapping and trace targeting options"
  style={{
  border: "1px solid #e1e5e9",
  maxWidth: "1200px",
  height: "auto",
  minHeight: "300px",
}}
/>

## Enable and Monitor

1. **Click "Enable Evaluator"** to start automatic evaluation
2. **Monitor evaluation progress** in the dashboard
3. **View evaluation results** as they complete


# Conversation Memory
URL: /typescript-sdk/memory

Understand how conversation history is managed and included in the context window for both main and delegated agents

***

title: Conversation Memory
sidebarTitle: Memory
description: Understand how conversation history is managed and included in the context window for both main and delegated agents
icon: "LuBrain"
keywords: memory, context window, conversation history, message limits, token limits, delegation, tool results
--------------------------------------------------------------------------------------------------------------

## Overview

Conversation memory determines how much of the conversation history is included in the context window when your Agent processes a new message. The Inkeep Agent Framework automatically manages conversation history to balance context retention with token efficiency, with specialized handling for delegated agents and tool results.

## What's Included in Memory

The conversation history now includes:

* **Chat messages**: User messages and agent responses
* **Tool results**: Results from tool executions, providing context about what actions were performed
* **Agent communications**: Messages exchanged between agents during transfers and delegations

## Default Limits

By default, the system includes conversation history using these limits:

* **50 messages**: Up to the 50 most recent messages from the conversation
* **8,000 tokens**: Maximum of 8,000 tokens from previous conversation messages (increased from 4,000 to accommodate tool results)

<Note>
  The 50-message and 8,000-token limits are the default values. The token limit can be adjusted via the `AGENTS_CONVERSATION_HISTORY_MAX_OUTPUT_TOKENS_DEFAULT` environment variable if needed.
</Note>

## How It Works

<Steps>
  <Step>
    **Message Retrieval**: The system retrieves up to 50 most recent messages from the conversation history
  </Step>

  <Step>
    **Delegation Filtering**: Messages are filtered based on delegation context - delegated agents see their own tool results plus top-level conversation context
  </Step>

  <Step>
    **Token Calculation**: Remaining messages are processed, calculating token count for each message
  </Step>

  <Step>
    **Exclusion**: If the total token count exceeds 4,000 tokens, older messages are excluded from the context window
  </Step>
</Steps>

## Memory for Delegated Agents

When agents delegate tasks to other agents, memory is intelligently filtered:

### Main Agents

* See complete conversation history including all tool results
* Maintain full context of delegated actions and their results

### Delegated Agents

* See conversation history filtered to their delegation scope
* Receive tool results from:
  * Their own tool executions
  * Top-level (non-delegated) tool executions
* Cannot see tool results from unrelated delegations

This ensures delegated agents have sufficient context while preventing memory pollution from unrelated parallel delegations.

## Tool Results in Memory

Tool execution results are automatically included in conversation history, helping agents:

* Understand what actions have already been performed
* Avoid duplicate tool calls
* Build on previous results when transferring between agents

The tool results include both the input parameters and output results, formatted as:

```
## Tool: search_knowledge_base

**Input:**
{
  "query": "API authentication methods"
}

**Output:**
{
  "results": [...]
}
```


# Model Configuration
URL: /typescript-sdk/models

Configure AI models for your Agents and Sub Agents

***

title: Model Configuration
description: Configure AI models for your Agents and Sub Agents
icon: "LuSettings2"
-------------------

Configure models at **Project** (required), **Agent**, or **Sub Agent** levels. Settings inherit down the hierarchy.

## Configuration Hierarchy

You **must configure at least the base model** at the project level:

```typescript
// inkeep.config.ts
export default defineConfig({
  models: {
    base: {
      model: "anthropic/claude-sonnet-4-5",
      providerOptions: { temperature: 0.7, maxOutputTokens: 2048 }
    }
  }
});
```

Override at agent or sub agent level:

```typescript
const myAgent = agent({
  models: {
    base: { model: "openai/gpt-4.1" }  // Override project default
  }
});

const mySubAgent = subAgent({
  models: {
    structuredOutput: { model: "openai/gpt-4.1-mini" }  // Override for JSON output
  }
});
```

## Model Types

| Type               | Purpose                       | Fallback                      |
| ------------------ | ----------------------------- | ----------------------------- |
| `base`             | Text generation and reasoning | **Required at project level** |
| `structuredOutput` | JSON/structured output only   | Falls back to `base`          |
| `summarizer`       | Summaries and status updates  | Falls back to `base`          |

## Supported Models

| Provider       | Example Models                                                                               | API Key                        |
| -------------- | -------------------------------------------------------------------------------------------- | ------------------------------ |
| **Anthropic**  | `anthropic/claude-sonnet-4-5`<br />`anthropic/claude-haiku-4-5`                              | `ANTHROPIC_API_KEY`            |
| **OpenAI**     | `openai/gpt-4.1`<br />`openai/gpt-4.1-mini`<br />`openai/gpt-4.1-nano`<br />`openai/gpt-5`\* | `OPENAI_API_KEY`               |
| **Google**     | `google/gemini-2.5-flash`<br />`google/gemini-2.5-flash-lite`                                | `GOOGLE_GENERATIVE_AI_API_KEY` |
| **OpenRouter** | `openrouter/anthropic/claude-sonnet-4-0`<br />`openrouter/meta-llama/llama-3.1-405b`         | `OPENROUTER_API_KEY`           |
| **Gateway**    | `gateway/openai/gpt-4.1-mini`                                                                | `AI_GATEWAY_API_KEY`           |

<Note>\*`openai/gpt-5`, `openai/gpt-5-mini`, and `openai/gpt-5-nano` require a verified OpenAI organization. If your organization is not yet verified, these models will not be available.</Note>

### Pinned vs Unpinned Models

**Pinned models** include a specific date or version (e.g., `anthropic/claude-sonnet-4-20250514`) and always use that exact version.

**Unpinned models** use generic identifiers (e.g., `anthropic/claude-sonnet-4-5`) and let the provider choose the latest version, which may change over time as providers update their models.

```typescript
models: {
  base: {
    model: "anthropic/claude-sonnet-4-5",  // Unpinned - provider chooses version
    // vs
    model: "anthropic/claude-sonnet-4-20250514"  // Pinned - exact version
  }
}
```

The TypeScript SDK also provides constants for common models:

```typescript
import { Models } from "@inkeep/agents-sdk";

models: {
  base: {
    model: Models.ANTHROPIC_CLAUDE_SONNET_4_5,  // Type-safe constants
  }
}
```

## Provider Options

Inkeep Agents supports all [Vercel AI SDK provider options](https://ai-sdk.dev/providers/ai-sdk-providers/).

### Complete Examples

**Basic configuration:**

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    models: {
      base: {
        model: "anthropic/claude-sonnet-4-5",
        providerOptions: {
          maxOutputTokens: 4096,
          temperature: 0.7,
          topP: 0.95,
          seed: 12345,
          maxDuration: 30,
        }
      }
    }
    ```
  </Tab>

  <Tab title="JSON">
    ```json
    {
      "maxOutputTokens": 4096,
      "temperature": 0.7,
      "topP": 0.95,
      "seed": 12345,
      "maxDuration": 30
    }
    ```
  </Tab>
</Tabs>

**OpenAI with reasoning:**

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    models: {
      base: {
        model: "openai/o1-preview",
        providerOptions: {
          openai: { reasoningEffort: 'medium' }, // 'low' | 'medium' | 'high'
          maxOutputTokens: 4096
        }
      }
    }
    ```
  </Tab>

  <Tab title="JSON">
    ```json
    {
      "openai": { "reasoningEffort": "medium" },
      "maxOutputTokens": 4096
    }
    ```
  </Tab>
</Tabs>

**Anthropic with thinking:**

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    models: {
      base: {
        model: "anthropic/claude-sonnet-4-5",
        providerOptions: {
          anthropic: {
            thinking: { type: 'enabled', budgetTokens: 8000 },
            temperature: 0.5
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="JSON">
    ```json
    {
      "anthropic": {
        "thinking": { "type": "enabled", "budgetTokens": 8000 }
      },
      "temperature": 0.5
    }
    ```
  </Tab>
</Tabs>

**Google with thinking:**

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    models: {
      base: {
        model: "google/gemini-2.5-flash",
        providerOptions: {
          google: {
            thinkingConfig: { thinkingBudget: 8192, includeThoughts: true }
          },
          temperature: 0.7
        }
      }
    }
    ```
  </Tab>

  <Tab title="JSON">
    ```json
    {
      "google": {
        "thinkingConfig": { "thinkingBudget": 8192, "includeThoughts": true }
      },
      "temperature": 0.7
    }
    ```
  </Tab>
</Tabs>

## CLI Defaults

When using `inkeep init`, defaults are set based on your chosen provider:

| Provider      | Base                | Structured Output       | Summarizer              |
| ------------- | ------------------- | ----------------------- | ----------------------- |
| **Anthropic** | `claude-sonnet-4-5` | `claude-sonnet-4-5`     | `claude-sonnet-4-5`     |
| **OpenAI**    | `gpt-4.1`           | `gpt-4.1-mini`          | `gpt-4.1-nano`          |
| **Google**    | `gemini-2.5-flash`  | `gemini-2.5-flash-lite` | `gemini-2.5-flash-lite` |


# Project Structure
URL: /typescript-sdk/project-structure

Learn how to organize your Inkeep Agent projects for optimal development and deployment

***

title: Project Structure
description: Learn how to organize your Inkeep Agent projects for optimal development and deployment
icon: "LuFolder"
----------------

## Overview

Inkeep Agent projects follow a standardized directory structure that enables the CLI to automatically discover and manage your Agents, Sub Agents, tools, and configurations. This convention-based approach simplifies project organization and deployment workflows.

## Standard Project Layout

```
workspace-root/               # Repository/workspace root
├── package.json              # Workspace package.json
├── tsconfig.json             # TypeScript configuration
├── inkeep.config.ts          # Inkeep configuration file
├── my-agent-project/         # Individual project directory
│   ├── index.ts              # Project entry point
│   ├── agents/               # Agent definitions
│   │   ├── main-agent.ts
│   │   └── support-agent.ts
│   ├── tools/                # Tool definitions
│   │   ├── search-tool.ts
│   │   └── calculator-tool.ts
│   ├── data-components/      # Data component definitions
│   │   ├── user-profile.ts
│   │   └── product-catalog.ts
│   ├── external-agents/      # External agent definitions
│   │   ├── exernal-agent-example.ts
│   └── environments/         # Environment-specific configurations
│       ├── index.ts
│       ├── development.env.ts
│       ├── staging.env.ts
│       └── production.env.ts
└── another-project/          # Additional projects can coexist
    ├── index.ts
    └── ...
```

## Core Files

### `inkeep.config.ts`

The configuration file at the workspace root that defines settings for all projects in this workspace:

```typescript
// Located at workspace root, same level as package.json
import { defineConfig } from '@inkeep/agents-cli/config';

export default defineConfig({
  tenantId: 'my-company',
  agentsManageApiUrl: 'http://localhost:3002',
  agentsRunApiUrl: 'http://localhost:3003',
});
```

**Important**: This file lives at the workspace/repository root level, **not** inside individual project directories.

### `index.ts`

The project entry point inside each project directory that exports your project definition:

```typescript
// Located inside project directory (e.g., my-agent-project/index.ts)
import { project } from '@inkeep/agents-sdk';
import { mainAgent } from './agents/main-agent';
import { supportAgent } from './agents/support-agent';
import { searchTool } from './tools/search-tool';
import { calculatorTool } from './tools/calculator-tool';
import { userProfile } from './data-components/user-profile';

export const myProject = project({
  id: 'my-agent-project',
  name: 'My Agent Project',
  description: 'A comprehensive multi-agent system',
  subAgents: () => [mainAgent, supportAgent],
  tools: () => [searchTool, calculatorTool],
  dataComponents: () => [userProfile],
});
```

## Directory Conventions

### `/agents/`

Contains agent definitions. Each file typically exports one agent:

```typescript
// agents/customer-support.ts
import { agent, subAgent } from '@inkeep/agents-sdk';

const routerSubAgent = subAgent({
  id: 'support-router',
  name: 'Support Router',
  prompt: 'Route customer inquiries to appropriate specialists',
});

const billingSubAgent = subAgent({
  id: 'billing-specialist',
  name: 'Billing Specialist',
  prompt: 'Handle billing and payment inquiries',
});

export const customerSupportAgent = agent({
  defaultSubAgent: routerSubAgent,
  subAgents: () => [routerSubAgent, billingSubAgent],
});
```

### `/tools/`

Tool definitions that can be used by Sub Agents:

```typescript
// tools/database-query.ts
import { tool } from '@inkeep/agents-sdk';

export const databaseQueryTool = tool({
  id: 'db-query',
  name: 'Database Query Tool',
  description: 'Execute SQL queries against the database',
  inputSchema: {
    type: 'object',
    properties: {
      query: { type: 'string' },
      database: { type: 'string' }
    }
  },
  // Tool implementation...
});
```

### `/data-components/`

Data components for structured UI output:

```typescript
// data-components/customer-data.ts
import { dataComponent } from '@inkeep/agents-sdk';
import { z } from 'zod';

export const customerData = dataComponent({
  id: 'customer-data',
  name: 'Customer Information',
  description: 'Customer profile and interaction history',
  props: z.object({
    customerId: z.string().describe("Customer ID"),
    name: z.string().describe("Customer name"),
    email: z.string().describe("Customer email"),
  }),
});
```

### `/external-agents/`

External agent definitions:

```typescript
import { externalAgent } from '@inkeep/agents-sdk';

export const exernalAgentExample = externalAgent({
  id: 'exernal-agent-example',
  name: 'Exernal Agent Example',
  description: 'An example external agent',
  baseUrl: 'https://api.example.com/agents/support',
  credentialReference: myCredentialReference,
});
```

### `/environments/`

Environment-specific configurations for different deployment stages:

```typescript
// environments/production.env.ts
import { registerEnvironmentSettings } from '@inkeep/agents-sdk';
import { CredentialStoreType } from '@inkeep/agents-core';

export const production = registerEnvironmentSettings({
  credentials: {
    "openai-prod": {
      id: "openai-prod",
      type: CredentialStoreType.memory,
      credentialStoreId: "memory-default",
      retrievalParams: {
        key: "OPENAI_API_KEY_PROD",
      },
    },
  },
});
```

## File Discovery Process

The CLI automatically discovers files using these patterns:

1. **Config Discovery**: Searches for `inkeep.config.ts`:
   * Starts from current working directory
   * Traverses **upward** through parent directories until found
   * Looks at the same level as `package.json` and `tsconfig.json`
   * Can be overridden with `--config` flag

2. **Project Discovery**: Once config is found:
   * Uses the config file's directory as the workspace root
   * Scans for project subdirectories containing `index.ts`
   * Each project directory is treated as a separate agent project

3. **Resource Discovery**: Within each project directory:
   * Excludes `node_modules/` and `.git/`
   * Categorizes files by directory name and content
   * Processes dependencies and relationships

4. **File Categorization**:
   * **Index files**: `index.ts`, `main.ts` (project entry points)
   * **Agent files**: Files in `/agents/` directory
   * **Sub Agent files**: Files containing Sub Agent definitions
   * **Tool files**: Files in `/tools/` directory
   * **Data component files**: Files in `/data-components/` directory
   * **External agent files**: Files in `/external-agents/` directory
   * **Environment files**: Files in `/environments/` directory

## Best Practices

### Naming Conventions

* Use kebab-case for file names: `customer-support-agent.ts`
* Use camelCase for variable names: `customerSupportAgent`
* Use descriptive IDs: `id: 'customer-support-router'`

### File Organization

* **One primary export per file**: Each file should export one main resource
* **Group related functionality**: Keep related Sub Agents in the same Agent file
* **Separate concerns**: Keep tools, data components, and agents in separate directories
* **Environment isolation**: Use separate files for different environments

### Dependencies

* **Explicit imports**: Import all dependencies explicitly
* **Circular dependency avoidance**: Structure imports to prevent circular references
* **Type safety**: Use TypeScript for all configuration files

## Troubleshooting

### Common Issues

**Config file not found:**

```bash
Error: Could not find inkeep.config.ts in current directory or parent directories
```

* Ensure `inkeep.config.ts` exists at your **workspace root** (same level as `package.json`)
* CLI searches upward from current directory - make sure you're in or below the workspace
* Use `--config` flag to specify custom location if needed

**Invalid project structure:**

```bash
Warning: No agents found in project
```

* Check that you're running from within a project directory (containing `index.ts`)
* Verify Agent files are in the project's `/agents/` subdirectory
* Ensure exports are properly named and typed

**Missing dependencies:**

```bash
Error: Cannot resolve import './agents/missing-agent'
```

* Ensure all imported files exist within the project directory
* Check relative file paths and extensions
* Verify imports use correct paths relative to project root

### Validation

Use the CLI to validate your project structure:

```bash
# Validate project without pushing
inkeep push --json

# Check config resolution
inkeep config get
```

## Migration from Legacy Structures

If migrating from older project structures:

1. **Move config to workspace root**: Ensure `inkeep.config.ts` is at same level as `package.json`
2. **Create project directories**: Organize agents into project subdirectories
3. **Create standard subdirectories**: Add `/agents/`, `/tools/`, `/data-components/` within each project
4. **Move files appropriately**: Organize existing files into correct project and subdirectories
5. **Update imports**: Fix import paths after restructuring
6. **Test compilation**: Run `inkeep push --json` to validate structure
7. **Update CI/CD**: Adjust build scripts for new workspace structure

This standardized structure ensures your projects work seamlessly with the Inkeep CLI and can be easily shared, deployed, and maintained across different environments.


# Push and Pull Workflows
URL: /typescript-sdk/push-pull-workflows

Understand the complete workflows for pushing and pulling agent projects with detailed flow diagrams

***

title: Push and Pull Workflows
description: Understand the complete workflows for pushing and pulling agent projects with detailed flow diagrams
icon: "LuGitBranch"
-------------------

## Overview

The `inkeep push` and `inkeep pull` commands implement sophisticated workflows for deploying and synchronizing agent projects. These workflows handle project discovery, configuration resolution, resource compilation, and bidirectional synchronization between local and remote environments.

## Push Workflow

The push workflow deploys your local project to the Inkeep management API:

```mermaid
graph TD
    A[inkeep push] --> B[Parse CLI Arguments]
    B --> C{--config provided?}
    C -->|Yes| D[Load specified config]
    C -->|No| E[Search for inkeep.config.ts]

    E --> F{Config found?}
    F -->|No| G[Error: Config not found]
    F -->|Yes| H[Load config file]

    D --> I[Apply Environment Variables]
    H --> I
    I --> J[Apply CLI Flag Overrides]

    J --> K{--env provided?}
    K -->|Yes| L[Load environment config]
    K -->|No| M[Use base config only]

    L --> N{Environment file exists?}
    N -->|No| O[Error: Environment not found]
    N -->|Yes| P[Merge environment settings]

    P --> Q[Project Discovery]
    M --> Q

    Q --> R[Scan project directory]
    R --> S[Find TypeScript files]
    S --> T[Categorize files by type]
    T --> U[Load and compile resources]

    U --> V{--json flag?}
    V -->|Yes| W[Export to JSON file]
    V -->|No| X[Validate project resources]

    X --> Y[Connect to Management API]
    Y --> Z[Deploy resources]
    Z --> AA[Print deployment summary]

    W --> BB[Save JSON and exit]
    G --> CC[Exit with error]
    O --> CC
```

### Push Process Details

1. **Argument Parsing**: CLI parses command-line arguments and flags
2. **Configuration Resolution**: Loads and merges configuration from multiple sources
3. **Environment Application**: Applies environment-specific settings if specified
4. **Project Discovery**: Scans project directory for resources
5. **Resource Compilation**: Compiles TypeScript files and resolves dependencies
6. **Validation**: Validates resource configurations and relationships
7. **Deployment**: Uploads resources to management API
8. **Confirmation**: Returns deployment summary

### Configuration Resolution Flow

```mermaid
graph TD
    A[Start Config Resolution] --> B{--config flag?}
    B -->|Yes| C[Load specified file]
    B -->|No| D[Current working directory]

    D --> E{inkeep.config.ts exists?}
    E -->|Yes| F[Load config from current dir]
    E -->|No| G[Check parent directory]
    G --> H{At filesystem root?}
    H -->|No| E
    H -->|Yes| I[Config not found error]

    C --> J[Base Configuration]
    F --> J

    J --> K[Apply Environment Variables]
    K --> L[Apply CLI Flags]
    L --> M{--env flag?}

    M -->|Yes| N[Load environments/env.env.ts from project]
    M -->|No| O[Final Configuration]

    N --> P{Environment file exists in project?}
    P -->|No| Q[Environment error]
    P -->|Yes| R[Merge environment settings]
    R --> O

    style C fill:#e1f5fe
    style F fill:#e1f5fe
    style O fill:#c8e6c9
    style I fill:#ffcdd2
    style Q fill:#ffcdd2

    %% Notes
    S["📝 Config file lives at workspace root<br/>same level as package.json"]
    T["📝 Projects are subdirectories<br/>containing index.ts"]

    style S fill:#fff3e0
    style T fill:#fff3e0
```

## Pull Workflow

The pull workflow synchronizes local files with remote configurations:

<Note>
  **Prerequisites:** The `inkeep pull` command uses AI to generate TypeScript files from your project configuration. You need **at least one** of these API keys set:

  * `ANTHROPIC_API_KEY` - Uses Claude Sonnet 4.5 (recommended)
  * `OPENAI_API_KEY` - Uses GPT-5.1
  * `GOOGLE_GENERATIVE_AI_API_KEY` - Uses Gemini 2.5 Flash

  ```bash
  # Choose one:
  export ANTHROPIC_API_KEY=your_anthropic_key_here
  # OR
  export OPENAI_API_KEY=your_openai_key_here
  # OR  
  export GOOGLE_GENERATIVE_AI_API_KEY=your_google_key_here
  ```

  The CLI automatically selects the first available model based on your configured API keys.
</Note>

```mermaid
graph TD
    A[inkeep pull] --> B[Parse CLI Arguments]
    B --> C[Configuration Resolution]
    C --> D[Connect to Management API]
    D --> E[Fetch project data]

    E --> F{--json flag?}
    F -->|Yes| G[Save as JSON file]
    F -->|No| H[Project File Discovery]

    H --> I[Scan local project directory]
    I --> J[Find TypeScript files]
    J --> K[Categorize files by type]

    K --> L[File Processing Loop]
    L --> M{File type?}

    M -->|Index| N[Full project context]
    M -->|Agent| O[Specific Agent data]
    M -->|Sub Agent| P[Specific Sub Agent data]
    M -->|Tool| Q[Specific tool data]
    M -->|Data Component| R[Specific component data]
    M -->|Other| S[General project context]

    N --> T[LLM Generation Request]
    O --> T
    P --> T
    Q --> T
    R --> T
    S --> T

    T --> U[Generate updated TypeScript]
    U --> V[Validate generated code]
    V --> W{Validation successful?}

    W -->|Yes| X[Write updated file]
    W -->|No| Y[Log generation error]

    X --> Z{More files?}
    Y --> Z
    Z -->|Yes| L
    Z -->|No| AA[Update complete]

    G --> BB[JSON saved]

    style T fill:#fff3e0
    style U fill:#fff3e0
    style V fill:#e8f5e8
    style X fill:#e8f5e8
    style Y fill:#ffebee
```

### Pull Process Details

1. **Configuration Resolution**: Same as push workflow
2. **API Connection**: Connects to management API
3. **Data Fetching**: Retrieves complete project data from server
4. **File Discovery**: Scans local project for TypeScript files
5. **File Categorization**: Identifies file types for context-aware processing
6. **LLM Generation**: Uses AI to update files with server data
7. **Validation**: Validates generated TypeScript syntax
8. **File Updates**: Writes updated content to local files

### File Categorization Logic

```mermaid
graph TD
    A[TypeScript File] --> B{Filename check}

    B -->|index.ts, main.ts| C[Index File]
    B -->|In /agents/ dir| D[Agent File]
    B -->|In /tools/ dir| E[Tool File]
    B -->|In /data-components/ dir| F[Data Component File]
    B -->|In /environments/ dir| G[Environment File]
    B -->|Contains subAgent call| H[Sub Agent File]
    B -->|Other| I[Generic File]

    C --> J[Full project context]
    D --> K[Relevant Agent data]
    E --> L[Relevant tool data]
    F --> M[Relevant component data]
    G --> N[Environment data]
    H --> O[Relevant Sub Agent data]
    I --> P[General context]

    style C fill:#e3f2fd
    style D fill:#f3e5f5
    style E fill:#e8f5e8
    style F fill:#fff3e0
    style G fill:#fce4ec
    style H fill:#e1f5fe
    style I fill:#f5f5f5
```

## Resource Processing Flow

Both push and pull operations process project resources systematically:

```mermaid
graph TD
    A[Workspace Root] --> A1[Find inkeep.config.ts]
    A1 --> B[Discover Project Directories]
    B --> B1[Look for subdirs with index.ts]
    B1 --> C[Scan Project Files]
    C --> D[Exclude patterns]

    D --> E{File location}
    E -->|/node_modules/| F[Skip]
    E -->|/.git/| F
    E -->|project/environments/| G[Environment Config]
    E -->|project/*.ts files| H[Project Resource]

    H --> I[Parse TypeScript]
    I --> J[Extract exports]
    J --> K{Export type}

    K -->|project call| L[Project Definition]
    K -->|agent call| M[Agent Definition]
    K -->|subAgent call| N[Sub Agent Definition]
    K -->|tool call| O[Tool Definition]
    K -->|dataComponent call| P[Data Component]
    K -->|Other| Q[Generic Resource]

    L --> R[Compile Resources per Project]
    M --> R
    N --> R
    O --> R
    P --> R
    G --> S[Load Environment per Project]

    R --> T[Validate Dependencies]
    T --> U[Build Resource Graph]
    U --> V[Ready for Push/Pull]

    style F fill:#ffcdd2
    style G fill:#fff9c4
    style R fill:#c8e6c9
    style V fill:#c8e6c9

    %% Structure note
    W["📁 Workspace Structure:<br/>config.ts at root<br/>projects in subdirs"]
    style W fill:#fff3e0
```

## Error Handling and Recovery

Both workflows include comprehensive error handling:

```mermaid
graph TD
    A[Operation Start] --> B{Config Resolution}
    B -->|Success| C[Continue Processing]
    B -->|Error| D[Config Error Handler]

    C --> E{Project Discovery}
    E -->|Success| F[Resource Processing]
    E -->|Error| G[Project Error Handler]

    F --> H{Resource Validation}
    H -->|Success| I[API Operation]
    H -->|Error| J[Validation Error Handler]

    I --> K{API Request}
    K -->|Success| L[Operation Complete]
    K -->|Error| M[API Error Handler]

    D --> N[Show Config Help]
    N --> O[Suggest Solutions]
    O --> P[Exit with Code 1]

    G --> Q[Show Project Structure Help]
    Q --> O

    J --> R[Show Validation Errors]
    R --> S[Suggest Fixes]
    S --> P

    M --> T[Show API Error Details]
    T --> U[Retry Suggestions]
    U --> P

    style L fill:#c8e6c9
    style P fill:#ffcdd2
    style N fill:#fff3e0
    style Q fill:#fff3e0
    style R fill:#fff3e0
    style T fill:#fff3e0
```

## Performance Optimizations

The workflows include several performance optimizations:

### Parallel Processing

```mermaid
graph TD
    A[File Discovery] --> B[Group by Type]
    B --> C[Parallel Processing]

    C --> D[Agent Files]
    C --> E[Tool Files]
    C --> F[Sub Agent Files]
    C --> G[Data Component Files]

    D --> H[Process Agents]
    E --> I[Process Tools]
    F --> J[Process Sub Agents]
    G --> K[Process Components]

    H --> L[Merge Results]
    I --> L
    J --> L
    K --> L

    L --> M[Dependency Resolution]
    M --> N[Final Resource Graph]
```

### Caching Strategy

```mermaid
graph LR
    A[API Request] --> B{Cache exists?}
    B -->|Yes| C{Cache valid?}
    B -->|No| D[Fetch from API]

    C -->|Yes| E[Return cached data]
    C -->|No| D

    D --> F[Update cache]
    F --> G[Return fresh data]

    style E fill:#c8e6c9
    style G fill:#c8e6c9
```

## Best Practices

### 1. Pre-Push Validation

Always validate your project before pushing:

```bash
# Validate without pushing
inkeep push --json

# Check for TypeScript errors
npx tsc --noEmit

# Run tests
npm test
```

### 2. Environment-Specific Deployments

Use environments for different deployment stages:

```bash
# Development deployment
inkeep push --env development

# Staging deployment
inkeep push --env staging

# Production deployment (with validation)
inkeep push --json && inkeep push --env production
```

### 3. Pull with Backup

Always backup before pulling changes:

```bash
# Create backup branch
git checkout -b backup-before-pull

# Pull changes
inkeep pull

# Review changes
git diff

# Commit or revert as needed
```

### 4. Monitoring Deployments

Use logging and monitoring during deployments:

```bash
# Enable debug logging
DEBUG=1 inkeep push --env production

# Monitor deployment
inkeep list-graphs
```

These workflows provide a robust foundation for managing your Inkeep Agent projects across different environments and deployment scenarios. The visual diagrams help understand the complex interactions between configuration resolution, resource processing, and API communication that make the CLI both powerful and reliable.


# Using SigNoz for Observability
URL: /typescript-sdk/signoz-usage

Complete guide to using SigNoz for observability, monitoring, tracing in the Inkeep Agent Framework

***

title: Using SigNoz for Observability
sidebarTitle: SigNoz Usage
description: Complete guide to using SigNoz for observability, monitoring, tracing in the Inkeep Agent Framework
keywords: SigNoz, observability, monitoring, tracing, OpenTelemetry, APM, metrics
icon: "brand/Signoz"
--------------------

SigNoz is a full-stack observability platform that provides distributed tracing so that you can track requests across multiple agents and services.

### Quick Start

Before using SigNoz, ensure it's properly set up and running. For setup instructions, see the [Quick Start](/get-started/traces) guide.

## Using SigNoz UI

The **Traces** page provides detailed request tracing:

#### Viewing Traces

The SigNoz traces interface provides comprehensive visibility into your agent operations:

<Image src="/images/signoz-traces-ui.png" alt="SigNoz Traces Explorer showing inkeep-agents-run-api service traces with timestamp, service name, operation name, duration, HTTP method, and response status code columns" style={{ border: "1px solid #e1e5e9" }} />

The traces explorer shows:

* **Timestamp**: When each span occurred
* **Service Name**: The service that generated the span (e.g., `inkeep-agents-run-api`)
* **Operation Name**: Specific operations like `ai.generateObject`, `tls.connect`, `ai.toolCall`
* **Duration**: How long each operation took (in milliseconds)
* **HTTP Method**: For HTTP operations, shows the method (POST, GET, etc.)
* **Response Status Code**: HTTP status codes (200, 404, etc.)

Key features of the traces view:

* **Filtering Options**: Use the left sidebar to filter by duration, deployment environment, service name, and more

* **Time Range Selection**: Choose from preset ranges or custom time periods

* **Multiple Views**: Switch between List View, Traces, Time Series, and Table View

* **Real-time Updates**: Traces refresh automatically to show new data

* **Trace List**: Browse all traces with filtering options

* **Trace Details**: Drill down into individual traces

* **Span Timeline**: See the execution flow across agents

#### Filtering Traces

```
# Filter by service
service_name = "inkeep-agents-run-api"

# Filter by operation
operation = "agent.generate"

# Filter by status
status = "error"

# Filter by duration
duration > 1000ms

# Filter by custom attributes
agent.id = "customer-support-agent"
```

#### Analyzing Individual Traces

When you click on a specific trace from the list, you'll see the detailed trace view with a flamegraph visualization:

<Image src="/images/signoz-trace-details.png" alt="SigNoz Trace Details showing flamegraph visualization with span hierarchy, timing information, and detailed span attributes" style={{ border: "1px solid #e1e5e9" }} />

**Flamegraph Visualization:**

* **Horizontal Bars**: Each bar represents a span (operation) in your trace
* **Bar Width**: Proportional to the duration of the operation
* **Color Coding**:
  * Blue bars: Successful operations
  * Red bars: Operations with errors

**Key Information Displayed:**

* **Total Spans**: Total number of operations in this trace (e.g., 122)
* **Error Spans**: Number of spans that encountered errors (e.g., 19)
* **Trace Duration**: Total time for the entire trace (e.g., 5.2 mins)
* **Timestamp**: When the trace occurred
* **Service**: The primary service (e.g., `inkeep-agents-run-api`)

**Span Details Panel (Right Side):**

* **Span Name & ID**: Operation name and unique identifier
* **Timing**: Start time and duration
* **Service & Kind**: Which service and span type (Server, Client, etc.)
* **Status**: Success/error status code
* **Attributes, Events & Links**: Additional span metadata

**How to Use This View:**

1. **Identify Bottlenecks**: Look for the widest bars in the flamegraph - these represent the longest-running operations
2. **Find Errors**: Red bars indicate operations that failed - click on them to see error details
3. **Understand Flow**: Follow the vertical hierarchy to see how operations call each other
4. **Analyze Performance**: Use the timeline to see which operations run in parallel vs. sequentially
5. **Drill Down**: Click on any span to see detailed attributes, events, and error information


# JSON Schema guide for components
URL: /ui-components/json-schema-validation

Guide for writing valid JSON Schemas for data components and artifact components

***

title: JSON Schema guide for components
sidebarTitle: JSON Schemas
description: Guide for writing valid JSON Schemas for data components and artifact components
icon: LuFileCheck
keywords: JSON Schema, data components, artifact components, LLM compatibility
------------------------------------------------------------------------------

This guide shows you how to write valid JSON Schemas for your components. The framework validates these schemas to ensure they work properly with LLMs.

## Why validation matters

LLMs need clear, structured information to understand how to use your components. The validation ensures:

* All properties have descriptions (so the LLM knows what they're for)
* Required fields are clearly marked
* The schema structure is correct

## Data component props

When creating data components, your `props` field must be a valid JSON Schema:

### ✅ Valid example

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "The title of the content item"
    },
    "url": {
      "type": "string",
      "description": "The URL where this content can be accessed"
    },
    "tags": {
      "type": "array",
      "description": "List of tags to categorize this content",
      "items": {
        "type": "string"
      }
    },
    "priority": {
      "type": "string",
      "enum": ["low", "medium", "high"],
      "description": "Priority level for this content item"
    }
  },
  "required": ["title", "url"]
}
```

### ❌ Common mistakes

```json
{
  // ❌ Missing "type": "object"
  "properties": {
    "title": {
      "type": "string"
      // ❌ Missing description
    }
  }
  // ❌ Missing required array
}
```

## Artifact component schemas

Artifact components use a single unified schema called `props` with `inPreview` indicators.

### Unified props schema

Fields marked with `inPreview: true` appear in summary views, while all fields are stored in the database:

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "Title of the artifact",
      "inPreview": true
    },
    "status": {
      "type": "string",
      "enum": ["draft", "published", "archived"],
      "description": "Current status of the artifact",
      "inPreview": true
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "When the artifact was created",
      "inPreview": true
    },
    "content": {
      "type": "string",
      "description": "Main content of the artifact"
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata for the artifact",
      "properties": {
        "author": {
          "type": "string",
          "description": "Who created this artifact"
        },
        "version": {
          "type": "string",
          "description": "Version number of the artifact"
        }
      },
      "required": ["author"]
    },
    "attachments": {
      "type": "array",
      "description": "Files attached to this artifact",
      "items": {
        "type": "object",
        "properties": {
          "filename": {
            "type": "string",
            "description": "Name of the attached file"
          },
          "url": {
            "type": "string",
            "description": "URL to download the file"
          }
        },
        "required": ["filename", "url"]
      }
    }
  },
  "required": ["title", "status", "content"]
}
```

### Using Zod schemas with preview helpers

You can also use Zod schemas with the preview helper:

```typescript
import { z } from 'zod';
import { preview } from '@inkeep/agents-core/utils/schema-conversion';

const artifactSchema = z.object({
  title: preview(z.string().describe("Title of the artifact")),
  status: preview(z.enum(["draft", "published", "archived"]).describe("Current status")),
  content: z.string().describe("Main content of the artifact"),
  metadata: z.object({
    author: z.string().describe("Who created this artifact"),
    version: z.string().describe("Version number")
  })
});
```

## Validation rules

The editor enforces these rules:

1. **Must be an object**: Top level must have `"type": "object"`
2. **Must have properties**: Include a `"properties"` object
3. **Must have required array**: Include a `"required"` array (even if empty)
4. **All properties need descriptions**: Every property must have a `"description"` field

### Quick template

Need a starting point? Click the "Template" button in the editor, or use this:

```json
{
  "type": "object",
  "properties": {
    "example_property": {
      "type": "string",
      "description": "Description of what this property represents"
    }
  },
  "required": ["example_property"]
}
```

## Common patterns

### Optional vs required

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "User's full name"
    },
    "email": {
      "type": "string",
      "description": "User's email address (optional)"
    }
  },
  "required": ["name"]
  // email is optional since it's not in the required array
}
```

### Enums for fixed choices

```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "enum": ["work", "personal", "urgent"],
      "description": "Category to organize this item"
    }
  },
  "required": ["category"]
}
```

### Arrays with specific item types

```json
{
  "type": "object",
  "properties": {
    "images": {
      "type": "array",
      "description": "List of image URLs for this item",
      "items": {
        "type": "string",
        "format": "uri"
      }
    }
  },
  "required": ["images"]
}
```

That's it! The editor will guide you with real-time validation feedback as you type.


# Context Fetchers
URL: /visual-builder/context-fetchers

Learn how to use context fetchers to fetch data from external sources and make it available to your agents

***

title: Context Fetchers
sidebarTitle: Context Fetchers
description: Learn how to use context fetchers to fetch data from external sources and make it available to your agents
icon: "LuCirclePlus"
--------------------

## Overview

Context fetchers allow you to embed real-time data from external APIs into your agent prompts. Instead of hardcoding information in your agent prompt, context fetchers dynamically retrieve fresh data for each conversation.

## Key Features

* **Dynamic data retrieval**: Fetch real-time data from APIs.
* **Dynamic Prompting**: Use dynamic data in your agent prompts
* **Headers integration**: Use request-specific parameters to customize data fetching.
* **Data transformation**: Transform API responses into the exact format your agent needs.

## Context Fetchers vs Tools

* **Context Fetchers**: Pre-populate agent prompts with dynamic data
  * Run automatically before/during conversation startup
  * Data becomes part of the agent's system prompt
  * Perfect for: Personalized agent personas, dynamic agent guardrails
  * Example Prompt: `You are an assistant for {{user.name}} and you work for {{user.organization}}`

* **Tools**: Enable agents to take actions or fetch data during conversations
  * Called by the agent when needed during the conversation
  * Agent decides when and how to use them
  * Example Tool Usage: Agent calls a "send\_email" tool or "search\_database" tool

## Basic Usage

1. Go to the Agents tab in the left sidebar. Then click on the agent you want to configure.
2. On the right pane scroll down to the "Context Variables" section.
3. Add your context variables in JSON format.
4. Click on the "Save" button.

## Defining Context Variables

The keys that you define in the Context Variables JSON object are used to reference fetched data in your agent prompts.
Each key in the JSON should map to a fetch definition with the following properties:

* **`id`** (required): Unique identifier for the fetch definition
* **`name`** (optional): Human-readable name for the fetch definition
* **`trigger`** (required): When to execute the fetch:
  * `"initialization"`: Fetch only once when a conversation is started with the agent
  * `"invocation"`: Fetch every time a request is made to the agent
* **`fetchConfig`** (required): HTTP request configuration:
  * **`url`** (required): The API endpoint URL (supports template variables)
  * **`method`** (optional): HTTP method - `GET`, `POST`, `PUT`, `DELETE`, or `PATCH` (defaults to `GET`)
  * **`headers`** (optional): Object with string key-value pairs for HTTP headers
  * **`body`** (optional): Request body for POST/PUT/PATCH requests
  * **`transform`** (optional): JSONPath expression or JavaScript transform function to extract specific data from the response
  * **`timeout`** (optional): Request timeout in milliseconds (defaults to 10000)
* **`responseSchema`** (optional): Valid JSON Schema object to validate the API response structure.
* **`defaultValue`** (optional): Default value to use if the fetch fails or returns no data
* **`credential`** (optional): Reference to stored credentials for authentication

Here is an example of a valid Context Variables JSON object:

```json
{
  "userInfo": {
    "id": "user-info",
    "name": "User Information",
    "trigger": "initialization",
    "fetchConfig": {
      "url": "https://api.example.com/users/{{headers.user_id}}",
      "method": "GET",
      "headers": {
        "Authorization": "Bearer {{headers.api_key}}"
      },
      "transform": "user"
    },
    "responseSchema": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "email": {
          "type": "string"
        }
      },
    },
    "defaultValue": "Unable to fetch user information"
  }
}
```

## Using Context Variables

Once you have defined your context variables, you can use them in your agent prompts.

1. Click on the agent you want to modify.
2. In the "Prompt" section, you can embed fetched data in the prompt using the key defined in the "Context Variables" section. Reference them using double curly braces `{{}}`.

Here is an example of an agent prompt using the context variable defined above:

```
You are a helpful assistant for {{userInfo.name}}.
```

# Related documentation

* [Headers](/visual-builder/headers) - Learn how to pass dynamic context to your agents via HTTP headers


# Headers
URL: /visual-builder/headers

Pass dynamic context to your agents via HTTP headers for personalized interactions

***

title: Headers
sidebarTitle: Headers
description: Pass dynamic context to your agents via HTTP headers for personalized interactions
icon: LuBoxes
keywords: headers, context fetchers, prompt variables, personalization
----------------------------------------------------------------------

## Overview

Headers allow you to pass request-specific values (like user IDs, authentication tokens, or organization metadata) to your agent at runtime via HTTP headers. These values are validated and made available throughout your agent system for:

* **Context Fetchers**: Dynamic data retrieval based on request values
* **External Tools**: Authentication and personalization for API calls
* **Agent Prompts**: Personalized responses using context variables

## Configuring Headers

1. Go to the Agents tab in the left sidebar. Then click on the agent you want to configure.
2. On the right pane scroll down to the "Headers schema" section.
3. Enter the schema in JSON Schema format.
4. Click on the "Save" button.

Here is an example of a valid headers schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "userId": {
      "type": "string"
    }
  },
  "required": [
    "userId"
  ],
  "additionalProperties": {}
}
```

You can generate custom schemas using this [JSON Schema generator](https://transform.tools/json-to-json-schema).

## Sending Custom Headers

1. On your agent page, click on the **Try it** button in the top right corner.
2. Click on the "Custom headers" button in the top right corner.
3. Enter the custom headers in JSON format.
4. Click on the "Apply" button.

## Using Headers in Your Agent Prompts

1. Go to the Agents tab in the left sidebar. Then click on the agent you want to configure.
2. Either add a new agent or edit an existing agent by clicking on the agent you want to edit.
3. On the right pane scroll down to the "Prompt" section.
4. Use the double curly braces `{{}}` to reference the headers variables.

Here is an example of a valid prompt:

```text
You are a helpful assistant for {{headers.user_id}}!.
```


# Project Management
URL: /visual-builder/project-management

Learn how to create and manage projects in the Inkeep Agent Framework

***

title: Project Management
description: Learn how to create and manage projects in the Inkeep Agent Framework
icon: "LuFolder"
----------------

## Overview

Projects are the top-level organizational unit in the Inkeep Agent Framework. Each project contains its own agents, tools, and resources. This allows you to separate different applications or environments within a single tenant.

## Creating a Project

There are two ways to create a new project:

### Using the Project Dialog

When you have existing projects, you can create a new one using the "Create Project" button in the project switcher at the bottom of the sidebar.

### First Project Creation

If you don't have any projects yet, you'll be automatically redirected to the project creation page when you log in. You can also access it directly at `/{tenantId}/projects/new`.

## Project Fields

When creating a project, you'll need to provide:

* **Project ID**: A unique identifier for your project. This must:

  * Start and end with lowercase alphanumeric characters
  * May contain hyphens in the middle
  * Cannot be changed after creation
  * Examples: `my-project`, `production-v2`, `test-env1`

* **Project Name**: A friendly display name for your project (up to 100 characters)

* **Description**: A brief description of what the project is for (up to 500 characters)

## Project Structure

Each project can contain:

* **Agents**: Collections of AI agents that work together
* **API Keys**: Authentication keys for accessing your agents via API
* **MCP Servers**: Model Context Protocol servers for external tools
* **Data Components**: Reusable data structures for your agents
* **Artifact Components**: Reusable UI components for agent outputs
* **Credentials**: Secure storage for API keys and authentication tokens

## Project-Level Configuration

Projects can define default configurations that cascade down to all agents and Sub Agents within the project. This provides a consistent baseline while allowing specific overrides where needed.

### Model Settings

Define default models at the project level that all agents and Sub Agents will inherit:

```typescript
// Project configuration
{
  id: "my-project",
  name: "My AI Project",
  models: {
    base: {
      model: "anthropic/claude-sonnet-4-5",
      providerOptions: {
        temperature: 0.7,
        maxOutputTokens: 4096
      }
    },
    structuredOutput: {
      model: "openai/gpt-4.1-mini",
      providerOptions: {
        temperature: 0.1,
        maxOutputTokens: 2048
      }
    },
    summarizer: {
      model: "openai/gpt-4.1-nano",
      providerOptions: {
        temperature: 0.3,
        maxOutputTokens: 1024
      }
    }
  }
}
```

### StopWhen Configuration

Configure default stopping conditions to prevent infinite loops:

```typescript
{
  id: "my-project",
  stopWhen: {
    transferCountIs: 5,    // Max transfers between Sub Agents per conversation
    stepCountIs: 20        // Max tool calls + LLM responses per Sub Agent execution
  }
}
```

## Configuration Inheritance

The framework uses a cascading inheritance system with specific rules for different configuration types:

### Model Inheritance - Partial Cascading

**Project** → **Agent** → **Sub Agent**

The framework supports **partial cascading**, meaning each level can override specific model types while inheriting others. This provides maximum flexibility while maintaining sensible defaults.

#### How Partial Cascading Works

Each model type (`base`, `structuredOutput`, `summarizer`) cascades independently:

```typescript
// Project Level - Sets defaults for all agents
Project: {
  models: {
    base: { model: "anthropic/claude-sonnet-4-5" },
    structuredOutput: { model: "openai/gpt-4.1-mini" },
    summarizer: { model: "openai/gpt-4.1-nano" }
  }
}

// Agent Level - Partially overrides project defaults
Agent: {
  models: {
    base: { model: "openai/gpt-4.1" }  // Override: use different base model
    // structuredOutput: INHERITED from project (openai/gpt-4.1-mini)
    // summarizer: INHERITED from project (openai/gpt-4.1-nano)
  }
}

// Sub Agent Level - Can override any inherited model
Sub Agent: {
  models: {
    summarizer: { model: "anthropic/claude-haiku-4-5" }  // Override: use faster summarizer
    // base: INHERITED from Agent (openai/gpt-4.1)
    // structuredOutput: INHERITED from project (openai/gpt-4.1-nano)
  }
}
```

#### Final Resolution Example

In the above example, the Sub Agent ends up with:

* **base**: `gpt-4.1` (from Agent)
* **structuredOutput**: `gpt-4.1-mini` (from project)
* **summarizer**: `claude-3.5-haiku` (from Sub Agent)

#### Provider Options Override

When a model is overridden at any level, the entire configuration (including provider options) is replaced:

```typescript
// Project defines base model with options
Project: {
  models: {
    base: {
      model: "claude-sonnet-4-0",
      providerOptions: {
        temperature: 0.7,
        maxOutputTokens: 4096
      }
    }
  }
}

// Agent completely overrides the base model settingsuration
Agent: {
  models: {
    base: {
      model: "claude-sonnet-4-0", // Same model
      providerOptions: {
        temperature: 0.3,  // New temperature
        maxOutputTokens: 2048    // New maxOutputTokens - project maxOutputTokens is NOT inherited
      }
    }
  }
}
```

#### Fallback to Base Model

**Important**: `structuredOutput` and `summarizer` only fall back to the `base` model when there's nothing to inherit from higher levels (project/agent).

#### System Defaults

**Supported Providers**: The framework supports Anthropic, OpenAI, and Google models.

**API Keys**: You need the appropriate API key for the provider you choose to use:

* `ANTHROPIC_API_KEY` for Anthropic models
* `OPENAI_API_KEY` for OpenAI models
* `GOOGLE_GENERATIVE_AI_API_KEY` for Google models

```typescript
// No higher-level defaults - fallback to base occurs
Project: {
  // No models configured
}

Agent: {
  // No models configured
}

Sub Agent: {
  models: {
    base: {
      model: "gpt-4.1-2025-04-14",
      providerOptions: {
        temperature: 0.7,
        maxOutputTokens: 2048
      }
    }
    // No structuredOutput or summarizer specified
  }
}
```

**Final Resolution with Fallback:**

* **base**: `gpt-4.1-2025-04-14` with specified provider options (from Agent)
* **structuredOutput**: `gpt-4.1-2025-04-14` with same provider options (falls back to Agent's base)
* **summarizer**: `gpt-4.1-2025-04-14` with same provider options (falls back to Agent's base)

**Contrast with Inheritance:**

```typescript
// Project has summarizer configured - inheritance takes priority
Project: {
  models: {
    summarizer: {
      model: "gpt-4.1-mini";
    }
  }
}

Sub Agent: {
  models: {
    base: {
      model: "gpt-4.1";
    }
  }
}
```

**Final Resolution with Inheritance:**

* **base**: `gpt-4.1` (from Sub Agent)
* **summarizer**: `gpt-4.1-mini` (inherited from project - NO fallback to Sub Agent's base)
* **structuredOutput**: Falls back to Sub Agent's base `gpt-4.1` (no inheritance available, so fallback occurs)

### StopWhen Inheritance

StopWhen settings inherit from Project → Agent → Sub Agent:

* **`transferCountIs`**: Project or Agent level
* **`stepCountIs`**: Project or Sub Agent level

```typescript
// Project sets defaults
Project: {
  stopWhen: {
    transferCountIs: 5,   // Max transfers per conversation
    stepCountIs: 15      // Max steps per Sub Agent
  }
}

// Agent can override transfer limit, inherits step limit
Agent: {
  stopWhen: {
    transferCountIs: 8    // Override: allow more transfers in this Agent
    // stepCountIs: 15 (inherited from project)
  }
}

// Individual Sub Agent can override its own step limit
Sub Agent: {
  stopWhen: {
    stepCountIs: 25      // This Sub Agent can take more steps
    // transferCountIs not applicable at Sub Agent level
  }
}
```

## Switching Between Projects

Use the project switcher in the bottom left of the sidebar to quickly switch between projects. The switcher shows:

* The project name (or ID if no name is set)
* The project ID
* A brief description (if provided)

## API Access

Projects can be accessed programmatically via the CRUD API:

```typescript
// List all projects
GET /tenants/{tenantId}/crud/projects

// Get a specific project
GET /tenants/{tenantId}/crud/projects/{projectId}

// Create a new project
POST /tenants/{tenantId}/crud/projects
{
  "id": "my-project",
  "name": "My Project",
  "description": "A project for my AI agents"
}

// Update a project
PATCH /tenants/{tenantId}/crud/projects/{projectId}
{
  "name": "Updated Name",
  "description": "Updated description"
}

// Delete a project
DELETE /tenants/{tenantId}/crud/projects/{projectId}
```

## Best Practices

1. **Use descriptive IDs**: Choose project IDs that clearly indicate their purpose (e.g., `customer-support`, `internal-tools`)

2. **Separate by environment**: Create different projects for development, staging, and production

3. **Document your projects**: Use the description field to explain what each project is for

4. **Organize by application**: Group related agents and tools within the same project

## Next Steps

After creating a project, you can:

* [Create your first Agent](/visual-builder/sub-agents)
* [Configure MCP servers for tools](/visual-builder/tools/mcp-servers)
* [Set up API keys for external access](/api-keys)


# Get started with the Visual Agent Builder
URL: /visual-builder/sub-agents

Create Agents with a No-Code Visual Agent Builder

***

title: Get started with the Visual Agent Builder
sidebarTitle: Agents & Sub Agents
description: Create Agents with a No-Code Visual Agent Builder
icon: "LuSpline"
----------------

## Overview

An Agent is the top-level entity you can chat and interact with in the Visual Builder.

An Agent is made up of one or more Sub Agents. The Sub Agents that make up an Agent can delegate or transfer control to each other, share context, or use tools to respond to a user or complete a task.

You can use the Visual Builder to add Sub Agents to an Agent, give Sub Agents tools, and connect Sub Agents with each other to establish their relationships.

## Creating your first Agent

<Video src="/videos/create-an-agent.mp4" />

1. Go to the Agents tab in the left sidebar. Then select "Create Agent".

2. Provide a name, prompt, and description.

### Agent Prompt

You can configure an Agent-level prompt that gets automatically added to all Sub Agents that make up the Agent. This provides consistent context and behavior guidelines so Sub Agents respond and act as one cohesive unit.

**Example uses:**

* Company-wide policies and tone guidelines
* Domain-specific context that applies to all sub-agents
* Consistent behavior rules across the sub-agent network

Once an Agent is created, you can always edit the prompt by:

1. Clicking on the **Agent Settings** button next to **Try it**
2. Modify your prompt in the "Agent Prompt" field
3. Click **Save**

## Default Sub Agent

When you create an Agent, it'll have a **Default Sub Agent** by default. This is the Sub Agent that first receives and processes a user message.

Configure its name and prompt, then click **Save**.

## Trying the Agent

To try the Agent, ensure it has at least one Sub Agent, then save the Agent by clicking the "Save changes" button in the top right corner.

Then, click the **Try it** button in the top right corner and type into the chat input.

<Video src="/videos/try-an-agent.mp4" />

## Adding tools

Tools are used to perform actions in the Agent. You can register MCP tools in the Visual Builder. See the [MCP Servers](/visual-builder/tools/mcp-servers) page to get started.

Once you have an MCP Server registered, you can add it to a Sub Agent by dragging and dropping the **MCP** block from the top left onto the Canvas.

To connect the tool to the Sub Agent, click the "+" icon at the top of the MCP block, then drag the connector to the Sub Agent. A line will appear, indicating that the tool is connected to the Sub Agent.

<Video src="/videos/add-tool-vb.mp4" />

<Note>
  To delete a tool, click on the tool box and then hit the backspace key.
</Note>

## Add other Sub Agents

When you have tasks that get more complex, you'll likely want to create more Sub Agents that are specialized in narrow tasks and have prompts and tools focused on their roles.

To create more Sub Agents:

1. Drag and drop a **Sub Agent** block from the top left toolbar onto the canvas.
2. Configure the Sub Agent with its own prompt and settings
3. Connect it to the parent Sub Agent by clicking the connector at the top of the Sub Agent box and dragging it to the main Sub Agent

When connected, a line will appear showing the relationship between the Sub Agents.

A few notes:

* To delete a Sub Agent, click on the Sub Agent box and then hit the backspace key.
* An Agent must have at least one Sub Agent. If you delete the default Sub Agent, add a new one before trying the Agent.

<Video src="/videos/add-sub-agent-vb.mp4" />

### Sub Agent configuration

The following are configurable options for the Sub Agent through the Visual Builder:

| Parameter             | Type   | Required | Description                                                                                                                                   |
| --------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                | string | Yes      | Human-readable name for the Sub Agent                                                                                                         |
| `description`         | string | No       | Brief description of the Sub Agent's purpose and capabilities                                                                                 |
| `prompt`              | string | Yes      | Detailed behavior guidelines and system prompt for the Sub Agent                                                                              |
| `model`               | string | No       | AI model identifier (e.g., "anthropic/claude-sonnet-4-20250514"). Choose a model that you prefer                                              |
| `providerOptions`     | object | No       | Model-specific configuration options (temperature, maxOutputTokens, etc.)                                                                     |
| `Data components`     | object | No       | Data components that the Sub Agent can use. See [Data Components](/visual-builder/structured-outputs/data-components) for details             |
| `Artifact components` | array  | No       | Artifact components that the Sub Agent can use. See [Artifact Components](/visual-builder/structured-outputs/artifact-components) for details |

## Adding data components

Data components are used to render rich UI components directly in the chat. Before adding a data component, you will first need to create a data component. See the [Data Components](/visual-builder/structured-outputs/data-components) page for more information.

Then, add the data component to your Sub Agent by clicking the Sub Agent box and then selecting which data components you want to add.

## Adding artifact components

To create artifact components, see the [Artifact Components](/visual-builder/structured-outputs/artifact-components) page for details.

Add the artifact component to your Sub Agent by clicking on the Sub Agent box in the Agent, then selecting which artifact components you want to add.

When the Sub Agent uses tools or delegates to other Sub Agents, artifacts will be automatically created according to your defined schema, capturing the source and content of each interaction.

## Adding team agents

Team agents are agents that are part of the same project. You can add team agents to your Agent by dragging and dropping the **Team Agent** block from the top left onto the Canvas.
You can configure custom headers to send on every request to the team agent by clicking on the team agent box and then populating the **Headers** field with your custom headers.

## Adding external agents

External agents let you integrate agents built outside of Inkeep (using other frameworks or platforms) into your Agent.
You can add an external agent to your Agent by dragging and dropping the **External Agent** block from the top left onto the Canvas.

You can configure custom headers to send on every request to the external agent by clicking on the external agent box and then populating the **Headers** field with your custom headers.


# Manage API Authentication
URL: /api-reference/authentication/manage-api

Authentication modes for Manage API

***

title: Manage API Authentication
description: Authentication modes for Manage API
icon: "LuShield"
----------------

The Manage API (`agents-manage-api`) has two authentication modes:

### Secured Mode

When `INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET` is set:

* Include the secret as a Bearer token in requests
* Recommended for production environments

### Open Mode

When `INKEEP_AGENTS_MANAGE_API_BYPASS_SECRET` is not set:

* No authentication required
* Useful for local development


# Run API Authentication
URL: /api-reference/authentication/run-api

Authentication modes for Run API

***

title: Run API Authentication
description: Authentication modes for Run API
icon: "LuShield"
----------------

The Run API (`agents-run-api`) has three authentication modes depending on your environment configuration:

### Development Mode

When `ENVIRONMENT=development`:

* No API key required
* Must include scope headers:
  * `x-inkeep-tenant-id`
  * `x-inkeep-project-id`
  * `x-inkeep-agent-id`

```bash
curl -H "x-inkeep-tenant-id: tenant-123" \
     -H "x-inkeep-project-id: project-456" \
     -H "x-inkeep-agent-id: agent-789" \
     https://localhost:3003/v1/chat/completions
```

### Standard Mode

When `ENVIRONMENT≠development` and `INKEEP_AGENTS_RUN_API_BYPASS_SECRET` is not set:

* Use API keys created from the Manage UI
* No additional headers required (scope encoded in key)

```bash
curl -H "Authorization: Bearer sk_live_abc123..." \
  https://localhost:3003/v1/chat/completions
```

### Bypass Mode

When `ENVIRONMENT≠development` and `INKEEP_AGENTS_RUN_API_BYPASS_SECRET` is set:

**Option 1: Bypass Secret**

* Use the bypass secret as token
* Must include scope headers

```bash
curl -H "Authorization: Bearer YOUR_BYPASS_SECRET" \
     -H "x-inkeep-tenant-id: tenant-123" \
     -H "x-inkeep-project-id: project-456" \
     -H "x-inkeep-agent-id: agent-789" \
     https://run-api.example.com/chat/completions
```

**Option 2: Standard API Keys remain valid**

* Use API keys from the Manage UI

```bash
curl -H "Authorization: Bearer sk_live_xyz789..." \
  https://run-api.example.com/chat/completions
```

## Running Multiple Instances

You can run multiple Run API instances with different auth configurations. If you're deploying Inkeep Agents to production, it is common to only expose the deployment of Run API in standard mode and all other services remain internal.

```bash
# Instance 1: Port 3003 with bypass secret (intended for internal purposes)
PORT=3003 INKEEP_AGENTS_RUN_API_BYPASS_SECRET=secret123 pnpm dev

# Instance 2: Port 3004 without bypass secret (intended for external purposes)
PORT=3004 pnpm dev
```

## Security Best Practices

1. **Production**: Always use Standard API keys
2. **Bypass Secret**: Use for internal services only
3. **API Keys**: Rotate regularly and set expiration dates


# Environment Configuration
URL: /community/contributing/environment-configuration

How to configure the environment variables for the Inkeep Agent Framework

***

title: Environment Configuration
description: How to configure the environment variables for the Inkeep Agent Framework
icon: "LuSettings"
------------------

# Environment Configuration

## Overview

The Inkeep Agents framework uses a **centralized environment configuration**. This approach provides a single source of truth for all environment variables across the monorepo, eliminating duplication and simplifying configuration management.

## Configuration Structure

### Single Root Configuration

All packages in the monorepo reference a **single `.env` file** at the repository root. This is different from the typical approach of having separate `.env` files per package.

```
agents-4/
├── .env                    # Main configuration (gitignored)
├── .env.example            # Template with all variables
└── packages/
    └── agents-core/
        └── src/env.ts      # Centralized env loader
```

### Loading Priority

Environment variables are loaded in the following order (highest priority first):

1. **`/package-name/.env`** Package specific configuration
2. **`.env`** - Main configuration file
3. **`~/.inkeep/config`** - User-global settings (shared across all repo copies)
4. **`.env.example`** - Default values

This hierarchy allows for flexible configuration management across different scenarios. If you have .env or .env.local in a package directory, they will override the root .env or .env.local for that package.

## Use Cases

### 1. Basic Local Development

For simple local development with a single repository copy:

```bash
# Copy the template
cp .env.example .env

# Edit .env with your configuration
vim .env

# Start development
pnpm dev
```

## Troubleshooting

### Environment variables not loading

1. Check loading order - later sources override earlier ones
2. Verify file paths are correct
3. Ensure `packages/agents-core` is built: `pnpm --filter @inkeep/agents-core build`

### Missing variables in production

Ensure all required variables are set in your deployment environment. The application will fail fast if critical variables are missing.

### Database connection issues

* For SQLite: Make sure youu are using an absolute path to the db file


# Contribute to Inkeep Open Source project
URL: /community/contributing/overview

How to contribute to the Inkeep Agent Framework

***

title: Contribute to Inkeep Open Source project
sidebarTitle: How to start
description: How to contribute to the Inkeep Agent Framework
icon: "LuZap"
-------------

# Making a Contribution

Thank you for your interest in contributing to the Agent Framework! This document provides guidelines and information for contributors.

# Launch the Visual Builder

### Prerequisites

Before getting started, ensure you have the following installed on your system:

* [Node.js](https://nodejs.org/en/download/) version 22 or higher
* [Docker](https://docs.docker.com/get-docker/)
* [pnpm](https://pnpm.io/installation) version 10 or higher

### Step 1: Clone the repository

```
git clone https://github.com/inkeep/agents.git
cd agents
```

### Step 2: Run the setup script

For first-time setup, run:

```bash
pnpm setup-dev
```

This will:

1. Create `.env` from the template
2. Set up user-global config at `~/.inkeep/config`
3. Install dependencies
4. Initialize the database, starting the postgres docker container and applying migrations

Add API keys for the AI providers you want to use to the root `.env`. You must have at least one AI provider configured.

```
ANTHROPIC_API_KEY=sk-ant-xyz789
OPENAI_API_KEY=sk-xxx
GOOGLE_GENERATIVE_AI_API_KEY=sk-xxx
```

Add your SigNoz API key to enable the traces feature (optional).

```
SIGNOZ_API_KEY=sk-xxx
```

Add your Nango secret key to enable the Nango credential store (optional).

```
NANGO_SECRET_KEY=sk-xxx
```

### Step 5: Run the agent framework

```bash
pnpm dev
```

### Step 6: Start building!

Open `http://localhost:3000` in the browser and start building agents.

# Push your project

A key advantage of the Inkeep agent framework is its seamless code-to-visual workflow: define your agents programmatically, push them to the Visual Builder, and continue developing with the intuitive drag-and-drop interface.

Follow the steps below to push your project using the [Inkeep CLI](/typescript-sdk/cli-reference).

### Step 1: Download the Inkeep CLI

```bash
pnpm install -g @inkeep/agents-cli
```

### Step 2: Push the project

```bash
cd agents-cookbook/template-projects/weather-project
inkeep push
```

<Note>
  The project will be pushed according to the project specified in the
  `/agents-cookbook/template-projects/inkeep.config.ts` file, which is set to the `default` project by
  default. Feel free to change it to your own project.
</Note>

### Step 3: Observe the Agent in the Visual Builder

<Image src="/gifs/basic-agent.gif" alt="Basic Agent" style={{ border: "1px solid #e1e5e9" }} />

# Set up live traces

### Step 1: Launch docker containers

```bash
cd deploy/docker
docker compose up -d
```

### Step 2: Fetch SigNoz API Key

Open `http://localhost:3080` in the browser. Go to **Settings** → **Workspace Settings** → **API Keys** and copy the API key.

### Step 3: Configure environment variable

Create a `.env` file at `/agents-manage-ui/` with the following variable:

```
SIGNOZ_API_KEY=your-signoz-api-key-here
```

### Step 4: View your live traces

Refresh the live traces panel on the right to see your agents in action.

<Image src="/images/live-traces.png" alt="Live traces showing" style={{ border: "1px solid #e1e5e9" }} />

# Set up credentials

### Step 1: Create .env file and generate encryption key

```bash
cp deploy/docker/.env.nango.example deploy/docker/.env && encryption_key=$(openssl rand -base64 32) && sed -i '' "s|REPLACE_WITH_BASE64_256BIT_ENCRYPTION_KEY|$encryption_key|" deploy/docker/.env && echo "Docker environment file created with auto-generated encryption key"
```

### Step 2: Restart the containers

```bash
cd deploy/docker
docker compose up -d
```

### Step 3: Get your Nango API key

Open the Nango Dashboard: `http://localhost:3050` and navigate to **Environment Settings** → **API Keys** and copy the API key.

### Step 4: Configure environment variables

Navigate back to the root directory and paste the below command. Enter your Nango API key when prompted:

```bash
cd ../../
printf "Enter your Nango API key: " && read key && sed -i '' "s|^NANGO_SECRET_KEY=.*|NANGO_SECRET_KEY=$key|" agents-manage-api/.env agents-run-api/.env agents-manage-ui/.env && echo "Application files updated with Nango API key"
```

### Step 5: Start creating credentials!

Navigate to the Credentials tab in the left sidebar and click "Create credential".

# Development Workflow

### Git Hooks

This project uses Husky for Git hooks to maintain code quality. The hooks are automatically installed when you run `pnpm install`.

#### Pre-commit Hook

The pre-commit hook runs the following checks before allowing a commit:

1. **Type checking** - Ensures type safety across all packages
2. **Tests** - Runs the test suite

##### Bypassing Checks

While we recommend running all checks, there are legitimate cases where you might need to bypass them:

**Skip typecheck only (tests still run):**

```bash
SKIP_TYPECHECK=1 git commit -m "WIP: debugging issue"
```

**Skip all hooks (use sparingly):**

```bash
git commit --no-verify -m "emergency: hotfix for production"
```

> **Note:** Use these bypass mechanisms sparingly. They're intended for:
>
> * Work-in-progress commits that you'll fix before pushing
> * Emergency fixes where speed is critical
> * Commits that only touch non-code files (though hooks are smart enough to handle this)

### Code Quality

#### Type Checking

Run type checking across all packages:

```bash
pnpm typecheck
```

#### Linting

Run the linter:

```bash
pnpm lint
```

Format code automatically:

```bash
pnpm format
```

#### Testing

Run tests:

```bash
pnpm test              # Run all tests
pnpm test:watch        # Run tests in watch mode
pnpm test:coverage     # Run tests with coverage report
```

### Building

Build all packages:

```bash
pnpm build
```

# CLI Development

## Running the CLI Locally

When developing the CLI, you can run the local version directly without global installation:

```bash
# Build the CLI first
cd agents-cli
pnpm build

# Run the local CLI from the repository root
node agents-cli/dist/index.js --version

# Or use the convenience script (if available)
./scripts/inkeep-local.sh --version
```

## Testing CLI Changes

1. **Build the CLI after making changes:**

```bash
cd agents-cli
pnpm build
```

2. **Test commands locally:**

```bash
# From repository root
node agents-cli/dist/index.js push examples/agent-configurations
node agents-cli/dist/index.js chat
```

3. **Run CLI tests:**

```bash
cd agents-cli
pnpm test
```

## Switching Between Local and Published CLI

During development, you may need to test both the local development version and the published npm package:

```bash
# Use local development version
node /path/to/agents/agents-cli/dist/index.js --version

# Use globally installed published version
inkeep --version
```

For detailed information about switching between versions, see the `INKEEP_CLI_SWITCHING.md` file in the repository root.

# Commit Messages

We follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:

* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation changes
* `style`: Code style changes (formatting, etc.)
* `refactor`: Code refactoring
* `test`: Test changes
* `chore`: Build process or auxiliary tool changes

# Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Make your changes
4. Ensure all checks pass (`pnpm typecheck && pnpm test`)
5. Commit your changes (following commit message guidelines)
6. Push to your fork
7. Open a pull request

### PR Guidelines

* Keep PRs focused on a single feature or fix
* Update tests for any behavior changes
* Update documentation as needed
* Ensure CI passes before requesting review

# Continuous Integration

Our CI pipeline runs on all pull requests and includes:

* Type checking (`pnpm typecheck`)
* Tests (`pnpm test`)
* Build verification (`pnpm build`)

These checks must pass before a PR can be merged. The same checks run in pre-commit hooks to catch issues early.

# Questions?

If you have questions about contributing, please:

1. Check existing issues and discussions
2. Open a new issue if your question isn't addressed
3. Reach out to the maintainers

Thank you for contributing!


# Data Layer constraints on Project relationships
URL: /community/contributing/project-constraints

How the Inkeep Agent Framework ensures data integrity with project constraints

***

title: Data Layer constraints on Project relationships
sidebarTitle: Project Data Layer
description: How the Inkeep Agent Framework ensures data integrity with project constraints
icon: "LuTriangleAlert"
-----------------------

# Project Constraints and Validation

The Inkeep Agent Framework implements multiple layers of validation to ensure that all agents and resources are associated with valid projects.

## Database-Level Constraints

### Foreign Key Constraints

All tables that reference projects include foreign key constraints to ensure referential integrity:

```sql
FOREIGN KEY (tenant_id, project_id)
REFERENCES projects(tenant_id, id)
ON DELETE CASCADE
```

This ensures that:

* No data can be inserted for non-existent projects
* Deleting a project cascades to remove all associated resources
* Data integrity is maintained at the database level

### Tables with Project Constraints

The following tables have foreign key constraints to the `projects` table:

1. `agent` - Agent definitions (top-level Agents)
2. `sub_agents` - Sub Agent configurations
3. `sub_agent_relations` - Relationships between Sub Agents
4. `tools` - Tool configurations
5. `context_configs` - Context configurations
6. `external_agents` - External agent references
7. `conversations` - Chat conversations
8. `messages` - Chat messages
9. `tasks` - Task records
10. And more...

## Runtime Validation

### CLI Validation

The Inkeep CLI validates project existence before pushing agents:

```typescript
// CLI checks if project exists
const existingProject = await getProject(dbClient)({
  scopes: { tenantId, projectId },
});

if (!existingProject) {
  // Prompt user to create project
  // ...
}
```

### Data Access Layer Validation

The core package provides validation utilities for runtime checks:

```typescript
import { validateProjectExists } from "@inkeep/agents-core";

// Validate before any operation
await validateProjectExists(db, tenantId, projectId);
```

### Wrapped Operations

Data access functions can be wrapped with automatic validation:

```typescript
import { withProjectValidation } from "@inkeep/agents-core";

const validatedCreateAgent = withProjectValidation(db, createAgent);
// Now automatically validates project before creating agent
```

## Implementation Details

### Schema Definition

```typescript
export const agents = sqliteTable(
  "agent",
  {
    tenantId: text("tenant_id").notNull(),
    projectId: text("project_id").notNull(),
    // ... other columns
  },
  (table) => [
    primaryKey({ columns: [table.tenantId, table.projectId, table.id] }),
    foreignKey({
      columns: [table.tenantId, table.projectId],
      foreignColumns: [projects.tenantId, projects.id],
      name: "agent_project_fk",
    }),
  ]
);
```

### Enabling Foreign Keys in SQLite

SQLite requires explicit enabling of foreign key constraints:

```sql
PRAGMA foreign_keys = ON;
```

This should be set when creating the database connection:

```typescript
const client = createClient({
  url: dbUrl,
  authToken: authToken,
});

// Enable foreign keys
await client.execute("PRAGMA foreign_keys = ON");
```

## Error Handling

When a constraint violation occurs, appropriate error messages guide users:

### CLI Error

```
⚠ Project "my-project" does not exist
? Would you like to create it? (Y/n)
```

### Database Error

```
Error: Project with ID "my-project" does not exist for tenant "my-tenant".
Please create the project first before adding resources to it.
```

## Best Practices

1. **Always validate at multiple levels**: Database constraints, runtime validation, and UI validation
2. **Provide clear error messages**: Help users understand what went wrong and how to fix it
3. **Offer solutions**: When a project doesn't exist, offer to create it
4. **Use transactions**: Ensure atomicity when creating projects and related resources
5. **Test constraints**: Verify that constraints work as expected in tests

## Migration Guide

For existing databases without constraints:

1. **Backup your database** before applying migrations
2. **Check for orphaned data**: Find resources referencing non-existent projects
3. **Clean up orphaned data** or create missing projects
4. **Apply foreign key constraints** using migrations
5. **Enable foreign key enforcement** in your database connection

```sql
-- Find orphaned agents
SELECT a.* FROM agent a
LEFT JOIN projects p
  ON a.tenant_id = p.tenant_id
  AND a.project_id = p.id
WHERE p.id IS NULL;
```

## Benefits

* **Data Integrity**: Prevents orphaned data and maintains consistency
* **Clear User Experience**: Users are guided to create projects when needed
* **Easier Debugging**: Constraint violations are caught early
* **Simplified Cleanup**: Cascading deletes remove all related data
* **Better Documentation**: Constraints document relationships in the schema


# Spans and Traces
URL: /community/contributing/spans

OpenTelemetry spans for distributed tracing and observability in the Inkeep Agent Framework

***

title: Spans and Traces
description: OpenTelemetry spans for distributed tracing and observability in the Inkeep Agent Framework
icon: "LuBug"
-------------

## Overview

The Inkeep Agent Framework uses OpenTelemetry for distributed tracing and observability. Spans provide detailed visibility into the execution flow of agents, context resolution, tool execution, and other framework operations.

## Getting Started with Spans

### 1. Import Required Dependencies

```typescript
import { SpanStatusCode, type Span } from "@opentelemetry/api";
import { getTracer, setSpanWithError } from "../tracer";
```

### 2. Get the Tracer

```typescript
// Use the centralized tracer utility
const tracer = getTracer("your-service-name");
```

## Creating and Using Spans

```typescript
return tracer.startActiveSpan(
  "context.resolve",
  {
    attributes: {
      "context.config_id": contextConfig.id,
      "context.trigger_event": options.triggerEvent,
    },
  },
  async (span: Span) => {
    try {
      // Your operation logic here
      return result;
    } catch (error) {
      // Use setSpanWithError for consistent error handling
      setSpanWithError(span, error);
      throw error;
    }
  }
);
```

## Setting Span Attributes

### Basic Attributes

```typescript
span.setAttributes({
  "user.id": userId,
  "request.method": "POST",
});
```

## Adding Events to Spans

### Recording Important Milestones

```typescript
// Add events for significant operations
span.addEvent("context.fetch_started", {
  definitionId: definition.id,
  url: definition.fetchConfig.url,
});
```

### Error Events

```typescript
span.addEvent("error.validation_failed", {
  definitionId: definition.id,
  error_type: "json_schema_validation",
  error_details: errorMessage,
});
```

## Error Handling and Status

### Using setSpanWithError Utility

The framework provides a convenient `setSpanWithError` utility function that handles error recording and status setting:

```typescript
try {
  // Your operation
} catch (error) {
  // Use the setSpanWithError utility for consistent error handling
  setSpanWithError(span, error);
  throw error;
}
```

## Best Practices

### 1. Consistent Naming Convention

The span naming convention follows a hierarchical structure that mirrors your code organization.

```typescript
// Format: 'class.function'
// Use descriptive span names that follow a hierarchical structure

// Agent operations
"agent.generate";
"agent.tool_execute";
"agent.transfer";

// Context operations
"context.resolve";
"context.fetch";
```

#### Naming Rules

1. **Class First**: Start with the class/module name (e.g., `agent`, `context`, `tool`)
2. **Function Second**: Follow with the specific function/method (e.g., `generate`, `resolve`)
3. **Use Underscores**: For multi-word functions, use underscores (e.g., `tool_execute`, `cache_lookup`)
4. **Consistent Casing**: Use lowercase with underscores for consistency

## Configuration and Setup

### Environment Variables

```bash
# OpenTelemetry configuration
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4317
```

### Instrumentation Setup

The framework automatically sets up OpenTelemetry instrumentation in `src/instrumentation.ts`:

## Examples in the Codebase

### Agent Operations

See `src/agents/Agent.ts` for span usage in agent generation and tool execution.

**Example from Agent.ts:**

```typescript
// Class: Agent
// Function: generate
return tracer.startActiveSpan(
  "agent.generate",
  {
    attributes: {
      "agent.id": this.id,
      "agent.name": this.name,
    },
  },
  async (span: Span) => {
    // ... implementation
  }
);
```

## Summary

Spans provide powerful observability into your Inkeep Agent Framework operations. By following these patterns:

1. **Use `getTracer()`** for consistent tracing
2. **Use consistent naming**
3. **Set meaningful attributes** for searchability
4. **Handle errors properly** using `setSpanWithError` for consistent error handling
5. **Use `startActiveSpan`** for automatic lifecycle management

This will give you comprehensive visibility into your agent operations, making debugging and performance optimization much easier.


# Exa
URL: /connecting-your-data/3rd-party-tools/exa

Exa is a data scraping tool that allows you to scrape data from websites.

***

title: Exa
description: Exa is a data scraping tool that allows you to scrape data from websites.
--------------------------------------------------------------------------------------

Exa is a data scraping tool that allows you to scrape data from websites.

## Using as a custom tool

Install the [exa-js](https://github.com/exa-labs/exa-js) SDK

```typescript
import Exa from 'exa-js';
import { agent, subAgent } from "@inkeep/agents-sdk";

const exaAgent = subAgent({
  id: 'exa-agent',
  tenantId,
  name: 'exa',
  description:
    'This agent is used to search and retrieve information from the web using Exa',
  prompt: 'Use the tools at your disposal to search and retrieve information from the web.',
  tools: {
    web_search_exa: tool({
      name: 'web_search_exa',
      description: 'Search the web and retrieve relevant results with optional content and highlights',
      parameters: {
        type: 'object',
        properties: {
          query: {
            type: 'string',
            description: 'The search query string'
          },
          numResults: {
            type: 'number',
            description: 'Number of search results to return (default: 10)',
            optional: true
          },
          includeDomains: {
            type: 'array',
            items: { type: 'string' },
            description: 'List of domains to include in the search',
            optional: true
          },
          excludeDomains: {
            type: 'array',
            items: { type: 'string' },
            description: 'List of domains to exclude from the search',
            optional: true
          },
          includeContent: {
            type: 'boolean',
            description: 'Whether to include the full text content of results',
            optional: true
          },
          includeHighlights: {
            type: 'boolean',
            description: 'Whether to include relevant highlights from the content',
            optional: true
          }
        },
        required: ['query']
      },
      execute: async ({ query, numResults = 10, includeDomains, excludeDomains, includeContent = false, includeHighlights = false }) => {
        try {
          const exa = new Exa(process.env.EXA_API_KEY);
          
          if (includeContent || includeHighlights) {
            const results = await exa.searchAndContents(query, {
              numResults,
              includeDomains,
              excludeDomains,
              text: includeContent,
              highlights: includeHighlights
            });
            return results;
          } else {
            const results = await exa.search(query, {
              numResults,
              includeDomains,
              excludeDomains
            });
            return results;
          }
        } catch (error) {
          console.error('Error executing Exa search:', error);
          throw new Error(`Failed to execute Exa search: ${error.message}`);
        }
      }
    })
  }
});
```

## Using as an MCP tool

Get your API key
Before you begin, you’ll need an Exa API key: [https://dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys)

Connect directly to Exa’s hosted MCP server using this URL:

[https://mcp.exa.ai/mcp?exaApiKey=your-exa-api-key](https://mcp.exa.ai/mcp?exaApiKey=your-exa-api-key)

```typescript
import { mcpTool } from "@inkeep/agents-sdk";

const exaTool = mcpTool({
  id: "exa-tool",  
  name: "exa",
  description: "Exa MCP tool for data scraping",
  serverUrl: "https://mcp.exa.ai/mcp?exaApiKey=your-exa-api-key"
});
```

This will give you access to the following tools:

web\_search\_exa
company\_research\_exa
crawling\_exa
linkedin\_search\_exa
deep\_researcher\_start
deep\_researcher\_check


# Datadog
URL: /self-hosting/add-other-services/datadog-apm

Add Datadog APM to your Inkeep Agent Framework services

***

title: Datadog
sidebarTitle: Add Datadog
description: Add Datadog APM to your Inkeep Agent Framework services
keywords: Datadog, monitoring, distributed tracing
icon: "brand/DatadogIcon"
-------------------------

## Overview

Learn how to add Datadog APM to your Inkeep Agent Framework services.

## Step 1: Install Datadog APM

From the root of your workspace, run the following command:

```bash
pnpm install dd-trace
```

## Step 2: Set up tracer.ts

In `apps/run-api` and `apps/manage-api` create a new file called `tracer.ts` and add the following code:

```typescript
import tracer from "dd-trace";
tracer.init(); // initialized in a different file to avoid hoisting.
export default tracer;
```

In `apps/run-api/src/index.ts` and `apps/manage-api/src/index.ts` add the following code to the top of the file before all other imports:

```typescript
import "./tracer";
```

## Additional Resources

For more information on how to configure APM, you can consult the official Datadog Node.js [documentation](https://app.datadoghq.com/apm/service-setup?architecture=host-based\&framework=typescript\&language=node\&product=apm).


# Sentry
URL: /self-hosting/add-other-services/sentry

Add Sentry monitoring to your agent services

***

title: Sentry
sidebarTitle: Add Sentry
description: Add Sentry monitoring to your agent services
keywords: Sentry, error tracking, monitoring, distributed tracing
icon: "brand/SentryIcon"
------------------------

## Overview

Learn how to add Sentry monitoring to your Inkeep Agent Framework services.

## Step 1: Install Sentry

```bash
pnpm install @sentry/node
```

## Step 2: Update your `.env` file

Add your Sentry DSN to the `.env` file in the root of your workspace.

```bash
SENTRY_DSN=https://<your-sentry-dsn>@sentry.io/<your-sentry-project>
```

## Step 3: Configure Sentry

In `apps/run-api` and `apps/manage-api` create a new file called `sentry.ts` and add the following code:

```typescript
import * as Sentry from "@sentry/node";

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  sampleRate: 1.0,
  tracesSampleRate: 1.0,
});
```

In `apps/run-api/src/index.ts` and `apps/manage-api/src/index.ts` add the following code to the top of the file before all other imports:

```typescript
import "./sentry";
```

## Forward Error Logs to Sentry

You can use [pino-sentry-transport](https://github.com/tomer-yechiel/pino-sentry-transport) to forward error logs to Sentry.

### Step 1: Install pino-sentry-transport

```bash
pnpm install pino-sentry-transport
```

### Step 2: Configure pino-sentry-transport

Add the following code to the top of your `apps/run-api/src/index.ts` file:

```typescript
logger = getLogger('agents-run-api');
logger.addTransport({
  target: 'pino-sentry-transport',
  options: {
    sentry: {
      dsn: process.env.SENTRY_DSN,
    },
  },
});
```

Add the following code to the top of your `apps/manage-api/src/index.ts` file:

```typescript
logger = getLogger('agents-manage-api');
logger.addTransport({
  target: 'pino-sentry-transport',
  options: {
    sentry: {
      dsn: process.env.SENTRY_DSN,
    },
  },
});
```

## Additional Resources

For more information on how to configure Sentry, you can consult the official Sentry Node.js [documentation](https://docs.sentry.io/platforms/node/).


# Chat Button
URL: /talk-to-your-agents/javascript/chat-button

Learn how to use the chat button component in JavaScript

***

title: Chat Button
description: Learn how to use the chat button component in JavaScript
icon: "LuMessageCircle"
-----------------------

The chat button component is a simple way to trigger the Inkeep chat bubble in your JavaScript application.

## Quick Start

<Steps>
  <Step>
    Add the below `<script>` tag to the `<head>` or `<body>` of your website.

    ```html
    <script
        type="module"
        src="https://cdn.jsdelivr.net/npm/@inkeep/agents-ui-js@0.15/dist/embed.js"
        defer
    ></script>
    ```
  </Step>

  <Step>
    Insert the Chat Button by using the `Inkeep.ChatButton()` function.

    ```ts
    const config: InkeepChatButtonProps = {
      aiChatSettings: {
        agentUrl: "https://your-api.example.com/api/chat",
        apiKey: process.env.INKEEP_API_KEY, // Your API key
      },
    };

    const chatButton = Inkeep.ChatButton(config);
    ```
  </Step>
</Steps>

## Config

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepChatButtonProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### Open Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="OpenSettingsChatButton" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />


# Custom Trigger
URL: /talk-to-your-agents/javascript/custom-trigger

Create custom UI elements to trigger Inkeep modals with complete control over appearance and behavior in JavaScript.

***

title: Custom Trigger
description: Create custom UI elements to trigger Inkeep modals with complete control over appearance and behavior in JavaScript.
icon: "LuMousePointerClick"
---------------------------

## Overview

Custom triggers give you complete control over how users open Inkeep modals in your JavaScript application. Instead of using pre-built widgets like `Inkeep.ChatButton()`, you can create your own UI elements that match your design system while maintaining full functionality.

## Quick Start

<Steps>
  <Step>
    Add the below `<script>` tag to the `<head>` or `<body>` of your website.

    ```html
    <script
        type="module"
        src="https://cdn.jsdelivr.net/npm/@inkeep/agents-ui-js@0.15/dist/embed.js"
        defer

    > </script>

    ```
  </Step>

  <Step>
    Insert the ModalChat widget by using the `Inkeep.ModalChat()` function.

    ```js
    const config = {
      baseSettings: {
        apiKey: "YOUR_API_KEY",
      },
      aiChatSettings: {
        aiAssistantName: "Keepie",
      },
      openSettings: {
        onOpenChange: handleOpenChange,
      },
    };

    // Initialize modal chat
    const modalChat = Inkeep.ModalChat(config);

    function handleOpenChange(newOpen) {
      modalChat.update({ openSettings: { isOpen: newOpen } });
    }

    // trigger
    document.querySelector("#chat-button").addEventListener("click", () => {
      modalChat.update({ openSettings: { isOpen: true } });
    });

    // Access chat methods
    modalChat.clearChat();
    ```
  </Step>
</Steps>

## Config

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepModalChatProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />

### Open Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="OpenSettingsModal" />


# Embedded Chat
URL: /talk-to-your-agents/javascript/embedded-chat

Integrate Inkeep's embedded chat component directly into your React application for inline agent conversations.

***

title: Embedded Chat
description: Integrate Inkeep's embedded chat component directly into your React application for inline agent conversations.
icon: "LuMonitor"
-----------------

The EmbeddedChat widget provides a fully embedded chat interface that you can integrate directly into your JavaScript application's layout. Unlike modal or sidebar implementations, the embedded chat becomes part of your page structure, perfect for dedicated support pages, dashboards, or help centers.

## Quick Start

<Steps>
  <Step>
    Add the below `<script>` tag to the `<head>` or `<body>` of your website.

    ```html
    <script
        type="module"
        src="https://cdn.jsdelivr.net/npm/@inkeep/agents-ui-js@0.15/dist/embed.js"
        defer

    > </script>
    ```
  </Step>

  <Step>
    Define an element in your page that will be the "container" for the embedded chat.

    ```html
    <div style="display: flex; align-items: center; justify-content: center; height: calc(100vh - 16px);">
      <div style="max-height: 600px; height: 100%;">
        <div id="ikp-embedded-chat-target"></div>
      </div>
    </div>
    ```
  </Step>

  <Step>
    Insert the EmbeddedChat widget by using the `Inkeep.EmbeddedChat()` function.

    ```ts
    <script type="module">
      const config = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.INKEEP_API_KEY, // Your API key
        },
      };

      // Initialize the widget
      const widget = Inkeep.EmbeddedChat("#ikp-embedded-chat-target", config);
    </script>
    ```
  </Step>
</Steps>

## Config

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepEmbeddedChatProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />


# Add Sidebar Chat to React
URL: /talk-to-your-agents/javascript/side-bar-chat

Integrate Inkeep's sidebar chat component into your React application for seamless agent conversations.

***

title: Add Sidebar Chat to React
sidebarTitle: Sidebar Chat
description: Integrate Inkeep's sidebar chat component into your React application for seamless agent conversations.
icon: "LuPanelLeft"
-------------------

The SidebarChat widget provides a slide-out panel interface for conversing with your agents. It can be positioned on either side of your application and supports both manual triggering and automatic element triggers.

## Quick Start

<Steps>
  <Step>
    Add the below `<script>` tag to the `<head>` or `<body>` of your website.

    ```html
    <script
        type="module"
        src="https://cdn.jsdelivr.net/npm/@inkeep/agents-ui-js@0.15/dist/embed.js"
        defer

    > </script>

    ```
  </Step>

  <Step>
    Define an element in your page that will be the "container" for the embedded chat.

    ```html
    <div style="display: flex; flex-direction: row; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow: hidden;">
      <div style="display: flex; flex-direction: column; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow-y: auto; flex: 1;">
        <!-- your app content here -->
      </div>
      <!-- the sidebar chat will be inserted into this div -->
      <div id="sidebar-chat"></div>
    </div>
    ```
  </Step>

  <Step>
    Add a button element that will trigger the sidebar chat and give it the data attribute data-inkeep-sidebar-chat-trigger. You can also use your own custom attribute if you prefer, just be sure to pass it to the triggerSelector prop.

    ```html
    <div style="display: flex; flex-direction: row; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow: hidden;">
      <div style="display: flex; flex-direction: column; height: 100vh; max-height: 100vh; padding: 0; margin: 0; overflow-y: auto; flex: 1;">
        <!-- your app content here -->
        <button data-inkeep-sidebar-chat-trigger="">Toggle Sidebar Chat</button>
      </div>
      <!-- the sidebar chat will be inserted into this div -->
      <div id="ikp-sidebar-chat-target"></div>
    </div>
    ```
  </Step>

  <Step>
    Insert the EmbeddedChat widget by using the `Inkeep.EmbeddedChat()` function.

    ```ts
    <script type="module">
      const config = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.INKEEP_API_KEY, // Your API key
        },
      };

      // Initialize the widget
      const widget = Inkeep.SidebarChat("#ikp-sidebar-chat-target", config);
    </script>
    ```
  </Step>
</Steps>

## Config

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepEmbeddedChatProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />

### Open Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="OpenSettingsSidebar" />


# Chat Button
URL: /talk-to-your-agents/react/chat-button

Learn how to use the chat button component in React

***

title: Chat Button
description: Learn how to use the chat button component in React
icon: "LuMessageCircle"
-----------------------

The chat button component is a simple way to trigger the Inkeep chat bubble.

## Installation

<CodeGroup>
  ```bash title="npm"
  npm install @inkeep/agents-ui
  ```

  ```bash title="yarn"
  yarn add @inkeep/agents-ui
  ```

  ```bash title="pnpm"
  pnpm add @inkeep/agents-ui
  ```
</CodeGroup>

## Quick Start

<Tabs>
  <Tab title="Production">
    Use an API key for secure authentication in production:

    ```tsx
    import { InkeepChatButton, type InkeepChatButtonProps } from "@inkeep/agents-ui";

    const buttonProps: InkeepChatButtonProps = {
      aiChatSettings: {
        agentUrl: "https://your-api.example.com/api/chat",
        apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
      },
    };

    const ChatButton = () => {
      return <InkeepChatButton {...buttonProps} />;
    };
    ```

    **To get an API key:**

    1. Open the Visual Builder Dashboard
    2. Navigate to your Project → **API Keys**
    3. Click **Create New Key** and select your agent
    4. Copy the key (shown once) and store it in your environment variables
  </Tab>

  <Tab title="Development">
    For local development, use headers with your agent IDs:

    ```tsx
    import {
      InkeepChatButton,
      type InkeepChatButtonProps,
    } from "@inkeep/agents-ui";

    const buttonProps: InkeepChatButtonProps = {
      aiChatSettings: {
        agentUrl: "http://localhost:3003/api/chat",
        headers: {
          "x-inkeep-tenant-id": "your-tenant-id",
          "x-inkeep-project-id": "your-project-id",
          "x-inkeep-agent-id": "your-agent-id",
        },
      },
    };

    const ChatButton = () => {
      return <InkeepChatButton {...buttonProps} />;
    };
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Props

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepChatButtonProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### Open Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="OpenSettingsChatButton" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />


# Custom Trigger
URL: /talk-to-your-agents/react/custom-trigger

Create custom UI elements to trigger Inkeep modals with complete control over appearance and behavior.

***

title: Custom Trigger
description: Create custom UI elements to trigger Inkeep modals with complete control over appearance and behavior.
icon: "LuMousePointerClick"
---------------------------

## Overview

Custom triggers give you complete control over how users open Inkeep modals in your React application. Instead of using pre-built components like `InkeepChatButton`, you can create your own UI elements that match your design system while maintaining full functionality.

## Installation

<CodeGroup>
  ```bash title="npm"
  npm install @inkeep/agents-ui
  ```

  ```bash title="yarn"
  yarn add @inkeep/agents-ui
  ```

  ```bash title="pnpm"
  pnpm add @inkeep/agents-ui
  ```
</CodeGroup>

## Quick Start

<Tabs>
  <Tab title="Production">
    Use an API key for secure authentication in production:

    ```tsx
    import { useState } from "react";
    import { InkeepModalChat, type InkeepModalChatProps } from "@inkeep/agents-ui";

    function App() {
      const [isModalOpen, setIsModalOpen] = useState(false);

      const modalProps: InkeepModalChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
        openSettings: {
          isOpen: isModalOpen,
          onOpenChange: setIsModalOpen,
        },
      };

      return (
        <>
          <button onClick={() => setIsModalOpen(true)}>
            Open Inkeep Assistant
          </button>

          <InkeepModalChat {...modalProps} />
        </>
      );
    }
    ```

    **To get an API key:**

    1. Open the Visual Builder Dashboard
    2. Navigate to your Project → **API Keys**
    3. Click **Create New Key** and select your agent
    4. Copy the key (shown once) and store it in your environment variables
  </Tab>

  <Tab title="Development">
    For local development, use headers with your agent IDs:

    ```tsx
    import { useState } from "react";
    import {
      InkeepModalChat,
      type InkeepModalChatProps,
    } from "@inkeep/cxkit-react";

    function App() {
      const [isModalOpen, setIsModalOpen] = useState(false);

      const modalProps: InkeepModalChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3003/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
        openSettings: {
          isOpen: isModalOpen,
          onOpenChange: setIsModalOpen,
        },
      };

      return (
        <>
          <button onClick={() => setIsModalOpen(true)}>
            Open Inkeep Assistant
          </button>

          <InkeepModalChat {...modalProps} />
        </>
      );
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Props

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepModalChatProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />

### Open Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="OpenSettingsModal" />


# Embedded Chat
URL: /talk-to-your-agents/react/embedded-chat

Integrate Inkeep's embedded chat component directly into your React application for inline agent conversations.

***

title: Embedded Chat
description: Integrate Inkeep's embedded chat component directly into your React application for inline agent conversations.
icon: "LuMonitor"
-----------------

The InkeepEmbeddedChat component provides a fully embedded chat interface that you can integrate directly into your React application's layout. Unlike modal or sidebar implementations, the embedded chat becomes part of your page structure, perfect for dedicated support pages, dashboards, or help centers.

## Installation

<CodeGroup>
  ```bash title="npm"
  npm install @inkeep/agents-ui
  ```

  ```bash title="yarn"
  yarn add @inkeep/agents-ui
  ```

  ```bash title="pnpm"
  pnpm add @inkeep/agents-ui
  ```
</CodeGroup>

## Quick Start

<Tabs>
  <Tab title="Production">
    Use an API key for secure authentication in production:

    ```tsx
    import { InkeepEmbeddedChat, type InkeepEmbeddedChatProps } from "@inkeep/agents-ui";

    export default function App() {
      const embeddedChatProps: InkeepEmbeddedChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
      };

      return <InkeepEmbeddedChat {...embeddedChatProps} />;
    }
    ```

    **To get an API key:**

    1. Open the Visual Builder Dashboard
    2. Navigate to your Project → **API Keys**
    3. Click **Create New Key** and select your agent
    4. Copy the key (shown once) and store it in your environment variables
  </Tab>

  <Tab title="Development">
    For local development, use headers with your agent IDs:

    ```tsx
    import {
      InkeepEmbeddedChat,
      type InkeepEmbeddedChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const embeddedChatProps: InkeepEmbeddedChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3003/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
      };

      return <InkeepEmbeddedChat {...embeddedChatProps} />;
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Props

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepEmbeddedChatProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />


# Add Sidebar Chat to React
URL: /talk-to-your-agents/react/side-bar-chat

Integrate Inkeep's sidebar chat component into your React application for seamless agent conversations.

***

title: Add Sidebar Chat to React
sidebarTitle: Sidebar Chat
description: Integrate Inkeep's sidebar chat component into your React application for seamless agent conversations.
icon: "LuPanelLeft"
-------------------

The InkeepSidebarChat component provides a slide-out panel interface for conversing with your agents. It can be positioned on either side of your application and supports both manual triggering and automatic element triggers.

## Installation

<CodeGroup>
  ```bash title="npm"
  npm install @inkeep/agents-ui
  ```

  ```bash title="yarn"
  yarn add @inkeep/agents-ui
  ```

  ```bash title="pnpm"
  pnpm add @inkeep/agents-ui
  ```
</CodeGroup>

## Quick Start

<Tabs>
  <Tab title="Production">
    Use an API key for secure authentication in production:

    ### Trigger through React state

    ```tsx
    import { useState } from "react";
    import { InkeepSidebarChat, type InkeepSidebarChatProps } from "@inkeep/agents-ui";

    export default function App() {
      const [isOpen, setIsOpen] = useState(false);

      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
        position: "right",
        openSettings: {
          isOpen: isOpen,
          onOpenChange: setIsOpen,
        },
      };

      return (
        <div>
          <button onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? "Close" : "Open"} Sidebar Chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    ### Trigger through data attributes

    ```tsx
    import {
      InkeepSidebarChat,
      type InkeepSidebarChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "https://your-api.example.com/api/chat",
          apiKey: process.env.REACT_APP_INKEEP_API_KEY, // Your API key
        },
        position: "right",
      };

      return (
        <div>
          <button data-inkeep-sidebar-chat-trigger>
            Click here to open sidebar chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    **To get an API key:**

    1. Open the Visual Builder Dashboard
    2. Navigate to your Project → **API Keys**
    3. Click **Create New Key** and select your agent
    4. Copy the key (shown once) and store it in your environment variables
  </Tab>

  <Tab title="Development">
    For local development, use headers with your agent IDs:

    ### Trigger through React state

    ```tsx
    import { useState } from "react";
    import {
      InkeepSidebarChat,
      type InkeepSidebarChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const [isOpen, setIsOpen] = useState(false);

      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3003/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
        position: "right",
        openSettings: {
          isOpen: isOpen,
          onOpenChange: setIsOpen,
        },
      };

      return (
        <div>
          <button onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? "Close" : "Open"} Sidebar Chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    ### Trigger through data attributes

    ```tsx
    import {
      InkeepSidebarChat,
      type InkeepSidebarChatProps,
    } from "@inkeep/agents-ui";

    export default function App() {
      const sidebarChatProps: InkeepSidebarChatProps = {
        aiChatSettings: {
          agentUrl: "http://localhost:3003/api/chat",
          headers: {
            "x-inkeep-tenant-id": "your-tenant-id",
            "x-inkeep-project-id": "your-project-id",
            "x-inkeep-agent-id": "your-agent-id",
          },
        },
        position: "right",
      };

      return (
        <div>
          <button data-inkeep-sidebar-chat-trigger>
            Click here to open sidebar chat
          </button>

          <InkeepSidebarChat {...sidebarChatProps} />
        </div>
      );
    }
    ```

    **Note:** Run your API server with `ENVIRONMENT=development` to bypass authentication.
  </Tab>
</Tabs>

## Configuration Options

### Required Props

| Property                  | Type   | Description                                         |
| ------------------------- | ------ | --------------------------------------------------- |
| `aiChatSettings`          | object | Configuration for the AI chat connection            |
| `aiChatSettings.agentUrl` | string | The URL of your agent endpoint                      |
| `aiChatSettings.headers`  | object | Headers for authentication and agent identification |

## Props

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepSidebarChatProps" />

### Base Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepBaseSettings" />

### AI Chat Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="InkeepAIChatSettings" />

### Open Settings

<AutoTypeTable path="./content/docs/talk-to-your-agents/types.ts" name="OpenSettingsSidebar" />


# Build chat UIs with Vercel AI Elements
URL: /talk-to-your-agents/vercel-ai-sdk/ai-elements

Use Vercel AI Elements to quickly assemble production-ready chat interfaces that connect to your Inkeep agent.

***

title: Build chat UIs with Vercel AI Elements
sidebarTitle: AI Elements
description: Use Vercel AI Elements to quickly assemble production-ready chat interfaces that connect to your Inkeep agent.
icon: LuPackage
keywords: Vercel AI Elements, shadcn ui, chat components, React, agents
-----------------------------------------------------------------------

## Overview

[Vercel AI Elements](https://ai-sdk.dev/elements/overview) is a set of prebuilt, headless-first UI primitives for building AI chat interfaces. Think of it as a `shadcn/ui`-like library of UI components for conversational experiences.

The library works out of the box with Inkeep Agents via the `/chat` [API endpoint](/talk-to-your-agents/api) since it follows the streaming protocol used by AI Elements.

For fully custom `useChat` hooks and lower-level control, see the [useChat guide](/talk-to-your-agents/vercel-ai-sdk/use-chat).

## Using AI Elements

```tsx
import { Conversation, Message, PromptInput, Actions } from '@ai-sdk/react-elements';
import { useChat } from '@ai-sdk/react';

export default function ChatWithElements() {
  const { messages, sendMessage } = useChat({
    transport: new DefaultChatTransport({
      api: "${process.env.NEXT_PUBLIC_INKEEP_AGENTS_RUN_API_URL}/api/chat", // 
      headers: {
        "x-inkeep-tenant-id": "default",
        "x-inkeep-project-id": "weather-project",
        "x-inkeep-agent-id": "weather-agent",
      },
    })
  });

  return (
    <Conversation messages={messages}>
      {messages.map(message => (
        <Message key={message.id} message={message}>
          <Actions message={message} />
        </Message>
      ))}
      <PromptInput onSubmit={sendMessage} />
    </Conversation>
  );
}
```

## Install (one-liner)

```sh
npx ai-elements@latest
```

This CLI adds selected components to your project under `@/components/ai-elements/` and wires up any required shadcn/ui primitives.

## Component quick reference

* **Core chat**: `Conversation`, `Message`, `PromptInput`, `Response`, `Actions`, `Sources`
* **Reasoning & tools**: `Reasoning`, `Tool`, `Task`, `InlineCitation`, `Context`
* **Workflow (React Flow)**: `Canvas`, `Node`, `Edge`, `Connection`, `Controls`, `Panel`, `Toolbar`
* **Coding artifacts**: `CodeBlock`, `Artifact`, `WebPreview`, `Image`
* **UX extras**: `Suggestion`, `Branch`, `Loader`, `OpenIn`

See the [AI Elements](https://ai-sdk.dev/elements/overview) site for detailed props and examples.


# Use Inkeep agents with Vercel AI SDK
URL: /talk-to-your-agents/vercel-ai-sdk/inkeep-provider

A custom AI SDK provider that lets you use Inkeep agents with generateText, streamText, and other AI SDK functions.

***

title: Use Inkeep agents with Vercel AI SDK
sidebarTitle: Inkeep Provider
description: A custom AI SDK provider that lets you use Inkeep agents with generateText, streamText, and other AI SDK functions.
icon: LuZap
keywords: Vercel AI SDK, provider, generateText, streamText, tool calling, agents
---------------------------------------------------------------------------------

## Overview

The `@inkeep/ai-sdk-provider` package is a custom AI SDK provider that exposes Inkeep agents through the Vercel AI SDK. This lets you call your agents with `generateText()` and `streamText()`.

## Installation

```bash
npm install @inkeep/ai-sdk-provider ai
```

## Basic Usage

### Text Generation

```typescript
import { generateText } from 'ai';
import { createInkeep } from '@inkeep/ai-sdk-provider';

const inkeep = createInkeep({
  baseURL: process.env.INKEEP_AGENTS_RUN_API_URL, // Required
  apiKey: '<your-agent-api-key>', // Created in the Agents Dashboard
  headers: { // Optional if you are developing locally and don't want to use an api key
    'x-inkeep-agent-id': 'your-agent-id',
    'x-inkeep-tenant-id': 'your-tenant-id',
    'x-inkeep-project-id': 'your-project-id',
  },
});

const { text } = await generateText({
  model: inkeep(),
  prompt: 'What is the weather in NYC?',
});

console.log(text);
```

### Streaming Responses

```typescript
import { streamText } from 'ai';
import { createInkeep } from '@inkeep/ai-sdk-provider';

const inkeep = createInkeep({
  baseURL: process.env.INKEEP_AGENTS_RUN_API_URL,
  apiKey: '<your-agent-api-key>', // The agent ID is encoded in the API key
  headers: {
    'x-emit-operations': 'true', // Enable tool event streaming
  },
});

const result = await streamText({
  model: inkeep(),
  prompt: 'Plan an event in NYC',
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Configuration

### Provider Settings

```typescript
createInkeep({
  baseURL: string,        // Required. Your agents-run-api URL
  apiKey?: string,        // Optional. Bearer token for authentication
  headers?: Record<string, string>, // Optional. Additional headers
})
```

### Provider Options

Pass options when creating a provider instance:

```typescript
const provider = inkeep({
  conversationId: 'conv-456',
  headers: { 'user-id': 'user-789' },
});
```

## Tool Call Observability

To receive tool call and result events in your stream, include the `x-emit-operations` header:

```typescript
const inkeep = createInkeep({
  baseURL: process.env.INKEEP_AGENTS_RUN_API_URL,
  apiKey: '<your-agent-api-key>', // The agent ID is encoded in the API key
  headers: {
    'x-emit-operations': 'true',
  },
});

const result = await streamText({
  model: inkeep(),
  prompt: 'Search for recent papers on AI',
});

for await (const event of result.fullStream) {
  switch (event.type) {
    case 'tool-call':
      console.log(`Calling: ${event.toolName}`);
      break;
    case 'tool-result':
      console.log(`Result: ${event.toolName}`);
      break;
  }
}
```

### Supported Stream Events

**Text events** (always emitted):

* `text-start`, `text-delta`, `text-end`

**Tool events** (requires `x-emit-operations: true`):

* `tool-call` - Tool invocations (including agent transfers and delegations)
* `tool-result` - Tool results (including delegation returns)

**Control events** (always emitted):

* `finish` - Stream completion with usage stats
* `error` - Stream errors

## Next Steps

<Cards>
  <Card title="useChat Hook" icon="LuCode" href="/talk-to-your-agents/vercel-ai-sdk/use-chat">
    Build React chat interfaces with streaming responses.
  </Card>

  <Card title="AI Elements" icon="LuPackage" href="/talk-to-your-agents/vercel-ai-sdk/ai-elements">
    Use prebuilt UI components for chat experiences.
  </Card>

  <Card title="Chat API" icon="LuNetwork" href="/talk-to-your-agents/chat-api">
    Learn about the underlying HTTP API endpoint.
  </Card>
</Cards>


# Create custom UIs using the Vercel AI SDK
URL: /talk-to-your-agents/vercel-ai-sdk/use-chat

Use the Vercel AI SDK's useChat hook to build React chat interfaces that stream responses from your agent.

***

title: Create custom UIs using the Vercel AI SDK
sidebarTitle: useChat hook
description: Use the Vercel AI SDK's useChat hook to build React chat interfaces that stream responses from your agent.
icon: LuCode
keywords: Vercel AI SDK, useChat, React, streaming, chat interface, agents
--------------------------------------------------------------------------

## Overview

Agents built with Inkeep have an `/api/chat` [API endpoint](/talk-to-your-agents/chat-api) that is compatible with Vercel AI SDK's streaming protocol, so it works out of the box with Vercel's AI SDK ecosystem.

To build totally custom UIs, you have two options in the AI SDK ecosystem:

* Use `useChat` hook to build custom UIs in React, Svelte, Vue.js, and Angular. (**← this guide**)
* Use the [AI Elements](/talk-to-your-agents/vercel-ai-sdk/ai-elements) library for a shadcn-like chat primitives.

## Using `useChat`

Install the Vercel AI SDK in your React application:

```bash
npm install ai @ai-sdk/react
```

## Basic Configuration

Here's a minimal example of using `useChat` with your agent:

```tsx
"use client";

import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport } from "ai";
import { useState } from "react";

export default function Page() {
  const { messages, sendMessage } = useChat({
    transport: new DefaultChatTransport({
      api: "${process.env.NEXT_PUBLIC_INKEEP_AGENTS_RUN_API_URL}/api/chat", // 
      headers: {
        "x-inkeep-tenant-id": "default",
        "x-inkeep-project-id": "activities-planner",
        "x-inkeep-agent-id": "activities-planner",
      },
    }),
  });
  const [input, setInput] = useState("");

  return (
    <div className="max-w-2xl mx-auto p-4">
      <div className="space-y-4 mb-4">
        {messages.map((message) => (
          <div key={message.id} className="border rounded p-3">
            <div className="font-semibold mb-2">
              {message.role === "user" ? "👤 User" : "🤖 Assistant"}
            </div>

            <div className="space-y-2">
              {message.parts.map((part, partIndex) => {
                const partKey = `${message.id}-${part.type}-${partIndex}`;

                if (part.type === "text") {
                  return (
                    <div key={partKey} className="whitespace-pre-wrap">
                      {part.text}
                    </div>
                  );
                }
                
                return null;
              })}
            </div>
          </div>
        ))}
      </div>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (input.trim()) {
            sendMessage({ text: input });
            setInput("");
          }
        }}
        className="flex gap-2"
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about weather, request confirmation, or ask for location..."
          className="flex-1 p-2 border rounded"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Send
        </button>
      </form>

      <div className="mt-4 text-sm text-gray-600">
        <p>Try asking:</p>
        <ul className="list-disc list-inside space-y-1">
          <li>"What's the weather in New York?"</li>
          <li>"Can you get my location?"</li>
          <li>"Ask me to confirm something"</li>
        </ul>
      </div>
    </div>
  );
}
```

## Configuration Options

### API Endpoint

The `api` parameter should point to your Run API's chat endpoint:

* **Local development**: `http://localhost:3003/api/chat`
* **Production**: `https://your-run-api-domain.com/api/chat`

<>
  ## Authentication

  Choose the authentication method:

  <Tabs>
    <Tab title="Using an API Key">
      **Create an API Key:**

      1. Open the Visual Builder Dashboard
      2. Go to your Project → **API Keys**
      3. Click **Create**, select the target agent
      4. Copy the API key (it will be shown once) and store it securely

      **Request Header:**

      ```http
      Authorization: Bearer <api_key>
      ```
    </Tab>

    <Tab title="Without API key">
      When running the API server locally with `pnpm dev`, authentication is automatically bypassed. You can use headers in the request instead:

      **Request Headers:**

      ```http
      x-inkeep-tenant-id: <tenant-id>
      x-inkeep-project-id: <project-id>
      x-inkeep-agent-id: <agent-id>
      ```

      <Warning>
        This mode is for development only. Never use in production as it bypasses all security checks.
      </Warning>
    </Tab>
  </Tabs>

  See [Authentication → Run API](/api-reference/authentication/run-api) for more details.
</>

### Optional Configuration

```tsx
const { messages, sendMessage, status } = useChat({
  api: 'http://localhost:3003/api/chat',
  headers: { /* ... */ },

  // Handle completion
  onFinish: (message) => {
    console.log('Agent finished responding:', message);
  },

  // Handle errors
  onError: (error) => {
    console.error('Chat error:', error);
  },
});
```

## Headers

To pass required headers (validated against your Context Config), include them as custom headers:

```tsx
const { messages, sendMessage } = useChat({
  api: 'http://localhost:3003/api/chat',
  headers: {
    'Authorization': `Bearer ${apiKey}`,
    // Custom context headers
    'x-user-id': 'user-123',
    'x-organization-id': 'org-456',
  },
});
```

<Note>
  See [Headers](/typescript-sdk/headers) for details.
</Note>

## Complete Example

Here's a more complete example with conversation management and custom styling:

```tsx
"use client";

import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport } from "ai";
import { useState } from "react";

export default function Page() {
  const { messages, sendMessage } = useChat({
    transport: new DefaultChatTransport({
      api: "{process.env.NEXT_PUBLIC_INKEEP_AGENTS_RUN_API_URL}/api/chat",
      headers: {
        "x-inkeep-tenant-id": "default",
        "x-inkeep-project-id": "activities-planner",
        "x-inkeep-agent-id": "activities-planner",
        tz: "US/Pacific",
      },
    }),
  });
  const [input, setInput] = useState("");

  return (
    <div className="max-w-2xl mx-auto p-4">
      <div className="space-y-4 mb-4">
        {messages.map((message) => (
          <div key={message.id} className="border rounded p-3">
            <div className="font-semibold mb-2">
              {message.role === "user" ? "👤 User" : "🤖 Assistant"}
            </div>

            <div className="space-y-2">
              {message.parts.map((part, partIndex) => {
                const partKey = `${message.id}-${part.type}-${partIndex}`;

                if (part.type === "text") {
                  return (
                    <div key={partKey} className="whitespace-pre-wrap">
                      {part.text}
                    </div>
                  );
                }

                if (part.type?.startsWith("data-")) {
                  return (
                    <div
                      key={partKey}
                      className="bg-blue-50 p-3 rounded border-l-4 border-blue-400"
                    >
                      <div className="font-semibold text-blue-700">
                        Data: {JSON.stringify(part, null, 2)}
                      </div>
                    </div>
                  );
                }
                return null;
              })}
            </div>
          </div>
        ))}
      </div>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (input.trim()) {
            sendMessage({ text: input });
            setInput("");
          }
        }}
        className="flex gap-2"
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about weather, request confirmation, or ask for location..."
          className="flex-1 p-2 border rounded"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Send
        </button>
      </form>

      <div className="mt-4 text-sm text-gray-600">
        <p>Try asking:</p>
        <ul className="list-disc list-inside space-y-1">
          <li>"What's the weather in New York?"</li>
          <li>"Can you get my location?"</li>
          <li>"Ask me to confirm something"</li>
        </ul>
      </div>
    </div>
  );
}
```

## Environment Variables

For production deployments, store configuration in environment variables:

```bash
NEXT_PUBLIC_INKEEP_AGENTS_RUN_API_URL=your_domain_for_run_api
NEXT_PUBLIC_INKEEP_API_KEY=your-api-key
NEXT_PUBLIC_TENANT_ID=your-tenant-id
NEXT_PUBLIC_PROJECT_ID=your-project-id
NEXT_PUBLIC_AGENT_ID=your-agent-id
```

<Note>
  In local development, the Run API runs at `http://localhost:3003`. For production, update this to your deployed Run API URL.
</Note>

## Next Steps

<Cards>
  <Card title="AI Elements" icon="LuPackage" href="/talk-to-your-agents/vercel-ai-sdk/ai-elements">
    Explore Vercel's prebuilt UI components library built on shadcn/ui for rapid development.
  </Card>

  <Card title="React UI Components" icon="LuLayers" href="/talk-to-your-agents/react/chat-button">
    Use prebuilt React components for a complete chat UI experience.
  </Card>

  <Card title="Via API" icon="LuNetwork" href="/talk-to-your-agents/chat-api">
    Learn about the underlying HTTP API and streaming protocol.
  </Card>
</Cards>


# Leverage Composio MCP Server Library
URL: /tutorials/mcp-servers/composio-mcp-servers

Connect to Composio MCP servers for 10,000+ out-of-box MCP servers

***

title: Leverage Composio MCP Server Library
sidebarTitle: Composio
description: Connect to Composio MCP servers for 10,000+ out-of-box MCP servers
icon: "brand/Composio"
----------------------

### Composio

[Composio](https://composio.dev/) offers a platform with access to 10,000+ out-of-box MCP servers for popular services.

#### Quick integration

Follow Composio's MCP Gateway setup to obtain your MCP server URL and credentials. Then register it as a tool in your project:

```typescript
import { mcpTool } from '@inkeep/agents-sdk';

const composioTool = mcpTool({
  id: 'composio-tools',
  name: 'Composio Integration',
  description: 'Access popular SaaS tools via Composio',
  serverUrl: 'YOUR_COMPOSIO_MCP_URL', // From Composio dashboard
});
```

<>
  ### Next steps

  Once you have your server, you can register it in one of:

  <Cards>
    <Card title="The TypeScript SDK" icon="LuCode" href="/typescript-sdk/tools/mcp-tools#step-2-register-the-mcp-server-as-a-tool-in-your-agent">
      Add your MCP server as a tool for your agents in the TypeScript SDK
    </Card>

    <Card title="The Visual Builder" icon="LuPalette" href="/visual-builder/tools/mcp-servers#register-an-mcp-server">
      Add your MCP server as a tool for your agents in the Visual Builder
    </Card>
  </Cards>
</>


# Build Custom MCP Servers
URL: /tutorials/mcp-servers/custom-mcp-servers

Build your own custom MCP servers

***

title: Build Custom MCP Servers
sidebarTitle: Custom
description: Build your own custom MCP servers
icon: "brand/Inkeep"
--------------------

## When to Build Custom MCP Servers

Build custom MCP servers when:

* Native servers don't exist for your specific APIs
* You need custom business logic beyond what existing servers provide
* You have proprietary systems that require custom integration

If pre-built servers meet your needs, consider [Native MCP servers](/tutorials/mcp-servers/native-mcp-servers), [Composio's platform](/tutorials/mcp-servers/composio-mcp-servers), or [Gram](/tutorials/mcp-servers/gram) instead.

## Getting Started

The Quick Start workspace includes a Next.js app in the `apps/mcp/app/` directory that you can use to expose your MCP servers.
Each MCP server you create will be exposed on a separate route on this app.

#### Creating from a template

You can add a custom MCP server template from our [template library](https://github.com/inkeep/agents/tree/main/agents-cookbook/template-mcps) for common use cases using the [CLI](/typescript-sdk/cli-reference#inkeep-add).

```bash
inkeep add --mcp [server-name]
```

This will automatically add a custom MCP server template to your Quick Start workspace. After customizing and deploying it, you can register it.

#### Using Vercel's Template

If you want to create a custom MCP server, you can use Vercel's [Next.js MCP template](https://vercel.com/templates/next.js/model-context-protocol-mcp-with-next-js) as a starting point.

<Steps>
  <Step>
    Create a new directory in your project's `apps/mcp/app/` directory with your desired server name (e.g. `apps/mcp/app/my-email-mcp/mcp`).

    ```bash
    mkdir -p apps/mcp/app/[server-name]/mcp
    ```
  </Step>

  <Step>
    Copy the template route.ts file from the [Vercel MCP template](https://github.com/vercel-labs/mcp-for-next.js/blob/main/app/mcp/route.ts) into `apps/mcp/app/[server-name]/mcp/route.ts`.
  </Step>

  <Step>
    Modify the template route.ts file with your desired tools and resources.
  </Step>

  <Step>
    Set the `basePath` of the `createMcpHandler` to `/[server-name]`.
  </Step>
</Steps>

#### Running locally

```bash
pnpm dev
```

This will start the server on port 3006.

#### Deploying to Vercel

Follow the instructions in [Deploy to Vercel](/self-hosting/vercel#step-9-create-a-vercel-project-for-your-mcp-server-optional).
If you have already deployed to Vercel, you can simply update the deployment by pushing to the same repository.

<Note>
  Enable Fluid compute and set `maxDuration` to 800 in `apps/mcp/app/[server-name]/[transport]/route.ts` if you're on a Pro or Enterprise plan and have long-running operations.
</Note>

<>
  ### Next steps

  Once you have your server, you can register it in one of:

  <Cards>
    <Card title="The TypeScript SDK" icon="LuCode" href="/typescript-sdk/tools/mcp-tools#step-2-register-the-mcp-server-as-a-tool-in-your-agent">
      Add your MCP server as a tool for your agents in the TypeScript SDK
    </Card>

    <Card title="The Visual Builder" icon="LuPalette" href="/visual-builder/tools/mcp-servers#register-an-mcp-server">
      Add your MCP server as a tool for your agents in the Visual Builder
    </Card>
  </Cards>
</>


# Create an OpenAPI-based MCP server
URL: /tutorials/mcp-servers/gram

undefined

***

title: Create an OpenAPI-based MCP server
sidebarTitle: Gram
icon: "brand/Gram"
------------------

## Overview

Gram by Speakeasy turns any OpenAPI specification into a production-ready MCP server. Upload your API spec, and Gram automatically generates tool definitions, handles hosting and authentication, and deploys your server—so you can focus on building powerful agents.

Visit [Gram's documentation](https://www.speakeasy.com/docs/gram/getting-started/openapi) for a complete guide.

### Step 1: Sign up for a Gram account

[Sign up](https://app.getgram.ai/login) for a free Gram account.

### Step 2: Upload your OpenAPI document

<Steps>
  <Step>
    Navigate to **Toolsets** in the Gram dashboard sidebar (under **Create**) and click **Get Started**
  </Step>

  <Step>
    Upload your OpenAPI document, provide a descriptive name, and click **Upload**
  </Step>
</Steps>

Gram extracts URL paths, HTTP methods, request schemas, and operation descriptions from your OpenAPI document to generate tool definitions.

<Note>
  Gram works with partial OpenAPI documents as long as key elements (paths, methods, schemas, descriptions) are present.
</Note>

### Step 3: Ship 🚢

Your MCP server is ready to ship! Open the MCP page, and open your MCP server by clicking it. Click Enable to allow the MCP server to handle requests.

### Step 4: Add authentication (optional)

To add authentication, set the appropriate environment variables. See [Step 3 in the Gram documentation](https://www.speakeasy.com/docs/gram/getting-started/openapi#step-3-set-environment-variables) for details.

<>
  ### Next steps

  Once you have your server, you can register it in one of:

  <Cards>
    <Card title="The TypeScript SDK" icon="LuCode" href="/typescript-sdk/tools/mcp-tools#step-2-register-the-mcp-server-as-a-tool-in-your-agent">
      Add your MCP server as a tool for your agents in the TypeScript SDK
    </Card>

    <Card title="The Visual Builder" icon="LuPalette" href="/visual-builder/tools/mcp-servers#register-an-mcp-server">
      Add your MCP server as a tool for your agents in the Visual Builder
    </Card>
  </Cards>
</>


# Connect to Native MCP Servers
URL: /tutorials/mcp-servers/native-mcp-servers

Connect to Native MCP servers provided by SaaS vendors

***

title: Connect to Native MCP Servers
sidebarTitle: Native
description: Connect to Native MCP servers provided by SaaS vendors
icon: "LuPackageCheck"
----------------------

The fastest way to get started is by connecting to existing MCP servers provided directly by SaaS providers that offer them.

### MCPs with OAuth 2.1/PKCE support

These servers often implement OAuth 2.1 with PKCE for secure authentication that allow for `1-click` authentication without the need for API keys.

<>
  Here's an example list of popular service-maintained MCP Servers that support **1-click** install via the OAuth 2.1/PKCE authentication flow.

  | Name                                                                                                             | URL                                                                  |
  | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
  | [Atlassian (SSE)](https://support.atlassian.com/rovo/docs/getting-started-with-the-atlassian-remote-mcp-server/) | [https://mcp.atlassian.com/v1/sse](https://mcp.atlassian.com/v1/sse) |
  | [Canva](https://www.canva.dev/docs/connect/canva-mcp-server-setup/)                                              | [https://mcp.canva.com/mcp](https://mcp.canva.com/mcp)               |
  | [Hugging Face](https://huggingface.co/mcp)                                                                       | [https://huggingface.co/mcp?login](https://huggingface.co/mcp?login) |
  | [Intercom](https://developers.intercom.com/docs/guides/mcp)                                                      | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp)         |
  | [Linear](https://linear.app/docs/mcp)                                                                            | [https://mcp.linear.app/mcp](https://mcp.linear.app/mcp)             |
  | [Neon](https://neon.com/docs/ai/neon-mcp-server)                                                                 | [https://mcp.neon.tech/mcp](https://mcp.neon.tech/mcp)               |
  | [Notion](https://developers.notion.com/docs/get-started-with-mcp)                                                | [https://mcp.notion.com/mcp](https://mcp.notion.com/mcp)             |
  | [Prisma](https://www.prisma.io/docs/postgres/integrations/mcp-server#remote-mcp-server)                          | [https://mcp.prisma.io/mcp](https://mcp.prisma.io/mcp)               |
  | [Sentry](https://docs.sentry.io/product/sentry-mcp/)                                                             | [https://mcp.sentry.dev/mcp](https://mcp.sentry.dev/mcp)             |
  | [Vercel](https://vercel.com/docs/mcp/vercel-mcp)                                                                 | [https://mcp.vercel.com](https://mcp.vercel.com)                     |

  To add them to your project:

  1. navigate to **MCP Servers** in the Inkeep Visual Builder.
  2. Click on **New MCP Server**
  3. Choose from the preset list under **Popular Services** or register any under **Custom Server**

  When you register the server, an authentication pop-up will appear and allow you to sign in. Your credentials will automatically be saved to your [Nango Store](/typescript-sdk/credentials/nango) or [Keychain](/typescript-sdk/credentials/keychain) credential store.
</>

<>
  ### Next steps

  Once you have your server, you can register it in one of:

  <Cards>
    <Card title="The TypeScript SDK" icon="LuCode" href="/typescript-sdk/tools/mcp-tools#step-2-register-the-mcp-server-as-a-tool-in-your-agent">
      Add your MCP server as a tool for your agents in the TypeScript SDK
    </Card>

    <Card title="The Visual Builder" icon="LuPalette" href="/visual-builder/tools/mcp-servers#register-an-mcp-server">
      Add your MCP server as a tool for your agents in the Visual Builder
    </Card>
  </Cards>
</>


# MCP Server Options
URL: /tutorials/mcp-servers/overview

Learn about the recommended ways to use MCP servers with your agents

***

title: MCP Server Options
sidebarTitle: Overview
description: Learn about the recommended ways to use MCP servers with your agents
icon: "LuSparkles"
------------------

MCP servers enable your agents to fetch real-time information and take action on your systems, services, and applications.

## Choose your approach

Select the option that best fits your needs:

* **Native MCP Servers** - Pre-built servers from SaaS vendors (Atlassian, Linear, Notion, etc.). Fastest setup, just register and go.
* **Composio MCP Servers** - Access 10,000+ pre-built servers through Composio's platform. Similar to Native, but with a wider selection.
* **Custom MCP Servers** - Build your own servers for custom APIs and business logic. Requires development and deployment.
* **Gram by Speakeasy** - Convert OpenAPI specs into MCP servers using Gram by Speakeasy.

## Get started

<Cards>
  <Card title="Native MCP Servers" icon="LuPackageCheck" href="/tutorials/mcp-servers/native-mcp-servers">
    Connect to pre-built servers from providers like Atlassian, Linear, Notion, and more. No building required.
  </Card>

  <Card title="Composio MCP Servers" icon="brand/Composio" href="/tutorials/mcp-servers/composio-mcp-servers">
    Access thousands of out-of-box MCP servers through Composio's platform.
  </Card>

  <Card title="Custom MCP Servers" icon="brand/Inkeep" href="/tutorials/mcp-servers/custom-mcp-servers">
    Build your own custom MCP servers using Inkeep templates or Vercel's Next.js template.
  </Card>

  <Card title="Gram" icon="brand/Gram" href="/tutorials/mcp-servers/gram">
    Convert OpenAPI specs into MCP servers using Gram by Speakeasy.
  </Card>
</Cards>


# Environment-aware Credentials
URL: /typescript-sdk/credentials/env-aware-credentials

undefined

***

title: Environment-aware Credentials
sidebarTitle: Env-aware Credentials
icon: "LuLayers"
----------------

Environment-aware credentials enable automatic loading of environment-specific credentials (development, production, etc.) while keeping them cleanly separated and easily switchable via the CLI's --env flag.

Credentials are referenced in the TypeScript SDK using the `envSettings` object. Creating environment-aware credentials is a two step process:

### Step 1: Define environment configurations

<Tabs>
  <Tab title="Development Config">
    ```typescript title="projects/my-project/environments/development.env.ts"
    import { registerEnvironmentSettings } from '@inkeep/agents-sdk';
    import { CredentialStoreType } from '@inkeep/agents-core';

    // How credentials are referenced depends on how the credential was created, in this case this credential was created as an environment variable
    export const development = registerEnvironmentSettings({
    credentials: {
    'stripe_api_key': {
      id: 'stripe-api-key',
      name: 'Stripe API Key',
      type: CredentialStoreType.memory,
      credentialStoreId: 'memory-default',
      retrievalParams: {
        key: 'STRIPE_API_KEY_DEV',
      },
    }
    },
    });
    ```
  </Tab>

  <Tab title="Production Config">
    ```typescript title="projects/my-project/environments/production.env.ts"
    import { registerEnvironmentSettings } from '@inkeep/agents-sdk';
    import { CredentialStoreType } from '@inkeep/agents-core';

    // How credentials are referenced depends on how the credential was created, in this case this credential was created as an environment variable
    export const production = registerEnvironmentSettings({
    credentials: {
    'stripe_api_key': {
      id: 'stripe-api-key',
      name: 'Stripe API Key',
      type: CredentialStoreType.memory,
      credentialStoreId: 'memory-default',
      retrievalParams: {
        key: 'STRIPE_API_KEY_PROD',
      },
    }
    },
    });
    ```
  </Tab>

  <Tab title="Index File">
    ```typescript title="projects/my-project/environments/index.ts"
    import { createEnvironmentSettings } from '@inkeep/agents-sdk';
    import { development } from './development.env';
    import { production } from './production.env';

    export const envSettings = createEnvironmentSettings({
    development,
    production,
    });
    ```
  </Tab>
</Tabs>

### Step 2: Use the credentials in tools

```typescript title="<your-project-name>/tools/stripe-tool.ts"
import { mcpTool } from "@inkeep/agents-sdk";
import { envSettings } from "../environments";

export const stripeTool = mcpTool({
  id: 'stripe-tool',
  name: 'Stripe',
  serverUrl: 'https://mcp.stripe.com/mcp',
  credential: envSettings.getEnvironmentCredential('stripe_api_key'),
});
```

This pattern is useful if you want to keep track of different credentials for different environments. When you push your project using the [Inkeep CLI](/typescript-sdk/cli-reference#inkeep-push) `inkeep push` command with the `--env` flag, the credentials will be loaded from the appropriate environment file. For example, if you run `inkeep push --env development`, the credentials will be loaded from the `environments/development.env.ts` file.


# Use Environment Variables as Credentials
URL: /typescript-sdk/credentials/environment-variables

undefined

***

title: Use Environment Variables as Credentials
sidebarTitle: Environment Variables
icon: "LuDatabase"
------------------

Environment variables are a simple way to store credentials in your environment. They are stored in the environment variables in your `.env` file.

## Referencing credentials in SDK

Here is an example of how to reference a credential in the TypeScript SDK for Bearer Authentication.

```typescript
import { agent, subAgent, mcpTool, credential } from "@inkeep/agents-sdk";
import { CredentialStoreType } from "@inkeep/agents-core";

// Step 1: Reference the credential created in the environment file
const stripeCredential = credential({
  id: 'stripe-credential',
  name: 'Stripe Credential',
  type: CredentialStoreType.memory,
  credentialStoreId: 'memory-default',
  retrievalParams: {
    "key": "<environment-variable-name>", // where <environment-variable-name> is the name of the environment variable that contains the credential value, for example, STRIPE_API_KEY
  },
});

// Step 2: Use credential in MCP tool
const stripeTool = mcpTool({
  id: 'stripe-tool',
  name: 'Stripe Tool',
  description: 'Access Stripe payment services',
  serverUrl: 'https://mcp.stripe.com/mcp',
  credential: stripeCredential,
});
```

### Credential Configuration

| Parameter           | Type                | Required | Description                                              |
| ------------------- | ------------------- | -------- | -------------------------------------------------------- |
| `id`                | string              | Yes      | Unique identifier for the credential                     |
| `type`              | CredentialStoreType | Yes      | Type of credential store (memory, nango, or keychain)    |
| `credentialStoreId` | string              | Yes      | Identifier for the specific credential store instance    |
| `retrievalParams`   | object              | Yes      | Parameters for retrieving the credential from the store. |


# Use Keychain for Local Development
URL: /typescript-sdk/credentials/keychain

undefined

***

title: Use Keychain for Local Development
sidebarTitle: Keychain
icon: "LuLock"
--------------

Keychain is the default method for storing credentials for every project. It is a locally stored credential store for OAuth tokens from OAuth2.1/PKCE flows and Bearer authentication, configured through Visual Builder and referenced in the TypeScript SDK.

<Warning>
  Keychain lacks automatic token refresh, production suitability, and metadata header support, making Nango the recommended solution for production-ready credential management. See setup instructions for Nango [here](/typescript-sdk/credentials/nango).
</Warning>

## Referencing credentials in SDK

Here is an example of how to reference a credential in the TypeScript SDK for both Bearer Authentication and OAuth2.1/PKCE.

<Tabs>
  <Tab title="Bearer Authentication">
    ```typescript
    import { agent, subAgent, mcpTool, credential } from "@inkeep/agents-sdk";
    import { CredentialStoreType } from "@inkeep/agents-core";

    // Step 1: Reference the credential created in the Visual Builder
    const stripeCredential = credential({
      id: 'stripe-credential',
      name: 'Stripe Credential',
      type: CredentialStoreType.memory,
      credentialStoreId: 'memory-default',
      retrievalParams: {
        "key": "<id-given-to-bearer-api-key>" // where <id-given-to-bearer-api-key> is the id given to the bearer api key created through the Visual Builder
      },
    });

    // Step 2: Use credential in MCP tool
    const stripeTool = mcpTool({
      id: 'stripe-tool',
      name: 'Stripe Tool',
      description: 'Access Stripe payment services',
      serverUrl: 'https://mcp.stripe.com/mcp',
      credential: stripeCredential,
    });
    ```
  </Tab>

  <Tab title="OAuth2.1/PKCE">
    ```typescript
    import { agent, subAgent, mcpTool, credential } from "@inkeep/agents-sdk";
    import { CredentialStoreType } from "@inkeep/agents-core";

    // Step 1: Reference the credential created in the Visual Builder
    const stripeCredential = credential({
      id: 'stripe-credential',
      name: 'Stripe Credential',
      type: CredentialStoreType.memory, // Memory store
      credentialStoreId: 'memory-default',
      retrievalParams: {
        "key": "oauth_token_<toolId>" // where <toolId> is the id of the MCP tool the credential is associated with
      },
    });

    // Step 2: Use credential in MCP tool
    const stripeTool = mcpTool({
      id: 'stripe-tool',
      name: 'Stripe Tool',
      description: 'Access Stripe payment services',
      serverUrl: 'https://mcp.stripe.com/mcp',
      credential: stripeCredential,
    });
    ```
  </Tab>
</Tabs>

### Credential Configuration

| Parameter           | Type                | Required | Description                                              |
| ------------------- | ------------------- | -------- | -------------------------------------------------------- |
| `id`                | string              | Yes      | Unique identifier for the credential                     |
| `type`              | CredentialStoreType | Yes      | Type of credential store (memory, nango, or keychain)    |
| `credentialStoreId` | string              | Yes      | Identifier for the specific credential store instance    |
| `retrievalParams`   | object              | Yes      | Parameters for retrieving the credential from the store. |


# Use Nango as a Credential Store
URL: /typescript-sdk/credentials/nango

undefined

***

title: Use Nango as a Credential Store
sidebarTitle: Nango
icon: "brand/Nango"
-------------------

Nango is an excellent choice for both development and production environments, particularly when working with OAuth2.1/PKCE flows and complex integrations.

To get started, first set up Nango either through cloud or local deployment, then create your credential, and finally consume the credential through the TypeScript SDK.

## Nango setup option 1: Nango Cloud

### Step 1: Create a Nango account

Sign up [here](https://app.nango.dev/signin).

### Step 2: Save your Nango secret key

After creating your Nango account, navigate to Environment Settings in your dashboard and copy the secret key.

### Step 3: Configure your root `.env` file

```
NANGO_SECRET_KEY=your_nango_secret_key
```

Restart your dev server to load the new environment variable:

```bash
pnpm dev
```

### Step 4: Create a new credential in the Visual Builder using Nango

<Video src="/videos/create-nango-credential.mp4" />

## Nango setup option 2: Nango local

### Step 1: Clone the optional services repository

```bash
git clone https://github.com/inkeep/agents-optional-local-dev
cd agents-optional-local-dev
```

### Step 2: Start Nango Services

Inside the `agents-optional-local-dev` repository, run the following command:

```bash
docker-compose --profile nango up -d
```

### Step 3: Save your Nango secret key

1. Open Nango at `http://localhost:3050`
2. Navigate to Environment Settings and copy the secret key

### Step 4: Configure your root `.env` file

In your **root project directory** (not inside the `agents-optional-local-dev` repository), update your `.env` file:

```bash
NANGO_SECRET_KEY=your_nango_secret_key
NANGO_HOST=http://localhost:3050
PUBLIC_NANGO_CONNECT_BASE_URL=http://localhost:3051
```

Restart your dev server to load the new environment variables:

```bash
pnpm dev
```

### Step 5: Create a new credential in the Visual Builder using Nango

Create a new credential in the [Visual Builder](/visual-builder/credentials) using Nango Store as the credential store.

<Video src="/videos/create-nango-credential.mp4" />

## Referencing credentials in SDK

Once you have created a credential in the Visual Builder, you can reference it in the TypeScript SDK for both Bearer Authentication and OAuth2.1/PKCE.

Here is an example of how to reference a credential in the TypeScript SDK for both Bearer Authentication and OAuth2.1/PKCE.

<Tabs>
  <Tab title="Bearer Authentication">
    ```typescript
    import { agent, subAgent, mcpTool, credential } from "@inkeep/agents-sdk";
    import { CredentialStoreType } from "@inkeep/agents-core";

    // Step 1: Reference the credential created in the Visual Builder
    const stripeCredential = credential({
      id: 'stripe-credential',
      name: 'Stripe Credential',
      type: CredentialStoreType.memory,
      credentialStoreId: 'memory-default',
      retrievalParams: {
        "connectionId": "<id-given-to-bearer-api-key>", // where <id-given-to-bearer-api-key> is the id given to the bearer api key created through the Visual Builder
        "providerConfigKey": "<id-given-to-bearer-api-key>",
        "provider": "private-api-bearer",
        "authMode": "API_KEY"
      },
    });

    // Step 2: Use credential in MCP tool
    const stripeTool = mcpTool({
      id: 'stripe-tool',
      name: 'Stripe Tool',
      description: 'Access Stripe payment services',
      serverUrl: 'https://mcp.stripe.com/mcp',
      credential: stripeCredential,
    });
    ```
  </Tab>

  <Tab title="OAuth2.1/PKCE">
    ```typescript
    import { agent, subAgent, mcpTool, credential } from "@inkeep/agents-sdk";
    import { CredentialStoreType } from "@inkeep/agents-core";

    // Step 1: Reference the credential created in the Visual Builder
    const stripeCredential = credential({
      id: 'stripe-credential',
      name: 'Stripe Credential',
      type: CredentialStoreType.memory, // Memory store
      credentialStoreId: 'memory-default',
      retrievalParams: {
        "connectionId": "<nango-connection-id>", // Nango connection ID that was generated. You can confirm this in your nango dashboard (cloud or self-hosted)
        "providerConfigKey": "<mcp-server-name>_<mcp-server-generated-id>", // For example, linear_AABBCC1234
        "provider": "mcp-generic",
        "authMode": "OAUTH2"
      },
    });

    // Step 2: Use credential in MCP tool
    const stripeTool = mcpTool({
      id: 'stripe-tool',
      name: 'Stripe Tool',
      description: 'Access Stripe payment services',
      serverUrl: 'https://mcp.stripe.com/mcp',
      credential: stripeCredential,
    });
    ```
  </Tab>
</Tabs>

### Credential Configuration

| Parameter           | Type                | Required | Description                                              |
| ------------------- | ------------------- | -------- | -------------------------------------------------------- |
| `id`                | string              | Yes      | Unique identifier for the credential                     |
| `type`              | CredentialStoreType | Yes      | Type of credential store (memory, nango, or keychain)    |
| `credentialStoreId` | string              | Yes      | Identifier for the specific credential store instance    |
| `retrievalParams`   | object              | Yes      | Parameters for retrieving the credential from the store. |


# Credential Store Options
URL: /typescript-sdk/credentials/overview

undefined

***

title: Credential Store Options
sidebarTitle: Overview
icon: "LuSparkles"
------------------

## Credential Store Options

MCP servers and external agents may require authentication for secure access. The Inkeep agent framework supports storing these credentials in three different ways:

<Cards>
  <Card title="Nango Store (Recommended)" icon="brand/Nango" href="/typescript-sdk/credentials/nango">
    **Best for:** Development or Production environments with OAuth2.1/PKCE flows and complex integrations

    **Pros:**

    * Automatic token refresh for OAuth
    * Supports additional metadata headers
    * Works with complex OAuth flows (OAuth2.0/PKCE)
    * Managed service (self-hosted or cloud)
  </Card>

  <Card title="Keychain Store (Default)" icon="LuLock" href="/typescript-sdk/credentials/keychain">
    **Best for:** Local development with OAuth services

    **Cons:**

    * Not suitable for production
    * No automatic token refresh
    * Requires manual re-authentication when tokens expire
    * Does not support additional metadata headers
  </Card>

  <Card title="Environment Variables" icon="LuDatabase" href="/typescript-sdk/credentials/environment-variables">
    **Best for:** Simple API keys and bearer tokens in development or production

    **Pros:**

    * Direct configuration via TypeScript SDK

    **Cons:**

    * Does not support additional metadata headers
    * Does not support OAuth2.1/PKCE flows
  </Card>
</Cards>

## Environment-aware Credentials

When you need different credentials for different environments (e.g., development vs. production), you can take advantage of [environment-aware credentials](/typescript-sdk/credentials/env-aware-credentials). This approach allows you to:

* Define separate credentials for each environment
* Automatically load the correct credentials based on your deployment environment
* Keep your development and production credentials cleanly separated
* Easily switch between environments using the CLI's `--env` flag

Learn more about setting up environment-aware credentials in the [dedicated guide](/typescript-sdk/credentials/env-aware-credentials).


# Artifact Components
URL: /typescript-sdk/structured-outputs/artifact-components

Learn how to use artifact components to store and retrieve data from the agent

***

title: Artifact Components
description: Learn how to use artifact components to store and retrieve data from the agent
icon: "TbInputSpark"
--------------------

<>
  Artifacts are structured components that capture and store source information when agents interact with tools or other agents. They act as a record-keeping system, automatically documenting where information comes from during tool and agent interactions.

  ## How Artifacts Work

  When an agent uses a tool (whether that's another agent or a utility tool), the response is automatically parsed to create artifacts. These artifacts store:

  * The source of the information (tool/agent used)
  * The relevant content from the response
  * Metadata about the interaction
</>

## Defining Artifact Components

Artifact components are defined using the `artifactComponent` builder function. **We recommend using Zod schemas** for type safety and better developer experience.

<Callout>
  **Quick Start**: Citation artifacts are automatically included when you create
  a new project with `npx @inkeep/create-agents`, providing a ready-to-use
  example.
</Callout>

```typescript
import { artifactComponent } from "@inkeep/agents-sdk";
import { z } from "zod";
import { preview } from "@inkeep/agents-core";

export const citation = artifactComponent({
  id: "citation",
  name: "citation",
  description: "Structured factual information extracted from search results",
  props: z.object({
    title: preview(z.string().describe("Title of the source document")),
    url: preview(z.string().describe("URL of the source document")),
    record_type: preview(
      z.string().describe("Type of record (documentation, blog, guide, etc.)")
    ),
    content: z
      .array(
        z.object({
          type: z
            .string()
            .describe("Type of content (text, image, video, etc.)"),
          text: z.string().describe("The actual text content"),
        })
      )
      .describe(
        "Array of structured content blocks extracted from the document"
      ),
  }),
});
```

<Callout>
  JSON Schema is also supported. Set `inPreview: true` on properties instead of
  using `preview()`.
</Callout>

## Schema Requirements

<Callout type="warning">
  **Critical**: Artifact schemas must match your tool's output structure. The
  system uses JMESPath selectors on JSON - it **cannot extract from free text**.
</Callout>

```typescript
// ❌ WRONG: Tool returns text, schema expects structured data
// Tool output: { result: { content: [{ text: "Weather: Sunny, 75°F" }] } }
props: z.object({
  temperature: z.number(), // ❌ Cannot extract number from text
  condition: z.string(), // ❌ Cannot extract condition from text
});

// ✅ CORRECT: Tool returns structured data matching schema
// Tool output: { result: { temperature: 75, condition: "Sunny" } }
props: z.object({
  temperature: z.number(),
  condition: z.string(),
});
```

Use OpenTelemetry traces to debug schema validation issues.

## Preview Fields

Use `preview()` to mark fields for immediate availability. The `preview()` helper automatically sets `inPreview: true` in the generated schema.

**Preview fields are:**

* Shown to other agents for reasoning
* Streamed in real-time to clients (Vercel AI SDK)
* Auto-rendered by Inkeep's widget (citations as interactive cards)
* Available immediately in UI (full artifact loads on-demand)

**Non-preview fields** require explicitly fetching the full artifact.

**No schema?** Omit `props` to save the entire tool result without filtering.

## Artifact Creation

When an agent uses a tool:

1. The tool processes the request and returns a response
2. **The agent decides** whether to create an artifact from the tool response
3. If created, the artifact is parsed according to the artifact component schema
4. The artifact can be associated with any data components that reference this information

## Artifacts vs Data Components

**Artifacts** and **Data Components** are different:

* **Artifacts**: Citations/sources from tool results stored in the database
* **Data Components**: UI elements agents output in responses (Text, Fact, etc.)

Artifacts provide the source citations that back up information in data components.

## Using in Agents

After defining your artifact component, use it in an agent:

```typescript
import { agent } from "@inkeep/agents-sdk";
import { citation } from "./artifact-components/citation";

const searchAgent = agent({
  id: "search-agent",
  canUse: () => [searchTool],
  prompt: "Search for information and cite sources using artifacts.",
  artifactComponents: () => [citation],
});
```

## Citation Artifacts

Citation artifacts that are named `citation` and have `title` and `url` preview fields are automatically rendered as interactive cards by Inkeep's widget library. This provides source attribution and allows users to verify information at the source.

<Image src="/images/citation-widget-example.png" alt="Citation artifact rendered as an interactive card in the Inkeep widget showing source attribution" style={{ marginTop: "1rem" }} />

## Example Flow

Here's a complete example with inline artifact component definition:

```typescript
import { agent } from "@inkeep/agents-sdk";
import { z } from "zod";
import { preview } from "@inkeep/agents-core";

const searchAgent = subAgent({
  id: "search",
  canUse: () => [searchTool],
  prompt: "Search for information and cite sources using artifacts.",
  artifactComponents: [
    {
      id: "citation",
      name: "citation",
      description: "Search result document",
      props: z.object({
        title: preview(z.string().describe("Document title")),
        url: preview(z.string().describe("Document URL")),
        content: z.string().describe("Document content"),
      }),
    },
  ],
});
```

## No Schema Example

```typescript
const rawDataAgent = subAgent({
  id: "raw-data",
  canUse: () => [apiTool],
  prompt: "Fetch data and save complete responses.",
  artifactComponents: [
    {
      id: "api-response",
      name: "API Response",
      description: "Complete API response data",
      // No props - saves entire tool result
    },
  ],
});
```

Example flow:

1. Agent uses search tool and gets results
2. **Agent decides** to create an artifact citing the source document
3. Artifact is stored with preview fields (title, url) shown to other agents
4. Other agents can reference this artifact or get full content when needed


# Create Rich UI Blocks with Data Components
URL: /typescript-sdk/structured-outputs/data-components

Learn how to create and use data components for rich, interactive Agent messages.

***

title: Create Rich UI Blocks with Data Components
sidebarTitle: Custom UI Blocks
description: Learn how to create and use data components for rich, interactive Agent messages.
icon: "LuBlocks"
----------------

<>
  ## What are Data Components?

  Data Components allow your agents to return rich, interactive content instead of just text. Think of them as reusable UI building blocks that your agent can populate with data.

  For example, instead of returning "You have 3 tasks: Task #123 (shipped), Task #124 (processing)...", your agent can return a properly formatted task list component.
</>

## Defining Data Components

Data components are defined using the `dataComponent` builder function. **We recommend using Zod schemas** for type safety and better developer experience.

```typescript
import { dataComponent } from '@inkeep/agents-sdk';
import { z } from 'zod';

export const taskList = dataComponent({
  id: "task-list",
  name: "TaskList", 
  description: "Display user tasks with status",
  props: z.object({
    tasks: z
      .array(
        z.object({
          id: z.string().describe("Unique task identifier"),
          title: z.string().describe("Task title"),
          completed: z.boolean().describe("Whether the task is completed"),
          priority: z.enum(["low", "medium", "high"]).describe("Task priority"),
        })
      )
      .describe("Array of user tasks"),
    totalCount: z.number().describe("Total number of tasks"),
    completedCount: z.number().describe("Number of completed tasks"),
  }),
});
```

<Callout>
  JSON Schema is also supported if you prefer traditional schema definitions.
</Callout>

## Using in Agents

Register data components with your agent:

```typescript
import { agent } from '@inkeep/agents-sdk';
import { taskList } from './data-components/task-list';

const taskAgent = agent({
  id: "task-agent",
  name: "Task Agent", 
  prompt: "Provide helpful answers and use data components when appropriate.",
  dataComponents: () => [taskList],
});
```

When a user asks "Show me my tasks", the agent will respond with:

```json
{
  "dataComponents": [
    {
      "id": "task-list",
      "name": "TaskList",
      "props": {
        "tasks": [
          { "id": "1", "title": "Review documentation", "completed": false },
          { "id": "2", "title": "Update website", "completed": true }
        ]
      }
    }
  ]
}
```

## Frontend Integration

Create a React component matching your data component name:

```tsx
const TaskList = ({ tasks, totalCount, completedCount }) => (
  <div className="task-list">
    <h3>Your Tasks ({completedCount}/{totalCount} completed)</h3>
    {tasks.map((task) => (
      <div key={task.id} className={task.completed ? "completed" : ""}>
        {task.title}
      </div>
    ))}
  </div>
);
```

Register it with the Inkeep chat component:

```tsx
<InkeepSidebarChat
  aiChatSettings={{
    agentUrl: "your-agent-url",
    components: {
      TaskList, // Component name must match data component name
    },
  }}
/>
```

The agent will automatically return structured data that renders as your React component.


# Status Updates
URL: /typescript-sdk/structured-outputs/status-updates

Real-time progress updates powered by AI that keep users informed during long-running agent operations

***

title: Status Updates
description: Real-time progress updates powered by AI that keep users informed during long-running agent operations
icon: "LuClock"
---------------

import { Callout } from "fumadocs-ui/components/callout";

# Status Updates

The Inkeep Agent Framework provides intelligent, AI-powered status updates that automatically generate contextual progress messages during agent execution. These updates give users ChatGPT-style feedback about what's happening behind the scenes without exposing internal technical details.

## Overview

Status updates are automatically generated summaries that:

* **Track Progress**: Monitor agent operations, tool calls, and task completions
* **Provide Context**: Generate user-friendly descriptions of what's happening
* **Hide Complexity**: Abstract away internal agent names and technical operations
* **Stream Real-time**: Send updates via the same streaming interface as responses

<Callout type="info">
  Status updates use your Agent's summarizer model to generate contextual,
  intelligent progress messages that feel natural to users.
</Callout>

## How It Works

The status updater operates through three main components:

### 1. Agent Session Event Tracking

Every agent operation is tracked as events:

* **agent\_generate**: Text generation or structured output
* **transfer**: Agent-to-agent transfers
* **delegation\_sent/returned**: Task delegation between agents
* **tool\_call**: When a tool is called with arguments
* **tool\_result**: When a tool execution completes (success or failure)
* **error**: System-level errors and configuration issues
* **artifact\_saved**: Document or data artifacts created

### 2. Intelligent Triggering

Status updates are triggered by:

* **Event Count**: After N events (tool calls, generations, etc.)
* **Time Intervals**: Every N seconds of processing
* **Smart Detection**: Avoids updates during text streaming

### 3. AI-Powered Summarization

The summarizer model:

* Analyzes recent events and progress
* Generates user-friendly status messages
* Maintains context across multiple updates
* Focuses on user-visible outcomes

## Configuration

Configure status updates in your agent:

```typescript
export const myAgent = agent({
  id: "my-agent",
  defaultSubAgent: myAgent,
  subAgents: () => [myAgent],

  // Model Settings with summarizer
  models: {
    base: { model: "anthropic/claude-sonnet-4-5" },
    summarizer: { model: "anthropic/claude-sonnet-4-5" }, // Model for status updates
  },

  // Status updates configuration
  statusUpdates: {
    numEvents: 3, // Trigger after 3 events
    timeInSeconds: 15, // Trigger every 15 seconds
    prompt: "Custom prompt for status updates", // Optional
  },
});
```

### Configuration Options

| Option             | Type   | Default       | Description                                                   |
| ------------------ | ------ | ------------- | ------------------------------------------------------------- |
| `numEvents`        | number | 10            | Trigger update after N events                                 |
| `timeInSeconds`    | number | 30            | Trigger update every N seconds                                |
| `model`            | string | agent default | Override model for summaries                                  |
| `prompt`           | string | undefined     | Custom prompt appended to base system prompt (max 2000 chars) |
| `statusComponents` | array  | undefined     | Structured status components (advanced)                       |

## Basic Example

```typescript
const searchAgent = subAgent({
  id: "search-agent",
  name: "Search Agent",
  prompt: "Help users search and analyze information.",
  canUse: () => [searchTool],
});

export const searchDemo = agent({
  id: "search-demo",
  defaultSubAgent: searchAgent,
  subAgents: () => [searchAgent],

  models: {
    base: { model: "anthropic/claude-sonnet-4-5" },
    summarizer: { model: "anthropic/claude-sonnet-4-5" },
  },

  // Enable status updates
  statusUpdates: {
    numEvents: 2, // Update every 2 operations
    timeInSeconds: 10, // Or every 10 seconds
  },
});
```

**User Experience:**
When a user asks "What's the weather in Paris?", they might see:

1. "Searching for current weather information..."
2. "Found weather data, analyzing conditions..."
3. "Preparing detailed weather report..."

## Custom Prompts

You can customize how status updates are generated by providing a custom prompt that gets appended to the base system prompt. Custom prompts are limited to 2000 characters to ensure optimal performance:

```typescript
export const myAgent = agent({
  id: "my-agent",
  defaultSubAgent: myAgent,
  subAgents: () => [myAgent],
  models: {
    summarizer: { model: "anthropic/claude-sonnet-4-5" },
  },
  statusUpdates: {
    numEvents: 3,
    timeInSeconds: 15,
    // Custom prompt is appended to the base system prompt
    prompt: "KEEP ALL STATUS UPDATES SHORT AND CONCISE. Use bullet points and focus only on user-visible progress.",
  },
});
```

### Custom Prompt Examples

**Concise Updates:**

```typescript
statusUpdates: {
  prompt: 'Keep responses to 5 words maximum. Use present tense verbs.',
}
// Results in: "Searching documentation", "Processing data", "Generating report"
```

**Detailed Progress:**

```typescript
statusUpdates: {
  prompt: 'Provide specific details about what was found or accomplished. Include relevant numbers or names when available.',
}
// Results in: "Found 12 API endpoints in authentication docs", "Retrieved user profile for john@example.com"
```

**Branded Tone:**

```typescript
statusUpdates: {
  prompt: 'Use a friendly, helpful tone. Start updates with action words like "Discovering", "Exploring", "Analyzing".',
}
// Results in: "Discovering relevant documentation...", "Analyzing search results for best matches"
```

## Default vs Structured Status Updates

Status updates can be generated in two ways:

### Default Status Components

When no `statusComponents` are configured, the system uses built-in default status components that generate structured labels with contextual details:

* **`label`**: AI-generated user-friendly description (e.g., "Searching documentation for API examples")
* **`details`**: Optional structured data with context about the operation

The default status components are defined in [`packages/agents-sdk/src/default-status-schemas.ts`](https://github.com/inkeep/agents/blob/main/packages/agents-sdk/src/default-status-schemas.ts):

```typescript
// Error loading local file from agents-run-api/src/utils/default-status-schemas.ts
// ENOENT: no such file or directory, open '/vercel/path1/agents-run-api/src/utils/default-status-schemas.ts'
```

### Custom Structured Components

For complete control over status format, define custom structured status components using Zod schemas with the `statusComponent` helper:

```typescript
import { z } from 'zod';
import { statusComponent } from '@inkeep/agents-sdk';

const toolSummary = statusComponent({
  type: 'tool_summary',
  description: 'Summary of tool calls and their purpose',
  detailsSchema: z.object({
    tool_name: z.string().describe('Name of tool used'),
    purpose: z.string().describe('Why this tool was called'),
    outcome: z.string().describe('What was discovered or accomplished'),
  }),
});

const progressUpdate = statusComponent({
  type: 'progress_update',
  description: 'Progress information with metrics',
  detailsSchema: z.object({
    current_step: z.string(),
    items_processed: z.number().optional(),
    status: z.enum(['in_progress', 'completed', 'pending']),
  }),
});

export const myAgent = agent({
  id: "my-agent",
  defaultSubAgent: myAgent,
  subAgents: () => [myAgent],
  models: {
    summarizer: { model: "anthropic/claude-sonnet-4-5" },
  },
  statusUpdates: {
    numEvents: 3,
    timeInSeconds: 15,
    statusComponents: [
      toolSummary.config,
      progressUpdate.config,
    ],
  },
});
```

<Callout type="info">
  The `statusComponent` helper provides type-safe status component definitions with automatic schema validation. Zod schemas are automatically converted to JSON Schema format at runtime.
</Callout>

### Status Component API

The `statusComponent` function accepts:

| Property        | Type               | Required | Description                                         |
| --------------- | ------------------ | -------- | --------------------------------------------------- |
| `type`          | string             | Yes      | Unique identifier for this status component type    |
| `description`   | string             | No       | Description of when/why this status is used         |
| `detailsSchema` | `z.ZodObject<any>` | No       | Zod schema defining the structure of status details |

**Note:** Use `.config` when passing status components to the agent configuration

## Frontend Integration

Status updates arrive as `data-summary` events with AI-generated labels and contextual details:

```typescript
// In your message processing
message.parts.forEach((part) => {
  if (part.type === "data-summary") {
    const { type, label, details } = part.data;

    // Display the user-friendly status label
    displayStatusUpdate(label);

    // Handle optional structured details
    if (details) {
      // For default status components: contextual operation details
      // For custom components: your defined schema structure
      displayStructuredDetails(details);
    }

    // The 'type' field indicates the summary category
    console.log(`Status update type: ${type}`);
  }
});
```

### Data Structure Examples

**Custom Status Components:**

```json
{
  "type": "tool_summary",
  "label": "Search completed successfully",
  "details": {
    "tool_name": "search_knowledge_base",
    "purpose": "Find API authentication documentation",
    "outcome": "Found 5 relevant articles with code examples"
  }
}
```

## Best Practices

### Timing Configuration

* **Quick Operations**: Use higher event counts (5-10) to avoid too many updates
* **Long Operations**: Use shorter time intervals (10-15 seconds) for responsiveness
* **Mixed Workloads**: Combine both triggers for balanced updates

### Model Selection

* **Faster Model**: Use a faster/cheaper model for status updates to reduce latency
* **Specialized Model**: Use a model optimized for summarization tasks

### User Experience

```typescript
// Good: Descriptive and actionable
"Searching through documentation to find API authentication methods...";
"Found OAuth2 setup prompt, now checking for code examples...";

// Avoid: Too technical or vague
"Agent thinking...";
"Processing data-operation with tool_invocation type...";
```

## Troubleshooting

### Updates Not Appearing

Check that:

1. Status updates are configured in your Agent
2. The summarizer model is specified
3. Events are being triggered (tool calls, generations)
4. The session hasn't ended prematurely

### Too Many/Few Updates

Adjust thresholds:

```typescript
statusUpdates: {
  numEvents: 5,        // Increase for fewer updates
  timeInSeconds: 20,   // Increase for less frequent updates
}
```

### Poor Update Quality

Improve with custom prompts:

```typescript
statusUpdates: {
  numEvents: 3,
  timeInSeconds: 15,
  prompt: `Generate a brief, user-friendly status update that explains what has been accomplished and what is currently happening. Focus on user-visible progress, not internal operations. Be specific about findings, not just actions.`
}
```

<Callout type="warning">
  Status updates are automatically paused during text streaming to avoid
  interrupting the response flow.
</Callout>

## Performance Considerations

* Status updates use additional model calls - consider costs for high-volume applications
* Updates are generated asynchronously and won't block main agent operations


# Function Tools
URL: /typescript-sdk/tools/function-tools

Create custom JavaScript functions that your agents can execute in secure sandboxes

***

title: Function Tools
description: Create custom JavaScript functions that your agents can execute in secure sandboxes
icon: "LuCode"
--------------

Function tools allow you to create custom JavaScript functions that agents can execute in secure, isolated sandboxes. Unlike [MCP servers](/typescript-sdk/tools/mcp-servers) that connect to external services, function tools run your own code directly within the agent framework.

## Overview

Function tools are perfect for:

* **Custom business logic** - Implement domain-specific calculations or workflows
* **Data processing** - Transform, validate, or analyze data using JavaScript
* **API integrations** - Make HTTP calls to services that don't have MCP servers
* **Utility functions** - Create reusable helper functions for your agents

## Creating Function Tools

### Basic Function Tool

```typescript
import { agent, functionTool } from "@inkeep/agents-sdk";

const calculateBMI = functionTool({
  name: "calculate-bmi",
  description: "Calculate BMI and health category",
  inputSchema: {
    type: "object",
    properties: {
      weight: { type: "number", description: "Weight in kilograms" },
      height: { type: "number", description: "Height in meters" },
    },
    required: ["weight", "height"],
  },
  execute: async ({ weight, height }) => {
    const bmi = weight / (height * height);
    let category = "Normal";
    if (bmi < 18.5) category = "Underweight";
    else if (bmi >= 30) category = "Obese";

    return { bmi: Math.round(bmi * 10) / 10, category };
  },
});

const healthAgent = subAgent({
  id: "health-agent",
  name: "Health Assistant",
  prompt: "I help with health calculations using available tools.",
  canUse: () => [calculateBMI],
});
```

### Function Tool with Dependencies

Dependencies are automatically detected from your code and use the versions installed in your project:

```typescript
const fetchJoke = functionTool({
  name: "fetch-joke",
  description: "Fetch a random programming joke",
  inputSchema: {
    type: "object",
    properties: {},
    required: [],
  },
  // Dependencies detected automatically from require() calls
  execute: async () => {
    const axios = require("axios"); // Uses version from your project
    const response = await axios.get(
      "https://official-joke-api.appspot.com/jokes/programming/random"
    );
    return {
      setup: response.data[0].setup,
      punchline: response.data[0].punchline,
    };
  },
});
```

### Pinning Dependency Versions

If you need to pin to specific versions, specify them explicitly:

```typescript
const fetchJoke = functionTool({
  name: "fetch-joke",
  description: "Fetch a random programming joke",
  dependencies: {
    axios: "1.6.0", // Pin to exact version
  },
  execute: async () => {
    const axios = require("axios");
    // Uses axios 1.6.0 regardless of your project version
    return {
      joke: "Why do programmers prefer dark mode? Because light attracts bugs!",
    };
  },
});
```

### Built-in Node.js Modules

Function tools have access to Node.js built-in modules:

```typescript
const generatePassword = functionTool({
  name: "generate-password",
  description: "Generate a secure random password",
  inputSchema: {
    type: "object",
    properties: {
      length: { type: "number", default: 12, description: "Password length" },
    },
  },
  execute: async ({ length = 12 }) => {
    const crypto = require("crypto");
    const charset =
      "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";

    let password = "";
    for (let i = 0; i < length; i++) {
      password += charset[crypto.randomInt(0, charset.length)];
    }

    return { password, length };
  },
});
```

## Input Schema Validation

Function tools use JSON Schema to validate input parameters. This ensures your functions receive properly typed and validated data.

### Supported JSON Schema Types

```typescript
// Example schema showing common types
{
  type: "object",
  properties: {
    name: { type: "string", description: "User name" },
    age: { type: "number", minimum: 0, description: "User age" },
    active: { type: "boolean", description: "Is active" },
    tags: { type: "array", items: { type: "string" } },
    status: { type: "string", enum: ["pending", "approved"] }
  },
  required: ["name"]
}
```

## Execution Environment

Function tools run in secure, isolated sandboxes that provide a safe execution environment for your code.

### Sandbox Providers

The framework supports multiple sandbox providers:

* **Native** (default) - Uses Node.js child processes, works in most environments including cloud VMs, Docker, Kubernetes, and traditional hosting
* **Vercel** - Uses Vercel Sandbox MicroVMs for serverless environments where child process spawning is restricted (Vercel, AWS Lambda, etc.)

The sandbox provider is configured at the application level when deploying. See [Deploy to Vercel](/self-hosting/vercel#function-tools-with-vercel-sandbox) for serverless deployment configuration.

### Runtime Configuration

Configure execution settings in your application:

```typescript
import { createExecutionApp } from "@inkeep/agents-run-api";

const app = createExecutionApp({
  sandboxConfig: {
    provider: "native", // or 'vercel' for serverless
    runtime: "node22", // Node.js 22 or 'typescript'
    timeout: 30000, // 30 second timeout
    vcpus: 2, // Max 2 concurrent executions
  },
});
```

### Security & Isolation

Function tools execute with strong security guarantees:

* **Isolated execution** - Each function runs in its own sandbox
* **No file system access** - Cannot read or write outside the sandbox
* **Network restrictions** - Only through explicitly declared dependencies
* **Resource limits** - CPU, memory, and execution time constraints enforced
* **No state persistence** - Functions are stateless between executions

### Best Practices

* **Keep functions focused** - Each function should do one thing well
* **Minimize dependencies** - Only include packages you actually need
* **Handle errors gracefully** - Always catch and return meaningful errors
* **Test independently** - Functions should be testable in isolation
* **Document thoroughly** - Clear descriptions help agents use tools effectively


# Register MCP Servers as Tools
URL: /typescript-sdk/tools/mcp-tools

Learn how to add and configure MCP tools for your agents

***

title: Register MCP Servers as Tools
sidebarTitle: MCP Tools
description: Learn how to add and configure MCP tools for your agents
icon: "LuHammer"
----------------

MCP tools connect to external servers that implement the MCP standard. This allows you to integrate with a wide ecosystem of existing tools and services.

Using MCP tools is a two step process:

### Step 1: Get an MCP server URL

You need access to an MCP server before you can use its tools. Learn about connecting to Native servers, using Composio, using Gram, or building Custom servers in the [MCP Servers tutorial](/tutorials/mcp-servers/overview).

### Step 2: Register the MCP server as a tool in your agent

```typescript
import { subAgent, mcpTool } from "@inkeep/agents-sdk";

// Register an existing MCP server as a tool
const knowledgeBaseTool = mcpTool({
  id: "knowledge-base-tool",
  name: "knowledge_base",
  description: "Search the company knowledge base for information",
  serverUrl: "https://kb.yourcompany.com/mcp", // URL of your deployed MCP server
});

const qaAgent = subAgent({
  id: "qa-agent",
  name: "QA Agent",
  description: "Responsible for answering questions about the company knowledge base.",
  prompt: `You are a Question-Answer agent that can answer questions about the company knowledge base. You have access to the knowledge base tool to search for information.`,
  canUse: () => [knowledgeBaseTool],
});
```

<Note>Tip: When adding tools to an agent, you can also reference the tool in the agent's prompt to help the agent understand how to use the tool.</Note>

## Authentication

If your MCP server requires authentication, we support various authentication methods (via credentials):

* **No Authentication** - For public APIs or internal services
* **API Key** - For services requiring API keys
* **Bearer Token** - For JWT or similar token-based authentication
* **Token Authentication** - For custom token schemes
* **OAuth Flows** - For standard OAuth 2.0 authentication
* **OAuth 2.1 Flows** - For modern OAuth 2.1 "1-click" authentication

For OAuth flows and OAuth 2.1 flows, it's recommended to use the [Visual Builder](/visual-builder/tools/mcp-servers) for easier configuration.

See [Credentials](/typescript-sdk/credentials/overview) for detailed examples and implementation guidance for each authentication type.

### Custom Headers

You can configure custom headers for your MCP server requests. Use credentials for sensitive information (API keys, tokens) and headers for non-sensitive metadata (user agent, version info, etc.).

```typescript
import { mcpTool } from "@inkeep/agents-sdk";

const customHeadersTool = mcpTool({
  id: "enterprise-api",
  name: "enterprise_data",
  description: "Enterprise API with custom headers",
  serverUrl: "https://enterprise.example.com/mcp",
  headers: {
    "User-Agent": "Inkeep-Agent/1.0",
    "X-Client-Version": "2024.1",
  },
});
```

## Selecting Tools

### Selective Tool Activation

Enable only specific tools from a server using MCP Server tool names in the `activeTools` field.

```typescript
import { mcpTool } from "@inkeep/agents-sdk";

const selectiveTool = mcpTool({
  id: "limited-server",
  name: "analytics_readonly",
  description: "Analytics server with limited access",
  serverUrl: "https://analytics.example.com/mcp",
  activeTools: ["get_metrics", "generate_report"], // Only these tools
});
```

### Using `with` for Tool Selection

While `activeTools` in `mcpTool` limits which tools are available from the server, you can further refine tool access at the sub agent level using `mcpTool.with`. This allows different agents to use different subsets of tools from the same MCP server.

```typescript
import { agent, mcpTool } from "@inkeep/agents-sdk";

// Define the MCP server with all available tools
const customerSupportTool = mcpTool({
  id: "customer-support-tool",
  name: "Customer Support Tool",
  description: "Customer Support Tool",
  serverUrl: "https://customer-support.example.com/mcp",
});

// Agent that only uses specific tools from the server
const customerSupportAgent = subAgent({
  id: "customer-support-agent",
  name: "Customer Support Agent",
  description: "Responsible for customer support",
  prompt: "You are a helpful assistant",
  canUse: () => [customerSupportTool.with({ 
      selectedTools: ["customer-support-tool"], 
      headers: { "X-Custom-Header": "custom-value" } 
    })],
});
```

## Environment-Aware MCP Servers

You can also configure MCP tools to switch based on your environment. This is useful when you want to use different MCP tool configurations for development vs production.

Creating environment-aware MCP tools is a two step process:

### Step 1: Define environment configurations

<Tabs>
  <Tab title="Development Config">
    ```typescript title="projects/my-project/environments/development.env.ts"
    import { registerEnvironmentSettings, mcpTool } from '@inkeep/agents-sdk';
    import { CredentialStoreType } from '@inkeep/agents-core';

    export const development = registerEnvironmentSettings({
    mcpServers: {
    'customer_support_tool': mcpTool({
      id: 'customer-support-tool',
      name: 'Customer Support Tool',
      description: 'Customer Support Tool for development',
      serverUrl: 'http://localhost:3000/customer-support/mcp',
    })
    },
    });
    ```
  </Tab>

  <Tab title="Production Config">
    ```typescript title="projects/my-project/environments/production.env.ts"
    import { registerEnvironmentSettings, mcpTool } from '@inkeep/agents-sdk';
    import { CredentialStoreType } from '@inkeep/agents-core';

    export const production = registerEnvironmentSettings({
    mcpServers: {
    'customer_support_tool': mcpTool({
      id: 'customer-support-tool',
      name: 'Customer Support Tool',
      description: 'Customer Support Tool for production',
      serverUrl: 'https://customer-support.example.com/mcp',
    })
    },
    });
    ```
  </Tab>

  <Tab title="Index File">
    ```typescript title="projects/my-project/environments/index.ts"
    import { createEnvironmentSettings } from '@inkeep/agents-sdk';
    import { development } from './development.env';
    import { production } from './production.env';

    export const envSettings = createEnvironmentSettings({
    development,
    production,
    });
    ```
  </Tab>
</Tabs>

### Step 2: Use the MCP tool in your sub agent

```typescript title="projects/my-project/agents/customer-support-agent.ts"
import { subAgent } from "@inkeep/agents-sdk";
import { envSettings } from "../environments";

const customerSupportAgent = subAgent({
  id: "customer-support-agent",
  name: "Customer Support Agent",
  description: "Responsible for customer support",
  prompt: "You are a helpful assistant",
  canUse: () => [envSettings.getEnvironmentMcp('customer_support_tool')],
});
```


# Style Components
URL: /ui-components/customization/styling

Customize the appearance of Inkeep's components.

***

title: Style Components
description: Customize the appearance of Inkeep's components.
keywords: UI styling, component customization, visual customization, theme configuration, CSS customization, design customization, UI appearance, style configuration, component theming, visual design, UI customization, component styling
icon: "LuPalette"
-----------------

The style configuration provides comprehensive settings for customizing the appearance of Inkeep widgets. This includes theming, typography, spacing, and component-specific styles.

## Theme Configuration

The theme configuration is defined through the `UserTheme` interface which extends `Partial<IkpTheme>`. This allows for deep customization of the widget's appearance.

```typescript
import { type InkeepBaseSettings } from "@inkeep/cxkit-types";

const baseSettings: InkeepBaseSettings = {
  theme: {
    // Basic color customization
    primaryColors: {
      primary: "#26D6FF",
      secondary: "#6366F1",
    },

    // Syntax highlighter themes
    syntaxHighlighter: {
      lightTheme: themes.github,
      darkTheme: themes.dracula,
    },

    // Custom styles injection
    styles: [
      {
        key: "google-fonts",
        type: "link",
        value:
          "https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap",
      },
      {
        key: "custom-theme",
        type: "style",
        value: `
          .ikp-ai-chat-message {
            border-radius: 8px;
            padding: 12px;
          }
          [data-theme='dark'] .ikp-ai-chat-message {
            background: #2D3748;
          }
        `,
      },
    ],

    // CSS variables container class name
    varsClassName: "ikp-variables",

    // Disable loading the default font for the widgets
    disableLoadingDefaultFont: true,
  },
};
```

### Theme Properties

#### Primary Colors

The `primaryColors` property allows you to define the color variations used throughout the widget. It accepts the following color options:

```typescript
primaryColors: {
  textBold?: string         // Bold text color
  textSubtle?: string       // Subtle text color
  lighter?: string          // Lightest shade
  light?: string           // Light shade
  lightSubtle?: string     // Subtle light shade
  medium?: string          // Medium shade
  mediumSubtle?: string    // Subtle medium shade
  strong?: string          // Strong shade
  stronger?: string        // Stronger shade
  textColorOnPrimary?: string     // Text color on primary background
}
```

All colors should be provided as valid CSS color values (hex, rgb, hsl, etc). Each property is optional, allowing you to customize only the specific color variations you need.

#### Syntax Highlighter Theme

The `syntaxHighlighter` property lets you configure different themes for code blocks in light and dark modes.

By default, the Prism syntax highlighting theme we use is [oneLight](https://github.com/FormidableLabs/prism-react-renderer/blob/master/packages/prism-react-renderer/src/themes/oneLight.ts) in light mode and [vsDark](https://github.com/FormidableLabs/prism-react-renderer/blob/master/packages/prism-react-renderer/src/themes/vsDark.ts) in dark mode. To use a different theme, you can provide it in the theme.syntaxHighlighter prop.

```typescript
syntaxHighlighter: {
  lightTheme: themes.github,  // Theme for light mode
  darkTheme: themes.dracula   // Theme for dark mode
}
```

You can use published Prism themes or [create your own](https://github.com/PrismJS/prism-themes).

#### Custom Styles

The `styles` property allows injection of custom styles through two methods:

1. External Resources (type: 'link'):

```typescript
{
  key: 'google-fonts',
  type: 'link',
  value: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap'
}
```

2. Inline CSS (type: 'style'):

```typescript
{
  key: 'custom-theme',
  type: 'style',
  value: `
    .ikp-ai-chat-message {
      border-radius: 8px;
      padding: 12px;
    }
  `
}
```

Each style entry requires:

* `key`: A unique identifier to prevent duplicates and enable updates
* `type`: Either 'link' for external resources or 'style' for inline CSS
* `value`: The style content (URL for links or CSS code for styles)

#### Variables Class Name

The `varsClassName` property specifies the class name for the container that holds CSS variables:

```typescript
varsClassName: "ikp-variables"; // Default value
```

This class is added to a wrapper div that provides theming context.

## Color Mode Configuration

The color mode configuration allows you to control how the widget handles light and dark modes. This is configured through the `colorMode` property in the base settings:

```typescript
const baseSettings: InkeepBaseSettings = {
  colorMode: {
    // Force a specific color mode
    forcedColorMode?: string,

    // Enable system color mode detection
    enableSystem?: boolean,

    // Sync with external element
    sync?: {
      // Element to watch for color mode changes
      target: HTMLElement | string,

      // Attributes to monitor
      attributes: string[],

      // Function to determine dark mode
      isDarkMode: (attributes: Record<string, string | null>) => boolean,

      // Optional callback for color mode changes
      onChange?: (colorMode: string) => void
    }
  }
}
```

### Color Mode Properties

#### Forced Color Mode

Use `forcedColorMode` to explicitly set the color mode for the current page:

```typescript
colorMode: {
  forcedColorMode: "dark"; // Forces dark mode
}
```

#### System Color Mode

Enable `enableSystem` to automatically switch between dark and light modes based on the user's system preferences:

```typescript
colorMode: {
  enableSystem: true; // Follows system preference
}
```

#### Color Mode Sync

The `sync` property allows you to synchronize the widget's color mode with your application's theme:

```typescript
colorMode: {
  sync: {
    // Watch the document root for theme changes
    target: document.documentElement,

    // Monitor the data-theme attribute
    attributes: ['data-theme'],

    // Determine dark mode based on attribute value
    isDarkMode: (attrs) => attrs['data-theme'] === 'dark',

    // Optional: Handle color mode changes
    onChange: (mode) => console.log(`Color mode changed to: ${mode}`)
  }
}
```

Common sync configurations:

1. **Data Attribute Sync**:

```typescript
{
  target: document.documentElement,
  attributes: ['data-theme'],
  isDarkMode: (attrs) => attrs['data-theme'] === 'dark'
}
```

2. **Class-based Sync**:

```typescript
{
  target: document.documentElement,
  attributes: ['class'],
  isDarkMode: (attrs) => attrs['class']?.includes('dark-mode')
}
```

## Using CSS Variables

Inkeep provides a set of CSS variables that you can use to customize the widget's appearance. These variables are prefixed with `--ikp-` and are available within the scope of the widget.

### Basic Usage

You can use Inkeep CSS variables within your stylesheets to customize elements. For example:

```css
.ikp-chat-button__button {
  background: var(--ikp-colors-inkeep-primary-medium);
}
```

### Dark Mode Styling

To apply specific styles for dark mode, use the `[data-theme='dark']` attribute selector:

```css
[data-theme="dark"] .ikp-chat-button__button {
  background: #353e52;
}
```

## Customizing Icons

### AI Assistant Avatar

The AI assistant avatar can be customized through the `aiChatSettings` using the `aiAssistantAvatar` property:

it's either a string URL or an object to specify light and dark mode avatars:

```typescript
aiAssistantAvatar: {
  light: string;
  dark?: string;
}
```

### User Avatar

The user avatar can be customized using the `userAvatar` property in the `aiChatSettings`.

```typescript
import { type InkeepAIChatSettings } from "@inkeep/cxkit-react";

export const aiChatSettings: InkeepAIChatSettings = {
  aiAssistantAvatar: "http://example.com/assistant-avatar.png",
  userAvatar: "http://example.com/user-avatar.png",
  // ...rest of aiChatSettings
};
```

### Custom Icons

You can customize various icons throughout the widget by providing a `customIcons` dictionary in the `baseSettings`. Each icon can be either a built-in icon or a custom SVG/image.

#### Available Icons

| Icon Name           | Description                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------- |
| search              | Search icon in search bar                                                                    |
| thumbsUp            | Thumbs up icon                                                                               |
| thumbsDown          | Thumbs down icon                                                                             |
| messageCopy         | Copy message icon                                                                            |
| codeCopy            | Copy code icon in code header                                                                |
| openLinkInNewTab    | Used on hover in chat citations and search results (when `shouldOpenLinksInNewTab` is true)  |
| openLinkInSameTab   | Used on hover in chat citations and search results (when `shouldOpenLinksInNewTab` is false) |
| breadcrumbSeparator | Breadcrumb separator icon                                                                    |
| switchToSearch      | Switch to search icon                                                                        |
| switchToChat        | Switch to chat icon                                                                          |
| chatSubmit          | Chat submit icon                                                                             |
| close               | Close icon                                                                                   |
| info                | Info icon next to the disclaimer and chat mode toggle                                        |
| command             | Command icon in search bar                                                                   |

#### Example Configuration

```typescript
import { type InkeepBaseSettings } from "@inkeep/cxkit-react";

export const baseSettings: InkeepBaseSettings = {
  customIcons: {
    // Using a built-in icon
    search: {
      builtIn: "IoSearch",
    },

    // Using custom SVG/image URLs
    thumbsUp: {
      custom: "/path/to/thumbs-up.svg",
    },
    thumbsDown: {
      custom: "/path/to/thumbs-down.svg",
    },
    messageCopy: {
      custom: "/path/to/message-copy.svg",
    },
    codeCopy: {
      custom: "/path/to/code-copy.svg",
    },
    openLinkInNewTab: {
      custom: "path/to/open-link-in-new-tab.svg",
    },
    openLinkInSameTab: {
      custom: "path/to/open-link-in-same-tab.svg",
    },
    breadcrumbSeparator: {
      custom: "path/to/breadcrumb-separator.svg",
    },
    switchToSearch: {
      custom: "/path/to/switch-to-search.svg",
    },
    switchToChat: {
      custom: "/path/to/switch-to-chat.svg",
    },
    chatSubmit: {
      custom: "/path/to/chat-submit.svg",
    },
    close: {
      custom: "/path/to/close.svg",
    },
    info: {
      custom: "/path/to/info.svg",
    },
    command: {
      custom: "/path/to/command.svg",
    },
  },
  // ...rest of baseSettings
};
```

> If the url for a `custom` icon is a `.svg` file it will be rendered as an `<svg>`, all other file types will be rendered using an `<Image>` tag.

## Default Theme

The default theme includes these core settings:

### Typography

```typescript
fontFamily: {
  heading: "'Space Grotesk', system-ui, sans-serif",
  body: "'Inter', system-ui, sans-serif",
  mono: "'Fira Code', monospace",
},
fontSize: {
  '3xs': '0.45rem',
  '2xs': '0.625rem',
  xs: '0.75rem',
  sm: '0.875rem',
  md: '1rem',
  lg: '1.125rem',
  xl: '1.25rem',
  '2xl': '1.5rem',
  '3xl': '1.875rem',
  '4xl': '2.25rem',
  '5xl': '3rem',
  '6xl': '3.75rem',
  '7xl': '4.5rem',
  '8xl': '6rem',
  '9xl': '8rem',
}
```

### Z-Index

```typescript
zIndex: {
  hide: -1,
  auto: 'auto',
  base: 0,
  docked: 10,
  dropdown: 1000,
  sticky: 1100,
  banner: 1200,
  overlay: 1300,
  modal: 1400,
  popover: 1500,
  skipLink: 1600,
  toast: 1700,
  tooltip: 1800,
}
```

## Component Class Names

All component class names are prefixed with `ikp-`. Here's the complete list of available class names:

<>
  ### Chat Components

  ```css
  ikp-ai-chat-wrapper
  ikp-ai-chat-root
  ikp-ai-chat-header
  ikp-ai-chat-header__toolbar
  ikp-ai-chat-header__toolbar-header
  ikp-ai-chat-header__toolbar-header-wrapper
  ikp-ai-chat-content
  ikp-ai-chat-content-scroll-area
  ikp-ai-chat-content-scroll-area__viewport
  ikp-ai-chat-content-scroll-area__scrollbar
  ikp-ai-chat-content-scroll-area__thumb
  ikp-ai-chat-content-scroll-area__corner
  ikp-ai-chat-disclaimer
  ikp-ai-chat-disclaimer-label
  ikp-ai-chat-disclaimer-trigger
  ikp-ai-chat-disclaimer-content
  ikp-ai-chat-disclaimer-text
  ikp-ai-chat-disclaimer-arrow
  ikp-ai-chat-example-questions
  ikp-ai-chat-example-questions-label
  ikp-ai-chat-example-questions-list
  ikp-ai-chat-example-question
  ikp-ai-chat-example-question-button
  ikp-ai-chat-workflows
  ikp-ai-chat-workflows-label
  ikp-ai-chat-workflows-list
  ikp-ai-chat-workflow
  ikp-ai-chat-workflow__icon
  ikp-ai-chat-messages
  ikp-ai-chat-message-wrapper
  ikp-ai-chat-message-header
  ikp-ai-chat-message-loading
  ikp-ai-chat-message-avatar
  ikp-ai-chat-message-avatar-fallback
  ikp-ai-chat-message-avatar-image
  ikp-ai-chat-message-avatar-content
  ikp-ai-chat-message-name
  ikp-ai-chat-message-content-wrapper
  ikp-ai-chat-message-content
  ikp-ai-chat-message-attachments
  ikp-ai-chat-message-attachments__list
  ikp-ai-chat-message-attachments__item
  ikp-ai-chat-message-attachments__item-icon
  ikp-ai-chat-message-attachments__item-title
  ikp-ai-chat-message-attachments-preview
  ikp-ai-chat-message-attachments-preview__overlay
  ikp-ai-chat-message-attachments-preview__content
  ikp-ai-chat-message-attachments-preview__header
  ikp-ai-chat-message-attachments-preview__close
  ikp-ai-chat-message-attachments-preview__body
  ikp-ai-chat-message-part
  ikp-ai-chat-message-toolbar
  ikp-ai-chat-message-annotation-actions
  ikp-ai-chat-message-annotation-action
  ikp-ai-chat-message-action
  ikp-ai-chat-message-sources
  ikp-ai-chat-message-sources__header
  ikp-ai-chat-message-sources__list
  ikp-ai-chat-message-source-item
  ikp-ai-chat-message-source-item__icon
  ikp-ai-chat-message-source-item__breadcrumbs
  ikp-ai-chat-message-source-item__breadcrumb
  ikp-ai-chat-message-source-item__breadcrumb-icon
  ikp-ai-chat-message-source-item__title
  ikp-ai-chat-message-source-item__tag
  ikp-ai-chat-message-source-item__description
  ikp-ai-chat-message-source-item__description-part
  ikp-ai-chat-message-source-item__indicator
  ikp-ai-chat-footer
  ikp-ai-chat-input__fieldset
  ikp-ai-chat-input__group
  ikp-ai-chat-input
  ikp-ai-chat-input__send-button
  ikp-ai-chat-input__send-button-icon
  ikp-ai-chat-attachments-bar
  ikp-ai-chat-attachments-bar__list
  ikp-ai-chat-attachments-bar__attachment
  ikp-ai-chat-attachments-bar__attachment-icon
  ikp-ai-chat-attachments-bar__attachment-title
  ikp-ai-chat-attachments-bar__attachment-delete
  ikp-ai-chat-attachments-bar__actions
  ikp-ai-chat-attachments-bar__info-tip
  ikp-ai-chat-attachments-bar__info-tip-icon
  ikp-ai-chat-attachments-bar__info-tip-arrow
  ikp-ai-chat-attachments-bar__info-tip-text
  ikp-ai-chat-attachments-bar__inputs
  ikp-ai-chat-attachments-bar__input
  ikp-ai-chat-attachments-bar__input-icon
  ikp-ai-chat-attachments-bar__modal
  ikp-ai-chat-attachments-bar__modal-overlay
  ikp-ai-chat-attachments-bar__modal-content
  ikp-ai-chat-attachments-bar__modal-header
  ikp-ai-chat-attachments-bar__modal-close
  ikp-ai-chat-attachments-bar__modal-body
  ikp-ai-chat-attachments-bar__modal-heading
  ikp-ai-chat-attachments-bar__modal-description
  ikp-ai-chat-attachments-bar__modal-help
  ikp-ai-chat-attachments-bar__form
  ikp-ai-chat-attachments-bar__form-title
  ikp-ai-chat-attachments-bar__form-title-label
  ikp-ai-chat-attachments-bar__form-title-input
  ikp-ai-chat-attachments-bar__form-title-error
  ikp-ai-chat-attachments-bar__form-content
  ikp-ai-chat-attachments-bar__form-content-label
  ikp-ai-chat-attachments-bar__form-content-input
  ikp-ai-chat-attachments-bar__form-content-error
  ikp-ai-chat-attachments-bar__form-submit-button
  ikp-ai-chat-action-bar
  ikp-ai-chat__chat-actions
  ikp-ai-chat__chat-action
  ikp-ai-chat__chat-action-label
  ikp-ai-chat__chat-action-feeback
  ikp-ai-chat-help-actions
  ikp-ai-chat-help-action
  ikp-ai-chat-help-actions__trigger
  ikp-ai-chat-help-actions__menu
  ikp-ai-chat-help-actions__menu-arrow
  ikp-ai-chat-help-actions__menu-item
  ikp-ai-chat-help-actions_menu-item-icon
  ikp-ai-chat-tagline__container
  ikp-ai-chat-tagline__text
  ikp-ai-chat-tagline__logo
  ikp-ai-chat-tagline__brand-name
  ikp-ai-chat-feedback-modal
  ikp-ai-chat-feedback-modal__overlay
  ikp-ai-chat-feedback-modal__content
  ikp-ai-chat-feedback-modal__header
  ikp-ai-chat-feedback-modal__close
  ikp-ai-chat-feedback-modal__body
  ikp-ai-chat-feedback-form
  ikp-ai-chat-feedback-item
  ikp-ai-chat-feedback-item__checkbox
  ikp-ai-chat-feedback-item__checkbox-indicator
  ikp-ai-chat-feedback-item__label
  ikp-ai-chat-feedback-item__description
  ikp-ai-chat-feedback-form__submit-button
  ikp-ai-chat-form__wrapper
  ikp-ai-chat-form
  ikp-ai-chat-form__close
  ikp-ai-chat-form__header
  ikp-ai-chat-form__heading
  ikp-ai-chat-form__description
  ikp-ai-chat-form__content
  ikp-ai-chat-form__field
  ikp-ai-chat-form__field-label
  ikp-ai-chat-form__field-text
  ikp-ai-chat-form__field-email
  ikp-ai-chat-form__field-file
  ikp-ai-chat-form__field-text-area
  ikp-ai-chat-form__field-checkbox
  ikp-ai-chat-form__field-checkbox-indicator
  ikp-ai-chat-form__field-select
  ikp-ai-chat-form__field-select__trigger
  ikp-ai-chat-form__field-select__value
  ikp-ai-chat-form__field-select__icon
  ikp-ai-chat-form__field-select__content
  ikp-ai-chat-form__field-select__viewport
  ikp-ai-chat-form__field-select__item
  ikp-ai-chat-form__field-select__item-indicator
  ikp-ai-chat-form__field-select__item-text
  ikp-ai-chat-form__field-error
  ikp-ai-chat-form__error
  ikp-ai-chat-form__footer
  ikp-ai-chat-form__cancel
  ikp-ai-chat-form__submit
  ikp-ai-chat-form__success
  ikp-ai-chat-form__success-heading
  ikp-ai-chat-form__success-message
  ikp-ai-chat-form__success-button
  ikp-ai-chat-link
  ```

  ### Markdown Components

  ```css
  ikp-codeblock-container
  ikp-codeblock-header
  ikp-codeblock-header-language
  ikp-codeblock-copy-button
  ikp-codeblock-highlighter-wrapper
  ikp-codeblock-highlighter
  ikp-codeblock-code
  ikp-markdown-h1
  ikp-markdown-h2
  ikp-markdown-p
  ikp-markdown-li
  ikp-markdown-ul
  ikp-markdown-ol
  ikp-markdown-link
  ikp-markdown-source-link
  ikp-markdown-table
  ikp-markdown-th
  ikp-markdown-td
  ikp-markdown-code
  ikp-markdown-input
  ikp-markdown-sup
  ikp-markdown-img
  ikp-markdown-hr
  ```

  ### Search Bar Components

  ```css
  ikp-search-bar__container
  ikp-search-bar__button
  ikp-search-bar__content-wrapper
  ikp-search-bar__text
  ikp-search-bar__icon
  ikp-search-bar__kbd-wrapper
  ikp-search-bar__cmd-icon
  ikp-search-bar__ctrl
  ikp-search-bar__kbd-shortcut-key
  ```

  ### Modal Components

  ```css
  ikp-modal
  ikp-modal__overlay
  ikp-modal__content
  ikp-modal__close
  ```

  ### Chat Button Components

  ```css
  ikp-chat-button__text
  ikp-chat-button__button
  ikp-chat-button__container
  ikp-chat-button__avatar-image
  ikp-chat-button__avatar-content
  ikp-chat-button__close-icon
  ```

  ### Miscellaneous Components

  ```css
  ikp-icon
  ikp-loading-indicator__text
  ikp-loading-indicator__dots
  ikp-loading-indicator__dot
  ikp-view_toggle
  ikp-view_toggle_button
  ikp-view_toggle_icon
  ```
</>


# Artifact Components
URL: /visual-builder/structured-outputs/artifact-components

Artifact components are used to add artifacts to the Agent.

***

title: Artifact Components
description: Artifact components are used to add artifacts to the Agent.
icon: "TbInputSpark"
--------------------

<>
  Artifacts are structured components that capture and store source information when agents interact with tools or other agents. They act as a record-keeping system, automatically documenting where information comes from during tool and agent interactions.

  ## How Artifacts Work

  When an agent uses a tool (whether that's another agent or a utility tool), the response is automatically parsed to create artifacts. These artifacts store:

  * The source of the information (tool/agent used)
  * The relevant content from the response
  * Metadata about the interaction
</>

<Callout>
  **Quick Start**: Citation artifacts are automatically included when you create
  a new project with `npx @inkeep/create-agents`. You'll find the complete
  implementation in `artifact-components/citation.ts` in your project. They
  provide a ready-to-use example for source attribution (for example, when
  citing webpages) and are automatically rendered by the Inkeep widget with
  professional styling and interactions.
</Callout>

## How to create an artifact component

1. Go to the Artifact Components tab in the left sidebar. Then select "New artifact component".
2. Add in an id, name, and description. These are required fields.
3. For the props schema, you can either:
   * **Enter a JSON schema** with `inPreview: true` properties to define specific fields that will be immediately available
   * **Leave empty** to save the entire tool result without filtering
4. Click "Submit".

To visually add the artifact component to the Agent, see the [Sub Agents](/visual-builder/sub-agents#adding-artifact-components) page for details.

## Schema Requirements

<Callout type="warning">
  **Critical**: Your artifact schema must match your tool's output structure.
  The system uses JMESPath selectors on JSON - it **cannot extract from free
  text**.
</Callout>

```json
// ❌ WRONG: Tool returns text, schema expects structured data
// Tool output: { "result": { "content": [{ "text": "Weather: Sunny, 75°F" }] } }
{
  "type": "object",
  "properties": {
    "temperature": { "type": "number" }, // ❌ Cannot extract number from text
    "condition": { "type": "string" }     // ❌ Cannot extract condition from text
  }
}

// ✅ CORRECT: Tool returns structured data matching schema
// Tool output: { "result": { "temperature": 75, "condition": "Sunny" } }
{
  "type": "object",
  "properties": {
    "temperature": { "type": "number" },
    "condition": { "type": "string" }
  }
}
```

Use OpenTelemetry traces to debug schema validation issues.

### Preview Fields

Set `inPreview: true` on properties for immediate availability. These fields are:

* Shown to other agents for reasoning
* Streamed in real-time to clients (Vercel AI SDK)
* Auto-rendered by Inkeep's widget (citations as interactive cards)
* Available immediately in UI (full artifact loads on-demand)

For more details on how artifact data is streamed via the API, see [Data Artifact Events](/talk-to-your-agents/api#data-artifact-events).

**Example:**

```json
{
  "type": "object",
  "properties": {
    "title": {
      "description": "Title of the source document",
      "type": "string",
      "inPreview": true
    },
    "url": {
      "description": "URL of the source document",
      "type": "string",
      "inPreview": true
    },
    "record_type": {
      "description": "Type of record (documentation, blog, guide, etc.)",
      "type": "string",
      "inPreview": true
    },
    "content": {
      "description": "Array of structured content blocks extracted from the document",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "description": "Type of content (text, image, video, etc.)",
            "type": "string"
          },
          "text": {
            "description": "The actual text content",
            "type": "string"
          }
        },
        "required": ["type", "text"],
        "additionalProperties": false
      }
    }
  },
  "required": ["title", "url", "content", "record_type"],
  "additionalProperties": false
}
```

Citation artifacts that are named `citation` and have `title` and `url` preview fields are auto-rendered by Inkeep's widget in two ways:

* **Inline footnotes**: Numbered references \[1], \[2], etc. appear inline with the response text
* **Interactive cards**: Source cards with title, URL, and content appear below the response for detailed exploration

<Callout>
  **Important**: The artifact must have a name of `citation` in order to be
  auto-rendered by Inkeep's widget.
</Callout>

<Image src="/images/citation-widget-example.png" alt="Citation artifact rendered as an interactive card in the Inkeep widget showing source attribution" style={{ marginTop: "1rem" }} />

## Artifact Name & Description Generation

**Important**: Artifact names and descriptions are automatically generated at the **agent level** using that specific agent's configured **summarizer model**.

### How It Works

When an agent creates an artifact during tool execution or data processing:

1. **Agent Creates Artifact**: During tool execution or data processing
2. **Summarizer Analysis**: The agent's summarizer model analyzes:
   * The artifact content and structure
   * Recent conversation context
   * The user's original question or request
3. **Name Generation**: Creates a concise, descriptive name (max 50 characters)
4. **Description Generation**: Provides context about relevance and content (max 150 characters)

### Model Settings for Artifacts

Each agent uses its configured summarizer model for artifact generation:

```typescript
// Agent with custom summarizer for artifact generation
const researchAgent = subAgent({
  id: "research-agent",
  name: "Research Agent",
  prompt:
    "You are a research agent that can generate artifact names and descriptions",
  models: {
    base: { model: "anthropic/claude-sonnet-4-0" },
    summarizer: {
      model: "openai/gpt-4.1-mini", // This model generates artifact names/descriptions
      providerOptions: {
        temperature: 0.2, // Lower temperature for consistent naming
        maxOutputTokens: 512,
      },
    },
  },
});
```

### Inheritance and Fallback

Artifact generation follows the same model inheritance rules:

* **Default**: Sub Agent uses the Agent's summarizer model (if configured)
* **Fallback**: If no summarizer configured at project/agent level, falls back to Sub Agent's base model
* **Override**: Agent can specify its own summarizer model

### Best Practices

* **Consistent Models**: Use the same summarizer model across related agents for consistent artifact naming
* **Appropriate Models**: Choose models good at summarization (GPT-4o-mini, claude-3.5-haiku work well)
* **Temperature Settings**: Lower temperatures (0.1-0.3) provide more consistent naming patterns


# Create Rich UI Blocks with Data Components
URL: /visual-builder/structured-outputs/data-components

Learn how to create and use data components for rich, interactive Agent messages.

***

title: Create Rich UI Blocks with Data Components
sidebarTitle: Custom UI Blocks
description: Learn how to create and use data components for rich, interactive Agent messages.
icon: "LuBlocks"
----------------

<>
  ## What are Data Components?

  Data Components allow your agents to return rich, interactive content instead of just text. Think of them as reusable UI building blocks that your agent can populate with data.

  For example, instead of returning "You have 3 tasks: Task #123 (shipped), Task #124 (processing)...", your agent can return a properly formatted task list component.
</>

## How to create a data component

1. Go to the Data Components tab in the left sidebar. Then select "New data component".
2. Add in an id, name, and description. These are required fields.
3. Enter a JSON schema defining the structure of your data component.
4. Click "Submit".

To visually add the data component to the Agent, see the [Sub Agents](/visual-builder/sub-agents#adding-data-components) page for details.

### Example JSON Schema

```json
{
  "type": "object",
  "properties": {
    "tasks": {
      "type": "array",
      "description": "Array of user tasks",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string", "description": "Task ID" },
          "title": { "type": "string", "description": "Task title" },
          "completed": { "type": "boolean", "description": "Task status" }
        }
      }
    },
    "totalCount": { "type": "number", "description": "Total tasks" }
  }
}
```

## Frontend Integration

Create a React component matching your data component name:

```tsx
const TaskList = ({ tasks, totalCount }) => (
  <div className="task-list">
    <h3>Your Tasks ({totalCount} total)</h3>
    {tasks.map((task) => (
      <div key={task.id} className={task.completed ? "completed" : ""}>
        {task.title}
      </div>
    ))}
  </div>
);
```

Register it with the Inkeep chat component:

```tsx
<InkeepSidebarChat
  aiChatSettings={{
    agentUrl: "your-agent-url",
    components: {
      TaskList, // Component name must match data component name
    },
  }}
/>
```

The agent will automatically return structured data that renders as your React component.


# Status Components
URL: /visual-builder/structured-outputs/status-components

Configure intelligent status updates using structured components in the Visual Builder

***

title: Status Components
description: Configure intelligent status updates using structured components in the Visual Builder
icon: "LuClock"
---------------

The Visual Builder provides powerful tools for configuring status updates across your agents. These features keep users informed during long-running operations with structured component data.

## Default Status Updates

By default, status updates use built-in **default status components** that provide structured labels with contextual details:

* **Label**: User-friendly description like "Searching for information about your query..."
* **Details**: Structured data with operation context, tool usage, and progress information

These are generated automatically by your Agent's summarizer model and provide richer information than plain text summaries.

## Custom Status Components

Status components allow you to define structured data formats for your status updates instead of generic text. This enables richer, more interactive status displays in your UI.

### Creating Status Components

1. **Navigate to your Agent** in the Visual Builder
2. **Open Agent Settings** and find the "Status Updates" section
3. **Enable Status Updates** by configuring trigger conditions
4. **Add Status Components** to define structured update formats

### Example: Tool Call Status Component

Here's an example of a custom status component that provides structured information about tool executions:

```typescript
// Tool Call Summary Component
{
  type: 'tool_call_summary',
  description: 'Summary of a tool execution and its results',
  detailsSchema: {
    type: 'object',
    properties: {
      tool_name: {
        type: 'string',
        description: 'Name of the tool that was executed'
      },
      summary: {
        type: 'string',
        description: 'Brief description of what was accomplished'
      },
    },
    required: ['tool_name', 'summary']
  }
}
```

With this component, instead of generic text, you get structured data like:

```json
{
  "tool_name": "search_knowledge_base",
  "summary": "Found 5 relevant articles about API authentication",
  "duration": 1250
}
```

## AI-Powered Status Generation

Status updates are generated using your Agent's configured **summarizer model**, which analyzes recent agent activity and creates contextual progress messages.

### How It Works

1. **Event Tracking**: The system monitors all agent operations (tool calls, transfers, generations)
2. **Intelligent Triggering**: Updates are sent based on event count or time intervals
3. **AI Analysis**: The summarizer model analyzes recent events and conversation context
4. **Output Generation**: Creates structured status updates with labels and contextual details

### Status Update Modes

* **Default Status Components**: Built-in structured format with `label` and `details` fields
* **Custom Status Components**: Your defined schemas for specific data structures

### Summarizer Model Settings

The summarizer model is configured in your Agent's model settings:

```typescript
// Agent-level model settings
models: {
  base: {
    model: 'anthropic/claude-sonnet-4-5' // Primary model
  },
  summarizer: {
    model: 'openai/gpt-4.1-mini', // Dedicated summarizer
    providerOptions: {
      temperature: 0.3, // Lower temperature for consistent summaries
      maxOutputTokens: 1024
    }
  }
}
```

## Visual Builder Configuration

### Agent-Level Setup

1. **Select your Agent** in the Visual Builder

2. **Open Model Settings**:

   * Set base model for agent conversations
   * Configure summarizer model for status updates
   * Adjust provider options (temperature, tokens)

3. **Configure Status Updates**:
   * **Trigger Events**: Number of operations before sending update
   * **Time Interval**: Seconds between time-based updates
   * **Custom Status Updates Prompt**: Additional context for the summarizer (max 2000 characters)

### Status Updates Prompt

You can provide a custom prompt that gets appended to the base system prompt for status generation. This allows you to:

* Customize the tone and style of status messages
* Add domain-specific context
* Guide the summarizer to focus on particular aspects

```typescript
statusUpdates: {
  numEvents: 3,
  timeInSeconds: 15,
  prompt: `Focus on user-visible progress and avoid technical details.
Keep messages encouraging and professional.
Always mention what information is being found or processed.`
}
```

### Status Component Designer

Use the visual component designer to create structured status updates:

1. **Component Properties**: Define the data structure
2. **Schema Validation**: Ensure consistent output format
3. **Preview Mode**: Test how components will appear
4. **Template Customization**: Style the component display

## Inheritance and Configuration

### Agent-Level Defaults

Status components, summarizer models, and status update prompts are configured at the agent level and apply to all sub-agents in that agent.

## Best Practices

### Model Selection

* **Summarizer Model**: Faster, efficient models (GPT-4.1-mini, Claude-3.5-Haiku) work well for status generation
* **Consistency**: Use the same summarizer across related agents for consistent status updates

### Status Component Design

* **Specific Schemas**: Define precise data structures for reliable output
* **Required Fields**: Mark essential properties as required
* **Descriptive Names**: Use clear component IDs and descriptions

### Custom Prompts

* **Keep it Concise**: Status update prompts are limited to 2000 characters
* **Be Specific**: Guide the model toward the type of information you want highlighted
* **User-Focused**: Emphasize user-visible progress over technical details

### Performance Optimization

* **Event Thresholds**: Balance responsiveness with API usage (3-5 events typically work well)
* **Time Intervals**: Adjust based on typical operation duration (10-30 seconds)
* **Model Efficiency**: Choose cost-effective models for high-frequency status generation

## Next Steps

* [Configure Data Components](/visual-builder/structured-outputs/data-components) for structured agent outputs
* [Set up Artifact Components](/visual-builder/structured-outputs/artifact-components) for rich content handling
* [Manage Credentials](/visual-builder/tools/credentials) for external tool access


# Manage Credentials in Visual Builder
URL: /visual-builder/tools/credentials

Credentials are used to authenticate MCP servers.

***

title: Manage Credentials in Visual Builder
sidebarTitle: Credentials
description: Credentials are used to authenticate MCP servers.
icon: "LuKey"
-------------

The credentials page allows you to add credentials to your MCP servers.

## Adding a credential

<>
  Make sure your Visual Builder is running (if you haven't set it up yet, see [Quick Start](/get-started/quick-start)). Navigate to the Credentials tab in the left sidebar, click "New credential", and select "Bearer authentication".

  1. Fill in the required credential details:

  | Field     | Description                                                         |
  | --------- | ------------------------------------------------------------------- |
  | `Name`    | A descriptive name for your credential (e.g., "production-api-key") |
  | `API key` | The authentication token or API key for the service                 |

  2. Optionally, configure additional settings:

  | Field                | Description                                                                                                                                                                                               |
  | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `Metadata`           | Additional headers to include with authentication requests (e.g., User-Agent, X-API-Key). Only available for Nango Store.                                                                                 |
  | `Credential store`   | Where to securely store the credential. Choose from available stores ([Nango Store](/typescript-sdk/tools/credentials#nango-store) or [Keychain Store](/typescript-sdk/tools/credentials#keychain-store)) |
  | `Link to MCP server` | Optionally associate this credential with a specific MCP server that does not have a credential configured                                                                                                |

  3. Click "Create Credential" to save the credential.
</>

To use the credential in an MCP server, you can reference it when creating or editing the MCP server. See the [MCP Servers](/visual-builder/tools/mcp-servers) page for more information.

***


# Function Tools
URL: /visual-builder/tools/function-tools

Create custom JavaScript functions that your agents can execute directly in the Visual Builder

***

title: Function Tools
description: Create custom JavaScript functions that your agents can execute directly in the Visual Builder
icon: "LuCode"
--------------

Function tools allow you to create custom JavaScript functions that agents can execute in secure sandboxes. Unlike [MCP servers](/visual-builder/tools/mcp-servers) that connect to external services, function tools run your own code directly within the agent framework.

## Overview

Function tools are ideal for:

* **Custom business logic** - Implement domain-specific calculations or workflows
* **Data processing** - Transform, validate, or analyze data using JavaScript
* **API integrations** - Connect to services that don't have MCP servers
* **Utility functions** - Create reusable helper functions across your agents

## Creating Function Tools

Function tools are created within an Agent and can be used by multiple Sub Agents in that Agent.

### In an Agent

1. **Add a Function Tool Node**: In the Agent editor, drag a "Function Tool" node from the node palette onto the canvas

2. **Configure the Function Tool**: Click on the function tool node to open the configuration panel in the right sidebar:

| Field          | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| `Name`         | A unique name for your function tool (e.g., "calculate\_tax") |
| `Description`  | What the function does and when to use it                     |
| `Code`         | The JavaScript function code to execute                       |
| `Input Schema` | JSON Schema defining the function parameters                  |
| `Dependencies` | NPM packages required by your function                        |

3. **Connect to Agents**: Drag from the function tool node to any agent nodes that should have access to this tool

<Image
  src="/images/function-tool-node-editor.png"
  alt="Function Tool Node Editor"
  style={{
  border: "1px solid #e1e5e9",
}}
/>

### Function Code

Write your JavaScript function in the Code editor. The function receives arguments based on your Input Schema and should return a result:

```javascript
// Example: BMI calculator
function calculateBMI({ weight, height }) {
  const bmi = weight / (height * height);
  let category = "Normal";
  if (bmi < 18.5) category = "Underweight";
  else if (bmi >= 30) category = "Obese";

  return { bmi: Math.round(bmi * 10) / 10, category };
}

return calculateBMI(args);
```

<Note>Code can be synchronous aor asynchronous, we accept any flavor.</Note>

### Input Schema

Define the parameters your function accepts using JSON Schema. This ensures proper validation and helps agents understand how to use your function:

```json
{
  "type": "object",
  "properties": {
    "weight": {
      "type": "number",
      "description": "Weight in kilograms"
    },
    "height": {
      "type": "number",
      "description": "Height in meters"
    }
  },
  "required": ["weight", "height"]
}
```

The Visual Builder provides syntax highlighting and validation for your JSON schema.

### Dependencies

If you need external packages for your code to run, then specify the desired version in dependencies; otherwise we always use the latest version.

```javascript
// Dependencies auto-detected from impports
const axios = require("axios"); // latest axios version
const lodash = require("lodash"); // Uses latest lodash version
```

**Manual Override**: Specify dependencies in the Dependencies field to pin to specific versions:

```json
{
  "axios": "1.6.0",
  "lodash": "4.17.21"
}
```

## Example: Weather API Integration

Here's a complete example of a function tool that fetches weather data:

**Name**: `get_current_weather`

**Description**: `Get current weather information for any city using OpenWeatherMap API`

**Code**:

```javascript
// Simple weather lookup example
async function getWeather({ city }) {
  const axios = require("axios");
  const response = await axios.get(`https://api.weather.com/city/${city}`);

  return {
    city: response.data.city,
    temperature: response.data.temp,
    description: response.data.weather,
  };
}

return getWeather(args);
```

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string",
      "description": "City name"
    }
  },
  "required": ["city"]
}
```

**Dependencies**:

```json
{
  "axios": "^1.6.0"
}
```

## Execution Environment

Function tools run in secure, isolated sandboxes that provide a safe execution environment for your code.

### Sandbox Execution

Functions execute with the following characteristics:

* **Isolated execution** - Each function runs in its own sandbox
* **No file system access** - Cannot read or write outside the sandbox
* **Network access** - Only through explicitly declared dependencies (like axios)
* **Resource limits** - CPU, memory, and execution time constraints enforced
* **Stateless execution** - No data persists between function calls

### Runtime Options

When deploying, you can configure:

* **Runtime**: Node.js 22 or TypeScript
* **Timeout**: Maximum execution time per function call
* **Concurrency**: Number of simultaneous function executions

See [Deploy to Vercel](/self-hosting/vercel#function-tools-with-vercel-sandbox) for deployment-specific configuration.

### Best Practices

* **Keep functions simple** - Each function should have a single, clear purpose
* **Minimize dependencies** - Only include packages you actually need for better performance
* **Handle errors** - Always catch and return meaningful error messages
* **Test thoroughly** - Test your functions independently before deploying
* **Clear descriptions** - Write descriptive names and descriptions to help agents use tools effectively

Function tools provide powerful customization capabilities while maintaining security and performance through sandboxed execution.


# Register MCP Servers in Visual Builder
URL: /visual-builder/tools/mcp-servers

Create MCP servers that agents can use to access external services.

***

title: Register MCP Servers in Visual Builder
sidebarTitle: MCP Servers
description: Create MCP servers that agents can use to access external services.
icon: "LuServer"
----------------

MCP servers provide tools that your agents can use to interact with external APIs and services. Once created, these servers are automatically synced to discover available tools, which can then be added to your agents.

<>
  To use MCP servers with your agents, you can:

  * **Connect to Native MCP servers** from providers like Atlassian, Linear, Notion, and more
  * **Use Composio's platform** for access to 10,000+ out-of-box MCP servers
  * **Use Gram** to easily convert existing OpenAPI APIs into MCP Servers
  * **Build Custom MCP servers** for totally custom MCP servers

  See the [MCP Servers tutorial](/tutorials/mcp-servers/overview) for details on all recommended approaches.

  Once you have access to an MCP server, you can register it with your agents.
</>

## Register an MCP server

1. Go to the **MCP Servers** tab in the left sidebar, then select "New MCP server".

2. Fill in the required server details:

| Field            | Description                         |
| ---------------- | ----------------------------------- |
| `Name`           | Server name                         |
| `URL`            | Endpoint URL of a remote MCP server |
| `Transport Type` | Streamable HTTP or SSE protocol     |

3. Optionally, configure additional settings:

| Field        | Description                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Image URL`  | Custom icon for the server (URL or base64 data URL)                                                                                                                                                                                                    |
| `Credential` | Authentication credential if the server requires it. Choose from existing credentials, or leave blank and add a credential later. For OAuth 2.1/PKCE flows, leave blank and use the `Click to Login` button in the server details page to authenticate |

4. Click "Create" to create the server.

## Viewing server details

After creating an MCP server, you can view its details:

1. Click on your created MCP server from the list
2. The server details page shows:
   * **Server information** - URL, transport type, creation date, etc.
   * **Status** - healthy, unhealthy, unknown, disabled, or shows a "Click to Login" button if OAuth 2.1/PKCE flow is detected
   * **Active tools** - Currently enabled tools for the server
   * **Available tools** - All tools discovered from the server with descriptions and parameters

<Image
  src="/images/mcp-server-healthy-status.png"
  alt="MCP server healthy status"
  width="60%"
  style={{
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

<Note>
  Tool discovery requires a successful connection to the MCP server. If the
  server shows "Click to Login" in the status, use the button to initiate the
  authentication process.
</Note>

## Editing server settings

To modify an existing MCP server:

1. From the server details page, click the **Edit** button
2. The edit form shows all the same fields as creation, plus the ability to update **Active Tools**. By default, all available tools are enabled. You can select specific tools to enable.
3. Click **Save** to apply changes

<Image
  src="/images/mcp-server-edit-form.png"
  alt="MCP server healthy status"
  width="60%"
  style={{
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

## Authentication setup

If your MCP server requires authentication, you have two options: either use the **"Click to Login"** button to authenticate or manually create a credential to use with the MCP server.

### OAuth 2.1/PKCE authentication

1. Create your MCP server without selecting a credential
2. Go to the server details page and click the **"Click to Login"** button
3. Complete the OAuth authentication flow in your browser
4. The credential will be automatically created and saved to your [Nango Store](/typescript-sdk/tools/credentials#nango-store) (follow steps to [setup Nango](/get-started/credentials)). If Nango is not set up, the framework will use the [Keychain Store](/typescript-sdk/tools/credentials#keychain-store) if available.

<Image
  src="/images/mcp-server-click-to-login.png"
  alt="MCP server click to login"
  width="60%"
  style={{
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

#### 1-click Install MCP servers

<>
  Here's an example list of popular service-maintained MCP Servers that support **1-click** install via the OAuth 2.1/PKCE authentication flow.

  | Name                                                                                                             | URL                                                                  |
  | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
  | [Atlassian (SSE)](https://support.atlassian.com/rovo/docs/getting-started-with-the-atlassian-remote-mcp-server/) | [https://mcp.atlassian.com/v1/sse](https://mcp.atlassian.com/v1/sse) |
  | [Canva](https://www.canva.dev/docs/connect/canva-mcp-server-setup/)                                              | [https://mcp.canva.com/mcp](https://mcp.canva.com/mcp)               |
  | [Hugging Face](https://huggingface.co/mcp)                                                                       | [https://huggingface.co/mcp?login](https://huggingface.co/mcp?login) |
  | [Intercom](https://developers.intercom.com/docs/guides/mcp)                                                      | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp)         |
  | [Linear](https://linear.app/docs/mcp)                                                                            | [https://mcp.linear.app/mcp](https://mcp.linear.app/mcp)             |
  | [Neon](https://neon.com/docs/ai/neon-mcp-server)                                                                 | [https://mcp.neon.tech/mcp](https://mcp.neon.tech/mcp)               |
  | [Notion](https://developers.notion.com/docs/get-started-with-mcp)                                                | [https://mcp.notion.com/mcp](https://mcp.notion.com/mcp)             |
  | [Prisma](https://www.prisma.io/docs/postgres/integrations/mcp-server#remote-mcp-server)                          | [https://mcp.prisma.io/mcp](https://mcp.prisma.io/mcp)               |
  | [Sentry](https://docs.sentry.io/product/sentry-mcp/)                                                             | [https://mcp.sentry.dev/mcp](https://mcp.sentry.dev/mcp)             |
  | [Vercel](https://vercel.com/docs/mcp/vercel-mcp)                                                                 | [https://mcp.vercel.com](https://mcp.vercel.com)                     |

  To add them to your project:

  1. navigate to **MCP Servers** in the Inkeep Visual Builder.
  2. Click on **New MCP Server**
  3. Choose from the preset list under **Popular Services** or register any under **Custom Server**

  When you register the server, an authentication pop-up will appear and allow you to sign in. Your credentials will automatically be saved to your [Nango Store](/typescript-sdk/credentials/nango) or [Keychain](/typescript-sdk/credentials/keychain) credential store.
</>

### Manual credential setup

1. Create a credential in the [Credentials](/visual-builder/tools/credentials) section. The credential can be API Key, Bearer Token, Basic, OAuth 2.0, etc.
2. When creating or editing your MCP server, select the credential from the dropdown
3. The credential will be automatically used when connecting to the server

## Finding more remote MCP servers

For additional remote MCP servers you can connect to:

* **[Anthropic's Remote MCP Servers](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers)** - Official documentation with curated third-party remote servers
* **[Awesome Remote MCP Servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - Community-curated list of high-quality remote MCP servers

## Using stdio-based MCP servers

The Visual Builder requires **Streamable HTTP or SSE transport** to connect to MCP servers. If you have an MCP server that runs in **stdio mode** locally, you can use the following setup to connect to it.

### Setup outline

1. **Deploy your stdio -> Streamable HTTP/SSE bridge** (locally or cloud)
2. **Set environment variables** (API tokens, etc.)
3. **Verify it's running** (i.e. on port `4000`, `4001`, etc.)
4. **Add to Visual Builder**:
   * **URL**: `http://localhost:4000/mcp` (or your server URL)
   * **Transport Type**: `Streamable HTTP` or `SSE`

### Example using `mcp-proxy`

1. Get familiar with [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) - proxy for MCP servers that use stdio transport
2. [Supabase MCP server](https://github.com/supabase-community/supabase-mcp)
3. Run the server locally:

```bash
SUPABASE_ACCESS_TOKEN=YOUR_SUPABASE_ACCESS_TOKEN mcp-proxy --port 4444 --shell "npx -y @supabase/mcp-server-supabase@latest --read-only"
```

4. Add to Visual Builder with the following settings:
   * **URL**: `http://localhost:4444/mcp`
   * **Transport Type**: `Streamable HTTP`

## Adding servers to agents

Once you have created an MCP server, you can add it to your agents:

1. Go to the [Sub Agents](/visual-builder/sub-agents) page
2. Drag and drop an MCP server into your agent
3. Connect the MCP server to a Sub Agent by dragging from the server's connector to the Sub Agent
4. Your Sub Agent can now use the tools provided by that MCP server

<Image
  src="/images/mcp-server-add-to-agent.png"
  alt="MCP server add to agent"
  width="60%"
  style={{
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

For detailed instructions on working with MCP servers in agents, see the [Sub Agents](/visual-builder/sub-agents#adding-tools) page.
