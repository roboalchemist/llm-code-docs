# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/getting-started/setup-and-quickstart.md

# Setup and Quickstart

{% hint style="warning" %}
Qodo CLI tool is currently **not supported** for on-prem environments.
{% endhint %}

## Installation

To use Qodo CLI tool, you’ll need [Node.js](https://nodejs.org/en/download) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.

To install, run:

```bash
npm install -g @qodo/command
```

***

## Starting to use Qodo CLI tool

To start using Qodo CLI tool, you need to log in first:

```bash
qodo login
```

<figure><img src="https://content.gitbook.com/content/E9WGt1PJng9hG0nmGaiF/blobs/87Mj3ySZNADolovu20Tg/Screenshot%202025-06-18%20at%2015.04.03.png" alt="" width="563"><figcaption></figcaption></figure>

### API key

Once login is completed you'll receive an **API key in the terminal**.

The API key is also saved locally in the `.qodo` folder in your home dir, and can be reused (e.g., in CI).

The key is tied to your user account and subject to the same usage limits.

There are a few commands that let you maintain the API key:

```bash
qodo key list               # List all API keys

qodo key create <name>      # Create a new API key with the given name

qodo key revoke <name>      # Revoke an API key by name
```

***

## Quickstart

### Qodo CLI tool **- Interactive AI Chat Mode**

Run [Qodo Command](https://docs.qodo.ai/qodo-documentation/qodo-gen/qodo-gen-chat) directly in your terminal:

```bash
qodo chat
```

In this mode you can send prompts such as:

```
Write tests for the files in the auth directory

Add better logging througout my project

Use Qodo Merge to describe the changes in my working folder
```

And Qodo will follow your guidelines.

The response is a markdown-formatted output.

You can exit at any time by pressing `Escape`.

***

### Agents

An agent is a configurable AI-powered assistant that can perform tasks, automate workflows, and interact with tools (MCPs). Each agent is defined by a set of instructions, optional arguments, and access to tools like version control, the file system, CI pipelines, or cloud environments.

Agents act as **task-specific operators**. You can think of them as highly focused copilots, each with a clear objective and strategy. Rather than manually guiding an AI through each step, you define the desired behavior once and reuse it reliably.

You can [create your own agent](https://docs.qodo.ai/qodo-documentation/qodo-command/features/creating-and-managing-agents) for Qodo CLI tool to use, then run Qodo with a customizable command.

{% hint style="success" %}
[Learn more about creating and managing agents with Qodo CLI tool.](https://docs.qodo.ai/qodo-documentation/qodo-command/features/creating-and-managing-agents)
{% endhint %}

***

### Tools (MCPs)

MCP stands for Model Context Protocol. It’s an open protocol that standardizes how applications provide context to AI Models. You can [learn more about MCPs in Anthropic's MCP documentation](https://modelcontextprotocol.io/introduction).

Using the MCP protocol, Qodo CLI tool can interact with external tools and services.

The tools currently being used by Qodo are:

**Local tools:**

* git
* filesystem
* shell
* `ripgrep`

**Remote tools:**

* web search
* Qodo Merge

You can control which tools will be used with [the `--tools` flag](https://docs.qodo.ai/qodo-documentation/qodo-command/getting-started/list-of-cli-commands-and-flags).&#x20;

***

### Interactive Web UI Mode

Use the Qodo web interface:

```bash
qodo --ui
```

The interactive web UI mode features full interactivity, and the same capabilities as in the terminal.

<figure><img src="https://content.gitbook.com/content/E9WGt1PJng9hG0nmGaiF/blobs/fzUU50nknBItrNQQ9rP2/image.png" alt="" width="563"><figcaption></figcaption></figure>

***

### AI Model selection

You can use a specific AI model with `--model=<model_name>`.

For a list of available model names, run `qodo models`.

***

## Learn More

### GitHub Example Repository

Find working examples and templates: <https://github.com/qodo-ai/qodo-gen-cli>

### Commands and Flags

[Learn more about Command available commands and flags in our documentation.](https://docs.qodo.ai/qodo-documentation/qodo-command/getting-started/list-of-cli-commands-and-flags)
