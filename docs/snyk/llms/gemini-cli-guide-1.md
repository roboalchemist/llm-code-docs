# Source: https://docs.snyk.io/integrations/snyk-studio-agentic-integrations/quickstart-guides-for-snyk-studio/gemini-cli-guide-1.md

# Goose CLI guide

You can access Snyk Studio, including Snyk's MCP server, in Goose CLI to secure code generated with agentic workflows through an LLM. This can be achieved in several ways. When you use it for the first time, the MCP server will ask for trust and trigger authentication if necessary.

## Prerequisites

* [Install the Goose CLI](#install-goosecli)
* [Install the Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli)
* [Install the Snyk MCP Server in Goose CLI using npx command](#install-the-snyk-mcp-server-in-goose-cli-using-npx-command) or [Install the Goose MCP Server in Goose CLI using Snyk CLI](#install-the-snyk-mcp-server-in-goose-cli-using-snyk-cli)

### Install GooseCLI

Install the GooseCLI. For mode details, see the official [Goose CLI installation instructions.](https://block.github.io/goose/docs/quickstart)

### Install the Snyk MCP Server in Goose CLI using npx command

This installation instruction assumes you have a Node.js local development environment setup with the `npx` executable.

To install the Snyk MCP Server using the Goose CLI interactive session, proceed with the following instructions:

* Start an interactive Goose configuration wizard by running the `goose configure` command:\\

  <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1819b8f04e316b59b8795c1b74093b19e6385cb3%2Fimage%20(288).png?alt=media" alt=""><figcaption></figcaption></figure>
* From the configuration menu, chose **Add Extension.**
* Choose **Command-line extension (run a local command or script).**
* Name this extension **Snyk Security.**
* Run the command by typing in: `npx -y snyk@latest mcp -t stdio`
* Continue with the defaults (timeout of 300 seconds), and optionally provide the Snyk API token if your Organization policy requires one.

A complete Goose configuration walkthrough should look as follows:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a45e57e5b60631e819108fcdafa6fc50b78aedd9%2Fimage%20(289).png?alt=media" alt=""><figcaption></figcaption></figure>

Start or resume your Goose session with the Snyk MCP server enabled.

### Install the Snyk MCP Server in Goose CLI using Snyk CLI

This installation instruction assumes you have installed the Snyk CLI and the `snyk` executable is available in your system's path.

Install the Snyk MCP Server using the Goose CLI interactive session by following these instructions:

* Start an interactive Goose configuration wizard by running the `goose configure` command.
* Choose **Add Extension f**rom the configuration menu.
* Select **Command-line extension (run a local command or script).**
* Name this extension **Snyk Security.**
* Run the command by typing in: `/path/to/snyk mcp -t stdio` - replacing `/path/to/snyk` with the fully qualified absolute path to your Snyk CLI.
* Continue with the defaults (timeout of 300 seconds), and optionally provide the Snyk API token if your Organization policy requires one.

{% hint style="info" %}
If you installed `snyk` using npm as a global module and you are using fnm to manage your versions, then you must specify the full path to the `snyk` executable. The path may look like this: `/Users/username/.local/state/fnm_multishells/8831_1753881185071/bin/snyk`.
{% endhint %}

Start or resume your Goose session with the Snyk MCP server enabled.

## Setting up the Snyk MCP Server

As a one-time setup, you may need to authenticate and trust the Project directory. If required, the agentic workflow will likely manage this automatically.

These workflows are mostly automatically executed by the underlying model and the agentic code assistant, and you will need to approve them using a browser confirmation dialog.

You can explicitly prompt to authenticate your account as follows:

```
Authenticate my Snyk account
```

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-916c73df40e72e8e1d5b6db7aac1db75920a177d%2Fimage%20(291).png?alt=media" alt=""><figcaption></figcaption></figure>

If you are not authenticated, this prompt opens a browser for you to authenticate to the Snyk Web UI, and then you can continue with the agent.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-69dd58982b2ea79470503c533166ebe742fa07df%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

## Examples

### Scanning for security vulnerabilities

In the chat, you can tag specific files or functions and ask the agent to scan your code and third-party dependencies of the Project.

{% code title="prompt" overflow="wrap" %}

```
Scan this directory for code security & dependency vulnerabilities and security issues
```

{% endcode %}

Goose CLI invokes Snyk scanning, providing output, and insights based on the results that Snyk returned:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f48164fbbbb56759b8347338d72672b415a98322%2Fimage%20(292).png?alt=media" alt=""><figcaption></figcaption></figure>

### "Secure at inception" rules

To practice [Secure at Inception](https://docs.snyk.io/discover-snyk/getting-started/glossary#secure-at-inception), Snyk recommends adopting rules that align the LLM for secure code generation and workflows.

The following is a suggested instruction to use with [Goose CLI recipes](https://block.github.io/goose/docs/guides/recipes/session-recipes) or with [Goose hints file](https://block.github.io/goose/docs/guides/using-goosehints). Add the following contents to the `.goosehints` file in the root directory of the Project:

{% code title=".goosehints" overflow="wrap" %}

```
# Project security best practices

- Always run **snyk_code_scan** tool for new first party code that is generated in a Snyk-supported language.
- If any security issues are found based on newly introduced or modified code or dependencies, attempt to fix the issues using the results context from **Snyk**.
- Rescan the code after fixing the issues to ensure that the issues were fixed and that there are no newly introduced issues.
- Repeat this process until no new issues are found.
```

{% endcode %}
