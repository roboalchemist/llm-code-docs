# Source: https://flatfile.com/docs/reference/cli.md

# CLI Reference

> Command line interface for developing, deploying, and managing Flatfile Agents

The Flatfile Command Line Interface (CLI) provides tools to develop, deploy, and manage [Listeners](/core-concepts/listeners) in your Flatfile environment.

<Note>
  Once listeners are deployed and hosted on Flatfile's secure cloud, they are
  called Agents.
</Note>

## Installation

```bash
npx flatfile@latest <command>
```

## Configuration

### Authentication

The CLI requires your Flatfile API key and Environment ID, provided either in Environment variables (ideally in a `.env` file) or as command flags. You can find your API key and Environment ID in your Flatfile dashboard under "[API Keys and Secrets](https://platform.flatfile.com/dashboard/keys-and-secrets)".

<Note>
  **Recommended approach:** Use a `.env` file in your project root for secure,
  convenient, and consistent authentication. If you're using Git, make sure to
  add `.env` to your `.gitignore` file.
</Note>

**Using `.env` file**

Create a `.env` file in your project root:

```bash
# .env file
FLATFILE_API_KEY="your_api_key_here"
FLATFILE_ENVIRONMENT_ID=your_environment_id_here
```

This approach keeps credentials out of your command history and makes it easy to switch between environments.

**Using command flags**

For one-off commands or CI/CD environments:

```bash
npx flatfile develop --token YOUR_API_KEY --env YOUR_ENV_ID
```

### Regional Servers

For improved performance and compliance, Flatfile supports regional deployments:

| Region | API URL                      |
| ------ | ---------------------------- |
| US     | platform.flatfile.com/api    |
| UK     | platform.uk.flatfile.com/api |
| EU     | platform.eu.flatfile.com/api |
| AU     | platform.au.flatfile.com/api |
| CA     | platform.ca.flatfile.com/api |

Set your regional URL in `.env`:

```bash
FLATFILE_API_URL=platform.eu.flatfile.com/api
```

<Tip>
  Contact support to enable regional server deployment for your account.
</Tip>

## Development Workflow

<Steps>
  <Step title="Develop Locally">
    Use `develop` to run your listener locally with live reloading
  </Step>

  <Step title="Deploy to Production">
    Use `deploy` to push your listener to Flatfile's cloud as an Agent
  </Step>

  <Step title="Manage Agents">
    Use `agents` commands to list, download, or delete deployed agents
  </Step>
</Steps>

<Warning>
  Use separate environments for development and production to avoid conflicts.
  The CLI will warn you when working in an environment with existing agents.
</Warning>

## Commands

### develop

Run your listener locally with automatic file watching and live reloading.

```bash
npx flatfile develop [file-path]
```

**Options**

| Option        | Description                                          |
| ------------- | ---------------------------------------------------- |
| `[file-path]` | Path to listener file (auto-detects if not provided) |
| `--token`     | Flatfile API key                                     |
| `--env`       | Environment ID                                       |

**Features**

* Live reloading on file changes
* Real-time HTTP request logging
* Low-latency event streaming (10-50ms)
* Event handler visibility

**Example output**

```bash
> npx flatfile develop
✔ 1 environment(s) found for these credentials
✔ Environment "development" selected
ncc: Version 0.36.1
ncc: Compiling file index.js into CJS
  ✓ 427ms      GET    200 https://platform.flatfile.com/api/v1/subscription 12345

 File change detected. 🚀
  ✓ Connected to event stream for scope us_env_1234
 ▶ commit:created  10:13:05.159 AM us_evt_1234
 ↳ on(**, {})
 ↳ on(commit:created, {"sheetSlug":"contacts"})
```

***

### deploy

Deploy your listener as a Flatfile Agent.

```bash
npx flatfile deploy [file-path] [options]
```

**Options**

| Option         | Description                                          |
| -------------- | ---------------------------------------------------- |
| `[file-path]`  | Path to listener file (auto-detects if not provided) |
| `--slug`, `-s` | Unique identifier for the agent                      |
| `--ci`         | Disable interactive prompts for CI/CD                |
| `--token`      | Flatfile API key                                     |
| `--env`        | Environment ID                                       |

**File detection order**

1. `./index.js`
2. `./index.ts`
3. `./src/index.js`
4. `./src/index.ts`

**Examples**

```bash
# Basic deployment
npx flatfile deploy

# Deploy with custom slug
npx flatfile deploy --slug my-agent

# CI/CD deployment
npx flatfile deploy ./src/listener.ts --ci
```

**Multiple agents**

Deploy multiple agents to the same environment using unique slugs:

```bash
npx flatfile deploy --slug agent-one
npx flatfile deploy --slug agent-two
```

<Note>
  Without a slug, the CLI updates your existing agent or creates one with slug
  `default`.
</Note>

***

### agents list

Display all deployed agents in your environment.

```bash
npx flatfile agents list
```

Shows each agent's:

* Agent ID
* Slug
* Deployment status
* Last activity

***

### agents download

Download a deployed agent's source code.

```bash
npx flatfile agents download <slug>
```

**Use cases**

* Examine deployed code
* Modify existing agents
* Back up source code
* Debug deployment issues

<Tip>Use `agents list` to find the agent slug you need.</Tip>

***

### agents delete

Remove a deployed agent.

```bash
npx flatfile agents delete <slug>
```

**Options**

| Option             | Description                  |
| ------------------ | ---------------------------- |
| `--agentId`, `-ag` | Use agent ID instead of slug |

***

## Related Resources

* [Listeners](/core-concepts/listeners) - Core concept documentation
* [Events](/reference/events) - Event system reference
