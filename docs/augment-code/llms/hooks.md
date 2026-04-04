# Source: https://docs.augmentcode.com/cli/hooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hooks

> Intercept and control tool execution with custom scripts

## Overview

Hooks allow you to intercept tool execution at specific lifecycle events and run custom scripts. This enables powerful workflows like:

* **Security auditing** - Block dangerous commands or log sensitive file access
* **Policy enforcement** - Enforce coding standards or restrict production access
* **Logging** - Track tool usage for compliance and analytics
* **Integration** - Connect with external systems and workflows

Hooks execute automatically when specific events occur during agent operation, giving you fine-grained control over tool execution and session lifecycle.

## Configuration

Hooks are configured in `settings.json` files:

### Settings File Locations

| Location                               | Platform    | Supported By          | Description                                        |
| :------------------------------------- | :---------- | :-------------------- | :------------------------------------------------- |
| `/etc/augment/settings.json`           | Linux/macOS | CLI, VSCode, IntelliJ | System-wide settings for enterprise/admin policies |
| `C:\ProgramData\Augment\settings.json` | Windows     | CLI, VSCode, IntelliJ | System-wide settings for enterprise/admin policies |
| `~/.augment/settings.json`             | All         | CLI, VSCode, IntelliJ | User-level settings                                |

<Note>
  System-level settings (`/etc/augment/settings.json`) take precedence and cannot be overridden by
  user settings.
</Note>

<Warning>
  `PreToolUse`, `PostToolUse`, and `Stop` hooks run **synchronously** - the agent waits for them to
  complete before proceeding. Use appropriate timeouts to prevent long delays. Note that only
  `PreToolUse` can block tool execution; `Stop` can block the agent from finishing (via `decision:
    "block"`), but `PostToolUse` cannot block anything.
</Warning>

### Structure

Hooks are organized by event type with optional matchers:

```json  theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "launch-process",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/validate-command.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

**Configuration fields:**

| Field      | Description                                                                                                                                                                                                                     |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `matcher`  | Pattern to match tool names (case-sensitive). Supports regex patterns. Optional for `PreToolUse` and `PostToolUse` (defaults to `".*"` to match all tools). Not used for session events (`SessionStart`, `SessionEnd`, `Stop`). |
| `hooks`    | Array of hook handlers to execute when the pattern matches.                                                                                                                                                                     |
| `type`     | Hook execution type - currently only `"command"` is supported.                                                                                                                                                                  |
| `command`  | Path to the shell script to execute (must be a `.sh` file).                                                                                                                                                                     |
| `timeout`  | *(Optional)* Timeout in milliseconds (default: 60000ms).                                                                                                                                                                        |
| `metadata` | *(Optional)* Configuration for additional context fields - see [Hook Metadata](#hook-metadata-configuration).                                                                                                                   |

**Matcher pattern examples:**

| Pattern                           | Description                               |
| :-------------------------------- | :---------------------------------------- |
| `"launch-process"`                | Match a specific tool                     |
| `"str-replace-editor\|save-file"` | Match multiple tools using regex OR       |
| `".*"`                            | Match all tools                           |
| `"mcp:*"`                         | Match all MCP tools (special case)        |
| `"mcp:.*_my-server$"`             | Match any tool from a specific MCP server |

For session events (`SessionStart`, `SessionEnd`, `Stop`) that don't require matchers:

```json  theme={null}
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/setup-script.sh"
          }
        ]
      }
    ]
  }
}
```

### Script Requirements

Hook scripts must:

1. **Use `.sh` file extension** - Only shell scripts are supported
2. **Be executable** - Run `chmod +x your-hook.sh`
3. **Have a valid shebang** - First line must specify the interpreter

<Tip>
  You can use any interpreter (Python, Node.js, Ruby, etc.) by specifying it in the shebang line.
  The file extension must still be `.sh`.
</Tip>

```bash  theme={null}
#!/usr/bin/env python3
# Python script with .sh extension - uses Python interpreter via shebang
import sys, json
event_data = json.load(sys.stdin)
# ... your Python code
```

## Hook Events

### PreToolUse

Runs **before** a tool executes. Can block tool execution.

**Common tool names:**

| Tool                 | Description        |
| :------------------- | :----------------- |
| `launch-process`     | Shell commands     |
| `view`               | File reading       |
| `str-replace-editor` | File editing       |
| `save-file`          | File writing       |
| `remove-files`       | File deletion      |
| `web-fetch`          | Fetch web content  |
| `web-search`         | Web search         |
| `codebase-retrieval` | Codebase search    |
| `github-api`         | GitHub integration |
| `linear`             | Linear integration |

Use [PreToolUse output control](#pretooluse-output) to block tools or modify inputs.

### PostToolUse

Runs immediately **after** a tool completes. Can provide feedback to the agent but cannot block execution.

Recognizes the same tool names as PreToolUse. Includes `tool_output` and `tool_error` in the event data.

### Stop

Runs when the agent finishes responding. Can block the agent from stopping (useful for requiring tests before completion).

<Note>Does not run if stopped by user interrupt.</Note>

### SessionStart

Runs when Auggie starts a new session. Useful for:

* Loading development context (git status, open issues)
* Installing dependencies
* Setting up environment variables

### SessionEnd

Runs when an Auggie session ends. Useful for:

* Cleanup tasks
* Logging session statistics
* Saving session state

## Hook Input

Hooks receive event data via **stdin** as a JSON object. The structure varies by event type, but all events share common base fields.

### Common Fields (All Events)

These fields are present in **every** hook event:

| Field             | Type      | Description                                                                                    |
| :---------------- | :-------- | :--------------------------------------------------------------------------------------------- |
| `hook_event_name` | string    | The type of event: `"PreToolUse"`, `"PostToolUse"`, `"Stop"`, `"SessionStart"`, `"SessionEnd"` |
| `conversation_id` | string    | Unique identifier for the current conversation                                                 |
| `workspace_roots` | string\[] | List of workspace root directories (usually contains one path)                                 |

### Event-Specific Fields

#### PreToolUse / PostToolUse Events

Tool events include information about the tool being executed:

| Field          | Type       | Availability     | Description                                                                                                                     |
| :------------- | :--------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `tool_name`    | string     | Always           | Name of the tool (e.g., `"launch-process"`, `"str-replace-editor"`). Use to filter which tools your hook applies to.            |
| `tool_input`   | object     | Always           | Input parameters passed to the tool. **Critical for security hooks** - extract and validate specific parameters.                |
| `tool_output`  | string?    | PostToolUse only | Output returned by the tool (if successful). Use for auditing or providing context to the agent.                                |
| `tool_error`   | string?    | PostToolUse only | Error message if tool execution failed. Use to detect failures and inject troubleshooting tips.                                 |
| `file_changes` | object\[]? | PostToolUse only | File changes for `save-file`, `str-replace-editor`, `remove-files`. Includes `path`, `changeType`, `content`, and `oldContent`. |

**Example: Extracting tool-specific parameters**

<CodeGroup>
  ```bash Bash - Extract Bash command theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')

  if [[ "$TOOL_NAME" == "launch-process" ]]; then
    # Extract the command being executed
    COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command')
    echo "Command: $COMMAND" >&2

    # Check for dangerous patterns
    if echo "$COMMAND" | grep -qE "rm -rf|sudo|curl.*sh"; then
      echo "Blocked dangerous command" >&2
      exit 2
    fi
  fi

  exit 0
  ```

  ```python Python - Extract file path theme={null}
  #!/usr/bin/env python3
  import sys, json

  event_data = json.load(sys.stdin)
  if event_data.get('tool_name') == 'str-replace-editor':
      path = event_data.get('tool_input', {}).get('path', '')
      if any(p in path for p in ['.env', 'secrets', 'credentials']):
          print(f"[AUDIT] Sensitive file: {path}", file=sys.stderr)

  sys.exit(0)
  ```
</CodeGroup>

**Example: Using `tool_output` for context (PostToolUse)**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')
  TOOL_OUTPUT=$(echo "$EVENT_DATA" | jq -r '.tool_output // ""')

  if [[ "$TOOL_NAME" == "launch-process" ]] && echo "$TOOL_OUTPUT" | grep -q "test.*passed"; then
    # Tests passed - inject success context
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": "All tests passed successfully!"
    }
  }
  EOF
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)
  tool_name = event_data.get('tool_name', '')
  tool_output = event_data.get('tool_output', '')

  if tool_name == 'launch-process' and 'test' in tool_output and 'passed' in tool_output:
      # Tests passed - inject success context
      output = {
          "hookSpecificOutput": {
              "hookEventName": "PostToolUse",
              "additionalContext": "All tests passed successfully!"
          }
      }
      print(json.dumps(output))

  sys.exit(0)
  ```
