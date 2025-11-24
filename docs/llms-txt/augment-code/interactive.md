# Source: https://docs.augmentcode.com/cli/interactive.md

# Interactive mode

> Use a rich interactive terminal experience to explore your codebase, build new features, debug issues, and integrate your tools.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

<Note>Auggie is currently in beta and does not support all features available in the Augment plugins for Visual Studio Code or JetBrains IDEs.</Note>

## About interactive mode

Auggie is an agentic terminal-based code assistant that has deep codebase knowledge powered by Augment's context engine. Auggie can help you understand a new codebase, fix bugs quickly, and build new features faster. Auggie has access to your connected integrations and MCP servers and can pull in additional context or run tools to get your tasks done.

## Using interactive mode

Run `auggie` without any mode flags to get the full-screen terminal user interface with rich interactive features, real-time streaming of responses, and visual progress indicators. This mode shows all tool calls, results, and allows ongoing conversation through an intuitive interface.

```sh  theme={null}
# Start Auggie in interactive mode
auggie

# Provide an initial instruction
auggie "Look at my open issues and prioritize the highest impact ones for me"
```

### Multi-line input

Entering a new line in the input box depends on your terminal configuration and platform. You can use `Ctrl + J` to enter a new line in any terminal. See below for instructions to configure your terminal to use `Option + Enter` to enter a new line.

| Terminal application       | New line shortcut |
| :------------------------- | :---------------- |
| All terminals              | `Ctrl + J`        |
| MacOS Terminal (see below) | `Option + Enter`  |
| iTerm2 (see below)         | `Option + Enter`  |
| VS Code Terminal           | `Option + Enter`  |
| Ghostty                    | `Shift + Enter`   |

**MacOS Terminal**

1. Go to <Command text="Terminal > Settings... > Profiles > Keyboard" />
2. Check <Command text="Use option key as meta key" />

**iTerm2**

1. Go to <Command text="iTerm2 > Settings... > Profiles > Keys" />
2. Check <Command text="Left or Right option key acts as Esc+" />

## Reference

### Shortcuts

| Command             | Description                                                 |
| :------------------ | :---------------------------------------------------------- |
| `Ctrl + P`          | Enhance your prompt with codebase context                   |
| `Escape`            | Interrupt the active agent                                  |
| `Ctrl + C`          | Interrupt the active agent                                  |
| `Escape` + `Escape` | Clear the input box                                         |
| `Ctrl + C`          | Press twice to exit                                         |
| `Ctrl + D`          | Press twice to exit                                         |
| `Up Arrow`          | Cycle through previous messages                             |
| `Down Arrow`        | Cycle through previous messages                             |
| `Ctrl + O`          | Open current input in external editor, inserts text on exit |

### Slash Commands

| Command            | Description                                                 |
| :----------------- | :---------------------------------------------------------- |
| `/account`         | Show account information                                    |
| `/clear`           | Clear the input box                                         |
| `/editor`          | Open current input in external editor, inserts text on exit |
| `/exit`            | Exit Auggie                                                 |
| `/feedback`        | Provide feedback to the Augment team                        |
| `/github-workflow` | Generate a GitHub Action workflow                           |
| `/help`            | Show help                                                   |
| `/logout`          | Logout of Augment                                           |
| `/mcp-status`      | View the status of all configured MCP servers               |
| `/model`           | Select the model for this session                           |
| `/new`             | Start a new conversation with no message history            |
| `/permissions`     | View and manage tool permissions                            |
| `/request-id`      | Show the request ID for the current conversation            |
| `/task`            | Open task manager to add, edit, and manage tasks            |
| `/verbose`         | Toggle verbose output for tools                             |
| `/vim`             | Toggle Vim mode for advanced text editing                   |

For more information about slash commands, including how to create custom commands, see [Custom Slash Commands](/cli/custom-commands).
