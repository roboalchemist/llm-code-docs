# Source: https://docs.windsurf.com/windsurf/cascade/hooks.md

# Cascade Hooks (Beta)

Cascade Hooks enable you to execute custom shell commands at key points during Cascade's workflow. This powerful extensibility feature allows you to log operations, enforce guardrails, run validation checks, or integrate with external systems.

<Warning>
  **Beta Release**: Cascade Hooks are currently in beta and undergoing active development. Features and APIs may change. Please contact [Windsurf Support](https://windsurf.com/support) with feedback or bug reports.
</Warning>

<Note>
  Hooks are designed for power users and enterprise teams who need fine-grained control over Cascade's behavior. They require basic shell scripting knowledge.
</Note>

## What You Can Build

Hooks unlock a wide range of automation and governance capabilities:

* **Logging & Analytics**: Track every file read, code change, or command executed by Cascade for compliance and usage analysis
* **Security Controls**: Block Cascade from accessing sensitive files or running dangerous commands
* **Quality Assurance**: Run linters, formatters, or tests automatically after code modifications
* **Custom Workflows**: Integrate with issue trackers, notification systems, or deployment pipelines
* **Team Standardization**: Enforce coding standards and best practices across your organization

## How Hooks Work

Hooks are shell commands that run automatically when specific Cascade actions occur. Each hook:

1. **Receives context** (details about the action being performed) via JSON as standard input
2. **Executes your script** - Python, Bash, Node.js, or any executable
3. **Returns a result** via exit code and output streams

For **pre-hooks** (executed before an action), your script can **block the action** by exiting with exit code `2`. This makes pre-hooks ideal for implementing security policies or validation checks.

## Configuration

Hooks are configured in JSON files that can be placed at three different levels. Cascade loads and merges hooks from all locations, giving teams flexibility in how they distribute and manage hook configurations.

#### System-Level

System-level hooks are ideal for organization-wide policies enforced on shared development machines. For example, you can use them to enforce security policies, compliance requirements, or mandatory code review workflows.

* **macOS**: `/Library/Application Support/Windsurf/hooks.json`
* **Linux/WSL**: `/etc/windsurf/hooks.json`
* **Windows**: `C:\ProgramData\Windsurf\hooks.json`

#### User-Level

User-level hooks are perfect for personal preferences and optional workflows.

* **Location**: `~/.codeium/windsurf/hooks.json`

#### Workspace-Level

Workspace-level hooks allow teams to version control project-specific policies alongside their code. They may include custom validation rules, project-specific integrations, or team-specific workflows.

* **Location**: `.windsurf/hooks.json` in your workspace root

<Note>
  Hooks from all three locations are **merged together**. If the same hook event is configured in multiple locations, all hooks will execute in order: system → user → workspace.
</Note>

### Basic Structure

Here is an example of the basic structure of the hooks configuration:

```json  theme={null}
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "python3 /path/to/your/script.py",
        "show_output": true
      }
    ],
    "post_write_code": [
      {
        "command": "python3 /path/to/another/script.py",
        "show_output": true
      }
    ]
  }
}
```

### Configuration Options

Each hook accepts the following parameters:

| Parameter           | Type    | Description                                                                                             |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `command`           | string  | The shell command to execute. Can be any valid executable with arguments.                               |
| `show_output`       | boolean | Whether to display the hook's stdout/stderr output on the user-facing Cascade UI. Useful for debugging. |
| `working_directory` | string  | Optional. The directory to execute the command from. Defaults to your workspace root.                   |

## Hook Events

Cascade provides eight hook events that cover the most critical actions in the agent workflow.

### Common Input Structure

All hooks receive a JSON object with the following common fields:

| Field               | Type   | Description                                                        |
| ------------------- | ------ | ------------------------------------------------------------------ |
| `agent_action_name` | string | The hook event name (e.g., "pre\_read\_code", "post\_write\_code") |
| `trajectory_id`     | string | Unique identifier for the overall Cascade conversation             |
| `execution_id`      | string | Unique identifier for the single agent turn                        |
| `timestamp`         | string | ISO 8601 timestamp when the hook was triggered                     |
| `tool_info`         | object | Event-specific information (varies by hook type)                   |

In the following examples, the common fields are omitted for brevity. There are eight major types of hook events:

### pre\_read\_code

Triggered **before** Cascade reads a code file. This may block the action if the hook exits with code 2.

**Use cases**: Restrict file access, log read operations, check permissions

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_read_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py"
  }
}
```

This `file_path` may be a directory path when Cascade reads a directory recursively.

### post\_read\_code

Triggered **after** Cascade successfully reads a code file.

**Use cases**: Log successful reads, track file access patterns

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_read_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py"
  }
}
```

