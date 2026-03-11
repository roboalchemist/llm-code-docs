# Source: https://docs.base44.com/Getting-Started/ai-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building an AI agent

> Build and deploy AI agents that manage tasks, monitor workflows, and act across your tools.

Build your own autonomous AI agent in Base44. An AI agent is a persistent assistant that can observe events, reason about information, and take action across your tools and systems.

Use an agent to monitor activity, connect to services, and automate workflows across your workspace. For example, your agent can watch for important emails, summarize Slack alerts, generate reports, or trigger actions when something changes.

<Frame caption="Building your personal AI agent">
    <img src="https://mintcdn.com/base44/W_eW1s6fjQwx9FSP/images/aiagentpage.png?fit=max&auto=format&n=W_eW1s6fjQwx9FSP&q=85&s=c773c94f441ba30135e3aecf4427c0b0" alt="Building your personal AI agent." width="1128" height="615" data-path="images/aiagentpage.png" />
</Frame>

<Note>
  **AI Agent** is currently rolling out and may not yet be available in all Base44 workspaces.
</Note>

<Card icon="robot" title="What your AI agent can do">
  Your AI agent can perform a wide range of tasks, including:

  * Monitor systems and respond to events automatically.
  * Run scheduled tasks and recurring workflows.
  * Connect to external tools such as Slack, Google Calendar, and GitHub.
  * Communicate through messaging channels.
  * Access knowledge and stored files to reason about problems.
  * Trigger actions such as sending alerts, updating data, or generating reports.
  * Search the web, gather information, and open live previews while researching topics.
</Card>

***

## Planning your AI agent

Before building your agent, decide what you want your agent to help you with.

**Typical workflow for building your first AI agent:**

<Steps>
  <Step title="Define the goal">
    Start by describing what you want the agent to help with.

    **For example:**

    * Monitor my Gmail inbox and summarize important emails.
    * Check Slack messages in #alerts and notify me if something looks critical.
    * Generate a daily summary of GitHub activity.
  </Step>

  <Step title="Connect your tools">
    Enable the relevant connectors so your agent can read data or trigger actions.
  </Step>

  <Step title="Add knowledge or context">
    Provide instructions, documents, or memory so the agent understands how to behave and make decisions.
  </Step>

  <Step title="Automate tasks">
    Create scheduled tasks so the agent can run workflows automatically, such as sending summaries or monitoring activity.
  </Step>
</Steps>

<Tip>
  Not sure what to try first? Start with something you already do every day, such as monitoring email, tracking Slack alerts, or generating daily summaries.
</Tip>

***

## Building your AI agent

Start building your agent by describing what you want it to do. The AI chat suggests tools, connectors, and tasks based on your instructions.

**To build your AI agent:**

