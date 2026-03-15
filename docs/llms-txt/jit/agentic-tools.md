# Source: https://docs.jit.io/docs/agentic-tools.md

# Agentic Tools

## Overview

Agentic Tools are the **fundamental building blocks** that Jit's agents use to operate.\
Every action an agent performs—retrieving data, analyzing context, correlating resources, detecting risk, creating tickets, sending alerts—is powered by one or more Tools.

Tools come in two categories:

1. **Internal Tools**\
   Powered by Jit’s **Knowledge Graph**, used for data retrieval, filtering, correlation, prioritization, and analysis.

2. **External Tools**\
   Integrations that allow agents to take actions outside Jit—such as querying Jira, creating tickets, querying AWS, reading uploaded files, or sending Slack messages.

Together, Internal + External Tools define what an agent can do and how it executes tasks.

Tools are **deterministic**, **structured**, and designed to be composed into powerful agent workflows.

***

## 1. Internal Tools: Knowledge Graph

Internal tools give agents access to Jit’s **Knowledge Graph** — the unified, structured model of your entire application and cloud environment.

### 1.1 What the Knowledge Graph Is

The Knowledge Graph stores **normalized, connected entities** such as:

* Applications and repositories
* Cloud resources and identities
* Security findings from all scanners
* Team and ownership relationships
* Resource links across code, cloud, and runtime

It acts as the agent's internal database and reasoning engine.

### 1.2 What Agents Can Do Through Internal Tools

Internal tools allow agents to:

#### **Retrieve**

Pull entities such as repositories, findings, cloud resources, services, or teams.

#### **Filter**

Narrow results by severity, environment, ownership, SLA status, or exposure.

#### **Correlate**

Connect resources across systems (e.g., repo → service → cloud asset → findings).

#### **Prioritize**

Rank assets or findings using risk factors, exposure, or priority score.

#### **Analyze**

Detect patterns, summarize posture, map dependencies, or combine signals from multiple security integrations.

#### **Visualize**

Render dashboards, tables, metrics, and breakdown widgets.

### 1.3 Examples (Internal Tools)

* *“Which production services have critical findings?”*
* *“Show vulnerabilities on externally exposed cloud resources.”*
* *“List the five riskiest repositories.”*

Internal tools drive **most agent behavior** and are the core of how agents understand your environment.

***

## 2. External Tools: Integrations Agents Can Act Through

External tools let agents interact with systems outside Jit.\
These tools allow agents to fetch external data, enrich context, or take automated actions in third-party platforms.

Below are the currently supported external tools, grouped by integration.

***

### 2.1 Jira Tools

#### **Fetch Jira Issues**

Retrieve Jira issues by project, JQL, or specific issue keys.\
Useful for backlog dashboards, SLA checks, and compliance reports.

#### **Get Jira User Details**

Retrieve information about Jira users (name, email, status).\
Useful for mapping findings to owners or validating assignments.

#### **Create Jira Tickets**

Open new tickets in Jira with structured fields such as summary, description, due date, and labels.\
Useful for automated escalation and remediation workflows.

***

### 2.2 AWS Tools

#### **Query AWS Resources**

Retrieve AWS metadata for resources such as IAM roles, S3 buckets, EC2 instances, VPC objects, and Security Groups.\
Useful for cloud posture analysis, exposure mapping, and asset correlation.

**Note:** Works best when scoped to **one AWS account**.\
Cross-account queries may return excessive or duplicated data.

***

### 2.3 Browser Tool

#### **Search the Web**

Perform a safe, scoped web search.\
Commonly used for:

* Threat intelligence lookups
* IoC and CVE verification
* Increasing context around emerging attacks

***

### 2.4 S3 Tools

#### **List Uploaded Files**

List files stored in your workspace's S3 bucket.\
Useful for accessing uploaded SBOMs, manifests, or configuration files.

#### **Read an Uploaded File**

Read the contents of an uploaded file.\
Useful when agents need to parse or process custom datasets provided by users.

***

### 2.5 Slack Tools

#### **List Workspace Users**

Retrieve all Slack workspace members.\
Useful for mapping teams or sending targeted alerts.

#### **List Slack Channels**

Retrieve available Slack channels that the bot can post into.\
Useful for ensuring alerts are routed correctly.

#### **Send Slack Messages**

Send formatted notifications or summaries into Slack channels.\
Useful for high-urgency alerts, daily/weekly reports, and workflow updates.

*Requires specifying a channel with a leading `#`.*

***

## 3. How Agents Combine Internal & External Tools

Agents rarely use a single tool in isolation.\
Their power comes from combining **internal reasoning** with **external actions**.

### Example: SLA Violations Workflow

1. Internal → Retrieve findings
2. Internal → Detect SLA violations
3. Internal → Build dashboard
4. External → Notify via Slack
5. External → (Optional) Create Jira tickets

***

### Example: Supply Chain IoC Detection

1. Internal → Analyze repositories and dependencies
2. Internal → Match against IoCs
3. Internal → Correlate to teams and services
4. External → Create Jira tickets
5. External → Send Slack alerts

***

### Example: Cloud Security Posture Assessment

1. External → Query AWS resources
2. Internal → Correlate with security findings
3. Internal → Identify exposed assets
4. Internal → Generate dashboards
5. External → Escalate via Jira or Slack

***

## Summary

Agentic Tools are the **operational engine** behind Jit’s agents.

They include:

* **Internal Tools** powered by the Knowledge Graph
* **External Tools** such as Jira, AWS, Browser Search, S3 File Access, and Slack

Agents use these tools to:

* Understand your environment
* Analyze and correlate risks
* Rank and prioritize issues
* Escalate findings
* Automate workflows end-to-end

Tools are **how agents operate** — they define what is possible inside Jit’s agentic system.