</CodeGroup>

**Example: Using `tool_error` for troubleshooting (PostToolUse)**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  TOOL_ERROR=$(echo "$EVENT_DATA" | jq -r '.tool_error // ""')

  if [[ -n "$TOOL_ERROR" ]] && echo "$TOOL_ERROR" | grep -q "permission denied"; then
    # Inject troubleshooting tip
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": "Permission denied error detected. Try running with appropriate permissions or check file ownership."
    }
  }
  EOF
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)
  tool_error = event_data.get('tool_error', '')

  if tool_error and 'permission denied' in tool_error.lower():
      output = {
          "hookSpecificOutput": {
              "hookEventName": "PostToolUse",
              "additionalContext": "Permission denied error detected. Try with appropriate permissions."
          }
      }
      print(json.dumps(output))

  sys.exit(0)
  ```
</CodeGroup>

**Example: Using `file_changes` for audit logging (PostToolUse)**

The `file_changes` field is populated for file-modifying tools and includes the old content for edits:

```json  theme={null}
{
  "hook_event_name": "PostToolUse",
  "conversation_id": "conv-xyz789",
  "tool_name": "str-replace-editor",
  "tool_input": {
    "path": "src/auth.ts",
    "old_str_1": "...",
    "new_str_1": "..."
  },
  "file_changes": [
    {
      "path": "src/auth.ts",
      "changeType": "edit",
      "content": "// New code content here...",
      "oldContent": "// Old code that was replaced..."
    }
  ]
}
```

```bash  theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
echo "$EVENT_DATA" | jq -c '.file_changes[]?' | while read -r change; do
  echo "[AUDIT] $(echo $change | jq -r '.changeType'): $(echo $change | jq -r '.path')" >&2
done
exit 0
```

#### SessionStart / SessionEnd Events

Session events have no additional fields beyond the common base fields.

**Example SessionStart event:**

```json  theme={null}
{
  "hook_event_name": "SessionStart",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"]
}
```

#### Stop Event

Stop events include information about why the agent stopped:

|        Field       |  Type  |                         Description                         |
| :----------------: | :----: | :---------------------------------------------------------: |
| `agent_stop_cause` | string | Why the agent stopped (e.g., `"end_turn"`, `"interrupted"`) |

**Example Stop event:**

```json  theme={null}
{
  "hook_event_name": "Stop",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "agent_stop_cause": "end_turn"
}
```

### Metadata-Based Fields

When hooks declare metadata options in their configuration, additional fields are included in the event data:

#### `context` field (when `includeUserContext: true`)

Available for: **All event types**

```json  theme={null}
{
  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  }
}
```

**How to use:**

* **`userEmail`**: Identify which user triggered the hook. Use for user-specific policies or analytics.
* **`modelName`**: AI model display name (e.g., "Claude Opus 4.5", "Sonnet-3.7"). Use for model-specific behavior.
* **`toolVersion`**: CLI or VSCode extension version (e.g., "0.6.0"). Use for debugging or version-specific behavior.
* **`timestamp`**: ISO 8601 timestamp. Use for auditing and analytics.

**Example: User-specific permissions**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  USER_EMAIL=$(echo "$EVENT_DATA" | jq -r '.context.userEmail // ""')
  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  # Only allow deployments for specific users
  if [[ "$TOOL_NAME" == "launch-process" ]] && echo "$COMMAND" | grep -q "deploy"; then
    if [[ "$USER_EMAIL" != "admin@example.com" ]]; then
      echo "Only admins can deploy" >&2
      exit 2
    fi
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)
  user_email = event_data.get('context', {}).get('userEmail', '')

  # Only allow deployments for specific users
  tool_name = event_data.get('tool_name', '')
  command = event_data.get('tool_input', {}).get('command', '')

  if tool_name == 'launch-process' and 'deploy' in command:
      if user_email != 'admin@example.com':
          print("Only admins can deploy", file=sys.stderr)
          sys.exit(2)

  sys.exit(0)
  ```
