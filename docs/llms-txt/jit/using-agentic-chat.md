# Source: https://docs.jit.io/docs/using-agentic-chat.md

# Using Agentic Chat

**Agentic Chat** is the interactive interface where you can ask questions, explore your environment, generate dashboards, and create agents from natural-language requests.\
Sera uses Jit’s knowledge graph and your connected integrations to produce contextual, structured, and actionable output.

Agentic Chat is ideal for:

* On-demand analysis
* Exploratory questions
* Building dashboards
* Investigating security findings
* Prototyping an agent before saving it

***

## 4.1 Asking Questions

You can type any security-related question into the chat input.\
Sera supports natural-language queries such as:

* *“Run a full risk assessment.”*
* *“Which apps are most exposed right now?”*
* *“Show me misconfigurations across AWS and GitHub.”*
* *“Create a dashboard of SLA-violating findings.”*
* *“Summarize our supply-chain risk.”*

Sera interprets your intent, retrieves the relevant data, and generates structured results based on the context.

**Using Tools from Chat:**\
Certain prompts in Chat may trigger built-in tools automatically when the task requires them.\
For example:

* Jira tools may be used to fetch or create tickets
* AWS queries may run when asking about cloud resources
* Slack messages may be sent for urgent alerts

Tools are not configured separately in Chat.\
They are invoked **implicitly** when your question requires a real action (fetching data, creating work, or alerting a team).

For details on each tool’s capabilities and limitations, see **[Tools](https://docs.jit.io/docs/agentic-tools)**.

***

<br />

## 4.2 Suggested Prompts

Agentic Chat includes **suggested prompts** underneath the input field to help you get started quickly.

Examples include:

* *Run a full risk assessment*
* *Which apps are most critical and exposed?*
* *What’s our OSS supply-chain risk?*
* *How vulnerable are we to cloud misconfigs?*

These prompts demonstrate the types of questions the agent can answer, and can be used as templates for your own queries.

***

## 4.3 Saving a Chat as an Agent

Any conversation can be turned into a reusable agent by selecting **Save Agent**.

Saving a chat:

* Extracts the underlying task from your request
* Prepares a reusable workflow
* Opens the agent configuration modal
* Allows you to adjust schedule, notifications, Slack output, and advanced settings

For more information on configuration fields, see **Section 2.2 — Agent Configuration**.

This is the recommended path when you prototype a workflow in chat and want to automate it.

***

## 4.4 Sharing a Chat

You can share the results of a chat using the **Share** button.

Sharing options include:

* **Copy Link** — Generates a read-only URL for the conversation
* **Download Run Report** — Provides a downloadable summary of Sera’s output

Sharing is useful for:

* Collaborating with teammates
* Escalating issues
* Demonstrating findings
* Preserving analysis for audit or review

## 4.6 Note on Accuracy (Beta)

Agentic Chat is currently in **Beta**.\
As with all LLM systems, answers may occasionally be partial, imprecise, or slightly off.\
For best results, ask clear and scoped questions.

***

### 4.7 What Chat Works Well For

Agentic Chat performs best with prompts that follow predictable, structured patterns—especially those that leverage Jit’s **knowledge graph**.

Below are the most reliable prompt types, each with examples taken from real-world usage.

***

#### **1. Relationship Queries**

Questions about how assets connect to each other.

Examples:

* *“Which teams own which services and repositories?”*
* *“Show me the dependency relationships between our microservices.”*

***

#### **2. Prioritization Queries**

Ranking or sorting by risk, severity, or impact.

Examples:

* *“List the top 3 prioritized production GitHub repositories.”*
* *“Show me the top 5 high-priority findings in production.”*
* *“Show a prioritized list of SCA vulnerabilities.”*

***

#### **3. Filtered / Scoped Queries**

Focusing on a specific environment, severity, or condition.

Examples:

* *“Show critical findings that violated their SLA of 90 days as of July 1, 2025.”*
* *“Which production repositories have no open findings?”*
* *“How many findings are both in production and externally accessible?”*

***

#### **4. Inventory & Count Queries**

Listing or counting assets.

Examples:

* *“How many production repositories do we have?”*
* *“Show me all repositories.”*
* *“List the top 25 GCP accounts with production resources.”*

***

#### **5. Time-Based Queries**

Limited to a time window.

Examples:

* *“Detect new S3 buckets created this week.”*
* *“What deployment activities happened in the last 7 days?”*

***

#### **6. Context Lookups**

Asking what Jit already knows about an entity.

Examples:

* *“What do you know about a repository called ‘smart-payment-service’?”*
* *“What security vulnerabilities exist in our critical production services?”*

***

#### **7. Reasoning / Explanation Queries**

Asking the model to interpret or analyze known data.

Examples:

* *“Show me 5 FPs detected by DAST on application X and explain why these are FPs.”*
* *“What are the 10 most urgent security issues we need to address?”*

***

### 4.8 Examples of Good Prompts (Quick Reference)

* *“List the top 3 prioritized production GitHub repositories.”*
* *“Group the top DAST vulnerabilities by application.”*
* *“Detect new S3 buckets created this week.”*
* *“How many high-priority findings (score > 60) exist in production?”*
* *“What do you know about the repository ‘smart-payment-service’?”*

***

## Summary

Agentic Chat is your interactive entry point for exploring Jit, generating insights, and building dashboards.\
From here, you can:

* Ask natural-language questions
* View structured widgets
* Prototype complex analyses
* Save your work as automated agents
* Share outputs with your team

Sera combines conversational ease with powerful analysis capabilities to help streamline your security workflows.