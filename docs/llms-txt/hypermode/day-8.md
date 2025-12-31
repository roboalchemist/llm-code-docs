# Source: https://docs.hypermode.com/agents/30-days-of-agents/day-8.md

# Day 8: Connections & Tools

> Give your agent the tools it needs to accomplish its goals

<Card title="Day 8 challenge" icon="link">
  **Goal**: provide the tools your agent needs to accomplish its goals

  **Theme**: community week - enabling agent capabilities

  **Time investment**: \~20 minutes
</Card>

Welcome to Day 8! Yesterday you created your first custom agent with Concierge.
Today we're diving deep into **connections and tools**—the integration ecosystem
that transforms chatbots into powerful agents. You'll learn to connect services
and understand what specific tools become available for your agent to use.

This is where agents evolve from helpful assistants to business-critical
automation.

## What you'll accomplish today

* Configure your deployed agent with the right connections
* Master the agent configuration interface and customization options
* Understand connection authorization flow and management
* Learn the difference between connections and tools
* Explore your agent's specific tool capabilities with its new connections
* Learn to iterate on agent instructions and model selection

<Warning>
  This builds on Day 7's agent creation. You'll need the custom agent you
  deployed yesterday to complete today's configuration and workflow development.
</Warning>

## Understanding connections and tools

Before diving into configuration, it's important to understand the distinction:

<Info>
  **Connection**: the authenticated integration to a service (for example: "Google sheets connection")

  **Tools**: the specific actions your agent can perform once connected (for
  example: "create spreadsheet", "update row", "fetch data")
</Info>

{/* <!-- trunk-ignore(markdownlint/MD036) --> */} **Google Sheets**

* **Connection**: OAuth authentication to your Google account
* **Tools unlocked**: Create, edit, and manage spreadsheets, rows, and data.

{/* <!-- trunk-ignore(markdownlint/MD036) --> */} **GitHub**

* **Connection**: Authentication to your GitHub account
* **Tools unlocked**: Create and manage repositories, pull requests, issues, and
  more.

This distinction helps you understand what capabilities your agent gains from
each connection you enable.

## Step 1: Explore your agent's configuration interface

Your agent from yesterday is now deployed in your sidebar, but let's dive into
its configuration options. The agent interface gives you powerful customization
capabilities.

<img className="w-2/3 mx-auto" src="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=a95e134374ce529d5d87d2b0130e8d06" alt="Agent About View" width="1902" height="1940" data-path="images/agents/30-days-of-agents/day-8-agent-about.png" srcset="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?w=280&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=0891ba680cc55c4bd4e764c533fb10f8 280w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?w=560&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=ef9a37c64f80d75e6c4bd63bbafd5062 560w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?w=840&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=4b06945ed301ccc6656e2c557efdb165 840w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?w=1100&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=e95ff9e9bed6d3e19b28956dca2ceb85 1100w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?w=1650&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=ff5090ec8d65137e388b72047ad752f0 1650w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-about.png?w=2500&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=68d339b7331199d8585b4285fc40d57e 2500w" data-optimize="true" data-opv="2" />

**Access your agent's configuration:**

1. **Click on your agent** in the sidebar to open its thread view
2. **Click the agent's name** at the top to access the "About" section
3. **Review the agent details** including its description, instructions, and
   current model

**Key configuration options available:**

* **Agent Instructions**: Edit the system prompt that guides your agent's
  behavior
* **Model Selection**: Currently set to GPT-4.1 (default), but you can
  experiment with other models
* **Agent Description**: Update how your agent presents itself
* **Connection Management**: Add and configure the services your agent can
  access

<Tip>
  **Customization power**: you have full control over your agent's instructions
  and model. GPT-4.1 is the default and works great for most use cases, but you
  can experiment with different models or collaborate with us on Discord to find
  what works best for your specific needs.
</Tip>

<Tip>
  **Model awareness**: not all models support tool use. GPT-4.1 is the most
  capable for this purpose, but you can experiment with others if you want to
  explore different behaviors.
</Tip>

## Step 2: Configure agent-specific connections

