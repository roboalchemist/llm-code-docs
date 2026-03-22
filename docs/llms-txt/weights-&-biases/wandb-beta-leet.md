# Source: https://docs.wandb.ai/models/ref/cli/wandb-beta/wandb-beta-leet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb beta leet

LEET is a local terminal UI for viewing a W\&B run's stats, metrics, and system health. LEET is a keyboard-driven interface designed for users who work on remote systems or HPC environments using tools like SSH or `tmux`.

<img src="https://mintcdn.com/wb-21fd5541/0773RQ2EQ0O9rvlT/images/leet/leet-tui.png?fit=max&auto=format&n=0773RQ2EQ0O9rvlT&q=85&s=56dfaaaeb3c13bb4b68da59e05c87305" alt="Screenshot demonstrating viewing a run in the LEET terminal UI" width="3450" height="2038" data-path="images/leet/leet-tui.png" />

Key features include:

* **Keyboard-first navigation**: All features accessible via keyboard shortcuts
* **Live updates**: Monitors the `.wandb` file in real-time as your run progresses
* **Metric filtering**: Filter metrics using glob patterns or substring matching
* **Smart zooming**: Mouse wheel zoom keeps the latest data points in view
* **Customizable grids**: Configure the number of rows and columns for metric and system displays
* **Human-readable formatting**: System metrics show friendly units (e.g., "GPU Utilization (%)", "RAM Used (GB)")

LEET provides a three-panel layout:

* **Left sidebar**: Run Overview showing environment variables, configuration, and summary statistics
* **Center panel**: Metrics grid with Braille-style line charts for logged metrics
* **Right sidebar**: System Metrics displaying GPU utilization, RAM, CPU, and other system health indicators

## Keyboard Shortcuts

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

## Usage

```bash  theme={null}
wandb beta leet COMMAND [ARGS]...
```

## Commands

| Command                                                                     | Description              |
| :-------------------------------------------------------------------------- | :----------------------- |
| [config](/models/ref/cli/wandb-beta/wandb-beta-leet/wandb-beta-leet-config) | Edit LEET configuration. |
| [run](/models/ref/cli/wandb-beta/wandb-beta-leet/wandb-beta-leet-run)       | Launch the LEET TUI.     |
