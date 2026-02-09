# Source: https://docs.bito.ai/help/billing-and-plans/overview.md

# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/overview.md

# Source: https://docs.bito.ai/ai-code-reviews-in-cli/overview.md

# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/overview.md

# Source: https://docs.bito.ai/ai-code-reviews-in-ide/overview.md

# Source: https://docs.bito.ai/ai-code-reviews-in-git/overview.md

# Source: https://docs.bito.ai/ai-architect/overview.md

# Overview

Bito’s **AI Architect** builds a knowledge graph of your codebase — from repos to modules to APIs — delivering deep codebase intelligence to the coding agents you already use. This fundamentally changes the game for enterprises with many microservices or large, complex codebases.

{% hint style="info" %}
Bito provides the AI Architect in a completely secure fashion, with the AI Architect available on-prem if you desire with no code ever being sent to Bito. No AI is trained on your code and your code is not stored.
{% endhint %}

{% embed url="<https://youtu.be/qAMtZ41-xJY>" %}

## Key capabilities of the AI Architect include:

* **Grounded 1-shot production-ready code** — The AI Architect learns all your services, endpoints, code usage examples, and architectural patterns. The agent automatically feeds those to your coding agent (Claude Code, Cursor, Codex, any MCP client) to provide it the necessary information to quickly and efficiently create production ready code.
  * [**Watch demo video**](https://www.youtube.com/watch?v=2yx_FfDsYco)
* **Consistent design adherence** — Code generated aligns with your architecture patterns and coding conventions.
* **Spec-driven development** — Automatically generate highly detailed, implementation-ready technical requirement documents (TRDs) and low-level designs (LLDs) with a deep, context-aware understanding of your codebase, services, and design patterns, ensuring architectural integrity and consistency at a granular level.
  * [**Watch demo video**](https://www.youtube.com/watch?v=xMmZbbZUcq0)
* **Triaging production issues** — Easily and quickly find root causes to production issues based on errors/logs/etc.
  * [**Watch demo video**](https://www.youtube.com/watch?v=05-2hKcaZKk)
* **Faster onboarding** — New engineers or AI agents can quickly understand how a system or component system structure.
* **Enhanced documentation and diagramming** — Through its internal understanding of interconnections between modules and APIs.
* **Smarter code reviews** — Reviews with system-wide awareness of dependencies and impacts.

The AI Architect builds the knowledge graph by analyzing all your repositories (whether you have 50 or 5,000 repos) to learn about your codebase architecture, microservices, modules, API endpoints, design patterns, and more.

## How you can use AI Architect

AI Architect is designed to be flexible and can power multiple use cases across different AI coding tools and workflows.

* [**Integrate via MCP server**](#getting-started) – Use AI Architect as an **MCP (Model Context Protocol) server** to connect with tools like [Claude Code](https://docs.bito.ai/ai-architect/guide-for-claude-code), [Cursor](https://docs.bito.ai/ai-architect/guide-for-cursor), [Windsurf](https://docs.bito.ai/ai-architect/guide-for-windsurf), [GitHub Copilot (VS Code)](https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code), [Junie (JetBrains)](https://docs.bito.ai/ai-architect/guide-for-junie-jetbrains), and [JetBrains AI Assistant](https://docs.bito.ai/ai-architect/guide-for-jetbrains-ai-assistant). It helps connected tools understand your codebase and workflows better, resulting in accurate and more reliable suggestions.
  1. **On-premises deployment** – Install and run AI Architect on your own infrastructure.
     * [**See the installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted)
  2. **Bito-hosted version** – Use the hosted version managed by Bito.
     * Contact [**support@bito.ai**](mailto:support@bito.ai) for a trial
* [**Example: Bito’s AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) – One example of AI Architect in action is **Bito’s AI Code Review Agent**, which uses AI Architect to deliver smarter, context-aware code reviews directly in your pull requests and IDEs.
  * [**View Guide**](https://docs.bito.ai/ai-architect/integrating-ai-architect-with-ai-code-review-agent)

## Why use the AI Architect?

Most AI coding tools struggle with accuracy in real-world codebases because they

1. Don’t fully understand the breadth and depth of your codebase. They read some of the code in your existing repository, but they don’t have a complete graph of your internal APIs, endpoints, libraries, etc. On top of that, if you are accessing a monorepo or many services not available on your machine locally, they have no context or get confused trying to access them. Bito’s AI Architect has built a knowledge graph to provide this information in a cheap and efficient way to your coding agent so it can accomplish the task with grounded and complete information.
2. They don’t fully understand how all of your services and modules interact with each other when you are trying to understand your overall system versus just one component. The AI Architect’s graph contains a mapping of all the dependencies, allowing to provide sophisticated analysis – how you would expect an Architect too.

## How AI Architect differs from Embeddings?

Traditional embeddings work like a search engine — they retrieve code snippets or documents similar to a given query.&#x20;

They can find related content but can’t understand how different parts of your system work together.&#x20;

The AI Architect, on the other hand:&#x20;

* Builds a knowledge graph that captures relationships between repositories, modules, APIs, and libraries.
* Provides precise answers and implementations, not just search results.
* Understands context and intent — how and why something is implemented in your codebase.
* Enables system-aware reasoning, allowing AI agents to generate or review code with full architectural understanding.

## Getting started

1. [**Try Bito's AI Architect**](https://alpha.bito.ai/home/welcome/ai-architect)
2. [**Get a demo**](https://calendly.com/d/csk7-8yg-pwf) with our team.
3. Lastly, email [**support@bito.ai**](mailto:support@bito.ai) if you have any additional questions.

## Demos of different ways to use AI Architect

{% embed url="<https://www.youtube.com/watch?v=2yx_FfDsYco>" %}

{% embed url="<https://www.youtube.com/watch?v=xMmZbbZUcq0>" %}

{% embed url="<https://www.youtube.com/watch?v=05-2hKcaZKk>" %}
