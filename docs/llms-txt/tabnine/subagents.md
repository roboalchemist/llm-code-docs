# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/subagents.md

# Subagents

A subagent is a specialized agent that runs under the main Tabnine Agent. Each subagent focuses on a narrower domain, such as code review, security scanning, refactoring, or documentation. The main agent delegates specific tasks to subagents when that specialization improves the quality, accuracy, or clarity of the result.

### How Subagents Are Used <a href="#how-subagents-are-used" id="how-subagents-are-used"></a>

When you ask the agent to perform a complex or multi-step task, it may:

1. Decide that a particular part of the task is best handled by a subagent.
2. Route that part of the conversation or a specific tool call to the subagent.
3. Collect the subagent’s result and integrate it back into the overall answer.

You generally do not need to interact with subagents directly. Instead, you describe the outcome you want, and the system selects and coordinates the relevant subagents automatically.

### Relationship to Extensions <a href="#relationship-to-extensions" id="relationship-to-extensions"></a>

Subagents can be provided by:

* Core Tabnine functionality, bundled with the CLI.
* Installed extensions, which may define additional subagents specialized for particular tools, frameworks, or workflows.

When you enable or disable extensions, any subagents they define become available or unavailable accordingly.

> **Note:** Subagents are currently an experimental feature.

To use custom subagents, you must explicitly enable them in your `settings.json`:

```json
{
  "experimental": { "enableAgents": true }
}
```

**Warning:** Subagents currently operate in a “YOLO mode,” meaning they may execute tools without asking for confirmation for each individual action. Use caution when defining agents that can access powerful tools such as `run_shell_command` or `write_file`.

### What Are Subagents? <a href="#what-are-subagents" id="what-are-subagents"></a>

Subagents act as focused “specialists” that the main Tabnine Agent can call for particular kinds of work.

* **Focused context:** Each subagent has its own system prompt and persona.
* **Specialized tools:** Subagents can be configured with a limited or specialized set of tools.
* **Independent context window:** Interactions with a subagent occur in a separate context loop, which helps keep the main conversation history compact.

Subagents are exposed to the main agent as tools named after the subagent. When the main agent invokes one of these tools, it delegates the task to the corresponding subagent. After the subagent completes its work, it returns its findings to the main agent, which then incorporates them into the overall response.

### Built-in Subagents <a href="#built-in-subagents" id="built-in-subagents"></a>

Tabnine CLI includes several built-in subagents.

#### Codebase Investigator <a href="#codebase-investigator" id="codebase-investigator"></a>

* **Name:** `codebase_investigator`
* **Purpose:** Analyze the codebase, reverse engineer behavior, and understand complex dependencies.
* **When to use:** Questions such as “How does the authentication system work?” or “What are the dependencies of the `AgentRegistry` class?”
* **Configuration:** Enabled by default. You can configure it in `settings.json`. For example, to force a specific model:&#x20;

```json
{
  "agents": {
    "overrides": {
      "codebase_investigator": {
        "enabled": true,
        "runConfig": { "maxTurns": 20 },
        "modelConfig": { "model": "..." }
      }
    }
  }
}
```

#### Remote Codebase Investigator <a href="#remote-codebase-investigator" id="remote-codebase-investigator"></a>

* **Name:** `remote-codebase-investigator`
* Purpose: Tabnine-only built-in subagent for investigating remote codebases
* **When to use:** Similar to `codebase_investigator` but for remote codebases
* **Configuration:** Available at runtime. Defined at `packages/core/src/tabnine/agents/subagents/remote-codebase-investigator.md` and registered in `registry.ts`

#### Generalist Agent <a href="#generalist-agent" id="generalist-agent"></a>

* **Name:** `generalist`
* **Purpose:** A general-purpose AI agent with access to all tools.
* **When to use:** Highly recommended for tasks that are turn-intensive or involve processing large amounts of data
* **Configuration:** Enabled by default. No additional configuration options.

#### Browser Agent <a href="#browser-agent" id="browser-agent"></a>

* **Name:** `browser_agent`
* **Purpose:** Automate web browser tasks such as navigating websites, filling out forms, clicking buttons, and extracting information from web pages, using the browser’s accessibility tree.
* **When to use:** Scenarios like “Go to [Example Domain](http://example.com/) and fill out the contact form,” “Extract the pricing table from this page,” or “Click the login button and enter my credentials.”

> **Note:** This is a preview feature and is still under active development.

**Prerequisites**

The browser agent requires:

* **Chrome** version 144 or later (any recent stable release is sufficient).
* **Node.js** with `npx` available (used to launch the `chrome-devtools-mcp` server).

**Enabling the Browser Agent**

The browser agent is disabled by default. Enable it in your `settings.json`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    }
  }
}
```

**Session Modes**

The `sessionMode` setting controls how Chrome is launched and managed. Configure it under `agents.browser`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "sessionMode": "persistent"
    }
  }
}
```

The available modes are:

| Mode         | Description                                                                                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `persistent` | **(Default)** Launches Chrome with a persistent profile stored at `~/.tabnine/agent/cli-browser-profile/`. Cookies, browsing history, and settings are preserved across sessions.          |
| `isolated`   | Launches Chrome with a temporary profile that is deleted after each session. Suitable when you require a clean environment for each run.                                                   |
| `existing`   | Attaches to an already running Chrome instance. You must enable remote debugging first by navigating to `chrome://inspect/#remote-debugging` in Chrome. No new browser process is started. |