This `file_path` may be a directory path when Cascade reads a directory recursively.

### pre\_write\_code

Triggered **before** Cascade writes or modifies a code file. This may block the action if the hook exits with code 2.

**Use cases**: Prevent modifications to protected files, backup files before changes

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_write_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py",
    "edits": [
      {
        "old_string": "def old_function():\n    pass",
        "new_string": "def new_function():\n    return True"
      }
    ]
  }
}
```

### post\_write\_code

Triggered **after** Cascade writes or modifies a code file.

**Use cases**: Run linters, formatters, or tests; log code changes

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_write_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py",
    "edits": [
      {
        "old_string": "import os",
        "new_string": "import os\nimport sys"
      }
    ]
  }
}
```

### pre\_run\_command

Triggered **before** Cascade executes a terminal command. This may block the action if the hook exits with code 2.

**Use cases**: Block dangerous commands, log all command executions, add safety checks

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_run_command",
  "tool_info": {
    "command_line": "npm install package-name",
    "cwd": "/Users/yourname/project"
  }
}
```

### post\_run\_command

Triggered **after** Cascade executes a terminal command.

**Use cases**: Log command results, trigger follow-up actions

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_run_command",
  "tool_info": {
    "command_line": "npm install package-name",
    "cwd": "/Users/yourname/project"
  }
}
```

### pre\_mcp\_tool\_use

Triggered **before** Cascade invokes an MCP (Model Context Protocol) tool. This may block the action if the hook exits with code 2.

**Use cases**: Log MCP usage, restrict which MCP tools can be used

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_mcp_tool_use",
  "tool_info": {
    "mcp_server_name": "github",
    "mcp_tool_arguments": {
      "owner": "code-owner",
      "repo": "my-cool-repo",
      "title": "Bug report",
      "body": "Description of the bug here"
    },
    "mcp_tool_name": "create_issue"
  }
}
```

### post\_mcp\_tool\_use

Triggered **after** Cascade successfully invokes an MCP tool.

**Use cases**: Log MCP operations, track API usage, see MCP results

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_mcp_tool_use",
  "tool_info": {
    "mcp_result": "...",
    "mcp_server_name": "github",
    "mcp_tool_arguments": {
      "owner": "code-owner",
      "perPage": 1,
      "repo": "my-cool-repo",
      "sha": "main"
    },
    "mcp_tool_name": "list_commits"
  }
}
```

## Exit Codes

Your hook scripts communicate results through exit codes:

| Exit Code | Meaning        | Effect                                                                                               |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| `0`       | Success        | Action proceeds normally                                                                             |
| `2`       | Blocking Error | The Cascade agent will see the error message from stderr. For pre-hooks, this **blocks** the action. |
| Any other | Error          | Action proceeds normally                                                                             |

<Warning>
  Only **pre-hooks** (pre\_read\_code, pre\_write\_code, pre\_run\_command, pre\_mcp\_tool\_use) can block actions using exit code 2. Post-hooks cannot block since the action has already occurred.
</Warning>

Keep in mind that the user can see any hook-generated standard output and standard error in the Cascade UI if `show_output` is true.

## Example Use Cases

### Logging All Cascade Actions

