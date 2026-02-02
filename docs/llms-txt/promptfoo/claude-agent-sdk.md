# Claude Agent SDK

This provider makes [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) available for evals through its [TypeScript SDK](https://docs.claude.com/en/api/agent-sdk/typescript).

The Claude Agent SDK was formerly known as the Claude Code SDK. It's still built on top of Claude Code and exposes all its functionality.

## Provider IDs

You can reference this provider using either:

- `anthropic:claude-agent-sdk` (full name)
- `anthropic:claude-code` (alias)

## Installation

The Claude Agent SDK provider requires the `@anthropic-ai/claude-agent-sdk` package to be installed separately:

```bash
npm install @anthropic-ai/claude-agent-sdk
```

This is an optional dependency and only needs to be installed if you want to use the Claude Agent SDK provider. Note that Anthropic has released the claude-agent-sdk library with a [proprietary license](https://github.com/anthropics/claude-agent-sdk-typescript/blob/9f51899c3e04f15951949ceac81849265d545579/LICENSE.md).

## Setup

The easiest way to get started is with an Anthropic API key. You can set it with the `ANTHROPIC_API_KEY` environment variable or specify the `apiKey` in the provider configuration.

Create Anthropic API keys [here](https://console.anthropic.com/settings/keys).

Example of setting the environment variable:

```sh
export ANTHROPIC_API_KEY=your_api_key_here
```

## Other Model Providers

Apart from using the Anthropic API, you can also use AWS Bedrock and Google Vertex AI.

### AWS Bedrock

- Set the `CLAUDE_CODE_USE_BEDROCK` environment variable to `true`:

```sh
export CLAUDE_CODE_USE_BEDROCK=true
```

- Follow the [Claude Code Bedrock documentation](https://docs.claude.com/en/docs/claude-code/amazon-bedrock) to make credentials available to Claude Agent SDK.

### Google Vertex

- Set the `CLAUDE_CODE_USE_VERTEX` environment variable to `true`:

```sh
export CLAUDE_CODE_USE_VERTEX=true
```

- Follow the [Claude Code Vertex documentation](https://docs.claude.com/en/docs/claude-code/google-vertex-ai) to make credentials available to Claude Agent SDK.

## Quick Start

### Basic Usage

By default, Claude Agent SDK runs in a temporary directory with no tools enabled, using the `default` permission mode. This makes it behave similarly to the standard [Anthropic provider](https://www.promptfoo.dev/docs/providers/anthropic/). It has no access to the file system (read or write) and can't run system commands.

```yaml
promptfooconfig.yaml
```

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      working_dir: ./src
```

When your test cases finish, the temporary directory is deleted.

### With Working Directory

You can specify a specific working directory for Claude Agent SDK to run in:

```yaml
promptfooconfig.yaml
```

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      working_dir: ./my-project
      append_allowed_tools: ["Write", "Edit", "MultiEdit"]
```

This allows you to prepare a directory with files or sub-directories before running your tests.

By default, when you specify a working directory, Claude Agent SDK is given read-only access to the directory.

### With Side Effects

You can also allow Claude Agent SDK to write to files, run system commands, call MCP servers, and more.

Here's an example that will allow Claude Agent SDK to both read from and write to files in the working directory. It uses `append_allowed_tools` to add tools for writing and editing files to the default set of read-only tools. It also sets `permission_mode` to `acceptEdits` so Claude Agent SDK can modify files without asking for confirmation.

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      working_dir: ./my-project
      append_allowed_tools: ["Write", "Edit"]
      permission_mode: acceptEdits
      allow_dangerously_skip_permissions: true
```

The `allow_dangerously_skip_permissions` parameter is required when using `bypassPermissions` mode.

### Tool Configuration

Customize available tools for your use case:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      tools: ["Read", "Edit", "Write", "MultiEdit"]
```

The `append_allowed_tools` option specifies the base set of available built-in tools, while `allowedTools` and `disallowedTools` filter from that base.

⚠️ **Security Note**: Some tools allow Claude Agent SDK to modify files, run system commands, search the web, and more. Think carefully about security implications before using these tools.

[Here's a full list of available tools.](https://docs.claude.com/en/docs/claude-code/settings#tools-available-to-claude)

## MCP Integration

Unlike the standard Anthropic provider, Claude Agent SDK handles MCP (Model Context Protocol) connections directly. Configuration is forwarded to the Claude Agent SDK:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      mcp:
        servers:
          - url: https://api.example.com/mcp
            name: api-server
            headers: 
              Authorization: Bearer token
          - command: node
            args: ["mcp-server.js"]
            name: local-server
```

For detailed MCP configuration, see [Claude Code MCP documentation](https://docs.claude.com/en/docs/claude-code/mcp).

## Setting Sources

By default, the Claude Agent SDK provider does not look for settings files, CLAUDE.md, or slash commands. You can enable this by specifying `setting_sources`:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      setting_sources: ["project", "local"]
```

Available values:

- `user` - User-level settings
- `project` - Project-level settings
- `local` - Local directory settings

## Budget Control

Limit the maximum cost of an agent execution with `max_budget_usd`:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      max_budget_usd: 0.50
```

The agent will stop execution if the cost exceeds the specified budget.

## Additional Directories

Grant the agent access to directories beyond the working directory:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      working_dir: ./project
      additional_directories:
        - /shared/libs
        - /data/models
```

## Structured Output

Get validated JSON responses by specifying an output schema:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      output_format:
        type: json_schema
        schema:
          type: object
          properties:
            analysis:
              type: string
            confidence:
              type: number
          required: [analysis, confidence]
```

When `output_format` is configured, the response will include structured output that conforms to the schema. The structured output is available in:

- `output` - The parsed structured output (when available)
- `metadata.structuredOutput` - The raw structured output value

## Session Management

Continue or fork existing sessions for multi-turn interactions:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      resume: session-id-from-previous-run
      continue: true
      resume: session-id-to-fork
      fork_session: true
```

Session IDs are returned in the response and can be used to continue conversations across eval runs.

### Disabling Session Persistence

By default, sessions are saved to disk (`~/.claude/projects/`) and can be resumed later. For ephemeral or automated workflows where session history is not needed, disable persistence:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      persist_session: false
```

## File Checkpointing

Track file changes during the session to enable rewinding to previous states:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      enable_file_checkpointing: true
      working_dir: ./my-project
      append_allowed_tools: ["Write", "Edit"]
```

When file checkpointing is enabled, the SDK creates backups of files before they are modified. This allows programmatic restoration to any previous state in the conversation.

## Beta Features

Enable experimental features using the `betas` parameter:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      betas:
        - context-1m-2025-08-07
```

Currently available betas:

| Beta | Description |
| --- | --- |
| `context-1m-2025-08-07` | Enable 1M token context window (Sonnet 4/4.5 only) |

See the [Anthropic beta headers documentation](https://docs.anthropic.com/en/api/beta-headers) for more information.

## Sandbox Configuration

Run commands in an isolated sandbox environment for additional security:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      sandbox:
        enabled: true
        autoAllowBashIfSandboxed: true
        network:
          allowLocalBinding: true
          allowedDomains: ["api.example.com"]
```

Available sandbox options:

| Option | Type | Description |
| --- | --- | --- |
| `enabled` | boolean | Enable sandboxed execution |
| `autoAllowBashIfSandboxed` | boolean | Auto-allow bash commands when sandboxed |
| `allowUnsandboxedCommands` | boolean | Allow commands that can't be sandboxed |
| `network.allowedDomains` | string[] | Domains allowed for network access |
| `network.allowLocalBinding` | boolean | Allow binding to localhost |
| `network.allowUnixSockets` | string[] | Unix sockets to allow |

See the [Claude Code sandbox documentation](https://docs.anthropic.com/en/docs/claude-code/settings#sandbox-settings) for more details.

## Advanced Runtime Configuration

### JavaScript Runtime

Specify which JavaScript runtime to use:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      executable: bun  # or 'node' or 'deno'
      executable_args:
        - --smol
```

### Extra CLI Arguments

Pass additional arguments to Claude Code:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      extra_args:
        verbose: null  # boolean flag (adds --verbose)
        timeout: '30'  # adds --timeout 30
```

### Custom Executable Path

Use a specific Claude Code installation:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      path_to_claude_code_executable: /custom/path/to/claude-code
```

### Custom Spawn Function (Programmatic Only)

For running Claude Code in VMs, containers, or remote environments, you can provide a custom spawn function when using the provider programmatically:

```typescript
import { ClaudeCodeSDKProvider } from 'promptfoo';

const provider = new ClaudeCodeSDKProvider({
  config: {
    spawn_claude_code_process: (options) => {
      // Custom spawn logic for VM/container execution
      // options contains: command, args, cwd, env, signal
      return myVMProcess; // Must satisfy SpawnedProcess interface
    },
  },
});
```

This option is only available when using the provider programmatically, not via YAML configuration.

## Programmatic Agents

Define custom subagents with specific tools and permissions:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      agents:
        code-reviewer:
          name: Code Reviewer
          description: Reviews code for bugs and style issues
          tools: ["Read", "Grep", "Glob"]
        test-runner:
          name: Test Runner
          description: Runs tests and reports results
          tools: ["Bash", "Read"]
```

## Handling AskUserQuestion Tool

The `AskUserQuestion` tool allows Claude to ask the user multiple-choice questions during execution. In automated evaluations, there's no human to answer these questions, so you need to configure how they should be handled.

### Using the Convenience Option

The simplest approach is to use the `ask_user_question` configuration:

```yaml
providers:
  - anthropic:claude-agent-sdk
    config:
      append_allowed_tools: ["AskUserQuestion"]
      ask_user_question:
        behavior: first_option
```

Available behaviors:

| Behavior | Description |
| --- | --- |
| `first_option` | Always select the first option |
| `random` | Randomly select from available options |
| `deny` | Deny the tool use |

### Programmatic Usage

For custom answer selection logic when using the provider programmatically, you can provide your own `canUseTool` callback:

```typescript
import { ClaudeCodeSDKProvider } from 'promptfoo';

const provider = new ClaudeCodeSDKProvider({
  config: {
    append_allowed_tools: ["AskUserQuestion"],
  },
  // Custom canUseTool passed via SDK options
});
```

The `canUseTool` callback receives the tool name and input, and returns an answer:

```typescript
async function canUseTool(toolName, input, options) {
  if (toolName !== 'AskUserQuestion') {
    return { behavior: 'allow', updatedInput: input };
  }

  const answers = {};
  for (const q of input.questions) {
    // Custom selection logic - prefer options marked as recommended
    const preferred = q.options.find((o) => o.description.toLowerCase().includes('recommended'));
    answers[q.question] = preferred?._0['label'] ?? q.options[0].label;
  }

  return { behavior: 'allow', updatedInput: { questions: input.questions, answers, } };
}
```

See the [Claude Agent SDK permissions documentation](https://platform.claude.com/docs/en/agent-sdk/permissions) for more details on `canUseTool`.

If you're testing scenarios where the agent asks questions, consider what answer would lead to the most interesting test case. Using `random` behavior can help discover edge cases.

## Caching Behavior

This provider automatically caches responses, and will read from the cache if the prompt, configuration, and files in the working directory (if `working_dir` is set) are the same as a previous run.

To disable caching globally:

```sh
export PROMPTFOO_CACHE_ENABLED=false
```

You can also include `bustCache: true` in the configuration to prevent reading from the cache.

## Managing Side Effects

When using Claude Agent SDK with configurations that allow side effects, like writing to files, running system commands, or calling MCP servers, you'll need to consider:

- How to reset after each test run
- How to ensure tests don't interfere with each other (like writing to the same files concurrently)

This increases complexity, so first consider if you can achieve your goal with a read-only configuration. If you do need to test with side effects, here are some strategies that can help:

- **Serial execution**: Set `evaluateOptions.maxConcurrency: 1` in your config or use `--max-concurrency 1` CLI flag
- **Hooks**: Use promptfoo [extension hooks](https://www.promptfoo.dev/docs/configuration/reference/#extension-hooks) to reset the environment after each test run
- **Wrapper scripts**: Handle setup/cleanup outside of promptfoo
- **Use git**: If you're using a custom working directory, you can use git to reset the files after each test run
- **Use a container**: Run tests that might run commands in a container to protect the host system

## Examples

Here are a few complete example implementations:

- [Basic usage](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#basic-usage) - Basic usage with no tools
- [Working directory](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#working-directory) - Read-only access to a working directory
- [Advanced editing](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#advanced-editing) - File edits and working directory reset in an extension hook
- [MCP integration](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#mcp-integration) - Read-only MCP server integration with weather API
- [Structured output](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#structured-output) - JSON schema validation for agent responses
- [Advanced options](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#advanced-options) - Sandbox, runtime configuration, and CLI arguments
- [AskUserQuestion handling](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk#askuserquestion-handling) - Automated handling of user questions in evaluations

## See Also

- [Claude Agent SDK documentation](https://docs.claude.com/en/api/agent-sdk)
- [Standard Anthropic provider](https://www.promptfoo.dev/docs/providers/anthropic/) - For text-only interactions