**Configuration reference**

All browser-specific settings are configured under `agents.browser` in your `settings.json`.

| Setting       | Type      | Default        | Description                                                                    |
| ------------- | --------- | -------------- | ------------------------------------------------------------------------------ |
| `sessionMode` | `string`  | `"persistent"` | Controls how Chrome is managed: `"persistent"`, `"isolated"`, or `"existing"`. |
| `headless`    | `boolean` | `false`        | If `true`, runs Chrome in headless mode (no visible window).                   |
| `profilePath` | `string`  | —              | Optional custom path to a browser profile directory.                           |
| `visualModel` | `string`  | —              | Optional model override for the visual agent (for example, `"gpt-5.2-codex"`). |

**Security**

The browser agent enforces several security restrictions:

* **Blocked URL patterns:** `file://`, `javascript:`, `data:text/html`, `chrome://extensions`, and `chrome://settings/passwords` *may* be blocked by the external `chrome-devtools-mcp` package rather than by Tabnine CLI itself.
* **Sensitive action confirmation:** Actions such as form filling, file uploads, and form submissions may require explicit confirmation, in line with the policy configuration.

**Visual Agent**

By default, the browser agent interacts with pages through the accessibility tree, addressing elements by their `uid` values. For tasks that require visual identification (for example, “click the yellow button” or “locate the red error message”), you can enable the visual agent by setting a `visualModel`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "visualModel": "gpt-5.2-codex"
    }
  }
}
```

When the visual agent is enabled, the browser agent gains access to the `analyze_screenshot` tool. This tool captures a screenshot and sends it to the vision model for analysis. The model returns coordinates and element descriptions that the browser agent uses together with the `click_at` tool for precise, coordinate-based interactions.

> **Note:** The visual agent requires API key or Vertex AI authentication and is not available when using Google Login.

### Creating Subagents <a href="#creating-subagents" id="creating-subagents"></a>

You can create your own subagents to automate specific workflows or enforce specific personas. To use custom subagents, ensure they are enabled in your `settings.json`:

```json
{
  "experimental": {
    "enableAgents": true
  }
}
```

#### Agent Definition Files <a href="#agent-definition-files" id="agent-definition-files"></a>

Custom agents are defined as Markdown (`.md`) files with YAML frontmatter. You can place them in:

1. **Project-level:** `.tabnine/agent/agents/*.md` (shared with your team)
2. **User-level:** `~/.tabnine/agent/agents/*.md` (personal agents)

#### File Format <a href="#file-format" id="file-format"></a>

Each file must begin with YAML frontmatter enclosed in triple dashes `---`. The body of the Markdown file becomes the agent’s system prompt.

**Example:** `.tabnine/``agents``/security-auditor.md`

```md
---
name: security-auditor
description: Specialized in finding security vulnerabilities in code.
kind: local
tools:
  - read_file
  - grep_search
model: gpt-5.2-codex
temperature: 0.2
max_turns: 10
---
You are a ruthless Security Auditor. Your job is to analyze code for potential
vulnerabilities.
Focus on:
1. SQL Injection
2. XSS (Cross-Site Scripting)
3. Hardcoded credentials
4. Unsafe file operations
When you find a vulnerability, explain it clearly and suggest a fix. Do not fix
it yourself; just report it.
```

#### Configuration Schema <a href="#configuration-schema" id="configuration-schema"></a>

| Field          | Type   | Required | Description                                                                                                                           |
| -------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | string | Yes      | Unique identifier (slug) used as the tool name for the agent. Must contain only lowercase letters, numbers, hyphens, and underscores. |
| `description`  | string | Yes      | Short description of what the agent does. Used by the main agent to decide when this subagent is appropriate.                         |
| `kind`         | string | No       | Either `local` (default) or `remote`.                                                                                                 |
| `tools`        | array  | No       | List of tool names that this agent can use. If omitted, it may inherit a default tool set.                                            |
| `model`        | string | No       | Specific model to use (for example, `gpt-5.2-codex`). Defaults to `inherit`, meaning it uses the main session model.                  |
| `temperature`  | number | No       | Model temperature (0.0–2.0).                                                                                                          |
| `max_turns`    | number | No       | Maximum number of conversation turns allowed for this agent before it must return. Defaults to `15`.                                  |
| `timeout_mins` | number | No       | Maximum execution time in minutes. Defaults to `5`.                                                                                   |

#### Optimizing your subagent <a href="#optimizing-your-subagent" id="optimizing-your-subagent"></a>

The main agent’s system prompt encourages it to rely on expert subagents when they are available. It decides whether a subagent is relevant based largely on that subagent’s description. You can improve how consistently a subagent is used by making its description clear about:

* Its area of expertise.
* When it should be preferred.
* Concrete example scenarios.

For example, the following description is likely to be chosen reliably for Git-related operations:

> Git expert agent that should be used for all local and remote git operations. For example: making commits, searching for regressions with bisect, and interacting with source control and issues providers such as GitHub.

If you want to fine-tune usage, select the model you want to optimize for (with `/model`), then ask the model why it did or did not call your subagent for a given prompt and description. Use that feedback to refine the description and examples.