1. Log in to [Base44](https://app.base44.com/).
2. From the Base44 home screen, click **AI Agent**.
3. Click **Start building your AI Agent**.
4. Start chatting with your new agent and describe what you want it to do. It will suggest tasks, automations, and tools based on your instructions.

**Example prompt to try:**

```text  theme={null}
Create an agent that monitors my Gmail inbox.

If an email looks important or requires a reply,
draft a response for me.

Send a summary every morning at 8 AM.
```

<Frame caption="Creating a new AI agent in Base44">
    <img src="https://mintcdn.com/base44/Qp5tKvUkTooteH--/images/buildingyouraiagent.png?fit=max&auto=format&n=Qp5tKvUkTooteH--&q=85&s=eebcef0552c36193121f5f7d814923f4" alt="Buildingyouraiagent" width="1042" height="777" data-path="images/buildingyouraiagent.png" />
</Frame>

***

## Configuring your AI agent

After creating your agent, configure how it thinks, what information it can access, and what actions it can perform.

### Chat

Interact directly with your AI agent, guide its behavior, create workflows, and observe how it performs tasks.

Your agent can also perform live tasks such as browsing the web, researching information, and previewing results directly in the workspace.

<Frame caption="Chatting with your AI agent">
    <img src="https://mintcdn.com/base44/6QRPe75nTTNSNuOA/images/chattingaiagent.png?fit=max&auto=format&n=6QRPe75nTTNSNuOA&q=85&s=c9a3698352d3d56aa265afc86453a217" alt="Chattingaiagent" width="1135" height="1105" data-path="images/chattingaiagent.png" />
</Frame>

<Tip>
  You can also chat with your AI agent on **Slack** or **Telegram**.
</Tip>

***

### Brain

The **Brain** defines how your AI agent thinks, remembers, and uses information. It contains two main areas:

* **Integrations** which determine what tools and services your agent can access.
* **Knowledge** which defines the identity, memory, and context your agent uses when reasoning and responding.

Here you configure the identity, memory, context, and reference materials your agent uses when completing tasks.

<Tip>
  Unlike traditional chatbots, an AI agent maintains persistent context using identity, user context, and long-term memory. Knowledge provides context the agent can reason about, while the **Files** tab stores working files, generated outputs, and apps created by the agent.
</Tip>

***

**Integrations**

Integrations determine what tools and services your agent can access when performing tasks. Connected services appear in the **Connectors** section. You can also browse and connect to additional services from the **Available** list.

Your agent uses two types of integrations:

* **Built-in Services:** Platform capabilities available to every agent by default, such as the **Base44 Backend**, which provides database access, functions, file storage, and automations.
* **Connectors:** OAuth integrations that link your agent to external services like Slack, Gmail, Google Docs, or GitHub. Once connected, your agent can read data, monitor activity, and trigger workflows using those services.

<Frame caption="Managing your agent's integrations and connectors">
    <img src="https://mintcdn.com/base44/Hg69Rhelj-w15QzQ/images/integrationsaiagent.png?fit=max&auto=format&n=Hg69Rhelj-w15QzQ&q=85&s=8db5b92d6aa44e1b24144dc495fd1e09" alt="Managing your agent's integrations and connectors" width="1320" height="1209" data-path="images/integrationsaiagent.png" />
</Frame>

<Tip>
  **Connectors allow your agent to:**

  * Read and summarize messages from Slack.
  * Monitor Gmail for important updates.
  * Query APIs to retrieve external data.
  * Access documentation or knowledge sources.
  * Run backend workflows and automations.
</Tip>

***

**Knowledge**

Your agent's knowledge defines the information it uses to reason and remember context across sessions. It includes several core files that shape how the agent understands and responds to requests.

<AccordionGroup>
  <Accordion title="Identity">
    Defines who the agent is.

    * Name
    * Avatar
    * Personality
    * Communication style
  </Accordion>

  <Accordion title="Soul">
    Defines how the agent behaves and makes decisions. This file establishes:

    * Behavioral principles
    * Communication tone
    * Boundaries
    * Decision-making guidelines
  </Accordion>

  <Accordion title="User">
    Stores context about the person the agent is assisting, like:

    * Name and preferences
    * Timezone
    * Role and responsibilities
    * Relevant working context
  </Accordion>

  <Accordion title="Memory">
    Memory entries store important information the agent should remember across conversations, and are used as the agent's **long-term memory**, such as:

    * Decisions
    * Preferences
    * Project context
    * Recurring tasks
  </Accordion>

  <Accordion title="Knowledge files">
    Upload documents and resources your agent can reference. These might include:

    * Documentation
    * Spreadsheets
    * Datasets
    * Reference materials
  </Accordion>
</AccordionGroup>

<Frame caption="Managing your agent's knowledge and behavior">
    <img src="https://mintcdn.com/base44/Hg69Rhelj-w15QzQ/images/knowledgeaiagent.png?fit=max&auto=format&n=Hg69Rhelj-w15QzQ&q=85&s=58a29edab81b73b138407c159f8b4c88" alt="Managing your AI agent's knowledge" width="1293" height="1063" data-path="images/knowledgeaiagent.png" />
</Frame>

<Note>
  Knowledge files provide reference material your agent can use when reasoning about tasks. For working files and generated outputs, use the **Files** tab, which acts as the agent's workspace storage.
</Note>

<Tip>
  Together, these elements give your agent persistent context, allowing it to remember information, understand your goals, and respond more intelligently over time.
</Tip>

***

### Tasks

Use tasks to run automated workflows on schedules or when events occur. Your agent can create tasks from updates, send daily or weekly summaries, sync data between systems, monitor incoming messages, and more.

<Frame caption="Scheduling tasks and automations for your agent">
    <img src="https://mintcdn.com/base44/dbaEAPy7lW6k3xl2/images/aiagentstasks.png?fit=max&auto=format&n=dbaEAPy7lW6k3xl2&q=85&s=f6c8047b1141095a4e44c6f7ecd2c2e7" alt="Scheduling tasks and automations for your AI agent" width="1408" height="1008" data-path="images/aiagentstasks.png" />
</Frame>

***

## Files

The **Files** section acts as your agent's workspace file system. It stores documents, datasets, scripts, and other working files your agent creates or uses while running tasks.

If your agent generates Base44 apps, those apps also appear here so you can open, review, and continue working on them.

<Frame caption="Uploading files for your agent">
  <img className="hidden dark:block" src="https://mintcdn.com/base44/rQknl3usBDtfGAlU/images/uploadagentfiles-2.png?fit=max&auto=format&n=rQknl3usBDtfGAlU&q=85&s=83c933d8ab775ca45c9db568f29e7818" alt="Uploading files for your AI agent" width="284" height="228" data-path="images/uploadagentfiles-2.png" />

  <img className="dark:hidden" src="https://mintcdn.com/base44/rQknl3usBDtfGAlU/images/uploadagentfiles-1.png?fit=max&auto=format&n=rQknl3usBDtfGAlU&q=85&s=f69979b609dc47d9678821fee994e038" alt="Uploading files for your AI agent" width="284" height="228" data-path="images/uploadagentfiles-1.png" />
</Frame>

<Note>
  Some system files may also appear here, such as the `.agents` folder used to store internal configuration and MCP connections.
</Note>

***

## Managing your agent settings

Manage your agent's configuration and credentials under the **Settings** tab.

### Secrets & Keys

Securely store credentials your agent needs to access external services. Secrets are stored as environment variables and can be used by your agent's backend functions or integrations.

<Frame caption="Managing agent secrets">
    <img src="https://mintcdn.com/base44/dbaEAPy7lW6k3xl2/images/aiagentsecrets-1.png?fit=max&auto=format&n=dbaEAPy7lW6k3xl2&q=85&s=1b167f3065ace6eedfecd7eae1add09e" alt="Managing your agent secrets" width="1382" height="768" data-path="images/aiagentsecrets-1.png" />
</Frame>

### API

The **API tab** lets you connect external systems to your AI agent through an API endpoint.

This allows other applications, services, or workflows to start conversations with your agent, send messages, and receive responses programmatically.

<Tip>
  **For example:** You can start conversations, send messages, retrieve conversation history, and access and manage your agent's memory.
</Tip>

<Frame caption="Connecting to your AI agent through the API">
    <img src="https://mintcdn.com/base44/dbaEAPy7lW6k3xl2/images/aiagentsapi.png?fit=max&auto=format&n=dbaEAPy7lW6k3xl2&q=85&s=0b341905a7ff0cc6516ff5cb402d8388" alt="Connecting your AI agents through the API" width="1366" height="1209" data-path="images/aiagentsapi.png" />
</Frame>

<Tip>
  Use **Leave feedback** in the sidebar to rate your experience and share feedback about the AI agent directly with the Base44 team.
</Tip>

***

## FAQs

<AccordionGroup>
  <Accordion title="Can AI agents connect to external services?">
    Yes. AI agents can connect to external tools using connectors or backend integrations, allowing them to interact with services like Slack, Gmail, or Google Calendar.
  </Accordion>

  <Accordion title="Should I create one agent or multiple agents?">
    Both approaches work. How you structure your agents depends on how you want to organize your workflows. Some people create several agents, each responsible for a specific task. Others prefer a single agent that handles multiple tasks.

    **Multiple specialized agents**

    This approach keeps responsibilities separated and can make complex workflows easier to manage.

    For example:

    * One agent monitors Gmail.
    * Another agent tracks Slack activity.
    * A third agent generates reports.

    **One central agent**

    In this model, a single agent:

    * Connects to multiple tools.
    * Runs several workflows.
    * Acts as a central assistant across your workspace.

    Many builders start with multiple specialized agents while experimenting. As their workflows evolve, they often consolidate those tasks into one central agent.
  </Accordion>

  <Accordion title="What is the difference between an AI agent and AI agents in apps?">
    * An **AI agent** works across your workspace and helps you manage tools, workflows, and information.
    * An **app agent** lives inside your app and interacts only within that app.

    <Tip>
      Use an **AI agent** when you want a personal assistant that helps you manage systems, workflows, and information across your Base44 workspace.
    </Tip>
  </Accordion>

  <Accordion title="What is the difference between an automation and an AI agent?">
    Automations run predefined workflows on schedules or triggers. AI agents operate dynamically. They analyze context, respond to messages, and decide which actions to take using the tools and knowledge you provide. Many workflows combine both. An agent can trigger automations or monitor their results.
  </Accordion>

  <Accordion title="Can I convert an app into an AI agent?">
    No. Apps and AI agents are separate creation types. However, you can create an [AI agent for your app](/Building-your-app/AI-agents).
  </Accordion>

  <Accordion title="How are credits used in AI agents?">
    AI agents use the same [credits model](/Account-and-billing/Credits) as building apps in Base44.

    * **Message credits:** Used when interacting with the agent through chat.
    * **Integration credits:** Used when the agent performs actions such as calling APIs, retrieving data, sending messages, or using connected services.

    Both credit types reset monthly according to your billing cycle.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).