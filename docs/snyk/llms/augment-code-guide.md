# Source: https://docs.snyk.io/integrations/snyk-studio-agentic-integrations/quickstart-guides-for-snyk-studio/augment-code-guide.md

# Augment Code guide

Add Snyk Studio to Augment Code to secure code generated with agentic workflows through a Large Language Model (LLM). You can achieve this in several ways. When you use it for the first time, Snyk Studio asks for trust and, if necessary, trigger authentication.

## Prerequisites

* [Install the code assistant extension](https://www.augmentcode.com/)
* [Install the Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli)
* [Install the Snyk MCP](#install-the-snyk-mcp-server-in-augment-code)

### Install Augment Code

Visit the [Augment Code](https://www.augmentcode.com/) website to download the correct version of the IDE plugin.

### Install the Snyk MCP Server in Augment Code

Install the Snyk MCP Server using the method that best suits your operating system and local development environment.

#### Install with Node.js and npx

* Name: Snyk
* Command: npx -y snyk\@latest mcp -t stdio

#### Install with pre-installed Snyk CLI

* Name: Snyk
* Command: /absolute/path/to/snyk mcp -t stdio

If the `snyk` command is not available, add it by following the instructions on the [Installing or updating the Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli) page.

## Setting up the Snyk MCP Server

The MCP Server starts automatically. The following example shows a Snyk MCP Server that was successfully configured and started.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FjPT4JTc4Fcf32Hk7thCg%2Fimage.png?alt=media&#x26;token=834a6e7e-fb6c-4ee5-bac1-b92e7b350641" alt=""><figcaption></figcaption></figure>

As a one-time setup, authenticate and trust the current Project directory. If required, the agentic workflow will likely manage this automatically.

If you are already authenticated with the Snyk CLI installed on your system path, or through a prior interaction, then proceed to work with the Snyk MCP Server.

## Examples <a href="#examples" id="examples"></a>

### Scanning for security vulnerabilities <a href="#scanning-for-security-vulnerabilities" id="scanning-for-security-vulnerabilities"></a>

In the chat, you can tag specific files or functions and ask Augment Code to scan your code for safe deployment to production.

```
Scan this directory for code security & dependency vulnerabilities and security issues
```

Augment Code indicates that this request is related to security vulnerability scanning and calls the Snyk MCP Server for various scans.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FR16GXH8dh4YSzxvsfU16%2Fimage.png?alt=media&#x26;token=1b139db3-67ec-4b3c-99f3-bb380a0216aa" alt=""><figcaption></figcaption></figure>

### "Secure at inception" rules

To practice [Secure at Inception](https://docs.snyk.io/discover-snyk/getting-started/glossary#secure-at-inception), Snyk recommends adopting rules that align the LLM for secure code generation and workflows.

The following is a suggested instruction for Augment Code user guidelines:

```
- Always run Snyk Code scanning tool for new first party code generated.
- Always run Snyk SCA scanning tool for new dependencies or dependency updates.
- If any security issues are found based on newly introduced or modified code or dependencies, attempt to fix the issues using the results context from Snyk.
- Rescan the code after fixing the issues to ensure that the issues were fixed and that there are no newly introduced issues.
- Repeat this process until no issues are found.
```

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FF7RlBDQUIEUB361TScfO%2Fimage.png?alt=media&#x26;token=4c9a89cc-9662-43d8-b60e-b44685f18131" alt=""><figcaption></figcaption></figure>
