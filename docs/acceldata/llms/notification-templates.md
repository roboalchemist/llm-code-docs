# Source: https://docs.acceldata.io/documentation/notification-templates.md

# Notification Templates

Notification templates let you customize the format and content of alerts in Acceldata Data Observability Cloud (ADOC). With templates, you control how notifications look, what information they include, and how they integrate with your downstream tools and workflows.

Templates make alerts **clearer, more actionable, and easier to automate** across email, chat, ITSM, and webhook-based systems.

## Why Use Custom Notification Templates?

By default, ADOC uses system-defined notification formats. These are safe, production-tested defaults, but they may not always match your business processes or tooling.

### Problems With Generic Notifications

| **Challenge** | **What It Looks Like in Practice** | 
| ---- | ---- | 
| Generic or inconsistent alerts | Different policies send slightly different subjects and payload layouts. | 
| Manual triage and routing | Engineers manually move alerts into the right Slack channels or queues. | 
| Slower response and remediation | On-call teams must click into ADOC to understand what happened. | 


### What Custom Templates Enable

| **Capability** | **Examples** | 
| ---- | ---- | 
| Tailored content | Emphasize severity, affected asset, and business impact. | 
| Tool-specific payloads | JSON bodies that match PagerDuty, ServiceNow, or custom webhook schemas. | 
| Routing & automation hints | Include fields used by runbooks or workflow engines for routing. | 
| Business-friendly summaries | Different layouts for on-call engineers vs. business stakeholders. | 


Custom notification templates transform alerts from “system messages” into **first-class workflow events**.

## Concepts and Terminology

### System Templates vs. Custom Templates

ADOC ships with **system templates** for every supported channel and source type. These are:

- Safe defaults
- Updated with each ADOC release
- Used automatically when no custom template is configured

You can optionally create **custom templates** that override system templates for a specific combination of:

- **Source type** (for example, Data Quality, Reconciliation, Data Freshness, Pipeline Monitoring, Profiling)
- **Channel** (Email, Webhook, Slack, Google Chat, Microsoft Teams, Jira, ServiceNow)

| **Type** | **Owned By** | **Editable?** | **When Used** | 
| ---- | ---- | ---- | ---- | 
| System template | Acceldata | No | Fallback when no custom template is configured | 
| Custom template | Your tenant | Yes | When a matching Template Group + channel + source type is set | 


System templates continue to work even when you add custom ones, so you always have a safe fallback.

### Notification Template Groups

Customization is organized into **Notification Template Groups**. A Template Group is a named **collection of templates** that:

- Targets **one or more source types**(for example, Data Quality, Reconciliation, Pipeline Monitoring)
- Contains one template **per channel** you want to customize
- Is attached to one or more **Notification Groups**

Think of a Template Group as:  “All the templates that define **how** this notification group talks to email, Slack, webhooks, etc.”

#### Template Group Structure

| **Field** | **Description** | 
| ---- | ---- | 
| Name | Human-friendly identifier (e.g., `Prod – DQ Alerts – Slack & PagerDuty`) | 
| Description | Optional business description or usage notes | 
| Source types | Policy types this group applies to (Data Quality, Freshness, etc.) | 
| Channels | Email, Webhook, Slack, Google Chat, Teams, Jira, ServiceNow | 
| Templates | Per-channel content authored in FreeMarker (FTL) | 


## Supported Channels and Source Types

## Channels

ADOC supports templates for multiple communication and incident-management systems.

| **Channel** | **Format Type** | **Typical Use Case** | 
| ---- | ---- | ---- | 
| Email | HTML or plain text | Human-readable notifications | 
| Webhook | JSON | Integration with workflow / custom tools | 
| Slack | JSON (Block Kit) | Team collaboration & on-call updates | 
| Google Chat | JSON (Card messages) | Chat-based collaboration | 
| Microsoft Teams | JSON (MessageCard / Adaptive Card) | Enterprise chat and incident channels | 
| ServiceNow | Plain text or JSON payload | ITSM incident creation / updates | 
| Jira | JSON (Atlassian Document Format / issue fields) | Issue / ticket creation & enrichment | 


Each channel has its **own schema and constraints**. Templates must emit valid HTML, JSON, or platform schema for that channel.

## Policy and Source Types

Template variables and data shape depend on the **source type** that generates the notification. Typical source types include:

| **Source Type** | **What It Represents** | 
| ---- | ---- | 
| Data Quality | Rules and scores for table-level quality checks | 
| Reconciliation | Cross-system comparison of record counts and values | 
| Schema Drift | Changes to table structure (added/removed/modified columns) | 
| Data Drift | Statistical changes in value distributions | 
| Data Freshness | Timeliness / delay of arriving data | 
| Pipeline Monitoring | Status and performance of data pipelines | 
| Profiling & Profile Anomaly | Table profiling and anomaly detection on profile metrics | 


Each source type exposes a **different set of template variables**.

## How ADOC Selects a Template

When a policy execution generates a notification, ADOC chooses a template in this order:

1. **Identify Notification Group**

Policy → Notification Group(s) based on your Alerts & Notifications configuration.

2. **Resolve Template Group**
Check if the Notification Group has a **Custom Template Group** selected.
3. **Determine Source Type and Channel**

**Example**: Data Quality → Slack.

4. **Find Matching Template in Group**

| **Case** | **Behavior** | 
| ---- | ---- | 
| Custom template exists for source + channel | ADOC renders notification using that custom template | 
| No custom template, but system template exists | ADOC uses **system template** for that source + channel | 
| Neither exists (edge cases) | Notification may be skipped or fall back to minimal default (rare) | 


As long as you have **either** a system template **or** a custom template for a source+channel, alerts keep flowing.

## Prerequisites and Roles

### Permissions and Access

To create and manage Notification Templates, you typically need an **admin-level or configuration role** in ADOC.

| Requirement | Why It Matters | 
| ---- | ---- | 
| Access to **Settings** | Notification Templates live under **Settings &gt; Notifications** | 
| Knowledge of **policies** | You need to know what your Data Quality / Pipeline policies do | 
| Knowledge of **channels** | Email / Slack / Webhook mappings and any external API requirements | 
| Coordination with owners | To agree on severity mapping, routing, and incident rules | 


## High-Level Workflow

At a high level, working with Notification Templates looks like this:

1. **Plan what you want to change**
Decide which alerts, channels, and teams you want to customize, and why (for example, on-call vs. business stakeholders, or different behavior for prod vs. non-prod).
2. **Create a Notification Template Group**
Define the “bundle” of templates that will apply to specific source types (such as Data Quality, Freshness, or Pipeline Monitoring).
3. **Author per-channel templates in FTL**
For each channel (Email, Webhook, Slack, etc.), build HTML/JSON content using variables and conditional logic that match your tools and audience.
4. **Preview and test against sample executions**
Use the preview and test functions to validate layout, variables, and schema against real or sample executions before going live.
5. **Attach the Template Group to a Notification Group**
Update your Notification Group configuration so that alerts use your new Template Group instead of only relying on system defaults.
6. **Monitor and refine over time**
Collect feedback from users, review incidents, and iterate on the templates to improve clarity, routing, and actionability.