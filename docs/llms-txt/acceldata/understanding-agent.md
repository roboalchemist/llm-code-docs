# Source: https://docs.acceldata.io/documentation/understanding-agent.md

# Understanding Agents

## What Are Agents?

**Agents** in ADM are specialized AI components designed to perform specific data management tasks.
 Each agent is equipped with a focused set of capabilities, access permissions, and tools that enable it to act autonomously or collaboratively within ADM’s multi-agent ecosystem.

An agent typically has:

- **Defined responsibilities** within a particular data domain
- **Access to targeted tools and datasets** relevant to its function
- **Expertise** in performing domain-specific analysis or actions
- **Collaboration capabilities** to work seamlessly with other agents

### Agent Architecture

![](https:\/\/uploads.developerhub.io\/prod\/Yoq2\/onc30pi1ihw22u0mnfkqivx2znjcfhg2q69dr2h9kmhlhy31noxkixmi9yhe6mke.png)

## Agent Types and Capabilities

ADM includes several classes of agents categorized by their purpose: **Discovery**, **Monitoring**, **Analysis**, and **Notification**. When you submit a complex query—such as _“Create a data quality policy for the customer table and notify me when it fails”_—multiple agents may work together through **collaborative execution**:

- The **Catalog Agent** retrieves schema and metadata.
- The **Data Quality Agent** recommends validation rules.
- The **Policy Creation Workflow** builds the policy configuration.
- The **Incidents Agent** sets up alerting and notifications.

ADM’s orchestration layer automatically routes the request, invokes the required agents (often in parallel), aggregates their results, and synthesizes the final response.

### Discovery Agents

| **Agent** | **Purpose** | **Capabilities** | **Use Case** | **Example Query** | 
| ---- | ---- | ---- | ---- | ---- | 
| **Catalog Agent** | Discovers and catalogs data assets | Discovery | Find datasets, retrieve metadata, view schema details | “Show me all tables containing customer data.” | 


### Monitoring Agents

| **Agent** | **Purpose** | **Use Case** | **Example Query** | 
| ---- | ---- | ---- | ---- | 
| **Data Quality Agent** | Monitors data quality standards and metrics | Track quality scores, check policy executions | “Which data quality policies failed in the last 24 hours?” | 
| **Schema Drift Agent** | Detects schema changes and drift patterns | Identify schema changes and breaking impacts | “Has the customer table schema changed recently?” | 
| **Data Drift Agent** | Monitors data distribution changes over time | Detect distribution shifts or anomalies | “Show me tables with significant data drift.” | 
| **Data Cadence Agent** | Tracks data freshness and arrival frequency | Monitor freshness and SLA compliance | “Which tables haven’t been updated today?” | 
| **Pipelines Agent** | Monitors data pipeline executions | Track pipeline health, history, and performance | “Show pipeline failures from yesterday.” | 


### Analysis Agents

| **Agent** | **Purpose** | **Use Case** | **Example Query** | 
| ---- | ---- | ---- | ---- | 
| **Reconciliation Agent** | Compares data across systems for consistency | Identify discrepancies and validate counts | “Compare customer counts between source and target.” | 
| **Web Search Agent** | Searches external sources for supporting information | Retrieve documentation or best practices | “What are the industry standards for data quality policies?” | 


### Notification Agents

| **Agent** | **Purpose** | **Use Case** | **Example Query** | 
| ---- | ---- | ---- | ---- | 
| **Incidents Agent** | Manages and tracks data incidents | Create, track, and resolve incidents | “Create an incident for the failed customer_orders policy.” | 


## How Agents Work Together

### Collaborative Execution

When you submit a query that requires multiple steps, ADM coordinates agent collaboration automatically.

**Example:**

> “Create a data quality policy for the customer table and notify me when it fails.”

| **Agent** | **Function** | 
| ---- | ---- | 
| **Catalog Agent** | Retrieves the customer table schema and metadata. | 
| **Data Quality Agent** | Analyzes the structure and recommends quality rules. | 
| **Policy Creation Workflow** | Builds and applies the policy configuration. | 
| **Incidents Agent** | Configures notifications for policy failures. | 


### Orchestration Process

- ADM’s **Routing Layer** determines which agents are relevant.
- Agents execute **in parallel** whenever possible to reduce latency.
- The **Orchestrator** aggregates and reconciles their outputs.
- The final, unified response is synthesized and displayed to the user.

## Enabling and Configuring Agents

To view or configure agents:

1. Navigate to **Settings &gt; Agents**.
2. The **Agents** page lists all available agents with:
    - Agent name and icon
    - Description of purpose
    - Capability badges (e.g., _Discovery_, _Monitoring_, _Analysis_, _Notification_)

3. Use the **search bar** to filter by agent name or capability.

### Enabling Agents

- Locate the desired agent and toggle the **Enable** switch to **ON**.
- The agent becomes active immediately, no restart required.
- Most agents use system defaults, but advanced users can configure:
    - Monitoring frequencies
    - Alert thresholds
    - Data source or integration parameters

> Note Advanced configuration should be performed by an administrator to maintain system consistency.

## Agent Orchestration in Action

During query execution, ADM provides **real-time visibility** into which agents are active through the **Agent Thinking Panel**. This view displays:

- The agents currently in use (e.g., Catalog, Data Quality, Reconciliation)
- Step-by-step progress indicators
- Execution timings for each agent
- Actions taken and their outcomes

### Benefits of Orchestration Transparency

- Understand how ADM interprets and executes your request
- Verify that the correct agents were invoked
- Troubleshoot unexpected outputs
- Learn better prompting strategies by observing how queries are processed

The orchestrator ensures that all relevant agents contribute efficiently, merging their outputs into a coherent and actionable response.