</CodeGroup>

#### `mcp_metadata` field (when `includeMCPMetadata: true`)

Available for: **PreToolUse and PostToolUse only**

```json  theme={null}
{
  "mcp_metadata": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "mcpDecision": "yes",
    "mcpTotalToolsCount": 215,
    "mcpExecutedToolName": "search_my-server",
    "mcpExecutedToolServerName": "my-server",
    "mcpExecutedToolServerToolsCount": 6
  }
}
```

**How to use:**

* **`timestamp`**: ISO 8601 timestamp. Use for auditing and analytics.
* **`mcpDecision`**: Whether this is an MCP tool (`"yes"`) or native tool (`"no"`).
* **`mcpTotalToolsCount`**: Total MCP tools available across all servers.
* **`mcpExecutedToolName`**: Full MCP tool name (e.g., `"search_my-server"`).
* **`mcpExecutedToolServerName`**: MCP server name (e.g., `"my-server"`).
* **`mcpExecutedToolServerToolsCount`**: Tools available from the executed server.

**Example: MCP-specific rate limiting**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  MCP_DECISION=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpDecision // "no"')
  MCP_TOTAL=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpTotalToolsCount // 0')

  # Block if too many MCP tools are enabled (security concern)
  if [[ "$MCP_DECISION" == "yes" ]] && [[ "$MCP_TOTAL" -gt 100 ]]; then
    echo "Too many MCP tools enabled ($MCP_TOTAL). Contact admin." >&2
    exit 2
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  # /etc/augment/hooks/mcp-limit.sh (Python via shebang)
  import sys
  import json

  event_data = json.load(sys.stdin)
  mcp_metadata = event_data.get('mcp_metadata', {})

  mcp_decision = mcp_metadata.get('mcpDecision', 'no')
  mcp_total = mcp_metadata.get('mcpTotalToolsCount', 0)

  # Block if too many MCP tools are enabled (security concern)
  if mcp_decision == 'yes' and mcp_total > 100:
      print(f"Too many MCP tools enabled ({mcp_total}). Contact admin.", file=sys.stderr)
      sys.exit(2)

  sys.exit(0)
  ```
</CodeGroup>

#### `conversation` field (when `includeConversationData: true`)

Available for: **Stop event only**

```json  theme={null}
{
  "conversation": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "userPrompt": "Add error handling to the login function",
    "agentTextResponse": "I'll add comprehensive error handling...",
    "agentCodeResponse": [
      {
        "path": "src/auth/login.ts",
        "changeType": "edit",
        "content": "export function login() { try { ... } catch (e) { ... } }"
      }
    ]
  }
}
```

**How to use:**

* **`timestamp`**: ISO 8601 timestamp. Use for auditing.
* **`userPrompt`**: The user's original request.
* **`agentTextResponse`**: Agent's explanation of what it did.
* **`agentCodeResponse`**: Array of file changes. Each entry has:
  * `path`: File path modified
  * `changeType`: `"edit"`, `"create"`, or `"delete"`
  * `content`: New content (for edit/create only)

**Example: Require tests before finishing**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  # Extract code changes
  CODE_RESPONSE=$(echo "$EVENT_DATA" | jq -r '.conversation.agentCodeResponse // []')

  # Check if any test files were modified
  TEST_FILES=$(echo "$CODE_RESPONSE" | jq -r '.[] | select(.path | test("test|spec")) | .path')

  if [[ -z "$TEST_FILES" ]]; then
    # No test files modified - block stop
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "Stop",
      "decision": "block",
      "reason": "Please add or update tests before finishing"
    }
  }
  EOF
    exit 0
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  conversation = event_data.get('conversation', {})
  code_response = conversation.get('agentCodeResponse', [])

  # Check if any test files were modified
  test_files = [
      change['path'] for change in code_response
      if re.search(r'test|spec', change.get('path', ''))
  ]

  if not test_files:
      # No test files modified - block stop
      output = {
          "hookSpecificOutput": {
              "hookEventName": "Stop",
              "decision": "block",
              "reason": "Please add or update tests before finishing"
          }
      }
      print(json.dumps(output))
      sys.exit(0)

  sys.exit(0)
  ```
</CodeGroup>

