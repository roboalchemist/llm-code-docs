# Source: https://circleci.com/product/mcp.md

# CircleCI MCP Server

Connect your AI assistant to your CircleCI data to debug failures, analyze test results, and improve pipelines using natural language.

   

## CI/CD context for AI tools

The CircleCI MCP server makes your build system understandable by AI tools like Cursor, Claude Code, Windsurf, and more. It’s built on the Model Context Protocol (MCP), a lightweight standard that allows LLM-powered agents to fetch structured data from external systems.

By connecting to the CircleCI MCP Server, agents gain real-time visibility into:

*   Build logs and test outputs
*   Pipeline statuses
*   Recent configuration changes
*   Workflow performance metrics

That means instead of digging through job logs or dashboard UIs, you can ask:

```plaintext
why did my last build fail?
```

and get all the context you need to fix the issue and keep moving without breaking stride.

## Turn build data into action

Once installed, the MCP server makes your CI/CD data accessible through natural language. LLM-based tools can:

*   **Diagnose failing builds**  
    Get structured error summaries and logs.
  
*   **Trace failures to recent changes**  
    Connect regressions to commits, diffs, or workflows.
  
*   **Spot flaky tests**  
    Surface instability patterns from test history.
  
*   **Recommend improvements**  
    Suggest config or timing optimizations in context.
  
*   **Bring CI data into your editor**  
    Use LLM tools to reason through builds without switching tabs.

With access to both code and build context, these tools can help you fix bugs faster, ship changes with confidence, and stay focused on the work that matters.

## Get started with MCP

The CircleCI MCP Server runs locally and integrates with a variety of editors and LLM development tools.

Below are ready-to-use configuration examples to help you install the MCP server in your preferred environment.

### Prerequisites

Before setting up your IDE, make sure you have the following:

*   **[CircleCI Personal API Token (PAT)](https://circleci.com/docs/guides/toolkit/managing-api-tokens/#creating-a-personal-api-token):**
    *   Go to **[User Settings > Personal API Tokens](https://app.circleci.com/settings/user/tokens)**
    *   Click **Create New Token**
    *   Copy and store it securely — you’ll use it as `CIRCLECI_TOKEN` during setup
*   **For NPX installation:**
    *   [pnpm package manager](https://pnpm.io/installation)
    *   Node.js version ≥ 18.0.0
*   **For Docker installation:**
    *   [Docker](https://docs.docker.com/get-docker/)

### Configuration instructions

Cursor

**Using NPX:**

```

{
  "mcpServers": {
    "circleci-mcp-server": {
      "command": "npx",
      "args": ["-y", "@circleci/mcp-server-circleci@latest"],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com"
      }
    }
  }
}
    
```

**Using Docker:**

```

{
  "mcpServers": {
    "circleci-mcp-server": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CIRCLECI_TOKEN",
        "-e", "CIRCLECI_BASE_URL",
        "circleci/mcp-server-circleci"
      ],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com"
      }
    }
  }
}
    
```

[Cursor setup docs](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)

VS Code

**Using NPX:**

```

{
  "inputs": [
    {
      "type": "promptString",
      "id": "circleci-token",
      "description": "CircleCI API Token",
      "password": true
    },
    {
      "type": "promptString",
      "id": "circleci-base-url",
      "description": "CircleCI Base URL",
      "default": "https://circleci.com"
    }
  ],
  "servers": {
    "circleci-mcp-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@circleci/mcp-server-circleci@latest"],
      "env": {
        "CIRCLECI_TOKEN": "${input:circleci-token}",
        "CIRCLECI_BASE_URL": "${input:circleci-base-url}"
      }
    }
  }
}
    
```

**Using Docker:**

```

{
  "inputs": [
    {
      "type": "promptString",
      "id": "circleci-token",
      "description": "CircleCI API Token",
      "password": true
    },
    {
      "type": "promptString",
      "id": "circleci-base-url",
      "description": "CircleCI Base URL",
      "default": "https://circleci.com"
    }
  ],
  "servers": {
    "circleci-mcp-server": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CIRCLECI_TOKEN",
        "-e", "CIRCLECI_BASE_URL",
        "circleci/mcp-server-circleci"
      ],
      "env": {
        "CIRCLECI_TOKEN": "${input:circleci-token}",
        "CIRCLECI_BASE_URL": "${input:circleci-base-url}"
      }
    }
  }
}
    
```

[VS Code setup docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

Claude Desktop

**Using NPX:**

```

{
  "mcpServers": {
    "circleci-mcp-server": {
      "command": "npx",
      "args": ["-y", "@circleci/mcp-server-circleci@latest"],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com"
      }
    }
  }
}
    
```

**Using Docker:**

```

{
  "mcpServers": {
    "circleci-mcp-server": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CIRCLECI_TOKEN",
        "-e", "CIRCLECI_BASE_URL",
        "circleci/mcp-server-circleci"
      ],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com"
      }
    }
  }
}
    
```

Config file location:  
macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`  
Windows: `%APPDATA%\Claude\claude_desktop_config.json`

[Claude Desktop setup docs](https://modelcontextprotocol.io/quickstart/user)

Claude Code

**Using NPX:**

```

claude mcp add circleci-mcp-server -e CIRCLECI_TOKEN=your-circleci-token -- npx -y @circleci/mcp-server-circleci@latest
    
```

**Using Docker:**

```

claude mcp add circleci-mcp-server \
  -e CIRCLECI_TOKEN=your-circleci-token \
  -e CIRCLECI_BASE_URL=https://circleci.com \
  -- docker run --rm -i \
  -e CIRCLECI_TOKEN \
  -e CIRCLECI_BASE_URL \
  circleci/mcp-server-circleci
    
```

[Claude Code setup docs](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp)

Windsurf

**Using NPX:**

```

{
  "mcpServers": {
    "circleci-mcp-server": {
      "command": "npx",
      "args": ["-y", "@circleci/mcp-server-circleci@latest"],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com"
      }
    }
  }
}
    
```

**Using Docker:**

```

{
  "mcpServers": {
    "circleci-mcp-server": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CIRCLECI_TOKEN",
        "-e", "CIRCLECI_BASE_URL",
        "circleci/mcp-server-circleci"
      ],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com"
      }
    }
  }
}
    
```

[Windsurf setup docs](https://docs.windsurf.com/windsurf/mcp)

Amazon Q Developer

**Configuration files:**  
Amazon Q Developer stores MCP client configuration in JSON format in `mcp.json` files.  
  
\- Global configuration: `~/.aws/amazonq/mcp.json` (applies to all workspaces)  
\- Workspace configuration: `.amazonq/mcp.json` (specific to the current project)  
  
Both are optional; if both exist, Amazon Q merges them. If a server is defined in both, the workspace config overrides and a warning is shown.

**Using NPX (local MCP server):**

```
{
  "mcpServers": {
    "circleci-local": {
      "command": "npx",
      "args": ["-y", "@circleci/mcp-server-circleci@latest"],
      "env": {
        "CIRCLECI_TOKEN": "your-circleci-token",
        "CIRCLECI_BASE_URL": "https://circleci.com" // optional, required for on-prem only
      },
      "timeout": 60000
    }
  }
}
```

**Using a Self-Managed Remote MCP Server:**

Create a wrapper script (e.g. `circleci-remote-mcp.sh`):

```
#!/bin/bash
export CIRCLECI_TOKEN="your-circleci-token"
npx mcp-remote http://your-circleci-remote-mcp-server-endpoint:8000/mcp --allow-http
```

Make it executable:

```
chmod +x circleci-remote-mcp.sh
```

Then add it to Amazon Q Developer:

```
q mcp add --name circleci --command "/full/path/to/circleci-remote-mcp.sh"
```

**IDE Integration:**  
You can also add servers through the [Amazon Q MCP configuration UI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-ide.html#mcp-ide-configuration-access-ui):

*   Choose global or workspace scope (`~/.aws/amazonq/mcp.json` vs `.amazonq/mcp.json`)
*   Enter a server name (e.g. `circleci-remote-mcp`)
*   Set transport protocol: `stdio`
*   Set command: the wrapper script path (e.g. `/full/path/to/circleci-remote-mcp.sh`)
*   Save configuration

Install with Smithery

```

npx -y @smithery/cli install @CircleCI-Public/mcp-server-circleci@latest --client claude
    
```
    

## Available tools

From accelerating AI-driven development to orchestrating agentic workflows, each tool exposed by the MCP server equips AI developers with structured CI/CD context for faster, more reliable release cycles.

| Tool | Uses |
| --- | --- |
| `config_helper` | Fix config issues before they break your pipeline |
| `create_prompt_template` | Generate prompts that support consistent AI behavior |
| `find_flaky_tests` | [Identify and troubleshoot unstable tests](https://circleci.com/blog/fix-flaky-tests-with-ai/) |
| `get_build_failure_logs` | [Debug and resolve failed builds faster](https://circleci.com/blog/fix-ci-build-errors-with-ai/) |
| `get_job_test_results` | [Understand and fix test failures and performance issues](https://circleci.com/blog/resolve-ci-test-failures-with-ai/) |
| `get_latest_pipeline_status` | Monitor and act on pipeline health |
| `list_followed_projects` | [Find projects you follow and their `projectSlug`](https://circleci.com/blog/explore-projects-with-ai/) |
| `recommend_prompt_template_tests` | Test and improve prompt reliability |
| `rerun_workflow` | Rerun workflows from the beginning or from a failed job |
| `run_pipeline` | [Trigger builds while staying in your editor](https://circleci.com/blog/trigger-pipelines-with-natural-language/) |
| `run_rollback_pipeline` | Roll back faulty deployments with a single command |

## Learn more

Get started with the CircleCI MCP Server, dive into examples, or keep up with platform updates:

*   [Project repository](https://github.com/CircleCI-Public/mcp-server-circleci) – Source code, issues, and contribution guide.
*   [MCP cookbook](https://github.com/CircleCI-Public/circleci-mcp-cookbook) – Prompt examples and tool usage patterns.
*   [Blog post: Introducing the CircleCI MCP Server](https://circleci.com/blog/circleci-mcp-server/) – Design background and use cases.
*   [CircleCI changelog](https://circleci.com/changelog) – See the latest platform updates and feature releases.