Track every action Cascade takes for auditing purposes.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_read_code": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_write_code": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_run_command": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_mcp_tool_use": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`log_input.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()
    
    # Parse the JSON
    try:
        data = json.loads(input_data)
        
        # Write formatted JSON to file
        with open("/Users/yourname/hooks/input.txt", "a") as f:
            f.write('\n' + '='*80 + '\n')
            f.write(json.dumps(data, indent=2, separators=(',', ': ')))
            f.write('\n')
    
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This script appends every hook invocation to a log file, creating an audit trail of all Cascade actions. You may transform the input data or perform custom logic as you see fit.

### Restricting File Access

Prevent Cascade from reading files outside a specific directory.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "python3 /Users/yourname/hooks/block_read_access.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`block_read_access.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

ALLOWED_PREFIX = "/Users/yourname/my-project/"

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()

    # Parse the JSON
    try:
        data = json.loads(input_data)

        if data.get("agent_action_name") == "pre_read_code":
            tool_info = data.get("tool_info", {})
            file_path = tool_info.get("file_path", "")
            
            if not file_path.startswith(ALLOWED_PREFIX):
                print(f"Access denied: Cascade is only allowed to read files under {ALLOWED_PREFIX}", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks the action
            
            print(f"Access granted: {file_path}", file=sys.stdout)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

When Cascade attempts to read a file outside the allowed directory, this hook blocks the operation and displays an error message.

### Blocking Dangerous Commands

Prevent Cascade from executing potentially harmful commands.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "pre_run_command": [
      {
        "command": "python3 /Users/yourname/hooks/block_dangerous_commands.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`block_dangerous_commands.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

DANGEROUS_COMMANDS = ["rm -rf", "sudo rm", "format", "del /f"]

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()

    # Parse the JSON
    try:
        data = json.loads(input_data)

        if data.get("agent_action_name") == "pre_run_command":
            tool_info = data.get("tool_info", {})
            command = tool_info.get("command_line", "")

            for dangerous_cmd in DANGEROUS_COMMANDS:
                if dangerous_cmd in command:
                    print(f"Command blocked: '{dangerous_cmd}' is not allowed for safety reasons.", file=sys.stderr)
                    sys.exit(2)  # Exit code 2 blocks the command
            
            print(f"Command approved: {command}", file=sys.stdout)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This hook scans commands for dangerous patterns and blocks them before execution.

### Running Code Formatters After Edits

Automatically format code files after Cascade modifies them.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_write_code": [
      {
        "command": "bash /Users/yourname/hooks/format_code.sh",
        "show_output": false
      }
    ]
  }
}
```

**Script** (`format_code.sh`):

```bash  theme={null}
#!/bin/bash

# Read JSON from stdin
input=$(cat)

# Extract file path using jq
file_path=$(echo "$input" | jq -r '.tool_info.file_path')

# Format based on file extension
if [[ "$file_path" == *.py ]]; then
    black "$file_path" 2>&1
    echo "Formatted Python file: $file_path"
elif [[ "$file_path" == *.js ]] || [[ "$file_path" == *.ts ]]; then
    prettier --write "$file_path" 2>&1
    echo "Formatted JS/TS file: $file_path"
elif [[ "$file_path" == *.go ]]; then
    gofmt -w "$file_path" 2>&1
    echo "Formatted Go file: $file_path"
fi