### Reading Hook Input

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash

  # Read entire JSON from stdin
  EVENT_DATA=$(cat)

  # Extract fields using jq
  HOOK_EVENT=$(echo "$EVENT_DATA" | jq -r '.hook_event_name')
  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name // ""')
  CONV_ID=$(echo "$EVENT_DATA" | jq -r '.conversation_id')

  echo "Event: $HOOK_EVENT, Tool: $TOOL_NAME, Conversation: $CONV_ID"
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)

  hook_event = event_data['hook_event_name']
  tool_name = event_data.get('tool_name', '')
  conv_id = event_data['conversation_id']

  print(f"Event: {hook_event}, Tool: {tool_name}, Conversation: {conv_id}")
  ```
</CodeGroup>

## Hook Output and Communication

Hooks communicate results through exit codes and output streams. The behavior depends on the exit code and the hook event type.

### Exit Codes

* **Exit code 0**: Success - Hook completed successfully
* **Exit code 2**: Blocking error - Prevents tool execution (PreToolUse only)
* **Other exit codes**: Non-blocking error - Logged but execution continues

### Output Streams

* **stdout**: Standard output from the hook
* **stderr**: Error output from the hook

### Communication Matrix

The following table shows how hook output is handled based on exit code and event type:

| Exit Code | Event Type   | Output Stream | Shown To |                         Behavior                        |
| :-------: | ------------ | :-----------: | -------- | :-----------------------------------------------------: |
|     2     | PreToolUse   |     stderr    | Agent    |   Blocks tool execution, agent sees why it was blocked  |
|     2     | SessionStart |     stderr    | User     | Hook failed at startup, user needs to fix configuration |
|     0     | PreToolUse   |     stderr    | User     |              Warning message shown to user              |
|     0     | PreToolUse   |     stdout    | User     |              Success message shown to user              |
|     0     | PostToolUse  |     stderr    | User     |              Warning message shown to user              |
|     0     | PostToolUse  |     stdout    | User     |              Success message shown to user              |
|     0     | SessionStart |     stdout    | Agent    |             Inject context at session start             |
|     0     | SessionEnd   |     stdout    | User     |                 Show completion message                 |
|   Other   | Any          |     stderr    | User     |            Error logged, execution continues            |

<Info>
  **Key Principle**: Exit code 2 with PreToolUse blocks the tool and shows stderr to the agent (so
  it knows why). Exit code 0 shows output to the user. SessionStart stdout is special - it injects
  context for the agent.
</Info>

### PreToolUse Output

**Blocking a tool (exit code 2):**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  if echo "$COMMAND" | grep -qE "rm -rf|sudo"; then
    echo "Blocked dangerous command: $COMMAND" >&2
    exit 2  # Blocks tool, stderr shown to agent
  fi

  exit 0  # Allow tool to proceed
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  command = event_data.get('tool_input', {}).get('command', '')

  if re.search(r'rm -rf|sudo', command):
      print(f"Blocked dangerous command: {command}", file=sys.stderr)
      sys.exit(2)  # Blocks tool, stderr shown to agent

  sys.exit(0)  # Allow tool to proceed
  ```
</CodeGroup>

**Warning message (exit code 0):**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  FILE_PATH=$(echo "$EVENT_DATA" | jq -r '.tool_input.path // ""')

  if echo "$FILE_PATH" | grep -qE "\.env|secrets"; then
    echo "Warning: Accessing sensitive file: $FILE_PATH" >&2
  fi

  exit 0  # Allow tool but show warning
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  file_path = event_data.get('tool_input', {}).get('path', '')

  if re.search(r'\.env|secrets', file_path):
      print(f"Warning: Accessing sensitive file: {file_path}", file=sys.stderr)

  sys.exit(0)  # Allow tool but show warning
  ```
</CodeGroup>

### SessionStart Output

SessionStart hooks can inject context for the agent by writing to stdout:

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash

  # Load current issues from issue tracker
  ISSUES=$(curl -s https://api.example.com/issues)

  # Output to stdout - this will be injected as context for the agent
  echo "Current open issues:"
  echo "$ISSUES"

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import requests

  # Load current issues from issue tracker
  response = requests.get('https://api.example.com/issues')
  issues = response.text

  # Output to stdout - this will be injected as context for the agent
  print("Current open issues:")
  print(issues)

  sys.exit(0)
  ```
</CodeGroup>

## Hook Output Reference

Hooks can return structured output to control execution and communicate with the agent or user. Output is provided via **stdout** (as JSON) and **stderr** (for error messages).

### Exit Codes

| Exit Code | Meaning            |                                           Behavior                                          |
| :-------: | ------------------ | :-----------------------------------------------------------------------------------------: |
|    `0`    | Success            |    Hook completed successfully. Tool execution continues (unless JSON output blocks it).    |
|    `2`    | Blocking Error     | **PreToolUse only**: Blocks tool execution. Stderr message is shown to both user and agent. |
|   Other   | Non-blocking Error |           Hook failed, but tool execution continues. Stderr shown in verbose mode.          |

### JSON Output Format

Hooks can return JSON on stdout (exit code 0 only) to provide structured control:

```json  theme={null}
{
  "continue": true,
  "stopReason": "Optional reason if continue=false",
  "suppressOutput": false,
  "systemMessage": "Message shown to user",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Security policy violation"
  }
}
```

### Common JSON Fields (All Events)

These fields can be returned by any hook:

|       Field      | Type    |                     Description                     | Destination |
| :--------------: | ------- | :-------------------------------------------------: | :---------: |
|    `continue`    | boolean | If `false`, stops execution (overrides exit code 0) |      -      |
|   `stopReason`   | string  |          Reason shown when `continue=false`         |     User    |
| `suppressOutput` | boolean |      If `true`, hides stdout from verbose mode      |      -      |
|  `systemMessage` | string  |           Warning or informational message          |     User    |

### Event-Specific JSON Output

#### PreToolUse Output

PreToolUse hooks can control tool execution and modify tool input:

|            Field           | Type     |           Description          |   Destination  |
| :------------------------: | -------- | :----------------------------: | :------------: |
|    `permissionDecision`    | `"deny"` |      Block tool execution      |        -       |
| `permissionDecisionReason` | string   |  Reason for blocking the tool  | Agent and User |
|       `updatedInput`       | object   | Modified tool input parameters |        -       |

<Note>
  Currently only `permissionDecision: "deny"` is supported. The `"allow"` and `"ask"` values will be
  implemented in a future release.
</Note>

**Example: Block dangerous command**

```json  theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Command contains 'rm -rf' which is not allowed"
  }
}
```

**Example: Modify tool input**

