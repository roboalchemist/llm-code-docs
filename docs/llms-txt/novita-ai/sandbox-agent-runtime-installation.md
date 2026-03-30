# Source: https://novita.ai/docs/guides/sandbox-agent-runtime-installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation

This feature is currently in **beta**. You need to install the beta versions of both the Novita Sandbox Python SDK and the CLI tool:

***

## Install Python SDK with pip

Use the `--pre` flag to install the latest beta version:

```bash  theme={"system"}
pip install --pre novita-sandbox
```

***

## Install Node.js CLI

### Option 1: Run with npx (Recommended)

Install the beta CLI locally in your project directory using `npm`, then run it with `npx`. This avoids polluting your global environment with the beta version.

```bash  theme={"system"}
# Install the latest beta version CLI
npm install novita-sandbox-cli@beta

# First, complete authentication
npx novita-sandbox-cli auth login

# Run agent configure command to configure your Agent
npx novita-sandbox-cli agent configure
```

### Option 2: Global Installation

If you use the CLI frequently, you can install it globally:

```bash  theme={"system"}
# Install the latest beta version
npm install -g novita-sandbox-cli@beta
```

After installation, you can use the command directly:

```bash  theme={"system"}
novita-sandbox-cli agent configure
```


Built with [Mintlify](https://mintlify.com).