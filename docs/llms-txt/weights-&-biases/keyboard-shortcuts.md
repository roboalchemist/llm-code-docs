# Source: https://docs.wandb.ai/models/app/keyboard-shortcuts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Learn about the keyboard shortcuts available in W&B.

# Keyboard shortcuts

W\&B supports keyboard shortcuts to help you navigate and interact with experiments, workspaces, and data more efficiently. This reference guide covers keyboard shortcuts for the W\&B App and the W\&B LEET (Lightweight Experiment Exploration Tool) terminal UI.

<Tabs>
  <Tab title="App">
    These keyboard shortcuts work in the W\&B App.

    ## Workspace management

    | Shortcut                                             | Description                                                                              |
    | ---------------------------------------------------- | ---------------------------------------------------------------------------------------- |
    | **Cmd+Z** (macOS) / **Ctrl+Z** (Windows/Linux)       | Undo a change you've made in the UI, such as a modification to the workspace or a panel. |
    | **Cmd+Shift+Z** (macOS) / **Ctrl+Y** (Windows/Linux) | Redo a change you previously undid in the workspace.                                     |

    ## Navigation

    | Shortcut                                       | Description                                                                                                                                                 |
    | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Tab**                                        | Navigate between interactive elements.                                                                                                                      |
    | **Cmd+J** (macOS) / **Ctrl+J** (Windows/Linux) | Switch between the Workspaces and Runs tabs in the project sidebar.                                                                                         |
    | **Cmd+.** (macOS) / **Ctrl+.** (Windows/Linux) | Minimize or restore the Runs selector sidebar to reclaim screen space.                                                                                      |
    | **Cmd+K** (macOS) / **Ctrl+K** (Windows/Linux) | Open the quick search dialog to search across projects, runs, and other resources.                                                                          |
    | **Esc**                                        | Throughout the W\&B App, exit full-screen panel views, close settings drawers, dismiss the quick search dialog, close an editor, or dismiss other overlays. |

    ## Panel navigation

    | Shortcut                                                                                                 | Description                                                          |
    | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
    | **Left Arrow / Right Arrow**                                                                             | Step through panels in a section when in full screen mode.           |
    | **Esc**                                                                                                  | Exit full-screen panel view and return to the workspace.             |
    | **Cmd+Left Arrow / Cmd+Right Arrow** (macOS)<br />**Ctrl+Left Arrow / Ctrl+Right Arrow** (Windows/Linux) | When viewing a media panel in full screen mode,move the step slider. |

    ## Reports

    | Shortcut               | Description                                               |
    | ---------------------- | --------------------------------------------------------- |
    | **Delete / Backspace** | Remove the selected panel grid from the report.           |
    | **Enter**              | Insert a Markdown block after typing "/mark" in a report. |
    | **Esc**                | Exit the report editor.                                   |
    | **Tab**                | Navigate between interactive elements in a report.        |

    ## Notes

    * Most keyboard shortcuts use **Cmd** on macOS and **Ctrl** on Windows/Linux.
    * The W\&B App implements custom handling for some browser default shortcuts.
    * Some shortcuts are context-sensitive and only work in specific areas of the application.
  </Tab>

  <Tab title="LEET">
    These keyboard shortcuts work in the W\&B LEET (Lightweight Experiment Exploration Tool) terminal UI. To launch LEET, run `wandb beta leet` in your terminal. For more information, see [`wandb beta leet`](/models/ref/cli/wandb-beta/wandb-beta-leet/).

    ### General

    | **Key**       | **Description**         |
    | :------------ | :---------------------- |
    | `h`, `?`      | Toggle this help screen |
    | `q`, `ctrl+c` | Quit                    |
    | `alt+r`       | Reload run data         |

    ### Panels

    | **Key** | **Description**                          |
    | :------ | :--------------------------------------- |
    | `[`     | Toggle left sidebar with run overview    |
    | `]`     | Toggle right sidebar with system metrics |
    | `l`     | Toggle run console logs pane             |
    | `s`     | Toggle system metrics pane               |

    ### Navigation

    | **Key**               | **Description**                       |
    | :-------------------- | :------------------------------------ |
    | `N`, `pgup`           | Navigate between chart pages          |
    | `n`, `pgdown`         | Navigate between chart pages          |
    | `alt+N`, `alt+pgup`   | Navigate between system metrics pages |
    | `alt+n`, `alt+pgdown` | Navigate between system metrics pages |

    ### Charts

    | **Key**  | **Description**                                                 |
    | :------- | :-------------------------------------------------------------- |
    | `/`      | Filter metrics by pattern (supports glob or substring matching) |
    | `ctrl+l` | Clear active filter                                             |
    | `\`      | Toggle system metrics filtering                                 |

    ### Run Overview

    | **Key**  | **Description**                                                                           |
    | :------- | :---------------------------------------------------------------------------------------- |
    | `o`      | Filter overview items (supports `@e`, `@c`, `@s` for environment/config/summary sections) |
    | `ctrl+k` | Clear overview filter                                                                     |

    ### Configuration

    | **Key** | **Description**                   |
    | :------ | :-------------------------------- |
    | `c`     | Set metrics grid columns          |
    | `r`     | Set metrics grid rows             |
    | `C`     | Set system grid columns (Shift+c) |
    | `R`     | Set system grid rows (Shift+r)    |

    ### Run Overview Navigation (when sidebar open)

    | **Key**            | **Description**                                      |
    | :----------------- | :--------------------------------------------------- |
    | `up`, `down`       | Navigate items in section                            |
    | `tab`, `shift+tab` | Switch between sections                              |
    | `left`, `right`    | Navigate pages in section                            |
    | `@e`, `@c`, `@s`   | Filter specific section (environment/config/summary) |

    ### Mouse

    | **Action**           | **Description**              |
    | :------------------- | :--------------------------- |
    | `mouse wheel`        | Zoom in/out on focused chart |
    | `shift+mouse select` | Select text                  |
  </Tab>
</Tabs>
