# Source: https://docs.jit.io/docs/creating-agents.md

# Creating Agents

Agents can be created in several ways: from scratch, directly from Agentic Chat, or using a template from the Agent Gallery. Regardless of the entry point, all agents use the same configuration modal, described in the **Agent Configuration** section below.

***

## 2.1 Ways to Create an Agent

### 2.1.1 Create an Agent From Scratch

You can create a new custom agent from the **My Agents** page using the **New Agent** button.

This path is ideal when:

* You have a specific task in mind
* You need full control over the agent’s instructions
* No existing template matches your needs

After selecting **New Agent**, the configuration modal opens.\
See **Agent Configuration (Section 2.2)** for full details.

***

### 2.1.2 Create an Agent From Agentic Chat

Any conversation inside **Agentic Chat** can be saved as an agent using the **Save Agent** button.

This method:

* Converts the underlying task into an automated workflow
* Automatically extracts the intent of your request
* Initializes the agent with the same context used in the chat

After selecting **Save Agent**, the configuration modal appears, allowing you to adjust the task, schedule, notifications, and other settings before saving.

See **Agent Configuration (Section 2.2)** for full details.

For more information on how to use Agentic Chat, including asking questions, viewing widgets, and understanding responses, see **Section 4 – Using Agentic Chat**.

***

### 2.1.3 Create an Agent From Templates (Agent Gallery)

The **Agent Gallery** provides a collection of prebuilt agent templates covering a wide range of security workflows, such as GitHub monitoring, AWS posture checks, supply chain analysis, code scanning, ticketing dashboards, and more.

The gallery is designed to help you quickly adopt proven workflows without writing instructions manually.

***

#### **Browsing the Gallery**

The Agent Gallery is organized using:

* **Category tabs across the top** (e.g., All, Cloud, Code, Compliance, Risk, Security, etc.)\
  These categories allow you to filter templates by their functional domain.

* **Tags on each template card**\
  Templates include tags such as `Risk`, `GitHub`, `Secrets`, `SLA`, `Compliance`, etc., making it easy to understand their scope at a glance.

* **Free-text search bar**\
  You can search by template name, description, or tags to find relevant workflows instantly.

***

#### **Adding a Template**

To create an agent from a template:

1. Open the **Agent Gallery**.
2. Browse using categories, tags, or free-text search.
3. Select **Add** on any template card.
4. The agent configuration modal will open, preloaded with a recommended task and defaults.
5. Click **Save** to add the new agent to your **My Agents** workspace.

***

#### **Customizing Template Settings**

Although templates come with predefined instructions and schedules, you can fully customize the agent by adjusting:

* Task instructions
* Schedule
* Notification settings
* Slack channel
* Advanced knowledge graph instructions
* Dashboard rendering instructions

All of these settings use the same configuration modal described in **Agent Configuration (Section 2.2)**

***

## 2.2 Agent Configuration (Universal for All Agents)

All agents—whether created from scratch, from Agentic Chat, or from the Agent Gallery—share a unified configuration modal. This modal contains all settings required to define how the agent behaves.

### 2.2.1 Task

Defines what the agent will do on each run.

The task includes:

* The agent’s instruction prompt
* Any context-specific parameters extracted from chat or templates
* Optional additional context you provide

The task forms the core logic of the agent.

**Using Tools in Tasks:**\
Tasks can call built-in tools such as:

* **Jira Fetch Ticket(s)**
* **Jira Create Ticket**
* **AWS Query Resources**
* **Slack Message**

Tools are triggered directly from the agent’s task instructions.\
For examples of how tools are used inside real agents, see **[Tools](https://docs.jit.io/docs/agentic-tools)**.

***

### 2.2.2 Schedule

Controls how and when the agent runs.

Schedule options typically include:

* **Manual Only**
* **Daily**
* **Weekly**
* **Semi-Monthly**
* **Custom schedules** (if available)

When scheduling is enabled, the agent runs automatically based on the selected cadence.

***

### 2.2.3 Notifications & Slack Settings

To receive agent results in Slack, your workspace must first have an active **Slack integration** configured in Jit. Without this integration, Slack notifications will not be available.

Once Slack is connected, you can control how notifications are delivered using two fields:

***

#### **Notification Settings**

This setting determines whether the agent sends notifications to Slack after each run.

Available options:

* **Always** — The agent will send a Slack notification every time it runs.
* **Never** — The agent will not send any Slack notifications.

If you select **Never**, the agent will run silently without posting results to any channel.

***

#### **Slack Channel**

Specifies the Slack channel where the agent will send notifications.

When entering a channel name:

* You must include the leading `#` (e.g., `#security`, `#product`, `#alerts`)
* You can change the channel at any time
* Leave this field empty if notifications are set to **Never**

Slack delivery is especially useful for operational workflows that require real-time visibility across teams.

***

### 2.2.7 Save and Run

After configuring an agent, you can:

* **Save** to store the agent
* **Save & Run** to execute the agent immediately

Running immediately is useful for validating configuration or producing the first report.

***

## Summary

Creating an agent always follows the same structure:

1. Choose an entry point (scratch, chat, or gallery)
2. Configure the agent using the unified configuration modal
3. Save and optionally run the agent

This consistent flow simplifies how you adopt automation across your security workflows.