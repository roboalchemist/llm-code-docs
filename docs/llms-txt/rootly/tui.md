# Source: https://docs.rootly.com/integrations/tui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Terminal UI (TUI)

> View and manage Rootly incidents and alerts from your terminal with the Rootly TUI application.

<Warning>
  Early Preview

  The Rootly TUI is currently in **early preview**. Features may change and some functionality may be limited. We welcome feedback and bug reports on [GitHub](https://github.com/rootlyhq/rootly-tui/issues).
</Warning>

The Rootly TUI is a terminal-based user interface for viewing Rootly incidents and alerts directly from your command line. Built for engineers who prefer working in the terminal, it provides a fast, keyboard-driven experience for monitoring and triaging incidents.

## Features

* **Incidents View**: Browse and view incident details including severity, status, timeline, roles, and more
* **Alerts View**: Monitor alerts with source information, labels, and status
* **Keyboard Navigation**: Vim-style navigation (j/k) and intuitive keyboard shortcuts
* **Detail Views**: Press Enter to load extended details for any incident or alert
* **Multi-language Support**: Available in 12 languages
* **Debug Logging**: Built-in log viewer for troubleshooting

## Installation

### Using Homebrew (macOS/Linux)

```bash  theme={null}
brew install rootlyhq/tap/rootly-tui
```

### Using Go

```bash  theme={null}
go install github.com/rootlyhq/rootly-tui@latest
```

### Download Binary

Download the latest release from [GitHub Releases](https://github.com/rootlyhq/rootly-tui/releases).

## Quick Start

1. **Launch the application**:
   ```bash  theme={null}
   rootly-tui
   ```

2. **Configure your API key**: On first launch, you'll be prompted to enter your Rootly API credentials:
   * **API Endpoint**: Usually `api.rootly.com` (or your custom endpoint)
   * **API Key**: Your Rootly API key (generate one from Settings > API Keys in Rootly)
   * **Timezone**: Select your preferred timezone for displaying timestamps
   * **Language**: Choose your preferred language

3. **Navigate**: Use the keyboard shortcuts below to browse incidents and alerts

## Keyboard Shortcuts

### Navigation

| Key       | Action                                   |
| --------- | ---------------------------------------- |
| `j` / `↓` | Move cursor down                         |
| `k` / `↑` | Move cursor up                           |
| `g`       | Go to first item                         |
| `G`       | Go to last item                          |
| `[`       | Previous page                            |
| `]`       | Next page                                |
| `Tab`     | Switch between Incidents and Alerts tabs |

### Actions

| Key     | Action                           |
| ------- | -------------------------------- |
| `Enter` | View details / Focus detail pane |
| `o`     | Open in browser                  |
| `r`     | Refresh data                     |

### General

| Key            | Action                |
| -------------- | --------------------- |
| `l`            | View debug logs       |
| `s`            | Open setup / settings |
| `A`            | About                 |
| `?`            | Show help             |
| `q` / `Ctrl+C` | Quit                  |

## Command Line Options

```bash  theme={null}
rootly-tui [flags]
```

| Flag           | Description                    |
| -------------- | ------------------------------ |
| `--debug`      | Enable debug logging to stderr |
| `--log <file>` | Write debug logs to a file     |
| `--version`    | Show version information       |

### Debug Mode

To troubleshoot API issues or unexpected behavior:

```bash  theme={null}
# Debug to stderr
rootly-tui --debug

# Debug to file
rootly-tui --log debug.log

# Debug to stderr, redirect to file
rootly-tui --debug 2> debug.log
```

Press `l` in the app to view logs in the built-in log viewer.

## Configuration

Configuration is stored at `~/.rootly-tui/config.yaml`:

```yaml  theme={null}
api_key: "your-api-key"
endpoint: "api.rootly.com"
timezone: "America/Los_Angeles"
language: "en_US"
```

To modify settings after initial setup, press `s` in the app.

## Supported Languages

The TUI supports the following languages:

* English (US/GB)
* Spanish
* French
* German
* Chinese (Simplified)
* Japanese
* Russian
* Portuguese (Brazilian)
* Hindi
* Arabic
* Bengali

## Requirements

* Terminal with 256-color support
* Minimum terminal size: 80x24

## Feedback & Support

* **Issues**: [GitHub Issues](https://github.com/rootlyhq/rootly-tui/issues)
* **Source Code**: [GitHub Repository](https://github.com/rootlyhq/rootly-tui)


Built with [Mintlify](https://mintlify.com).