# Source: https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Auggie CLI

> Install Auggie to get agentic coding capabilities in your terminal, on your server, or anywhere your code runs.

```sh  theme={null}
npm install -g @augmentcode/auggie
```

# About installing Auggie

Installing Auggie CLI is easy and will take you less than a minute. You can install Auggie CLI directly from npm anywhere you can run Node 22 or later. Many systems do not ship with the latest version of Node.js, so you may need to upgrade Node to use Auggie.

Auggie is currently in beta and may not run on all environments and terminal configurations.

## Automatic Updates

Auggie CLI automatically updates itself when running in interactive mode to ensure you always have the latest features and bug fixes. This feature is enabled by default and works seamlessly in the background. You can [disable automatic updates](/cli/reference#environment-variables).

## System requirements

* [**Node.js 22+**](https://nodejs.org/en/download/)
* **Platforms**: MacOS, Windows WSL, Linux
* **Shells**: zsh, bash, fish

### Interactive mode

Using Auggie in interactive mode requires a terminal that supports ANSI escape codes. We recommend using Ghostty, iTerm2, MacOS Terminal, Windows Terminal, Alacritty, Kitty, and other modern terminals.

If you are connecting to your shell over SSH or through tmux you may need to adjust your terminal settings or configuration to enable proper color support, font rendering, and interactivity.