```json  theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "git status --short"
    }
  }
}
```

#### PostToolUse Output

PostToolUse hooks can provide additional context to the agent:

|        Field        | Type      |                     Description                    | Destination |
| :-----------------: | --------- | :------------------------------------------------: | :---------: |
|      `decision`     | `"block"` |              Blocks agent with reason              |      -      |
|       `reason`      | string    | Reason for blocking (required if decision="block") |    Agent    |
| `additionalContext` | string    |    Additional context for the agent to consider    |    Agent    |

**Example: Provide context to agent**

```json  theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command modified 3 files in the authentication module"
  }
}
```

#### Stop Output

Stop hooks can prevent the agent from finishing:

|    Field   | Type      |                       Description                       | Destination |
| :--------: | --------- | :-----------------------------------------------------: | :---------: |
| `decision` | `"block"` |                      Prevents stop                      |      -      |
|  `reason`  | string    | Reason for blocking stop (required if decision="block") |    Agent    |

**Example: Prevent stop**

```json  theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "decision": "block",
    "reason": "Please run tests before finishing"
  }
}
```

#### SessionStart Output

SessionStart hooks can inject context for the agent:

|        Field        | Type   |             Description            | Destination |
| :-----------------: | ------ | :--------------------------------: | :---------: |
| `additionalContext` | string | Context to inject at session start |    Agent    |

**Example: Inject context**

```json  theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Current sprint: Sprint 23. Focus: Authentication refactor"
  }
}
```

### Output Routing

Different output goes to different destinations:

**To Agent (injected into conversation):**

* Exit code 2 stderr (PreToolUse, PostToolUse, Stop events)
* `permissionDecisionReason` (when decision="deny")
* `reason` (when decision="block")
* `additionalContext`
* SessionStart stdout or `additionalContext`

**To User (displayed in UI):**

* Exit code 2 stderr (SessionStart, SessionEnd events)
* `systemMessage`
* `permissionDecisionReason` (when decision="allow" or "ask")
* Plain stdout (in verbose mode, for non-SessionStart events)

### Complete Output Examples

<CodeGroup>
  ```bash Bash - Block with Exit Code 2 theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  if echo "$COMMAND" | grep -qE "rm -rf"; then
    echo "Blocked dangerous command: $COMMAND" >&2
    exit 2  # Blocks tool, stderr shown to agent and user
  fi

  exit 0
  ```

  ```python Python - Block with Exit Code 2 theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  command = event_data.get('tool_input', {}).get('command', '')

  if re.search(r'rm -rf', command):
      print(f"Blocked dangerous command: {command}", file=sys.stderr)
      sys.exit(2)  # Blocks tool, stderr shown to agent and user

  sys.exit(0)
  ```
</CodeGroup>

<CodeGroup>
  ```bash Bash - Block with JSON theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  if echo "$COMMAND" | grep -qE "rm -rf"; then
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PreToolUse",
      "permissionDecision": "deny",
      "permissionDecisionReason": "Command contains 'rm -rf' which violates security policy"
    }
  }
  EOF
    exit 0
  fi

  exit 0
  ```

  ```python Python - Block with JSON theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  command = event_data.get('tool_input', {}).get('command', '')

  if re.search(r'rm -rf', command):
      output = {
          "hookSpecificOutput": {
              "hookEventName": "PreToolUse",
              "permissionDecision": "deny",
              "permissionDecisionReason": "Command contains 'rm -rf' which violates security policy"
          }
      }
      print(json.dumps(output))
      sys.exit(0)

  sys.exit(0)
  ```
</CodeGroup>

## Hook Metadata (Configuration)

Hook metadata options are **configuration-level flags** that control what data is included in the hook input. They provide a privacy-first, opt-in model for accessing conversation data, MCP metadata, and user context.

### Available Metadata Options

Metadata options are specified in the hook configuration (not in hook output):

```json  theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/analytics.sh"
          }
        ],
        "metadata": {
          "includeConversationData": true,
          "includeMCPMetadata": true,
          "includeUserContext": false
        }
      }
    ]
  }
}
```

**Metadata flags:**

* **`includeUserContext`**: Include user and environment context in hook input
  * Adds `context` field to hook event data
  * Available for: **All event types** (PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd)
  * Fields included:
    * `userEmail` - User's email address (e.g., "[user@example.com](mailto:user@example.com)")
    * `modelName` - Model name being used (e.g., "Claude Opus 4.5")
    * `timestamp` - ISO 8601 timestamp (e.g., "2025-01-15T10:30:00-08:00")
  * Default: `false` (user context excluded)

* **`includeMCPMetadata`**: Include MCP-specific metadata in hook input
  * Adds `mcp_metadata` field to hook event data
  * Available for: **PreToolUse and PostToolUse only**
  * Fields included:
    * `mcpDecision` - Whether MCP tools were used ("yes" | "no")
    * `mcpTotalToolsCount` - Total number of MCP tools available across all servers
    * `mcpExecutedToolName` - Name of the executed MCP tool (if any)
    * `mcpExecutedToolServerName` - Server name of the executed MCP tool (if any)
    * `mcpExecutedToolServerToolsCount` - Number of tools from the executed server (if any)
  * Default: `false` (MCP metadata excluded)

* **`includeConversationData`**: Include conversation fields in hook input
  * Adds `conversation` field to hook event data
  * Available for: **Stop event only**
  * Fields included:
    * `userPrompt` - The user's prompt/message that triggered the agent response
    * `agentTextResponse` - Agent's text response (markdown format)
    * `agentCodeResponse` - Array of file changes made by the agent, each containing:
      * `path` - File path relative to workspace root
      * `changeType` - Type of change ("edit" | "create" | "delete")
      * `content` - File content after the change (undefined for deletions)
  * Default: `false` (conversation data excluded for privacy)

**Metadata availability by event type:**

