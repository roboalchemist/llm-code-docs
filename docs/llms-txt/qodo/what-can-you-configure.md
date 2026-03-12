# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/what-can-you-configure.md

# What can you Configure?

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

### Why configure Qodo?

Configuring Qodo Git interface lets you shape Qodo to match your team's needs:

* Automate the right tools at the right time.
* Filter out noise from irrelevant PRs.
* Guide Qodo to respond in a way that aligns with your practices.
* Maintain consistency across projects.&#x20;
* Improve the quality and relevance of the suggestions you get.

{% hint style="warning" %}
**Only configure what you need.**

Don’t copy the entire configuration into your `.pr_agent` file, include only the settings you actually use.

Keeping your configuration file minimal ensures better performance.
{% endhint %}

### What can you configure?

* **General Settings**\
  Set the response language, control log verbosity, and set ignores.
* **Tool Behavior**\
  Customize how each tool works. For example, choose which sections to show in `/review`, set the number or style of suggestions in `/improve`, or change the output format for `/describe`.
* **Automation**\
  Decide which tools should run automatically when a PR is opened or updated.
* **AI Model**\
  Pick the main AI model used by Qodo, set fallback models, and configure provider-specific options such as API keys or endpoints.
* **Configuration Methods**\
  Apply settings using a wiki page, a local `.pr_agent.toml` file in the repo, a global `pr-agent-settings` repo, command-line flags, or inline PR comments.
* **Extra Instructions**\
  Add free-text guidance to customize how tools respond.
* **Best Practices**\
  Define custom coding standards in a `best_practices.md` file to guide the `/improve` tool.
* **Integrations**\
  Connect to Jira to pull in ticket context or enable RAG-based context enrichment.
* **Qodo Features**\
  Turn features on or off, including suggestion tracking, auto-approval, CI feedback, interactive suggestion application, and custom labels in the repo UI.
* Compliance\
  Use `pr_compliance_checklist.yaml`, to define your organization’s custom PR compliance checks for the [/compliance](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/compliance) tool.

## The configuration file

`.pr_agent.toml` is a file name used for user-defined configurations.

You can create a `.pr_agent.toml` file to customize settings [at different levels](#how-to-set-configurations).

## How to set configurations

You can set configurations in three ways:

1. [**Local configuration file**](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file)\
   Upload a `.pr_agent.toml` file to the root of your repository. The settings will apply to PRs created after the file is uploaded.
2. [**Global configuration file**](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file)\
   At the organization level, create a repository called `pr-agent-settings`. The `.pr_agent.toml` file inside will serve as the default configuration for all repositories under the organization, unless overridden by a local configuration or a wiki config.
3. [**Wiki configuration page**](#wiki-configuration-file)\
   Create a `.pr_agent.toml` page in the repository’s wiki. This method doesn’t require committing changes to the repo and is easy to update at any time.

### Precedence of Configurations

Configurations follow an order of precedence:

* Wiki configurations override local configurations.
* Local configurations override global configurations.