Now let's give your agent access to the services it needs. There are two types
of connections: **agent connections** (specific to your agent) and **workspace
connections** (shared across all agents). Let's start with agent-specific
connections.

<img className="w-2/3 mx-auto" src="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=5bbcf3f16f9cfa9a9c16955fe729b04b" alt="Agent Connections View" width="986" height="1918" data-path="images/agents/30-days-of-agents/day-8-agent-connections.png" srcset="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?w=280&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=157f7a59531faea23c1f9dde94475c64 280w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?w=560&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=2ba22b2a719fadbf3c5608d72b8df908 560w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?w=840&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=3ca7027ce42546bb8154c2849e0f2dd3 840w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?w=1100&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=d1b9ba64f8ef8a15dd983bdd82beca98 1100w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?w=1650&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=ce9907cf507a0d4715be24586808ac30 1650w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day-8-agent-connections.png?w=2500&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=461d523178a4ea234917132a377352fb 2500w" data-optimize="true" data-opv="2" />

**Configure agent connections:**

1. **Navigate to your agent** by clicking it in the sidebar
2. **Click the agent's name** at the top to open the About section
3. **Click the Connections tab** to see available connections for this agent
4. **Browse available connections** or search for specific services your agent
   needs
5. **Click "Add Connection"** for services that align with your agent's purpose
6. **Complete the OAuth flow** when prompted for authentication
7. **Verify successful connection** with the green checkmark indicator

<Info>
  **Agent connections are specific**: connections you add here are only
  available to this particular agent. If you want connections available to all
  agents in your workspace, you'll need to configure workspace connections
  (covered in Step 3).
</Info>

**Connection selection strategy:**

Think about what your agent was designed to do (from Day 7) and add connections
that support those capabilities. For example:

* **Code-related agents**: GitHub connection (unlocks repository management, PR
  creation tools)
* **Marketing agents**: HubSpot connection (unlocks CRM management, campaign
  tracking tools)
* **Research agents**: Google Drive connection (unlocks document access,
  creation tools)
* **Operations agents**: Google Sheets connection (unlocks spreadsheet
  management, data analysis tools)

<Tip>
  **Connection vs. Tools reminder**: when you add a Google Sheets connection,
  you're not just connecting to Google Sheets—you're unlocking specific tools
  like "create spreadsheet," "update row," and "analyze data." Each connection
  provides multiple tools for your agent to use.
</Tip>

<Info>
  **Start focused**: add 2-3 connections initially rather than overwhelming your
  agent with too many options. You can always add more as you discover new use
  cases.
</Info>

## Step 3: Configure workspace-level connections

In addition to agent-specific connections, you can configure workspace
connections that are shared across all agents in your workspace.

<img src="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=3a3505437e387232f1de1eca6122f3ae" alt="Connections Management" width="2572" height="1020" data-path="images/agents/connections-manage.png" srcset="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=280&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=482281b2dbafc51f7120d559efc2cc91 280w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=560&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=66ae48f1052f6fa3f5589173fae93bed 560w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=840&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=e70bf6c755a3a2d0cfeb63e512593aae 840w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=1100&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=9d8f4aac8cc5865cb156105c1a205002 1100w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=1650&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=20dd5055918aded0f46f934492147382 1650w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=2500&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=fef4c23dcb54a178701d3161efb58f48 2500w" data-optimize="true" data-opv="2" />

**Configure workspace connections:**

1. **Navigate to Workspace Settings** from your profile menu (click your avatar
   in the top right)
2. **Click the Connections tab** to see all available workspace-wide
   integrations
3. **Add connections** that multiple agents might need to share
4. **Complete authentication** for each service you connect
5. **Manage authentication status** and review permissions

<Info>
  **When to use workspace vs. agent connections**: - **Workspace connections**:
  for services that multiple agents need to access (like company Google Drive or
  Slack) - **Agent connections**: for services specific to one agent's role
  (like a specific GitHub repository for a code agent)
</Info>

<Tip>
  **Connection hierarchy**: agents can use both their specific connections and
  any workspace connections. This gives you flexibility in how you organize
  access across your team.
