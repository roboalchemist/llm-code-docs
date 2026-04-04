# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/usage/usage-guide/agent-modes.md

# Agent Modes

## Ask Agent

**Ask Agent gives you fast, context-aware answers about your codebase.**\
It’s the best tool when you want quick understanding, navigation, or clarification—without digging through files yourself.

### What it does

Ask Agent is optimized for:

* Answering questions about *how* something works
* Tracing logic across functions, files, or services
* Surfacing relevant parts of the codebase based on your question

It uses Qodo Context Engine’s indexing system to retrieve relevant context and answer from the real code—not hallucinations.

### When to use it

* You’re exploring an unfamiliar repo
* You want to quickly understand logic or design
* You’re trying to trace how a component or flow works
* You’re reviewing a PR and need additional insight

### Example Prompts

* *"Where is this hook defined and used?"*
* *"How does our login middleware handle errors?"*
* *"What are the main responsibilities of this class?"*
* *"Show me where we configure timeouts in the request layer."*

### What it won’t do

Ask Agent is fast and lightweight, so it won’t perform multi-step reasoning or deep architectural analysis. For that, use **Deep Research Agent**.

***

## Deep Research Agent

**Deep Research Agent is built for complex, multi-step reasoning tasks.**\
It’s like having a senior engineer who can map the system, gather what’s relevant, and come back with a clear answer.

### What it does

This agent:

* Searches deeply across your codebase (multiple files, repos, services)
* Chains multiple retrieval + reasoning steps
* Plans answers like an engineer: identifies dependencies, evaluates impact, surfaces edge cases

It’s slow by design—because it thinks deeply.

### When to use it

* You’re planning a refactor or system change
* You want to understand impact across services
* You’re building something on top of existing infrastructure
* You need to trace usage patterns or design choices across time and teams

### Example Prompts

* *"If I change how sessions are handled, what breaks?"*
* *"Where in our system do we serialize this object type?"*
* *"Help me refactor our shared utils to avoid duplication."*
* *"How would you redesign this flow to support multi-tenancy?"*

### What it won’t do

It’s not built for quick reads or simple function lookups. Use **Ask Agent** if you’re looking for speed and clarity over depth.

***

## Deep Issue Agent

Deep Issue Agent analyzes code diffs to surface potential breaking changes and their impact across repositories.

It’s the right tool when you want to ensure that edits—especially to shared contracts like APIs, schemas, or utilities—don’t silently break consumers.

### **What it does**

Deep Issue Agent is optimized for:

* Reviewing code diffs for breaking changes
* Checking API/contract modifications against dependent repos
* Identifying downstream impacts (services, clients, tests)
* Surfacing risky changes early in the review process

It uses Qodo Context Engine’s indexing + reasoning to cross-check edits against the broader codebase and connected repositories.

### **When to use it**

* You’re reviewing a PR and want to catch regressions or API breaks
* You’re changing shared schemas, routes, or interfaces
* You need to see which downstream repos or components a change might affect
* You’re validating refactor safety before merging

### **Example Prompts**

* "Does this API route change break existing clients?"
* "If I rename this field in the response object, where else needs to update?"
* "Show me potential issues from this diff."
* "What downstream services consume this endpoint?"

### **What it won’t do**

Deep Issue Agent isn’t for quick understanding of code or high-level design reasoning.\
It’s focused specifically on **impact analysis of changes**—use Ask Agent for quick lookups, or Deep Research Agent for multi-step system-wide reasoning.
