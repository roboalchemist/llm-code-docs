# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/cli-commands.md

# CLI Commands

### Built-In Commands

| Category                      | Feature                       | Command/Key                        | Description                                                       | Purpose                                    |
| ----------------------------- | ----------------------------- | ---------------------------------- | ----------------------------------------------------------------- | ------------------------------------------ |
| Core                          | Context files                 | TABNINE.md                         | Persistent, hierarchical context files for the model.             | Provides always-on project knowledge to AI |
| Core                          | Context referencing           | @\<file/folder>                    | Specify files/folders (e.g., @src/myFile.ts) for session context. | Targets AI focus on relevant code/docs     |
| Core                          | Model selection               | `/model`                           | Configure active AI model.                                        | Switch models for speed vs. depth          |
| Core                          | System prompt override        | .tabnine/agent/system.md           | Replace built-in system instructions.                             | Customizes AI behavior per project .       |
| Shell & Automation            | Shell execution               | `!` or natural language            | Run shell commands (e.g., !npm run start).                        | Stays in AI flow for ops tasks             |
| Shell & Automation            | Headless/non-interactive mode | `--prompt` or `-p` or `pipe input` | Scriptable execution without UI.                                  | CI/CD, automation pipelines.               |
| Shell & Automation            | YOLO mode                     | Ctrl+Y                             | Toggle aggressive auto-execution.                                 | Speeds up trusted workflows (risky).       |
| Configuration & Customization | Commands (slash)              | `/about`                           | Core utilities (version, auth, clear, copy, docs, stats, etc.).   | Daily ops and troubleshooting.             |
| Configuration & Customization | Commands (slash)              | `/auth`                            | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Commands (slash)              | /clear                             | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Commands (slash)              | /copy                              | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Commands (slash)              | /help                              | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Commands (slash)              | /quit                              | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Commands (slash)              | /resume                            | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Commands (slash)              | /stats                             | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Workspace directories         | /directory (add/show)              | Manage project folders.                                           | Defines multi-repo scope.                  |
| Configuration & Customization | Settings                      | /settings                          | Edit CLI behavior/appearance.                                     | Personalizes UX.                           |
| Configuration & Customization | Themes                        | /theme                             | Change visual themes.                                             | Accessibility/preference .                 |
| Configuration & Customization | Editor integration            | /editor                            | Set external editor.                                              | Multiline input in VSCode/etc.             |
| Configuration & Customization | Vim mode                      | /vim                               | Toggle Vim keybindings.                                           | Power-user navigation.                     |
| Configuration & Customization | Commands (slash)              | /bug                               | <p><br></p>                                                       | <p><br></p>                                |
| Configuration & Customization | Terminal keybindings          | /terminal-setup                    | Config for VSCode/Cursor/Windsurf.                                | Smooth multiline terminals.                |

<br>

#### Custom Commands

Tabnine-CLI lets you create global custom commands universal to all your projects OR local custom commands specific to a project.

Global commands are stored in `~/.tabnine/agent/commands/`.

Local (project-specific) commands are stored in that project’s folder at `<your-project-root>/.tabnine/agent/commands/`.

<br>