|      Metadata Option      | PreToolUse | PostToolUse | Stop | SessionStart | SessionEnd |
| :-----------------------: | :--------: | :---------: | :--: | :----------: | :--------: |
|    `includeUserContext`   |      ✓     |      ✓      |   ✓  |       ✓      |      ✓     |
|    `includeMCPMetadata`   |      ✓     |      ✓      |   -  |       -      |      -     |
| `includeConversationData` |      -     |      -      |   ✓  |       -      |      -     |

### When to Use Metadata Options

**Use `includeUserContext` when:**

* Implementing user-specific rate limiting
* Building per-user analytics
* Tracking model usage by user
* Implementing user-based access controls
* Logging user activity for compliance

**Use `includeMCPMetadata` when:**

* Monitoring MCP tool usage patterns
* Debugging MCP integration issues
* Building MCP usage analytics
* Rate limiting MCP tool calls
* Tracking which MCP servers are being used

**Use `includeConversationData` when:**

* Building analytics dashboards that track user interactions
* Implementing compliance logging for audit trails
* Analyzing agent response quality
* Tracking code changes made by the agent
* Capturing complete conversation context for debugging

### Hook Input with Metadata

When metadata options are enabled, the hook receives additional fields in the event data. Here's an example showing all three options enabled:

**Configuration:**

```json  theme={null}
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/analytics.sh"
          }
        ],
        "metadata": {
          "includeUserContext": true,
          "includeConversationData": true
        }
      }
    ]
  }
}
```

**Hook Input (Stop event with all metadata options):**

```json  theme={null}
{
  "hook_event_name": "Stop",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "agent_stop_cause": "end_turn",

  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  },

  "conversation": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "userPrompt": "Add error handling to the login function",
    "agentTextResponse": "I'll add comprehensive error handling...",
    "agentCodeResponse": [{ "path": "src/auth/login.ts", "changeType": "edit" }]
  }
}
```

**Hook Input (PostToolUse event with metadata - MCP tool):**

```json  theme={null}
{
  "hook_event_name": "PostToolUse",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "tool_name": "search_example-server",
  "tool_input": { "query": "latest documentation" },
  "tool_output": "Found 5 results...",
  "is_mcp_tool": true,
  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  },
  "mcp_metadata": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "mcpDecision": "yes",
    "mcpTotalToolsCount": 15,
    "mcpExecutedToolName": "search",
    "mcpExecutedToolServerName": "example-server",
    "mcpExecutedToolServerToolsCount": 5
  }
}
```

**Hook Input (PostToolUse event with file\_changes - file edit):**

```json  theme={null}
{
  "hook_event_name": "PostToolUse",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "tool_name": "str-replace-editor",
  "tool_input": {
    "path": "src/auth.ts",
    "old_str_1": "...",
    "new_str_1": "..."
  },
  "tool_output": "File edited successfully",
  "is_mcp_tool": false,
  "file_changes": [
    {
      "path": "src/auth.ts",
      "changeType": "edit",
      "content": "// New content...",
      "oldContent": "// Old content that was replaced..."
    }
  ],
  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  }
}
```

### Privacy Considerations

Metadata options follow a **privacy-first, opt-in model**:

1. **Default deny**: All sensitive data is excluded by default
2. **Explicit opt-in**: Hooks must explicitly request metadata options
3. **Minimal access**: Request only the options you need
4. **Audit trail**: Metadata usage should be logged for compliance

<Warning>
  When using metadata options that include user data (`includeConversationData`,
  `includeUserContext`), ensure your hook scripts: - Handle sensitive data securely - Comply with
  privacy regulations (GDPR, CCPA, etc.) - Implement appropriate data retention policies - Use
  encryption for data at rest and in transit
</Warning>

### Example: Analytics Hook with Metadata

**Configuration:**

```json  theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/analytics.sh"
          }
        ],
        "metadata": {
          "includeUserContext": true,
          "includeMCPMetadata": true
        }
      }
    ]
  }
}
```

**Hook script (with metadata options):**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  # /etc/augment/hooks/analytics.sh

  EVENT_DATA=$(cat)

  # Extract user context (available because includeUserContext=true)
  USER_EMAIL=$(echo "$EVENT_DATA" | jq -r '.context.userEmail // ""')
  MODEL_NAME=$(echo "$EVENT_DATA" | jq -r '.context.modelName // ""')

  # Extract MCP metadata (available because includeMCPMetadata=true)
  MCP_DECISION=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpDecision // "no"')
  MCP_SERVER=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpExecutedToolServerName // ""')

  # Log analytics
  echo "User: $USER_EMAIL, Model: $MODEL_NAME, MCP: $MCP_DECISION, Server: $MCP_SERVER"
  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  # /etc/augment/hooks/analytics.sh (Python via shebang)

  import sys
  import json

  event_data = json.load(sys.stdin)

  # Extract user context
  context = event_data.get('context', {})
  user_email = context.get('userEmail', '')
  model_name = context.get('modelName', '')

  # Extract MCP metadata
  mcp = event_data.get('mcp_metadata', {})
  mcp_decision = mcp.get('mcpDecision', 'no')
  mcp_server = mcp.get('mcpExecutedToolServerName', '')

  print(f"User: {user_email}, Model: {model_name}, MCP: {mcp_decision}")
  sys.exit(0)
  ```
</CodeGroup>

## Working with MCP Tools

Hooks work seamlessly with [Model Context Protocol (MCP)](/setup-augment/mcp) tools. MCP tools have special naming and metadata that you can use in hooks.

### MCP Tool Naming

MCP tools follow the naming pattern `{toolName}_{serverName}`. For example:

* `search_my-server` - "search" tool from "my-server"
* `query_database-server` - "query" tool from "database-server"
* `read_filesystem-mcp` - "read" tool from "filesystem-mcp"

<Note>
  Both tool names and server names can contain underscores. The server name is always the suffix
  after the **last** underscore that matches the known server name. For reliable matching, use the
  `mcp_server_name` field in your hook script rather than parsing the tool name.
</Note>

### MCP Tool Matchers

Use the `mcp:` prefix to match MCP tools. The pattern after `mcp:` is a regex matched against the full tool name (`toolName_serverName`):

* `"mcp:*"` - Match ALL MCP tools (special case)
* `"mcp:.*_my-server$"` - Match any tool from `my-server` (use `$` anchor)
* `"mcp:^search_my-server$"` - Match exact tool `search` from `my-server`
* `"mcp:^search_.*"` - Match `search` tool from any server

<Info>
  The `mcp:` prefix ensures only MCP tools are matched. The pattern is a standard regex applied to
  the full tool name. Use the `$` anchor when matching server names to avoid partial matches.
</Info>

### MCP Hook Examples

**Log MCP tool usage:**

```bash  theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
SERVER=$(echo "$EVENT_DATA" | jq -r '.mcp_server_name // ""')
echo "[MCP] Server: $SERVER, Tool: $(echo "$EVENT_DATA" | jq -r '.tool_name')" >&2
exit 0
```

**Configuration:**

```json  theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp:*",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/log-mcp-tools.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

