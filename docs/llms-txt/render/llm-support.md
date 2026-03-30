# Source: https://render.com/docs/llm-support.md

# Using Render with Coding Agents — Deploy and manage apps using LLM-powered tools.

Render integrates with popular coding agents to help you manage your infrastructure, diagnose issues, and learn about the platform.

## Agent skills

Render's official *skills* enable agents to deploy, debug, and monitor your apps. Use skills with popular tools like Codex, Claude Code, and Cursor.

### Install

**Render CLI (recommended)**

##### Render CLI

> *Requires version 2.10 or later of the [Render CLI](cli).*
>
> Check your current version with `render --version`

Run the following command:
```shell
render skills install
```

The CLI detects supported tools on your system (Claude Code, Codex, Cursor, OpenCode) and prompts you to select which skills to install.

You can also specify options directly for non-interactive use:

```shell
render skills install --tool cursor --skill render-deploy --skill render-debug
```

See the [CLI docs](cli#common-commands) for the full list of `skills` subcommands, including `update`, `remove`, and `list`.

**Install script**

##### Quick-install script

Run the following script to automatically detect popular supported tools (Claude Code, Cursor, etc.) on your system and install Render's official skills for each:

```shell
curl -fsSL https://raw.githubusercontent.com/render-oss/skills/main/scripts/install.sh | bash
```

The output looks like this:

[image: Running the quick-install script]

**Codex**

##### Codex installation

Render provides a curated skill in the Codex skill installer. Run the following in Codex:

```codex
$skill-installer render-deploy
```

**Manual installation**

##### Manual installation

1. Clone the [Render Skills GitHub repository](https://github.com/render-oss/skills).
2. From the repo's `skills/` directory, copy each skill directory into your tool's skills directory.

    Default skills directories for popular tools are listed below:

| Tool | Skills Directory |
| --- | --- |
| Claude Code | `~/.claude/skills/<skill-name>/` |
| Codex | `~/.codex/skills/<skill-name>/` |
| Cursor | `~/.cursor/skills/<skill-name>/` |
| OpenCode | `~/.config/opencode/skills/<skill-name>/` |

> Depending on your tool, you might need to restart it after installing.

After installing, you can invoke the skill using your tool's syntax (usually a `/` or `$` symbol followed by the skill name). Your tool also invokes the skill automatically to fulfill relevant prompts.

[image: Invoking the render-deploy skill in Codex]

### Supported skills

| Skill | Description |
| --- | --- |
| *render-deploy* | Deploy applications using IaC with Render Blueprints or directly via MCP. Includes automatic codebase analysis and environment variable management. |
| *render-debug* | Debug deployment issues using logs, metrics, and database queries. Detects common issues like missing environment variables, port binding errors, and resource constraints. |
| *render-monitor* | Monitor service health, performance metrics, logs, and resource usage in real-time. |

### Example prompts

Ask your tool to perform any of these tasks:

> Deploy my application to Render

> Debug my Render deployment

> Is my Render service healthy?

Your tool will invoke the appropriate set of skills and guide you through the process.

## Jules integration

[Jules by Google Labs](https://jules.google/?utm_source=render) provides a managed integration with Render. Whenever you open a pull request in your service's repo, Jules can detect failures in your service's preview build and automatically push fixes to address them.

#### Prerequisites

- Your Render service's repo must be hosted on GitHub.
- Jules must have access to your service's repo.
- [Pull request previews](service-previews#pull-request-previews-git-backed) must be enabled for your service.
    - These are the preview builds that Jules uses to detect and address issues.

#### Setup

1. Go to [dashboard.render.com/jules](https://dashboard.render.com/jules).

    This opens the API Keys section of your user settings with a Jules-specific section:

    [image: Jules API Keys section]

2. Next to the *Jules by Google Labs* section, click *+ Create API Key*.

    A creation dialog appears.

3. Review and accept the terms for Render's Jules integration, then click *Create API Key*.

4. Copy the created API key to your clipboard.

5. Open your [Jules integrations page](https://jules.google.com/settings/integrations?utm_source=render):

    [image: Jules integrations page]

6. Under the *Render* integration, paste the API key you copied and submit it.

You're all set! Whenever a pull request preview fails for your repo, Jules will automatically analyze its logs to identify the root cause and push a fix to address it.

You can also *enable MCP features* to use Render's official [MCP server](mcp-server) with the Jules agent:

[image: Enabling MCP features in Jules]

You can disconnect the integration at any time by deleting the API key from the Jules integrations page.

## Render MCP server

Connect to Render's official MCP server to manage your Render infrastructure directly from apps like Cursor and Claude Code:

[video]

The MCP server provides tools for actions such as:

- Spinning up new services
- Querying databases
- Analyzing metrics and logs

It's especially useful for helping you identify and resolve issues with service deploys.

## Documentation features

The Render documentation provides the following capabilities to improve content discoverability and parsing for LLMs:

### Articles as markdown

Each article under `render.com/docs/` is available in a simplified markdown format that's well suited for LLMs.

Obtain an article's markdown version by doing any of the following:

- Append `.md` to the end of an article's URL:

    ```
    https://render.com/docs/llm-support.md
    ```
- Include an `Accept: text/markdown` header in your request to an article's URL (no `.md` extension required).
    - Agentic tools like Claude Code often include this header in their HTTP requests by default.
- Click *Copy page* in the top-right corner of an article to copy its markdown version to your clipboard (not available on smaller screen widths).

### Reading `llms.txt` and `llms-full.txt`

The Render documentation includes `llms.txt` and `llms-full.txt` files at the following URLs:

```
https://render.com/docs/llms.txt
https://render.com/docs/llms-full.txt
```

| File | Description |
| --- | --- |
| [`llms.txt`](llms.txt) | Provides a summary of the Render documentation, including links and descriptions of each article. |
| [`llms-full.txt`](llms-full.txt) | Combines most of the Render documentation into a single, simplified markdown file. Some content types are omitted for brevity. |

### Docs via MCP

> *This feature is experimental.*
>
> Render might discontinue support for this documentation-specific MCP server at any time in the future.

Render's primary [MCP server](#render-mcp-server) does not yet provide tools for querying the Render documentation.

To query the Render docs from LLMs, you can connect your app or agent to the following additional MCP server:

```
https://mcp.inkeep.com/render/mcp
```

This MCP server provides "tools" for searching and asking questions about the Render docs. It uses the same LLM-powered answer engine as the *Ask AI* assistant in the documentation.