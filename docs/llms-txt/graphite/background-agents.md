# Source: https://graphite-58cc94ce.mintlify.dev/docs/background-agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://graphite-58cc94ce.mintlify.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Background Agents

> Describe what you want built or fixed in plain language, and Graphite spins up a remote sandbox to write the code, run tests, and open a pull request for your review.

Ship code without opening your IDE. Background Agents let you describe what you want built or fixed in plain language, and Graphite spins up a remote sandbox to write the code, run tests, and open a pull request for your review.

It's the fastest way to go from idea to reviewable PR - no local environment, no setup, just results.

## What you can do

* **Quick fixes on the go** - Push a small change from your phone or browser without cloning a repo
* **Generate boilerplate** - Scaffold new features, add API endpoints, or write SQL queries
* **Add tests** - Expand coverage without context-switching out of code review
* **Ship faster** - Delegate repetitive tasks and review the output in Graphite's PR interface

## Getting started

1. Go to [**Preferences → Background Agents**](https://app.graphite.com/settings/preferences) and toggle it on
2. Open the **Background Agents** page in the sidebar (🪄 icon)
3. Select a repo and enter a prompt describing what you want
4. Hit **Submit** - Graphite runs the agent and opens a draft PR when it's done

You'll get **\$10 of free usage** to try it out. For unlimited usage, add your own Claude API key in the Background Agents settings.

## Privacy and security

**No training on your code.** Graphite does not train models on your code, regardless of the product you use.

**Zero Data Retention.** Graphite maintains Zero Data Retention agreements with all model providers. Your code is processed only to complete the requested task and is not stored or used for training.

### Using Graphite-managed credits

When using free credits or a Graphite-managed API key, your usage is covered under Graphite's privacy terms and our Zero Data Retention agreements with model providers.

### Bring your own API key

When you provide your own API key (e.g., for Anthropic's Claude), the data handling and privacy terms are governed by your direct agreement with that provider.

## Execution environment

Background Agents run in isolated, ephemeral sandboxes. Each task spins up a fresh environment with access only to the repository and context you provide. Sandboxes are destroyed after task completion.

## Related

* [AI Privacy and Security](/ai-privacy-and-security) - Overview of Graphite's AI privacy practices