**Block specific MCP server:**

```bash  theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
MCP_SERVER=$(echo "$EVENT_DATA" | jq -r '.mcp_server_name // ""')

if [ "$MCP_SERVER" = "blocked-server" ]; then
  echo "This MCP server is blocked by security policy" >&2
  exit 2
fi

exit 0
```

**Configuration:**

```json  theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp:.*_blocked-server$",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/block-mcp-server.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

## Examples

For ready-to-use hook examples, see [Hooks Examples](/cli/hooks-examples).

## Debugging Hooks

### Environment Variables

Hooks have access to these environment variables during execution:

|          Variable         | Description                                                  |          Example          |
| :-----------------------: | ------------------------------------------------------------ | :-----------------------: |
|   `AUGMENT_PROJECT_DIR`   | First workspace root directory (or `process.cwd()` if empty) | `/Users/username/project` |
| `AUGMENT_CONVERSATION_ID` | Current conversation ID                                      |       `conv-xyz789`       |
|    `AUGMENT_HOOK_EVENT`   | Event type                                                   |        `PreToolUse`       |
|    `AUGMENT_TOOL_NAME`    | Tool name (PreToolUse/PostToolUse only)                      |      `launch-process`     |

```bash  theme={null}
#!/usr/bin/env bash
echo "Project: $AUGMENT_PROJECT_DIR, Event: $AUGMENT_HOOK_EVENT" >&2
exit 0
```

### Testing Hooks Locally

**1. Create a test event file:**

```bash  theme={null}
cat > test-event.json << 'EOF'
{
  "hook_event_name": "PreToolUse",
  "conversation_id": "test-conv",
  "workspace_roots": ["/Users/username/project"],
  "tool_name": "launch-process",
  "tool_input": { "command": "git status" }
}
EOF
```

**2. Test your hook script:**

```bash  theme={null}
# Test your hook script (works for both bash and Python via shebang)
cat test-event.json | /etc/augment/hooks/my-hook.sh
echo "Exit code: $?"
```

**3. Validate JSON output:**

```bash  theme={null}
# Test and validate JSON output
OUTPUT=$(cat test-event.json | /etc/augment/hooks/my-hook.sh)
echo "$OUTPUT" | jq .  # Validates JSON syntax
```

### Viewing Hook Execution Logs

Hooks log to the Augment logger. To see hook execution details:

**CLI:**

```bash  theme={null}
# Run with verbose logging
auggie --verbose "your prompt here"

# Or set log level
export AUGMENT_LOG_LEVEL=debug
auggie "your prompt here"
```

**Check logs for:**

* `[HookExecutor]` - Hook execution details
* `[HookManager]` - Hook matching and routing
* `[hook-output-router]` - Output routing decisions

### Common Debugging Techniques

**Log to stderr (won't affect hook output):**

```bash  theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
echo "[DEBUG] $(echo "$EVENT_DATA" | jq -r '.hook_event_name')" >&2
exit 0
```

**Save event data for inspection:**

```bash  theme={null}
#!/usr/bin/env bash
cat > /tmp/hook-debug.json
exit 0
```

#### 3. Validate hook matcher patterns

To test if your matcher pattern works:

```bash  theme={null}
# Test regex pattern in bash
TOOL_NAME="search_my-server"
PATTERN=".*_my-server$"

if [[ "$TOOL_NAME" =~ $PATTERN ]]; then
  echo "Pattern matches!"
else
  echo "Pattern does not match"
fi
```

```python  theme={null}
# Test regex pattern in Python
import re

tool_name = "search_my-server"
pattern = r".*_my-server$"

if re.match(pattern, tool_name):
    print("Pattern matches!")
else:
    print("Pattern does not match")
```

### Performance Tips

1. **Keep hooks fast** - Hooks run synchronously and block tool execution
2. **Cache expensive operations** - Store results in files or environment variables
3. **Use early returns** - Exit as soon as you know the result
4. **Avoid network calls** - Network requests add latency
5. **Minimize JSON parsing** - Parse only the fields you need

**Example: Fast hook with early return**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  # Early return if not a launch-process tool
  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')
  if [[ "$TOOL_NAME" != "launch-process" ]]; then
    exit 0  # Not interested, return immediately
  fi

  # Only parse command if we got here
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command')

  # Check command
  if echo "$COMMAND" | grep -qE "rm -rf"; then
    echo "Blocked dangerous command" >&2
    exit 2
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)

  # Early return if not a launch-process tool
  tool_name = event_data.get('tool_name', '')
  if tool_name != 'launch-process':
      sys.exit(0)  # Not interested, return immediately

  # Only parse command if we got here
  command = event_data.get('tool_input', {}).get('command', '')

  # Check command
  if re.search(r'rm -rf', command):
      print("Blocked dangerous command", file=sys.stderr)
      sys.exit(2)

  sys.exit(0)
  ```
