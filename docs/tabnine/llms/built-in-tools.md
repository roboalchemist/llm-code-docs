# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/built-in-tools.md

# Built-In Tools

Tabnine CLI provides powerful built-in tools that the AI uses automatically to fulfill your requests.

### How Tools work

You don't need to call tools directly. The AI automatically uses them when needed.

Example:

```
> What files are in the src directory?
```

The AI automatically uses the `list_directory` tool.

### Available tools

#### File operations

* **list\_directory** - List directory contents\
  Lists files and subdirectories in a specified directory. Can filter using glob patterns and respects `.gitignore`.

Example usage:

```
> What files are in the src directory?
> Show me all TypeScript files in @src/
```

* **read\_file** - Read file contents\
  Reads text files, images (PNG, JPG, SVG, etc.), audio files, and PDFs. Supports reading specific line ranges for large text files.

Example usage:

```
> Read @package.json and show the dependencies
> Show me lines 10-50 of @src/index.ts
```

* **write\_file** - Create or overwrite files\
  Creates new files or overwrites existing ones. Creates parent directories if needed.

Example usage:

```
> Create a README.md file for this project
> Write a .gitignore file with Node.js defaults
```

* **replace** - Edit existing files\
  Makes precise text replacements in files. Requires significant context to ensure correct edits. Includes multi-stage correction for reliability.

Example usage:

```
> In src/config.ts, change the API timeout from 5000 to 10000
> Update the error message in @utils/validator.ts
```

* **glob** - Find files by pattern\
  Finds files matching glob patterns (e.g., `*.ts`, `src/**/*.js`). Returns paths sorted by modification time (newest first).

Example usage:

```
> Find all test files
> Show me all JSON files in the project
```

* **search\_file\_content** - Search file contents\
  Searches for text patterns (regex) across files. Fast search powered by ripgrep. Can filter by glob patterns.

Example usage:

```
> Find all TODO comments in @src/
> Search for "import React" in TypeScript files
```

* **save\_memory** - Save information across sessions\
  Saves facts and preferences that persist across CLI sessions.

Example usage:

```
> Remember that I prefer TypeScript for new projects
> Remember our team uses Jest for testing
```

* **write\_todos** - Task management\
  Manages subtasks for complex requests. Helps track progress and organize multi-step operations.

Example usage:

```
> (Used automatically by AI for complex tasks)
```

#### Shell & web operations

* **run\_shell\_command** - Execute shell commands\
  Runs shell commands in your terminal. Always asks for confirmation before executing.

Example usage:

```
> Run the tests with npm test
> What's the git status?
> Install the lodash package
```

#### Built-In MCP tools

The following tools are powered by Tabnine's infrastructure.

* **Remote Code Search** - Search across massive codebases using Tabnine's cloud indexing.

Example usage:

```
> Find all functions that handle authentication
```

* **Coaching Guidelines** - AI-powered best practices tailored to your code.

Example usage:

```
> What are the best practices for error handling?
```

Learn more: [Coaching Guidelines](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/coaching-guidelines-v)

### Tool summary

Here's a complete list of all built-in tools:

| Tool Name             | Display Name | Description                |
| --------------------- | ------------ | -------------------------- |
| `list_directory`      | ReadFolder   | List directory contents    |
| `read_file`           | ReadFile     | Read file contents         |
| `write_file`          | WriteFile    | Create or overwrite files  |
| `replace`             | Edit         | Edit existing files        |
| `glob`                | FindFiles    | Find files by pattern      |
| `search_file_content` | SearchText   | Search file contents       |
| `run_shell_command`   | Shell        | Execute shell commands     |
| `save_memory`         | Memory       | Save facts across sessions |
| `write_todos`         | Todos        | Manage task lists          |

### Tool Configuration

#### View available tools

To see which tools are currently available and enabled:

```bash
tabnine
> /tools
```

This displays a list of all tools with their status (enabled/disabled).

#### Enable/disable tools

You can configure which tools are available, either open the `/settings` menu or edit your `settings.json` file and adding the following settings:

| UI Label (/settings)             | Setting                              | Description                                                                                                                                                                | Default   |
| -------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Enable Interactive Shell         | `tools.shell.enableInteractiveShell` | Use node-pty for an interactive shell experience. Fallback to child\_process still applies.                                                                                | `true`    |
| Show Color                       | `tools.shell.showColor`              | Show color in shell output.                                                                                                                                                | `false`   |
| Auto Accept                      | `tools.autoAccept`                   | Automatically accept and execute tool calls that are considered safe (e.g., read-only operations).                                                                         | `false`   |
| Use Ripgrep                      | `tools.useRipgrep`                   | Use ripgrep for file content search instead of the fallback implementation. Provides faster search performance.                                                            | `true`    |
| Enable Tool Output Truncation    | `tools.enableToolOutputTruncation`   | Enable truncation of large tool outputs.                                                                                                                                   | `true`    |
| Tool Output Truncation Threshold | `tools.truncateToolOutputThreshold`  | Truncate tool output if it is larger than this many characters. Set to -1 to disable.                                                                                      | `4000000` |
| Tool Output Truncation Lines     | `tools.truncateToolOutputLines`      | The number of lines to keep when truncating tool output.                                                                                                                   | `1000`    |
| Disable LLM Correction           | `tools.disableLLMCorrection`         | Disable LLM-based error correction for edit tools. When enabled, tools will fail immediately if exact string matches are not found, instead of attempting to self-correct. | `false`   |

#### Tool Confirmation

Tools that modify files or execute commands require confirmation:

* Auto-approved: Read operations (list, read, search)
* Requires confirmation: Write operations, edits, shell commands

When a tool requires confirmation, you'll see a diff or preview of the changes before they're applied.

{% hint style="info" %}
Tools that modify files or run shell commands always ask for confirmation before performing the action. Read-only tools do not require confirmation.
{% endhint %}