exit 0
```

This hook automatically runs the appropriate formatter based on the file type after each edit.

## Best Practices

### Security

<Warning>
  **Use Cascade Hooks at Your Own Risk**: Hooks execute shell commands automatically with your user account's full permissions. You are entirely responsible for the code you configure. Poorly designed or malicious hooks can modify files, delete data, expose credentials, or compromise your system.
</Warning>

* **Validate all inputs**: Never trust the input JSON without validation, especially for file paths and commands.
* **Use absolute paths**: Always use absolute paths in your hook configurations to avoid ambiguity.
* **Protect sensitive data**: Avoid logging sensitive information like API keys or credentials.
* **Review permissions**: Ensure your hook scripts have appropriate file system permissions.
* **Audit before deployment**: Review every hook command and script before adding to your configuration.
* **Test in isolation**: Run hooks in a test environment before enabling them on your primary development machine.

### Performance Considerations

* **Keep hooks fast**: Slow hooks will impact Cascade's responsiveness. Aim for sub-100ms execution times.
* **Use async operations**: For non-blocking hooks, consider logging to a queue or database asynchronously.
* **Filter early**: Check the action type at the start of your script to avoid unnecessary processing.

### Error Handling

* **Always validate JSON**: Use try-catch blocks to handle malformed input gracefully.
* **Log errors properly**: Write errors to `stderr` so they're visible when `show_output` is enabled.
* **Fail safely**: If your hook encounters an error, consider whether it should block the action or allow it to proceed.

### Testing Your Hooks

1. **Start with logging**: Begin by implementing a simple logging hook to understand the data flow.
2. **Use `show_output: true`**: Enable output during development to see what your hooks are doing.
3. **Test blocking behavior**: Verify that exit code 2 properly blocks actions in pre-hooks.
4. **Check all code paths**: Test both success and failure scenarios in your scripts.

## Enterprise Distribution

Enterprise organizations need to enforce security policies, compliance requirements, and development standards that individual users cannot bypass. Cascade Hooks supports this through **system-level configuration**, which takes precedence and cannot be disabled by end users without root permissions.

Deploy your mandatory `hooks.json` configuration to these OS-specific locations:

**macOS:**

```
/Library/Application Support/Windsurf/hooks.json
```

**Linux/WSL:**

```
/etc/windsurf/hooks.json
```

**Windows:**

```
C:\ProgramData\Windsurf\hooks.json
```

Place your hook scripts in a corresponding system directory (e.g., `/usr/local/share/windsurf-hooks/` on Unix systems).

### Deployment Methods

Enterprise IT teams can deploy system-level hooks using standard tools and workflows:

**Mobile Device Management (MDM)**

* **Jamf Pro** (macOS) - Deploy via configuration profiles or scripts
* **Microsoft Intune** (Windows/macOS) - Use PowerShell scripts or policy deployment
* **Workspace ONE**, **Google Endpoint Management**, and other MDM solutions

**Configuration Management**

* **Ansible**, **Puppet**, **Chef**, **SaltStack** - Use your existing infrastructure automation
* **Custom deployment scripts** - Shell scripts, PowerShell, or your preferred tooling

### Verification and Auditing

After deployment, verify that hooks are properly installed and cannot be bypassed:

```bash  theme={null}
# Verify system hooks are present
ls -la /etc/windsurf/hooks.json  # Linux
ls -la "/Library/Application Support/Windsurf/hooks.json"  # macOS

# Test hook execution (should see hook output in Cascade)
# Have a developer trigger the relevant Cascade action

# Verify users cannot modify system hooks
sudo chown root:root /etc/windsurf/hooks.json
sudo chmod 644 /etc/windsurf/hooks.json
```

<Note>
  **Important**: System-level hooks are entirely managed by your IT or security team. Windsurf does not deploy or manage files at system-level paths. Ensure your internal teams handle deployment, updates, and compliance according to your organization's policies.
</Note>

### Workspace Hooks for Team Projects

For project-specific conventions, teams can use workspace-level hooks in version control:

```bash  theme={null}
# Add to your repository
.windsurf/
├── hooks.json
└── scripts/
    └── format-check.py

# Commit to git
git add .windsurf/
git commit -m "Add workspace hooks for code formatting"
```

This allows teams to standardize development practices. Be sure to keep security-critical policies at the system level, and be sure not to check in any sensitive information to version control.

## Additional Resources

* **MCP Integration**: Learn more about [Model Context Protocol in Windsurf](/windsurf/cascade/mcp)
* **Workflows**: Discover how to combine hooks with [Cascade Workflows](/windsurf/cascade/workflows)
* **Analytics**: Track Cascade usage with [Team Analytics](/windsurf/accounts/analytics)