</Tip>

## Step 4: Test your agent's new tool capabilities

Now that your agent has connections, let's explore what specific tools it can
use. Start with simple requests to understand how it uses its new capabilities.

**Test basic tool awareness:**

```text
What connections do you have access to now? What specific tools can you use with each connection?
```

Your agent can:

* **List available connections** and explain the services it can access
* **Describe specific tools** it can use with each connection
* **Suggest workflows** based on your agent's role and available tools

**Try a simple task:**

```text
Can you help me with [specific task related to your agent's purpose]?
Use whatever tools you think are most appropriate.
```

Watch how your agent:

* **Evaluates available tools** for the task at hand
* **Plans its approach** using the specific tools you've provided
* **Executes actions** across the integrated services
* **Reports results** and suggests next steps

<Tip>
  **Discovery approach**: rather than prescribing specific workflows, let your
  agent show you what's possible. Ask open-ended questions about what it can
  help you accomplish with its current tools.
</Tip>

## Step 5: Customize your agent's instructions and model

The configuration interface gives you direct control over your agent's behavior.
You can edit the agent's prompt and experiment with different models right from
the About section.

**Direct customization options:**

1. **Edit Agent Instructions**: Click "Edit" to modify the system prompt that
   guides your agent's behavior
2. **Change Model Selection**: Switch from the default GPT-4.1 to experiment
   with other models
3. **Update Description**: Adjust how your agent presents itself

**When to customize:**

* **Tool usage patterns**: Guide which tools to prioritize for specific tasks
* **Tone adjustments**: Make the agent more formal, casual, technical, or
  business-focused
* **Process preferences**: Specify how the agent should approach tasks
* **Communication style**: Adjust how the agent reports progress and results

**Model experimentation:**

GPT-4.1 is the default and works great for most use cases, but you can
experiment with different models based on your needs. If you're unsure about
optimization, collaborate with us on Discord to find what works best for your
specific requirements.

<Info>
  **Direct control**: unlike other platforms, you have full access to customize
  your agent's instructions and model selection. This gives you complete control
  over behavior and performance.
</Info>

## What you've accomplished

In 20 minutes, you've mastered agent configuration and tool enablement:

**Interface mastery**: learned to navigate and customize your agent through the
About section, including instructions and model selection

**Connection configuration**: successfully added agent-specific connections
through the agent's Connections tab and learned to configure workspace-wide
connections through Workspace Settings

**Tool capability exploration**: tested your agent's new abilities and
discovered what specific tools are available with each connection

**Direct customization**: learned to edit agent instructions and experiment with
different models for optimal performance

**Optimization awareness**: understand when and how to get community support for
advanced optimization

## The transformation from advisor to executor

Today's work establishes the foundation for powerful agent automation:

**Before connections**: your agent could only provide advice and suggestions
based on its training

**After connections**: your agent can take real actions with specific tools,
access live data, and integrate with your actual workflows and business systems

This transformation from "advisor" to "executor" is what makes Hypermode Agents
different from traditional AI assistants.

<Card title="Tomorrow - Day 9" icon="arrow-right" href="/agents/30-days-of-agents/day-9">
  Transform your successful interactions into reusable tasks. Learn to capture
  institutional knowledge and scale your agent's capabilities across your
  organization.
</Card>

## Pro tip for today

Now that your agent has connections and tools, spend some time exploring:

```text
What are some creative ways I could use the specific tools you now have access to?
What would be most valuable for me to automate or streamline in my current work?
```

Let your agent guide you toward discovering workflows that you might not have
considered, based on its understanding of the tools now available.

***

**Time to complete**: \~20 minutes

**Skills learned**: agent configuration interface, connection management for
both agent-specific and workspace connections, understanding connections vs.
tools, agent instruction editing, model selection, tool capability exploration
and testing

**Next**: day 9 - Create reusable tasks from successful workflows

<Tip>
  **Remember**: today was about setting up your agent's foundation. The real
  magic happens when you start using these tools in creative ways. Let your
  agent surprise you with what becomes possible when it has the right tools to
  work with.
</Tip>