</CodeGroup>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Hook not being triggered">
    **Check:**

    1. **Matcher pattern** - Verify your regex pattern matches the tool name
    2. **Event type** - Ensure you're listening to the correct event (PreToolUse vs PostToolUse)
    3. **Settings file location** - Verify hooks are in the correct settings file (project vs user vs system)
    4. **Hook path** - Ensure the hook script path is correct and the file exists
    5. **File permissions** - Make sure the hook script is executable (`chmod +x hook.sh`)

    **Debug:**

    ```bash  theme={null}
    # Check if hook file exists and is executable
    ls -la /etc/augment/hooks/my-hook.sh

    # Test matcher pattern
    echo "launch-process" | grep -E "launch-process|str-replace-editor"  # Should match
    echo "view" | grep -E "launch-process|str-replace-editor"  # Should not match
    ```
  </Accordion>

  <Accordion title="Hook execution timeout">
    Hooks have a **60-second timeout** by default. If your hook takes longer:

    1. **Optimize the hook** - Make it faster
    2. **Run async operations** - Don't wait for slow operations
    3. **Use background jobs** - Start long-running tasks in the background

    ```bash  theme={null}
    #!/usr/bin/env bash
    EVENT_DATA=$(cat)

    # Start long-running task in background (don't wait)
    (
      # Long-running operation here
      sleep 300
    ) &

    # Return immediately
    exit 0
    ```
  </Accordion>

  <Accordion title="JSON parsing errors">
    **Common issues:**

    * **Invalid JSON syntax** - Use `jq` to validate
    * **Missing quotes** - Ensure all strings are quoted
    * **Trailing commas** - JSON doesn't allow trailing commas
    * **Special characters** - Escape special characters in strings

    **Validate JSON:**

    ```bash  theme={null}
    # Test JSON output
    cat << 'EOF' | jq .
    {
      "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny"
      }
    }
    EOF
    ```
  </Accordion>

  <Accordion title="Hook blocks but shouldn't">
    **Check:**

    * **Exit code** - Make sure you're returning `exit 0` for success
    * **JSON output** - Verify `permissionDecision` is not set to `"deny"`
    * **stderr output** - Ensure you're not writing errors to stderr with exit code 2

    **Debug:**

    ```bash  theme={null}
    #!/usr/bin/env bash
    EVENT_DATA=$(cat)

    # Explicitly allow
    echo "Allowing tool execution" >&2  # Debug message
    exit 0  # Success - don't block
    ```
  </Accordion>

  <Accordion title="Hook errors in logs">
    Check the Auggie logs for hook execution errors:

    ```bash  theme={null}
    # View recent logs
    tail -f ~/.augment/logs/auggie.log | grep -i hook
    ```
  </Accordion>

  <Accordion title="Testing hooks locally">
    Test your hook script manually:

    ```bash  theme={null}
    # Create test event data
    echo '{
      "hook_event_name": "PreToolUse",
      "tool_name": "launch-process",
      "tool_input": {"command": "ls -la"}
    }' | /etc/augment/hooks/your-hook.sh

    # Check exit code
    echo $?
    ```
  </Accordion>
</AccordionGroup>

## Security Considerations

<Warning>
  **USE AT YOUR OWN RISK**: Hooks execute arbitrary shell commands on your system automatically. By using hooks, you acknowledge that:

  * You are solely responsible for the commands you configure
  * Hooks can modify, delete, or access any files your user account can access
  * Malicious or poorly written hooks can cause data loss or system damage
  * You should thoroughly test hooks in a safe environment before production use

  Always review and understand any hook commands before adding them to your configuration.
</Warning>

### Security Best Practices

1. **Validate and sanitize inputs** - Never trust input data blindly
2. **Always quote shell variables** - Use `"$VAR"` not `$VAR`
3. **Block path traversal** - Check for `..` in file paths
4. **Use absolute paths** - Specify full paths for scripts
5. **Skip sensitive files** - Avoid `.env`, `.git/`, keys, etc.
6. **Set appropriate timeouts** - Prevent hooks from hanging indefinitely
7. **Test thoroughly** - Test hooks with various inputs before deploying

## Best Practices

1. **Keep hooks fast**: Hooks should complete quickly (\< 1 second) to avoid slowing down the agent
2. **Use timeouts**: Always set reasonable timeouts to prevent hanging
3. **Handle errors gracefully**: Use exit code 0 for non-critical errors to avoid blocking the agent
4. **Log appropriately**: Use stderr for user-facing messages, log files for detailed audit trails
5. **Test thoroughly**: Test hooks with various tool inputs before deploying
6. **Version control**: Keep hook scripts in version control with your project
7. **Document behavior**: Add comments explaining what each hook does and why

## Limitations

* Hooks currently only support command execution (webhooks planned for future)
* PostToolUse hooks cannot modify tool output (read-only)
* Hooks cannot access the agent's conversation history directly
* Maximum timeout is enforced to prevent indefinite blocking
* Hook execution is sequential, not parallel

## Hook Execution Details

* **Timeout**: 60-second execution limit by default, configurable per command
* **Execution order**: Hooks execute in the order they are defined
* **Environment**: Runs in current directory with Auggie's environment
* **Input**: JSON via stdin
* **Output**:
  * PreToolUse/PostToolUse/Stop: Progress shown in logs
  * SessionStart: stdout added as context for agent
  * SessionEnd: Logged to debug only

## Related Documentation

* [Hooks Examples](/cli/hooks-examples) - Ready-to-use hook examples
* [MCP (Model Context Protocol)](/setup-augment/mcp) - External tool integration
* [Permissions](/cli/permissions) - Tool permission system
* [Rules & Guidelines](/cli/rules) - Custom rules and guidelines
* [Custom Commands](/cli/custom-commands) - Create custom CLI commands
