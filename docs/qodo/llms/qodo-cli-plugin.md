# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/products-integrations/qodo-cli-plugin.md

# Qodo CLI plugin

{% hint style="success" %}
This article explains how to use **Qodo Context Engine in Qodo CLI plugin.**

For a deeper dive on Qodo Gen, [**visit the dedicated Qodo CLI Plugin documentation portal**](https://docs.qodo.ai/qodo-documentation/qodo-command)**.**
{% endhint %}

Qodo Context Engine integrates seamlessly into Qodo CLI plugin, giving you **built-in tools for gathering context and running deep research** on both open source and private codebases.

It’s like having a **Research Engineer** inside your CLI—one who can instantly pull examples, trace patterns, and surface insights across vast repositories.

***

### Why Qodo Context Engine Inside Qodo CLI plugin Is a Game-Changer

Qodo CLI plugin already lets you run and manage AI agents from the terminal. With QQodo Context Engine, those agents get depth—connecting research and context-gathering directly to your workflows.

Most CLI-based assistants can only answer based on your current prompt. Qodo Context Engine integrates directly with open source ecosystems and (with QAW) your organization’s repositories, enabling answers that are grounded in **real code, real dependencies, and real design patterns**.

#### What this enables:

* **Context-aware search**\
  Find implementation patterns and code examples across open source projects or your internal repositories.
* **Deep technical research**\
  Ask complex, multi-layered questions and get comprehensive answers grounded in actual source code.
* **Architecture-level insight**\
  Understand how systems are structured, how dependencies interact, and how design patterns are applied.
* **Intelligent planning**\
  Plan refactors, migrations, or large-scale feature rollouts with insight into both open source practices and your own codebase.
* **Faster problem-solving**\
  Get research-quality answers without leaving the terminal or juggling multiple tools.

It’s like having a **Principal Engineer + Research Assistant** who already knows both the global open source landscape and your organization’s codebase—and who’s always available, right where you work.

***

### Available Commands

#### Multi-tenant (open source)

* `get_open_source_context` → Search for code examples and implementation patterns from open source projects.
* `deep_research_open_source` → Get comprehensive answers to complex questions about open source projects.

#### Single-tenant (with QAW enabled)

* `get_organization_context <QUERY>` → Search for code examples and implementation patterns from your organization’s repositories.

usage example:

```shellscript
> get_organization_context auth management backend/repo1 and frontend/repo2.
```

* `deep_research_organization <QUERY>` → Get comprehensive answers to complex questions about your organization’s projects.

usage example:

```bash
> get_organization_context explain how auth is handled in the following repositories backend/repo1 and frontend/repo2.
```
