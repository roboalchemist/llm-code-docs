# Warp Documentation

Source: https://docs.warp.dev/llms-full.txt

---

# Quickstart Guide

Warp is the terminal for AI development, built to help developers ship faster with agents.

## Key Features:

* [**Code**](https://docs.warp.dev/documentation/code/code-overview): Warp is optimized for writing code by prompt on large, existing codebases. When Warp detects an opportunity to write code, it will enter an advanced code generation flow.
* [**Modern terminal**](https://docs.warp.dev/documentation/terminal/editor): A fast, editor-style input environment with cursor movement, multi-line editing, and rich completions. Every command or prompt appears in clean, navigable Blocks. Includes built-in SSH support, flexible window management, and full Mac/Windows/Linux compatibility.
* [**Agents**](https://docs.warp.dev/documentation/agents/agents-overview): Warp autodetects whether you are typing a natural language prompt or a command. Use natural language prompts to have Warp write code, debug issues, or write commands for you.
* [**Context management**](https://docs.warp.dev/documentation/agents/using-agents/agent-context): Warp will use codebase context, images, URLs, and documentation you save in Warp as context for agents.
* [**Multi-agent management**](https://docs.warp.dev/documentation/agents/using-agents/managing-agents): Warp is designed to have multiple agents running at once. Agents will send you notifications if they require your input, and you can see all your agents in one panel.
* [**Universal Input**](https://docs.warp.dev/documentation/terminal/universal-input): Type naturally and let Warp understand what you mean. You can talk to it in plain English, ask for fixes or explanations, and invoke agents without switching modes or special syntax.
* [**Code Review**](https://docs.warp.dev/documentation/code/code-review): Warp surfaces agent-generated code diffs in an integrated diff view, letting you inspect changes, refine them with natural language, or apply them when ready. You stay in control while agents produce and update code across your repo.
* [**Integrations**](https://github.com/warpdotdev/gitbook/blob/main/docs/broken-reference/README.md): Warp connects directly with your team’s tools. Use [Slack](https://docs.warp.dev/documentation/integrations/slack), [Linear](https://docs.warp.dev/documentation/integrations/linear), [GitHub Actions](https://docs.warp.dev/documentation/integrations/github-actions), and other integrations to trigger agents in the cloud, run workflows on your codebase, and make changes asynchronously.

You can fully customize Warp's appearance, prompts, settings, and keybindings to fit your preferences. Warp works with zsh, bash, fish, and PowerShell, and is built with Rust for high performance.

***

#### **Learn More**

For an inside look at how Warp is built, you can read the blog post on [How Warp Works](https://www.warp.dev/blog/how-warp-works). To understand the product philosophy behind Warp’s evolution, see [Warp 2.0: The Agentic Development Environment](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment). To see Warp in action, watch this walkthrough:

{% embed url="<https://youtu.be/0yAL7iA0po4>" %}

## Join the community

Stay connected to the team at Warp and get updates on the latest releases:

* Visit Warp's [Blog](https://www.warp.dev/blog) to read about new features and engineering topics.
* Join Warp's [Slack community](https://go.warp.dev/join-preview) to interact directly with Warp engineers and other developers.
* Subscribe to Warp's [YouTube](http://www.youtube.com/@warpdotdev) and [TikTok](https://www.tiktok.com/@warp.dev) channels for longer demos and insider stories.
* Visit [Warp University](https://app.gitbook.com/o/-MbqIZLCtzerswjFm7mh/s/c5dAwvMCRiTxUOdDicqy/) to get end-to-end workflows for coding, deploying, and becoming pro AI developer.
* Follow Warp on [Twitter](https://twitter.com/warpdotdev) for updates and tips.


# Installation and setup

Learn how to install Warp and get it running on your machine. All installation options support auto-update, ensuring you receive new features, bug fixes, and performance improvements.

{% hint style="info" %}
**Platform support:** Warp is supported on macOS (Intel and Mac Silicon), Windows (x86\_64 and ARM64), and Linux (x86\_64 and ARM64)
{% endhint %}

## Install Warp

{% hint style="warning" %}
**Visit** [Known Issues](https://docs.warp.dev/documentation/support-and-billing/known-issues) **to get more details on setting up and troubleshooting Warp.**
{% endhint %}

{% tabs %}
{% tab title="macOS" %}
{% hint style="info" %}
**Minimum requirements:** Intel or Apple silicon macOS 10.14 or above and hardware that supports [Metal](https://support.apple.com/en-us/HT205073).
{% endhint %}

**Download Warp and drag into your Applications folder**

{% embed url="<https://www.warp.dev/download>" %}
Download Warp
{% endembed %}

**Install using Homebrew by running the command below**

```bash
brew install --cask warp
```

After installation, you can find Warp in your Applications folder.
{% endtab %}

{% tab title="Windows" %}
{% hint style="info" %}
**Minimum requirements:** Warp requires Windows 10 version 1809 (build 17763) or later, Windows Server 2019 (build 17763) and Windows Server 2022 (build 20348) or later. This is a requirement for [Windows Pseudo Console (ConPTY)](https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/).
{% endhint %}

**Download Warp, then open and run the installer**

{% embed url="<https://www.warp.dev/download>" %}
Download Warp
{% endembed %}

**Install using WinGet by running the command below**

```powershell
winget install Warp.Warp
```

After installation, you can find Warp in the Start menu.
{% endtab %}

{% tab title="Linux" %}
{% hint style="info" %}
**Minimum requirements:** Linux distribution with glibc >= 2.31 (released Feb. 2020) and support for *either* [OpenGL ES 3.0+ or Vulkan](https://github.com/gfx-rs/wgpu?tab=readme-ov-file#supported-platforms).

This includes (but is not limited to) the following:

* Ubuntu 20.04
* Debian 11 ("bullseye")
* Fedora 32
* Arch Linux
  {% endhint %}

**Visit the Warp download page for the full list of Linux installation options**

{% embed url="<https://www.warp.dev/download>" %}
Download Warp
{% endembed %}

**Debian- and Ubuntu-based distributions**

The easiest way to install Warp is to download [x64 .deb package](https://app.warp.dev/download?package=deb) or [ARM64 deb package](https://app.warp.dev/download?package=deb_arm64). After downloading, you can install the package with:

```
sudo apt install ./<file>.deb
```

Installing the .deb package will automatically set up the Warp apt repository and signing key needed to automatically update Warp and verify the integrity of the downloaded packages.

Alternatively, you can manually configure the Warp apt repository and install Warp by running the following commands:

```
sudo apt-get install wget gpg
wget -qO- https://releases.warp.dev/linux/keys/warp.asc | gpg --dearmor > warpdotdev.gpg
sudo install -D -o root -g root -m 644 warpdotdev.gpg /etc/apt/keyrings/warpdotdev.gpg
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/warpdotdev.gpg] https://releases.warp.dev/linux/deb stable main" > /etc/apt/sources.list.d/warpdotdev.list'
rm warpdotdev.gpg
sudo apt update && sudo apt install warp-terminal
```

**RHEL-, Fedora-, and CentOS-based distributions**

The easiest way to install Warp is to download the [x64 .rpm package](https://app.warp.dev/download?package=rpm) or [ARM64 .rpm package](https://app.warp.dev/download?package=rpm_arm64). After downloading, you can install the package with:

```bash
sudo dnf install ./<file>.rpm
```

Installing the .rpm package will automatically set up the Warp yum repository. On first update, `dnf` will retrieve the signing key needed to verify the integrity of the downloaded packages.

Alternatively, you can manually configure the Warp yum repository and install Warp by running the following commands:

```bash
sudo rpm --import https://releases.warp.dev/linux/keys/warp.asc
sudo sh -c 'echo -e "[warpdotdev]\nname=warpdotdev\nbaseurl=https://releases.warp.dev/linux/rpm/stable\nenabled=1\ngpgcheck=1\ngpgkey=https://releases.warp.dev/linux/keys/warp.asc" > /etc/yum.repos.d/warpdotdev.repo'
sudo dnf install warp-terminal
```

**Arch Linux-based distributions**

The easiest way to install Warp is to download the [x64 .pkg.tar.zst package](https://app.warp.dev/download?package=pacman) or [ARM64 pacman package](https://app.warp.dev/download?package=pacman_arm64). After downloading, you can install the package with:

```bash
sudo pacman -U ./<file>.pkg.tar.zst
```

The first time you update Warp through the app, it will guide you through setting up the Warp pacman repository and signing key.

Alternatively, you can manually configure the Warp pacman repository and install Warp by running the following commands:

```bash
sudo sh -c "echo -e '\n[warpdotdev]\nServer = https://releases.warp.dev/linux/pacman/\$repo/\$arch' >> /etc/pacman.conf"
sudo pacman-key -r "linux-maintainers@warp.dev"
sudo pacman-key --lsign-key "linux-maintainers@warp.dev"
sudo pacman -Sy warp-terminal
```

**OpenSUSE- and SLE-based distributions**

The Warp yum repository also works for OpenSUSE- and SLE-based systems. Download the [x64 .rpm package](https://app.warp.dev/download?package=rpm) or [ARM64 .rpm package](https://app.warp.dev/download?package=rpm_arm64). After downloading, you can install the package with:

```bash
sudo zypper install ./<file>.rpm
```

Installing the .rpm package will automatically set up the Warp yum repository. On first update, `zypper` will retrieve the signing key needed to verify the integrity of the downloaded packages.

Alternatively, you can manually configure the Warp yum repository and install Warp by running the following commands:

```bash
sudo rpm --import https://releases.warp.dev/linux/keys/warp.asc
sudo sh -c 'echo -e "[warpdotdev]\nname=warpdotdev\ntype=rpm-md\nbaseurl=https://releases.warp.dev/linux/rpm/stable\nenabled=1\nautorefresh=1\ngpgcheck=1\ngpgkey=https://releases.warp.dev/linux/keys/warp.asc\nkeeppackages=0" > /etc/zypp/repos.d/warpdotdev.repo'
sudo zypper install warp-terminal
```

**AppImage**

We also provide an [AppImage](https://appimage.org), a single-file executable version of Warp. Installing Warp via a package manager is recommended, as it will ensure your system has all necessary dependencies installed.

You can download the Warp AppImage with the following commands:

```bash
# On x64 systems
curl -L "https://app.warp.dev/download?package=appimage" -o Warp-x64.AppImage
chmod +x Warp-x64.AppImage
```

```bash
# On ARM64 systems
curl -L "https://app.warp.dev/download?package=appimage_arm64" -o Warp-ARM64.AppImage
chmod +x Warp-ARM64.AppImage
```

**Running Warp on Linux**

If you installed a package, find Warp in your desktop manager or run `warp-terminal` on your terminal. If you're using the AppImage, you can launch it by navigating to the directory where the AppImage is located and running `./Warp-*.AppImage`.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Want to try our newest features? [Warp Preview](https://docs.warp.dev/documentation/community/warp-preview-and-alpha-program) is available on all platforms and architectures (macOS, Windows, Linux) for early access to experimental features.
{% endhint %}

## Initial Setup

### Log in to Warp (Optional)

After installation, you have the option to create a Warp account thru the "Sign up" bottom on the top right or in `Settings > Account > Sign up`. You have the option to skip this step. If you're having issues logging in, you can check out the [Login Troubleshooting](https://docs.warp.dev/documentation/support-and-billing/troubleshooting-login-issues) page.

{% hint style="info" %}
If you sign up using Google or GitHub, Warp only gets access to the associated email address. Visit the [Privacy](https://docs.warp.dev/documentation/privacy/privacy) page for more details on Warp's approach to privacy.
{% endhint %}

### Use Warp offline

You will only need an active internet connection when you open the Warp app for the first time. Once opened, [Warp is able to run with no internet connection](https://docs.warp.dev/documentation/support-and-billing/using-warp-offline), although certain features that require an internet connection like AI and real-time collaboration features will be unavailable.

### Import your settings

If you are migrating to Warp from a terminal like iTerm2, you can easily import your settings, such as keyboard shortcuts and color themes. For more details, visit the [Migrate to Warp](https://docs.warp.dev/documentation/getting-started/migrate-to-warp) docs.

### Set up your Warp default shell

Warp tries to load your login shell by default. Currently, Warp supports bash, fish, zsh, and PowerShell (pwsh). If your login shell is set to something else (for example, Nushell) Warp will load zsh by default.

Zsh is the default login and interactive shell on macOS (starting with macOS Catalina in 2019), replacing the bash shell. For most Linux distributions, the default shell is bash.

You can change your default shell by going to `Settings > Features > Session`. In the Startup shell for new sessions section, you can choose which shell you want Warp to use.


# Coding in Warp

Agents can generate and edit code directly from within Warp.

When you enter a git repo for the first time, Warp will enter an initialization flow to index your codebase and generate a WARP.md file.

As you're in the repo, Warp will enter an advanced code generation flow that supports both single-line and multi-file changes when it detects an opportunity to write code.

For example, Warp may write code when you prompt:

* **Code creation**: “Write a function in JavaScript to debounce an input”
* **Based on error outputs, suggest fixes**: “Fix this TypeScript error.”
* **Edit a single file**: “Update all instances of ‘var’ to ‘let’ in this file.”
* **Make batch changes**: “Add headers to all .py files in this directory”

**The best way to experience this is to try it yourself —** [*open the Prompt below in Warp*](https://app.warp.dev/drive/prompt/Generate-a-custom-Warp-theme-K8oloLrCZAHuaYKfz2cNqI)

{% code overflow="wrap" %}

```markup
Detect the correct Warp themes directory based on the current operating system:
- On macOS, use ~/.warp/themes/
- On Linux, use ${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/themes/
- On Windows, use $env:APPDATA\warp\Warp\data\themes\

Create the directory if it doesn’t already exist. 

Then, generate a custom Warp theme named {{theme_name}} in valid YAML format, following the official structure from Warp’s documentation. Exclude the background_image field, and do not include any extra or missing fields. Save the theme as {{theme_name}}.yaml in the detected themes directory.

Once the theme is created and verified, confirm completion by telling me where the theme file was saved.
```

{% endcode %}

***

### Context

#### Codebase Context

Warp can index your Git-tracked codebases to help agents understand your code and generate accurate, context-aware responses. **No code is stored on Warp servers**.

You can view and manage your indexed codebases under `Settings > Code > Codebase Index` and you can also specify whether to automatically index new folders as you navigate them.

If your codebase is large, you can exclude specific files by adding them to a `.warpindexingignore` file.

#### Other types of context

You can provide different types of input as context directly to the agent to guide its behavior and improve response quality. This includes:

* [Blocks](https://docs.warp.dev/agents/using-agents/agent-context#attaching-blocks-as-context) from your terminal output
* [Images](https://docs.warp.dev/agents/using-agents/agent-context#attaching-images-as-context)
* [Files and code](https://docs.warp.dev/agents/using-agents/agent-context#referencing-files-and-code-using) (using the @ symbol)
* [Public websites](https://docs.warp.dev/agents/using-agents/agent-context#referencing-websites-via-urls) via URLs

#### Warp Drive as Context

Agents pull directly from your [**Warp Drive**](https://docs.warp.dev/features/warp-drive) contents to generate more accurate responses -- including your **Workflows**, **Notebooks**, **Prompts**, and **Environment Variables**.

* When used, context appears under the “References” or “Derived from” section in the conversation.
* This setting is **enabled by default** and can be managed via: `Settings > AI > Knowledge > Warp Drive as Agent Mode Context`.

#### Rules

**Rules** let you provide persistent context to Agents, enabling smarter and more personalized responses.

You can create global rules (accessed through [Warp Drive](https://docs.warp.dev/features/warp-drive) > Personal > Rules) or project scoped rules, defined in a WARP.md file.

**Examples of Rules include:**

* Coding standards and best practices
* Project- or workspace-specific guidelines
* Personal preferences for tools, formatting, or behavior

How to access project-specific Rules

1. From the file-searcher, CMD+O and search "WARP.md"
2. From the file tree, click the "code" icon when in a repo

How to access Global Rules

1. From the [Warp Drive](https://docs.warp.dev/features/warp-drive) > Personal > Rules
2. From the [Command Palette](https://github.com/warpdotdev/gitbook/blob/main/docs/features/warp-ai/command-palette.md), search for "Open AI Rules"
3. From the Settings panel, `Settings > AI > Knowledge > Manage Rules`
4. From the macOS Menu, `AI > Open Rules`


# Agents in Warp

Warp's agents are capable collaborators that help you write code, debug issues, and complete terminal workflows -- all from natural language prompts.

Describe what you want to do (*you can even use your voice*), and Warp’s agents will intelligently take action using your environment, codebase, and saved context to tailor their responses.

**Agents can:**

1. Write and edit code across single or multiple files.
2. Fix errors based on output or stack traces.
3. Execute shell commands and use the output to guide next steps
4. Automatically recover from common errors and retry with adjustments.
5. Learn and integrate with any tool that offers public docs or `--help`.
6. Leverage your saved [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) contents, [MCP servers](https://docs.warp.dev/knowledge-and-collaboration/mcp), and [Rules](https://docs.warp.dev/knowledge-and-collaboration/rules) to provide tailored responses.

**Give this prompt a try —** [*open the below Prompt in Warp*](https://app.warp.dev/drive/prompt/Clone-and-install-Warps-themes-repository-PkK9Zw16SCD3JKzOUoGuj4)

{% code overflow="wrap" %}

```markup
Detect my current operating system. Based on that, navigate to the appropriate Warp themes directory (e.g. ~/.warp/ on macOS). 

Then, clone the official Warp themes repository using SSH (git@github.com:warpdotdev/themes.git) into that directory, following the structure and instructions provided in the repo’s README. If SSH does not work, try HTTPS (https://github.com/warpdotdev/themes.git) or via the GitHub CLI (gh repo clone warpdotdev/themes).
```

{% endcode %}

### Agent Autonomy

Under `Settings > AI > Agents > Permissions`, you can control how much autonomy the agent has when performing different types of actions, such as:

* Reading files
* Creating plans
* Executing commands
* Calling MCP servers, and more

For each action, you can set the autonomy level to one of the following:

* Let the agent decide
* Always prompt for confirmation
* Always allow
* Never

You can also configure an **allowlist** and **denylist** for specific commands you always want to run—either with or without confirmation.

### Agent Profiles

Define profiles in `Settings > AI` with unique permissions and model choices. You can switch profiles at any time by clicking the "profile" icon in Warp's input area. In addition to your default permissions, you may create:

* YOLO mode: Loose permissions for using in personal projects
* Prod mode: Limit AI permissions to "Always Ask" when in high-risk environments like your production server

### Managing multiple agents

You can run multiple agents in Warp simultaneously, monitor their status, and step in when needed—without losing track of what’s happening across your sessions. Each tab includes a [status icon](https://docs.warp.dev/agents/using-agents/managing-agents#agent-status-indicators) that shows the agent’s current state. All of your active agents are tracked in the [Agent Management Panel](https://docs.warp.dev/agents/using-agents/managing-agents#agent-management-panel), located in the top-right corner next to your avatar.

Agents will also [notify](https://docs.warp.dev/agents/using-agents/managing-agents#agent-status-indicators) you when they need input, such as permission to run a command or approval to apply a code diff. This lets you focus on other work, knowing you’ll be alerted when your attention is required.


# Customizing Warp

Learn some of the ways you can customize Warp's appearance and behavior.

## Customizing Warp's appearance

Warp has many [Appearance](https://docs.warp.dev/documentation/terminal/appearance) settings you can configure:

* [**Themes**](https://docs.warp.dev/appearance/themes): You can choose from pre-loaded themes or create your own [custom theme](https://docs.warp.dev/appearance/custom-themes), using .yaml or based on a background image you upload.
* **Input format**: Choose between Warp's Standard input or Classic input. Standard enables easier access to AI features, while Classic resembles a traditional terminal input more closely.
* [**Text and fonts**](https://docs.warp.dev/appearance/text-fonts-cursor): You can customize your font type and font size. You can also adjust the font to improve readability and accessibility.
* [**Input position**](https://docs.warp.dev/appearance/input-position): Set your prompt and command line to the top or bottom of your Warp window.

Navigate to `Settings > Appearance` to customize your setup.

{% embed url="<https://youtu.be/fzb1JcZ0fFA>" %}

### Modify behavior settings

There are a number of behavior settings and features that will help you customize Warp to best suit your needs:

* [Dedicated window](https://docs.warp.dev/features/windows/global-hotkey#dedicated-window): Dedicated hotkey window (also known as Quake Mode) allows you to customize your window's position, width, and height ratio relative to your active screen size.
* [Tabs](https://docs.warp.dev/documentation/terminal/windows/tabs): Organize your windows into multiple sessions, and customize them with different titles and/or colors.
* [Split panes](https://docs.warp.dev/features/windows/split-panes): Divide any tab into multiple panels, side-by-side or stacked.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-52a1ba898ec1b52dc1632e36c63a1700e713a749%2Ftab-splitpane-examples.png?alt=media" alt=""><figcaption><p>Organize tabs and divide them into multiple panels</p></figcaption></figure>

* [Auto suggestions](https://docs.warp.dev/features/command-completions/autosuggestions): As you type, Warp will automatically suggest commands based on shell history and possible completions.
* [Completions](https://docs.warp.dev/features/command-completions/completions): When you press TAB, Warp will suggest commands, option names, and path parameters for you. Customize your TAB key behavior under `Settings > Features`.
* [Vim keybindings](https://docs.warp.dev/features/editor/vim): Warp supports default Vim keybindings, allowing for keyboard-driven text editing.
* [Keyboard shortcuts](https://docs.warp.dev/features/keyboard-shortcuts): Warp supports commonly used keyboard shortcuts. You can also set custom keyboard shortcuts by creating new commands or editing existing shortcuts.
* [Open files and links](https://docs.warp.dev/features/files-and-links): Using your cursor, you can open files, folders, and URL links that are within Blocks. You can also [configure the default editor to open files](https://docs.warp.dev/features/files-and-links#files-and-links-1).
* [Command Corrections](https://docs.warp.dev/documentation/terminal/entry/command-corrections): Get auto-correct suggestions on commands to catch typos, forgotten flags, and general console errors.


# Migrate to Warp

Learn how to import settings from other terminals when you switch to Warp.

## From iTerm2

You can easily import your settings from iTerm2 to Warp. This includes custom keybindings and color themes.

To do so, you can open the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) and search for Import External Settings. This will enter you into the workflow to import your settings.

Select **iTerm2 Profile: Default** to import your settings.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-355fb38a9eca18812a736fe79f11c7ee142ec30f%2Fmigrate-to-warp.png?alt=media" alt=""><figcaption><p>Select a settings profile to import</p></figcaption></figure>

Warp will only import settings associated with the Default profile.

### Choose your Prompt

Next, you can choose your [prompt](https://docs.warp.dev/documentation/terminal/appearance/prompt) and decide whether or not to inherit your existing prompt configuration. There are two prompt options:

1. [Warp prompt](https://docs.warp.dev/documentation/terminal/appearance/prompt#warp-prompt): This is Warp's native prompt that you can customize to meet your needs. In `Settings > Appearance > Prompt`, you can drag and drop context chips into your Warp prompt to display specific information, like git branches or timestamps.
2. [Shell prompt (PS1)](https://docs.warp.dev/documentation/terminal/appearance/prompt#custom-prompt): This custom prompt inherits your pre-existing prompt configuration. Select this option if you want your Warp prompt to match your settings from iTerm2.

After choosing a prompt, you’re ready to start using Warp.

### Import additional settings

After importing your iTerm2 profile and choosing your prompt, you might have additional settings from iTerm2 that you would like to configure. For example:

* Customizing your dedicated hotkey window, allowing you to customize your windows relative to your active screen size.
* Dividing and organizing tabs into multiple panels or terminal sessions.
* Setting up your keyboard shortcuts and completion suggestions.

You can find more information on these behavior settings in our Quickstart guide.


# Supported Shells

Warp supports popular shells across macOS, Windows, and Linux. On macOS and Linux, this includes bash, zsh, fish, and PowerShell (pwsh). On Windows, this includes PowerShell 5 & 7, WSL2, and Git Bash.

## Warp default shell

Warp tries to load your login shell by default. Currently, Warp supports bash, fish, zsh, and PowerShell (pwsh). If your login shell is set to something else (e.g. Nushell) Warp will show a banner indicating it's not supported and load the default shells listed below:

* On macOS, zsh is the default shell.
* On Windows, PowerShell (pwsh) is the default shell.
* On Linux, bash is the the default shell.

{% hint style="info" %}
If you run into issues configuring your RC files (`~/.bashrc`, `~/.zshrc`, `config.fish`, `Microsoft.PowerShell_profile.ps1`) with Warp, please see [Configuring and debugging your RC files](https://docs.warp.dev/help/known-issues#configuring-and-debugging-your-rc-files).
{% endhint %}

### Changing what shell Warp uses

To change the default shell, e recommend you choose a shell in Warp by going to `Settings > Features` and scrolling to the `Session` section, then select the "Startup shell for new sessions"

{% hint style="info" %}
The changes to your shell will only take effect when you start a new session.
{% endhint %}

## Customizing Your Shell Environment

### Customize Your zsh Shell Environment

Zsh can be customized via the `~/.zshrc` file, which runs whenever a new session starts (window, tab, or pane). Use it to set environment variables, aliases, and customize the [prompt](https://docs.warp.dev/features/prompt).

#### Editing the .zshrc File

Edit `~/.zshrc` using `nano ~/.zshrc` or `vi ~/.zshrc`.

{% hint style="info" %}
Files starting with a dot (`.`) are hidden by default. Check your file explorer’s settings to show hidden files.
{% endhint %}

#### Reloading the zshrc File

Apply changes by running `source ~/.zshrc` or restarting Warp/opening a new session.

### Customize Your Bash Shell Environment

Bash is pre-installed on macOS and can be customized using `~/.bashrc` (for non-login shells) or `~/.bash_profile` (for login shells). Use these files to set environment variables, aliases, and customize the [prompt](https://docs.warp.dev/features/prompt).

#### Editing the .bashrc File

Edit `~/.bashrc` using `nano ~/.bashrc` or `vi ~/.bashrc`.

#### Reloading the bashrc File

Apply changes by running `source ~/.bashrc` or restarting Warp/opening a new session.

{% hint style="info" %}
Files starting with a dot (`.`) are hidden by default. Check your file explorer’s settings to show hidden files.
{% endhint %}

### Customize Your Fish Shell Environment

Fish is a user-friendly shell with autosuggestions and syntax highlighting. Its configuration file is `~/.config/fish/config.fish`.

#### Editing the config.fish File

Edit `~/.config/fish/config.fish` using `nano ~/.config/fish`. Use it to set environment variables, aliases, and functions.

#### Reloading the config.fish File

Apply changes by running `source ~/.config/fish` or restarting Warp/opening a new session.

{% hint style="info" %}
Unlike Bash and Zsh, Fish does not use `export VAR=value`. Use `set -Ux VAR value` for persistent environment variables.
{% endhint %}

### Customize Your PowerShell Shell Environment

PowerShell can be customized via its profile script, located at `$PROFILE`. Check if it exists with `Test-Path $PROFILE`, and create it if needed with `New-Item -Path $PROFILE -ItemType File -Force`.

#### Editing the PowerShell Profile

Edit the profile using `code $PROFILE`, and use it to set environment variables, aliases, custom prompts, and scripts.

#### Reloading the PowerShell Profile

Apply changes by restarting Warp or opening a new session.

{% hint style="info" %}
PowerShell’s execution policy may block scripts. Enable profile execution with:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

{% endhint %}

## Additional shell guidance for macOS

#### Setting up zsh on Warp

By default, macOS ships with [zsh](https://zsh.sourceforge.io/Doc/Release/zsh_toc.html) located in `/bin/zsh`. You can confirm this location by typing `which zsh` in Warp. You can also check the version of zsh installed on your system by simply typing the following:

`$ zsh --version`

### Using fish shell with Warp on macOS

#### Step 1: Install fish

While bash, and zsh come pre-installed on macOS systems, fish shell does not. So before using fish with Warp, you will need to install it. Install fish 3.6 or above using one of the methods listed below -

1. With Homebrew: If you already have homebrew installed, you can simply type `brew install fish`, and follow the instructions.
2. Download the installer at [fishshell.com](https://fishshell.com/)

#### Step 2: Switch to fish as the default shell

Once you’ve installed fish on your computer, you can set it as your default shell, so Warp will use it every time a new tab, pane, or window is opened. You can either make fish the default shell for only Warp, from the session settings (`Settings > Features > Session`), or for your user account. To change your account's default shell, you need to run two commands.

**If you used Homebrew to install fish on a macOS or if you used the Mac installer** available on fishshell.com to install fish, type the following two commands in Warp:

```
echo $(which fish) | sudo tee -a /etc/shells
chsh -s $(which fish)
```

{% hint style="info" %}
If you prefer, you can also manually edit the `/etc/shells` file using the editor of your choice (you may need sudo privileges).
{% endhint %}

{% hint style="info" %}
**Why the different locations?** The location of fish depends on how it was installed. Homebrew installs programs under `/usr/local` on Macs running Intel processors, but under `/opt/homebrew` for Macs running Apple Silicon. So, if you used Homebrew to install fish on a Mac with Apple Silicon, the location of the executable is - `/opt/homebrew/bin/fish`.\
You can identify where fish is installed by running `which fish`.
{% endhint %}

### Using PowerShell (pwsh) with Warp on macOS

#### Step 1: Install PowerShell

While bash, and zsh come pre-installed on macOS systems, PowerShell shell does not. So before using PowerShell with Warp, you will need to install it. Install PowerShell 7.0 or above using one of the methods listed below -

1. With Homebrew: If you already have homebrew installed, you can simply type `brew install powershell/tap/powershell`, and follow the instructions.
2. Download from the [official Microsoft website](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell).

#### Step 2: Switch to pwsh as the default shell

Once you’ve installed PowerShell on your computer, you can set it as your default shell, so Warp will use it every time a new tab, pane, or window is opened. You can either make pwsh the default shell for only Warp, from the session settings (`Settings > Features > Session`), or for your user account. To change your account's default shell, you need to run two commands.

```
echo $(which pwsh) | sudo tee -a /etc/shells
chsh -s $(which pwsh)
```

{% hint style="info" %}
If you prefer, you can also manually edit the `/etc/shells` file using the editor of your choice (you may need sudo privileges).
{% endhint %}

{% hint style="info" %}
**Why the different locations?** The location of pwsh depends on how it was installed. Homebrew installs programs under `/usr/local` on Macs running Intel processors, but under `/opt/homebrew` for Macs running Apple Silicon. So, if you used Homebrew to install pwsh on a Mac with Apple Silicon, the location of the executable is - `/opt/homebrew/bin/pwsh`.\
You can identify where pwsh is installed by running `which pwsh`.
{% endhint %}

## Using Warp with shells on Windows

On Windows, Warp's default shell is PowerShell 7 (pwsh). Warp for Windows supports several shells:

* PowerShell 7 (default)
* PowerShell 5
* Windows Subsystem for Linux (WSL2)
* Git Bash

{% hint style="info" %}
Windows Command Prompt (cmd.exe) is not currently supported. For more information and updates about cmd.exe support, please see [this GitHub issue](https://github.com/warpdotdev/Warp/issues/5882).
{% endhint %}


# Keyboard Shortcuts

Warps commonly used keyboard shortcuts.

Warp opens with a shortcut screen showing some of the most commonly used keyboard shortcuts. Hide the shortcut screen by clicking the x button. Quickly view keyboard shortcuts via the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or the Resource Center keyboard shortcut sidebar.

## Custom Keyboard Shortcuts

Set custom, clear, or default keyboard shortcuts by navigating to `Settings > Keyboard Shortcuts`. Search through the re-mappable actions or existing shortcuts using the search bar.

Remap the keyboard shortcuts using a file. See our [keysets repository](https://github.com/warpdotdev/keysets/tree/main) for instructions.

{% hint style="info" %}
On macOS, [system keyboard shortcuts](https://support.apple.com/en-us/HT201236) like `CMD-ESC`, `CMD-BACKTICK`, `CMD-TAB`, `CMD-PERIOD`, and `CMD-TILDE` need to be [unbound](https://support.apple.com/guide/mac-help/keyboard-shortcuts-mchlp2262/mac) before you can use them in Warp.
{% endhint %}

{% hint style="warning" %}
Keybinds that conflict with others are highlighted with an orange border.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b1deaff708f95fdb8ebffe491a823ccea24bac6c%2Fkeybinds-conflict.png?alt=media&#x26;token=e89cb316-87ee-4c85-a0f5-e21270b15649" alt="keybinds that conflict with others are highlighted in orange"><figcaption><p>Keybind Conflict Example</p></figcaption></figure>

## All Available Shortcuts

{% tabs %}
{% tab title="macOS" %}
**Warp Essentials**

| Shortcut       | Command                      | Action                                         |
| -------------- | ---------------------------- | ---------------------------------------------- |
| `CMD-D`        | Split Pane Right             | `pane_group:add_right`                         |
| `CTRL-CMD-L`   | Launch Configuration Palette | `workspace:toggle_launch_config_palette`       |
| `CTRL-CMD-T`   | Open Theme Picker            | `workspace:show_theme_chooser`                 |
| `CTRL-R`       | Command Search               | `workspace:show_command_search`                |
| `CTRL-SHIFT-R` | Workflows                    | `input:toggle_workflows`                       |
| `` CTRL-` ``   | Generate                     | `input:toggle_natural_language_command_search` |
| `CMD-L`        | Focus Terminal Input         | `terminal:focus_input`                         |
| `CTRL-I`       | Warpify Subshell             | `terminal:trigger_subshell_bootstrap`          |
| `CMD-\`        | Warp Drive                   | `terminal:toggle_warp_drive`                   |
| `CMD-O`        | File search                  |                                                |
| `CMD-P`        | Open command pallette        |                                                |

**Blocks**

| Shortcut          | Command                           | Action                                                 |
| ----------------- | --------------------------------- | ------------------------------------------------------ |
| `ALT-DOWN`        | Select the Closest Bookmark Down  | `terminal:select_bookmark_down`                        |
| `ALT-SHIFT-CMD-C` | Copy Command Output               | `terminal:copy_outputs`                                |
| `ALT-UP`          | Select the Closest Bookmark Up    | `terminal:select_bookmark_up`                          |
| `CMD-A`           | Select All Blocks                 | `terminal:select_all_blocks`                           |
| `CMD-K`           | Clear Blocks                      | `terminal:clear_blocks`                                |
| `CMD-B`           | Bookmark Selected Block           | `terminal:bookmark_selected_block`                     |
| `CMD-DOWN`        | Select Next Block                 | `terminal:select_next_block`                           |
| `CMD-I`           | Reinput Selected Commands         | `terminal:reinput_commands`                            |
| `CMD-UP`          | Select Previous Block             | `terminal:select_previous_block`                       |
| `CTRL-M`          | Open Block Context Menu           | `terminal:open_block_list_context_menu_via_keybinding` |
| `SHIFT-CMD-C`     | Copy Command                      | `terminal:copy_commands`                               |
| `SHIFT-CMD-I`     | Reinput Selected Commands as Root | `terminal:reinput_commands_with_sudo`                  |
| `SHIFT-CMD-S`     | Share Selected Block              | `terminal:open_share_modal`                            |
| `SHIFT-DOWN`      | Expand Selected Blocks Below      | `terminal:expand_block_selection_below`                |
| `SHIFT-UP`        | Expand Selected Blocks Above      | `terminal:expand_block_selection_above`                |

**Input Editor**

| Shortcut          | Command                                   | Action                                     |
| ----------------- | ----------------------------------------- | ------------------------------------------ |
| `ALT-BACKSPACE`   | Delete Word Left                          | `editor:delete_word_left`                  |
| `ALT-CMD-F`       | Fold Selected Ranges                      | `editor_view:fold_selected_ranges`         |
| `ALT-CMD-[`       | Fold                                      | `editor_view:fold`                         |
| `ALT-CMD-]`       | Unfold                                    | `editor_view:unfold`                       |
| `ALT-DELETE`      | Delete Word Right                         | `editor:delete_word_right`                 |
| `CMD-A`           | Select All                                | `editor_view:select_all`                   |
| `CMD-BACKSPACE`   | Delete All Left                           | `editor_view:delete_all_left`              |
| `CMD-DELETE`      | Delete All Right                          | `editor_view:delete_all_right`             |
| `CMD-DOWN`        | Move Cursor to the Bottom                 | `editor_view:cmd_down`                     |
| `CMD-I`           | Inspect Command                           | `editor_view:cmd_i`                        |
| `CMD-LEFT`        | Home                                      | `editor_view:home`                         |
| `CMD-RIGHT`       | End                                       | `editor_view:end`                          |
| `CTRL-A`          | Move to Start of Line                     | `editor_view:move_to_line_start`           |
| `CTRL-B`          | Move Cursor Left                          | `editor_view:left`                         |
| `CTRL-C`          | Clear Command Editor                      | `editor_view:clear_buffer`                 |
| `CTRL-D`          | Delete                                    | `editor_view:delete`                       |
| `CTRL-E`          | Move to End of Line                       | `editor_view:move_to_line_end`             |
| `CTRL-F`          | Move Cursor Right / Accept Autosuggestion | `editor_view:right`                        |
| `CTRL-G`          | Add Selection for Next Occurrence         | `editor_view:add_next_occurrence`          |
| `CTRL-H`          | Remove the Previous Character             | `editor_view:backspace`                    |
| `CTRL-J`          | Insert Newline                            | `editor_view:insert_newline`               |
| `CTRL-K`          | Cut All Right                             | `editor_view:cut_all_right`                |
| `CTRL-L`          | Clear Screen                              | `input:clear_screen`                       |
| `CTRL-N`          | Move Cursor Down                          | `editor_view:down`                         |
| `CTRL-P`          | Move Cursor Up                            | `editor_view:up`                           |
| `CTRL-SHIFT-A`    | Select to Start of Line                   | `editor_view:select_to_line_start`         |
| `CTRL-SHIFT-B`    | Select One Character to the Left          | `editor_view:select_left`                  |
| `CTRL-SHIFT-DOWN` | Add Cursor Below                          | `editor_view:add_cursor_below`             |
| `CTRL-SHIFT-E`    | Select to End of Line                     | `editor:select_to_line_end`                |
| `CMD-Z`           | Undo                                      | `editor:undo`                              |
| `CMD-SHIFT-Z`     | Redo                                      | `editor:redo`                              |
| `CTRL-SHIFT-F`    | Select One Character to the Right         | `editor:select_right`                      |
| `CTRL-SHIFT-N`    | Select Down                               | `editor_view:select_down`                  |
| `CTRL-SHIFT-P`    | Select Up                                 | `editor_view:select_up`                    |
| `CTRL-SHIFT-UP`   | Add Cursor Above                          | `editor_view:add_cursor_above`             |
| `CTRL-U`          | Copy and Clear Selected Lines             | `editor_view:clear_and_copy_lines`         |
| `CTRL-W`          | Cut Word Left                             | `editor_view:cut_word_left`                |
| `META-.`          | Insert Last Word of Previous Command      | `editor:insert_last_word_previous_command` |
| `META-A`          | Move to the Start of the Paragraph        | `editor_view:move_to_paragraph_start`      |
| `META-B`          | Move Backward One Word                    | `editor_view:move_backward_one_word`       |
| `META-D`          | Cut Word Right                            | `editor_view:cut_word_right`               |
| `META-E`          | Move to the End of the Paragraph          | `editor_view:move_to_paragraph_end`        |
| `META-F`          | Move Forward One Word                     | `editor_view:move_forward_one_word`        |
| `CTRL-OPT-LEFT`   | Move Backward One Subword                 | `editor_view:move_backward_one_subword`    |
| `CTRL-OPT-RIGHT`  | Move Forward One Subword                  | `editor_view:move_forward_one_subword`     |
| `SHIFT-CMD-K`     | Clear Selected Lines                      | `editor_view:clear_lines`                  |
| `SHIFT-META-<`    | Move to the Start of the Buffer           | `editor_view:move_to_buffer_start`         |
| `SHIFT-META->`    | Move to the End of the Buffer             | `editor_view:move_to_buffer_end`           |
| `SHIFT-META-B`    | Select One Word to the Left               | `editor_view:select_left_by_word`          |
| `SHIFT-META-F`    | Select One Word to the Right              | `editor_view:select_right_by_word`         |

**Terminal**

| Shortcut          | Command                                           | Action                                       |
| ----------------- | ------------------------------------------------- | -------------------------------------------- |
| `ALT-CMD-DOWN`    | Switch Panes Down                                 | `pane_group:navigate_down`                   |
| `ALT-CMD-LEFT`    | Switch Panes Left                                 | `pane_group:navigate_left`                   |
| `ALT-CMD-RIGHT`   | Switch Panes Right                                | `pane_group:navigate_right`                  |
| `ALT-CMD-UP`      | Switch Panes Up                                   | `pane_group:navigate_up`                     |
| `ALT-CMD-V`       | \[a11y] Set Concise Accessibility Announcements   | `workspace:set_a11y_concise_verbosity_level` |
| `ALT-CMD-V`       | \[a11y] Set Verbose Accessibility Announcements   | `workspace:set_a11y_verbose_verbosity_level` |
| `CMD-,`           | Open Settings                                     | `workspace:show_settings_modal`              |
| `CMD-,`           | Open Settings: Account                            | `workspace:show_settings_account_page`       |
| `CMD-G`           | Find the Next Occurrence of Your Search Query     | `find:find_next_occurrence`                  |
| `CMD-P`           | Toggle Command Palette                            | `workspace:toggle_command_palette`           |
|                   | Toggle Mouse Reporting                            | `workspace:toggle_mouse_reporting`           |
| `CMD-[`           | Activate Previous Pane                            | `pane_group:navigate_prev`                   |
| `CMD-]`           | Activate Next Pane                                | `pane_group:navigate_next`                   |
| `CTRL-CMD-DOWN`   | Resize Pane > Move Divider Down                   | `pane_group:resize_down`                     |
| `CTRL-CMD-K`      | Open Keybindings Editor                           | `workspace:show_keybinding_settings`         |
| `CTRL-CMD-LEFT`   | Resize Pane > Move Divider Left                   | `pane_group:resize_left`                     |
| `CTRL-CMD-RIGHT`  | Resize Pane > Move Divider Right                  | `pane_group:resize_right`                    |
| `CTRL-CMD-UP`     | Resize Pane > Move Divider Up                     | `pane_group:resize_up`                       |
| `CTRL-SHIFT-?`    | Open Resource Center                              | `workspace:toggle_resource_center`           |
| `SHIFT-CMD-D`     | Split Pane Down                                   | `pane_group:add_down`                        |
| `SHIFT-CMD-ENTER` | Toggle Maximize Active Pane                       | `pane_group:toggle_maximize_pane`            |
| `SHIFT-CMD-G`     | Find the Previous Occurrence of Your Search Query | `find:find_prev_occurrence`                  |
| `SHIFT-CMD-P`     | Toggle Navigation Palette                         | `workspace:toggle_navigation_palette`        |

**Fundamentals**

| Shortcut           | Command                    | Action                           |
| ------------------ | -------------------------- | -------------------------------- |
| `CMD--`            | Decrease Font Size         | `workspace:decrease_font_size`   |
| `CMD-0`            | Reset Font Size to Default | `workspace:reset_font_size`      |
| `CMD-1`            | Switch to 1st Tab          | `workspace:activate_first_tab`   |
| `CMD-2`            | Switch to 2nd Tab          | `workspace:activate_second_tab`  |
| `CMD-3`            | Switch to 3rd Tab          | `workspace:activate_third_tab`   |
| `CMD-4`            | Switch to 4th Tab          | `workspace:activate_fourth_tab`  |
| `CMD-5`            | Switch to 5th Tab          | `workspace:activate_fifth_tab`   |
| `CMD-6`            | Switch to 6th Tab          | `workspace:activate_sixth_tab`   |
| `CMD-7`            | Switch to 7th Tab          | `workspace:activate_seventh_tab` |
| `CMD-8`            | Switch to 8th Tab          | `workspace:activate_eighth_tab`  |
| `CMD-9`            | Switch to Last Tab         | `workspace:activate_last_tab`    |
| `CMD-=`            | Increase Font Size         | `workspace:increase_font_size`   |
| `CMD-C`            | Copy                       | `terminal:copy`                  |
| `CMD-F`            | Find                       | `terminal:find`                  |
| `CMD-V`            | Paste                      | `terminal:paste`                 |
| `CMD-T`            | Open New Tab               | `workspace:open_new_tab`         |
| `SHIFT-CMD-T`      | Reopen Closed Tab          | `workspace:reopen_closed_tab`    |
| `CTRL-SHIFT-LEFT`  | Move Tab Left              | `workspace:move_tab_left`        |
| `CTRL-SHIFT-RIGHT` | Move Tab Right             | `workspace:move_tab_right`       |
| `SHIFT-CMD-{`      | Activate Previous Tab      | `workspace:activate_prev_tab`    |
| `SHIFT-CMD-}`      | Activate Next Tab          | `workspace:activate_next_tab`    |
| {% endtab %}       |                            |                                  |

{% tab title="Windows" %}
**Warp Essentials**

| Shortcut       | Command                      | Action                                         |
| -------------- | ---------------------------- | ---------------------------------------------- |
| `CTRL-SHIFT-D` | Split Pane Right             | `pane_group:add_right`                         |
|                | Launch Configuration Palette | `workspace:toggle_launch_config_palette`       |
|                | Open Theme Picker            | `workspace:show_theme_chooser`                 |
| `CTRL-R`       | Command Search               | `workspace:show_command_search`                |
| `CTRL-SHIFT-R` | Workflows                    | `input:toggle_workflows`                       |
| `` CTRL-` ``   | Generate                     | `input:toggle_natural_language_command_search` |
| `CTRL-SHIFT-L` | Focus Terminal Input         | `terminal:focus_input`                         |
| `CTRL-I`       | Warpify Subshell             | `terminal:trigger_subshell_bootstrap`          |
| `CTRL-SHIFT-\` | Warp Drive                   | `terminal:toggle_warp_drive`                   |

**Blocks**

| Shortcut           | Command                           | Action                                                 |
| ------------------ | --------------------------------- | ------------------------------------------------------ |
| `ALT-DOWN`         | Select the Closest Bookmark Down  | `terminal:select_bookmark_down`                        |
| `CTRL-SHIFT-ALT-C` | Copy Command Output               | `terminal:copy_outputs`                                |
| `ALT-UP`           | Select the Closest Bookmark Up    | `terminal:select_bookmark_up`                          |
| `CTRL-SHIFT-A`     | Select All Blocks                 | `terminal:select_all_blocks`                           |
| `CTRL-SHIFT-K`     | Clear Blocks                      | `terminal:clear_blocks`                                |
| `CTRL-SHIFT-B`     | Bookmark Selected Block           | `terminal:bookmark_selected_block`                     |
| `CTRL-DOWN`        | Select Next Block                 | `terminal:select_next_block`                           |
| `CTRL-SHIFT-I`     | Reinput Selected Commands         | `terminal:reinput_commands`                            |
| `CTRL-UP`          | Select Previous Block             | `terminal:select_previous_block`                       |
|                    | Open Block Context Menu           | `terminal:open_block_list_context_menu_via_keybinding` |
| `CTRL-SHIFT-C`     | Copy Command                      | `terminal:copy_commands`                               |
|                    | Reinput Selected Commands as Root | `terminal:reinput_commands_with_sudo`                  |
| `CTRL-SHIFT-S`     | Share Selected Block              | `terminal:open_share_modal`                            |
| `SHIFT-DOWN`       | Expand Selected Blocks Below      | `terminal:expand_block_selection_below`                |
| `SHIFT-UP`         | Expand Selected Blocks Above      | `terminal:expand_block_selection_above`                |

**Input Editor**

| Shortcut           | Command                                   | Action                                     |
| ------------------ | ----------------------------------------- | ------------------------------------------ |
| `CTRL-BACKSPACE`   | Delete Word Left                          | `editor:delete_word_left`                  |
| `CTRL-ALT-F`       | Fold Selected Ranges                      | `editor_view:fold_selected_ranges`         |
| `CTRL-ALT-[`       | Fold                                      | `editor_view:fold`                         |
| `CTRL-ALT-]`       | Unfold                                    | `editor_view:unfold`                       |
| `CTRL-DELETE`      | Delete Word Right                         | `editor:delete_word_right`                 |
| `CTRL-A`           | Select All                                | `editor_view:select_all`                   |
| `CTRL-Y`           | Delete All Left                           | `editor_view:delete_all_left`              |
|                    | Delete All Right                          | `editor_view:delete_all_right`             |
| `CTRL-END`         | Move Cursor to the Bottom                 | `editor_view:cmd_down`                     |
| `CTRL-I`           | Inspect Command                           | `editor_view:cmd_i`                        |
| `HOME`             | Home                                      | `editor_view:home`                         |
| `END`              | End                                       | `editor_view:end`                          |
| `CTRL-A`           | Move to Start of Line                     | `editor_view:move_to_line_start`           |
| `CTRL-B`           | Move Cursor Left                          | `editor_view:left`                         |
| `CTRL-C`           | Clear Command Editor                      | `editor_view:clear_buffer`                 |
| `CTRL-D`           | Delete                                    | `editor_view:delete`                       |
| `CTRL-E`           | Move to End of Line                       | `editor_view:move_to_line_end`             |
| `CTRL-F`           | Move Cursor Right / Accept Autosuggestion | `editor_view:right`                        |
| `CTRL-G`           | Add Selection for Next Occurrence         | `editor_view:add_next_occurrence`          |
| `CTRL-H`           | Remove the Previous Character             | `editor_view:backspace`                    |
| `CTRL-J`           | Insert Newline                            | `editor_view:insert_newline`               |
| `CTRL-K`           | Cut All Right                             | `editor_view:cut_all_right`                |
| `CTRL-L`           | Clear Screen                              | `input:clear_screen`                       |
| `CTRL-N`           | Move Cursor Down                          | `editor_view:down`                         |
| `CTRL-P`           | Move Cursor Up                            | `editor_view:up`                           |
|                    | Select to Start of Line                   | `editor_view:select_to_line_start`         |
| `CTRL-SHIFT-B`     | Select One Character to the Left          | `editor_view:select_left`                  |
| `CTRL-SHIFT-DOWN`  | Add Cursor Below                          | `editor_view:add_cursor_below`             |
|                    | Select to End of Line                     | `editor:select_to_line_end`                |
| `CTRL-Z`           | Undo                                      | `editor:undo`                              |
| `CTRL-SHIFT-Z`     | Redo                                      | `editor:redo`                              |
| `CTRL-SHIFT-F`     | Select One Character to the Right         | `editor:select_right`                      |
|                    | Select Down                               | `editor_view:select_down`                  |
| `CTRL-SHIFT-P`     | Select Up                                 | `editor_view:select_up`                    |
| `CTRL-SHIFT-UP`    | Add Cursor Above                          | `editor_view:add_cursor_above`             |
| `CTRL-U`           | Copy and Clear Selected Lines             | `editor_view:clear_and_copy_lines`         |
| `CTRL-W`           | Cut Word Left                             | `editor_view:cut_word_left`                |
| `META-.`           | Insert Last Word of Previous Command      | `editor:insert_last_word_previous_command` |
| `META-A`           | Move to the Start of the Paragraph        | `editor_view:move_to_paragraph_start`      |
| `CTRL-LEFT`        | Move Backward One Word                    | `editor_view:move_backward_one_word`       |
| `ALT-D`            | Cut Word Right                            | `editor_view:cut_word_right`               |
| `META-E`           | Move to the End of the Paragraph          | `editor_view:move_to_paragraph_end`        |
| `CTRL-RIGHT`       | Move Forward One Word                     | `editor_view:move_forward_one_word`        |
| `CTRL-ALT-LEFT`    | Move Backward One Subword                 | `editor_view:move_backward_one_subword`    |
| `CTRL-ALT-RIGHT`   | Move Forward One Subword                  | `editor_view:move_forward_one_subword`     |
| `SHIFT-META-<`     | Move to the Start of the Buffer           | `editor_view:move_to_buffer_start`         |
| `SHIFT-META->`     | Move to the End of the Buffer             | `editor_view:move_to_buffer_end`           |
| `CTRL-SHIFT-LEFT`  | Select One Word to the Left               | `editor_view:select_left_by_word`          |
| `CTRL-SHIFT-RIGHT` | Select One Word to the Right              | `editor_view:select_right_by_word`         |

**Terminal**

| Shortcut           | Command                                           | Action                                       |
| ------------------ | ------------------------------------------------- | -------------------------------------------- |
| `CTRL-ALT-DOWN`    | Switch Panes Down                                 | `pane_group:navigate_down`                   |
| `CTRL-ALT-LEFT`    | Switch Panes Left                                 | `pane_group:navigate_left`                   |
| `CTRL-ALT-RIGHT`   | Switch Panes Right                                | `pane_group:navigate_right`                  |
| `CTRL-ALT-UP`      | Switch Panes Up                                   | `pane_group:navigate_up`                     |
| `CTRL-ALT-V`       | \[a11y] Set Concise Accessibility Announcements   | `workspace:set_a11y_concise_verbosity_level` |
| `CTRL-ALT-V`       | \[a11y] Set Verbose Accessibility Announcements   | `workspace:set_a11y_verbose_verbosity_level` |
| `CTRL-,`           | Open Settings                                     | `workspace:show_settings_modal`              |
| `CTRL-,`           | Open Settings: Account                            | `workspace:show_settings_account_page`       |
| `F3`               | Find the Next Occurrence of Your Search Query     | `find:find_next_occurrence`                  |
| `CTRL-SHIFT-P`     | Toggle Command Palette                            | `workspace:toggle_command_palette`           |
|                    | Toggle Mouse Reporting                            | `workspace:toggle_mouse_reporting`           |
| `CTRL-SHIFT-[`     | Activate Previous Pane                            | `pane_group:navigate_prev`                   |
| `CTRL-SHIFT-]`     | Activate Next Pane                                | `pane_group:navigate_next`                   |
|                    | Resize Pane > Move Divider Down                   | `pane_group:resize_down`                     |
| `CTRL-CMD-K`       | Open Keybindings Editor                           | `workspace:show_keybinding_settings`         |
|                    | Resize Pane > Move Divider Left                   | `pane_group:resize_left`                     |
|                    | Resize Pane > Move Divider Right                  | `pane_group:resize_right`                    |
|                    | Resize Pane > Move Divider Up                     | `pane_group:resize_up`                       |
| `CTRL-SHIFT-/`     | Open Resource Center                              | `workspace:toggle_resource_center`           |
| `CTRL-SHIFT-E`     | Split Pane Down                                   | `pane_group:add_down`                        |
| `CTRL-SHIFT-ENTER` | Toggle Maximize Active Pane                       | `pane_group:toggle_maximize_pane`            |
| `SHIFT-F3`         | Find the Previous Occurrence of Your Search Query | `find:find_prev_occurrence`                  |
|                    | Toggle Navigation Palette                         | `workspace:toggle_navigation_palette`        |

**Fundamentals**

| Shortcut           | Command                    | Action                           |
| ------------------ | -------------------------- | -------------------------------- |
| `CTRL--`           | Decrease Font Size         | `workspace:decrease_font_size`   |
| `CTRL-0`           | Reset Font Size to Default | `workspace:reset_font_size`      |
| `CTRL-1`           | Switch to 1st Tab          | `workspace:activate_first_tab`   |
| `CTRL-2`           | Switch to 2nd Tab          | `workspace:activate_second_tab`  |
| `CTRL-3`           | Switch to 3rd Tab          | `workspace:activate_third_tab`   |
| `CTRL-4`           | Switch to 4th Tab          | `workspace:activate_fourth_tab`  |
| `CTRL-5`           | Switch to 5th Tab          | `workspace:activate_fifth_tab`   |
| `CTRL-6`           | Switch to 6th Tab          | `workspace:activate_sixth_tab`   |
| `CTRL-7`           | Switch to 7th Tab          | `workspace:activate_seventh_tab` |
| `CTRL-8`           | Switch to 8th Tab          | `workspace:activate_eighth_tab`  |
| `CTRL-9`           | Switch to Last Tab         | `workspace:activate_last_tab`    |
| `CTRL-=`           | Increase Font Size         | `workspace:increase_font_size`   |
| `CTRL-SHIFT-C`     | Copy                       | `terminal:copy`                  |
| `CTRL-SHIFT-F`     | Find                       | `terminal:find`                  |
| `CTRL-SHIFT-V`     | Paste                      | `terminal:paste`                 |
| `CTRL-SHIFT-T`     | Open New Tab               | `workspace:open_new_tab`         |
| `CTRL-ALT-T`       | Reopen Closed Tab          | `workspace:reopen_closed_tab`    |
| `CTRL-SHIFT-LEFT`  | Move Tab Left              | `workspace:move_tab_left`        |
| `CTRL-SHIFT-RIGHT` | Move Tab Right             | `workspace:move_tab_right`       |
| `CTRL-PAGEUP`      | Activate Previous Tab      | `workspace:activate_prev_tab`    |
| `CTRL-PAGEDOWN`    | Activate Next Tab          | `workspace:activate_next_tab`    |
| {% endtab %}       |                            |                                  |

{% tab title="Linux" %}
**Warp Essentials**

| Shortcut       | Command                      | Action                                         |
| -------------- | ---------------------------- | ---------------------------------------------- |
| `CTRL-SHIFT-D` | Split Pane Right             | `pane_group:add_right`                         |
|                | Launch Configuration Palette | `workspace:toggle_launch_config_palette`       |
|                | Open Theme Picker            | `workspace:show_theme_chooser`                 |
| `CTRL-R`       | Command Search               | `workspace:show_command_search`                |
| `CTRL-SHIFT-R` | Workflows                    | `input:toggle_workflows`                       |
| `` CTRL-` ``   | Generate                     | `input:toggle_natural_language_command_search` |
| `CTRL-SHIFT-L` | Focus Terminal Input         | `terminal:focus_input`                         |
| `CTRL-I`       | Warpify Subshell             | `terminal:trigger_subshell_bootstrap`          |
| `CTRL-SHIFT-\` | Warp Drive                   | `terminal:toggle_warp_drive`                   |

**Blocks**

| Shortcut           | Command                           | Action                                                 |
| ------------------ | --------------------------------- | ------------------------------------------------------ |
| `ALT-DOWN`         | Select the Closest Bookmark Down  | `terminal:select_bookmark_down`                        |
| `CTRL-SHIFT-ALT-C` | Copy Command Output               | `terminal:copy_outputs`                                |
| `ALT-UP`           | Select the Closest Bookmark Up    | `terminal:select_bookmark_up`                          |
| `CTRL-SHIFT-A`     | Select All Blocks                 | `terminal:select_all_blocks`                           |
| `CTRL-SHIFT-K`     | Clear Blocks                      | `terminal:clear_blocks`                                |
| `CTRL-SHIFT-B`     | Bookmark Selected Block           | `terminal:bookmark_selected_block`                     |
| `CTRL-DOWN`        | Select Next Block                 | `terminal:select_next_block`                           |
| `CTRL-SHIFT-I`     | Reinput Selected Commands         | `terminal:reinput_commands`                            |
| `CTRL-UP`          | Select Previous Block             | `terminal:select_previous_block`                       |
|                    | Open Block Context Menu           | `terminal:open_block_list_context_menu_via_keybinding` |
| `CTRL-SHIFT-C`     | Copy Command                      | `terminal:copy_commands`                               |
|                    | Reinput Selected Commands as Root | `terminal:reinput_commands_with_sudo`                  |
| `CTRL-SHIFT-S`     | Share Selected Block              | `terminal:open_share_modal`                            |
| `SHIFT-DOWN`       | Expand Selected Blocks Below      | `terminal:expand_block_selection_below`                |
| `SHIFT-UP`         | Expand Selected Blocks Above      | `terminal:expand_block_selection_above`                |

**Input Editor**

| Shortcut           | Command                                   | Action                                     |
| ------------------ | ----------------------------------------- | ------------------------------------------ |
| `CTRL-BACKSPACE`   | Delete Word Left                          | `editor:delete_word_left`                  |
| `CTRL-ALT-F`       | Fold Selected Ranges                      | `editor_view:fold_selected_ranges`         |
| `CTRL-ALT-[`       | Fold                                      | `editor_view:fold`                         |
| `CTRL-ALT-]`       | Unfold                                    | `editor_view:unfold`                       |
| `CTRL-DELETE`      | Delete Word Right                         | `editor:delete_word_right`                 |
| `CTRL-A`           | Select All                                | `editor_view:select_all`                   |
| `CTRL-Y`           | Delete All Left                           | `editor_view:delete_all_left`              |
|                    | Delete All Right                          | `editor_view:delete_all_right`             |
| `CTRL-END`         | Move Cursor to the Bottom                 | `editor_view:cmd_down`                     |
| `CTRL-I`           | Inspect Command                           | `editor_view:cmd_i`                        |
| `HOME`             | Home                                      | `editor_view:home`                         |
| `END`              | End                                       | `editor_view:end`                          |
| `CTRL-A`           | Move to Start of Line                     | `editor_view:move_to_line_start`           |
| `CTRL-B`           | Move Cursor Left                          | `editor_view:left`                         |
| `CTRL-C`           | Clear Command Editor                      | `editor_view:clear_buffer`                 |
| `CTRL-D`           | Delete                                    | `editor_view:delete`                       |
| `CTRL-E`           | Move to End of Line                       | `editor_view:move_to_line_end`             |
| `CTRL-F`           | Move Cursor Right / Accept Autosuggestion | `editor_view:right`                        |
| `CTRL-G`           | Add Selection for Next Occurrence         | `editor_view:add_next_occurrence`          |
| `CTRL-H`           | Remove the Previous Character             | `editor_view:backspace`                    |
| `CTRL-J`           | Insert Newline                            | `editor_view:insert_newline`               |
| `CTRL-K`           | Cut All Right                             | `editor_view:cut_all_right`                |
| `CTRL-L`           | Clear Screen                              | `input:clear_screen`                       |
| `CTRL-N`           | Move Cursor Down                          | `editor_view:down`                         |
| `CTRL-P`           | Move Cursor Up                            | `editor_view:up`                           |
|                    | Select to Start of Line                   | `editor_view:select_to_line_start`         |
| `CTRL-SHIFT-B`     | Select One Character to the Left          | `editor_view:select_left`                  |
| `CTRL-SHIFT-DOWN`  | Add Cursor Below                          | `editor_view:add_cursor_below`             |
|                    | Select to End of Line                     | `editor:select_to_line_end`                |
| `CTRL-Z`           | Undo                                      | `editor:undo`                              |
| `CTRL-SHIFT-Z`     | Redo                                      | `editor:redo`                              |
| `CTRL-SHIFT-F`     | Select One Character to the Right         | `editor:select_right`                      |
|                    | Select Down                               | `editor_view:select_down`                  |
| `CTRL-SHIFT-P`     | Select Up                                 | `editor_view:select_up`                    |
| `CTRL-SHIFT-UP`    | Add Cursor Above                          | `editor_view:add_cursor_above`             |
| `CTRL-U`           | Copy and Clear Selected Lines             | `editor_view:clear_and_copy_lines`         |
| `CTRL-W`           | Cut Word Left                             | `editor_view:cut_word_left`                |
| `META-.`           | Insert Last Word of Previous Command      | `editor:insert_last_word_previous_command` |
| `META-A`           | Move to the Start of the Paragraph        | `editor_view:move_to_paragraph_start`      |
| `CTRL-LEFT`        | Move Backward One Word                    | `editor_view:move_backward_one_word`       |
| `ALT-D`            | Cut Word Right                            | `editor_view:cut_word_right`               |
| `META-E`           | Move to the End of the Paragraph          | `editor_view:move_to_paragraph_end`        |
| `CTRL-RIGHT`       | Move Forward One Word                     | `editor_view:move_forward_one_word`        |
| `CTRL-ALT-LEFT`    | Move Backward One Subword                 | `editor_view:move_backward_one_subword`    |
| `CTRL-ALT-RIGHT`   | Move Forward One Subword                  | `editor_view:move_forward_one_subword`     |
| `SHIFT-META-<`     | Move to the Start of the Buffer           | `editor_view:move_to_buffer_start`         |
| `SHIFT-META->`     | Move to the End of the Buffer             | `editor_view:move_to_buffer_end`           |
| `CTRL-SHIFT-LEFT`  | Select One Word to the Left               | `editor_view:select_left_by_word`          |
| `CTRL-SHIFT-RIGHT` | Select One Word to the Right              | `editor_view:select_right_by_word`         |

**Terminal**

| Shortcut           | Command                                           | Action                                       |
| ------------------ | ------------------------------------------------- | -------------------------------------------- |
| `CTRL-ALT-DOWN`    | Switch Panes Down                                 | `pane_group:navigate_down`                   |
| `CTRL-ALT-LEFT`    | Switch Panes Left                                 | `pane_group:navigate_left`                   |
| `CTRL-ALT-RIGHT`   | Switch Panes Right                                | `pane_group:navigate_right`                  |
| `CTRL-ALT-UP`      | Switch Panes Up                                   | `pane_group:navigate_up`                     |
| `CTRL-ALT-V`       | \[a11y] Set Concise Accessibility Announcements   | `workspace:set_a11y_concise_verbosity_level` |
| `CTRL-ALT-V`       | \[a11y] Set Verbose Accessibility Announcements   | `workspace:set_a11y_verbose_verbosity_level` |
| `CTRL-,`           | Open Settings                                     | `workspace:show_settings_modal`              |
| `CTRL-,`           | Open Settings: Account                            | `workspace:show_settings_account_page`       |
| `F3`               | Find the Next Occurrence of Your Search Query     | `find:find_next_occurrence`                  |
| `CTRL-SHIFT-P`     | Toggle Command Palette                            | `workspace:toggle_command_palette`           |
|                    | Toggle Mouse Reporting                            | `workspace:toggle_mouse_reporting`           |
| `CTRL-SHIFT-[`     | Activate Previous Pane                            | `pane_group:navigate_prev`                   |
| `CTRL-SHIFT-]`     | Activate Next Pane                                | `pane_group:navigate_next`                   |
|                    | Resize Pane > Move Divider Down                   | `pane_group:resize_down`                     |
| `CTRL-CMD-K`       | Open Keybindings Editor                           | `workspace:show_keybinding_settings`         |
|                    | Resize Pane > Move Divider Left                   | `pane_group:resize_left`                     |
|                    | Resize Pane > Move Divider Right                  | `pane_group:resize_right`                    |
|                    | Resize Pane > Move Divider Up                     | `pane_group:resize_up`                       |
| `CTRL-SHIFT-/`     | Open Resource Center                              | `workspace:toggle_resource_center`           |
| `CTRL-SHIFT-E`     | Split Pane Down                                   | `pane_group:add_down`                        |
| `CTRL-SHIFT-ENTER` | Toggle Maximize Active Pane                       | `pane_group:toggle_maximize_pane`            |
| `SHIFT-F3`         | Find the Previous Occurrence of Your Search Query | `find:find_prev_occurrence`                  |
|                    | Toggle Navigation Palette                         | `workspace:toggle_navigation_palette`        |

**Fundamentals**

| Shortcut           | Command                    | Action                           |
| ------------------ | -------------------------- | -------------------------------- |
| `CTRL--`           | Decrease Font Size         | `workspace:decrease_font_size`   |
| `CTRL-0`           | Reset Font Size to Default | `workspace:reset_font_size`      |
| `CTRL-1`           | Switch to 1st Tab          | `workspace:activate_first_tab`   |
| `CTRL-2`           | Switch to 2nd Tab          | `workspace:activate_second_tab`  |
| `CTRL-3`           | Switch to 3rd Tab          | `workspace:activate_third_tab`   |
| `CTRL-4`           | Switch to 4th Tab          | `workspace:activate_fourth_tab`  |
| `CTRL-5`           | Switch to 5th Tab          | `workspace:activate_fifth_tab`   |
| `CTRL-6`           | Switch to 6th Tab          | `workspace:activate_sixth_tab`   |
| `CTRL-7`           | Switch to 7th Tab          | `workspace:activate_seventh_tab` |
| `CTRL-8`           | Switch to 8th Tab          | `workspace:activate_eighth_tab`  |
| `CTRL-9`           | Switch to Last Tab         | `workspace:activate_last_tab`    |
| `CTRL-=`           | Increase Font Size         | `workspace:increase_font_size`   |
| `CTRL-SHIFT-C`     | Copy                       | `terminal:copy`                  |
| `CTRL-SHIFT-F`     | Find                       | `terminal:find`                  |
| `CTRL-SHIFT-V`     | Paste                      | `terminal:paste`                 |
| `CTRL-SHIFT-T`     | Open New Tab               | `workspace:open_new_tab`         |
| `CTRL-ALT-T`       | Reopen Closed Tab          | `workspace:reopen_closed_tab`    |
| `CTRL-SHIFT-LEFT`  | Move Tab Left              | `workspace:move_tab_left`        |
| `CTRL-SHIFT-RIGHT` | Move Tab Right             | `workspace:move_tab_right`       |
| `CTRL-PAGEUP`      | Activate Previous Tab      | `workspace:activate_prev_tab`    |
| `CTRL-PAGEDOWN`    | Activate Next Tab          | `workspace:activate_next_tab`    |
| {% endtab %}       |                            |                                  |
| {% endtabs %}      |                            |                                  |


# Changelog

Warp auto-updates whenever a new release comes out. We try to ship an update every week usually on Thursday!

Submit bugs and feature requests on our [GitHub board!](https://github.com/warpdotdev/Warp/issues/new/choose)

## 2025.11.19 (v0.2025.11.19.08.12)

**New features**

* MCP server configurations can now be shared with others on your team. You can install a server shared by your team with minimal configuration.
* Warp now provides out-of-box MCP servers for common services like Github and Linear that can be installed and run with a single click.
* Find now works in the code review pane.

## 2025.11.18 (v0.2025.11.18.12.24)

**New features**

* [Full Terminal Use](https://docs.warp.dev/documentation/agents/full-terminal-use): Let the agent use the terminal as you would: interact with REPLs, debuggers, and full-screen apps like `top`. Warp is the only product on the market with Full Terminal Use capabilities.
* [`/plan`](https://docs.warp.dev/documentation/agents/using-agents/planning): do spec-driven development in Warp. Work with an agent to align on an implementation plan that can be saved, versioned, and even attached to a PR for teammates.
* [Interactive Code Review](https://docs.warp.dev/documentation/code/code-review/interactive-code-review): Review an agent's code like you would a teammate's, directly in Warp, and ask the agent to address the comments.
* [Slack and Linear integrations](https://docs.warp.dev/documentation/integrations/integrations-overview/integrations-and-environments):\*\* Ask the agent to get to work from the tools you already use, track their progress, and take the wheel via live session sharing.
* Warp's Agents can now [search the web](https://docs.warp.dev/documentation/agents/using-agents/web-search) to retrieve information, when relevant. This capability is configurable via Agent Profiles.

## 2025.11.12 (v0.2025.11.12.08.12)

**Improvements**

* \[Vim mode] Paragraph text objects are now supported, e.g. `dip` to delete a paragraph.
* \[Vim mode] In terminal mode, press `K` over part of a command to inspect it.
* Agent notifications now reference conversations' titles instead of their queries.

**Bug Fixes**

* The copy link button now works as expected after shared sessions have been closed.

## 2025.11.05 (v0.2025.11.05.08.12)

**New Features**

* From the code review panel, add file diffs or the entire diff set as context to an agent conversation.

**Improvements**

* Warp now defaults to requiring approval before the agent will execute a command.
* Shared session links will open in a new tab by default, rather than a new window.
* Display summarization tokens when conversation summarization is triggered.

### 2025.10.29 (v0.2025.10.29.08.12)

**Improvements**

* Display conversation summaries when summarization is triggered.
* Added completions for the Warp CLI.
* Updated community links from Discord to Slack throughout the app.

**Bug Fixes**

* Reduce padding on restored Agent Mode blocks and expanded shell commands.
* Add support for delete key in vim mode in code editors.
* Fix rendering for multi-line Agent Mode shell commands.

### 2025.10.22 (v0.2025.10.22.08.13)

**New Features**

* Warp will suggest new unit tests in addition to code fixes via Suggested Code Banners

**Improvements**

* Fixed an issue where the model specs menu would get cut off.

**Bug Fixes**

* Fixed the close icon from becoming too small on the Warp Drive notebook viewer.
* Fixed an issue where the CLI would report invalid debug IDs in its troubleshooting output.

### 2025.10.15 (v0.2025.10.15.08.12)

**New Features**

* Warp now supports scaling the entire application. Change the zoom level in `Settings > Appearance > Window` or by pressing `CMD-+` on Mac or `CTRL-+` on Windows / Linux.

**Improvements**

* The code review pane can now show diffs against other base branches.
* Added confirmation dialog when cancelling AI summarization requests.
* You can now expand Suggested Code Diffs further on down arrow.
* Restore closed panes using `CMD-SHIFT-T` or `CTRL-ALT-T` on Windows / Linux within 60 seconds of them being closed.
* Added shell completions for the Warp CLI.
* Warp Drive Environment Variables are now supported for Warp for Windows (PowerShell, Git Bash, and WSL).
* Enriched the model picker to include detailed specs of each model's intelligence, speed and cost.

**Bug Fixes**

* Fixed the custom window size setting not reliably applying on startup.

### 2025.10.08 (v0.2025.10.08.08.12)

**Improvements**

* Added the ability to sort team members by usage in `Settings > Billing and usage`.
* Added UI indication of when agent mode conversation summarization is in progress, with a cancellation confirmation dialog.
* Made the sizing for headings consistent across all collapsible blocks.
* `@` menu no longer appears when running JS package manager subcommands, like `yarn workspace @org/package add`.
* \[macOS] Resolved an issue re-mapping keybindings that conflict with MacOS keybindings.

**Bug Fixes**

* Agent mode requested command previews now only show the first line of multi-line commands.
* Removed misleading "auto-approve" button while Warp is generating a fix for failed terminal commands.

### 2025.10.01 (v0.2025.10.01.08.12)

**Improvements**

* Editing suggested file changes now takes place in the same pane, instead of a new tab.
* When using the `@` context menu outside of a repo, current folder's contents are now listed.
* The code mode file picker will now display gitignored files.
* \[macOS] Warp now stores session restoration data in a more-secure application container.

### 2025.09.24 (v0.2025.09.24.08.11)

**New features**

* You can now create new files directly in Warp. Search "New File" in the command palette. MacOS users can find it in the app menu under "File".

**Improvements**

* Change the "Reject" label to "Refine" for code diffs and plans. They're functionally the same, though we think this will clear up some confusion over what hitting "Reject" will do.
* Added realtime form validation to Environment Variables when secret redaction is enabled.
* Avoid showing the `@` context completions menu when typing a package name. This covers common installers for JS, Python, Ruby, Go, PHP, and more.
* Add an "auto-approve" option with a keyboard shortcut for requested commands and MCP tool calls. This makes it easier to accept a command and auto-approve future commands in a single button.

**Bug fixes**

* Fixed error with fish shell v4.
* Avoid showing multiple "stopped task" banners when toggling a resumed conversation back to stopped before the agent begins responding.
* Fix input problems with Russian on PowerShell.

### 2025.09.17 (v0.2025.09.17.08.11)

**New Features**

* Warp agents are now available via the command line! [Learn more](https://docs.warp.dev/developers/cli)
* Added support for custom Regex names in Enterprise Secret Redaction.

**Improvements**

* The @ context menu can now be activated outside of Git repositories (for actions such as attaching blocks/workflows), when in autodetection or AI input mode.
* move the auto-approve button alongside the agent "stop" button for easier access.
* Move the "stop" button alongside the "Warping..." indicator. This restores the "stop" button to classic input users, and offers a more intuitive experience for universal input users.
* Added right-click context menu to code review pane with split pane controls.
* Files selected in the file tree now open in a preview mode until interacted with.
* Warp's agent now shows reasoning traces from reasoning models.
* Ctrl-c during a long running command run by the agent will also stop the agent, not just the command.

**Bug Fixes**

* Fixed nested lists in agent markdown output sometimes not rendering properly.
* Fix slow scrolling on macOS Tahoe.
* Fix todo lists overflowing off of the screen for 10 or more items.
* Fix code review maximize button appearing outside of split pane mode.
* Fix the stop button unexpectedly disappearing when accepting the "start a new conversation" suggestion.

### 2025.09.10 (v0.2025.09.10.08.11)

**Improvements**

* Added support for ignoring input suggestions. Click the X next to an item in your up-arrow history menu to hide that from showing up again. You can also enable the `Show autosuggestion ignore button` setting to add an X to autosuggestions directly in your input.
* Git UI detects more changes in git worktrees.
* You can now rename/delete items in the file picker and open them with the system file explorer.
* Combine "refine" and "cancel" buttons into a single "reject" button. This lets you give feedback on code diffs, commands, and plans with a single button.
* You can now switch node versions by clicking on the node version chip.
* Added a "New Agent" button to the agent management panel to start a new agent conversation more easily."

**Bug fixes**

* Fixed an issue where agent output in a code block could be inserted at the wrong place.
* Fixed code review diff buttons incorrectly receiving mouse events.
* Avoid auto-expanding an agent's requested commands while you are using voice dictation.
* Add back the auto-approve button for classic input mode.
* Fixed keyboard navigation of chip menus in the input while an agent is running.
* Properly reset context when user sends query to agent.

### 2025.09.03 (v0.2025.09.03.08.11)

**Improvements**

* Added support for rendering H4-H6 in markdown.

### 2025.09.01 (v0.2025.09.01.20.54)

**New features**

* Revert diff hunks directly from the Code Review Pane.
* Add lines of a file to the context of a conversation from the Warp code editor.
* You can now search and restore Agent conversations in your history using the `conversations:` prefix.
* You can now search and navigate to indexed code bases using the `repos:` prefix.

**Improvements**

* Voice transcriptions are no longer cut off when unfocusing an input editor.
* You can now select the $EDITOR environment variable as the default application for opening file links.
* Added new header treatment for unfocused Warp windows.
* \[Mac] A new dock icon option to celebrate Code Country - the Cow icon! (`Appearance > Icon` to change)
* Pasting images in the terminal input switches to Agent mode and attaches the image as context.
* Added support for the Streamable HTTP transport for MCP servers.

**Bug fixes**

* \[Windows/Linux] Fixed keybinding conflict for split pane down action for the Input, when a code diff is not active.
* Fixed tab tooltips displaying unwanted leading and trailing whitespace.
* Pressing the up key while the model picker is open no longer opens the command history. Opening the model picker while the command history is open now closes the command history.

### 2025.08.27 (v0.2025.08.27.08.11)

**New Features**

* [Agent Profiles](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions#agent-profiles): define how your agent operates.
* New pane to view changes to a git repository.
* Files now open in a tabbed viewer.
* Syntax highlighting for Scala files in Warp.

**Bug Fixes**

* Fix paths not inserted when pasted images are not attached.

### 2025.08.20 (v0.2025.08.20.08.11)

**New features**

* [Suggested Code Diffs](https://docs.warp.dev/documentation/agents/active-ai#suggested-code-diffs) - Warp now intelligently suggests the appropriate fixes for any simple errors encountered in the command line e.g. compiler errors. Head to `Settings > Active AI` to toggle this feature.

**Improvements**

* Added setting to hide fixed prompt suggestions.
* Updated default input type from 'Classic' to 'Universal'.
* Improve the styling and usability of tabs for narrow windows.

**Bug fixes**

* Fix failures to start zsh sessions when using prezto.
* The agent status indicator no longer disappears while a command is running.
* Selecting a workflow will correctly close the workflows menu.
* Don't auto-attach image if file pasted as plaintext.
* Fixed issue with drag-drop images.
* Fixed display of completions that may have included special characters.

### 2025.08.13 (v0.2025.08.13.08.12)

**New Features**

* Agent Mode now displays interactive code blocks when referencing snippets from your codebase. You can easily copy the snippet, add the snippet as Agent Mode context, or open the file in Warp's built-in editor.
* Agent Mode now creates and tracks task lists for more complex workflows. See [Agent Task Lists](https://docs.warp.dev/documentation/agents/using-agents/agent-tasklists).
* Added support for defining project-scoped rules with a WARP.md file. See [Rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules#project-scoped-rules).
* Added Slash Commands (/) in Agent Mode or Auto-Detection Mode to quickly run built-in actions or saved prompts without leaving the input field. See [Slash Commands](https://docs.warp.dev/documentation/agents/slash-commands).

**Improvements**

* Added syntax highlighting for SQL in Warp's code editor.
* Added button to dismiss suggestions footer.
* \[Linux and Windows] Added support for drag-dropping multiple images.
* New files in Warp open in a pane by default. You can customize this behavior via `Settings > Features > General > Choose a layout to open files in Warp`, where you can switch between opening files in a pane or a new tab.
* Input stays in Agent Mode after an image is attached, instead of switching to shell mode.

**Bug Fixes**

* Fixed behavior when clicking Agents chip in Classic input mode.
* Repository-scoped Warp features are now available in git worktrees.
* Fixed drag-drop of images for long-running commands (eg Claude Code, vim).
* \[Linux and Windows] Fixed attaching images from pasted files.
* Fixed "Find in selected block" feature after clicking on an active running block.
* Fixed text overlap on narrow panes with Classic Warp Prompt with Same Line Prompt.
* \[macOS] Fixed a bug that would cause text to disappear for very long Agent Mode prompts.

### 2025.08.06 (v0.2025.08.06.08.12)

**New Features**

* GPT-5 is now available to all users. Use the model selector in the input bar to try it yourself.
* \[MacOS] Added the ability to attach images as context by drag-and-dropping them or pasting from your clipboard.

**Improvements**

* You can now open any files within Warp's editor (including txt/csv files)!
* Warp can now edit Bazel files.
* Warp can now edit `.bashrc` and `.zshrc` files.
* Added `Always show secrets` to Secret Redaction for a less obtrusive secret redaction mode.
* Added reset time to the Billing and usage menu.

**Bug Fixes**

* Fix fish version <= 3.7 when vi keybindings were activated.
* Fixed bug affecting the "Open in Markdown Viewer by default" setting, you can use this setting to determine whether you'd like to view/edit MD files in Warp by default.
* Fixed an issue where typeahead for the next command could be lost if you typed really quickly after hitting enter on the previous command.
* Resolved an issue where stopping voice recording via the button would interrupt transcription.

### 2025.07.30 (v0.2025.07.30.08.12)

**New Features**

* You can now set a configurable block size limit for higher scrollback limits! Head to `Settings > Features > Session > Maximum rows in a block` to configure.
* \[Linux] Added support for pasting images as context.

**Improvements**

* The "Open in Warp" banner now supports code files.
* When using Agent Mode, user-configured redaction rules are now applied to the contents of diffs and files, in addition to terminal blocks.
* Add SHIFT-ENTER keybinding. Claude Code users can use this to add linefeeds to their prompt.
* Added an overflow menu button in the top right of AI blocks for copying contents.

**Bug Fixes**

* Deleted files no longer appear in the @-context selection box.
* Users with Turkish locale will no longer see an extra letter "i" between commands.
* \[Windows] Restored windows will no longer be positioned with the title bar above the top of the display.

### 2025.07.23 (v0.2025.07.23.08.12)

**New Features**

* \[Windows] Added support for pasting images from Clipboard into Agent Mode context.

**Improvements**

* Added image filename when pasting images into Agent Mode context.
* Added support for restarting MCP servers when Warp restarts.
* Added support for copying AI block and conversation contents via the context menu.
* Added Node.js prompt chip.

**Bug Fixes**

* Fixed a bug where attaching a block as AI context would reset the input state.
* Fixed a spacing issue with horizontal scrollbars in agent planning view.
* Added support for auto-expanding manually executed Agent Mode suggested commands.
* Fixed a bug where Warp would hang while updating code symbols in the @-context menu.
* Modified secret redaction regexes to be case sensitive. Use a `(?i)` prefix to make your regex case insensitive.
* Modified the Universal Input to no longer exit a conversation via "backspace".

### 2025.07.16 (v0.2025.07.16.08.12)

**New Features**

* \[macOS] Support pasting images from clipboard into Agent Mode context.
* Migrated Warp's built-in set of Secret Redaction regexes into user's regexes, giving users more fine-grained control over their secret redaction.
* Added support for Find and Replace using `CMD-F` when viewing diffs or editing files in the built-in code editor.

**Improvements**

* Removed lock icon from Secret Redaction in favor of asterisks when ligatures are enabled.
* Added individual keybinding shortcuts to change input modes.

**Bug Fixes**

* Fixed an issue where the hover tooltip for disabled prompt suggestions either didn't render at all or was incredibly hard to read.
* Fixed the background color of inline code in restored AI blocks.

### 2025.07.09 (v0.2025.07.09.08.11)

**New Features**

* New secret redaction strikethrough UI. Comes with new `Settings > Privacy > Hide secrets in block list` setting that defaults to off.

**Improvements**

* You can now resume stopped AI conversations: `CTRL-C` to stop and `CMD-SHIFT-R` to resume on macOS or `CTRL-SHIFT-R` on Windows and Linux.
* Code Diff view's default Edit and Revise keybindings changed and made configurable.
* Added syntax highlighting for PowerShell, Kotlin and Swift.

**Bug Fixes**

* Fixed an issue with `.inc` file chunking.
* Clicking on an active, long running block will no longer select the block, but focus the input.

### 2025.07.02 (v0.2025.07.02.08.36)

**New features**

* Tab close button can now be set to the left.

**Improvements**

* Added syntax highlighting for TOML, PHP, Lua, Ruby, and Groovy (with Java syntax).
* Added conda chip support to new Universal Input prompt.
* Increased color contrast on tabs.
* Added "Upgrade" menu item for free users and "Billing and Usage" menu item for paid users in the user menu for easier access to subscription management.

**Bug fixes**

* When AI is disabled, ESC should no longer enter Agent Mode.
* Fixed an issue on WSL where files created by Agent Mode would have CRLF line endings.
* \[Mac] Tweaked autoupdate logic to more reliably remove old applications off disk.
* Fixed "Manage plan suggestion setting" link.

### 2025.06.25 (v0.2025.06.25.08.12)

**New Features**

* Git branch and directory chip now are searchable.

**Improvements**

* Added support for HCL syntax highlighting in Terraform files.

**Bug Fixes**

* Fixed potential crash when displaying context chips with Unicode characters in file paths.
* Fixed a rendering issue with line numbers in suggested diffs.
* Attach context chip no longer appears if there is no context you can attach.

### 2025.06.20 (v0.2025.06.20.22.47)

**New Features**\
\
**Warp 2.0 is here - The Agentic Development Environment**

Built from the ground up for agentic workflows, Warp is the most powerful tool for prompting, coding, and collaborating with multiple agents.

**Multithread yourself with agents**

* Launch intelligent tasks (agents) with a prompt. Agents gather context using CLI commands, MCP, Warp Drive, and Codebase Context.
* New Agent Management Panel to monitor, multitask, and intervene across multiple agents.
* Set autonomy controls and get notified when agents need your help.

**A state-of-the-art coding platform**

* 70% on SWE-bench, #1 on Terminal-Bench — the highest quality coding agent available.
* Codebase Context: Warp indexes and understands your codebase, allowing you to debug and write code faster without storing any code on Warp's servers.
* Review and edit diffs directly in Warp's native code editor.

**Still a great command-line**\n-

* A new Universal Input: run commands or prompt agents from a single interface. Lock into command- or agent-mode, or let Warp detect automatically.
* Choose your model, continue a conversation, attach images, link URLs, or reference files using `@`.
* Modern, IDE-like terminal experience with completions, predictions, and mouse support, all built natively in Rust for performance.

**Context for your teammates and agents**

* A knowledge store where you can configure MCP, define Rules, and store shared commands, notebooks, env vars, and prompts as context.

All of this comes with higher AI usage limits on our Pro and Turbo plans, plus new pay-as-you-go overages for continued access to premium models.\
\
**Watch the full Warp 2.0 launch event →** [**warp.dev/future**](https://warp.dev/future)

### 2025.06.11 (v0.2025.06.11.08.11)

**New Features**

* You can now attach images as context for Agent Mode! Simply use the image icon and select the files you wish to attach.

**Improvements**

* \[Linux] Added support for standard installed Zed and Zed Preview as default code editors.
* \[macOS] Added support for Zed Preview as a default code editor.
* Added syntax highlighting support for TSX and JSX.
* Increased visibility of non-focused diff hunks when navigating diffs.
* New Agent Mode output will no longer force-scroll.

**Bug Fixes**

* Fixed keybinding being missing for editing requested commands.
* Removed keybindings for zero-state prompt suggestions, to avoid conflicting with tab switching keybindings.

### 2025.06.04 (v0.2025.06.04.08.11)

**New Features**

* Sonnet 4 is now an available model (enabled by default in the "auto" model).

**Improvements**

* Press the hovering fast-forward button to auto-execute all Agent actions until the task completes.
* Added ability to share session via `RIGHT-CLICK` on tab.
* You can now give the Agent permission to auto-execute MCP tool calls.

**Bug Fixes**

* Fixed an issue where Agent Mode would sometimes not find untracked files in git repos.
* Fixed Agent Mode file editor randomly scrolling to the first line of a file.

### 2025.05.28 (v0.2025.05.28.08.11)

**New Features**

* Added MCP server support. It's now possible to extend Agent Mode's capabilities using programs that support the [Model Context Protocol](https://docs.warp.dev/documentation/knowledge-and-collaboration/mcp).

### 2025.05.21 (v0.2025.05.21.08.11)

**New Features**

* Set new Agent Mode permissions around executing commands, reading files, coding, and planning in AI settings.

**Improvements**

* You can now choose the coding model behind Agent Mode.
* Agent Mode conversations can now be paused via a hovering control panel in the right corner.
* Improved maximum block output capacity to 50k lines.

**Bug Fixes**

* Fix edit icon positioning for shared sessions.

### 2025.05.14 (v0.2025.05.14.08.11)

**Improvements**

* Introduced refining functionality for requested commands.
* Added ability to continue previous Agent Mode conversations directly from response blocks.
* Overhauled the editing experience for suggested plans.
* Renamed input auto-detection setting to natural language detection in Command Palette for better clarity.
* Zero-state prompt suggestion chips are now horizontally clipped instead of being individually shrunk.

**Bug Fixes**

* Fixed incorrect ordering in history of executed commands and agent mode queries.
* Copying text from Agent Mode plans and suggested code changes now works more reliable.
* \[Windows] Made some changes to reduce false-positives from virus scanners.

### 2025.05.07 (v0.2025.05.07.08.12)

**Improvements**

* Redesigned env var collection block UX.
* Added ability to embed Warp Drive Prompts inside Notebooks.
* Added AI block loading animation.
* Added ability to select and continue previous Agent Mode conversations.
* \[MacOS] Improved time to update and relaunch Warp.

**Bug Fixes**

* Fixed a bug where escape was clearing autosuggestions in Vim's insert mode.
* Stopped showing an unexpected block in the planning output for o3.
* \[Windows] Fixed a bug when hovering symlinks in WSL sessions.
* Fixed terminal input remaining hidden after cancelling an env var block.
* Prevented unexpected empty code fences in agent mode when using Gemini 2.5 Pro or o3.

### 2025.04.30 (v0.2025.04.30.08.11)

**New Features**

* Added desktop notifications for Agent Mode. Now, you can be notified when an agent completes a task, or when an agent needs your attention to continue (i.e. to review a command, to run an unsafe command, etc). You can configure these settings from `Features > Notifications`.

**Improvements**

* Agent Mode is now more robust at applying code diffs.
* Redesigned requested commands UX.
* Improved readability for "needs password prompt" desktop notifications.

### 2025.04.23 (v0.2025.04.23.08.11)

**Improvements**

* Restored Agent Mode conversations can now be continued.
* Agent Mode now has access to a filepath search tool for coding tasks.
* Improved the reliability and positioning of suggestion dialogs for rules and Agent Mode workflows.
* We reworked the command palette search to make it more useful.

**Bug Fixes**

* Fix XML parse errors complaining that a "thought" cannot be empty.
* \[Windows] Fixed an issue where Agent Mode would fail to search when in WSL or Git Bash.
* Show "copy" button and other text selection tools when right clicking selected environment variable text.
* Fixed old shortcuts icon appearing in new tab page, if recommended AI prompts are disabled.
* Fish commands containing syntax errors now correctly "finish" the block.

### 2025.04.16 (v0.2025.04.16.08.11)

**New features**

* After editing a code diff, you will now be returned to your original Agent Mode conversation.
* Commands with certain invalid arguments will no longer be suggested, such as file paths, git branches, and docker images.
* \[Windows/Linux] You can now open launch configurations in the current window with `SHIFT-ENTER` or `CTRL-ENTER` on the Command Palette.
* Added more default regexes for Secret Redaction, pertaining to AI API keys.
* Typing `ESC` in the terminal input editor now clears any Autosuggestions.

**Bug Fixes**

* Fixed issue with rendering performance for file links in AI output.
* Fixed an issue that causes Warp to crash when Agent Mode outputs broken links.
* New tab page no longer falls back to email if display name is not set.
* Fixed prompt chips not being clickable in new session with prompt pinned to top.
* Agent Mode now properly greps for queries containing double quotes.

### 2025.04.09 (v0.2025.04.09.08.11)

**New features**

* Recommended AI prompts are shown in new tabs, go to Settings > Features to disable.

**Improvements**

* Agent Mode is now better at searching for exact function / symbol / etc. names in your code.
* Fix text selection for environment variable blocks.
* You can now attach select text in a code block as the Agent Mode context.
* Warp now supports marked text in the IME (non-English keyboards).
* Make text selectable for non-expandable command outputs (ex. failed agent tasks).
* Zero-state chips are no longer shown when entering AI input with a non-empty input buffer.

**Bug fixes**

* Fixed a bug that prevented copying of selected text of a code block when Agent Mode is enabled.
* Fixed a bug that allows a selection in the code block and a selection on the text simultaneously.
* \[Mac] Fixed shells installed via Homebrew not appearing in the list of available shells.

### 2025.04.02 (v0.2025.04.02.08.11)

**New features**

* Get early access to unreleased and experimental features with [Warp Preview](https://docs.warp.dev/documentation/community/warp-preview-and-alpha-program).

**Improvements**

* Improved login item management to respect when users manually remove Warp from login items in System Preferences.
* The input editor now supports `CMD-SHIFT-UP/DOWN` on macOS or `CTRL-SHIFT-HOME/END` on Windows/ to move and select to the top/bottom of the text buffer.
* Removed 3-hour conversation timeout, allowing AI conversations to remain active indefinitely.
* Show a small popup when users who are at AI limits have their quota reset.
* Display a notification when AI request quota resets after hitting the limit in the previous billing cycle.
* \[Windows] Added “Open Warp in new tab / window” item for folders in the File Explorer context menu under “Show more options”.

**Bug fixes**

* Minor fixes for iTerm and Kitty images.
* Fixed regression related to using keyboard shortcuts to navigate a command an empty split pane.
* Fixed some issues with Agent Mode failing to read files.
* Click targets in scroll views should more reliably click while moving the mouse.
* \[Linux] Window corners are correctly rounded with themes having background images.
* Fix a few common failure modes for Agent Mode response deserialization errors.

### 2025.03.26 (v0.2025.03.26.08.10)

**New features**

* Kitty Image Protocol is now supported on macOS and Linux!

**Improvements**

* Agents may suggest using Dispatch to create a plan for complex tasks. You can disable suggestions to create plans under `Settings > AI > Dispatch`.
* You can now resume auto-execution of a previously dispatched plan if your follow-up query is set to "Dispatch", instead of creating a new plan.
* Added a keyboard shortcut to accept the most recent command correction.
* Zero-state suggestions are no longer shown when using a saved Prompt or past AI query.
* Tabs will not resize while hovered, making closing multiple tabs easier.
* The warning dialog for closing sessions now responds to the `ENTER` and `ESC` keys.
* Selected text within Agent responses can now be copied via the `RIGHT-CLICK` menu.
* \[Windows/Linux] You can now toggle whether a block is selected using `CTRL+CLICK`.

**Bug fixes**

* Fixed an issue that caused Agent mode blocks to be incorrectly highlighted when performing rectangular selection.
* Fixed an issue where duplicate cloud preferences could be created during sync operations.
* Fixed keyboard shortcut padding for prompt suggestions.
* Fixed color contrast issues with light themes for the Pair & Dispatch chip in Prompt Editor.
* Agent Mode will no longer default to Windows-style line endings when creating a new file on macOS or Linux.
* PowerShell sessions will start even if the profile has a terminating error.
* The numpad `ENTER` key now behaves like the `ENTER` key in Agent Mode.
* \[Mac] Fixed a scenario where Warp would beachball while updating.
* \[Windows] In WSL, show completions for symlinked files.
* \[Windows] Fixed completions with `.exe` suffixes.
* \[Windows] Fixed setting Git Bash custom shell paths.

### 2025.03.12 (v0.2025.03.12.08.02)

**New features**

* Agent Mode output is now rendered with Markdown formatting.
* You can now change the font used for Agent Mode output (Settings > Appearance).

**Improvements**

* \[Windows] Significantly improved pseudoconsole throughput (\~3x improvement).
* The Agent Mode model will now automatically select the best model based on your specific task.
* Ordered lists in Markdown now uses alphabetical or Roman numeral labels when nested.
* \[Windows] We now search more locations for a PowerShell executable.
* Reduced the size of Markdown headings.

**Bug fixes**

* Control whether Warp starts at login via a setting under Settings > Features > Start Warp at login (MacOS only).
* \[Windows] Fixed an issue where dynamic enums commands weren't being executed.
* Fixed a bug with the mouse cursor when hovering over buttons.
* Fixed a bug that causes high CPU load with codebase context.

### 2025.03.05 (v0.2025.03.05.08.02)

**New features**

* iTerm Image Protocol is now supported on Mac and Linux!
* \[macOS] Warp now starts at login (can be disabled in System Settings > Login Items & Extensions).

**Improvements**

* Input mode automatically returns to command mode when a command is detected in an AI follow-up request. (Only applies if natural language detection is turned on.)
* Text selections can now be attached to Agent Mode queries as context.
* \[Windows] Window transparency now works when using DirectX 12.
* \[Windows] Added “Open Warp Here” item for folders in the File Explorer context menu under “Show more options”.

**Bug fixes**

* Fixed an issue where `bazel` completions could use up a lot of CPU.
* \[macOS] Fixed a regression where the title bar would be transparent in fullscreen windows.
* \[Windows] Fixed children of shell processes not always exiting properly at shell termination.
* \[Windows] Fixed Warpification for custom-built WSL distributions.
* \[Windows] Fixed Ctrl-Up and Ctrl-Down shortcuts not working in alt screen programs (e.g. vim and emacs).
* \[Windows] Fixed last line of output getting truncated with some prompt configs in WSL.
* \[Windows] Fixed some hangs when using Agent Mode.
* \[Windows] Fixed issues starting PowerShell in strict mode.
* \[Windows] Fixed an issue where `.` would turn into n in ZSH when using ohmyzsh in WSL with an Italian keyboard layout.

### 2025.02.26 (v0.2025.02.26.08.02)

**New features**

* Warp is now available for Windows! See our [#windows](https://docs.warp.dev/documentation/readme#windows "mention") Quickstart Guide
* Prompt, plan, and execute fully autonomous tasks from [Agent Mode with Dispatch](https://docs.warp.dev/documentation/agents/using-agents#dispatch) (Beta)
* Add codebase context support to Agent Mode. Currently enabled for git repositories only.
* \[macOS] You can now customize your [App Icon](https://docs.warp.dev/documentation/terminal/appearance/app-icons) in `Settings > Appearance > Icon`.
* Create and store [Rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules) to use as Agent Mode context.
* Show default suggestions in Agent Mode input.

**Bug fixes**

* Multicursor input is now `ALT` on Linux and Windows.
* Fix prompt chip misalignment for certain fonts.
* Autosuggestions remain visible when the input is not focused, to prevent height flickering when the autosuggestion soft wraps.

### 2025.02.19 (v0.2025.02.19.08.02)

**New features**

* Create and store AI memories to use as Agent Mode context.

**Improvements**

* Expanded Prompt Suggestions to cover more use cases.

**Bug fixes**

* Fixed Warp Prompt clipping issues encountered with certain fonts.
* Fixed inverse and double-underline cell styling not persisting through session restoration.

### 2025.02.12 (v0.2025.02.12.16.51)

**New features**

* `CTRL-TAB` is now configurable under `Settings > Features` to cycle between the most recently used sessions rather than just activating the next tab.

**Improvements**

* The LLM menu is now keyboard-navigable.

**Bug fixes**

* Clearing Blocks now also clears any active Prompt Suggestions.
* Fix Kali Linux `.bashrc` breaking Warp.
* Fix bug with Agent Mode in PowerShell sessions with multi-line commands.
* Fixed a bug that prevented Autosuggestions from being accepted and Agent Mode model from being selected while up arrow history was open.
* Fixed cases where dragged Warp tabs would get stuck.
* Restores subshell Warpification script.
* \[macOS] Fix hotkey keybinding not triggering on non-US keyboard input source.

### 2025.02.05 (v0.2025.02.05.08.02)

**New features**

* You can now talk to Warp to transcribe Agent Mode prompts or any other text! Set up the hotkey in `Settings > AI > Voice` or use the microphone button in AI input mode to trigger this.

**Improvements**

* Autosuggestions in the input now soft-wrap.
* You can now attach default environment variables to a workflow.

### 2025.01.29 (v0.2025.01.29.08.02)

**New features**

* Added support for DeepSeek R1 and V3 in Agent Mode! Try them out by switching to Agent Mode and clicking on the model name in the prompt.
* Agent Mode can now auto-execute readonly requested commands. Commands can also be explicitly allowlisted or denylisted. See `Settings` -> `AI` -> `Autonomy` to configure.

**Improvements**

* You can now use `j`/`k` keys to navigate up and down Warp Drive.
* Agent Mode chip added to Warp prompt.
* Next Command is preferred over Command Corrections in cases where Corrections has less confidence.
* Moved the Settings modal to its own tab.

**Bug fixes**

* Fixed a bug that caused double-clicking to select the incorrect range of text when non-ASCII characters are present.
* Saving workflow aliases no longer deletes aliases from other workflows.
* Fixed cases where a small part of the bottom of the editor would be cut off at certain appearance settings.

### 2025.01.22 (v0.2025.01.22.08.02)

**New features**

* Generate input for any interactive CLI using ⌘I on macOS and Ctrl-Shift I on Linux.
* You can now dynamically populate arguments in Workflows with shell commands.
* Added support for rectangular selection when holding ⌘⌥ on Mac and Ctrl-Alt on Linux.

**Improvements**

* Settings are now searchable and rendered in a separate tab
* Terminal font weight is now configurable.
* Launch Configurations now save the focused window state and active pane.
* Autosuggestions in the input now soft-wrap.

**Bug fixes**

* Fixed several issues where hovering over URLs in the blocklist sometimes resulted in URLs only being partially detected, or not detected at all.
* Fixed issue with Prompt Suggestions occasionally remaining visible after subsequent command exeuction.
* \[macOS] Changed the download location for new Warp updates to prevent corruption.

### 2025.01.15 (v0.2025.01.15.08.02)

**New features**

* Font ligatures in grids! See setting under Settings > Appearance > Text to enable.
* You can now define aliases that expand to Warp Drive workflows.

**Improvements**

* Launch configurations now save focused tab state.
* Added support for Windsurf as an external editor.
* Mac-only: added a new AI app menu.

**Bug fixes**

* Fixed pane navigation when panes are not overlapping.
* Fixed a bug where Agent Mode LLM choices weren't populated correctly upon logging in.
* Fixed bug with drag-and-drop files causing duplicated filepaths.

### 2025.01.08 (v0.2025.01.08.08.02)

**New features**

* A percentage of Warp users may now enable cloud syncing of their Warp settings under `Settings` > `Account`. We are gradually enabling this feature for all Warp users starting in this release. See the [documentation](https://docs.warp.dev/features/settings-sync) for more information.
* Introduced a setting to hide the tab bar (Zen mode). See the [documentation](https://docs.warp.dev/appearance/tabs-behavior) for more information.
* Introduced new profile menu.

**Improvements**

* Removed the Command Corrections banner, as there's already an autosuggestion in the input editor.
* Implemented `_`, `+`, and `-` motions in Vim mode.
* Warp will now show a warning before closing a session with a long-running process.
* Pasting multiple lines of content into the terminal's `Find` feature will convert it into a single line of text, rather than hide previous lines.
* Titles of notebooks imported from Markdown files no longer end in `.md`.
* "What's new" no longer shows on update.
* Added the ability to hide blocklist lines.
* Consolidated top bar navigation items.
* Settings are now in the profile menu.
* Scrollbars and pane controls only show on hover.

**Bug fixes**

* Fixed the rendering of keyboard shortcuts at larger font sizes.
* Tab completion menu now closes after selecting a single remaining suggestion.
* Warp displays an error if relaunching to apply an update failed.
* Old prompt suggestions won't reappear when issuing AI queries rapidly or after clearing the blocklist.
* Accepting the 'What happened here?' autosuggestion no longer clears AI context blocks.
* `alt` key now sends meta control codes to the shell in long-running blocks and the alt screen.
* When secret redaction is disabled, secrets are not redacted in command corrections.
* \[MacOS] Fixed a bug where assigning `cmd-shift-left` and `cmd-shift-right` to an action sometimes wouldn't work.

### 2025.01.02 (v0.2024.12.18.08.02)

**Improvements**

* We now immediately show an error when trying to Warpify unsupported shells over SSH.

**Bug fixes**

* Fixed blank lines being appended to some blocks on resize.
* Fixed an issue where the AI context disappears when accepting the default autosuggestion.

### 2024.12.26 (v0.2024.12.18.08.02)

**Improvements**

* We now immediately show an error when trying to Warpify unsupported shells over SSH.

**Bug fixes**

* Fixed blank lines being appended to some blocks on resize.
* Fixed an issue where the AI context disappears when accepting the default autosuggestion.

### 2024.12.19 (v0.2024.12.18.08.02)

**New features**

* Introducing: Next Command! Next Command uses AI to suggest the next command to run based on your active terminal session and command history. Visit Settings > AI to turn it off.
* Added support for block and underline-styled cursors in the input editor (while vim mode is disabled).

**Improvements**

* Clarified default permission information for sessions and Warp Drive objects.
* F11 (configurable) now toggles fullscreen on Linux and Windows.
* PowerShell environment variables are now recognized in completions.
* Cursor shape is now more responsive to clickable buttons.

**Bug fixes**

* Characters from unhandled keystrokes no longer handled as typed characters in the alt screen, e.g. when using vim.
* Fixed issue with copying secrets when secret redaction is disabled.
* kubectl completions now respect your kubeconfig, specified through environment variables or command line flag.
* ssh commands with permission issues should no longer suggest sudo.
* Fixed an issue with lazygit entering a blank screen.
* \[macOS] Fixed a bug where Warp disk images volumes might not be unmounted after an update.
* \[macOS] Improved robustness of autoupdate process.

### 2024.12.13 (v0.2024.12.10.15.55)

**New features**

* Prompt Suggestions may appear above the input, helping you activate Agent Mode quickly in scenarios where it might be helpful. Note this feature sends activity to an LLM to generate prompts, head to Settings > AI > Agent Mode if you'd like to turn it off.
* Warp now has support for Claude 3.5 Sonnet and Haiku. Choose which model to use in the dropdown menu above your Agent Mode prompts.
* Agent Mode can now leverage your Warp Drive contents to tailor responses to your personal and team developer workflows.
* Warp has added a Shell Selector - a dropdown menu next to the 'New tab' button in the tab bar - to quickly pick from the shells available on your system.
* Agent Mode can now suggest code changes in a built-in code editor.
* \[macOS] You can now configure whether closing the last window quits the app (in Settings > Features).

**Improvements**

* Added settings to manage Warp's AI integration and permissions. Visit Settings > AI to learn more.
* Single-window launch configs can be launched into the active window from the launch config palette using cmdorctrl-enter.
* You can now set `PS1` with `PROMPT_COMMAND` in bash.

**Bug fixes**

* Fixed an issue where the 'Git Uncommitted File Count' prompt chip did not work on fish on Linux.
* Fixed highlighting for arguments in workflows with multibyte characters
* Hitting ENTER within the Launch Config Save Modal will work as expected.
* Fixed issue with copying secrets when secret redaction is disabled.

### 2024.12.11 (v0.2024.12.10.15.55)

**New features**

* Prompt Suggestions may appear above the input, helping you activate Agent Mode quickly in scenarios where it might be helpful. Note this feature sends activity to an LLM to generate prompts, head to Settings > AI > Agent Mode if you'd like to turn it off.
* Warp now has support for Claude 3.5 Sonnet and Haiku. Choose which model to use in the dropdown menu above your Agent Mode prompts.
* Agent Mode can now leverage your Warp Drive contents to tailor responses to your personal and team developer workflows.
* Warp has added a Shell Selector - a dropdown menu next to the 'New tab' button in the tab bar - to quickly pick from the shells available on your system.
* Agent Mode can now suggest code changes in a built-in code editor.
* \[macOS] You can now configure whether closing the last window quits the app (in Settings > Features).

**Improvements**

* Single-window launch configs can be launched into the active window from the launch config palette using cmdorctrl-enter.
* You can now set `PS1` with `PROMPT_COMMAND` in bash.

**Bug fixes**

* Fixed an issue where the 'Git Uncommitted File Count' prompt chip did not work on fish on Linux.
* Fixed highlighting for arguments in workflows with multibyte characters
* Hitting ENTER within the Launch Config Save Modal will work as expected.

### 2024.12.05 (v0.2024.12.03.08.02)

**New features**

* You can now share shared sessions directly with your Warp team, another Warp user, and non Warp users via a URL.
* You can now share Warp Drive objects directly with others via email or a URL.
* Padding in the alt-screen can now be manually adjusted. Defaults to no padding.

**Improvements**

* Improved PTY throughput by \~13% through more efficient dirty region computation.

### 2024.12.02 (v0.2024.12.02.15.50)

**Bug fixes**

* Warp no longer uses so much CPU.

### 2024.11.27 (v0.2024.11.27.01.55)

**Improvements**

* \[Agent Mode] Code outputs no longer show a confusing code diff UI.
* You can now sort Warp Drive objects by type, with folders on top.

**Bug fixes**

* \[Agent Mode] Single-line code suggestions are no longer hidden behind the horizontal scrollbar.
* Fixed a crash interacting with Env Vars in the command palette.

### 2024.11.25 (v0.2024.11.25.16.32)

**Improvements**

* \[Agent Mode] Code outputs no longer show a confusing code diff UI.
* You can now sort Warp Drive objects by type, with folders on top.

**Bug fixes**

* \[Agent Mode] Single-line code suggestions are no longer hidden behind the horizontal scrollbar.
* Fixed a crash interacting with Env Vars in the command palette.

### 2024.11.22 (v0.2024.11.22.18.28)

**Improvements**

* \[Agent Mode] Code outputs no longer show a confusing code diff UI.
* You can now sort Warp Drive objects by type, with folders on top.

**Bug fixes**

* \[Agent Mode] Single-line code suggestions are no longer hidden behind the horizontal scrollbar.
* Fixed a crash interacting with Env Vars in the command palette.

### 2024.11.26 (v0.2024.11.19.08.02)

**New features**

* You can now use Warp without login!

**Improvements**

* \[Agent Mode] Code outputs no longer show a confusing code diff UI.
* You can now sort Warp Drive objects by type, with folders on top.

**Bug fixes**

* \[Agent Mode] Single-line code suggestions are no longer hidden behind the horizontal scrollbar.
* Fixed a crash interacting with Env Vars in the command palette.
* Fixed a bug where `command substitution: ignored null byte in input` would appear as output while using a Bash subshell.

### 2024.11.19 (v0.2024.11.19.08.02)

**New features**

* You can now use Warp without login!

**Improvements**

* \[Agent Mode] Code outputs no longer show a confusing code diff UI.
* You can now sort Warp Drive objects by type, with folders on top.

**Bug fixes**

* \[Agent Mode] Single-line code suggestions are no longer hidden behind the horizontal scrollbar.
* Fixed a crash interacting with Env Vars in the command palette.

### 2024.11.18 (v0.2024.11.18.16.37)

**Improvements**

* Added padding after an expanded Agent Mode requested command.
* Improved the quality of autosuggestions.
* Warp Drive workflow links now open in the active terminal session rather than a new tab.
* On the web, Warp Drive workflows now have a button to quickly open the workflow in Warp's desktop app.

**Bug fixes**

* Fixed Graphite CLI (`gt`) completions.
* Fixed completion and syntax highlighting behavior for arguments containing backslashes in PowerShell.
* Fixed an issue where opening Warp Drive in a browser could cause the tab to stop responding.

### 2024.11.12 (v0.2024.11.12.08.02)

**Improvements**

* Added padding after an expanded Agent Mode requested command.
* Improved the quality of autosuggestions.
* Warp Drive workflow links now open in the active terminal session rather than a new tab.
* On the web, Warp Drive workflows now have a button to quickly open the workflow in Warp's desktop app.
* \[Linux] Increased the app icon size to match other apps.

**Bug fixes**

* Fixed Graphite CLI (`gt`) completions.
* Fixed completion and syntax highlighting behavior for arguments containing backslashes in PowerShell.
* Fixed an issue where opening Warp Drive in a browser could cause the tab to stop responding.
* \[Linux] Tightened timeout for looking up the system color scheme at app startup to avoid hangs if the `org.freedesktop.portal.Desktop` D-Bus service is unresponsive.
* \[macOS] Fixed a crash that can occur when starting the app or opening a new window.

### 2024.11.11 (v0.2024.11.05.08.02)

**Improvements**

* Fixes a bug where Warpifying subshells could crash if you had something typed in your input.
* Renamed the Subshells tab to Warpify in Settings.

**Bug fixes**

* Fixed an issue where kubectl resource names wouldn't complete given a prefix.
* Fixed bug causing not all memory to be immediately freed when clearing the blocklist.
* \[macOS] Fixed a crash that can occur when starting the app or opening a new window.

### 2024.11.05 (v0.2024.11.05.08.02)

**Improvements**

* Fixes a bug where Warpifying subshells could crash if you had something typed in your input.
* Renamed the Subshells tab to Warpify in Settings.

**Bug fixes**

* Fixed an issue where kubectl resource names wouldn't complete given a prefix.
* Fixed bug causing not all memory to be immediately freed when clearing the blocklist.

### 2024.10.23 (v0.2024.10.29.08.02)

**Bug fixes**

* Improved command completions to no longer attempt to use error messages as valid options.
* Fixed some kubectl completions not working as intended.

### 2024.10.17 (v0.2024.10.15.08.02)

**New features**

* Warp.dev has a fresh look today! Check out what's new and read about the design process behind the launch: <https://www.warp.dev/blog/world-of-warp>

**Improvements**

* Created a setting allowing focus to follow mouse hover (requested in issue [699](https://github.com/warpdotdev/warp/issues/699)).
* Automatically switch to shell command input mode if accepting a shell command autosuggestion from Agent Mode.
* \[macOS] Adjusted default font smoothing (Appearance > "Use thin strokes") configuration to improve text legibility.

**Bug fixes**

* Alt-screen find doesn't beachball when scrolling through find matches.
* You can now select individual cells in the alt-screen.
* All find matches are correctly highlighted in the alt-screen.
* Hitting ENTER within the Launch Config Save Modal will work as expected.
* Removed node prompt chip due to slow performance.
* Fixed an issue on Linux distributions where Warp took a long time to start up.

### 2024.10.11 (v0.2024.10.08.08.02)

**Improvements**

* Tab key always accepts active autosuggestions in zero-state.
* Command suggestions from Agent Mode are now ghosted autosuggestions instead of direct buffer text.
* Warp now shows a warning when closing a tab with running commands or shared sessions.
* New Agent Mode panes will open to a useful minimum width if the Warp window is big enough to support it.
* Clearing the terminal input via ctrl-c will now also close the command search.
* \[macOS] You can now access Warp Drive features from mac menus.
* \[macOS] You can click the mouse middle-button to paste from the clipboard.

**Bug fixes**

* Agent Mode queries are now de-duplicated in up-arrow history and Command Search.
* `ctrl-d` can now be used to signal EOF when the shell is bootstrapping.
* Double-clicking the tab bar now correctly toggles maximizing the Warp window even when an AI block is present in the focused pane.
* Hovering over the block insertion menu at the bottom of a notebook no longer causes Warp to hang.
* Fixed crash when search result in alt screen is scrolled out of view.
* Fixed broken `cmd-shift-R`/`ctrl-shift-R` keybinding for accessing the Workflows view.

### 2024.10.10 (v0.2024.10.08.08.02)

**Improvements**

* Tab key always accepts active autosuggestions in zero-state.
* Command suggestions from Agent Mode are now ghosted autosuggestions instead of direct buffer text.
* Warp now shows a warning when closing a tab with running commands or shared sessions.
* New Agent Mode panes will open to a useful minimum width if the Warp window is big enough to support it.
* Clearing the terminal input via ctrl-c will now also close the command search.
* \[macOS] You can now access Warp Drive features from mac menus.
* \[macOS] You can click the mouse middle-button to paste from the clipboard.

**Bug fixes**

* Agent Mode queries are now de-duplicated in up-arrow history and Command Search.
* `ctrl-d` can now be used to signal EOF when the shell is bootstrapping.
* Double-clicking the tab bar now correctly toggles maximizing the Warp window even when an AI block is present in the focused pane.
* Hovering over the block insertion menu at the bottom of a notebook no longer causes Warp to hang.

### 2024.09.24 (v0.2024.09.24.08.02)

**New features**

* Powershell is now supported! Make `pwsh` your default shell for your user account or select `pwsh` in Settings > Features > Startup shell for new sessions.
* You can now save and sync environment variable collections in Warp Drive. Learn more: <https://docs.warp.dev/features/warp-drive/environment-variables> .
* Your Agent Mode blocks and queries are now restored across sessions.

**Improvements**

* Secret redaction now applies to AI Blocks within Warp, in addition to Command Blocks.
* New Agent Mode panes always open to the right.
* You can now navigate the trash index via your keyboard.

**Bug fixes**

* `fish` config is no longer sourced twice during shell startup.
* The first window after launching Warp will now use a custom window size if set.
* When opening a launch configuration, Warp now respects restored and custom window sizes.

### 2024.09.17 (v0.2024.09.17.08.02)

**New features**

* \[Linux] Warp now supports Wayland. You can configure the window system in `Settings > Features > System`.

**Improvements**

* Adds a Command Palette action called “Export all Warp Drive objects” that enables bulk export of a Warp Drive.
* Completion suggestions for git commit hashes are now sorted reverse-chronologically.
* History shows the working directory in which you made an Agent Mode query.
* Agent Mode Blocks are surfaced in Find.

**Bug fixes**

* Fixed an infinite loop bug that could lead to runaway memory usage and the application hanging.
* Fixes a regression where the Setup Guide didn't work.

### 2024.09.05 (v0.2024.09.10.08.02)

**Improvements**

* Links are now detected in Agent Mode responses.

**Bug fixes**

* Fixed an infinite loop bug that could lead to runaway memory usage and the application hanging.

### 2024.08.29 (v0.2024.08.27.08.02)

**Bug fixes**

* Link highlights now correctly disappear when making changes in alt-screen programs.

### 2024.08.22 (v0.2024.08.20.08.02)

**New Features**

* You can now specify a cursor color in Warp themes.

**Improvements**

* Warp now restores fullscreen windows to fullscreen.

**Bug fixes**

* \[MacOS] Completions for commands now work when you type a command name containing capital letters. This does not apply to aliases.

### 2024.08.14 (v0.2024.08.13.08.02)

**New Features**

* New enums for Workflow arguments. Now you can set a list of suggested options for any argument in a workflow so it's easier to fill in parameters correctly. Learn more at <https://docs.warp.dev/features/warp-drive/workflows#working-with-arguments>

### 2024.08.07 (v0.2024.08.06.08.01)

**New Features**

* You can now find your past Agent Mode queries in Command Search (ctrl-r).

**Improvements**

* Completions-as-you-type now works in AI input for filepath completions.

**Bug Fixes**

* Warp now recognizes more escape codes for toggling alternate screen mode.

### 2024.07.30 (v0.2024.07.30.08.02)

**Improvements**

* Now it's easier to find and configure settings related to AI on the command line. You can enable / disable natural language detection or input hint text under Settings > AI

### 2024.07.24 (v0.2024.07.23.08.02)

**New features**

* You can now find AI queries from other sessions in up-arrow history.

**Improvements**

* Clicking an attached block on an AI block no longer affects your pending query's context selection.
* Clicking the terminal input box will no longer remove the blocks you selected as context.
* Added support for smart selections in AI blocks.
* Increased priority of command matches when searching for a workflow.

**Bug fixes**

* Opening file links with line and column numbers in Zed now works.

### 2024.07.19 (v0.2024.07.16.08.02)

**Improvements**

* Completions for git push origin now include tags in addition to branches.
* Docker extension: The "Open in Warp" feature now requires you to run the command in order to open the Warpified Docker subshell. Attempts to open an invalid link will display an error toast.

**Bug fixes**

* Warp prompt text now respects custom line height settings.
* Scroll positions are now stable when hitting block line limits ([1355](https://github.com/warpdotdev/warp/issues/1355)).
* Fixed binaries listed directly in `PATH` being automatically executed when running commands in Bash.

### 2024.07.18 (v0.2024.07.16.08.02)

**Improvements**

* Completions for git push origin now include tags in addition to branches.
* Docker extension: The "Open in Warp" feature now requires you to run the command in order to open the Warpified Docker subshell. Attempts to open an invalid link will display an error toast.

**Bug fixes**

* Warp prompt text now respects custom line height settings.
* Scroll positions are now stable when hitting block line limits ([1355](https://github.com/warpdotdev/warp/issues/1355)).
* Fish commands containing syntax errors now correctly "finish" the block.
* Fixed binaries listed directly in `PATH` being automatically executed when running commands in Bash.

### 2024.07.11 (v0.2024.07.09.08.01)

**New features**

* Same line prompt. Now you can choose whether you'd like your prompt on a new line (Warp's default) or on the same line with commands, like a classic terminal. If you're using PS1, Warp will use the same line prompt setting to respect theme configurations. Visit Settings > Appearance > Prompt to configure your prompt style. [Learn more](https://docs.warp.dev/appearance/prompt#same-line-prompt)

**Improvements**

* Added support for completions while using Agent Mode input.
* Semantic selection now works in AI blocks.
* Shift+click now lets you select text for alternate screen apps in SGR mouse mode.

**Bug fixes**

* Pressing Esc in Vim insert mode no longer closes the history menu.
* Made sure terminal context menus close when opening the settings modal.

### 2024.06.27 (v0.2024.06.25.08.02)

**New features**

* Warp’s new Pro plan includes higher AI requests for individuals or small teams.
* Learn more at <https://www.warp.dev/blog/pro-plan>

**Bug fixes**

* Text selection in full screen apps will change as you scroll.
* \[MacOS] Meta shortcuts, e.g. `OPT-U`, `OPT-I`, will no longer be ignored.

### 2024.06.21 (v0.2024.06.18.08.02)

**Improvements**

* The glyph over the cursor will take on a high-contrast color to make sure it's legible.
* Dragging a word or line selection in a notebook now extends the selection.

**Bug fixes**

* Fixes a crash where text layout would not expect the BOM marker at the beginning of a string.
* \[Linux] Fix middle-click paste doubling the text.

### 2024.06.20 (v0.2024.06.18.08.02)

**Improvements**

* The glyph over the cursor will take on a high-contrast color to make sure it's legible.
* Dragging a word or line selection in a notebook now extends the selection.

**Bug fixes**

* Fixes a crash where text layout would not expect the BOM marker at the beginning of a string.

### 2024.06.17 (v0.2024.06.11.08.02)

**New features**

* New Agent Mode in Warp AI: Use plain English on the command line to accomplish multi-step workflows.
* Learn more at <https://www.warp.dev/blog/agent-mode>

### 2024.06.13 (v0.2024.06.11.08.02)

**Improvements**

* Brackets and quotes are now autocompleted in the workflow editor.
* Improved support for editing multi-line workflows.

### 2024.06.06 (v0.2024.06.04.08.02)

**Improvements**

* Warp now supports Unicode emoji presentation selectors when rendering glyphs
* Removed the default keybindings for Warp Drive object creation actions, in order to free up more keyboard shortcut options. You can still assign custom keybindings to these actions in Settings > Keyboard shortcuts

**Bug fixes**

* When editing with Vim visual line mode and the cursor is at the end of the line, operators will only affect the correct lines

### 2024.05.30 (v0.2024.05.28.08.02)

**Improvements**

* Warp now renders terminal text ANSI colors as specified by the theme without any dimming

### 2024.05.23 (v0.2024.05.21.16.09)

**Bug fixes**

* Fixed a bug where a terminal session could get stuck in a bad state if an SSH connection is lost while the alternate screen is in use (e.g.: tmux, TUI programs, pagers)
* Fixed a bug where 00\~ and 01\~ characters could get erroneously added to user-submitted commands after an SSH connection is lost

### 2024.05.16 (v0.2024.05.14.08.01)

**New features**

* Team admins can now make their teams discoverable to colleagues from the same custom email domain. This feature is available under Settings -> Teams.

**Bug fixes**

* The prompt and command should no longer overlap the output (or each other) for multi-line commands in Bash versions earlier than 4.4--such as the default Bash installation for MacOS.

### 2024.05.09 (v0.2024.05.07.08.02)

**Bug fixes**

* Vim-related settings no longer appear in the Command Palette when editing with Vim keybindings is disabled
* Warp’s Input Editor now immediately reflects any changes to the Vim status bar settings
* Fixed a bug when handling URLs with parentheses in notebooks and Warp AI

### 2024.05.02 (v0.2024.04.30.08.02)

**Bug fixes**

* In Notebooks, code block menus no longer overlap with rich text menus
* Fixed an issue that could cause Warp to display an invisible/empty window
* Fixed a crash that could occur when unindenting multiple lines within the Input Editor
* Fixed a Vim Mode bug when “cutting word left” (and similar actions) while the (up-arrow) history menu is open
* \[Linux] Fixed an issue where Warp would flicker on Intel UHD 620 drivers when using Vulkan due to a bug in specific versions of Mesa
* \[Linux] Fixed a regression in input latency

### 2024.03.27 (v0.2024.04.23.08.01)

**New features**

* The free preview for Warp AI and Warp Drive for teams has ended. \[Learn about Warp’s new self-service plan]

**Improvements**

* Shared links to notebooks and workflows are now opened directly in Warp and no longer need to go through a browser

**Bug fixes**

* Warp now supports completions for directories that contain spaces when in a remote session
* Warp’s notebook editor now only shows hint text when it’s in edit mode

### 2024.04.18 (v0.2024.04.16.08.02)

**Improvements**

* You can now navigate and expand folders in Warp Drive with left/right arrow keys

**Bug fixes**

* Middle-click now works even when the mouse is within the prompt area
* Already-open notebooks no longer open in a new tab
* Fixed an issue where autocd completions were incorrect for file paths starting with `~`
* Opening a Workflow through a link now focuses it, even while in trash view
* Fixed a bug handling carriage returns in notebooks, the markdown viewer, and Warp AI

### 2024.04.11 (v0.2024.04.09.08.01)

**Improvements**

* Improved Warp’s prompt performance for large repositories
* When switching panes directionally, Warp now automatically selects the most recently focused pane in that given direction

**Bug fixes**

* Fixed a pane management bug where dragging a pane to a new location wouldn't initiate the option to drop it there

### 2024.04.04 (v0.2024.04.02.08.02)

**New features**

* Notebooks in Warp Drive. Create and share interactive runbooks with your team. [Learn more](https://www.warp.dev/blog/notebooks-in-warp-drive)

**Improvements**

* You can now export workflows and notebooks from Warp Drive
* Middle-clicking to paste now automatically focuses the Input Editor
* Warp no longer automatically expands aliases that are escaped using a backslash
* \[Linux] Adds support for Android Studio, DataGrip, DataSpell, Goland, Pycharm, Rider, Rubymine, and Sublime Text as external editors

**Bug fixes**

* \[Linux] Warp now case-sensitively parses top-level commands on Linux
* \[Linux] Fixed an issue where middle-click paste could paste across multiple panes

### 2024.03.21 (v0.2024.03.19.08.01)

**Bug fixes**

* Symlinks to a directory are now properly treated as a directory instead of as a file
* \[Linux] Warp's windows are no longer escalated into an urgent state (tiling window managers) after a Warp URL is opened

### 2024.03.14 (v0.2024.03.12.08.02)

**Improvements**

* Warp now supports the primary selection protocol, which allows you to paste with a middle click. On platforms that don't support this, Warp will read/write from the default clipboard.
* You can now filter out unwanted lines from a block, using the new "invert filter" toggle in the block filtering menu
* Continuous block selections are now rendered with a single border instead of a border around each individual block
* The `` and `^` patterns are now supported in Warp's regex search (find bar and block filtering)
* \[Linux] The hotkey window now has a unique instance name on X11.

**Bug fixes**

* "Copy on Select" now works within alt-screens

### 2024.03.07 (v0.2024.03.05.08.02)

**Improvements**

* You can now adjust the number of lines the mouse wheel scrolls in Warp. Go to Settings > Features > General > Lines Scrolled by Mouse Wheel Interval to configure this setting.
* You can now close the Warp window using the Command Palette (`SHIFT-CMD-W` for Mac).
* You can now quit Warp using the Command Palette (“Quit Warp”)
* \[Linux] Warp can now automatically hide the window's traffic lights when using a tiling manager
* \[Linux] Improved (a window’s) rounded corners when using a tiling manager
* \[Linux] You can now move tabs left or right using keyboard shortcuts. Use `SHIFT-CTRL-PGUP` to move a tab to the left and `SHIFT-CTRL-PGDN` to move a tab to the right

**Bug fixes**

* Fixed a bug where Warp could crash because of an invalid Vim command
* \[Linux] Fixed a bug where errors encountered while running `pacman-key` could lead to an invalid pacman repository configuration

### 2024.03.05 (v0.2024.03.05.08.02)

**Improvements**

* Improved Warp's appearance and behavior when running in some tiling window managers.

**Bug fixes**

* Fixed crash that occurs when dragging the mouse.

### 2024.02.29 (v0.2024.02.27.08.01)

**Improvements**

* Added completion support for `dnf`
* Configuring the global hotkey window settings (Quake Mode) now updates the window in real time
* \[Linux] Can now `CTRL-CLICK` to open a file
* \[Linux] Added support for IntelliJ, CLion, Webstorm, and PhpStorm

**Bug fixes**

* Fix issue with typeahead commands overlapping the prompt’s content
* Command X-Ray now recognizes builtins and functions, hover over a command in the Input Editor to see the command description
* Fixed an issue where the shell couldn’t accept pasted text when an rc file expected user input.
* \[Linux] Modified pacman-key -r invocation during Arch Linux auto-update to be more robust
* \[Linux] Fixed crash on Linux that could occur if device was missing a symlink from libX11.so to libX11.so.6
* \[Linux] Fixed issues where opening external links would cause Firefox 123 to use 100% CPU and never launch
* \[Linux] X11 Users can now open links when default browser is firefox
* \[Linux] Fix some global hotkey combinations crashing the app.

### 2024.02.26 (v0.2024.02.20.08.01)

**New features**

* Warp is now available for Linux!

**Improvements**

* Completions for apt-get, aptitude, and pacman
* You can now type to search in the font picker in Settings > Appearance

### 2024.02.20 (v0.2024.02.20.08.01)

**Improvements**

* Completions for apt-get, aptitude, and pacman.

### 2024.02.16 (v0.2024.02.16.17.24)

**New features**

* Warp on Linux (Private Beta): Added support for the Input Mode Editor (IME).

### 2024.02.14 (v0.2024.02.14.15.46)

**New features**

* Warp on Linux (Private Beta): Added support for the Input Mode Editor (IME).

### 2023.02.08 (v0.2024.02.13.08.02)

**Bug fixes**

* Fix the inputted command sometimes overlapping rprompt (right-sided prompt)

### 2023.02.01 (v0.2024.01.30.16.52)

**Improvements**

* Improved UX for pasting an auth token to complete the sign-in flow
* Subversion (svn) information is now available in Warp's prompt

### 2023.01.18 (v0.2024.01.16.16.31)

**New features**

* Warp on Linux (Private Beta): System fonts now load as expected

**Bug fixes**

* Warp on Linux (Private Beta): `ALT-TAB` no longer incorrectly inserts 4 spaces into the Input Editor

### 2023.01.11 (v0.2024.01.09.08.02)

**New features**

* New workflow metadata for shared workflows in Warp Drive! Hover over any workflow to learn how recently the workflow has been executed, who edited it last, and when it was last edited.

### 2023.12.21 (v0.2024.01.02.08.02)

**Improvements**

* The toolbelt displayed when hovering over background Blocks now has a solid background

**Bug fixes**

* The Markdown Viewer now respects the start number of ordered lists
* Completing a path that includes the tilde (`~`) character now works as expected
* Fixed an issue where Warp could quit before saving changes to Warp Drive
* Fix Warp hanging when using the 'Insert into Input' context menu action

### 2023.12.14 (v0.2023.12.12.08.02)

**New features**

* Editing with Vim keybindings is now out of beta and generally available! Warp will detect vi mode in shell settings and suggest Vim keybindings.

**Improvements**

* You can now use `CMD-F` to search text in the Markdown Viewer

**Bug fixes**

* Block hover buttons now have a solid background when they overlap with your prompt
* The Block filter editor now has a clear button
* `J` and `K` (Vim Mode) can be used for navigation within a multi-line command
* Fixed the left alignment of the tab bar when in full-screen mode on Mac
* Fixed triple-click selection (selecting a line) when filtering a Block
* Fixed potential crash when using the find bar
* Fixed potential crash when retrieving accessibility contents
* Fix bug where "R" is erroneously inserted into the input in zsh sessions

### 2023.12.07 (v0.2023.12.05.08.02)

**Improvements**

* Markdown file links can now be configured to open with the default external editor or Warp's built-in markdown viewer
* Warp Drive folders now keep their opened/closed state through app restarts

**Bug fixes**

* The Input Editor now refocuses correctly after pasting terminal contents and running a command
* Fixed issue with missing toolbelt buttons when using fish wih Vim Mode

### 2023.11.30 (v0.2023.11.28.08.02)

**Improvements**

* Warp’s custom prompt builder now includes a context chip for Kubernetes context
* Improved completions for kubectl, including suggestions for resource, global options, and namespaces

**Bug fixes**

* Fixed a UI bug in the workflows editor where the editor for arguments was overflowing
* Search bar focuses as expected when you open Launch Configurations with the Command Palette

### 2023.11.16 (v0.2023.11.14.08.02)

**Bug fixes**

* The informational block that shows workflow metadata now resizes with your Warp window
* The scrolling speed is now standardized across Warp

### 2023.11.09 (v0.2023.11.07.08.02)

**New features**

* New Markdown Viewer: You can now open .md files in Warp and run the shell commands within these files
* Block Filtering: You can now filter block output (SHIFT-OPT-F) to quickly find matching lines based on a query.

**Improvements**

* Removed the workflow button from the toolbelt section (top-right buttons) of a block. It is still accessible through the right-click menu (see “Save as Workflow”) and its default keybinding CMD-S.
* Improved performance of Warp Drive team and state syncing

### 2023.11.02 (v0.2023.10.31.08.03)

**Improvements**

* You can now invite new team members to your shared Warp Drive by email address and revoke invitations

### 2023.10.23 (v0.2023.10.17.08.03)

**Improvements**

* Indicators appear in the tab bar when the current pane is maximized (a full-screen icon) and when a command exits with an error
* The Git context chip in Warp’s prompt now shows the commit hash instead of “HEAD” when in a detached state
* Easier to add and remove allowlisted domains when inviting teammates to Warp Drive
* Added a menu option for copying a workflow command (into the clipboard)

### 2023.10.19 (v0.2023.10.17.08.03)

**Improvements**

* Indicators appear in the tab bar when the current pane is maximized (a full-screen icon) and when a command exits with an error
* The Git context chip in Warp’s prompt now shows the commit hash instead of “HEAD” when in a detached state
* Easier to add and remove allowlisted domains when inviting teammates to Warp Drive
* Added a menu option for copying a workflow command (into the clipboard)

### 2023.10.12 (v0.2023.10.10.08.06)

**Improvements**

* Warp can now support MacOS's proxy settings
* You can now toggle whether to render Warp using the integrated GPU for dual GPU Macs
* Warp now escapes the file path of an executable loaded from Finder

**Bug fixes**

* Fixed a crash on startup for some users on MacOS Sonoma
* The workflow info box now refreshes when edited

### 2023.10.05 (v0.2023.10.03.08.03)

**New features**

* Now you can use Vim keybindings to edit text on the command line in Warp. Navigate to Settings > Feature > Editor and enable "Edit commands with Vim keybindings." This feature is currently in beta and available to try today.

**Improvements**

* Admins can now control whether the team invite link is accessible for other team members to copy and share. Admins can also reset the URL token if needed.
* You can now add a 24-hour timestamp to your Warp prompt with context chips in the prompt editor.
* The free preview for Warp AI and Warp Drive for teams has been extended. [Learn More](https://www.warp.dev/blog/free-preview-extended)

### 2023.09.28 (v0.2023.09.26.08.09)

**New features**

* If you have Cursor installed, you can now set this as your default code editor under Settings > Features > General.

**Improvements**

* Enhanced user accessibility by adding a tab bar button as a new entry point for the command palette.
* Improved user guidance by displaying a warning when attempting to run a workflow while another command is already in progress.

**Bug fixes**

* Resolved an issue where autosuggestions were not being inserted when bound to certain keybindings.
* Fixed a bug affecting Input Method Editor functionality on non-English keyboards, which caused incorrect positioning and prevented text input after opening a new window.

### 2023.09.14 (v0.2023.09.19.08.04)

**New features**

* You can now edit keybindings to scroll up and down by one line.

**Improvements**

* The input editor remains visible in inactive panes when using split panes.

**Bug fixes**

* Resolved a regression where the filled bookmark icon didn’t display on bookmarked blocks unless hovered on.
* Fixed the `TAB` key not cycling through fields in the Workflow editor under certain circumstances.
* Restored functionality of the keybinding for “New Tab” to work even when no windows are open.

### 2023.09.07 (v0.2023.09.06.18.09)

**Improvements**

* The new tab keyboard shortcut (`CMD-T` by default) can now be re-mapped.
* Warp Drive now shows a loading indicator when syncing.

**Bug fixes**

* The command timestamp tooltip is no longer hidden when the Input Editor is pinned to the top.

### 2023.08.31 (v0.2023.08.29.08.04)

**Improvements**

* You can now delete custom themes from the Warp UI
* You can now scroll to the top or bottom of a selected block from the Command Palette.

**Bug fixes**

* Fixed an issue where CPU was being used up by git processes ([3563](https://github.com/warpdotdev/warp/issues/3563))
* Fixed a Zsh bug where `set sh_word_split` could break Warp's bootstrapping

### 2023.08.24 (v0.2023.08.22.08.03)

**New features**

* Secret Redaction - Warp can now automatically redact secrets and sensitive information in terminal output, including passwords, IP addresses, API keys, and PII. Enable Secret Redaction from the Command Palette or Settings > Privacy > Secret Redaction

**Improvements**

* Special keys used in conjunction with `META` e.g. `META-DELETE` should now work within the alt-screen
* The line height for the text within the Input Editor should now actually change when the custom height in `Settings > Appearance > Text > Line Height` is updated
* Alias Abbreviations in fish should no longer show a red error underline within the Input Editor
* Reduced the bottom padding within the Input Editor when Warp is in Compact Mode

### 2023.08.17 (v0.2023.08.15.08.03)

**New features**

* Warp now displays richer metadata for each command in history, including exit code, working directory, git branch, and whether the command is part of a workflow.
* Warp's native prompt is now customizable directly within the app with drag-and-drop Context Chips (`Settings > Appearance > Prompt`)

**Improvements**

* Warp now supports xterm's escape codes (sequences) for focus reporting
* The Command Palette now supports searching for workflows with their Warp Drive folder name, in addition to the Workflow's name and description.
* Auto-generating custom themes from starting images now work even with a missing `~/.warp/themes` directory
* The "New Workflow" modal now supports more text for longer commands

### 2023.08.10 (v0.2023.08.08.08.04)

**New features**

* Automatically create new themes based on a background image! Click the `+` button in the theme picker (`Settings -> Appearance -> Current Theme`) or search `Open Theme Picker` within the Command Palette

**Improvements**

* Workflows and folders in Warp Drive can now be sorted alphabetically and by last updated
* Multiple JetBrains IDEs are now supported as external editors (e.g. WebStorm, PhpStorm, GoLand)
* The Command Palette now shows which folders a Workflow is in (breadcrumbs)
* Aliases like `...` and `....` no longer incorrectly have an error underline

### 2023.08.03 (v0.2023.08.01.08.05)

**New features**

* Reopen closed tabs with `SHIFT-CMD-T` for up to one minute; configure or disable this feature in `Settings > Features > Enable reopening of closed sessions`
* Autogenerate descriptions for Workflows in Warp Drive using Warp AI

**Improvements**

* Nested folders in Warp Drive can now be collapsed all at once
* Fixed issue where fish abbreviation expansion would include comments
* Fixed a regression with fish history becoming inaccessible

### 2023.07.27 (v0.2023.07.25.08.03)

**Improvements**

* Fixed an issue where $PATH could be overwritten in Bash subshells
* Fixed an issue where completions for file-paths broke when using Named Flags e.g. `ls --color=auto`
* Fixed an issue where Warp Drive objects could get stuck in a sync state
* The down arrow `DOWN` now correctly moves the cursor within Warp AI's text editor

### 2023.07.20 (v0.2023.07.18.08.03)

**New features**

* Can now configure whether `TAB` accepts autosuggestions or opens the completions menu; switch between the configurations via `Settings > Features > Editor`
* Improved completions behavior by improving common prefix detection, and supporting case sensitivity
* Can now natively draw some Unicode block element characters instead of using font glyphs--improves alignment and reduces fuzziness
* Warp's Resource Center now displays new features and improvements

**Improvements**

* Increased the maximum blur radius from 18 to 64

### 2023.07.13 (v0.2023.07.11.08.03)

**New features**

* Warp Drive items that failed to sync can now be retried
* Workflows in Warp Drive drive can now be edited with the workflow execution modal

**Improvements**

* Fixed a bug where git information could sometimes be missing from the prompt
* Adjusted some colors throughout Warp--replaced gradients with solid colors.

### 2023.07.06 (v0.2023.07.04.08.03)

**New features**

* A new AI Command Search experience that allows you to translate natural language to shell commands and integrates directly with workflows! Type '#' in the input to try it out!

**Improvements**

* Fixed a bug where Warp was not recognizing some single character commands and aliases.
* Fixed a bug where command output would sometimes be cut off after finishing (most notably in Gradle).
* Fixed a bug where two prompts could appear for remote Bash sessions

### 2023.06.29 (v0.2023.06.27.19.34)

**New features**

* App links of the form Warp\://launch/\<launch\_configuration\_name> directly open a launch configuration
* Added a new setting for creating new windows with a specific size in terms of rows and columns.

**Improvements**

* Fix rendering of multiple ANSI styles on the same character. This fixes rendering issues commonly encountered in Vim and emacs.
* Fix tabs (indentations) sometimes being inserted into the Input Editor when the completion menu should open.
* Added tooltip for “New tab” button
* The “Launch Configurations” sub-menu (under the Mac File menu) now updates dynamically as launch configurations are added and removed.
* Find bar is able to match double-width unicode characters, including CJK and emojis.
* Fixed a crash that could occur when pasting a command in the workflow editor

### 2023.06.20 (v0.2023.06.20.08.04)

**New features**

* You can now bring the power of your Powerlevel10k (P10K) prompt to Warp! For best results, you’ll need the latest version of P10K; see their GitHub page for upgrade instructions
* Right-side prompts are now supported in Zsh and fish!
* Warp AI commands can now be executed as workflows.

**Bug fixes**

* Clicking on an inactive Warp window now focuses the underlying pane correctly.

### 2023.06.08 (v0.2023.06.13.08.03)

**New features**

* Added a settings page for our upgraded referral system--we’ve added new swag options.
* Right-click a highlighted file path to open a context menu that now supports showing the file in Finder
* The Command Palette can now search through Warp sessions, actions and launch configurations

**Bug fixes**

* The completions menu now supports fish abbreviations
* Fixed an issue where certain aliases would be incorrect after expansion.
* Fixed command search to ignore the extra whitespace before and after the search query
* Restored background Blocks no longer create blank history entries
* Fixed an issue where enabling the “Open completions as you type” setting could sometimes break path completions
* Fixed an issue where Zsh could fail to bootstrap when `$PATH` is an a bad state
* Fixed issue where Warp’s bootstrap logic could leak into Zsh’s history
* Fix issue with properly underlining when hyperlinks are in lists or span across multiple lines

### 2023.06.01 (v0.2023.05.30.08.03)

**New features**

* Right-clicking the New Tab (`+`) button opens a context menu to select saved Launch Configurations
* Use Page Up (`PG-UP`) and Page Down (`PG-DOWN`) in the Command Palette for faster navigation
* Added support for Zed as a default code editor
* Referral counts have been updated to only include referrals who’ve onboarded onto (actually tried) Warp

**Bug fixes**

* Warp’s hotkey window (Quake Mode) now properly retains its size
* Fixed issue where command output would temporarily cutoff when resizing Warp.
* Fixed the Sticky Command Header covering content for pager commands.
* Fixed tabs showing stale text when being renamed.
* Clicking a Mac menu bar item that has a sub-menu no longer incorrectly closes the menu
* Warp now automatically focuses the shortcut search bar when the keyboard shortcuts pane is opened (`CMD-/`)
* Fixed regression where Warp’s native prompt no longer showed the virtual environment

### 2023.05.25 (v0.2023.05.23.08.05)

**Bug fixes**

* Improved shell startup performance after a system restarts for users with Xcode installed
* Fixed issue with Warpifying a pipenv shell subshell from zsh
* Fixed issue with updating the git status prompt indicator in remote subshells

### 2023.05.18 (v0.2023.05.18.01.08)

**New features**

* Warp now supports subshells in Zsh, Bash, and fish for a better experience with Docker, GCP, Poetry, and more. Configure which commands you’d like to “Warpify” under Settings > Subshells

**Bug fixes**

* Fixed an issue with Warp's completions when using flags that start with a single dash e.g. `-namespace`
* Fixed an issue with Synchronized Inputs where switching from alt-screens focused on the incorrect terminal session
* Fixed an issue where command history suggestions could cause Synchronized Inputs to get out of sync

### 2023.05.11 (v0.2023.05.09.08.03)

**New features**

* Warp now sends the output of background shell processes into new (distinct) Blocks--separate from user generated Blocks.
* Synchronize (broadcast) input across multiple panes in a single tab or multiple tabs (`Mac Menu > Edit > Synchronize Inputs` or `Synchronize` within the Command Palette)
* Added option to enable (disabled by default) an audible terminal bell (`Settings > Features > Terminal` or “Enable/Disable Audible Terminal Bell” within the Command Palette)
* Now opens new windows with the same position and size of the most recently closed window (if there is one)
* Fish aliases are now supported in the completions menu

**Bug fixes**

* Support for `SHIFT-UP` and `SHIFT-DOWN` within alt-screen editors
* Fixed incorrect alt-screen scrolling behavior when scroll reporting is enabled
* `SHIFT-TAB` now (correctly) sends the ANSI (backward-tab) escape sequence (for Vim and NeoVim)
* SSH wrapper now also loads your /etc/profile and supports login-like prompts and interactions like printing the message of the day (MOTD)

### 2023.05.04 (v0.2023.05.02.08.03)

**New features**

* Indicate when Warp is downloading an update in Settings > Account > About Warp
* Support alias expansion for bash/zsh aliases

### 2023.04.27 (v0.2023.04.25.08.05)

**New features**

* Support for Fish abbreviations
* Right-click within the Input Editor to open a context menu where you can split panes, etc.

**Bug fixes**

* Starting a command with whitespace in the Workflow creation dialog no longer breaks its argument parser
* Fixed a bug when commands were aliased to `comm` because of a naming clash with Warp's wrapper
* `Cut word left` (`CTRL-W`) and `Cut word right` (`OPT-D`) now use the shell clipboard instead of the system clipboard

### 2023.04.13 (v0.2023.04.11.08.03)

**New features**

* Navigation by subword within the Input Editor with `CTRL-OPT-LEFT` and `CTRL-OPT-RIGHT`
* View prior Warp AI questions using the `UP` arrow even after the transcript is cleared

**Bug fixes**

* Fixed a bug in proxied SSH while not on the default shell
* Background blur now also applies to windows that are opened via drag-and-drop from Finder
* The Sticky Command Header no longer cuts off text for pagers

### 2023.04.06 (v0.2023.04.04.08.03)

**New features**

* The position of the input and direction of the terminal output are now configurable. You can start the input at the top and have it move down as new commands are run (to clear the screen and reset the position press `CTRL-L`, `CMD-K` or type `clear`). Or you can keep the input pinned to the top of the pane and have terminal outputs flow in reverse order. Settings are available under `Settings > Appearance > Input Position`
* Added a button for “jumping to the bottom” of the currently hovered Block to make it easy to get to the bottom of an output. Configurable with a setting under `Settings > Appearance > Blocks`
* Warp AI transcripts can now be navigated via keyboard (`UP` / `DOWN` arrows)
* Added a right-click context menu in the alt-screen (that still respects mouse reporting and SGR\_MOUSE)
* Warp AI's past prompts can be accessed via `UP` (arrow)
* `CMD-ENTER` within Warp AI now inputs the selected command into the Input Editor

**Bug fixes**

* Workflows can now be searched by their description in Command Search
* Consolidated “Ask Warp AI” keybindings into one
* Fixed an issue causing “Move cursor by word” and “Select left/right by word” to not work if “Left/Right Option key is Meta” is enabled
* Can now unset cursor navigation bindings within an executing command

### 2023.03.30 (v0.2023.03.28.08.03)

**New features**

* Warning if a known-incompatible custom prompt is detected
* Keybindings for cursor navigation in REPLs and subshells, e.g. ⌥←, ⌥→, ⌥⌫, ⌘←, ⌘→, ⌘⌫, ⌘fn⌫

**Bug fixes**

* Fixed an issue where an input suggestion tooltip could overflow outside the visible window
* Fixed keybinding conflict with Warp AI
* Fixed completion and syntax highlighting when local paths contain separators, not in the prefix

### 2023.03.23 (v0.2023.03.21.08.02)

**New features**

* Added VSCode Insiders as a supported code editor
* Added completions for pnpm.

**Bug fixes**

* Fixed an issue where AI command results with multiple commands would all render on the same line
* The configurable width of Universal Search is now persistent (doesn’t reset to default in new sessions).
* “Copy Prompt” now correctly respects your PS1 prompt, if enabled
* Fixed automatic command corrections for cargo.

### 2023.03.20 (v0.2023.03.14.08.03)

**New features**

* Added support to configure which shell Warp should use when starting a terminal session. Configurable under Settings -> Features -> Session.
* Tabs can now be renamed via mouse double-click.

**Bug fixes**

* Launch configuration templates now support use of `~` in the `cwd` field.
* Double-clicking a button/tab in the title bar no longer resizes the whole window.
* Context menus in the blocklist are now more pronounced and easier to dismiss by clicking.
* Increased the clickable area of small search boxes.
* A keyboard shortcut can now be registered to clear all blocks.
* Fixed some locale-related issues due to use of `LC_ALL` environment variable.
* Xterm escape code OSC 4 (“change color”) no longer crashes the app when it appears in PS1.
* Fixed a crash that occurs when resizing windows after dismissing a notification banner.
* Fixed crash that occurs if you unset the keybinding for the keyboard shortcuts side panel.
* Added Warp AI to resource center.

### 2023.03.16 (v0.2023.03.07.08.02)

**New features**

* Introducing Warp AI ⚡ Get explanations for errors and outputs, ask for help with complicated workflows and scripts, easily execute suggested commands, all without leaving Warp!

### 2023.03.09 (v0.2023.03.07.08.02)

**New features**

* Added support for clearing a keybinding for an action [2300](https://github.com/warpdotdev/warp/issues/2300).
* Added support for showing/hiding Warp windows with a system-wide Activation hotkey [2585](https://github.com/warpdotdev/warp/issues/2585).
* Improved scroll speed for Sidebar menu 'Warp Essentials'/'Keyboard Shortcuts' [2673](https://github.com/warpdotdev/warp/issues/2673).
* Users may now set a custom keybinding to open the completions menu.
* Enabling/disabling mouse reporting is no longer bound to CMD-R by default.
* Toggling mouse reporting enabled shows a banner.

**Bug fixes**

* Fixed SSH wrapper hanging forever when SSH host is Arch Linux with the latest bash package [2636](https://github.com/warpdotdev/warp/issues/2636).
* Fixed Bash commands having escape codes in the last 20 characters producing incorrect output.
* Fixed a bug with bash prompt expansion on recent macOS versions.

### 2023.02.28 (v0.2023.02.28.08.03)

**New features**

* Warp now suggests a URL for creating a GitHub PR on `git push`.
* Command Search and Workflow menus are now horizontally resizable.

**Bug fixes**

* Fixed a bug where Warp doesn’t correctly Auto-Raise.
* Fixed issue where formatting is lost when pasting into nano.
* Fixed issue where Warp doesn’t detect process termination when exiting `info`.
* Fixed a bug with bash prompt expansion not working on v4.4 or earlier.
* Fixed a bug where profile pictures don’t show in the Account menu.
* Fixed Syntax Highlighting and Error Underlining’s handling of multi-byte characters.
* Fixed issue where 'Checking for Update’ doesn’t reflect the current status.

### 2023.02.23 (v0.2023.02.21.08.03)

**New features**

* Support for configuring the initial working directory for new sessions. New tabs/windows/split panes can have separate configurations, or you can set one value for all new sessions.

**Bug fixes**

* Warp now supports syntax highlighting and error underlining for multi-line inputs with multibyte characters
* Fixed a bug where the update status in Warp’s `About Section` was incorrect.
* Improved GPU memory consumption when multiple windows are open.

### 2023.02.16 (v0.2023.02.14.08.05)

**New features**

* Improved double-click selection. Double-clicking text now smart selects patterns like file paths, URLs, email addresses, etc. - [659](https://github.com/warpdotdev/warp/issues/659)
* Warp can now be opened from Finder - [102](https://github.com/warpdotdev/warp/issues/102)

**Bug fixes**

* Warp no longer hangs after exiting the alt-screen--having searched for text using Find.
* The Block-list now scrolls to the correct position after returning from the alt-screen.
* Clicking above the scroll-bar no longer (incorrectly) changes its scroll position.
* The terminal cell dimensions now update immediately after modifying the Font size.
* Hyperlinks no longer incorrectly highlight on hover when Warp is not focused.
* The Input Method Editor (non-English keyboards) is now positioned correctly in the alt-screen and in running Blocks
* When there are no windows open, clicking `New Tab` from the Mac menu will create a new window

### 2023.02.09 (v0.2023.02.07.08.03)

**Bug fixes**

* Warp now sets the Mac window title; right-clicking on the dock icon will show the name of the active tab.
* Fixed a bug where navigating the theme picker with the arrow keys would lead to a crash when no theme matches the search.
* The Input Editor now refocuses correctly after clicking hyperlinks.
* Custom keybindings incorporating the `SPACE` key now persist after closing Warp.
* The Input Method Editor (non-English keyboards) now positions itself within the Input Editor

### 2023.02.02 (v0.2023.01.31.08.08)

### 2023.01.26 (v0.2023.01.24.08.03)

**New features**

* Warp can now dim inactive terminal panes, navigate to `Settings > Appearance > Panes > Dim inactive panes`

**Bug fixes**

* Fixed crash when selecting multiple occurrences of multi-byte characters using `CTRL-G`

### 2023.01.19 (v0.2023.01.17.08.03)

**New features**

* The current Git branch can now be copied using the Command Palette (`CMD-P`)

**Bug fixes**

* Fixed bug where some keybinding actions would be applied to the wrong terminal pane.
* Warp now checks the input values for font size and line height and ignores them if they are too small or large
* The `missing update permissions banner`, can now be dismissed
* Fixed a rare crash when closing panes created by a launch configuration

### 2023.01.12 (v0.2023.01.10.08.02)

**New features**

* Support setting window background transparency and blur radius, via sliders under `Settings > Appearance`
* Revamped resource center! Click the Warp icon in the top right to see keyboard shortcuts and learn how to best use Warp
* Quit modal: Quitting or closing Warp while a session is running triggers a warning prompt–that also lets you view which sessions are running
* Added a toggle to disable cursor blinking

**Bug fixes**

* Can now support completions that have escaped paths
* Can now support background images with paths that start with \~
* Can now properly restore a Warp window’s position when using multiple monitors
* Commands from restored sessions run on the local machine no longer appear in the SSH server’s history
* Fixed issues SSHing into RHEL/Fedora machines with PackageKit-command-not-found installed
* Fixed incorrect handling of `->` as the user's prompt
* Fixed ls completions when using the --color option

### 2023.01.05 (v0.2023.01.03.08.03)

**Bug fixes**

* Trailing periods are no longer considered part of a URL.
* Fixed regression where the "autocomplete symbols" setting was not being respected.

### 2022.12.15 (v0.2022.12.13.08.04)

**New features**

* You can now reorder and drag tabs around with your mouse!

**Bug fixes**

* The welcome Block now also works when using Fish shell.
* AI Command Search no longer crashes from multi-byte characters when opened via the `#` prefix
* Warp no longer crashes when starting a new session in a deleted or inaccessible directory
* Resolved rendering bugs and hangs in full-screen applications like 'k9s' and 'less'.
* Added a login failure notification.

### 2022.12.06 (v0.2022.12.06.08.03)

**New features**

* Users may now opt out of telemetry (app analytics and crash reporting)
* Added 'Tail Warp network log' workflow for viewing logs of all app network activity.

**Bug fixes**

* Full-screen CLI commands like mitmproxy now correctly span the entire view.
* Improved styling and organization of Features page in settings.
* Completions While Typing menu closes while generating new results.
* Added a hidden completion result for root dir.
* Warp now consumes less memory when a session has many blocks.
* Fixed an issue over SSH where logs were being inserted into input.

### 2022.12.02 (v0.2022.11.29.08.03)

**New features**

* Users may now opt out of telemetry (app analytics and crash reporting)
* Added 'Tail Warp network log' workflow for viewing logs of all app network activity.

**Bug fixes**

* Mitigated an issue where running a command over SSH would emit spurious output (specifically, 'channel: open failed' statements) in a block.

### 2022.12.01 (v0.2022.11.29.08.03)

**New features**

* Warp now supports using the find bar within the alt-screen! `CMD-F` now opens find within vim, less, and other alt-screen apps!

**Bug fixes**

* Respect symlinks in Warp configuration directories (for themes and workflows).
* Fixed unwanted text appearing in the Input Editor when RPROMPT is set
* Fixed the emoji composer not working properly.
* Fixed a crash that could occur when using the Unicode Hex Input keyboard.
* Fixed escape binding not closing the resource center
* Move Backward/Forward One Word bindings can now be overridden.
* Fixed crash when hovering over multiple byte text within the Input Editor
* Fixed “command not found: sed” and “command not found: tr” issues with the SSH wrapper.
* Fixed issue where tab completions and command search could be visible at the same time.

### 2022.11.15 (v0.2022.11.14.14.55)

**New features**

* Command Search: Ctrl-R opens a panel where you can search your history, workflows, and other command execution-related items, all in one place.
* Sticky command header: Warp now pins the prompt/command section of a Block to the top of the screen; click it to scroll to the top of the Block. Can be toggled via Settings > Features > Show Sticky Command Header
* Warp’s Input Editor now supports soft wrapping; long commands are now fully visible!

**Bug fixes**

* Warp now sets the TERM\_PROGRAM environment variable correctly in wrapped SSH sessions.

### 2022.11.10 (v0.2022.11.08.08.07)

**New features**

* Warp now offers Command Corrections! Warp will suggest corrections for errors in previous console commands
* Warp now also detects invalid file paths -- they are underlined red when error underlining is enabled
* Added a toggle in `Settings > Appearance` to configure whether and how Warp enforces minimum contrast

**Bug fixes**

* Fixed an issue where toggling the default prompt would not update it immediately
* Improved positioning of the `TAB` completions menu when using split panes

### 2022.11.03 (v0.2022.11.01.08.03)

**New features**

* Warp's prompt now shows the number of modified files on your local git branch! Search "changed file count" in the Command Palette or right-click the Prompt to toggle.

**Bug fixes**

* Dim-styled colors are now restored properly.

### 2022.10.27 (v0.2022.10.25.08.06)

**Bug fixes**

* Fixed a bug when hovering over hover icons

### 2022.10.20 (v0.2022.10.18.08.10)

**Bug fixes**

* Modifying the mouse and scroll reporting settings now applies immediately
* Fixed cursor not blinking when starting a shell instance
* Fixed temporarily flashing the wrong prompt while Warp is still bootstrapping
* Removed duplicate entry for toggling error underlining and syntax highlighting within the Command Palette

### 2022.10.13 (v0.2022.10.11.08.13)

**New features**

* Warp’s Input Editor now has Syntax Highlighting and Error Underlining, with no configuration!
* Warp now uses a pointer cursor when hovering over links

**Bug fixes**

* Git branches in the completions menu now bold correctly
* Warp no longer crashes when `/bin/bash` is missing

### 2022.10.06 (v0.2022.10.04.08.05)

**New features**

* Drag and drop a folder or file onto the Warp dock icon to open a new tab in this directory
* Added dividers between Blocks in compact mode
* Shell keywords are now supported for completions and Command Inspector

**Bug fixes**

* Accessibility support for context menu keybinding
* Keystrokes typed while a command is still executing no longer gets dropped
* Link recognition no longer includes trailing quotes
* Find search results will continue to be highlighted after clearing the screen during a long running command
* Fixed completions for commands prefixed with environment variables
* Warp’s resource center is now center aligned

### 2022.09.29 (v0.2022.09.27.08.11)

**New features**

* Extend the currently selected text (within Blocks) with `SHIFT-LEFT`, `SHIFT-RIGHT`, `SHIFT-UP`, and `SHIFT-DOWN`
* Double-click and drag to select text in the Input Editor
* Insert the last word of the previous command with `META-.`
* Added a toggle to enable mouse and scroll reporting to the settings dialog (`Settings > Features`)

**Bug fixes**

* The `clear` command no longer appears in the snackbar at the top of the window
* Warp’s completions now support executables in remote sessions (no longer just bash)
* Fixed subcommand completions for commands with proper prefixes of each other (e.g. `npm r` and `npm run`)
* The completion spec for `lsd` now supports files

### 2022.09.22 (v0.2022.09.20.08.08)

**New features**

* After selecting a Block press `CTRL-M` to open its context menu
* Commands in the tab completions menu and history menu can now be executed directly with `CMD-ENTER`
* Completions now support shell builtins, git aliases, and also npm aliases

**Bug fixes**

* Command Palette now includes the most useful features at the top
* Improved flag completions for cargo

### 2022.09.15 (v0.2022.09.13.08.15)

**New features**

* Warp Resource Center - explore Warp features and documentation by clicking the `?` icon or pressing `SHIFT-CTRL-?`
* New icons in the completion menu denoting flags, folders, branches, etc.

**Bug fixes**

* Press `CMD-ENTER` within the history menu (`CTRL-R`) to directly execute the highlighted command
* Fixed crash when opening many tabs (due to MacOS’s default open file descriptor limits)
* Fixed crash when laying out RTL text

### 2022.09.08 (v0.2022.09.07.14.56)

**New features**

* Global hotkey window can now float above full-screen apps
* Tabs can now have their color customized (via right-clicking on a tab)
* Terminal line height is now configurable (via Settings > Appearance)

### 2022.09.01 (v0.2022.08.31.18.11)

**New features**

* Tab completions now support fuzzy string matching
* Improve completions for over 450 commands, including docker, kubernetes, cargo, node, and git

**Bug fixes**

* Properly send C0 control codes for \<ctrl-\[2-8]> keystrokes
* Session restoration now also persists bold, underline, italic, and strikethrough formatting
* Inspect mode now works for the changelog modal
* Fixed a crash when highlighting a link
* Fixed Find occasionally returning only partial results
* Fixed occasional crash when loading images
* Fixed display issue in the Mac Menu for keyboard shortcuts with special keys

### 2022.08.25 (v0.2022.08.23.08.06)

**New features**

* Experimental feature: support for always-on completions — the completions menu can now open automatically while typing (enable via Settings -> Features)

**Bug fixes**

* Custom tab titles no longer get overwritten when using multiple panes
* A Block’s execution duration is now formatted in hours, minutes, and seconds
* Improved rendering of the ‘Current session’ text in the Navigation Palette
* Warp properly hides the cursor when a CLI sends the respective escape sequence
* Warp stays focused (keyboard-interactive) after closing the Share Block menu and the context menu
* Warp no longer lags when the Ctrl-R menu is opened
* Confirming a tab suggestion appends a space to the buffer

### 2022.08.18 (v0.2022.08.16.10.16)

**New features**

* Launch Configurations - Save a configuration of windows, tabs, and panes to open later with `CTRL-CMD-L`
* Session Navigation - Navigate to any session in Warp with `SHIFT-CMD-P`
* Added exclusive theme for users who joined Warp through a referral

**Bug fixes**

* Prompt now shows Git SHA instead of HEAD when you’re not on a branch
* Filepath completions now include current directory ('.') and parent directory ('..')
* Support `SHIFT-HOME` and `SHIFT-END` keybindings to select text to line start and end.
* Items in the Command Palette now highlight when you hover over them with your mouse
* Improved how Warp cleans up the warptmp directory for Zsh SSH sessions
* Already open dropdown menus are now properly closed when clicked
* Warp no longer crashes when dragging a window that’s running htop
* Warp no longer crashes when the find bar is open

### 2022.08.10 (v0.2022.08.08.09.21)

**New features**

* Can now Middle-click a tab to close it
* Added additional tab reordering options (Close: tab, other tabs, and tabs to the right) via the Mac Menu, the Command Palette, and a tab’s context menu (right click)

**Bug fixes**

* Added a toggle to the Mac Menu for maximizing panes
* Can now switch panes using keyboard shortcuts even when a pane is maximized
* Add support for opening file paths with RubyMine, PhpStorm, and WebStorm
* Fixed crash when highlighting links
* Fixed issue where the HISTCONTROL environment variable was ignored in bash
* Pressing `CTRL-R` to open history search no longer crashes Warp when you have multiple cursors

### 2022.08.03 (v0.2022.08.01.09.12)

**New features**

* Updated Mac menus to make Warp actions more discoverable - [101](https://github.com/warpdotdev/warp/issues/101)
* Warp now supports opening file links and urls via CMD-CLICK! - [177](https://github.com/warpdotdev/warp/issues/177)

**Bug fixes**

* Various CLI tools no longer hang e.g. Bazel and Maven
* Command Inspector hover no longer crashes with UTF-8 encoded strings
* Opening the find / search bar (`CMD-F`) now automatically selects the text
* Tab titles are no longer reset when changing panes

### 2022.07.27 (v0.2022.07.25.09.05)

**Bug fixes**

* Closing and re-opening the Command Palette now resets the selected item
* The cursor’s position is now restored after exiting the Command History Search (`CTRL-R`) menu.
* Shorthand and longhand flags are now correctly surfaced (based on the number of dashes) in tab completions
* Added voiceover support for `BACKSPACE` and `DELETE` keystrokes within the Input Editor

### 2022.07.20 (v0.2022.07.18.09.06)

**New features**

* Command Inspector - hover over any piece of a command in Warp’s Input Editor to surface documentation or press `CMD+I` to inspect at the cursor’s current location
* Improved ordering in the tab completions menu

**Bug fixes**

* Font color for links in light mode (themes) now set correctly
* Moving forward by a word no longer moves farther than expected
* Warp no longer hangs when passing an invalid file path
* Fixed issues with persisting the selected theme when “Sync with OS” is enabled and the theme picker is launched from the Command Palette (or a keyboard shortcut)
* Fixed issues with text input after clearing Blocks (`CMD-K`) while in a REPL environment.
* Fixed shortcut for select-left-by-word (`SHIFT-CMD-B`), select-right-by-word (`SHIFT-CMD-F`), select-line-to-end (`SHIFT-CTRL-E`), and select-line-to-start (`SHIFT-CTRL-A`)

### 2022.07.13 (v0.2022.07.11.09.11)

**Bug fixes**

* Improved startup time for Fish shells
* Find Bar no longer crashes on selected text
* Scrollbar now supports jumping to where you click
* Fixed a bug with the referral link for sharing Warp not loading

### 2022.07.07 (v0.2022.07.04.09.08)

**New features**

* Bookmark a Block (or multiple) for quick access via the scroll-bar
* Added a referral counter to the Settings > Account screen and the referral screen
* Added support for rendering text with a lower visual weight; enable the thin strokes option in Settings > Appearance (enabled by default for low-DPI displays)
* Togglable settings, overflow menu items, and settings pages are now accessible through the Command Palette
* CLI options are now surfaced by default without needing to type '-'
* Press SHIFT-CMD-C while in VSCode (Visual Studio Code) to open a new Warp session

**Bug fixes**

* Fixed referal links and share by email
* Fixed a hang that would sometimes occur when connecting with SSH
* Now support requesting media permissions (camera, audio, etc)
* Correctly parse Git commit SHAs in completion menus
* Improved tab completion support for command line arguments that are behind flags

### 2022.07.06 (v0.2022.07.04.09.08)

**New features**

* Bookmark a Block (or multiple) for quick access via the scroll-bar
* Added a referral counter to the Settings > Account screen and the referral screen
* Added support for rendering text with a lower visual weight; enable the thin strokes option in Settings > Appearance (enabled by default for low-DPI displays)
* Togglable settings, overflow menu items, and settings pages are now accessible through the Command Palette
* CLI options are now surfaced by default without needing to type '-'
* Press SHIFT-CMD-C while in VSCode (Visual Studio Code) to open a new Warp session

**Bug fixes**

* Fixed a hang that would sometimes occur when connecting with SSH
* Now support requesting media permissions (camera, audio, etc)
* Correctly parse Git commit SHAs in completion menus
* Improved tab completion support for command line arguments that are behind flags

### 2022.06.29 (v0.2022.06.27.09.14)

**Bug fixes**

* Cursor changes when hovering over clickable UI elements and the Input Editor
* Dim colors now render correctly

### 2022.06.27 (v0.2022.06.20.09.15)

**New features**

* Improved auto-focus behavior when closing panes by keeping track of history when navigating or clicking around panes
* Performance improvements when executing Blocks: Warp no longer flashes on every command!

**Bug fixes**

* Input Editor re-focuses after renaming a tab
* Reduced visual weight of the active tab title to improve legibility.
* Improved blending along the inside edge of rounded corners
* Global Hotkey Windows (Quake Mode) now correctly respect the active screen setting
* Completions for flag arguments now support absolute and relative file paths (when applicable)
* Git checkout <`TAB`> now also completes branches with the remote prefixed.
* Pressing Arrow-up (`UP`) when the Input Editor is non-empty opens the command history with prefix filtering
* Button to copy app version moved to main settings page

### 2022.06.22 (v0.2022.06.20.09.15)

**New features**

* Improved auto-focus behavior when closing panes by keeping track of history when navigating or clicking around panes
* Performance improvements when executing Blocks: Warp no longer flashes on every command!

**Bug fixes**

* Input Editor re-focuses after renaming a tab
* Reduced visual weight of the active tab title to improve legibility.
* Improved blending along the inside edge of rounded corners
* Global Hotkey Windows (Quake Mode) now correctly respect the active screen setting
* Completions for flag arguments now support absolute and relative file paths (when applicable)
* Git checkout <`TAB`> now also completes branches with the remote prefixed.
* Pressing Arrow-up (`UP`) when the Input Editor is non-empty opens the command history with prefix filtering
* Button to copy app version moved to main settings page

### 2022.06.17 (v0.2022.06.13.09.15)

**New features**

* Added keyboard shortcuts to reorder tabs (CTRL-SHIFT-LEFT and CTRL-SHIFT-RIGHT)

**Bug fixes**

* Warp no longer crashes on MacOS 13 (Ventura)
* Global Hotkey Window (Quake Mode) no longer overlaps Spotlight, Raycast, Alfred, and the Mac Dock
* Now correctly display the user and hostname in the Prompt after exiting an SSH session
* Fixed a memory leak on window close.

### 2022.06.15 (v0.2022.06.13.09.15)

**New features**

* Added keyboard shortcuts to reorder tabs (CTRL-SHIFT-LEFT and CTRL-SHIFT-RIGHT)

**Bug fixes**

* Global Hotkey Window (Quake Mode) no longer overlaps Spotlight, Raycast, Alfred, and the Mac Dock
* Now correctly display the user and hostname in the Prompt after exiting an SSH session
* Fixed a memory leak on window close.

### 2022.06.08 (v0.2022.06.06.09.05)

**New features**

* Now support renaming tabs (right click on your tab title!)
* Now support enabling custom prompt from prompt context menu (right-click on prompt)
* Now support splitting panes (left and right) from the context menu (right click) and through the Command Palette
* Now support CTRL-Click as an alternative to right-clicking

**Bug fixes**

* Improved completions support for arguments nested under options (e.g. git branch -D \<branch\_name...>)
* Modified files are now included (in addition to commit SHAs) for `git diff`

### 2022.06.01 (v0.2022.05.30.09.10)

**New features**

* Added information about rewards to the referral screen
* Added a button that toggles regex search in the Find Bar
* Added completion support for shell functions

**Bug fixes**

* Hotfix - a regression that caused Warp to stall when using nano
* Improved kerning (font rendering) throughout the app
* Added a hyperlink (to our changelog history) in the Changelog modal
* Multiline commands that don't have any output are no longer cut off

### 2022.05.26 (v0.2022.05.23.09.07)

**New features**

* Warp can now send you desktop notifications for long-running commands and password prompts - [628](https://github.com/warpdotdev/warp/issues/628)
* Added keybinding to toggle fullscreen mode

**Bug fixes**

* Stopped prepending \ before \~ in tab titles for older versions of Bash
* Added support for CMD-G and SHIFT-CMD-G to tab between results in the Find Bar

### 2022.05.18 (v0.2022.05.16.09.01)

**New features**

* Added exclusive theme available to anyone who has referred someone to Warp. (Open Theme Picker > Warp Referral to use it)

**Bug fixes**

* Improved rendering of rounded corners throughout the app
* Fixed cell dimension computation for some fonts
* Fixed labels rendering incorrectly in the font selector dropdown in settings
* Fixed Bash remote sessions missing tab titles
* Reduced UI flickering after executing commands
* Fixed errors when sshing into remote machines which do not have xxd available
* Fixed some anti-aliased glyphs getting clipped during rasterization
* Fixed search bar stealing focus after command execution

### 2022.05.11 (v0.2022.05.09.09.06)

**New features**

* Filepath completions without needing to cd
* Support for any font (not just monospaced)

**Bug fixes**

* Tab completions (cd) with international characters are now properly escaped (edited)
* Improve rendering performance when many tabs are open (fixes non-responsiveness when searching history)
* Fixed a race condition with autoupdate a11y announcements and other a11y messaging
* Fixed a regression that would cut off the output of some long-running Blocks

### 2022.05.04 (v0.2022.05.02.09.00)

**New features**

* Added default tab titles for Bash
* Improved default tab title in Zsh
* Maximize a split pane
* Support rcfiles that check PS1 to determine if it's an interactive shell; this may explain missing aliases or commands in Warp!

**Bug fixes**

* History now correctly shows results after hitting ESC when a Block is focused
* Fixed crash when quitting AI Command Search while a command was being generated
* Global keybindings with function keys and numeric keys are now properly registered
* Warp no longer jumps up and down for single-line commands that take more than 50ms

### 2022.05.02 (v0.2022.04.25.09.59)

**New features**

* Added a Quake Mode setting that configures whether Warp should automatically hide when losing focus - [1077](https://github.com/warpdotdev/warp/issues/1077)
* Added a Quake Mode setting that configures which screen to pin Warp on - [862](https://github.com/warpdotdev/warp/issues/862)
* Expanded the keybindings supported by Quake Mode / Global Hotkey Window - [856](https://github.com/warpdotdev/warp/issues/856)

**Bug fixes**

* Commands prepended with space are now stored in history if hist\_ignore\_space option is not set
* Now support dotfile configurations with non-English quotation marks
* Continued improving the reliability of login and auth within the app
* Improved performance for commands with large outputs
* Improved performance for long running commands
* Improved text alignment within inline banners

### 2022.04.27 (v0.2022.04.25.09.59)

**New features**

* Added a Quake Mode setting that configures whether Warp should automatically hide when losing focus - [1077](https://github.com/warpdotdev/warp/issues/1077)
* Added a Quake Mode setting that configures which screen to pin Warp on - [862](https://github.com/warpdotdev/warp/issues/862)
* Expanded the keybindings supported by Quake Mode / Global Hotkey Window - [856](https://github.com/warpdotdev/warp/issues/856)

**Bug fixes**

* Commands prepended with space are now stored in history if hist\_ignore\_space option is not set
* Now support dotfile configurations with non-English quotation marks
* Continued improving the reliability of login and auth within the app
* Improved performance for commands with large outputs
* Improved performance for long running commands
* Improved line height computation for some fonts
* Improved text alignment within inline banners

### 2022.04.20 (v0.2022.04.18.09.08)

**New features**

* Support logging into Warp by pasting the auth url when "Take me to Warp" fails in browser

**Bug fixes**

* Improved reliability of login and auth within the app
* Buttons within the find bar are now properly shaded for gradient themes
* Workflows with default values are now registered by Warp
* Fixed bootstrapping bug that affected Fish versions older than 3.2.0
* Fixed a memory leak that occurred when new tabs were opened or panes were split

### 2022.04.15 (v0.2022.04.11.09.09)

**Bug fixes**

* Support parsing PS1’s exit codes (Bash’s $?) and improved PS1 parsing for newer Bash versions (4.4+)
* Fixed prompt showing up as exit in Bash - [793](https://github.com/warpdotdev/warp/issues/793)
* Improved parsing of Zsh default prompts
* Opening the find bar will automatically select any existing text - [831](https://github.com/warpdotdev/warp/issues/831)

### 2022.04.13 (v0.2022.04.11.09.09)

**Bug fixes**

* Support parsing PS1’s exit codes (Bash’s $?) and improved PS1 parsing for newer Bash versions (4.4+)
* Fixed prompt showing up as exit in Bash - [793](https://github.com/warpdotdev/warp/issues/793)
* Improved parsing of Zsh default prompts
* Opening the find bar will automatically select any existing text - [831](https://github.com/warpdotdev/warp/issues/831)

### 2022.04.08 (v0.2022.04.04.09.07)

**Bug fixes**

* Block sharing dialog now scrolls properly

### 2022.04.01 (v0.2022.04.01.01.37)

**New features**

* Warm welcome!
* A.I. Command Search

**Bug fixes**

* Warp now properly registers `SPACE` and `SHIFT` modifier keys for Global Hotkey Windows
* Page Up and Page Down keys now work correctly in vim and other fullscreen apps - [560](https://github.com/warpdotdev/warp/issues/560)
* SSH now supports bootstrapping if bash-preexec is included in a Debian VM’s system rcfiles (eg by default at Google) - [578](https://github.com/warpdotdev/warp/issues/578)
* Corrected keyboard shortcut for split pane in context menu

### 2022.03.30 (v0.2022.03.29.02.23)

**New features**

* Workflows: an easier way to share, parameterize, and execute commands - [625](https://github.com/warpdotdev/warp/issues/625)
* Quake mode / Focus Warp with a Global Hotkey - [091](https://github.com/warpdotdev/warp/issues/091)

**Bug fixes**

* Magnet, Swish and ALT-Tab window managers now work with Warp - [776](https://github.com/warpdotdev/warp/issues/776)
* SSH now handles control master connection errors - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH now handles verbose mode, no longer leaks into the Input Editor as a typeahead - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH now boots normally for POSIX shells that aren’t supported by Warp’s wrapper - [578](https://github.com/warpdotdev/warp/issues/578)

### 2022.03.24 (v0.2022.03.23.22.10)

**New features**

* Fish support - [190](https://github.com/warpdotdev/warp/issues/190)
* Basic screenreader support (Voiceover) - Warp is now an accessible terminal!
* Added a toggle in the settings to disable the SSH wrapper - [821](https://github.com/warpdotdev/warp/issues/821)

**Bug fixes**

* Hitting tab with a text selection shows tab completions instead of indenting
* SSH no longer hangs when /tmp is not writable for Zsh - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH no longer bootstrap the shell if it’s not meant to be an interactive session (e.g. if -T or a command is passed) - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH now supports Starship and Zsh's $PROMPT variable - [803](https://github.com/warpdotdev/warp/issues/803)
* Also import themes in subdirectories e.g. `~/.warp/themes/subdirectory/theme.yaml`

### 2022.03.16 (v0.2022.03.14.08.49)

**New features**

* Multi-block selections and corresponding actions - [146](https://github.com/warpdotdev/warp/issues/146)
* Case-sensitive search

**Bug fixes**

* SSH no longer returns 0\~ and 1\~ after executing commands for Zsh 5.0.8 or older - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH now supports LocalCommand / RemoteCommand - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH over Zsh no longer depends on configuring locales on the remote machine - [578](https://github.com/warpdotdev/warp/issues/578)
* SSH sources /etc/bash.bashrc which is an extra rcfile in Debian and other Linux distributions - [578](https://github.com/warpdotdev/warp/issues/578)
* Improved completions stability when there are multiple panes on the same remote machine
* Vim and other alt-screen apps properly expand to take up the full window - [552](https://github.com/warpdotdev/warp/issues/552)
* Clicking into Warp from other foreground window focuses the clicked pane - [739](https://github.com/warpdotdev/warp/issues/739)
* Warp now respects ignore-space history options for Zsh and Bash - [044](https://github.com/warpdotdev/warp/issues/044)
* Warp now creates a \~/.warp folder to persist custom keybindings - [801](https://github.com/warpdotdev/warp/issues/801)

### 2022.03.09 (v0.2022.03.07.08.51)

**Bug fixes**

* Added missing actions to Command Palette
* Option is meta is now in the settings menu
* Fix for SSH hanging when Zsh is the remote login shell
* Fix for SSH with Zsh that would break with certain rcfiles because of incorrectly set ZDOTDIR

### 2022.03.02 (v0.2022.02.28.08.45)

**New features**

* Can now edit the keybindings for arrow navigation (Up/Down/Left/Right)
* Can now edit the keybindings for activating specific tabs (by number CMD-1, CMD-2, …)

**Bug fixes**

* Crash in theme chooser
* Fix for tab completion sometimes deleting characters

### 2022.02.23 (v0.2022.02.21.08.55)

**New features**

* Zsh support over SSH
* Partially complete autosuggestion (by word) using CTRL-RIGHT and ALT-RIGHT - [488](https://github.com/warpdotdev/warp/issues/488)
* Added a Copy URL menu item after right-clicking a URL - [154](https://github.com/warpdotdev/warp/issues/154)
* Indicator for conflicting keybindings in keyboard customization UI

**Bug fixes**

* Able to fill-in longest common prefix after filtering tab completions - [618](https://github.com/warpdotdev/warp/issues/618)
* Block completion causes Input Editor to steal focus from find bar - [452](https://github.com/warpdotdev/warp/issues/452)
* UP-arrow in history menu sometimes scrolls more than one item
* CMD-F opens a no-op find bar in alt screen

### 2022.02.16 (v0.2022.02.14.08.44)

**New features**

* Customizable key bindings (accessible via the settings menu) - [579](https://github.com/warpdotdev/warp/issues/579)
* Users can opt in to use their shell’s prompt rather than Warp’s default (select the Honor PS1 toggle under the settings menu) - [580](https://github.com/warpdotdev/warp/issues/580)
* Added a timestamp showing Block runtime duration; hover to see start and end date + time - [178](https://github.com/warpdotdev/warp/issues/178)
* CTRL-F now accepts autosuggestions - [403](https://github.com/warpdotdev/warp/issues/403)
* CTRL-E and CMD-RIGHT accept autosuggestions when at the end of the buffer - [403](https://github.com/warpdotdev/warp/issues/403)
* Allow input height to expand to half the pane height - [621](https://github.com/warpdotdev/warp/issues/621)

**Bug fixes**

* Arrow key presses now (up and down now) cycle themes in the theme picker - [294](https://github.com/warpdotdev/warp/issues/294)
* ESC keypress now exits the theme picker
* CMD-Down when on most recent block to focus input now clears Block selection
* Fixed a bug where resizing a pane while a command was running made it impossible to scroll to the bottom of the pane
* Fixed a bug where resizing a pane could cause Warp to show a blank screen
* Parentheses, quotes, and brackets now also auto-close after typing an alphanumeric character
* Remapped multi-cursor key bindings to CTRL-SHIFT-UP and CTRL-SHIFT-DOWN - [374](https://github.com/warpdotdev/warp/issues/374)
* Restored OPT-CMD-UP and OPT-CMD-DOWN for switching panes up and down - [730](https://github.com/warpdotdev/warp/issues/730)

### 2022.02.02 (v0.2022.01.31.09.03)

**New features**

* Multi-cursor keybindings for adding cursors above and below current selections with OPT-CMD-UP/DOWN - [374](https://github.com/warpdotdev/warp/issues/374)

**Bug fixes**

* Double clicking the top of the window maximizes the app - [097](https://github.com/warpdotdev/warp/issues/097)
* Icon, cursor and selection contrast fixes
* Scrolling performance improvements with bg image themes
* Changelog visual glitch
* Resize bug - losing scroll position when viewing blocks with long output

### 2022.01.26 (v0.2022.01.24.08.55)

**New features**

* Auto-close symbols (parentheses, quotes, and brackets) like VSCode

**Bug fixes**

* Block sharing link no longer cuts off - [660](https://github.com/warpdotdev/warp/issues/660)
* Right clicking a Block now focuses that Block
* Mouse dragging in vim
* Restoring history bug on session restore
* Automatically focus the last active window on session restore

### 2022.01.19 (v0.2022.01.17.08.48)

**New features**

* Restore block contents
* The longest common prefix in the completions menu auto-fills the Input Editor - [479](https://github.com/warpdotdev/warp/issues/479)
* Add description for paths in completion results - [103](https://github.com/warpdotdev/warp/issues/103)
* Can right click the prompt and copy: git branch, prompt, cwd - [346](https://github.com/warpdotdev/warp/issues/346)

**Bug fixes**

* Fixed bug where venv was inserted into input editor - [599](https://github.com/warpdotdev/warp/issues/599)
* Improved url detection

### 2022.01.12 (v0.2022.01.10.17.24)

**New features**

* Added a Changelog page to our documentation

**Bug fixes**

* Double clicking text in a url now highlights the word instead of the whole url - [508](https://github.com/warpdotdev/warp/issues/508)
* Double clicking a string with underscores now selects the whole string and not just the subword
* Selection updates correctly when a block hit its max line length
* Can now also close the Command Palette using CMD-P - [184](https://github.com/warpdotdev/warp/issues/184)
* Moved check for update button to settings dialog - [070](https://github.com/warpdotdev/warp/issues/070)
* Fixes tabs not opening in new windows when autoupdate is pending
* Fix regression with input box not being focused on app relaunch

### 2022.01.05 (v0.2022.01.03.09.07)

**New features**

* Native undo and redo in the text editor using CMD-Z - [113](https://github.com/warpdotdev/warp/issues/113)
* Added CMD-M to minimize the Window - [107](https://github.com/warpdotdev/warp/issues/107)
* Added our open source licenses to the Warp Documentation
* Split pane focus indicator - a triangle in the top left corner of the pane in focus

**Bug fixes**

* CTRL-SPACE is now properly passed to Emacs and other terminal apps - [499](https://github.com/warpdotdev/warp/issues/499)
* Copy on select setting persists across sessions and does not reset after updates

### 2021.12.29 (v0.2021.12.27.09.04)

**New features**

* Find in block (+ other find improvements)

### 2021.12.22 (v0.2021.12.20.09.04)

**New features**

* Windows, tabs, and panes are restored whenever you reopen Warp. Restoring block content is on its way!
* Warp now supports completions for over 300 commands and more information about existing commands by using Fig’s completion specs
* Git aliases are now included in completions menu - [210](https://github.com/warpdotdev/warp/issues/210)
* Switch to next pane and previous pane with CMD-\[ and CMD-] - [392](https://github.com/warpdotdev/warp/issues/392)
* Scrolling the Block list with PG-UP and PG-DOWN - [370](https://github.com/warpdotdev/warp/issues/370)
* Copy and paste the file directory into Warp from Finder - [514](https://github.com/warpdotdev/warp/issues/514)
* When the last Block is selected, can re-focus the input editor using CMD-DOWN key
* Arrow down scrolls to bottom of last block

**Bug fixes**

* Copying selected text to clipboard creates a new entry for each selected character - [504](https://github.com/warpdotdev/warp/issues/504)
* Needed an extra backspace to escape CTRL-R / history menu - [427](https://github.com/warpdotdev/warp/issues/427)
* VIM performance improvements - we’ve made progress but would love more sample cases of slowness

**Updates to Mac Menu Bar (Window)**

* Zoom
* Minimize
* Tile Window to Left of Screen (Default)
* Tile Window to Right of Screen (Default)
* Move to X screen (Default)
* Enter Full Screen (Default)
* Bring All to Front

### 2021.12.15 (v0.2021.12.13.08.40)

**New features**

* Fuzzy search in CTRL-R and Command Palette
* When you share a link to a block, up to 5 recipients may now download Warp’s beta via the link

**Bug fixes**

* Fix bug where opening file:// urls would not include query params like '?foo=bar' - [426](https://github.com/warpdotdev/warp/issues/426)
* More prominent highlights in CTRL-R, Command Palette, tab completion
* Vim bug fixes and performance improvements - please let us know what else you see

### 2021.12.08 (v0.2021.12.06.19.09)

**New features**

* Added a send invite button in account section of the settings dialog
* You can now request more invites in the invite modal

**Bug fixes**

* Copy on select persistence bug
* UI Bug when trying to un-share a block - [439](https://github.com/warpdotdev/warp/issues/439)

### 2021.12.01 (v0.2021.11.29.18.59)

**New features**

* Added 15 extra invites for everyone!
* Copy on select (highlighting text will automatically copy to clipboard). This can be turned off in the settings dialog - [077](https://github.com/warpdotdev/warp/issues/077)
* CTRL-L shortcut to clear the screen - [049](https://github.com/warpdotdev/warp/issues/049)

**Bug fixes**

* Can now highlight and copy sections of a URL without it automatically opening - [138](https://github.com/warpdotdev/warp/issues/138)

### 2021.11.24 (v0.2021.11.23.17.55)

**New features**

* Background images + gradients in themes: You can now set a background image or gradient as your theme background. Warp ships with a few of these already or you can create your own via a yaml file. - [032](https://github.com/warpdotdev/warp/issues/032)
* Changelog dialog
* Emoji rendering: 😂, 😃, 🌍, 🍞, 🚗, 📞, 🎉, ❤️ - [075](https://github.com/warpdotdev/warp/issues/075)
* Improved settings dialog
* Theme search - [237](https://github.com/warpdotdev/warp/issues/237)

**Bug fixes**

* Properly escapes whitespace when you drag and drop files

### 2021.11.17 (v0.2021.11.16.20.05)

**New features**

* Drag and drop files & directories from finder - [069](https://github.com/warpdotdev/warp/issues/069)

### 2021.11.10 (v0.2021.11.09.19.46)

**New features**

* Autosuggestions: Warp now suggests commands as you type, similar to Fish or Gmail - [052](https://github.com/warpdotdev/warp/issues/052)
* Button to copy the app/version - [106](https://github.com/warpdotdev/warp/issues/106)
* Conda context to the prompt - [235](https://github.com/warpdotdev/warp/issues/235)

**Bug fixes**

* Conda info (prompt) locking input editor
* CTRL-D now deletes forward one character
* History now preserved across sessions - [337](https://github.com/warpdotdev/warp/issues/337)
* Enter (numpad) was inputting as CTRL-C - [330](https://github.com/warpdotdev/warp/issues/330)

### 2021.11.03 (v0.2021.11.02.00.38)

**New features**

* CJK (Chinese, Japanese, and Korean) character support - [327](https://github.com/warpdotdev/warp/issues/327)
* Autocompletions for missing tar commands
* Enforcement of minimum contrasts in grid - [249](https://github.com/warpdotdev/warp/issues/249)

**Bug fixes**

* Runaway memory usage (from font loading on initial run) - [232](https://github.com/warpdotdev/warp/issues/232)
* Directories with non-english filenames not rendering on screen - [309](https://github.com/warpdotdev/warp/issues/309)
* App crashes from missing current working directory
* Pure Prompt being inserted as a typehead into editor - [242](https://github.com/warpdotdev/warp/issues/242)

### 2021.10.27 (v0.2021.10.25.22.47)

**New features**

* Ability to unshare blocks in settings modal
* Link to the documentation in kebab menu (three dots in top right corner)

**Bug fixes**

* Double character entry after input editor loses focus

### 2021.10.20 (v0.2021.10.19.21.38)

**New features**

* Switch theme based on OS appearance - [068](https://github.com/warpdotdev/warp/issues/068)
* Toggles instead of buttons in the setttings!
* Link to Custom themes documentation in the settings

**Bug fixes**

* IME support (non-English keyboards are now better supported in input box!)
* Show a banner instead of a popup when app startup takes longer than expected
* git log (and similar commands) no longer treated as a failed block

### 2021.10.13 (v0.2021.10.12.19.34)

**Bug fixes**

* Shell Bootstrapping should be a lot faster
* Support 3-char color representation for hex colors in theme
* Fix crashes relating to reading history files
* Prevent block completion from stealing focus
* Fix broken click handling for showing and hiding overflow menu

### 2021.10.06 (v0.2021.10.05.20.07)

**Bug fixes**

* Split pane navigation when 'Left / Right Option is Meta' settings are enabled
* Crash when opening a new window

### 2021.09.29 (v0.2021.09.29.13.26)

**New features**

* Split panes: create multiple panes in the same tab via shortcuts (CMD-E/SHIFT-CMD-E), the Command Palette, or by right clicking in any pane.
* Custom themes via files. You can now define your own theme as a yaml file in \~/.warp/themes. For more information on the file format and to see \~100 of the most popular themes already implemented in this format, see <https://github.com/warpdotdev/themes>. The ability to add and share themes directly within Warp is coming soon!

**Bug fixes**

* Add better messaging when Warp does not have permission to autoupdate
* Crash if a tab completion result was accepted after the cursor was moved to the beginning of the editor

### 2021.09.22 (v0.2021.09.21.20.54)

**New features**

* Theme picker available from the Command Palette

**Bug fixes**

* Occasional crash when opening a new Warp window
* Font selection dropdown didn't respect theme choice
* Issues with padding and hover detection when toggling Compact Mode on or off

### 2021.09.15 (v0.2021.09.14.21.25)

**Bug fixes**

* Crash when closing full-screen window
* Executables in path were not appearing for completions in Bash
* Completions menu overlaps theme picker

### 2021.09.09 (v0.2021.09.09.0.0)

**New features**

* New themes for Warp!!! (Access them via Settings on the overflow menu. We have Dracula, Solarized, & Gruvbox)
* CMD-, opens the Settings menu

**Bug fixes**

* Fixed crash when we fail to load a font or when we scroll through fonts
* Fixed visual artifacts around windows and modals jumping
* Fixed crash that occurs when you CMD-F while selecting an already selected text

### 2021.08.31 (v0.2021.08.31.0.0)

**New features**

* Support emacs bindings in input box
* History up menu performs a prefix search based on input

**Bug fixes**

* Warp not rendering after executing long-running command
* Stop powerlevel10k instant prompt from hanging on bootstrap
* Changing “font-size” via CTRL-- and CTRL-0 should stay in sync with font size in settings menu
* Bracketed paste mode bug: 0\~ \~1 on every command when ssh-ing
* Crash when tab completing with multibyte characters
* Download page doesn’t render correctly on safari
* Login is broken for some users using Chrome
* Make it more prominent in onboarding that we are collecting telemetry during the beta

### 2021.08.25 (v0.2021.08.25.0.0)

**New features**

* Custom fonts
* Completions for aliases and environment variables

**Bug fixes**

* Completions loose ends, including completions for path names with spaces and if commands are separated by &&
* Function key support within running programs (such as htop)
* Editor text respects zoom level
* Regression that caused URLs to not be highlighted
* Opening a new window required Internet connection

### 2021.08.18 (v0.2021.08.18.0.0)

**New features**

* Re-run with sudo

**Bug fixes**

* Crash caused by pressing CMD-K
* Completion not working when cursor is mid-line
* Re-input of multi-line commands
* [084](https://github.com/warpdotdev/warp/issues/084) - Rendering of colors correctly in diffs
* Selection showing after closing and re-opening alt-screen

### 2021.08.09 (v0.2021.08.09.0.0)

**New features**

* New settings modal (accessible from the top right overflow button) to set font size, toggle between light mode and dark mode, compact mode and normal mode
* CTRL-U and CTRL-K now cut to clipboard
* Typeahead: characters you type in a long-running command will now show up in the input box when the command completes

**Bug fixes**

* Handle arrow keys with modifiers (option and command) in CLIs and full-screen apps (Previously, users were unable to navigate with option and command keys in - Postgres CLI)
* Straightening the text baseline
* Translucent colors (e.g. for diff-so-fancy) are now correct (We now support the full range of opacity)
* Dotfile path completions + Completions improvements for more commands
* Artifacts when rendering svgs, especially on low res monitors. Overflow menu looks a lot better now!

### 2021.07.28 (v0.2021.07.28.0.0)

**New features**

* Compact Mode (see GIF below)
* Support for mouse events in Vim and other programs that can handle mouse input
* Completions for npm / yarn scripts

**Bug fixes**

* Major improvements to the consistency of completions, especially for commands that can take multiple arguments (e.g. rm -rf)
* Proper path completions for absolute paths
* Hang when PROMPT\_COMMAND is set for the shell
* Context Menu not closing when clicking outside of the menu
* Crashes after executing multi-line commands and on older versions of macOS

### 2021.07.21 (v0.2021.07.21.0.0)

**New features**

* Support for numpad ENTER
* More npm & yarn completions

**Bug fixes**

* Down arrow sends unrecognized escape sequence to Github CLI
* Can’t use UP arrow if item in history is multiple lines
* Crash when closing a tab when there are multiple tabs
* File-only completion signatures should also show directories

### 2021.07.13 (v0.2021.07.13.0.0)

**New features**

* New invite system to add users to Warp. To invite new users, click the overflow menu at the top right and click 'invite users'. For now we ask that you please don't post these invites on social media!
* URLs in the terminal screen are auto-linkified
* Double clicking the title bar maximizes/minimizes the window

**Bug fixes**

* Various Command Palette bugs
* Find box is populated with the user's text selection
* 3 second latency when changing the prompt upon first SSHing

### 2021.07.07 (v0.2021.07.07.0.0)

**New features**

* Command Palette for most keyboard shortcuts (CMD-P)
* Previously, tab completion descriptions were cut off. Now we display them in a floating box
* You can now switch tabs using CTRL-TAB and CTRL-SHIFT-TAB

**Bug fixes**

* Intermittent crashes with Zsh sessions and switching tabs
* Always fall back to path suggestions for completions
* Various bugs related to completions

### 2021.06.29 (v0.2021.06.29.0.0)

**New features**

* Multiple window support
* New completions UI and in-line documentation for commands and flags
* Horizontal scrolling of input box to support long commands

**Bug fixes**

* Crash when exiting from logout or exit when there’s a background process
* Crash when bootstrapping from detecting incorrect shell name
* Various bugs related to completions

### 2021.06.15 (v0.2021.06.15.19.04)

**New features**

* Mac File and Edit menus, along with Mac standard menu items (although New Window not yet working)

**Bug fixes**

* Crash when closing last window
* CMD-F: when there are no matches, display 0/0
* CMD-F should not scroll away if navigating to a match on the same row
* CMD-F: render the yellow rectangle at the layer of rendering the cell
* Unable to move cursor upwards on multi-line previous command
* Warp bootstrap commands showing up in history over ssh
* Accept input via input box before terminal has bootstrapped
* New tab button should have hover and click state
* Output stops midway through session on iMac running Mojave 10.14.6
* Backspace doesn’t work while holding shift
* Clipping issue in share dialog
* Input suggestions closes if you click on the scrollbar
* Hitting up/down while input suggestions are open causes menu to move
* Paste is not working for full screen apps
* Underline does not render with Hack font

### 2021.06.09 (v0.2021.06.09.15.14)

**New features**

* SSH support (Warp now works the same when you SSH as it does locally!)
* Improved completions: we’ve built out new completions support that are snappier and have more intelligent suggestions for options and arguments for some of the most used commands
* Find: Pressing CMD-F now brings up a find view to search for text in the terminal

**Bug fixes**

* Text rendering was faded on certain monitors


# Agents Overview

Powerful AI features like Agents, Code, Voice, Generate, and Active AI, fully integrated into the Warp Agentic Development Environment.

## AI in Warp

Warp includes intelligent agents designed to help you build, test, deploy, and debug while keeping you in control. Agents can look up commands, execute tasks, fix bugs, and adapt to your workflows. You can manage agent behavior directly, with full context from your Warp Drive and your team.

{% hint style="info" %}
Warp's AI features can be globally disabled in `Settings > AI` with the AI toggle.\
\
These features sends input data to various LLM providers through their API. Warp is **SOC 2 compliant** and has **Zero Data Retention** policies with all contracted LLM providers -- no customer AI data is retained, store, or used for training. Read more about data privacy for Warp features [on our privacy page](https://www.warp.dev/privacy).
{% endhint %}

## Included Agent features:

* [Agents](https://docs.warp.dev/documentation/agents/using-agents) - Run and manage multiple agents natively in Warp using natural language.
* [Agent Conversations](https://docs.warp.dev/documentation/agents/using-agents/agent-conversations) - Warp organizes your AI interactions into conversations tied to sessions, allowing you to attach context blocks, continue previous conversations, or start new threads for distinct tasks.
* [Agent Context](https://docs.warp.dev/documentation/agents/using-agents/agent-context) - Attach multimodal context directly to Warp’s Agent within the prompt.
* [Full Terminal Use](https://docs.warp.dev/documentation/agents/full-terminal-use) - Lets Warp’s agent drive interactive terminal apps—seeing live output, running commands and keystrokes, and handing control back to you whenever you want.
* [Managing Agents](https://docs.warp.dev/documentation/agents/using-agents/managing-agents) - Track, control, and configure all active agents in Warp using visual status indicators, in-app notifications, and the Agent Management Panel.
* [Agent Profiles and Permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions) - Set up Profiles to control what permissions and autonomy Agents have to run commands, apply code changes, and more.
* [Planning](https://docs.warp.dev/documentation/agents/using-agents/planning) - turn any Agent request into an organized, editable, and executable plan that the agent can run step-by-step with full visibility and version control.
* [Agent Task Lists](https://docs.warp.dev/documentation/agents/using-agents/agent-tasklists) - Track and manage complex workflows with automatic task lists that break requests into clear, actionable steps and update progress in real time.
* [Model Choice](https://docs.warp.dev/documentation/agents/using-agents/model-choice) - Pick your preferred LLM for Warp’s Agent from a curated set of the top models, or rely on Warp to choose the optimal model.
* [Active AI](https://docs.warp.dev/documentation/agents/active-ai) - Proactively recommends fixes and next actions based on errors, inputs, and outputs.
* [Model Context Protocol](https://docs.warp.dev/documentation/knowledge-and-collaboration/mcp) - Expose data sources or tools to Warp’s Agents via MCP Servers.
* [Rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules) - Create and store Global and Project Rules to set guidelines and constraints for Agents.
* [Voice](https://docs.warp.dev/documentation/agents/voice) - Talk to Warp AI using voice commands to accomplish tasks.
* [AI Autofill in Warp Drive](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/workflows#ai-autofill) - let Warp's Agent name and describe the workflows you create.


# Using Agents

Agents in Warp let you collaborate with AI in natural language to run terminal and coding workflows, manage context, and break complex tasks into clear, actionable steps.

## Agents in Warp

Agents in Warp let you go beyond manual commands by collaborating with AI directly inside the [Agentic Development Environment](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment). You can describe a task in natural language, and the Agent will translate it into runnable commands, manage context, and break complex requests into clear steps.

Agents are designed to work alongside you. They never act without visibility, and you remain in control of their autonomy and permissions.

**Key concepts related to Agents include:**

* Agent Mode — run terminal or coding workflows with natural language.
* [Conversations](https://docs.warp.dev/documentation/agents/using-agents/agent-conversations) — group queries and blocks for a specific task.
* [Context](https://docs.warp.dev/documentation/agents/using-agents/agent-context) — attach and manage information to improve responses.
* [Task Lists](https://docs.warp.dev/documentation/agents/using-agents/agent-tasklists) — break complex requests into clear, trackable steps.
* [Agent Management](https://docs.warp.dev/documentation/agents/using-agents/managing-agents) — monitor, configure, and control active agents.
* [Profiles and Permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions) — customize autonomy, tools, and behavior.

{% hint style="info" %}
To make sure you can fully use Agents, confirm that the global AI toggle is enabled under `Settings > AI`.
{% endhint %}

## What is Agent Mode?

Agent Mode is the primary way to interact with Warp’s Agent. It lets you run terminal or coding workflows by typing plain English instead of shell commands or IDE operations. When you enter a request, Warp uses leading LLMs to interpret it, suggest or run the right commands , surface code diffs when applicable, and stream results directly into your session, all tailored to your environment and setup.\
\
**Agent Mode can:**

1. Understand natural language input, not just command syntax.
2. Execute commands and use their output to guide the next step.
3. Correct itself when it encounters mistakes or errors occur.
4. Learn and integrate with any service that has public docs or `--help`.
5. Leverage saved workflows, project context, and other guidelines to improve accuracy.

### Entering Agent Mode

Agent Mode is how you interact directly with Warp’s AI to ask questions, run tasks, and collaborate in natural language. There are multiple ways to enter Agent Mode depending on where you are in your workflow:

{% tabs %}
{% tab title="macOS" %}

* Type natural language directly: If auto-detection is enabled, you can type a task or question into the input, and Warp will recognize it as natural language using its local auto-detection feature.
* Use keyboard shortcuts: Quickly toggle into Agent Mode with `CMD + I`.
* Attach blocks to a prompt: From any block you want to use as context, click the ✨ icon in the toolbelt or select Attach block(s) to AI query from the block’s context menu.
  {% endtab %}

{% tab title="Windows" %}

* Type natural language directly: If auto-detection is enabled, you can type a task or question into the input, and Warp will recognize it as natural language using its local auto-detection feature.
* Use keyboard shortcuts: Quickly toggle into Agent Mode with `CTRL + I`.
* Attach blocks to a prompt: From any block you want to use as context, click the ✨ icon in the toolbelt or select Attach block(s) to AI query from the block’s context menu.
  {% endtab %}

{% tab title="Linux" %}

* Type natural language directly: If auto-detection is enabled, you can type a task or question into the input, and Warp will recognize it as natural language using its local auto-detection feature.
* Use keyboard shortcuts: Quickly toggle into Agent Mode with `CTRL + I`.
* Attach blocks to a prompt: From any block you want to use as context, click the ✨ icon in the toolbelt or select Attach block(s) to AI query from the block’s context menu.
  {% endtab %}
  {% endtabs %}

When you’re in Agent Mode, the **Agent icon** will be highlighted in the [universal-input](https://docs.warp.dev/documentation/terminal/universal-input "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-459e3d0871237902108a86d93231039a60126d95%2Fusing-agents-universal-input.png?alt=media" alt=""><figcaption><p>The Agent icon in the Universal input indicates that Agent Mode is active.</p></figcaption></figure>

In Classic Input, you’ll also see a ✨ sparkles indicator inline.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f886e83dea97c4d46e3af7e2ee5274d8da4c79a1%2Fundo_my_git_commit.png?alt=media" alt="The sparkles on the command line indicate Agent Mode is active."><figcaption><p>The sparkles in the Classic input indicates that Agent Mode is active.</p></figcaption></figure>

By default, entering Agent Mode starts you in *Pair Mode*, where you can continue an ongoing conversation by asking follow-up questions or assigning tasks. From here, you can ask the agent to build, debug, fix, or even deploy code as needed.

### Models Powering Agent Mode

Agent Mode is backed by a curated selection of leading large language models (LLMs). By default, Warp uses **Claude 4 Sonnet** for "auto", balancing speed and quality.

However, you can switch to other supported models at any time based on your needs—for example, choosing a faster model for quick iterations or a more advanced model for complex reasoning.

For the full list of available models and guidance on when to use each, see [model-choice](https://docs.warp.dev/documentation/agents/using-agents/model-choice "mention").

### Demo: Starting a Coding Task with Warp

Here's an example from [Warp University](https://www.warp.dev/university), where Zach demonstrates a quick fix using Warp’s Agents to code:

{% embed url="<https://www.youtube.com/watch?v=IuFSuOYstfg>" %}


# Agent Conversations

Warp organizes your Agent interactions into conversations tied to sessions, allowing you to attach context blocks, follow up on previous queries, or begin new threads for distinct tasks.

## Conversations with Warp's Agent

Conceptually, a conversation is a sequence of AI queries and blocks. Conversations are tied to sessions and you can run multiple Agent Mode conversations simultaneously in different windows, tabs, or panes.

Conversations work best when the queries are related. If your new question builds on the last one, continue in the same conversation. If it is unrelated, it is better to start a new one so that the context remains relevant.

{% hint style="info" %}
Long conversations can cause slower performance and lower-quality answers. When working on a separate task or question, start fresh rather than relying on context from earlier interactions.
{% endhint %}

### Staying in a Conversation (Follow-Ups)

By default, if you ask an AI query immediately after interacting in Agent Mode, your query is sent as a **follow-up** to the current conversation.

* In **Classic Input**, you’ll see both the pink highlight bar on the left side of the block and a bent follow-up arrow (↳) next to your input. The conversation input chip also shows which conversation you are in.
* In **Universal Input,** the pink highlight bar and the conversation input chip serve as the indicators, but the bent arrow is not shown.

**To follow-up on a previous conversation:**

* Simply continue prompting the agent if you are already in an active conversation.
* Open the **Conversations menu** (`CMD + Y` on macOS, `CTRL + SHIFT + Y` on Windows/Linux), select a conversation, and then enter your query.
* Alternatively, click the pink conversation chip in the input field to resume.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-10ca9fc0fbd10a8c0b963fff410891815f02419f%2Fclassic-input-follow-up.png?alt=media" alt=""><figcaption><p>Continuing an Agent conversation in Classic Input (with indicator)</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-53193ed375af7ad39235ed33c0a805bd644dd572%2Ffollow-up-universal-input.png?alt=media" alt=""><figcaption><p>Continuing an Agent conversation in Universal Input</p></figcaption></figure>

### **Managing Conversations**

You can view previous conversations or start a new conversation via the **Conversations Menu** (`CMD + Y` on macOS, `CTRL + SHIFT + Y` on Windows/Linux).

{% embed url="<https://www.loom.com/share/9cc2451412be43e389a6b1414ea185e4?sid=4457ba14-4876-4988-ade6-1dca43dda96a>" %}

{% hint style="info" %}
The "New Conversation" item disappears once you start searching for an actual conversation.
{% endhint %}

### **Starting a New Conversation**

Warp automatically creates a new conversation in a few situations. For example, if you ask an AI query after running a shell command or if three hours pass without activity, Agent Mode will start a fresh conversation.

Visual indicators differ slightly depending on input mode:

* In **Classic Input,** a new conversation begins when there is no follow-up arrow (↳) next to your input.
* In **Universal Input**, a new conversation begins when there is no pink highlight bar on the left side of the block. The conversation input chip also helps confirm whether you’re in a new or existing thread.

{% tabs %}
{% tab title="macOS" %}
You can also start a new conversation manually at any time:

* In **Classic Input**, press `CMD + I` or press `BACKSPACE` while in follow-up mode.
* In **Universal Input**, press `CMD + SHIFT + N` or click directly on the conversation input chip.
* Open the **Conversations Menu** using `CMD + Y` and selecting "New Conversation".
  {% endtab %}

{% tab title="Windows" %}
You can also start a new conversation manually at any time:

* In **Classic Input**, press `CTRL + I` or press `BACKSPACE` while in follow-up mode.
* In **Universal Input**, press `CTRL + ALT + SHIFT + N` or click directly on the conversation input chip.
* Open the **Conversations Menu** using `CMD + SHIFT + Y` and selecting "New Conversation".
  {% endtab %}

{% tab title="Linux" %}
You can also start a new conversation manually at any time:

* In **Classic Input**, press `CTRL + I` or press `BACKSPACE` while in follow-up mode.
* In **Universal Input**, press `CTRL + ALT + SHIFT + N` or click directly on the conversation input chip.
* Open the **Conversations Menu** using `CMD + SHIFT + Y` and selecting "New Conversation".
  {% endtab %}
  {% endtabs %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4d44c077a13ae854ad47a6b045cffea39e2778d3%2Fclassic-input-new-convo.png?alt=media" alt=""><figcaption><p>Starting a new Conversation in Classic Input</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-c6ce01bb4be37f61d54d37766cf59e5d0ebf1ef9%2Funiversal-input-new-convo.png?alt=media" alt=""><figcaption><p>Starting a new Agent Conversation in Universal Input</p></figcaption></figure>

## Context Window Management

Every conversation with an agent consumes tokens stored in a **context window**. The context window (sometimes called *context length*) is the amount of text (measured in tokens) that a Large Language Model (LLM) can process at one time. **The size of the context window depends on the model you are using.**

As tokens accumulate and exceed the context window, performance and response quality may degrade. If the context window is exceeded, the model may lose track of earlier parts of the conversation, and **Warp will automatically summarize the conversation to free up space**.

### Warp provides a **context window usage indicator** to help you track this:

When less than 20% of the window is used, no indicator is shown. As more tokens accumulate, the usage bar progresses to reflect how much of the context window has been consumed.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-87b334f6c1c7c2dde8b16a5f2168f3247500f30e%2Fcontext-window-1.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e40fc2d2dea97ac30623dcbe6e959eb4e683589c%2Fcontext-window-2.png?alt=media" alt=""><figcaption></figcaption></figure>

As you approach the limit, the indicator turns red to warn that the context window is nearly full.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-94ab5eb10db6a1a1b520b8d3a321aa53fda7d2db%2Fcontext-window-2.png?alt=media" alt=""><figcaption></figcaption></figure>

Once the limit is exceeded, Warp automatically summarizes the conversation so you can continue without losing important context.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f52b179a0fb1eca0b0270e3a3a77bfbb881078d3%2Fcontext-window-3.png?alt=media" alt=""><figcaption></figcaption></figure>

The context window usage indicator is available only in **Universal Input**, which you can enable under `Settings > Appearance > Input`.

{% hint style="info" %}
If you switch models during a conversation, the context usage indicator updates only after you send your next message.
{% endhint %}

## Conversation Segmentation

Warp automatically detects when your query has shifted to a new topic. When this happens, it suggests starting a new conversation instead of continuing in the same context.

These options appear in the blocklist, where you can decide whether to branch off into a new conversation or keep going with the current one.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-1c939aecc15116a2b240cd0d3490784c5f6f7132%2Fconversation-segmentation.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also create a new conversation manually at any time by using the keyboard shortcut, opening a new tab, or opening a new pane.

{% tabs %}
{% tab title="macOS" %}

* Start a new conversation: `CMD + SHIFT + N`
* Open a new tab: `CMD + T`
* Open a new pane: `CMD + D`
  {% endtab %}

{% tab title="Windows" %}

* Start a new conversation: `CTRL + SHIFT + N`
* Open a new tab: `CTRL + SHIFT + T`
* Open a new pane: `CTRL + SHIFT + D`
  {% endtab %}

{% tab title="Linux" %}

* Start a new conversation: `CTRL + SHIFT + N`
* Open a new tab: `CTRL + SHIFT + T`
* Open a new pane: `CTRL + SHIFT + D`
  {% endtab %}
  {% endtabs %}


# Conversation Forking

Conversation forking lets you branch off into a new thread with the full context of the original, so you can explore different directions without changing the first conversation.

Warp allows you to **fork conversations** to create a new thread that inherits all of the context, messages, and history from an existing conversation. This is useful when you want to branch off in a new direction without affecting the original conversation.

{% embed url="<https://www.loom.com/share/15164f2abc19437ebefb47a8c6b52eb8?t=54>" %}

### How conversation forking works

* When you fork a conversation, the new thread starts with the same context and history as the original.
* Any follow-ups in the forked conversation do **not** impact the original. Likewise, continuing in the original conversation does not change the fork.
* Forked conversations behave just like any other conversation: you can move them into new windows, panes, or tabs.

*Example*: You can fork a conversation to explore an alternate solution, ask “what if” questions, or continue down two separate paths in parallel.

### Ways to fork a conversation

There are two ways to fork an existing conversation:

#### **1. From the command palette**

Open the menu using the command palette (`CMD + Y` on macOS / `CTRL + SHIFT + Y` on Windows/Linux).

Select **Fork current conversation** to fork your current conversation, or fork a specific conversation from open conversations.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-76923961454a4ed5b990183d7b84aeed22f1697b%2Fconversation-forking-palette.png?alt=media" alt=""><figcaption></figcaption></figure>

In addition, when you hover over any open conversation in the command palette, you’ll see a **fork button**. This lets you fork not only active conversations, but also inactive and historical ones.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-78a0cc4938a84942ef2e0226cccb9d3d953a7718%2Fconversation-forking-open-conversations.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also access this conversation view from the [universal input chip](https://docs.warp.dev/documentation/terminal/universal-input) in the current conversation.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4ad356110556f0fd52eae5e17187ad633b484cef%2Fconversation-forking-chip.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **2. From the footer of the most recent AI response block**

In any conversation in the blocklist, click the **fork button** in the footer of the most recent AI block. A new conversation opens in a separate pane with the full context of the original.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4d05d9b53ff9e7c2efbbd96d0a0a659ac87a786e%2Fconversation-forking-footer.png?alt=media" alt=""><figcaption></figcaption></figure>

### Using forked conversations <a href="#using-forked-conversations" id="using-forked-conversations"></a>

* Once forked, you can continue prompting as if you were still in the original conversation. The original conversation remains unchanged, allowing you to reference or continue both in parallel.
* For example, after forking you might ask *“Could you explain more?”* and Warp will respond using the inherited context.

**Forking is especially useful when:**

* You want to explore different approaches without losing the original thread.
* You need to keep one conversation “clean” while experimenting in another.
* You want to reuse context or specific blocks from older conversations.


# Agent Context

How to attach various forms of multi-modal context directly to Warp's Agent within a prompt.

In Warp, you can pass different types of input directly to the Agent to guide its behavior and improve response quality. These inputs are known as **Agent Context**: ad-hoc pieces of information you manually supply during a session.

**You can attach context in several ways:**

* [blocks-as-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/blocks-as-context "mention") - share output from your terminal to help the Agent understand errors, logs, or previous commands.
* [images-as-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/images-as-context "mention") - include screenshots, diagrams, or other visuals to provide additional clarity.
* [urls-as-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/urls-as-context "mention") - attach public webpages so the Agent can extract and reference their content.
* [selection-as-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/selection-as-context "mention") - attach code snippets from the editor or review panel to enrich your prompts with precise context.
* [using-to-add-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/using-to-add-context "mention") - reference files, folders, code symbols, or Warp Drive objects directly in your prompts.

***

This is distinct from other persistent or automatic sources of context, such as [rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules "mention"), [warp-drive-as-agent-mode-context](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/warp-drive-as-agent-mode-context "mention"), and [mcp](https://docs.warp.dev/documentation/knowledge-and-collaboration/mcp "mention"), which the Agent also uses when available.


# Blocks as Context

Attach blocks from your terminal as context so Warp’s Agent can understand errors, outputs, or previous commands when responding to your queries.

## Attaching blocks as context

Warp’s Agent can use blocks from your Agent conversations as context to better understand your queries and generate more relevant responses.

You can attach a block directly from the terminal blocklist by clicking the AI sparkles icon on it and selecting “Attach as context.”

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-974d0c18bc9b51dc26a5591c6613e69065891e5e%2Fremove_all_untracked_files.png?alt=media&#x26;token=2e0441da-f351-4df8-a8b3-b531d9dc0937" alt=""><figcaption><p>From a block of output, attach the block and ask Agent Mode to remove all untracked files.</p></figcaption></figure>

The most common use case is to ask the AI to fix an error. You can attach the error in a query to Agent Mode and type "fix it."

**If you're already in Agent Mode, use the following ways to attach or clear context from your query:**

{% tabs %}
{% tab title="macOS" %}
**Attach a previous block**

* To attach blocks to a query, you can use `CMD-UP` to attach the previous block as context to the query. While holding `CMD`, you can then use your `UP/DOWN` keys to pick another block to attach.
  * You may also use your mouse to attach blocks in your session. Hold `CMD` as you click on other blocks to extend your block selection.

**Clear a previous block**

* To clear blocks from a query, you can use `CMD-DOWN` until the blocks are removed from context.
  * You may also use your mouse to clear blocks in your session. Hold `CMD` as you click on an attached block to clear it.

{% hint style="info" %}
When using "Pin to the top" [Input Position](https://docs.warp.dev/documentation/terminal/appearance/input-position), the direction for attaching or detaching is reversed (i.e. `CMD-DOWN` attaches blocks to context, while `CMD-UP` clears blocks from context).
{% endhint %}
{% endtab %}

{% tab title="Windows" %}
**Attach a previous block**

* To attach blocks to a query, you can use `CTRL-UP` to attach the previous block as context to the query. While holding `CTRL`, you can then use your `UP/DOWN` keys to pick another block to attach.
  * You may also use your mouse to select blocks in your session. Hold `CTRL` as you click on other blocks to extend your block selection.

**Clear a previous block**

* To clear blocks from a query, you can use `CTRL-DOWN` until the blocks are removed from context.
  * You may also use your mouse to clear blocks in your session. Hold `CTRL` as you click on an attached block to clear it.

{% hint style="info" %}
When using "Pin to the top" [Input Position](https://docs.warp.dev/documentation/terminal/appearance/input-position), the direction for attaching or detaching is reversed (i.e. `CTRL-DOWN` attaches blocks to context, while `CTRL-UP` clears blocks from context).
{% endhint %}
{% endtab %}

{% tab title="Linux" %}
**Attach a previous block**

* To attach blocks to a query, you can use `CTRL-UP` to attach the previous block as context to the query. While holding `CTRL`, you can then use your `UP/DOWN` keys to pick another block to attach.
  * You may also use your mouse to select blocks in your session. Hold `CTRL` as you click on other blocks to extend your block selection.

**Clear a previous block**

* To clear blocks from a query, you can use `CTRL-DOWN` until the blocks are removed from context.
  * You may also use your mouse to clear blocks in your session. Hold `CTRL` as you click on an attached block to clear it.

{% hint style="info" %}
When using "Pin to the top" [Input Position](https://docs.warp.dev/documentation/terminal/appearance/input-position), the direction for attaching or detaching is reversed (i.e. `CTRL-DOWN` attaches blocks to context, while `CTRL-UP` clears blocks from context).
{% endhint %}
{% endtab %}
{% endtabs %}


# Images as Context

Attach screenshots, diagrams, or other images to your prompt so Warp’s Agent can use visual context when generating responses.

## **Attaching images as context**

To provide visual context, you can attach images directly to an agent prompt. This is useful for including screenshots, diagrams, or other visual references alongside your query.

You can attach images in the following ways:

* Using the **image upload button** found on the toolbelt (either on the bottom left or right), depending on which input mode you're using:

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-80b86c4c1b497d18e27403dba7a5e4b75eb61536%2Fimage-as-context-universal.png?alt=media" alt=""><figcaption><p>Attaching 5 images on the new "Universal" input (bottom left toolbelt)</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-9df3481f3deeeeae681bad2f4699b0194e69a91b%2Fimage-as-context-classic.png?alt=media" alt=""><figcaption><p>Attaching 4 images on the "Classic" input (bottom right)</p></figcaption></figure>

* Copy and paste images directly (e.g. right-click an image > "Copy image" or copy from a file manager) into Warp.
* Drag and drop images, such as from a file manager or screenshot utility.

{% hint style="info" %}
Warp accepts the following image formats: `.jpg` , `.jpeg` , `.png` , `.gif` , and .`webp` .
{% endhint %}

You can attach up to **5 images per request**, and up to **20 images across a single conversation**. Each image is sent to the model provider and immediately discarded — nothing is stored on Warp's servers.

### Model behavior and image handling

All supported models listed in [model-choice](https://docs.warp.dev/documentation/agents/using-agents/model-choice "mention") can interpret image input.

Attaching images will consume additional requests, proportional to the number of images added. To stay within model limits, Warp will intelligently resize images before passing it as context, minimizing token usage and respecting the model's maximum image dimensions.


# URLs as Context

Attach a public webpage link to your prompt to use its content as context—letting the agent extract and reference information directly from that page in its response.

## Referencing websites via URLs

You can attach a public URL to any prompt to provide page content as context. Warp will scrape the page and surface the extracted text directly to the model.

* Only publicly accessible pages are supported.
* The full page is added to the model’s context, which may increase credit usage for long documents.
* Only the specific URL you provide is processed. The agent won’t explore the site, follow links, or crawl beyond that page.

{% hint style="info" %}
**Important**: URL attachments are different from web search. If you need the agent to look something up, gather real-time information, or pull in multiple sources, use [web-search](https://docs.warp.dev/documentation/agents/using-agents/web-search "mention") instead.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-176c44d1b3c99c2e2f5dbc7b87ff754a9fa38c26%2Furl-as-context.png?alt=media" alt=""><figcaption><p>Example of referencing docs via a URL</p></figcaption></figure>


# Selection as Context

Attach text or diffs directly from Warp’s editor or Code Review panel as context for your Agent prompts.

### Attaching selections from Warp's native code editor

When you have Warp’s [native code editor](https://docs.warp.dev/documentation/code/code-editor) open beside a regular pane, you can easily attach specific lines of code as context:

1. **Select text** in the editor. A tooltip will appear in the bottom-right corner of the selection.
2. **Add as context** by clicking the tooltip or using the keyboard shortcuts `Cmd + L` (macOS) or `CTRL + SHIFT + L` (Windows or Linux).
3. Warp automatically adds the relative file path and context, in addition to the line numbers of the hunk, as a formatted string into the prompt.

This makes it easy to highlight just the lines you want the Agent to analyze or modify.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a89c3696c9e73dd6a438ef8b2882033e9450d338%2Fselection-as-context.png?alt=media" alt=""><figcaption><p>Selecting a function and attaching it as context from Warp's native code editor.</p></figcaption></figure>

### Attaching selections from Warp’s Code Review panel

You can also directly attach context from the [Code Review panel](https://docs.warp.dev/documentation/code/code-review):

1. Hover over any **diff hunk** to reveal the option to attach it as context.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-c30d5ecb033398472f18c58d7e4144b7d44bd5c7%2FAdd%20diff%20as%20context.png?alt=media" alt=""><figcaption><p>On-hover option to attach diff as context into the prompt.</p></figcaption></figure>

2. Attaching a diff will automatically insert the relevant file path and changed lines into your prompt.

This helps the Agent understand exactly what has been modified, making it easier to request explanations, feedback, or follow-up edits.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-47423aa917a4c53595a1eda0523841bdfd86cbaf%2Fgit%20diff%20full%20view.png?alt=media" alt=""><figcaption><p>Code Review panel with diffs for review.</p></figcaption></figure>


# Using @ to Add Context

Use @ to reference files, folders, code symbols, Warp Drive objects, or even blocks from other sessions as context, giving Warp’s Agent richer and more precise information to work with.

## How the @ context menu works

You can attach specific files, folders, code symbols, Warp Drive objects, and blocks from other sessions as context to a prompt using the @ symbol. When you’re inside a **Git repository**, typing @ opens a context menu that allows you to search for and select files or directories to include.

{% hint style="info" %}
Attaching context with @ works in **both natural language mode** (when interacting with Agents) and **classic terminal commands** for referencing file paths.
{% endhint %}

**Note**: the search in the @-context menu is always relative to the root of the Git repository, even when you're working in a subdirectory. This means you can reference *any* file or folder tracked in the repo, regardless of the current working directory.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d7cba00e669cdcfc69701594c81b3953d75b62a3%2Fat-context.png?alt=media" alt=""><figcaption><p>Using the @ symbol to search for and attach a file or folder from the project root.</p></figcaption></figure>

Additionally, no codebase indexing (via [codebase-context](https://docs.warp.dev/documentation/code/codebase-context "mention")) is required — file search is available immediately in any Git-initialized directory. The search also respects `.gitignore` rules and will exclude ignored files from the results.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6d78304b9065ad3e81f8064a769dca86e5fde610%2Fat-context-app.png?alt=media" alt=""><figcaption><p>Filtering files using @app to locate files containing “app” in their name or path.</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6fa227e2f327c03cb4d1486bbaeef05e4c00c6ad%2Fat-context-styles.png?alt=media" alt=""><figcaption><p>Referencing a folder or all files within it by typing @styles.</p></figcaption></figure>

### Referencing code symbols

The @ menu can also be used to fuzzy-search for code symbols in your codebase. This includes functions, classes, interfaces, etc.

If you type something like `@main`, Warp will surface a matching `main()` function and insert it into your prompt as a reference with the line number. By pointing the Agent to a specific symbol, you can give it exactly the context it needs to make a targeted edit or explanation.

{% embed url="<https://www.loom.com/share/da0c491bd2a44ed58d4fbdf2c260b019>" %}

### Referencing Warp Drive objects

Warp Drive objects are another way to attach context with **@**. You can reference:

* [workflows](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/workflows "mention") — parameterized commands you can name and save in Warp with descriptions and arguments.
* [notebooks](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/notebooks "mention") — runnable documentation consisting of markdown text and list elements, code blocks, and runnable shell snippets that can be automatically executed in your terminal session.
* [rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules "mention") — reusable guidelines and constraints that inform how Agents respond to your prompts/

When you select one of these objects, Warp inserts a reference token into your prompt. The contents of the object are then automatically passed as context to the Agent.

{% embed url="<https://www.loom.com/share/abd065af9fea421d925664135341c682>" %}

### Referencing blocks from other sessions

You are not limited to the current terminal session. With @, you can also bring in blocks of output from earlier sessions.

In the demo below, Ian shows how he previously ran cargo clippy and now wants help fixing the reported errors. Typing `@cargo clippy` surfaces the relevant block, which you can insert into your prompt. Once added, the Agent parses the output and generates fixes or explanations directly.

You can also reference live blocks, not just those that have already completed execution.

{% embed url="<https://www.loom.com/share/a4e72847341044cca2fed59a6299e1b7>" %}

### Why @ to reference context?

Attaching context with @ helps you:

* Reference exact outputs instead of copy-pasting entire logs
* Attaching relevant files or directories without leaving Warp
* Reuse existing context and knowledge in Warp Drive

This makes Agent interactions more accurate, clearer, and efficient, without additional setup.


# Agent Profiles & Permissions

Agent Profiles let you customize how your Agent behaves, from its models and autonomy to the tools and permissions it can use.

## Agent Profiles

Agent Profiles let you configure how your Agent behaves in different situations. Each profile defines the Agent's autonomy, base models, and tool access. You can create multiple profiles and edit them directly in `Settings > AI > Agents > Profiles`.

* **Default profile**: Every user starts with a default profile, you can edit it at any time, and new profiles will copy its settings as a starting point.
* **Other profiles**: Set up different profiles for different workflows (e.g., "Safe & cautious", "YOLO mode", etc.). Manage them in the Profiles settings menu.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-3268384dc2edf5ade8e322c57b894a520bd156e0%2Fagent-profiles.png?alt=media" alt=""><figcaption><p>Agent Profiles in Settings: define how your Agent operates.</p></figcaption></figure>

**In each Agent Profile, you can configure:**

* The name of the profile
* **Base model**: The core engine for your Agent. It handles most interactions and invokes other models when needed (e.g. for code generation).
  * This model is also used for [planning](https://docs.warp.dev/documentation/agents/using-agents/planning "mention"), which is responsible for breaking down complex tasks into actionable steps. It generates structured execution plans and decides how to route work between models.
* Agent autonomy and permissions

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-1560870ccbbb9be601226971ecf5dfa2d1205119%2Fagent-profiles-settings.png?alt=media" alt=""><figcaption><p>Agent Profiles in Settings: editting a Profile.</p></figcaption></figure>

## Agent Permissions

Agent Permissions let you define how your Agent in a specific Profile operates — control its autonomy, choose what tools or MCP servers it can access, and set when it should act independently or ask for approval.

You can control how much autonomy the Agent has when performing different types of actions under `Settings > AI > Agents > Profiles > Permissions` . Agent permission types:

* Apply code diffs
* Read files
* Create plans
* Execute commands
* Interact with running commands (via [full-terminal-use](https://docs.warp.dev/documentation/agents/full-terminal-use "mention"))

<div align="center"><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bf381f2dba1cc2eddb99dc969ee9619a4f5e165f%2Fagent-permissions-with-full-terminal-use.png?alt=media" alt=""><figcaption><p>Fine-tuning agent control: This permissions panel lets users customize how much autonomy the Agent has when applying code diffs, reading files, creating plans, and executing commands.</p></figcaption></figure></div>

**Each permission has different levels of autonomy:**

<table><thead><tr><th width="196.3369140625">Autonomy level</th><th>Description</th></tr></thead><tbody><tr><td>Agent Decides</td><td>Agent will act autonomously when it's confident, but prompt for approval when uncertain. This option balances speed with control, allowing the Agent to go ahead with common workflows while keeping you in the loop for more complex or risky steps.</td></tr><tr><td>Always ask</td><td>Agent will request explicit user approval before taking any action. Choose this for sensitive actions.</td></tr><tr><td>Always allow</td><td>Agent will perform the action without ever requesting explicit conformation. Use this for tasks you fully trust the Agent to handle on its own.</td></tr><tr><td>Never</td><td>Agent will not ever take the action (i.e. Create plans).</td></tr></tbody></table>

{% hint style="info" %}
*When all Agent permissions are set to Always allow, the Agent gains full autonomy (“YOLO mode”); however, any denylist rules will still override these settings.*
{% endhint %}

### Command allowlist

The Warp Agent lets you define an allowlist of commands that run automatically without confirmation. It’s empty by default, but users often add read-only commands such as:

* `which .*` - Find executable locations
* `ls(\s.*)?` - List directory contents
* `grep(\s.*)?` - Search file contents
* `find .*` - Search for files
* `echo(\s.*)?` - Print text output

You can add your own regular expressions to this list in `Settings > AI > Agents > Command allowlist`. Commands in the allowlist will always auto-execute, even if they are not read-only operations.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-01a396aec1551b41f950851c4d3bcd1593687884%2Fagent-profiles-allow-and-denylists.png?alt=media" alt=""><figcaption><p>Command allowlist and denylists as part of an Agent Profile.</p></figcaption></figure>

### Command denylist

For safety, the Agent always prompts for confirmation before executing potentially risky commands. The default denylist includes several examples, such as:

* `wget(\s.*)?` - Network downloads
* `curl(\s.*)?` - Network requests
* `rm(\s.*)?` - File deletion
* `eval(\s.*)?` - Shell code execution

The denylist takes precedence over both the allowlist and `Agent decides`. If a command matches the denylist, user permission will always be required, regardless of other settings. You can add your own regular expressions to this list in `Settings > AI > Agents > Command denylist`.

### MCP permissions

MCP servers let you extend the Agent with custom tools and data sources using standardized, plugin-like modules.

In this settings menu, you can configure which MCP servers the Agent is allowed to call:

* Use the MCP allowlist to give the Agent permission to call specific servers without asking.
* Use the MCP denylist to require approval before calling certain servers, even if they’re also in the allowlist.
* Or set the Agent to “decide” — it will act autonomously when confident, and ask for confirmation when uncertain.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-344ffccc0b38f35cf6237784a18b7913ef92e343%2FMCP_servers_agent_permissions.png?alt=media" alt=""><figcaption><p>Customize how the Agent interacts with MCP servers by choosing between “Agent decides,” allowlist, or denylist settings.</p></figcaption></figure>

{% hint style="info" %}
To learn how to build and configure your own MCP server, check out the [MCP feature docs](https://docs.warp.dev/documentation/knowledge-and-collaboration/mcp).
{% endhint %}

## Run until completion

During an Agent interaction, you can give the Agent full autonomy for the current task. When auto-approve is on, every suggested command runs immediately until the task finishes, or you stop it with `Ctrl + C`.

{% tabs %}
{% tab title="macOS" %}
Auto-approve all Agent actions with: `CMD + SHIFT + I`
{% endtab %}

{% tab title="Windows" %}
Auto-approve all Agent actions with: `CTRL + SHIFT + I`
{% endtab %}

{% tab title="Linux" %}
Auto-approve all Agent actions with: `CTRL + SHIFT + I`
{% endtab %}
{% endtabs %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d0711cc28a1082a1faab7728b5330034cd6fd1de%2Frun-until-completion.png?alt=media" alt=""><figcaption><p>A button overlay in the lower-right corner lets you enable auto-approve or end the Agent interaction.</p></figcaption></figure>

{% hint style="info" %}
*Run until completion* ignores the denylist entirely. It’s the purest form of “YOLO” mode and essentially a fully “autonomous mode” where the Agent proceeds without asking for confirmation.
{% endhint %}


# Agent Task Lists

Track and manage complex Agent workflows with automatic task lists that break requests into clear, actionable steps and update progress in real time.

The Agent can automatically break down complex requests into clear, trackable steps in the form of a task list with to-do items.\
\
When you make a sufficiently complex request that requires multiple actions, the Agent will automatically create a list of steps, execute them in order, and track progress from start to finish. There’s no need to adjust settings or enable a special mode—the Agent detects and creates task lists automatically.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8fc56bb8b1cad994773fea9568368a864a80e973%2Fin-progress-tasklist.png?alt=media" alt=""><figcaption><p>An example of a Task List in progress.</p></figcaption></figure>

### **How Task Lists work**

1. **Automatic task creation** — For complex requests, the Agent generates a structured list of tasks to complete.
2. **Step-by-step execution** — The Agent works through each task in sequence, updating statuses in real time.
3. **Summary** — Once all tasks are complete, the Agent provides a concise summary of what was done, including outputs, results, and relevant context. If any tasks were skipped or couldn’t be completed, it explains why.

After each step is completed, there is also a completion marker in the Agent conversation.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d2650352ed9c6ddd1e6dbadceaffaab3d577c228%2Fcompletion-markers.png?alt=media" alt=""><figcaption><p>Completion markers inside the Agent conversation after each task is completed.</p></figcaption></figure>

### Task statuses

Each task in the list has a visual indicator so you can quickly see its progress.

<table><thead><tr><th width="145.5">Status</th><th width="186.2265625">Icon</th><th>Meaning</th></tr></thead><tbody><tr><td>Current task</td><td>● (filled circle)</td><td>The Agent is actively working on this task.</td></tr><tr><td>Completed</td><td>✔︎</td><td>The Agent has finished this task successfully.</td></tr><tr><td>Not started</td><td>○ (empty circle)</td><td>The task is in the queue but work hasn’t begun.</td></tr><tr><td>Cancelled</td><td>■ (filled square)</td><td>The task was stopped before completion.</td></tr></tbody></table>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6846a8fa439fad543fc7510cce200d0476bdf7c1%2Ftasklist-small.png?alt=media" alt="" width="349"><figcaption></figcaption></figure>

### Task List access

During any Agent conversation, a task list chip appears at the bottom-right of the screen (when input is pinned to the bottom; otherwise, it may appear along the right side).

* Click the chip to open the current task list.
* You can collapse or expand the view at any time without interrupting the Agent.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-9180348ecd737faea5b77d00a5d133a4fe8bd78c%2Ftasklist-popup.png?alt=media" alt=""><figcaption><p>Access the Task List during an Agent conversation in the Task List chip in the conversation.</p></figcaption></figure>


# Planning

Planning lets you turn any request into an organized, editable, and executable plan that the agent can run step-by-step with full visibility and version control.

Warp has native planning functionality that helps you break down complex engineering tasks into structured, executable steps. Planning is tightly integrated with Warp's coding agent and provides a persistent plan editor, version history, selective execution, and deep links into your workspace.

{% embed url="<https://youtu.be/DawcFWyudV0?si=OzvuInMl8DoNR97R>" %}

***

### Creating a Plan

You can generate a plan using the `/plan` [slash command](https://docs.warp.dev/documentation/agents/slash-commands) or by asking the agent in natural language in the [universal-input](https://docs.warp.dev/documentation/terminal/universal-input "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2dac8a2b54cc62baa10c5e14e0641af2c9303b52%2Fplan-slash-command.png?alt=media" alt="" width="375"><figcaption><p>Prompting the agent to create a plan using the slash command.</p></figcaption></figure>

The agent then creates a structured plan inside Warp’s native rich text editor, which is designed for long, multi-step workflows. The editor includes clean formatting, inline code blocks, and clickable file paths so you can open referenced files immediately in Warp (see below) or in your external editor.

### Reviewing and Editing

Once a plan is generated, you can review it, reorganize steps, or refine details. You can edit the document manually or ask the agent to revise sections for you.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2b9f06a850d55a7cd8369a0e33598ffa3a6a1b37%2Fplanning-main-view.png?alt=media" alt=""><figcaption><p>Plan editor in Warp.</p></figcaption></figure>

Any updates made by the agent **creates a new version**. Version history lets you compare past iterations and restore an older version if you want to revert your approach, preserving a clear decision trail as the plan evolves.

### Executing a Plan

When you’re ready to start implementing, prompt the agent to run the plan. You can ask it to execute the full set of steps or only a specific section, such as “Implement phase 1 of the plan.”

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6a2f4dc0cc2cccd3e7448b85cb3da532d5d53ed6%2Fmanually-trigger-plan.png?alt=media" alt=""><figcaption><p>Manually referencing the plan using @ to kickoff the plan.</p></figcaption></figure>

The agent applies changes incrementally and updates files as it proceeds. This makes it easy to validate early steps before moving forward, adjust the plan mid-run, or try alternative paths without committing to the full workflow.

If you revise the plan while the agent is running, you can notify it directly; the agent will adjust its execution based on your updates.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ad09cd96d943dcb0c73a7c15baa1e434ac4b918b%2Fupdate-agent-mid-plan.png?alt=media" alt="" width="375"><figcaption><p>Option to pass new plan to agent if plan changes during runtime.</p></figcaption></figure>

### Monitoring Progress

While the agent is running, you can reopen the plan at any time by selecting **View plan** in the [universal-input](https://docs.warp.dev/documentation/terminal/universal-input "mention"). You can also follow each change in real time through the [code-review](https://docs.warp.dev/documentation/code/code-review "mention") panel and add comments or guidance using [interactive-code-review](https://docs.warp.dev/documentation/code/code-review/interactive-code-review "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4703d53513d43853ad57e375ed190b3e83dab114%2Fview-plan-udi.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

This gives you clear oversight, helps confirm expected behavior, and lets you intervene quickly if something needs correction.

### Saving and Sharing

Warp automatically saves all plans in the *Plans* folder in [warp-drive](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive "mention"). You can export any plan as Markdown, check it into your repository, or share a link—useful for GitHub PRs, design reviews, or async collaboration.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-03cb4b5e7d423b431f583a10bf6ae9aacbf67999%2Fexport-notebooks.png?alt=media" alt="" width="375"><figcaption><p>Different ways to share a plan.</p></figcaption></figure>

Because plans persist in Warp Drive, you can return to them later, reuse them for new work, or treat them as documentation for ongoing projects. This is also naturally passed to the agent as context.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-34bb48924cc40fb7ba788480e93cf6ea7b2b6e37%2Fplans-in-drive.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

You can configure whether your plans will be automatically added and synced to Warp drive In your [agent-profiles-permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions "mention") under `Settings > AI > Agents > Profiles`.

<figure><img src="broken-reference" alt="" width="371"><figcaption></figcaption></figure>

### Using Plans Across Conversations

Plans are reusable across tasks and sessions. You can reference them in future prompts, continue where you left off, or build follow-up plans that rely on earlier work.

The **@plans** command helps you quickly search for and reopen previously saved plans, making planning a consistent part of your development workflow rather than a one-off step. Learn more about attaching context using @ [here](https://docs.warp.dev/documentation/agents/using-agents/agent-context/using-to-add-context).

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bc2e9b17ad413a97c3f265de815c8f9dd0d2996f%2F%40-reference-plans.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>


# Managing Agents

Track, control, and configure all active agents in Warp using visual status indicators, in-app notifications, and the Agent Management Panel.

Warp’s agent management system is designed to support complex, multi-agent workflows across multiple terminal panes. You can run several agents at once, monitor their status, and step in when needed, without losing track of what’s happening across your sessions.

Agents will notify you when they need input, such as permission to run a command or approval to apply a code diff. This allows you to shift focus to other work, knowing you’ll be alerted when intervention is required. At any point, you can cancel an agent that’s stuck or going in circles. The agent will pause and wait for your input before continuing the task.

This page covers how agent statuses are displayed, how to use the Agent Management Panel, how notifications work, and how to configure agent autonomy and permissions.

{% embed url="<https://youtu.be/3jwus1bfKv4>" %}

### **Agent status indicators**

Each tab that contains an agent conversation will display a status icon indicating the agent’s current state.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-24c4b2e6eccf4db485edac546f3b9ffb01884387%2Fmgmt-tab-indicators.png?alt=media" alt=""><figcaption><p>Tabs with agents in different states, each displaying a corresponding status icon.</p></figcaption></figure>

<table><thead><tr><th width="84.34765625">Icon</th><th>Agent status</th></tr></thead><tbody><tr><td><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-7de35cc00ed15e080fb097475e6f58c58b39b356%2Fmgmt-pink-dot.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td>In progress. The agent is currently running.</td></tr><tr><td><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-798661b194c1f2d04dc64559d66f9cce96748a8b%2Fmgmt-green-checkmark.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td>Task delegated to agent has completed successfully.</td></tr><tr><td><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-dd1c7eb39671e0353ef420c8733d7273210337c2%2Fmgmt-yellow-square.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td>Agent requires your attention (e.g. waiting for input or approval).</td></tr><tr><td><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d568064417c65937090157c4be567945ff9b0ad4%2Fmgmt-grey-square.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td>Agent was manually stopped and is idle.</td></tr><tr><td><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-cb6c493bd5b031f91b7b373791663e805b2c40a5%2Fmgmt-red-triangle.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td>An error occurred. This may be due to a model failure, an API issue (such as LLM provider downtime), a lost internet connection, or other unexpected problems.</td></tr></tbody></table>

**Notes:**

* Status icon colors follow Warp's semantic theme settings, so they appear as theme-specific variants rather than the exact shades shown above.
* If an agent encounters an error, the error will be surfaced in the last block of the affected conversation.
* In tabs with multiple agent interactions (across different panes), the status icon reflects the agent state of the most recently focused pane.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-baf49b64f297293071c0ffac3390137e288ad64a%2Fmgmt-two-panes.png?alt=media" alt=""><figcaption><p>Agent status icons shown across multiple panes in a tab.</p></figcaption></figure>

### **Agent Management Panel**

Warp includes an Agent Management Panel that provides a centralized view of all active agents across your sessions. You can monitor their status, cancel running tasks, review errors, and jump directly to conversations that need input.

This panel is accessible from the top right of the interface and is designed to keep you informed without disrupting your workflow.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-efd61393d1233b9965f811332d3d62458d402b24%2Fmgmt-panel.png?alt=media" alt=""><figcaption><p>Agent management panel, highlighting five agents with differing statuses.</p></figcaption></figure>

The Agent Management Panel provides a centralized view of all agent activity across your sessions. From this panel, you can:

* View the current status of all agents across active terminal sessions
* Cancel agents that are currently in progress (only agents in the “in progress” state will show a stop option)
* Review agents that are waiting for input or have encountered an error
* Jump directly to the associated terminal pane or conversation

Once an agent is cancelled, it will stop executing and no further updates or notifications will be sent.

Agent activity is ordered by most recent interaction. If a single tab contains multiple agents across different panes, each conversation will appear separately in the panel, sorted by recency.

### **In-app agent notifications**

Warp provides two types of in-app notifications to keep you informed about agent activity:

1. **Toasts** appear briefly at the top right of the screen and link directly to the relevant conversation. If dismissed or ignored, they disappear from view but remain marked as unread in the Agent Management Panel.
2. The **red dot indicator** appears on the Agent Management button in the top-right corner when there are unread agent notifications. Opening the panel clears the red dot and marks all associated notifications as read.

These notifications ensure you don’t miss critical updates, such as when an agent encounters an error or requests manual approval.

### **Autonomy and controls**

You can configure how much autonomy and control agents have in `Settings > AI > Agents > Permissions` . From this settings page, you can:

* Require manual approval before the agent applies code diffs, reads files, creates plans, or runs commands
* Define allowlists or denylists to control agent behavior based on command types or patterns

These settings let you fine-tune how agents interact with your system and control the level of automation based on task sensitivity. For more information on autonomy, please reference: [agent-profiles-permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions "mention").

### Demo: Using multiple agents at once in Warp

Here's an example from [Warp University](https://www.warp.dev/university), where Zach demonstrates how he uses and manages multiple agents in Warp:

{% embed url="<https://www.youtube.com/watch?t=&v=3jwus1bfKv4>" %}


# Model Choice

Choose from a curated set of top LLMs for Warp's Agents (or let Warp auto-select the best model).

## Available models

Warp lets you choose from a curated set of Large Language Models (LLMs) to power your Agentic Development Environment.

**Warp supports the following models:**

* OpenAI: `GPT-5` and `GPT-5.1` (select between *low, medium,* and *high* reasoning modes)
* Anthropic: `Claude Sonnet 4.5`, `Claude Opus 4.1`, `Claude Haiku 4.5` , `Claude Sonnet 4`
* Google: `Gemini 3 Pro`, `Gemini 2.5 Pro`
* z.ai: `GLM 4.6` (hosted in the US, by [Fireworks AI](https://fireworks.ai/models/fireworks/glm-4p6))

### Auto Models

Warp also offers two *Auto* modes that intelligently select the best model for your task based on the context and request type:

1. **Auto (Cost-efficient)**: Optimizes for lower credit consumption while maintaining strong output quality, helping extend your available usage.
2. **Auto (Responsiveness)**: Prioritizes the highest-quality results using the fastest available model, though it may consume credits more quickly.

Both Auto models perform well across all agent workflows and are ideal if you prefer Warp to manage model selection dynamically.

### How to change models

You can use the model picker in your prompt input to quickly switch between models. The currently active model appears directly in the input editor.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4c4f5c6af395a6aa3835eca0cf62f3073b145274%2Fnew-models-oct-2025.png?alt=media" alt=""><figcaption><p>Model selector in Warp's Universal Input.</p></figcaption></figure>

To change models, click the displayed model name (for example, *Claude Sonnet 4.5*) to open a dropdown with all supported options. Your selection will automatically persist for future prompts.

### Configuring models per Agent Profile

You can configure the base and planning models for each [agent-profiles-permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions "mention"), defining the Agent’s autonomy, tool access, and other permissions.

Edit your default profile or more profiles directly in `Settings > AI > Agents > Profiles`.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-fbc1b3e768939a6b52ca17d7da2cc995907b0eae%2Fbase-planning-model-pickers.png?alt=media" alt=""><figcaption><p>Model choice example, where the base model is Auto (Claude 4 Sonnet) and the planning model is o3.</p></figcaption></figure>

### Zero Data Retention Policies

Warp integrates with multiple Large Language Model (LLM) providers to power its AI-driven features.

These providers include, but are not limited to:

* OpenAI
* Anthropic
* OpenAI
* Google
* Fireworks AI

Warp has executed Zero Data Retention (ZDR) agreements with these providers. This means that, by default across all plans:

* LLM providers commit not to train their models on any customer-generated data processed through Warp’s services.
* LLM providers commit to delete inputs and outputs after generating the relevant output, within a fixed time period.

Warp enforces these commitments through both technical measures and contractual safeguards with the LLM providers.


# Web Search

Warp’s web search lets agents pull in real-time information, documentation, and cited sources whenever it improves an answer.

Warp includes native web search for models that support first-party search tools. When enabled, agents can look up information in real time, consult documentation, retrieve current version numbers, and cite the sources used to generate responses.

{% embed url="<https://www.loom.com/share/06a4ba98f2e0446d80cb37aa4c23848c>" %}

This page covers how web search works, supported models, what you can expect inside Warp, configuration options, and how this differs from attaching URLs directly to a prompt.

***

### When the Agent uses web search

Models initiate a web search when it improves the quality or accuracy of an answer. **Common scenarios include:**

* Retrieving official documentation or API references
* Getting the latest version of a library or tool
* Checking error messages, GitHub issues, or StackOverflow discussions
* Looking up ongoing incidents or recent changes
* Answering questions where recency matters (e.g., “best approach in 2025 to…”)

Web searches are automatically triggered when the model considers them useful. You don’t need special syntax.

### How web search works in Warp

**When a search occurs:**

1. Warp shows a “Searching the web…” indicator inside the conversation.
2. You can expand the search result to view:
   * The query issued
   * The pages retrieved
3. **The model reads results and produces a grounded response.**
   * Claude models cite sources in the references footer.
   * OpenAI models use inline citations and also shows references in the footer.

### Supported and Unsupported Models

Web search is available only for models that offer a native web search integration, that works in tandem with other custom tools.

**Models that support web search**

* Anthropic: `Claude 4.5 Series`, `Claude 4 Series`
* OpenAI: `GPT-5.1`, `GPT-5`
  * *Note: GPT-5 mini with minimal reasoning does not support web search*

Warp uses each vendor’s official tool:

* **Claude Web Search**: <https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool>
* **OpenAI Web Search**: <https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses>

{% hint style="info" %}
**Note**: We plan to add native web search for additional models as soon as their APIs fully support it. We’ll continue updating the list of search-capable models as vendors roll out broader tooling. We're also exploring custom web search tools that'll work across all models.
{% endhint %}

### Viewing Search Results

You can inspect the web search UI at any time:

* Expand the **Web Search** section in the agent response
* You can see:
  * The list of pages fetched
  * The text used to answer your question
  * Citations and reference metadata

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-3233fd85ddac77de6e46d22d23ff538db08ff5b6%2Fweb-search-results.png?alt=media" alt=""><figcaption></figcaption></figure>

This makes it easy to verify accuracy, audit reasoning, and validate sources.

### Enabling or Disabling Web Search

Web search is controlled per [agent-profiles-permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions "mention").

**To configure:**

1. Open `Settings > AI`
2. Select an **Agent Profile**
3. Scroll to **Call web tools**
4. Toggle the **setting on or off**

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-acd80903bfbfee24d75aaf1c86014a86805a5bdc%2Fweb-search-settings.png?alt=media" alt=""><figcaption></figcaption></figure>

Disabling this prevents the agent from performing searches, even if a model would normally use them.

### Credit Usage

Web search incurs two types of credit usage:

1. A small fixed cost per search invocation
2. Additional cost proportional to retrieved content, since retrieved text is passed to the model

You’ll see these contributions itemized in the conversation’s credit usage footer, alongside model calls, planning calls, and other tool usage.


# Full Terminal Use

Full Terminal Use means Warp's agents can interact with active terminal apps to monitor live output and run commands.

Full Terminal Use lets Warp's agent operate directly inside interactive terminal applications, such as database shells, debuggers, text editors, long-running servers, and more.

The agent can see the live terminal buffer (terminal state), write to the PTY to run commands, respond to prompts, and continue working inside the running process while you stay in control.

{% embed url="<https://youtu.be/gBdehHrtb94?si=-vvl4ipGwwoWxEJq>" %}

## Overview

With Full Terminal Use, Warp’s agent can attach to interactive tools like `psql`, `vim`, `python`, `gdb`, `top`, or your dev server, read the terminal output as it changes, and interact with the application as if you were typing.

You can either ask the agent to start an interactive program, or you can start it yourself and then tag the agent in once the tool is already running. In both cases, the agent sees the same terminal buffer (and PYT session) you do and can act on it.

## How Full Terminal Use works

#### Start an interactive command

You can either ask the agent to run an interactive command, or start one manually and then tag the agent in:

* **Ask the agent to start an interactive tool**
  * Example:
    * “Open a Postgres shell and help me inspect the orders table.”
    * “Start the dev server and debug this 500 error.”
* **Or start the command yourself, then tag the agent in**
  * Example:
    * If you’ve already launched an interactive tool (for example `psql` or `npm run dev`), you can bring the agent into the running session using the "Use Agent" button in the terminal footer or via `CMD + I` .
    * Once the agent is tagged in, you can follow up with natural-language requests such as:

      “Watch this process and help debug the error on the /session endpoint.”
    * Warp then attaches the agent to the active PTY so it can see the current terminal buffer and propose actions inside the session.

{% embed url="<https://www.loom.com/share/bcedc521071a4b6a9bbcf74b5156f903>" %}
Tagging in the agent.
{% endembed %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2f8585e1281b597d7fce11f32ba026c6fd20d0d0%2Ffull-terminal-use-npm.png?alt=media" alt=""><figcaption></figcaption></figure>

Warp attaches the agent to the running command so it can see and control the terminal buffer.

#### Agents propose actions inside the session

Once attached, you can continue using natural language and the agent turns your requests into concrete terminal actions. For example, in a Postgres shell:

* You: “Show me all the tables and describe the orders table.”
* Agent: proposes running commands like: `\dt` --> `\d+ orders`

In the UI, you’ll see a request to:

* Run a specific command
* Optionally enable auto-approval for similar commands in this session

#### Switching control between user and the agent

You can swap control at any time.

**Take over**

* Use the Takeover control to stop the agent from typing or performing any actions.
* The shell stays open, and you can type directly into the same session.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-efa5d3dd7fffc6ef7c28b2aa51829950bcf75fb5%2Ffull-terminal-use-takeover.png?alt=media" alt="" width="310"><figcaption><p>Option to take over from agent in the footer.</p></figcaption></figure>

**Hand back control**

* When you’re ready for the agent to continue, click the control again.
* The agent resumes where you left off, with full access to the current terminal state.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-77a908698b93f516dee09dfcdd7d768fbc900d26%2Ffull-terminal-use-handoff.png?alt=media" alt=""><figcaption><p>Option to hand-off to the agent in the conversation footer.</p></figcaption></figure>

This makes it easy to:

* Let the agent do mechanical work (paging output, trying variants of a command)
* Step in for delicate or security-sensitive actions
* Then let the agent continue once the critical step is done

#### Showing and hiding agent responses

Warp gives you control over how much agent output appears in Full Terminal Use.

**Toggle visibility**

Use the `Hide responses` or `Show responses` button or `CMD + G` in the interactive command footer to switch between showing all agent output or hiding it from the terminal view.

Note that this only affects the agent's messages and proposals; your terminal state and command output remain unchanged.

**Behavior when hidden**

* When agent responses are hidden, your own agent requests automatically dismiss after **4 seconds** to keep the terminal clear.
* You can also manually dismiss any user query at any time by hovering over it and clicking the X.

{% embed url="<https://www.loom.com/share/c639fb4ab33343a39037b2083c66858a>" %}

***

### Configuring agent permissions and autonomy

You control how much autonomy the agent has when interacting with the terminal.

#### Session-level approvals

Each time the agent wants to take an action inside an interactive shell, you’ll see the agent’s reasoning, a brief explanation, and the proposed command. From there you can:

* Allow the command once (for example by approving it or pressing `ENTER`).
* Turn on auto-approval for similar commands in this session (for example with `CMD + SHIFT + I`).
* Refine the request with `CTRL + C`, which clears the proposed action and lets you follow up with a different query.
* Take over manually with `CMD + I`, which stops the agent from issuing any further PTY writes until you hand control back.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6ae5c11e62b4d454af2fe00031e96501cfee50d3%2Fallow-refine-takeover.png?alt=media" alt=""><figcaption><p>Allow, Refine, or Take over an agent response.</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-947c49794d86c393955e932adf7bb718d390a5d7%2Ffull-terminal-use-options.png?alt=media" alt="" width="375"><figcaption><p>Ability to accept or auto-approve future interactions.</p></figcaption></figure>

This lets you tighten or loosen control for the current task:

* For exploratory work, you might Always allow to reduce friction.
* For production systems or sensitive operations, you might Allow once and review each step.

#### Global permission settings

You can configure global defaults from your [agent-profiles-permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions "mention") settings:

* **Ask on first write**: The first write to a shell process requires approval. After that, all subsequent writes for that specific process/command will be approved.
* **Always ask**: Every write to the shell process from the agent requires your explicit approval.
* **Always allow**: The agent can write to the shell process without prompting you each time.

These settings apply to every session that uses Full Terminal Use. You can still override them on a per-session basis when prompted. For example, you can enable **auto-approval** for similar commands in the current session using the fast-forward control, or switch to a **different AI profile** with its own permission settings for that conversation.

{% hint style="info" %}
**Note**: All [Secret Redaction](https://docs.warp.dev/documentation/privacy/secret-redaction) features still apply during Full Terminal Use, so sensitive values in your environment or output remain protected.
{% endhint %}

### AI credits usage

All AI interactions from Full Terminal Use consume [ai-credits](https://docs.warp.dev/documentation/support-and-billing/plans-and-pricing/ai-credits "mention"), including understanding your natural language requests, planning and generating terminal commands, interpreting and summarizing command output, and iterating on commands in long-running sessions.

Credits are consumed in a similar way as other Warp AI actions that use the same model and a similar context size.

**Interactive sessions can consume more credits if:**

* The agent runs many commands in an interactive shell on your behalf.
* There is a significant amount of terminal output to read and summarize.

**To manage credit usage:**

* Use tighter scopes:
  * “Describe just the orders table.” instead of “Explain the entire database.”
* Pause autonomy for high-volume tasks with copius terminal output:
  * Take over manual control when running large batches or long logs.
* Use stricter permissions:
  * Set global permissions to "Ask on first write" or "Always ask", then approve only what you need.

{% hint style="info" %}
To learn more about what goes into a credit and how to get more value from AI usage in Warp, see: [*Getting the most out of AI credits in Warp*](https://www.warp.dev/blog/warp-ai-requests).
{% endhint %}

## Example workflows

Here’s a demo from one of our engineers, Maggie, that walks through a couple of Full Terminal Use examples.

{% embed url="<https://www.loom.com/share/d47ee09153df417983df65a339a9d6f2>" %}

Below are some common interactive tools where Full Terminal Use is particularly useful: database shells (Postgres, MySQL, SQLite), debuggers such as gdb, language-specific REPLs like python or node, text editors and file explorers, and long-running dev servers or monitoring tools such as top and htop.

<table><thead><tr><th width="158.5418701171875">Tool</th><th width="326.64208984375">Example tasks</th><th>Agents can...</th></tr></thead><tbody><tr><td><strong>Database shells (REPLs)</strong><br><br>e.g. <code>psql</code>, <code>mysql</code>, <code>sqlite</code>, etc.</td><td><ul><li>“List all tables and describe the users and orders tables.”</li><li>“Create a new table to store archived user sessions.”</li><li>“Show me all rows in orders from the last 30 days, grouped by status.”</li><li>“Generate and run a query that finds the top 10 customers by revenue.”</li></ul></td><td><ul><li>Navigate <code>\d</code>, <code>\dt</code>, <code>DESCRIBE</code>, etc.</li><li>Write and execute SQL queries</li><li>Summarize results in plain language</li></ul></td></tr><tr><td><strong>Text editors</strong><br><br>e.g. <code>vim</code>, <code>nano</code>, etc.</td><td><ul><li>“Open this file in vim and add a Markdown header and a boilerplate section.”</li><li>“Insert a docstring above this function explaining what it does.”</li><li>“Generate a CSS utility class block and insert it in this file.”</li></ul></td><td><ul><li>Navigate within the editor using keystrokes</li><li>Insert, edit, and delete text</li><li>Save and quit when done</li></ul></td></tr><tr><td><strong>Python REPLs</strong><br><br>e.g. <code>python</code>, <code>ipython</code></td><td><ul><li>“Start a Python REPL and define a function that calculates a moving average.”</li><li>“Write a unit test for this function and run it.”</li><li>“Plot x from 0 to 10 and y = sin(x).”</li></ul></td><td><ul><li>Import modules</li><li>Define functions and classes</li><li>Run tests and small scripts</li><li>Print or summarize results back to you</li></ul></td></tr><tr><td><strong>Debuggers</strong><br><br>e.g. <code>gdb</code>, <code>lldb</code>, language-specific debuggers</td><td><ul><li>“Start gdb for this binary and set a breakpoint on <code>handle_request</code>.”</li><li>“Run until the breakpoint, then show the stack and local variables.”</li><li>“Inspect this pointer and tell me if it looks invalid.”</li></ul></td><td><ul><li>Issue debugger commands (break, run, next, continue, bt, etc.)</li><li>Walk through execution step by step</li><li>Summarize relevant state so you don’t have to remember every command</li></ul></td></tr><tr><td><strong>Long-running servers and services</strong><br><br>e.g. <code>npm run dev</code>, <code>uvicorn</code>, Rails servers, etc</td><td><ul><li>“Run the dev server and debug the internal server error on /session.”</li><li>“Send a sample request to this endpoint and explain the failure.”</li><li>“Kill the server once you identify the error and propose a code diff.”</li></ul></td><td><ul><li>Watch server logs in real time</li><li>Notice new errors as they appear</li><li>Stop the server when appropriate</li><li>Propose code changes (for example, via a diff) based on what it observes</li></ul></td></tr><tr><td><strong>Version control workflows</strong><br><br>e.g. <code>git rebase -i</code>, complex git commands</td><td><ul><li>“Interactively rebase master onto <code>feature-branch</code> to squash these commits into one.”</li><li>“Resolve these merge conflicts and ensure tests pass.”</li></ul></td><td><ul><li>Navigate interactive rebase prompts</li><li>Edit commit messages</li><li>Apply conflict resolutions you approve</li></ul></td></tr><tr><td><strong>Cloud provider CLIs</strong><br><br>e.g. <code>gcloud</code>, <code>aws</code>, <code>az</code>, etc.</td><td><ul><li>“Use gcloud to create a new Kubernetes cluster with these settings.”</li><li>“Provision a new RDS instance for staging and show me the connection details.”</li></ul></td><td><ul><li>Walk through multi-step CLI workflows</li><li>Handle prompts and confirmations</li><li>Summarize the resulting resources</li></ul></td></tr></tbody></table>


# Slash Commands

Use Slash Commands in Agent Mode or Auto-Detection Mode to quickly run built-in actions or saved prompts without leaving the input field.

When using Agent Mode or Auto-Detection Mode, typing `/` in the input field opens the Slash Commands menu.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d74394b5f83dd754c9a5132ccd44345c75b4b0f7%2Fslash-commands-menu.png?alt=media" alt=""><figcaption><p>Slash Commands menu</p></figcaption></figure>

As you type, the menu filters results in real time, making it easy to find and run the command or prompt you need.

## Static Slash Commands

Warp currently supports the following built-in Slash Commands:

<table><thead><tr><th width="211.64453125">Slash Command</th><th>Description</th></tr></thead><tbody><tr><td><code>/add-mcp</code></td><td>Add a new <a href="../knowledge-and-collaboration/mcp">MCP server</a>.</td></tr><tr><td><code>/add-prompt</code></td><td>Add a new <a href="../knowledge-and-collaboration/warp-drive/prompts">Agent Prompt</a> in Warp Drive.</td></tr><tr><td><code>/add-rule</code></td><td>Add a new <a href="../knowledge-and-collaboration/rules">Global Rule</a> for the Agent.</td></tr><tr><td><code>/create-environment</code></td><td>Create a <a href="../integrations/integrations-overview">Warp Environment</a> (Docker image + repos) via guided setup. <code>*</code></td></tr><tr><td><code>/create-new-project</code></td><td>Have the agent walk you through creating a new coding project. <code>*</code></td></tr><tr><td><code>/diff-review</code></td><td>Open the <a href="../code/reviewing-code">diff review pane</a>.</td></tr><tr><td><code>/index</code></td><td>Index the current codebase using <a href="../code/codebase-context">Codebase Context</a>.</td></tr><tr><td><code>/init</code></td><td>Index the current codebase and generate a <a href="../knowledge-and-collaboration/rules">WARP.md file</a>. <code>*</code></td></tr><tr><td><code>/plan</code></td><td>Prompt the agent to do some research and create a <a href="using-agents/planning">plan</a> for a task.</td></tr><tr><td><code>/open-project-rules</code></td><td>Open the <a href="../../knowledge-and-collaboration/rules#project-rules">Project Rules</a> file (<code>WARP.md</code>).</td></tr><tr><td><code>/view-mcp</code></td><td>View the status of your <a href="../knowledge-and-collaboration/mcp">MCP servers</a>.</td></tr></tbody></table>

{% hint style="warning" %}
Slash commands marked with a `*` consume AI credits to complete the task.
{% endhint %}

#### Using Prompts via Slash Commands

In addition to static commands, the menu also shows [Agent Prompts](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/prompts) saved in your [Warp Drive](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive).

* These prompts can be custom ones you’ve created or ones shared with you.
* As you type after `/`, prompts are filtered dynamically, so you can quickly run them without leaving the input field.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-15807b88aca5d87bf4df6de5147fa7715dfe5299%2Fslash-commands-prompts.png?alt=media" alt=""><figcaption><p>Slash Commands menu with filtered Agent Prompts</p></figcaption></figure>

### Tips

* **Context-aware:** Many Slash Commands use your current working directory or file selection as context.
* **Quick access:** Use `/` from anywhere in Agent Mode or Auto-Detection Mode to avoid navigating through menus.

### Example of using a Slash Command

Below is an example interaction when `/init` is ran:

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6f17d3c88d28b77d8dbdda74f5a4249335b8168c%2Finit-setup-flow-1.png?alt=media" alt=""><figcaption><p>/init setup flow; 1 of 2</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a32d318f47a11bf5a2cbcbebdc0fbc37f01eacb1%2Finit-setup-flow-2.png?alt=media" alt=""><figcaption><p>/init setup flow; 2 of 2</p></figcaption></figure>


# Active AI

Active AI proactively recommends fixes and next actions based on your command line errors, inputs, and outputs.

## Active AI

{% hint style="info" %}
Active AI features can be disabled in `Settings > AI` with the Active AI toggle.
{% endhint %}

### Prompt Suggestions

Prompt Suggestions are contextual, AI-powered suggestions that activate Agent Mode. These banners will provide suggestions for what to ask Agent Mode in specific scenarios, similar to how Warp already suggests commands to run.

To disable, please visit `Settings > AI > Active AI > Prompt Suggestions`

<figure><img src="broken-reference" alt=""><figcaption><p>Example of inline banner popping up when relevant contextually.</p></figcaption></figure>

#### Accepting a Prompt Suggestion

If you press `CMD-ENTER` (on Mac), `CTRL-SHIFT-ENTER` (on Linux/Windows), or click on the chip, the suggestion will auto-populate into your input and run against [Agent Mode](https://docs.warp.dev/documentation/agents/using-agents) (with the most recent block attached).

{% hint style="info" %}
Prompt Suggestions use an LLM to generate prompts based on your terminal session, specifically the most recent block. These AI requests do not contribute towards your AI limits, however, any accepted prompts run in Agent Mode contribute as normal. Visit **Settings > AI > Active AI** if you'd like to turn it off.

If [Secret Redaction](https://docs.warp.dev/documentation/privacy/secret-redaction) is enabled, any selected regexes are applied to content sent to Active AI features to prevent any sensitive data being leaked.
{% endhint %}

<figure><img src="broken-reference" alt=""><figcaption><p>Setting for Prompt Suggestions</p></figcaption></figure>

### Next Command

Next Command uses AI to suggest the next command to run based on your active terminal session and command history. It uses your active terminal session contents and an LLM to generate commands.

To disable, please visit `Settings > AI > Active AI > Next Command`

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-289af9c9cd2fb02ca803eab4b469215a56ad851c%2FScreenshot%202024-12-12%20at%205.26.10%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Next Command is an LLM-based feature which utilizes your command history (enriched with git branch, exit code, and directory metadata) as well as recent block input and output to generate the next command suggestions.

[Secret Redaction](https://docs.warp.dev/documentation/privacy/secret-redaction) is automatically applied to any content sent to Active AI features to prevent any sensitive data being leaked.
{% endhint %}

#### Accepting Next Commands

Accept a Next Command Suggestion with `TAB` , `→` , or `CTRL-F` to add the suggested next command to your input buffer. `ENTER` executes the accepted command.

#### Billing

Next Commands are unlimited across all of Warp's plans, including the Free plan. For the latest information on other AI limits and other pricing details, visit [warp.dev/pricing](https://warp.dev/pricing).

### Suggested Code Diffs

Suggested Code Diffs automatically surface potential fixes for command-line errors encountered within Warp. These are most often compiler errors, but they may also include other situations where Warp can confidently predict a straightforward resolution, such as simple merge conflicts.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-0dabe7c7313fc92d98dbb646fc0f30e6a95faf93%2Fsuggested-code-diffs-generating-fix.png?alt=media" alt=""><figcaption></figcaption></figure>

When an error occurs, Warp evaluates whether it is appropriate for an LLM to generate a fix. If so, a “Generating fix” banner will appear while Warp prepares a proposed diff. You can stop this process at any time by pressing `CTRL + C` or the stop button.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a659d3c741620c94996bca9f732f68f09b39f984%2Fsuggested-code-diffs.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Using a Suggested Code Diff**

Once the diff is generated, you can either dismiss it or accept it. Acceptance can be done directly via the buttons in the diff view, or with `CMD + ENTER` on macOS and `CTRL + ENTER` on Windows/Linux.

You can also view additional details of the diff by pressing `CMD + E` (macOS) or `CTRL + E` (Windows/Linux), which expands the view to allow further inspection (including refining or editing it). You can also use `↓` to view the entire diff.

**Billing**

Suggested Code Diffs do not count toward your AI request limits. There are maximum limits to the number of code diffs surfaced per month, which scales based on your plan tier. For the latest details on plan limits and pricing, please visit [warp.dev/pricing](https://warp.dev/pricing).

## Active AI Privacy

See our [Privacy Page](https://docs.warp.dev/documentation/privacy/privacy) for more information on how we handle data with Active AI.


# Generate (Legacy)

Use natural language to look up commands or input, accessible either directly from the command line input or inside any interactive command or program.

## What is Generate?

Generate helps turn natural language queries into precise commands as terminal input or contextual suggestions inside interactive commands and programs, whether you're using psql, gdb, git, mysql, or any other CLI tool.

Generate is backed by Large Language Models from API providers like OpenAI and Anthropic, and are completely opt-in.

{% hint style="info" %}
Currently, you need to be online to use this feature. If this feature doesn't work, your ISP or firewall may be blocking the calls to `app.warp.dev`
{% endhint %}

## Ways to Generate with AI

### Generate commands as command line input

Type `#` on the command line input to generate command suggestions.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-7b0133ba50eb0441f47f6a75516f9779ec294e95%2FScreenshot%202024-06-15%20at%205.05.29%E2%80%AFPM.png?alt=media&#x26;token=a3885336-4e7e-4f40-9c47-0929743c4704" alt=""><figcaption><p>Typing '#' on the command line opens the suggestions interface</p></figcaption></figure>

{% embed url="<https://www.loom.com/share/424a763ef0c8455e8269e541301968f2>" %}
Generating commands as command line input demo
{% endembed %}

1. Press `` CTRL-` `` or type `#` into the text input editor to search using natural language.
2. Type in the input box what you'd like to do. For example, "replace a string in a file."
3. Results are generated in real-time, and you can keep the current prompt or modify the prompt to generate new commands.
4. When you've found the command you want to execute, it can be run or saved as a Workflow onto Warp Drive to easily recall it in the future.

### \[Legacy] Generate text and contextual suggestions in interactive CLIs

{% hint style="warning" %}
**Our legacy Generate feature which works in interactive CLIs has been replaced by** [full-terminal-use](https://docs.warp.dev/documentation/agents/full-terminal-use "mention")**, where Warp’s agent can now run and control long-running or full-screen terminal applications**. This includes debuggers, database shells, installers, and system monitors.\
\
The agent can provide input when prompted, navigate interactive screens, and continue execution without stalling.
{% endhint %}

In interactive CLI applications, you can generate input using natural language.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-871566298096cf5d5a414d6447ee934ad9a5f288%2Fgenerate-psql.png?alt=media" alt=""><figcaption><p>Generate a SQL query</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-338c694a332b866a25c1bde9795ac0bb733a0260%2Fgenerate-vim.png?alt=media" alt=""><figcaption><p>Generate Vim input</p></figcaption></figure>

{% tabs %}
{% tab title="macOS" %}

1. Inside a long-running, interactive command, press `CMD-I` when you see the hint text appear.
2. Type what you would like to generate in the input box. For example, "show me all tables in my Postgres database" or in Vim, "generate a recursive Fibonacci function and save it to the file."
3. Results are generated in real time using the [LLM of your choice](#supported-interactive-cli-models).
4. To refine or follow up on your query, press `CMD-Y`. You can then either edit your last message by pressing `UP ↑` or add a follow-up by typing in new text.
5. When you've found the text you want to add or execute, press `Enter` or click the Accept button.
   {% endtab %}

{% tab title="Windows" %}

1. Inside a long-running, interactive command, press `CTRL-SHIFT-I` when you see the hint text appear.
2. Type what you would like to generate in the input box. For example, "show me all tables in my Postgres database" or in Vim, "generate a recursive Fibonacci function and save it to the file."
3. Results are generated in real time using the [LLM of your choice](#supported-interactive-cli-models)
4. To refine or follow up on your query, press `CTRL-SHIFT-Y`. You can then either edit your last message by pressing `UP ↑` or add a follow-up by typing in new text.
5. When you've found the text you want to add or execute, press `Enter` or click the Accept button.
   {% endtab %}

{% tab title="Linux" %}

1. Inside a long-running, interactive command, press `CTRL-SHIFT-I` when you see the hint text appear.
2. Type what you would like to generate in the input box. For example, "show me all tables in my Postgres database" or in Vim, "generate a recursive Fibonacci function and save it to the file."
3. Results are generated in real time using the [LLM of your choice](#supported-interactive-cli-models)
4. To refine or follow up on your query, press `CTRL-SHIFT-Y`. You can then either edit your last message by pressing `UP ↑` or add a follow-up by typing in new text.
5. When you've found the text you want to add or execute, press `Enter` or click the Accept button.
   {% endtab %}
   {% endtabs %}

A couple of other examples of interactive CLIs where you can invoke Generate:

* **Database REPL** (e.g. `psql`, `mysql`, `sqlite`): Generate SQL queries such as "create a table to store user data" or "show me all the rows in orders for the last month"
* **Text editors** (e.g. `vim`, `nano`): Quickly generate text such as a markdown header, a code block comment, or a boilerplate CSS class.
* **Python REPL** (e.g. `ipython`, `python`): Quickly generate Python snippets such as "create a simple plot of x" or "write a unit test for this function"
* **Debugger tools** (e.g. `gdb`, `lldb`): Get commands for setting breakpoints or inspecting memory
* **Version control** (e.g. `git rebase -i`): Speed up complex git commands by describing your goal such as "interactively rebase master onto feature-branch"
* **Cloud provider shells** (e.g. `gcloud`, `aws cli`): faster setup or resource management such as "create a new Kubernetes cluster" or "provision a new RDS instance"

{% hint style="warning" %}
If you experience any issues with Generate, please visit known issues for [troubleshooting steps](https://docs.warp.dev/documentation/support-and-billing/known-issues#online-features-dont-work).
{% endhint %}


# Voice

Voice enables natural language interaction with Warp, letting you speak commands and queries directly to your terminal.

Warp's Voice feature transforms how you interact with your terminal, letting you naturally speak commands and questions instead of typing them. This is especially powerful when combined with Agent Mode for complex operations or when you need to explain longer scenarios.

{% hint style="info" %}
Voice input functionality can be configured in `Settings > AI > Voice`. You can toggle voice input and select your preferred activation hotkey from pre-defined options.
{% endhint %}

{% embed url="<https://www.loom.com/share/77399be4e434443488bbe267b3548552?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Voice Demo
{% endembed %}

## Getting Started with Voice

### Initial Setup

First-time users will need to grant microphone permissions:

* On macOS: Accept the system permission prompt or allow Warp microphone access in `System Settings > Privacy & Security > Microphone`
* On Windows: Allow Warp microphone access in `Settings > Privacy & Security > Microphone`
* On Linux: Configure through system sound settings

### Using Voice

There are two ways to activate Voice:

1. **Microphone Button in Agent Mode**
   * Click the microphone icon in Agent Mode
   * Start speaking when the indicator shows it's listening
   * Click again to stop recording
2. **Hotkey Method**

{% tabs %}
{% tab title="macOS" %}

* Press and hold the `Fn` key (configurable) to start recording
* Speak your command or query while holding the key
* Release the `Fn` key to stop recording and transcribe
  {% endtab %}

{% tab title="Windows" %}

* Press and hold the `ALT-RIGHT` key (configurable) to start recording
* Speak your command or query while holding the key
* Release the `ALT-RIGHT` key to stop recording and transcribe
  {% endtab %}

{% tab title="Linux" %}

* Press and hold the `ALT-RIGHT` key (configurable) to start recording
* Speak your command or query while holding the key
* Release the `ALT-RIGHT` key to stop recording and transcribe
  {% endtab %}
  {% endtabs %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8ec7b05f1abdfc4fa153e33dfde31bd2213efbc0%2Fvoice-settings.png?alt=media" alt=""><figcaption><p>Voice settings panel showing hotkey configuration and voice input toggle options</p></figcaption></figure>

### Sample use cases

Voice input makes complex interactions with Agent Mode more natural and efficient. Instead of typing lengthy queries, you can speak naturally to accomplish various tasks. For example, you might ask "Create a new Node.js project, install Express and MongoDB, then set up a basic server with a health check endpoint," or "What's the difference between chmod and chown? Give me examples of when to use each one."

You can also describe multi-step system tasks like "Find all log files in my project that contain errors from the last 24 hours, create a summary of the errors, and email it to me." Agent Mode will help break down these requests into the necessary commands and provide detailed explanations.

Voice input is not limited to just Agent Mode - it works across all of Warp's input interfaces. Whether you're using the Find dialog to search through text, entering commands in the terminal, or working with other input editors, you can use voice commands to quickly input your text.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f221503dbf54c309fa459017ce8809890a8b7c84%2Fvoice-in-find.png?alt=media" alt=""><figcaption><p>Voice input works across Warp's editor interfaces, including the Find dialog and other input editors</p></figcaption></figure>

## Privacy & Security

The transcription is powered by [Wispr Flow](https://wisprflow.ai/). Voice data is processed in real-time by Wispr Flow and is not retained as a recording after transcription.

## Usage Limits

Voice features have anti-abuse limits in place to ensure fair usage. These limits are subject to change as we continue to improve the service.

## Troubleshooting

### Common Issues

1. **Microphone not detected** If your microphone isn't being detected, first check your system permissions to ensure Warp has access. You should also verify that your microphone is properly connected to your system. If issues persist, try restarting Warp to reset the connection.
2. **Poor transcription quality** To improve transcription quality, try to minimize background noise in your environment. Position yourself closer to the microphone while speaking, and verify that your microphone input levels are properly adjusted in your system settings. For best results, speak clearly at a natural pace and use complete sentences to provide better context. When referring to specific file names or commands, enunciate them clearly. It's also recommended to review the transcription before sending to ensure accuracy.
3. **Feature not activating** If the Voice feature isn't activating, confirm that your hotkey settings are correctly configured in Warp. Check for any conflicting keyboard shortcuts that might interfere with Voice activation. Also ensure that you're running the latest version of Warp, as older versions may have compatibility issues.

   If you are on an Enterprise plan, your administrator may have disabled Voice functionality, or it may be pending approval.


# AI FAQs

Frequently asked questions about Warp's AI features, including supported models, privacy practices, credit limits, billing, and usage guidelines.

## General

### What data is sent and/or stored when using Agents in Warp?

See our [Privacy Page](https://docs.warp.dev/documentation/privacy/privacy) for more information on how we handle data used by Agents in Warp.

### What happened to the old Warp AI chat panel?

Agent Mode has replaced the Warp AI chat panel. Agent Mode is more powerful in all of the chat panel's use cases. Not only can Agent Mode run commands for you, it can also gather context without you needing to copy and paste. To start a similar chat panel, click the AI button in the menu bar to start on a new AI pane.

### Is my data used for model training?

No, Warp nor its providers (i.e. OpenAI, Anthropic, etc.) train on your data.

### What model are you using for Agent Mode?

Warp supports a curated list of LLMs from providers like OpenAI, Anthropic, and Gemini. To view the full list of supported models and learn how to switch between them, visit the [model-choice](https://docs.warp.dev/documentation/agents/using-agents/model-choice "mention") page.

### Can I use my own LLM API key?

Organizations on the Enterprise plan can enable a “Bring Your Own LLM” option to meet strict security or compliance requirements. Our team will work closely with you to support your preferred LLM provider. This feature is not currently available on other plans.

## Billing

Every Warp plan includes a set number of AI credits per user per month. Please refer to [pricing](https://www.warp.dev/pricing) to compare plans.

AI credit limits apply to Agent Mode, [Generate](https://docs.warp.dev/documentation/agents/generate), and [AI autofill in Workflows](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/workflows#ai-autofill). When you have used up your allotted credits for the cycle, you will not be able to issue any more AI credits until the cycle renews.

For questions around what counts as a AI credit, what counts as a token, and how often credits refresh, please refer to [ai-credits](https://docs.warp.dev/documentation/support-and-billing/plans-and-pricing/ai-credits "mention")and more on the [plans-and-pricing](https://docs.warp.dev/documentation/support-and-billing/plans-and-pricing "mention")page.

## Common AI error messages

#### **"Message token limit exceeded" error**

This error means your input (plus attached context) exceeds the maximum context window of the model you're using. For example, GPT-4o has a context window limit of 123,904 tokens. If you exceed that, you may receive no output.

To fix this, try:

* Starting a new conversation
* Reducing the number of blocks or lines attached to your query

#### **"Monthly request limit exceeded" or "Monthly credit limit exceeded" errors**

Once you exceed your AI credits on the Turbo plan (see [pricing](https://www.warp.dev/pricing) for current limits), premium models will be disabled until your quota resets at the start of your next billing cycle.

**Request failed with error: QuotaLimit**

Once you exceed your AI token limits, all models will be disabled. Note that credits and tokens are calculated separately, and even though the plans may have a set number of credits, they also have a limited number of tokens.

**Request failed with error: ErrorStatus (403, "Your account has been blocked from using AI features")**

This message means your account has been blocked from using AI features, typically due to a violation of our [Terms of Service](https://www.warp.dev/terms-of-service) or suspected abuse (e.g. attempting to bypass credit or token limits).

To resolve or clarify this, please contact our team at <appeals@warp.dev> if you believe this was an error. We'll review your case and respond as soon as possible.

{% hint style="warning" %}
Note that any error that does not mention <appeals@warp.dev> isn't related to being blocked and should be reported as feedback or a bug. See [sending-us-feedback](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback "mention") for more.
{% endhint %}

## Gathering AI debugging ID

In cases where you have issues with the Agent, we may ask for the AI debugging ID to troubleshoot the specific conversation. To gather the debugging ID, see [#gathering-ai-debugging-id](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback#gathering-ai-debugging-id "mention") for detailed steps.


# Code Overview

Warp enables intelligent code generation and editing through AI-powered diffs, allowing you to review, refine, and apply changes seamlessly across your codebase.

## From Prompt to Production

Warp Code is a suite of features designed to help you take agent-generated code from the initial prompt and project setup all the way to deployment and production. It is powered by Warp’s dedicated coding agent, which consistently ranks among the top results on [SWE-bench Verified](https://www.swebench.com/#verified) and [Terminal-Bench](https://www.tbench.ai/leaderboard).

In addition to Warp’s modern, [native code editor](https://docs.warp.dev/documentation/code/code-editor), it includes:

* [Codebase Context](https://docs.warp.dev/documentation/code/codebase-context) for accurate, context-aware agent responses
* [Project Rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules) and Commands to tailor agent behavior per repository
* A dedicated [Code Review](https://docs.warp.dev/documentation/code/code-review) experience for reviewing and editing diffs
* [Zero-state and setup flows](#getting-started-with-coding-in-warp) to quickly start a new project or initialize an existing one

### Coding Agent

Warp’s coding agent is designed to help you generate, edit, and manage code directly in the [Agentic Development Environment](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment). It detects opportunities to apply code diffs and surfaces them inline, allowing you to review and apply changes without switching to an external IDE. When you need to make manual edits, you can open Warp’s native code editor.

### How It Works

* **Prompt-driven coding**: You write natural language prompts such as *“Add a retry mechanism to this API call”* or *“Fix the failing unit test in auth.test.ts.”*
* **Inline code diffs**: When the agent proposes changes, it shows them as diffs you can inspect, modify, or reject.
* **Agent steering**: You can refine prompts, interrupt and retry, or attach context (such as a file, diff, or selection) to guide the agent toward better results.

{% embed url="<https://screen.studio/share/VwLoR3BE>" %}

{% hint style="info" %}
Warps coding agent only work on local repositories. The agent can make changes on remote or docker repositories, but fallback to using terminal commands (i.e. `sed`, `grep` ) to make the changes.
{% endhint %}

### Examples of Coding Capabilities

Code responds to prompts related to code generation, editing, and analysis. Here are some examples:

* **Code creation**
  * “Write a function in JavaScript to debounce an input”
  * “Generate a Python class for managing user sessions with Redis.”
* **Error-driven fixes**
  * “Fix the TypeScript error shown in the last build output.”
  * “Resolve this merge conflict by keeping backend changes and updating tests accordingly.”
* **Refactoring**
  * “Update all instances of var to let in this file.”
  * “Extract the database logic from app.js into a new db.js module and update imports.”
* **Multi-file and repo-wide changes**
  * “Add headers to all .py files in this directory.”
  * “Replace requests with httpx across the codebase, updating imports and error handling.”
* **Complex workflows** (examples shown below — in practice, prompts should include more detail for best results)
  * “Implement OAuth2 authentication, update affected routes, and add tests.”
  * “Identify functions without test coverage and create Jest test files for them.”
  * “Optimize slow SQL queries in queries.sql and regenerate migrations.”

{% embed url="<https://youtu.be/IuFSuOYstfg>" %}
How to kick off a coding task
{% endembed %}

{% embed url="<https://youtu.be/dm-P63USsVg>" %}
How to interpret & edit Warp’s coding output
{% endembed %}

## Getting Started With Coding in Warp

Warp provides multiple entry points to begin coding with agents, whether you are starting a new project, opening an existing one, or cloning from GitHub. Each new tab shows a **zero state** that lets you choose how to proceed.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a4cf0a11bc936300d5d2a00e21a5f59135bbf08b%2Fcode_mode.png?alt=media" alt=""><figcaption><p>Zero-state tab with 3 starting points for agentic coding in Warp.</p></figcaption></figure>

#### 1. Starting a New Project

To begin a new project, select `Create a New Project` from the tab. You can start directly with a prompt (Warp will suggest ideas) or configure the project manually. Warp sets up the repository with a `WARP.md` file containing [project rules](https://docs.warp.dev/documentation/knowledge-and-collaboration/rules#project-rules) and enables [codebase indexing](https://docs.warp.dev/documentation/code/codebase-context) to provide the agent with full context.

#### 2. Open an Existing Repo

Select `Open Repository` to use your computer’s file picker. If you choose a Git repository, Warp automatically changes into the directory and runs the `/init` setup command (a built-in “[slash command](https://docs.warp.dev/documentation/agents/slash-commands)”) if the repo has not already been initialized. Warp will detect the repository, index the codebase, and prepare it for coding.

* For non-Git folders, Warp simply changes into the directory without initialization.
* If you have an existing project that is not yet initialized, you can run `/init` manually to bootstrap it with a version-controlled `WARP.md` file.
* This view also shows a list of your three most recently used repositories and AI conversations for quick access, as well as a list of recent directories (which behave like running `cd`).

#### 3. Clone a Repo

Select `Clone Repository` to paste in a repo link or clone directly from GitHub. Warp places you in the cloned folder and automatically runs the `/init` flow to set up project rules and indexing.

## Learn More About Code Features:

* [Code Editor](https://docs.warp.dev/documentation/code/code-editor) - Warp’s built-in code editor lets you make quick, in-context edits with essentials like syntax highlighting, tabs, find and replace, Vim keybindings, and a file tree.
* [Codebase Context](https://docs.warp.dev/documentation/code/codebase-context) - Warp indexes your Git-tracked codebase to help Agents understand your code and generate accurate, context-aware responses. No code is stored on Warp servers.
* [Code Review](https://docs.warp.dev/documentation/code/code-review) - review, edit, and manage Git diffs in real time, with options to attach, revert, or open files directly.
  * You can also enter [Interactive Code Review](https://docs.warp.dev/documentation/code/code-review/interactive-code-review) to comment on changes, guide the agent, or adjust individual edits as they happen.
* [Code Diffs in Agent Conversations](https://docs.warp.dev/documentation/code/reviewing-code) - Learn how to review, refine, and apply code changes generated by Warp’s agents using the built-in visual diff editor.


# Code Editor

Warp’s built-in code editor lets you make quick, in-context edits with essentials like syntax highlighting, tabs, find and replace, Vim keybindings, and a file tree.

## Built-in Code Editor

Warp comes with a native code editor designed for quick, in-flow edits alongside your Agent conversations. Instead of switching back and forth to an IDE, you can open and edit files directly in Warp — with essentials like syntax highlighting, a tabbed file viewer, find and replace, Vim keybindings, and a file tree for browsing and adding files as context.

The editor is built for fast changes to agent-generated code: renaming a variable, tweaking copy, or rewriting a short function. Having just enough editing power in-context makes it easier to land an agent’s changes and keep momentum.

### Opening Files in Warp

**You can open files in the editor in several ways:**

1. **Click a file path** from the terminal output or an AI conversation and select "Open in Warp."
2. **Use the file menu in the command palette** (`CMD + O` on macOS, `CTRL + SHIFT + O` on Windows or Linux) when in a Git-tracked repo to search for and open files inside that repo.

   1. You can also access this via the magnifying glass icon in the pane coding toolbelt at the top left of any pane.

   <figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-68913a093169d16c73c8d451558165dc54fbd566%2Fsearch-files-icon.png?alt=media" alt=""><figcaption></figcaption></figure>
3. **Browse via the** [file-tree](https://docs.warp.dev/documentation/code/code-editor/file-tree "mention") to open or create files.
4. **Opening a generated code diff** from an Agent Conversation: [reviewing-code](https://docs.warp.dev/documentation/code/reviewing-code "mention").

{% embed url="<https://screen.studio/share/H7hTUgf2>" %}

**To save your changes to files**: use `CMD + S` on macOS or `CTRL + S` on Windows or Linux.

### Tabbed File Viewer

Warp can group multiple files into a single tabbed viewer, reducing clutter and making it easier to work across multiple files.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-30d23d44aaee5cf76e0b05db106c1d846e3eb500%2Ftabbed-file-viewer.png?alt=media" alt=""><figcaption></figcaption></figure>

* Enabled by default for new users (can be toggled in `Settings > Features > General > Group files into a single editor pane`)
* Reorder, close, or drag file viewers between tabs.
* Merge enter panes together by dragging one into another.

**Here's a more in-depth demo:**

{% embed url="<https://www.loom.com/share/a682461da66944f583e2fa3d27b71189?sid=679ce8f6-e530-4c0d-99ab-0613d1269f8b>" %}

### **File Layout Options**

Choose how new files open in Warp by default in: `Settings > Features > General > Choose a layout to open files in Warp`

* **Split pane**: new files open alongside the current editor
* **New tab**: new files open in their own tabbed viewer

### Supported Languages

The editor supports syntax highlighting and editing for a wide range of languages, including:

Rust, Go, YAML, Python, JavaScript/TypeScript, JSX/TSX, Java/Groovy, C++, Shell/Bash, C#, HTML, CSS, C, JSON, HCL/Terraform, Lua, Ruby, PHP, TOML, Swift, Kotlin, Starlark, SQL, Powershell, and Elixir.

We’re continuously expanding language support.

### Other Editor Features

Warp's native code editor also supports the following features:

* [file-tree](https://docs.warp.dev/documentation/code/code-editor/file-tree "mention") — Browse, open, and manage your project with Warp’s native file tree.
* [find-and-replace](https://docs.warp.dev/documentation/code/code-editor/find-and-replace "mention") — Use Warp’s built-in find and replace to quickly search across a file, jump between matches, and make precise edits with options for regex, case sensitivity, and smart case preservation.
* [code-editor-vim-keybindings](https://docs.warp.dev/documentation/code/code-editor/code-editor-vim-keybindings "mention") - Use Vim keybindings to edit code and text in Warp's native code editor.


# File Tree (Project Explorer)

Browse, open, and manage your project with Warp’s native file tree, complete with keyboard shortcuts, file icons, and context menu actions for files and folders.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-39320c4ee515f98d017a80234b2643627e73ca10%2Ffiletree-main.png?alt=media" alt=""><figcaption></figcaption></figure>

Warp includes a **native file tree** that makes it easy to explore and manage project files. The file tree is available whenever in any directory and it automatically reflects your project structure as files are added, removed, or changed.

### Opening the file tree

You can open the file tree from the tools panel on the left hand side:

* **Tools panel**: Click the Tools sidebar button, then open the File Tree tab (first tab in the panel).
* Press `CMD + \` to open the left panel, then assign your own shortcut for File Tree (and Warp Drive) in `Settings > Keyboard Shortcuts`.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b0938a3ca17c57a0c85ec12aa18b5d03ca726a4b%2Ffile-tree-project-explorer-tools-panel.png?alt=media" alt="" width="329"><figcaption></figcaption></figure>

{% hint style="info" %}
Warp supports icons for common file types. If a file type is missing an icon, please [file a GitHub issue](https://github.com/warpdotdev/Warp/issues) so we can review and add support.
{% endhint %}

### Browsing and opening files

Clicking on a file opens it directly in Warp’s [**native Code Editor**](https://docs.warp.dev/documentation/code/code-editor), where you can view and edit code in a separate pane or tab.

## File and Folder Actions

Right-clicking any **file** opens a context menu with several useful options:

* **Open in new pane**: Open the file in a side-by-side pane.
* **Open in new tab**: Open the file in a new tab.
* **Attach as context**: Insert the file into an agent prompt so the Agent can analyze or reference it.
* **Copy path**: Copy the absolute file path.
* **Copy relative path**: Copy the path relative to your current working directory.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6a53ac223a00996dc726ad69f21b08942a634e23%2Ffile-tree-context-menu.png?alt=media" alt=""><figcaption><p>Right-click context menu on a folder in the file tree.</p></figcaption></figure>

Right-clicking any **folder** opens a context menu with the following options:

* **Create new file**: Add a new file directly from the tree.

  <figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-af5ce16167eaedd311b54a5d8fbefd60468ca8aa%2Ffile-tree-new-file.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>
* **Attach as context**: Insert the selected file into your agent prompt so the Agent can analyze or reference it.
* **Copy path**: Copy the absolute file path to your clipboard.
* **Copy relative path**: Copy the path relative to your current working directory.


# Find and Replace

Use Warp’s built-in find and replace to quickly search across a file, jump between matches, and make precise edits with options for regex, case sensitivity, and smart case preservation.

## Find

Press `CMD-F` on macOS or `CTRL-SHIFT-F` on Windows and Linux to open the find menu. As you type, all matches in the file are highlighted, and the match closest to your cursor is selected.

* Press `ENTER` or use the down arrow to jump to the next match
* Press `SHIFT-ENTER` or use the up arrow to go to the previous match
* Click "Select All" to highlight all matches and close the menu

You can toggle regex and case-sensitive search options directly in the query editor.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-855117616ffd1d4361aaf770ac3388045616e48d%2Fcode-find-menu.gif?alt=media" alt="using find in the code editor"><figcaption><p>Using the find menu in Warp's Code Editor</p></figcaption></figure>

## Replace

Click the dropdown to the left of the find menu to open the replace options.

* Press Enter to replace the currently selected match
* Use Replace All to replace all matches

Toggle Preserve Case to keep the original casing of replaced text. Case is preserved in text that contains PascalCase, camelCase, hyphens, and underscores. For example:

* Replacing “old” with “new” will turn “Old” into “New” and “OLD” into “NEW”
* Replacing “oldValue” with “NewValue” will result in “newValue”
* Replacing “OldValue” with “newValue” will result in “NewValue”
* Replacing “my-Old-VALUE” with “my-new-value” will result in “my-New-VALUE”

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8e786a8f163bde3d9e695a1485e7f55d921222dd%2Fcode-replace-menu.gif?alt=media" alt="using replace in the code editor"><figcaption><p>Using the replace menu in Warp's Code Editor</p></figcaption></figure>


# Code Editor Vim Keybindings

Warp’s code editor now supports Vim keybindings, offering the same keyboard-driven experience available in the input editor — with a few additional commands tailored for editing code.

## About Vim keybindings

The Vi family of programs (including Vim and Neovim) are modal text editors that allow for keyboard-driven text editing. Vi-style keybindings are especially popular among developers for their speed and precision in navigating and manipulating code. Warp’s [code editor](https://docs.warp.dev/documentation/code/code-editor) now includes native support for Vim keybindings (also known as Vim mode), offering a familiar editing experience directly within your coding workflows.

### How to enable Vim Keybindings

Vim mode in the code editor uses the same setting toggle as the input editor. To enable:

* Through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), search for "Vim Keybindings".
* Through `Settings > Features > General`, toggle "Edit code and commands with Vim keybindings".

Unlike the input editor, the Vim implementation in the code editor starts in Normal mode.

### Customizing Keybindings

At the moment, Warp only supports default Vim keybindings.

One exception is the keyboard shortcut for exiting insert mode, which can be rebound under `Settings > Keyboard Shortcuts > Exit Vim Insert Mode`, or through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) search for "Exit Vim Insert Mode".

## Supported Keybindings

Below is a list of the vim functionality implemented in Warp so far.

### Movement

See [Vim docs: motion](https://vimdoc.sourceforge.net/htmldoc/motion.html) for more information.

#### Basic

| Command(s)                   | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| `h`, `j`, `k`, `l`           | single-char movement                                |
| `<space>`, `<backspace>`     | single-char movement with line wrap                 |
| `w`, `W`, `b`, `B`, `e`, `E` | word movement                                       |
| `ge`, `gE`                   | end of previous word                                |
| `$`                          | end of line                                         |
| `0`                          | beginning of line                                   |
| `^`                          | first non-whitespace character of line              |
| `%`                          | jump to matching bracket                            |
| `[`, `]`                     | prev/next unmatched bracket                         |
| `_`                          | beginning of the current line                       |
| `+`                          | first non-whitespace character of the next line     |
| `-`                          | first non-whitespace character of the previous line |
| `{`, `}`                     | prev/next paragraph                                 |

#### Multi-line-related

| Command(s) | Description             |
| ---------- | ----------------------- |
| `gg`, `G`  | jump to first/last line |

### Editing

| Command(s) | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| `r`        | replace character under cursor                              |
| `d`, `D`   | delete a range or object                                    |
| `c`, `C`   | change a range or object (delete, then go to insert mode)   |
| `s`, `S`   | substitute (like change, but can only delete at the cursor) |
| `x`, `X`   | delete under cursor                                         |
| `y`, `Y`   | yank (copy) into the clipboard                              |
| `p`, `P`   | paste from the clipboard                                    |
| `u`, `⌃r`  | undo, redo                                                  |
| `~`        | toggle upper/lowercase under cursor                         |
| `gu`       | lowercase under cursor (`u` in visual mode)                 |
| `gU`       | uppercase under cursor (`U` in visual mode)                 |
| `J`        | join current and following lines                            |
| `.`        | repeat last edit                                            |
| `gcc`      | toggle comments on current line                             |
| `gc`       | toggle comments on visual selection                         |

See [Vim docs: editing](https://vimdoc.sourceforge.net/htmldoc/editing.html) for more information.

#### Text Objects

| Command(s)       | Description                                |
| ---------------- | ------------------------------------------ |
| `i`              | inner (exclude delimiters in text object)  |
| `a`              | around (include delimiters in text object) |
| `w`, `W`         | whitespace-delimited string (word)         |
| `"`, `'`, \`\`\` | quote-delimited string                     |
| `(`, `{`, `[`    | parenthesized/bracketed string             |

See [Vim docs: text objects](https://vimdoc.sourceforge.net/htmldoc/motion.html#text-objects) for more information.

### Search

#### Character Search

| Command(s)         | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `t`, `T`, `f`, `F` | find next/prev matching character on line              |
| `;`                | repeat last character search in the same direction     |
| `,`                | repeat last character search in the opposite direction |

See [Vim docs: left-right motions](https://vimdoc.sourceforge.net/htmldoc/motion.html#f) for more information.

#### General Search

Unlike Vim, general search commands don't search within the buffer. Instead, they open Warp's native command search.

| Command(s)         | Description              |
| ------------------ | ------------------------ |
| `/`, `?`, `*`, `#` | open Warp command search |

### Mode Switching

| Command(s) | Description                                                       |
| ---------- | ----------------------------------------------------------------- |
| `i`        | insert text before the cursor                                     |
| `I`        | insert text before the first non-whitespace character in the line |
| `a`        | append text after the cursor                                      |
| `A`        | append text at the end of the line                                |
| `o`        | begin new line below the cursor and insert text                   |
| `O`        | begin new line above the cursor and insert text                   |
| `v`        | visual character mode                                             |
| `V`        | visual line mode                                                  |

See [Vim docs: insert](https://vimdoc.sourceforge.net/htmldoc/insert.html#insert) and [Vim docs: visual mode](https://vimdoc.sourceforge.net/htmldoc/visual.html#visual-mode) for more information.

### Registers

| Command(s) | Description     |
| ---------- | --------------- |
| `"`        | register prefix |

Warp currently supports the following registers:

| Register name    | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| `a`–`z`, `A`–`Z` | named registers                                                  |
| `+`              | system clipboard                                                 |
| `*`              | system clipboard                                                 |
| `"`              | unnamed register, containing the text of the last delete or yank |

See [Vim docs: registers](https://vimdoc.sourceforge.net/htmldoc/change.html#registers) for more information.

## Feedback

The best way to report bugs and request features is through Warp's [GitHub Issues](https://github.com/warpdotdev/Warp/issues) page. Please note that the issue or request is for Vim Keybindings.


# Code Review

The Code Review panel lets you review, edit, and manage Git diffs in real time, with options to attach, revert, or open files directly.

## Overview

When you are working locally in a Git repository with uncommitted changes, the **Code Review panel** lets you inspect, edit, and manage code changes directly inside Warp. It integrates with Git and Warp's Agents, giving you the ability to:

* Review diffs and attach them as context for the Agent
* Apply, edit, or revert changes in real time
* See changes made outside of Warp or by Warp's Agents automatically reflected

Any uncommitted changes appear in the panel (or compare the changes on your branch against `main` or `master` ). Switching branches or saving files updates the panel instantly, so it always reflects the current state of your codebase.

{% embed url="<https://www.loom.com/share/96581523168742eb9b95c3973924728c?sid=a3ee9164-4274-4468-ac32-38ce6807f9a8>" %}
Code Review Demo
{% endembed %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-380b08f2356cdb3390646691e30c929cba0d0025%2Fcode-review-panel-update.png?alt=media" alt=""><figcaption><p>Full view of Code Review panel and terminal pane.</p></figcaption></figure>

{% hint style="info" %}
To review agent-generated diffs, leave inline comments, batch your feedback, and have the agent apply all requested changes, see [interactive-code-review](https://docs.warp.dev/documentation/code/code-review/interactive-code-review "mention").
{% endhint %}

## Opening the Code Review panel

The Code Review panel can be opened in several ways. Each entry point makes it easy to inspect and manage changes without leaving your workflow.

{% hint style="success" %}
You can also open the Code Review panel with `CMD – SHIFT – +` on macOS or `CTRL – SHIFT – +` on Windows and Linux.
{% endhint %}

#### 1. Universal Input: Git diff chip

In the [universal-input](https://docs.warp.dev/documentation/terminal/universal-input "mention") editor, when you’re in a Git repository with changes, the chip shows the number of files modified along with lines added and removed. Clicking the chip opens the Code Review panel with the relevant diffs.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-7c440f8e587ca77a4b3dbd040902306cecf80a77%2Fwhole%20UDI%20bar.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-cf1d23a5793eb9d59594623b9d682f41fdf74ca1%2Fgit%20chip%20tooltip%201.png?alt=media" alt=""><figcaption></figcaption></figure>

#### 2. Agent Conversation: Review Changes Button

When an Agent makes code edits in an [agent-conversations](https://docs.warp.dev/documentation/agents/using-agents/agent-conversations "mention"), a `Review changes` button appears at the bottom of the conversation. Clicking it opens the code review panel.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-62fa47f13942e16b39a009c7ac4ed14d3147536d%2FBlocklist%20with%20review%20changes.png?alt=media" alt=""><figcaption><p>Review changes at bottom of Agent Conversation.</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-593ea47a3a2df70aef6409d3cb350be43fcc003c%2Freview%20changes%20in%20footer.png?alt=media" alt=""><figcaption></figcaption></figure>

#### 3. Agent Conversation: Toolbelt (Bottom Right)

During an Agent conversation, you can view all changed files in the toolbelt chips at the persistent bottom right. From there, you can open the Code Review panel directly.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-9026ae0da1e5f81fb45160a4dcebf0b81090ad4c%2Fai_control_panel_buttons_larger_view.png?alt=media" alt=""><figcaption></figcaption></figure>

#### 4. Warp Tab Bar

In any Git-tracked repository, you can open the Code Review panel by clicking the plus/minus icon in the top-right corner of Warp, next to your avatar.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-11a3ccd59f79cced7f18a9ef03c583efa39594e2%2Fwarp-tab-bar-review-code.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Viewing All Edited Files

Inside the Code Review panel, you can open the file sidebar to browse all changed files in your repository. Clicking on a file will automatically scroll to that file in the panel.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6b0cfb0199c6310f6c6bbc3f7ef5c5567e663375%2Fwhole%20git%20diff%20view%20with%20one%20file%20collapsed.png?alt=media" alt=""><figcaption><p>Viewing all edited files in the code review panel, with the file sidebar open.</p></figcaption></figure>

{% hint style="info" %}
By default, the Code Review panel opens as a pane on the right, but you can drag it to reposition wherever you prefer.
{% endhint %}

## Reviewing diffs

By default, the Code Review panel shows all **uncommitted changes** on your current branch, excluding changes to files ignored by `.gitignore`.

Warp offers two ways to review changes:

1. **Uncommitted changes**: view all edits you've made locally on the current branch.
2. **Changes vs. main**: compare your branch against `main` or `master` to see what would be included in a pull request to that branch, for instance.
   1. Warp automatically detects the target branch and updates the comparison accordingly.
3. **Changes vs. another branch**: compare your work against any arbitrary branch for stacked PRs, feature comparisons, or alternate base branches.

You can manually switch between the two views either in the Code Review panel or via the unviersal input chip:

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-067d344b4753797939eb64d41ec32927fb7477af%2Fdiff%20dropdown%20to%20change%20base%20from%20the%20code%20review%20pane.png?alt=media" alt=""><figcaption><p>Changing diff view in the Code Review Panel.</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-1e4414371c81d16b3ea0fe67ce8aea1bef8f6a2e%2Fgit%20diff%20change%20base%20dropdown.png?alt=media" alt=""><figcaption><p>Changing diff view in the Universal input.</p></figcaption></figure>

<div data-full-width="false"><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-c0aacdd7d981e5adaa4bc8ce65f63e70fe7190ff%2Farbitrary-branch-diff.png?alt=media" alt="" width="298"><figcaption><p>Changing diff view against an arbitrary branch.</p></figcaption></figure></div>

Any saved edits made outside of Warp (e.g. in another editor), as well as changes applied by Warp's Agents, appear automatically. The panel updates in real time, ensuring it always reflects the current state of your working file and directory.

#### Attaching diffs as context

The Code Review pane makes it simple to share changes with the Agent. You can attach an entire diff to a prompt so the Agent has full visibility into what was added or removed.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d7bca69edda163d79e0a4954554049ce55fd2c0e%2Fattach-diff-hunk-as-context.png?alt=media" alt="" width="299"><figcaption><p>Attaching a diff as context from the Code Review panel.</p></figcaption></figure>

This ensures responses are grounded in your latest edits, whether you’re asking for feedback, explanations, or follow-up changes. For more details, see [selection-as-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/selection-as-context "mention").

#### Reverting diffs

The Code Review panel lets you easily undo changes at different levels. In the gutter next to each diff, you’ll see an option to revert a hunk: roll back a specific set of changes (a “diff hunk”) within a file. This removes the added or modified lines and restores the previous version.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f53f6912cf72da635fec9fc6ff5dd9bafbfc66c2%2Frevert%20diff%20hunk.png?alt=media" alt=""><figcaption></figcaption></figure>

When you revert, the changes are immediately updated in your working directory. The file is restored to match the selected version, so you can continue editing or commit without the reverted code.

### Opening Files from Code Review

In addition to reviewing and editing diffs directly in the Code Review pane, you can open a file directly in Warp’s [code-editor](https://docs.warp.dev/documentation/code/code-editor "mention"). Each file listed in the Code Review pane includes an expand button in the top-right corner of its diff view.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-07c81eaffe1eedb328e4f21d39ebdf613a5b95b6%2Fcode-review-header.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

* Clicking the **expand button** (right-most button on the header) opens the file in a new editor tab, allowing you to see the full file beyond just the changed lines.
  * This is useful when you need additional context around a diff, want to make broader edits, or prefer working in the full editor rather than inline.
* Once opened, the file behaves like any other editor tab: you can scroll, edit, search, and save.
* Any changes made in the editor automatically sync back into the Code Review pane, so the diff view always stays current.

**Note**: from this code review file header, you can also attach a file diff as context into Warp's agent, or discard all the changes on a single file.

#### Directly editing code diffs

Alternatively, from the Code Review panel, you are able to click and edit the diffs directly:

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-fa033b4ef71089a7b7682bed39f04fdbd9b15898%2Fdirectly-editing-diffs.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Discarding all changes

The Code Review panel also lets you discard every uncommitted change on your branch in one action. Clicking Discard all removes all local modifications shown in the panel and restores each file to its state on the base branch. This is useful when you want to reset your working directory, abandon a set of edits, or start a new iteration from a clean slate.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ee4807923d6ff3bf13139f1d787c8288ed1d446b%2Fdiscard-all-changes.png?alt=media" alt="" width="348"><figcaption></figcaption></figure>

Discarding changes will ask you confirm, but still make sure you’ve saved or backed up anything you want to keep before using it.


# Interactive Code Review

Interactive Code Review lets you review agent-generated code, leave inline comments, and have the agent apply all your feedback in one pass.

### Overview

Interactive Code Review lets you review, annotate, and refine code generated by Warp's agents. Instead of relying on an AI to review another AI's output, Warp keeps the developer in control.

You can inspect diffs, leave inline comments, batch feedback, and send all requested changes back to the agent in a single pass.

{% embed url="<https://youtu.be/jit_6eevt8w?si=EFKYUSsofvBYUPI->" %}

**Interactive Code Review builds on Warp’s existing** [](https://docs.warp.dev/documentation/code/code-review "mention") **panel.** For details on diff views, reverting hunks, opening files, and all available entry points, see the Code Review documentation.

{% hint style="info" %}
Note that both the [](https://docs.warp.dev/documentation/code/code-review "mention") panel and Interactive Code Review require working in a Git-indexed directory.
{% endhint %}

***

When an agent modifies files, Warp automatically gathers those edits into a diff. Opening the Code Review panel shows you every change the agent made.

From there, you can leave comments on specific lines or blocks, review your comment list, and submit all feedback to the agent at once. The agent applies the requested updates and returns an updated diff for further review.

This gives you a familiar pull-request style workflow inside Warp without switching editors or tools.

### Leave inline comments

Select any changed line or block and add a comment describing what you want adjusted. Warp anchors each comment to the relevant file and line so the agent understands exactly what to fix.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6d67e7a7945b5f699ea7856311dba5434c67e96a%2Finteractive-code-review-adding-comment.png?alt=media" alt=""><figcaption></figcaption></figure>

### Batch comments and submit once

Add as many comments as you need before submitting them. The agent receives your entire batch of feedback, applies the changes in one iteration, and returns an updated diff for verification.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-48389133fc3d7eee365bbfcf9e2434c133839af5%2Finteractive-code-review-batch-comments.png?alt=media" alt=""><figcaption></figcaption></figure>

### Example demo

In the example from Kevin on the Warp team, you’ll see how to:

* open the Code Review panel after an agent produces changes
* browse the diffs for each edited file
* add multiple inline comments
* review all comments in the list view
* send those comments to the agent for resolution
* inspect the updated diffs once the agent applies the changes

This workflow can be repeated until the code matches your expectations.

{% embed url="<https://www.loom.com/share/bdeb2eb1ff3640faa2cbacda9420c3a8>" %}


# Codebase Context

Warp indexes your Git-tracked codebase to help Agents understand your code and generate accurate, context-aware responses. No code is stored on Warp servers.

Codebase Context helps Warp Agents understand your project by indexing your local codebase. This allows Agents to generate more accurate completions, suggest context-aware edits, and answer questions using real knowledge of your code.

{% hint style="info" %}
Code indexed with Codebase Context is never stored on our servers. Warps coding agent only work on local repositories. The agent can make changes on remote or docker repositories, but fallback to using terminal commands (i.e. `sed`, `grep` ) to make the changes.
{% endhint %}

{% hint style="danger" %}
**Codebase context doesn't work within SSH or WSL sessions.**\
\
Feature requests for support are being tracked in the following Github issues:\
\- SSH: <https://github.com/warpdotdev/Warp/issues/6831>\
\- WSL: <https://github.com/warpdotdev/Warp/issues/6744>
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-caec9a890fdca582d43b9d519c28db26e677b687%2Fcodebase-context-main.png?alt=media" alt=""><figcaption><p>Codebase indexing settings in Warp. Easily track sync status and manage which folders are indexed for AI-powered context and suggestions.</p></figcaption></figure>

## Indexing your codebase

When you open a directory in Warp, we check if it is part of a Git repository. If it is, Warp begins indexing the source code to provide rich context for Warp Agents.

**Codebase indexing intervals and triggers:**

* Initially when you have Codebase Context enabled.
* Warp automatically triggers a codebase index periodically.
* Whenever a new Agent conversation begins.
* When you click on the sync 🔄 button in `Settings > Code` menu.

**This embeddings index helps Agents:**

* Understand your project structure and reference relevant code
* Generate completions that match your style and patterns
* Suggest edits in the correct locations based on real context

For large projects, indexing may take a few minutes. Warp Agents will not use codebase context until indexing is complete, but **agentic coding features remain fully available in the meantime**.

{% hint style="info" %}
You can view and manage your indexed codebases under `Settings > Code > Codebase Index`. You can also choose whether to automatically index new folders as you navigate them.
{% endhint %}

{% embed url="<https://youtu.be/11rz9OYQ8Hg>" %}

### **Codebase indexing states**

When viewing indexed codebases in Warp under `Settings > Code`, you may see different status indicators:

* **Synced** — Indexing is complete and the codebase is ready to be used as context.
* **Discovering files** – Warp is currently scanning and indexing files in the codebase.
* **Failed** – Indexing failed. Common reasons include unreadable `.git` directories or corrupted repositories. Try re-cloning the repo and syncing again.
* **Codebase too large** – The number of files in the codebase exceeds your current plan’s limit. You can either reduce the number of files being indexed using `.warpindexingignore`, or [contact sales](https://warp.dev/contact-sales) for support with larger codebases.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-dba9d09e439e026a99ba9352675835c6691b4fe4%2Fcodebase-context-statuses.png?alt=media" alt=""><figcaption><p>View and manage the indexing status of your codebases in Warp. Easily see which projects are synced, in progress, or require attention.</p></figcaption></figure>

### When does codebase syncing happen?

Warp automatically triggers a codebase sync initially and periodically, when you click on the sync 🔄 button in `Settings > Code` menu, or when you start a new Agent conversation. However, if many files have changed or the network is slow, the sync may not complete before the Agent tries to access context.

{% hint style="info" %}
In large projects (e.g. after a branch switch), there may be a short delay where the Agent references stale or outdated files.
{% endhint %}

### File and Codebase Limits

The number of codebases you can index and the maximum number of files per codebase vary by plan. All plans support indexing **at least 5,000 files per codebase**, with higher tiers including support for more files and additional codebases.

For full details, visit our [pricing page](https://www.warp.dev/pricing).

### Ignore files

For large codebases, Warp supports several ignore files to give you control over what gets indexed. This allows each developer to focus context on the parts of the codebase most relevant to their work.

Warp respects the following ignore files:

* `.gitignore`
* `.warpindexingignore`
* `.cursorignore`
* `.cursorindexingignore`
* `.codeiumignore`

Use these files to skip indexing of folders, generated files, or any content you don't want agents to reference. This can improve performance and result quality.

{% hint style="info" %}
Files excluded by ignore rules **do not** count toward your codebase's file limit.
{% endhint %}

## Multi-repo context

Warp supports referencing context across multiple indexed repositories. Note that you don’t need to be inside a specific repo for agents to use its context.

**This is especially useful when:**

* Implementing a feature across multiple repos, such as full-stack work across client and server
* Using one repo as a reference while building in another, for example: “copy the implementation from repo A into my repo B”

Agents will only reference other repositories if they are already indexed. During cross-repo tasks, Warp's Agents have access to the file paths of all indexed repos. It is more likely to use cross-repo context when you mention the exact name of the repo in your prompt.

## Demo: Explain My Codebase with Warp

Here's an example from [Warp University](https://www.warp.dev/university), where Zach demonstrates how Warp uses Codebase Context to search for and use the relevant files as context:

{% embed url="<https://www.youtube.com/watch?v=11rz9OYQ8Hg>" %}


# Code Diffs in Agent Conversations

How to review, refine, and apply code changes generated by Warp’s Agents with the built-in diff editor in Agent Conversations.

## Reviewing Code Diffs

During an Agent Conversation, Warp can generate code diffs that open directly in a built-in diff editor.

This lets you review proposed changes line by line, refine them with natural language, or make manual edits before choosing whether to apply them. It’s a fast, transparent way to stay in control of agent-generated code.

**Note**: If the `Apply Code Diffs` permission is set to `Agent decides` or `Always allow` in [agent-profiles-permissions](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions "mention"), code diffs will not be surfaced for you to review. If it’s set to `Always ask`, you’ll always be prompted to review them.

{% hint style="info" %}
Code diffs generated by Warp are never stored on our servers. Warps coding agent only work on local repositories. The agent can make changes on remote or docker repositories, but fallback to using terminal commands (i.e. `sed`, `grep` ) to make the changes.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b46a55cb41760b643577d70244140211ccd0291a%2Fgenerated_blocklist_diff.png?alt=media" alt=""><figcaption><p>A code diff surfaced in an Agent Conversation.</p></figcaption></figure>

You can also choose whether Warp automatically opens the [code-review](https://docs.warp.dev/documentation/code/code-review "mention") panel the first time you accept a diff in a conversation. This behavior can be toggled in `Settings > Features > General > Auto-open Code Review Panel`.

## **Navigating and applying diffs**

When a Warp Agent generates a code diff, Warp opens it in a built-in text editor with a visual diff view. Changes are grouped into clear hunks for easy inspection.

* Use the `UP` and `DOWN` arrow keys (or mouse clicks) to move between hunks.
* For multi-file changes, use `LEFT` and `RIGHT` arrow keys to switch between files.
* Once satisfied with the changes, you can apply the diffs using `ENTER` or clicking "**Accept Changes**" to apply the modifications.

{% hint style="warning" %}
These modifications will not be applied to the files unless you explicitly accept them.
{% endhint %}

## **Refining or editing the diffs**

If the initial suggestion needs more work:

* Press `R` or select the "**Refine**" button to provide follow-up instructions in natural language. The agent will regenerate the diff based on your input.
* To manually adjust the code, press `E` or click "**Edit**" to switch into an editable view.
* To cancel a pending operation, use `CTRL-C` (on Mac, Windows, or Linux systems). Similarly, you can exit the editor at any time with `ESC` .

{% hint style="info" %}
You can open up code files in Warp in various different ways, refer to: [#opening-files-in-warp](https://docs.warp.dev/documentation/code-editor#opening-files-in-warp "mention")
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-3e295beac4f441f221dddee6b480b4d3ea792ffa%2Feditting_diff.png?alt=media" alt=""><figcaption><p>Editing the code diff directly in Warp's native code editor.</p></figcaption></figure>

### Demo: Editing Agent Code in Warp

Here's an example from [Warp University](https://www.warp.dev/university), where Zach demonstrates a how to review and edit Agent code diffs natively in Warp:

{% embed url="<https://www.youtube.com/watch?time_continue=111&v=dm-P63USsVg>" %}


# Universal Input

Warp’s Universal Input unifies shell commands, agent prompts, and contextual tools into one editor built for modern coding with agents.

The **Universal Input** is the main input interface for using Warp. It accepts both terminal commands and natural language [Agent](https://docs.warp.dev/documentation/agents/agents-overview) prompts, letting you run shell workflows and kick off agentic tasks from the same place.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-766a60f8279296a57ecf75be97c6f290c3a0fcfc%2Funiversal-input-header.png?alt=media" alt=""><figcaption><p>The Universal Input with an Agent prompt and multiple contextual chips active.</p></figcaption></figure>

{% embed url="<https://www.youtube.com/watch?v=4c05OEqzQIA>" %}
Using the Universal Input
{% endembed %}

### Breaking down the Universal Input

The Universal Input brings together all of Warp's input features into one streamlined editor:

* **Natural language auto-detection**: Warp can automatically detect when you're writing in plain English, as opposed to a shell command, and switch you into [Agent Mode](https://docs.warp.dev/documentation/agents/using-agents#what-is-agent-mode).
* **Contextual chips**: See your current directory, previous conversations, Git status, node version, and more, all inline with your input.
* [**Modern text editing**](https://docs.warp.dev/documentation/terminal/editor): Enjoy IDE-like editing features such as [completions](https://docs.warp.dev/documentation/terminal/command-completions), [syntax highlighting](https://docs.warp.dev/documentation/terminal/editor/syntax-error-highlighting), mouse support, [rectangular selection](https://docs.warp.dev/documentation/terminal/more-features/text-selection), and [Next Command](https://docs.warp.dev/documentation/agents/active-ai) predictions.
* **Input toolbelt**: Quickly access [@-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/using-to-add-context), [Slash Commands](https://docs.warp.dev/documentation/agents/slash-commands), [voice input](https://docs.warp.dev/documentation/agents/voice), [image attachments](https://docs.warp.dev/documentation/agents/using-agents/agent-context/images-as-context) as context, and other AI features.

If you prefer a more traditional terminal input experience, you can switch to [Classic Input](https://docs.warp.dev/documentation/terminal/universal-input/classic-input) in `Settings > Appearance > Input`. Classic input also supports oh-my-posh, PS1 customizations, and [same line prompt.](https://docs.warp.dev/documentation/appearance/prompt#same-line-prompt)

## Input Modes

The Universal Input supports three modes, shown in the input switcher:

#### 1. Agent Mode (natural language)

Ask Warp's agent to build, debug, or run tasks in natural language. Warp uses leading LLMs to interpret your request, run the right commands, surface code diffs, and stream results directly into your session.

*Indicator:* Agent icon is highlighted in the switcher.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-44313f3ec0b837a7e2511a5697ef9ccfc20df579%2Fagent-mode-locked-universal-input.png?alt=media" alt=""><figcaption><p>Universal Input locked in Agent Mode.</p></figcaption></figure>

#### 2. Terminal Mode (shell commands)

Enter shell commands just like any terminal, with the benefit of Warp’s modern editor features—completions, syntax highlighting, error underlining, and more included.

*Indicator*: Terminal icon highlighted in the switcher

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-333abe5879df0e4996845818c6533a815b814c05%2Funiversal-input-terminal-mode.png?alt=media" alt=""><figcaption><p>Universal Input locked in Terminal Mode.</p></figcaption></figure>

#### 3. Auto-detection Mode

Warp automatically detects whether your input is natural language or a shell command. You can stay in detection mode or explicitly lock into Terminal or Agent Mode.

*Indicator*: Neither mode highlighted.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d5dcbebd1f2e208464691577da766cc4b778b3d7%2Fzero-state-universal-input.png?alt=media" alt=""><figcaption><p>Universal Input in an empty / zero state.</p></figcaption></figure>

When Warp detects an input type, the input switcher softly highlights the corresponding mode.

| Agent (natural language) mode detected                                                   | Terminal (shell) mode detected                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div><figure><img src="broken-reference" alt=""><figcaption></figcaption></figure></div> | <div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4a1d11df3d7a2172061b4cf4fdbd71a358244451%2Fauto-detection-terminal-mode.png?alt=media" alt=""><figcaption></figcaption></figure></div> |

{% hint style="info" %}
The model Warp uses to detect natural language automatically is completely local.
{% endhint %}

#### Disabling Natural Language Auto-detection

By default, auto-detection is enabled. This means Warp decides whether to treat your input as a command or an Agent prompt.

* **To turn off auto-detection**: go to `Settings > AI > Input > Natural Language Detection`
* When disabled: You’ll explicitly be in either Terminal or Agent Mode. Use the following keyboard shortcuts to switch between modes:
  * `CMD+I` (macOS)
  * `CTRL+I` (Windows/Linux)

| Agent (natural language) mode enabled                                                                                                                                                                                                                                                              | Terminal (shell) mode enabled                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-3347460337471dc4b017a308c4deabf46f9da05d%2Fauto-detection-off-terminal-mode.png?alt=media" alt=""><figcaption></figcaption></figure></div> | <div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-18af28c161f1ef2a6277fb3fae7b21009cf1f4ac%2Fauto-detection-off-agent-mode.png?alt=media" alt=""><figcaption></figcaption></figure></div> |

### Entering Agent Mode

[Agent Mode](https://docs.warp.dev/documentation/agents/using-agents) is how you interact directly with Warp’s AI to ask questions, run tasks, and collaborate in natural language. There are multiple ways to enter Agent Mode depending on where you are in your workflow:

{% tabs %}
{% tab title="macOS" %}

* **Type natural language directly**: If auto-detection is enabled, you can type a task or question into the input, and Warp will recognize it as natural language using its local auto-detection feature.
* **Use keyboard shortcuts**: Quickly toggle into Agent Mode with `CMD + I`.
* **Attach blocks to a prompt**: From any block you want to use as context, click the ✨ icon in the toolbelt or select "Attach block(s)" to AI query from the block’s context menu.
* **Force a mode with special characters**:
  * `!` at the start of input forces Terminal Mode.
  * `*` at the start of input forces Agent Mode.
* **Switch modes manually**: Click the Agent icon in the input switcher to lock into Agent Mode, or click the terminal icon to switch to Terminal Mode.
  {% endtab %}

{% tab title="Windows" %}

* **Type natural language directly**: If auto-detection is enabled, you can type a task or question into the input, and Warp will recognize it as natural language using its local auto-detection feature.
* **Use keyboard shortcuts**: Quickly toggle into Agent Mode with `CTRL + I`.
* **Attach blocks to a prompt**: From any block you want to use as context, click the ✨ icon in the toolbelt or select "Attach block(s)" to AI query from the block’s context menu.
* **Force a mode with special characters**:
  * `!` at the start of input forces Terminal Mode.
  * `*` at the start of input forces Agent Mode.
* **Switch modes manually**: Click the Agent icon in the input switcher to lock into Agent Mode, or click the terminal icon to switch to Terminal Mode.
  {% endtab %}

{% tab title="Linux" %}

* **Type natural language directly**: If auto-detection is enabled, you can type a task or question into the input, and Warp will recognize it as natural language using its local auto-detection feature.
* **Use keyboard shortcuts**: Quickly toggle into Agent Mode with `CTRL + I`.
* **Attach blocks to a prompt**: From any block you want to use as context, click the ✨ icon in the toolbelt or select "Attach block(s)" to AI query from the block’s context menu.
* **Force a mode with special characters**:
  * `!` at the start of input forces Terminal Mode.
  * `*` at the start of input forces Agent Mode.
* **Switch modes manually**: Click the Agent icon in the input switcher to lock into Agent Mode, or click the terminal icon to switch to Terminal Mode.
  {% endtab %}
  {% endtabs %}

When you’re in Agent Mode, the **Agent icon** will be highlighted in the [universal-input](https://docs.warp.dev/documentation/terminal/universal-input "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-459e3d0871237902108a86d93231039a60126d95%2Fusing-agents-universal-input.png?alt=media" alt=""><figcaption><p>The Agent icon in the Universal input indicates that Agent Mode is active.</p></figcaption></figure>

In Classic Input, you’ll also see a ✨ sparkles indicator inline.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f886e83dea97c4d46e3af7e2ee5274d8da4c79a1%2Fundo_my_git_commit.png?alt=media" alt="The sparkles on the command line indicate Agent Mode is active."><figcaption><p>The sparkles in the Classic input indicates that Agent Mode is active.</p></figcaption></figure>

By default, entering Agent Mode starts you in *Pair Mode*, where you can continue an ongoing conversation by asking follow-up questions or assigning tasks. From here, you can ask the agent to build, debug, fix, or even deploy code as needed.

### Exiting Agent or Terminal Modes

You can leave Agent or Terminal Modes in several ways:

{% tabs %}
{% tab title="macOS" %}

* **Keyboard shortcuts**
  * Press `ESC` to quit the current mode.
  * Toggle modes with `CMD + I`
* **Force modes with special characters**
  * `!` at the start of input forces Terminal Mode.
  * `*` at the start of input forces Agent Mode.
* **Manual switching**: click the Agent icon or Terminal icon in the input switcher to swap modes directly.
  {% endtab %}

{% tab title="Windows" %}

* **Keyboard shortcuts**
  * Press `ESC` to quit the current mode.
  * Toggle modes with `CTRL + I`
* **Force modes with special characters**
  * `!` at the start of input forces Terminal Mode.
  * `*` at the start of input forces Agent Mode.
* **Manual switching**: click the Agent icon or Terminal icon in the input switcher to swap modes directly.
  {% endtab %}

{% tab title="Linux" %}

* **Keyboard shortcuts**
  * Press `ESC` to quit the current mode.
  * Toggle modes with `CTRL + I`
* **Force modes with special characters**
  * `!` at the start of input forces Terminal Mode.
  * `*` at the start of input forces Agent Mode.
* **Manual switching**: click the Agent icon or Terminal icon in the input switcher to swap modes directly.
  {% endtab %}
  {% endtabs %}

### Natural Language Auto-detection Settings

Warp can automatically detect when you’re writing in plain English and switch you into Agent Mode. If needed, you can customize or disable this behavior.

#### Fixing false detections

If certain shell commands are mistakenly detected as natural language, you can add them to the denylist: `Settings > AI > Input > Natural language denylist`

#### Turning off auto-detection

To disable natural language detection entirely, go to: `Settings > AI > Input Auto-detection`

When auto-detection is turned off, you’ll need to explicitly switch between Terminal Mode and Agent Mode using `CMD + I` (macOS) or `CTRL + I` (Windows/Linux).

#### First-time setup

The first time you enter Agent Mode, Warp will display a banner with the option to disable natural language detection for your command line:

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-33884cb98a4271fb1f7f91f543c69a916201ad4e%2Fbanner_for_auto-detection_first_experience.png?alt=media&#x26;token=43bd3585-ef9e-4021-aa1e-e1b470b01440" alt="Warp displays an option to toggle natural language detection on / off"><figcaption><p>Warp displays an option to toggle natural language detection on / off</p></figcaption></figure>

***

## Contextual Input Chips

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d17dca10aa39d057a67cf1f658d6ccb70136a9f1%2Funiversal-input.png?alt=media" alt=""><figcaption><p>Universal Input's contextual input chips, from left to right: conversation management, node version, active directory, Git and code diffs, and 2 attached images.</p></figcaption></figure>

The Universal Input includes **contextual chips** that provide inline information about your current environment. These chips surface relevant details such as directory paths, Git status, conversations, or runtime versions, making it easier to navigate, manage context, and take quick actions without leaving the input.

#### Conversation Management chip

The conversation management chip shows your recent [Agent conversations](https://docs.warp.dev/documentation/agents/using-agents/agent-conversations), allowing you to reference or reopen them directly.

These chips appear in both Agent Mode and Terminal Mode, so you can continue a previous conversation without starting from scratch. For more details, see [agent-conversations](https://docs.warp.dev/documentation/agents/using-agents/agent-conversations "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e6aebd77f638d66aa5b8139f15e723a1640d88a1%2Fconversation-management-chip-universal-input.png?alt=media" alt=""><figcaption><p>The Conversation Management chip displays recent Agent conversations and lets you continue or reopen them directly from the input.</p></figcaption></figure>

These chips appear in both Agent Mode and Terminal Mode, helping you continue a previous conversation without starting from scratch. For more details, refer to [agent-conversations](https://docs.warp.dev/documentation/agents/using-agents/agent-conversations "mention").

#### Active directory chip

The active directory chip displays your current working directory and enables simple file navigation. Clicking on a folder moves you into that folder, while clicking on a file opens it in [Warp’s native code editor](https://docs.warp.dev/documentation/code/code-editor). This makes it possible to move around your workspace seamlessly from within the input.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-fbafa08ab1d21e589fb926d91f1f1adb53d01ea4%2Factive-directory-chip.png?alt=media" alt=""><figcaption><p>The Active Directory chip lets you browse directories and open files directly from the input.</p></figcaption></figure>

#### Git Status chip

When you’re in a Git-tracked repository, the Git Status chip displays file- and line-level changes. You can switch branches by clicking on the branch name or review modified files in Warp’s [native Code Review panel](https://docs.warp.dev/documentation/code/code-review).

The chip updates automatically as files are added, removed, or changed, giving you a real-time view of your repository state.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e0404cd113606edbb9935fcf1a1e09fae9c41e84%2Fgit-branch-chip.png?alt=media" alt=""><figcaption><p>The Git Status chip highlights repository changes and provides quick access to code review.</p></figcaption></figure>

#### File attachments chips

The file attachments chip lets you attach images and other files directly to a prompt. You can upload up to five [images at a time (as Agent Context)](https://docs.warp.dev/documentation/agents/using-agents/agent-context/images-as-context) using the upload button in the toolbelt or by dragging and dropping files into the input. This makes it possible to add screenshots, diagrams, PDFs, or other references directly to your query, giving the Agent richer context.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-7d042eb500539619b25cc68a4e2dd7d3aa7f7ec9%2Fimages-as-context-chip.png?alt=media" alt=""><figcaption><p>The File Attachments chip allows you to add images or files as context for your queries.</p></figcaption></figure>

**Node version chip**

In repositories that include a `package.json`, a Node Version chip appears to show the detected Node.js version. This gives you visibility into your runtime environment without needing to run additional commands.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-70bfe906800315b7d2c69f88959b0ad88ae233c6%2Fnode-version-chip.png?alt=media" alt=""><figcaption><p>The Node Version chip displays the Node.js version detected in your repository.</p></figcaption></figure>

{% hint style="info" %}
At this time, contextual chips are not configurable, but they update automatically based on your workspace and repository state.
{% endhint %}

***

## Input toolbelt

The **Input Toolbelt** provides quick-access controls alongside the Universal Input. These tools allow you to attach context, run shortcuts, and configure Agent behavior without leaving the input field. Depending on the mode you are in, some features are automatically enabled or will place you into Agent Mode.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-355d68a2299029c670c9c5acaee63d414e51f728%2Finput-toolbar.png?alt=media" alt=""><figcaption><p>The Input Toolbelt in Warp’s Universal Input, showing quick-access controls for context, slash commands, voice input, attachments, profiles, and model selection.</p></figcaption></figure>

#### @ - Context

The [@ context chip](https://docs.warp.dev/documentation/agents/using-agents/agent-context/using-to-add-context) is available when you are working in a Git repository. Outside of a Git repo, it appears dimmed.

This feature allows you to attach specific files, folders, code symbols, Warp Drive objects, or blocks from other sessions as context for a prompt. Typing **@** inside the input also opens a context menu where you can search for and select files or directories to include.

Attaching context with @ works in both Agent mode (when interacting with Agents) and classic Terminal commands (for referencing file paths).

**Slash Commands**

[Slash Commands](https://docs.warp.dev/documentation/agents/slash-commands) are available in Agent Mode and Auto-detection Modes. They allow you to quickly run built-in actions or saved prompts without leaving the input field. Typing / displays a menu of available commands, which can be customized or extended.

**Voice Input**

[Voice Input](https://docs.warp.dev/documentation/agents/voice) automatically places you in Agent Mode. Speaking directly into Warp lets you phrase tasks, commands, or queries in natural language, and Warp will interpret them as if you had typed them. This feature is especially useful when you want hands-free interaction or when dictating longer tasks.

**Image Attachments**

You can [attach images as context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/images-as-context) directly to a prompt, which will automatically place you in Agent Mode. This is useful when you want the Agent to reference visual materials such as screenshots, diagrams, or other assets.

You can add images using the image upload button in the toolbelt (located at the bottom left or right, depending on your input layout). For additional methods of attaching images, see [images-as-context](https://docs.warp.dev/documentation/agents/using-agents/agent-context/images-as-context "mention").

**Fast Forward**

Fast Forward gives the Agent full autonomy for the remainder of a task or conversation. When enabled, the next prompt you enter allows the Agent to execute commands, read files, and apply code diffs without asking for confirmation each time. This is useful for complex workflows where step-by-step approval would slow things down.

#### Profile Picker

The Profile Picker allows you to select from different [Agent Profiles](https://docs.warp.dev/documentation/agents/using-agents/agent-profiles-permissions), each with its own configuration of autonomy, tools, and default model. If you have only one profile, the picker will not appear in the UI.

From the Profile Picker, you can view all available profiles, switch between them, and quickly see the default model attached to each one. Profiles make it possible to tailor Agent behavior for different types of tasks or projects.

### Model Picker

The Model Picker is tied to your current Agent Profile. Each profile has a default model, but you can override it at any time using the picker. Warp curates a selection of top large language models (LLMs) for you to choose from, balancing speed, quality, and reasoning ability depending on your needs.

For a full list of supported models and guidance on when to use them, see [model-choice](https://docs.warp.dev/documentation/agents/using-agents/model-choice "mention").


# Classic Input

Classic Input lets you use Warp with an editor that resembles a traditional terminal, offering full terminal features and Agent Mode support out of the box.

## Classic Input Style

Warp supports two input styles: **Classic Input** and [Universal Input](https://docs.warp.dev/documentation/terminal/universal-input). Classic Input is closer to a traditional terminal experience, with support for shell customizations (e.g. PS1, same-line prompts, oh-my-zsh themes, and more).

You can switch between input styles in `Settings > Appearance > Input`.

{% hint style="info" %}
[Universal Input](https://docs.warp.dev/documentation/terminal/universal-input) is the default input style in Warp. Many of our newest features are only available in Universal Input and may not work in Classic Input.\
\
Classic Input remains supported for users who prefer a traditional terminal experience, but it is considered a legacy option. We encourage you to use Universal Input for the best experience.
{% endhint %}

[Agent Mode](https://docs.warp.dev/documentation/agents/using-agents) works in Classic Input just like it does in Universal Input, with some minor differences.

### Learn more about Classic Input

Classic Input supports all of Warp’s core terminal features, including the following and more:

* [prompt](https://docs.warp.dev/documentation/terminal/appearance/prompt "mention") — Use a fully customizable Warp prompt or your shell prompt, with support for PS1 and same-line prompts.
* [input-position](https://docs.warp.dev/documentation/terminal/appearance/input-position "mention") — Choose where the input appears in Warp, including both the prompt and the command line.
* [editor](https://docs.warp.dev/documentation/terminal/editor "mention")— Warp’s input editor works like a modern IDE, with rich editing capabilities not found in most terminals.
* [entry](https://docs.warp.dev/documentation/terminal/entry "mention") — Access Warp’s features for command history, synchronized inputs, YAML workflows, and more.
* [text-selection](https://docs.warp.dev/documentation/terminal/more-features/text-selection "mention") — Use smart selection or rectangular (column) selection to highlight text precisely without tedious cleanup.

### How to enter Agent Mode

You may enter Agent Mode in a few ways:

{% tabs %}
{% tab title="macOS" %}

* Type any natural language, like a task or a question, in the terminal input. Warp will recognize natural language with a local auto-detection feature and prepare to send your query to Warp AI.
* Use keyboard shortcuts to toggle into Agent Mode `CMD-I` or type `ASTERISK-SPACE`.
* Click the “AI” sparkles icon in the menu bar, and this will open a new terminal pane that starts in Agent Mode.
* From a block, you want to ask Warp AI about. You can click the sparkles icon in the toolbelt, or click on its block context menu item “Attach block(s) to AI query”.
  {% endtab %}

{% tab title="Windows" %}

* Type any natural language, like a task or a question, in the terminal input. Warp will recognize natural language with a local auto-detection feature and prepare to send your query to Warp AI.
* Use keyboard shortcuts to toggle into Agent Mode `CTRL-I` or type `ASTERISK-SPACE`.
* Click the “AI” sparkles icon in the menu bar, and this will open a new terminal pane that starts in Agent Mode.
* From a block, you want to ask Warp AI about. You can click the sparkles icon in the toolbelt, or click on its block context menu item “Attach block(s) to AI query”.
  {% endtab %}

{% tab title="Linux" %}

* Type any natural language, like a task or a question, in the terminal input. Warp will recognize natural language with a local auto-detection feature and prepare to send your query to Warp AI.
* Use keyboard shortcuts to toggle into Agent Mode `CTRL-I` or type `ASTERISK-SPACE`.
* Click the “AI” sparkles icon in the menu bar, and this will open a new terminal pane that starts in Agent Mode.
* From a block, you want to ask Warp AI about. You can click the sparkles icon in the toolbelt, or click on its block context menu item “Attach block(s) to AI query”.
  {% endtab %}
  {% endtabs %}

This will put you in *Pair* mode by default. While pairing with Warp, you can write out questions and tasks in an ongoing conversation.

When you are in Agent Mode, a ✨ sparkles icon will display in line with your terminal input.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f886e83dea97c4d46e3af7e2ee5274d8da4c79a1%2Fundo_my_git_commit.png?alt=media" alt="The sparkles on the command line indicate Agent Mode is active."><figcaption><p>The sparkles on the command line indicate Agent Mode is active.</p></figcaption></figure>

### Auto-detection for natural language and configurable settings

The feature Warp uses to detect natural language automatically is completely local. None of your input is sent to AI unless you press `ENTER` in Agent Mode.

If you find that certain shell commands are falsely detected as natural language, you can fix the model by adding those commands to a denylist in `Settings > AI > Auto-detection denylist`.

You may also turn autodetection off from `Settings > AI > Input Auto-detection`.

The first time you enter Agent Mode, you will be served a banner with the option to disable auto-detection for natural language on your command line:

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-33884cb98a4271fb1f7f91f543c69a916201ad4e%2Fbanner_for_auto-detection_first_experience.png?alt=media&#x26;token=43bd3585-ef9e-4021-aa1e-e1b470b01440" alt="Warp displays an option to toggle natural language detection on / off"><figcaption><p>Warp displays an option to toggle natural language detection on / off</p></figcaption></figure>

### Input Hints

Warp input occasionally shows hints within the input editor in a light grey text that helps users learn about features. It's enabled by default.

* Toggle this feature `Settings > AI > Show input hint text` or search for "Input hint text" in the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or Right-click on the input editor.

### How to exit Agent Mode

{% tabs %}
{% tab title="macOS" %}
You can quit Agent Mode at any point with `ESC` or `CTRL-C`, or toggle out of Agent Mode with `CMD-I`.
{% endtab %}

{% tab title="Windows" %}
You can quit Agent Mode at any point with `ESC` or `CTRL-C`, or toggle out of Agent Mode with `CTRL-I`.
{% endtab %}

{% tab title="Linux" %}
You can quit Agent Mode at any point with `ESC` or `CTRL-C`, or toggle out of Agent Mode with `CTRL-I`.
{% endtab %}
{% endtabs %}

### How to run commands in Agent Mode

Once you have typed your question or task in the input, press `ENTER` to execute your AI query. Agent Mode will send your request to Warp AI and begin streaming output in the form of an AI block.

Unlike a chat panel, Agent Mode can complete tasks for you by running commands directly in your session.

#### Agent Mode Command Suggestions

If Agent Mode finds a suitable command that will accomplish your task, it will describe the command in the AI block. It will also fill your terminal input with the suggested command so you can press `ENTER` to run the command.

When you run a command suggested by Agent Mode, that command will work like a standard command you've written in the terminal. No data will be sent back to the AI.

If the suggested command fails and you want to resolve the error, you may start a new AI query to address the problem.

<figure><img src="broken-reference" alt="Agent Mode makes a suggestion to run a command."><figcaption><p>Agent Mode makes a suggestion to run a command.</p></figcaption></figure>

#### Agent Mode Requested Commands

If Agent Mode doesn't have enough context to assist with a task, it will ask permission to run a command and read the output of that command.

You must explicitly agree and press `ENTER` to run the requested command. When you hit enter, both the command input and the output will be sent to Warp AI.

If you do not wish to send the command or its output to AI, you can click Cancel or press `CTRL-C` to exit Agent Mode and return to the traditional command line.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6872236ded0f64a0dfb3de102a23be643f7e8974%2FScreenshot%202024-06-14%20at%205.13.02%E2%80%AFPM.png?alt=media&#x26;token=582d7764-319c-4c2d-b3b4-e98b21c935f8" alt="Warp AI asks permission to run a command and read the output."><figcaption><p>Warp AI asks permission to run a command and read the output.</p></figcaption></figure>

Once a requested command is executed, you may click to expand the output and view command details.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-85e9e1e0fd2be28e1e4515bcd0b54673d2b8cbbf%2FScreenshot%202024-06-14%20at%205.21.37%E2%80%AFPM.png?alt=media" alt=""><figcaption><p>Viewing command details</p></figcaption></figure>

In the case that a requested command fails, Warp AI will detect that. Agent Mode is self-correcting. It will request another command until it completes the task for you.

Warp lets you choose from a curated list of LLMs for use in Agent Mode. By default, Warp uses **Claude 4 Sonnet** for auto, but you can switch to other supported models. For all available models, please refer to [model-choice](https://docs.warp.dev/documentation/agents/using-agents/model-choice "mention").


# Appearance


# Themes

Warp includes several themes (out-of-box) and also supports setting custom themes.

### Theme Picker

The Theme Picker can be accessed by:

1. Navigating to `Settings > Appearance`.
2. Clicking the Custom Themes (shaded) box.
3. Upon selecting a theme, Warp's appearance will update accordingly.
4. Press the checkmark to save the selection, or the X to revert.

{% hint style="info" %}
The Theme setting persists, meaning Warp will open with the same settings in the next session.
{% endhint %}

### Theme Creator

Automatically create new themes based on a background image.

1. Go to `Settings > Appearance > Current Theme` or search "Open Theme Picker" within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).
2. Click the `+` button in the theme picker.
3. Upload the image and select the background color.
4. Click "Create Theme" to save and accept the new theme.

### OS Theme Sync

Warp supports synchronizing your theme with the OS’s light and dark themes. To enable this:

1. Open the `Settings > Appearance` dialog.
2. Click the toggle "Sync with OS".
3. You will then be able to select a specific theme for when the OS is in light mode and dark mode.

## How it works

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-20d3599d5fd425ac06adcd83837e4d1f634007c2%2Ftheme-picker.gif?alt=media" alt=""><figcaption><p>Theme picker demo</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-69f7fa985fdb3acdc6041af64bf848ba31a6698b%2Ftheme-creator.gif?alt=media" alt=""><figcaption><p>Theme creator demo</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-1fa2c838244f1456a5aebf16a8037fa8eb9e9d6a%2Ftheme-sync-demo.gif?alt=media" alt="theme os sync demo"><figcaption><p>Theme sync demo</p></figcaption></figure>

## Default Themes

By default, Warp ships with these themes:

<table data-view="cards"><thead><tr><th align="center"></th><th align="center"></th></tr></thead><tbody><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-72c990c1e5ed682da0cffad5eba740be47cc4c3a%2Fwarp-dark.png?alt=media&#x26;token=f1b7fb5a-4552-41ee-8feb-9bc652f39357" alt=""></td><td align="center">Warp Dark</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b0abfd1f53b1783766aa380b576e2daf30359735%2Fwarp-light.png?alt=media&#x26;token=8211c0fc-e385-4d76-b107-e87bc0192650" alt=""></td><td align="center">Warp Light</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-1e0219a8ecbe3bdba5006c597c3e6def69e95e81%2Fdracula.png?alt=media" alt=""></td><td align="center">Dracula</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-67eab274f75fc910b76a19a7a7947aa670f8b8cf%2Fsolarized-dark.png?alt=media&#x26;token=1bf1819d-2cd0-4067-9dce-8c99f8a7fa41" alt=""></td><td align="center">Solarized Dark</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b03986790eb80a9087d659b7eb45a026593f4ec6%2Fsolarized-light.png?alt=media" alt=""></td><td align="center">Solarized Light</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f6e839e7ad1200efd3b46f3ca37cd13822133ac1%2Fgruvbox-dark.png?alt=media&#x26;token=a7149ca5-cc93-4077-94d8-80778f911055" alt=""></td><td align="center">Gruvbox Dark</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-94f2d3bc7a8ca1ad8dfb9cf6b256c9823206be30%2Fgruvbox-light.png?alt=media" alt=""></td><td align="center">Gruvbox Light</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d42e247d0d2dc8d282acc9ef25a7c2ab215014fe%2Fjellyfish.png?alt=media" alt=""></td><td align="center">Jellyfish</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d7f6bf7d62fb8cdce0018dedb084ab4302efa1f0%2Fkoi.png?alt=media&#x26;token=beb1fa6c-78b3-49f7-afd6-270b7eb3083e" alt=""></td><td align="center">Koi</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-70e5bf4ed6afcaeff767a8e419e0e9a76ff548ee%2Fleafy.png?alt=media&#x26;token=8504f09b-ac09-405d-b6f9-3ce9651e9434" alt=""></td><td align="center">Leafy</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-09d390fb3a434925c2d1737487f52fa935a003d4%2Fmarble.png?alt=media&#x26;token=34daf0dc-0ad1-40ad-ba53-de881ddc1b00" alt=""></td><td align="center">Marble</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-c9c84d02776d187532fbb09e032a931360903194%2Fpink-city.png?alt=media" alt=""></td><td align="center">Pink City</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-aeb07839e2c782c93f2f3f5dd770b86ef1fc48ab%2Fsnowy.png?alt=media&#x26;token=8a8cc755-73ce-4108-bf3a-1ef194ff51b0" alt=""></td><td align="center">Snowy</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-17befdfb17abf9cc24fe987e167ae472f75b1dfb%2Fdark-city.png?alt=media" alt=""></td><td align="center">Dark City</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8cb7c1179d71b0d823e88a3eb323a7b30a4853aa%2Fred-rock.png?alt=media" alt=""></td><td align="center">Red Rock</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2016bedb055f6ba3f07e47c2e5796defaa531636%2Fcyber-wave.png?alt=media&#x26;token=df8f117f-f117-4646-995b-b1e855555347" alt=""></td><td align="center">Cyber Wave</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-aab7a9ff8985507e7ea67488a3135fc1ae2b8c7b%2Fwillow-dream.png?alt=media&#x26;token=3cd00a0a-3900-4e53-b850-3a7b566fd80f" alt=""></td><td align="center">Willow Dream</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-625611e115a2ee1566b5a2460ccc364432e25fed%2Ffancy-dracula.png?alt=media&#x26;token=6e8535fd-9bcf-4c2b-9b5d-82785adb8e95" alt=""></td><td align="center">Fancy Dracula</td></tr><tr><td align="center"><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d94d4ec01ba78e9978b75519ba484fe8188b2fbe%2Fphenomenon.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td align="center">Phenomenon</td></tr><tr><td align="center"><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-be7d03d1002c3e2e6d9761b72f941211d6d8af06%2Fsolar-flare.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td align="center">Solar Flare</td></tr><tr><td align="center"><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5c5a5a42ffc69b154b37dcab65475b56a2a94e48%2Fadeberry.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td align="center">Adeberry</td></tr></tbody></table>


# Custom Themes

Warp supports Custom Themes which can be created manually or downloaded from our repo.

{% hint style="info" %}
Examples and a collection of themes can be found in the [Warp themes repository](https://github.com/warpdotdev/themes).
{% endhint %}

## Warp's Custom Theme Repository

We have a [repository of themes hosted on GitHub.](https://github.com/warpdotdev/themes)

Each theme has a preview generated in the README.

The main difference between "standard" and "base16" themes is that "standard" themes follow the typical color setup, while "base16" themes follow the framework suggested by [@chriskempson](https://github.com/chriskempson/base16).

There are 2 ways to install a theme from this repo.

1. Download a single file and follow the steps in the section below.
2. Clone the entire repo into the appropriate location based on your OS below:

{% tabs %}
{% tab title="macOS" %}

```bash
mkdir -p $HOME/.warp
cd $HOME/.warp/
git clone https://github.com/warpdotdev/themes.git
```

{% endtab %}

{% tab title="Windows" %}

```powershell
New-Item -Path "$env:APPDATA\warp\Warp\data\" -ItemType Directory
Set-Location -Path $env:APPDATA\warp\Warp\data\
git clone https://github.com/warpdotdev/themes.git
```

{% endtab %}

{% tab title="Linux" %}

```bash
mkdir -p ${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal
cd ${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/
git clone https://github.com/warpdotdev/themes.git
```

{% endtab %}
{% endtabs %}

Here is a step-by-step YouTube video that goes through these 2 steps for an example theme. Note the location for the files is based on macOS.

{% embed url="<https://www.youtube.com/watch?v=UTYgwD-cLbk>" %}
Adding a Custom Theme to Warp
{% endembed %}

## How do I use a custom theme in Warp?

1. To start, create the following directory:

{% tabs %}
{% tab title="macOS" %}

```bash
mkdir -p $HOME/.warp/themes/
```

{% endtab %}

{% tab title="Windows" %}

```powershell
New-Item -Path "$env:APPDATA\warp\Warp\data\themes\" -ItemType Directory
```

{% endtab %}

{% tab title="Linux" %}

```bash
mkdir -p ${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/themes/
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
It may take several minutes for Warp to initially discover the new themes directory. You can either wait or restart Warp. After that step, all future changes to the directory will be reflected within seconds.
{% endhint %}

2. Add your new custom theme yaml file to this directory:

```bash
cp ~/Downloads/my_awesome_theme.yaml {{path_to_your_themes_directory_from_step1}}
```

Your new theme should now be visible on the list of available themes.

## Create your custom theme, manually

Warp supports creating custom themes using .yaml files.

The format itself might expand, but we'll do our best to avoid breaking changes and maintain forward compatibility. We also plan on supporting sharing/creating custom themes directly within Warp.

A custom theme in Warp has the following `.yaml` structure:

```yaml
name: Custom Theme # Name for the theme
accent: '#268bd2' # Accent color for UI elements
cursor: '#95D886' # Input cursor color (optional; defaults to accent color if omitted)
background: '#002b36' # Terminal background color
foreground: '#839496' # The foreground color
details: darker # Whether the theme is lighter or darker
terminal_colors: # Ansi escape colors
  bright:
    black: '#002b36'
    blue: '#839496'
    cyan: '#93a1a1'
    green: '#586e75'
    magenta: '#6c71c4'
    red: '#cb4b16'
    white: '#fdf6e3'
    yellow: '#657b83'
  normal:
    black: '#073642'
    blue: '#268bd2'
    cyan: '#2aa198'
    green: '#859900'
    magenta: '#d33682'
    red: '#dc322f'
    white: '#eee8d5'
    yellow: '#b58900'
```

{% hint style="info" %}
Each color is represented in hex and must start with `#`.
{% endhint %}

* `name`: Name for the theme, will show up in the Theme picker.
* `accent`: Color used for highlights in Warp's UI
* `cursor`: Color for the input cursor (optional; defaults to accent color if omitted)
* `background`: Color of background
* `foreground`: Color of foreground
* `details`: Color used for detailing options
  * `darker`: Color used for dark theme
  * `lighter`: Color used for light-mode theme
* `terminal_colors`: Collection of normal & bright colors (16 total) known for other terminal themes (ANSI colors)

## Create your custom theme, automatically

Automatically create new themes based on a background image. Click the `+` button in the theme picker `Settings > Appearance > Current Theme` or search `Open Theme Picker` within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).

## Create your custom theme, with a tool

Use [Terminal-Themes](https://terminal-themes.com/) to create a custom theme and generate the appropriate RGB values for your custom theme. Once the YAML file is created, you can edit the file to add the background images or gradients.

## Background Images and Gradients

To add a background image you can use this attribute: `background_image:` with the name of the image you want to use as the background.

{% hint style="info" %}
Note: Warp currently only supports images with the *.jpg* file format:

* `.jpeg`
* `.jpg`
* `.JPEG`
  {% endhint %}

A `.yaml` config looks like this:

```yaml
name: Custom Theme
accent: '#268bd2'
cursor: '#95D886'
background: '#002b36'
details: darker
foreground: '#839496'

############################################################### SEE BELOW
background_image:
  # the path is relative to ~/.warp/themes/
  # the full path to the picture is: ~/.warp/themes/warp.jpg
  path: warp.jpg
  # the opacity value is required and can range from 0-100
  opacity: 60
############################################################### SEE ABOVE

terminal_colors:
  bright:
    black: '#002b36'
    blue: '#839496'
    cyan: '#93a1a1'
    green: '#586e75'
    magenta: '#6c71c4'
    red: '#cb4b16'
    white: '#fdf6e3'
    yellow: '#657b83'
  normal:
    black: '#073642'
    blue: '#268bd2'
    cyan: '#2aa198'
    green: '#859900'
    magenta: '#d33682'
    red: '#dc322f'
    white: '#eee8d5'
    yellow: '#b58900'
```

To set up a gradient, create a sublevel under accent with two key-value pairs:

* "left" and "right" or
* "top" and "bottom".

```yaml
accent:
  top: '#abcdef'
  bottom: '#fedcba'
```

```yaml
accent:
   left: '#abcdef'
   right: '#fedcba'
```

Warp also supports setting a gradient for the background.

```yaml
# accent has a gradient
accent:
  left: '#474747'
  right: '#ffffff'
# background has a gradient
background:
  top: '#474747'
  bottom: '#ffffff'
```

### Contributing

Contributions to this repo are greatly appreciated!

1. Fork the project
2. Create your branch with `git checkout -b theme/AwesomeTheme`
3. Regenerate thumbnails
4. Commit and open a pull request

Run this script to generate the thumbnails.

```bash
# Assuming you're adding the theme to the `standard` directory:
python3 ./scripts/gen_theme_previews.py standard
```

{% hint style="info" %}
Note: We cannot accept pull requests that include custom background images because:

* Licensing restrictions
* Trying to keep the binary size of the repo as small as possible (only the yaml files)

If your theme has an intended custom background image, include a comment in the yaml with a link to where people should download it.
{% endhint %}

## Community

All other Warp-related things can be discussed, please [contact us](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback).

## Open source dependencies

We'd like to call out a few of the open-source themes and repositories that helped bootstrap the set of themes for Warp:

* [iTerm colors pencil](https://github.com/mattly/iterm-colors-pencil)
* [Alacritty-theme](https://github.com/eendroroy/alacritty-theme)
* [base16-Alacritty](https://github.com/aarowill/base16-alacritty)
* [base16](https://github.com/chriskempson/base16)
* [Solarized](https://ethanschoonover.com/solarized/)
* [Dracula](https://draculatheme.com/)
* [Gruvbox](https://github.com/morhetz/gruvbox)


# Prompt

Warp allows you to configure its Warp prompt or a Shell prompt. A terminal prompt is a text that appears in the command line interface, indicating that the terminal is ready to accept commands.

### Warp prompt

Warp has a native prompt that is customizable and can show a variety of information including cwd, git, svn, kubernetes, pyenv, date, time, an so on. You can visit `Settings > Appearance > Input > Classic > Current prompt > Warp Prompt` to drag and drop context chips into your Warp prompt until it displays the pieces of information you'd like to include.

#### Git and Subversion

Git and Subversion context chips show which branch you are on locally, as well as the number of uncommitted changed files. This includes any new files, modified files, and deleted files that are staged or unstaged.

#### Kubernetes

Kubernetes context chip shows relevant information when you're using one of the following commands:

`kubectl|helm|kubens|kubectx|oc|istioctl|kogito|k9s|helmfile|flux|fluxctl|stern|kubeseal|skaffold|kubent|kubecolor|cmctl|sparkctl|etcd|fubectl`

{% hint style="info" %}
Warp respects the `KUBECONFIG` environmental variable, make sure you set it to your preferred configuration file location, if it's not the default path of `~/.kube/config`
{% endhint %}

### Same line prompt

By default, Warp's prompt displays on two lines where the command line input is one line below the prompt.

If you'd like to set your prompt such that the command line input and the prompt display together inline, you can configure this under `Settings > Appearance > Input > Classic > Current prompt > Warp Prompt` and check the box for "Same line prompt."

If you're using a [Shell prompt (PS1)](#custom-prompt), Warp will use the same line prompt settings to respect any styles or theme configurations. You may optionally configure a new line prompt with PS1 but you will need to write your configuration, according to your theme of choice.

{% hint style="info" %}
If you want to add back the new line on your Shell prompt, please run the following based on your shell or prompt:

```sh
# Bash
echo -e '\nPS1="${PS1}"$'\''\\n'\''' >> ~/.bashrc

# Zsh
echo -e '\nPROMPT="${PROMPT}"$'\''\\n'\''' >> ~/.zshrc

# Fish
echo -e '\nfunctions --copy fish_prompt fish_prompt_orig; function fish_prompt; fish_prompt_orig; echo; end' >> ~/.config/fish/config.fish

# Powershell
$rawString = @'
$originalPrompt = Get-Item Function:\prompt
Set-Item -Path Function:\prompt_original -Value $originalPrompt
function prompt {
    "$(& prompt_original)`n"
}
'@
Add-Content -Path $PROFILE -Value "`n$rawString`n"

# Powerlevel10k
p10k configure

# Starship Prompt
echo '[line_break]\ndisabled = false' >> ~/.config/starship.toml
```

{% endhint %}

### Shell prompt (PS1)

You can also set up a Shell prompt by configuring the **PS1** variable or installing a supported shell prompt plugin, see [Shell Prompt Compatibility Table](#shell-prompt-compatibility-table). Visit `Settings > Appearance > Input > Classic > Current prompt > Shell Prompt (PS1)` to enabled it.

{% hint style="info" %}
The PS1 is a variable used by the shell to generate the prompt, it represents the primary prompt string (hence the “PS”) - which the terminal typically displays before typing new commands.
{% endhint %}

#### Multi-Line and Right-Sided Prompts

The Shell prompt supports multi-line or right-sided prompts in zsh and fish, not bash. However, you can't have a multiline right-side prompt, only a multiline left prompt.

## How to access it

* Toggle the prompt by right-clicking on the prompt area above the input and selecting `Settings > Appearance > Input > Classic > Current prompt`. There you will be able to select and customize the Warp prompt or select the Shell prompt (PS1).
  * When using Warp prompt, you can right-click the prompt to copy the entire prompt, working directory, current git branch, git uncommitted file count, etc.
  * When using a Shell prompt, you can right-click the prompt to copy the entire prompt or select any part of the custom prompt in previously run blocks in your session.

## How it works

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-79eae94dc5a59ae0085534de4dc77d0c6d43a6d4%2Fclassic-prompt.gif?alt=media" alt=""><figcaption><p>Classic input</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8b122e4df5d9c51a70da30de03ee1d10e9ffffb5%2Fwarp-custom-prompt-demo.gif?alt=media&#x26;token=90ec41c0-bd0c-4b75-babf-891ae5af681e" alt="Warp Prompt + Custom Prompt Demo"><figcaption><p>Warp Prompt | Shell Prompt Demo</p></figcaption></figure>

<figure><img src="broken-reference" alt=""><figcaption><p>Prompt edit modal</p></figcaption></figure>

### Shell Prompt Compatibility Table

| Shell                       | Tool                                                                      | Does it work?                                                   |
| --------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------- |
| bash \| zsh                 | [PS1](https://www.warp.dev/blog/whats-so-special-about-ps1)               | Working                                                         |
| bash \| zsh \| fish \| pwsh | [Starship](https://github.com/starship/starship)                          | [Working\*](#starship)                                          |
| bash \| zsh \| fish \| pwsh | [oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh)                | Working                                                         |
| zsh                         | [Powerlevel10k](https://github.com/romkatv/powerlevel10k)                 | [Working\*](#powerlevel10k)                                     |
| zsh                         | [Spaceship](https://github.com/spaceship-prompt/spaceship-prompt)         | [Working\*](#spaceship)                                         |
| zsh                         | [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh)                           | Working                                                         |
| zsh                         | [prezto](https://github.com/sorin-ionescu/prezto)                         | [Working\*](#prezto)                                            |
| ssh                         |                                                                           | Working                                                         |
| bash                        | [oh-my-bash](https://github.com/ohmybash/oh-my-bash)                      | Not supported                                                   |
| bash                        | [bash-it](https://github.com/Bash-it/bash-it)                             | Not supported                                                   |
| bash                        | [SBP](https://github.com/brujoand/sbp)                                    | Not supported                                                   |
| bash                        | [synth-shell-prompt](https://github.com/andresgongora/synth-shell-prompt) | Not supported                                                   |
| bash \| zsh                 | [Powerline-shell](https://github.com/b-ryan/powerline-shell)              | Not supported                                                   |
| zsh                         | [zplug](https://github.com/zplug/zplug)                                   | Not supported                                                   |
| fish                        | [tide](https://github.com/IlanCosman/tide)                                | [Not supported](https://github.com/warpdotdev/Warp/issues/3358) |
| fish                        | [oh-my-fish](https://github.com/oh-my-fish/oh-my-fish)                    | [Not supported](https://github.com/warpdotdev/Warp/issues/3796) |

## Known incompatibilities

If you’re having issues with prompts, please see below or our [Known Issues](https://docs.warp.dev/documentation/support-and-billing/known-issues#configuring-and-debugging-your-rc-files) for more troubleshooting steps. Also, although some prompts are not officially supported, they may still work in Warp.

### Starship

#### Starship Settings

Some `~/.config/starship.toml` settings are known to cause errors in Warp. `#` or `DEL` the following lines to resolve known errors:

```
# Get editor completions based on the config schema
'' = 'https://starship.rs/config-schema.json'

# Disables the custom module
[custom]
disabled = false
```

For `fish` shell, optional for `bash|zsh`, disable the multi-line prompt in Starship by putting the following in your `~/.config/starship.toml`:

```
[line_break]
disabled = true
```

You may also see an error relating to timeout. You can set the `command_timeout` variable in your `~/.config/starship.toml` to fix this. See more in the [starship docs](https://starship.rs/config/#prompt).

#### Starship + bash

Starship prompt may not render properly if your [default shell](https://docs.warp.dev/documentation/getting-started/supported-shells#changing-default-shell) is `/bin/bash`. To [workaround](https://github.com/warpdotdev/Warp/issues/3066#issuecomment-1548643121) the issue, we recommend you upgrade bash, find the path with `echo $(which bash)`, then put the path in your `Settings > Features > Session > "Startup shell for new sessions" > Custom`.

#### Starship + zsh

If you want to restore the additional line after the Starship prompt on `zsh`, add the following to the bottom of your `~/.zshrc` file: `PROMPT="${PROMPT}"$'\n'`

### Powerlevel10k

When installing the Powerlevel10k (P10k) prompt, we recommend you use the [Meslo Nerd Font](https://github.com/romkatv/powerlevel10k/blob/master/font.md).\
\
P10K may display the arrow dividers as grey instead of color. The color for those chars is rendered grey due to Warp's minimum contrast setting. To [workaround](https://github.com/warpdotdev/Warp/issues/2851#issuecomment-1605005256) this issue, go to `Settings > Appearance > Text > Enforce minimum contrast` and set it to "Never".

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-3a6ac0a4154cd83d02dda41e9d1e65f21fdeb7de%2Fp10k-grey-arrow-prompt.png?alt=media" alt="" width="563"><figcaption><p>Example of the grey dividers in p10k</p></figcaption></figure>

Warp does support [p10k](https://github.com/romkatv/powerlevel10k#installation) version 1.19.0 and above. Ensure you have the latest version installed and restart Warp after the installation/update of p10k. Then enable the custom prompt as stated [above](#how-to-access-it) and it should work.

{% hint style="info" %}
Warp still doesn't fully support some p10k features like transient prompt and visual features like gradients.
{% endhint %}

{% embed url="<https://www.youtube.com/watch?t=18s&v=dIV9Cso4Mi8>" %}
Installing Powerlevel10k
{% endembed %}

{% hint style="warning" %}
Please note the Installing Powerlevel10k video mentions enabling a custom prompt in `Settings > Features > Honor users custom prompt (PS1)`, but it's now in `Settings > Appearance > Input > Classic > Current prompt > Shell Prompt (PS1)` .
{% endhint %}

### Spaceship

This prompt can cause an issue with typeahead in Warp's input editor. To [workaround](https://github.com/warpdotdev/Warp/issues/1973#issuecomment-1340150521) the issue, run `echo "SPACESHIP_PROMPT_ASYNC=FALSE" >>! ~/.zshrc`.

### Prezto

Although Warp does have support for prezto's prompt, enabling the [prezto utility module](https://github.com/sorin-ionescu/prezto/blob/master/modules/utility/README.md) in the `.zpreztorc` is not supported as with many other autocompletion [plugins that are incompatible](https://docs.warp.dev/documentation/support-and-billing/known-issues#list-of-incompatible-tools).

### Disabling unsupported prompts for Warp

We advise using Warp's default prompt or installing one of the supported tools, see [Compatibility Table](#custom-prompt-compatibility-table). You can disable unsupported prompts for Warp as such:

```
if [[ $TERM_PROGRAM != "WarpTerminal" ]]; then
##### WHAT YOU WANT TO DISABLE FOR WARP - BELOW

    # Unsupported Custom Prompt Code

##### WHAT YOU WANT TO DISABLE FOR WARP - ABOVE
fi
```

#### iTerm2

The iTerm2 shell integration breaks Warp and your custom prompt will not be able to be visible with this on. If you're coming from iTerm2 please check your dotfiles for it. We advise disabling the integration for Warp like so:

```
if [[ $TERM_PROGRAM != "WarpTerminal" ]]; then
##### WHAT YOU WANT TO DISABLE FOR WARP - BELOW

test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

##### WHAT YOU WANT TO DISABLE FOR WARP - ABOVE
fi
```


# Input Position

Warp gives you the ability to configure the position of your input, which includes both the prompt and the command line.

You can select from three different input positions, which each have different modes of behavior for the flow of input/output Blocks.

<table><thead><tr><th>Input position</th><th>Behavior</th><th data-hidden></th></tr></thead><tbody><tr><td>Start at the top (Classic mode)</td><td>When you select “start at the top,” the prompt with input will initiate at the top of the view and move down in the view as you enter commands. Blocks of input/output will stack above the prompt and command input. You can scroll up or navigate up to visit past commands. You can enter <code>CTRL-L</code> or the <code>clear</code> command at any time to return the input to the top of the screen while still maintaining your scroll history.</td><td></td></tr><tr><td>Pin to the top (Reverse mode)</td><td>When you select “pin to the top,” the prompt with input will display pinned to the top of your terminal view. Blocks of grouped input/output will flow down the view in reverse order with your latest results at the top. You can scroll down or navigate down to visit past commands. For long-running commands, you can also click "Lock scrolling at bottom of block" to continue to follow the stdout.</td><td></td></tr><tr><td>Pin to the bottom (Warp mode)</td><td>Warp mode starts with input pinned to the bottom of your terminal view. Blocks of grouped input/output flow up and out of view. You can scroll up or navigate up to visit past commands.</td><td></td></tr></tbody></table>

## How to access it

* You can configure your input position by navigating to `Settings > Appearance > Input`.
* You can also choose and set modes from the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).

{% hint style="info" %}
Changes to the Input position take place immediately and apply to all open panes.
{% endhint %}

### Related commands

{% tabs %}
{% tab title="macOS" %}

* `CMD-K` will clear the entire list of input/output blocks for a clean view
* `CTRL-L` will move the list of input/output blocks outside of the view and past the scroll so you have a clean view and the ability to easily visit past commands
* For long Blocks, you can press `SHIFT-CMD-UP`/`SHIFT-CMD-DOWN` to Scroll to the top/bottom the selected block.
  {% endtab %}

{% tab title="Windows" %}

* `CTRL-SHIFT-K` will clear the entire list of input/output blocks for a clean view
* `CTRL-L` will move the list of input/output blocks outside of the view and past the scroll so you have a clear view and the ability to easily visit past commands
* For long Blocks, you can press `CTRL-SHIFT-UP`/`CTRL-SHIFT-DOWN` to Scroll to the top/bottom of the selected block.
  {% endtab %}

{% tab title="Linux" %}

* `CTRL-SHIFT-K` will clear the entire list of input/output blocks for a clean view
* `CTRL-L` will move the list of input/output blocks outside of the view and past the scroll so you have a clear view and the ability to easily visit past commands
* For long Blocks, you can press `CTRL-SHIFT-UP`/`CTRL-SHIFT-DOWN` to Scroll to the top/bottom of the selected block.
  {% endtab %}
  {% endtabs %}

## How it works

{% embed url="<https://www.youtube.com/watch?end=147&start=37&v=z1rDVPxaNCo>" %}
Input Position Demo
{% endembed %}


# Text, Fonts, & Cursor

Warp supports customizing the font and how text is displayed. This can help improve readability and usability. Warp also supports disabling the blinking cursor.

{% hint style="info" %}
Once a new font is installed in your system, you need to restart Warp for it to show on the list of options. You may also need to check "View all available system fonts" to see the new font.
{% endhint %}

## How to use it

### Text and Fonts

To access it, go to `Settings > Appearance > Text`

From there you can customize:

* Font type
* Font weight
* Font size
* Line height
* Use thin strokes
  * The default setting prevents text from being blurry on low-DPI displays.

{% hint style="warning" %}
On Linux, Warp does not support the "Use thin stroke" feature.
{% endhint %}

* Enforce minimum contrast
  * The default setting tweaks named colors to meet accessibility standards.
* Show ligatures in terminal

{% hint style="info" %}
Enabling ligatures can reduce performance. Warps default font, Hack, doesn't yet have ligature support. We recommend font that supports ligatures (e.g. [Fira Code](https://github.com/tonsky/FiraCode)) as a stopgap.
{% endhint %}

### Cursor

To access it, go to `Settings > Appearance > Cursor`

From there you can customize:

* Select the Cursor type to Bar, Block, or Underline.
* Toggle the Blinking cursor or from the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), type "Cursor blink" and toggle the setting.

{% hint style="info" %}
Cursor type preference is disabled while [Vim keybindings](https://docs.warp.dev/documentation/terminal/editor/vim) (vim mode) is active.
{% endhint %}

## How it works

{% embed url="<https://www.loom.com/share/be2fa6ab10a3494a8c57a5431966905b?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Text and Fonts Demo
{% endembed %}

{% embed url="<https://www.loom.com/share/6ce3218472894763bb80a26b6c632c4d?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Cursor Demo
{% endembed %}


# Size, Opacity, & Blurring

Warp supports settings for Window size, opacity(transparency), and blurring effects. This can help with setting up specific terminal layouts and visual preferences.

## How to use it

### Window Size

To access size settings, go to `Settings > Appearance > Window`.

* Enable "Open new windows with custom size", Then configure your preferred columns and rows.

{% hint style="info" %}
If [Session Restoration](https://docs.warp.dev/documentation/terminal/sessions/session-restoration) is enabled, Warp will restore the size of the last window closed when you quit the app. Either make sure the custom-sized window is the last one closed, or disable Session Restoration to ensure Warp launches with the custom-sized window.
{% endhint %}

### Window Opacity

To access it, go to `Settings > Appearance > Themes`

* The slider supports setting the opacity value between `1` and `100` where `100` is completely opaque or solid.

### Window Blurring

After decreasing Opacity (moving the slider to a value less than `100`), you can also blur the background.

* On MacOS, this is done using the blur slider. Increasing the slider increases the blur radius that's applied to the background image.
* On Windows, this is done by toggling the Acrylic background texture on or off.

{% hint style="warning" %}
On macOS, large blur radiuses may affect performance, especially on Retina displays.

On Linux, window blurring is not supported.

On Windows, some graphics drivers may not support rendering transparent or translucent windows. See below for troubleshooting tips.
{% endhint %}

## How it works

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-79a7d9b64b98fad12b103e20f755d20d59d1f88c%2Fwindow_size_demo.gif?alt=media" alt="Window Size Demo"><figcaption><p>Window Size Demo</p></figcaption></figure>

{% embed url="<https://www.loom.com/share/22c9ef25392e4a5e80f9e01394c84dc4?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Window Opacity and Blurring Demo
{% endembed %}

### Troubleshooting transparency on Windows

{% hint style="info" %}
At the moment, window opacity in Warp on Windows **does not work** in the following circumstances:

* When using DirectX 12 as the rendering backend
* When using any rendering backend with an Nvidia GPU when "Auto" or "Prefer layered" is selected as the value for "Vulkan/OpenGL present method" in NVIDIA Control Panel > Manage 3D Settings
  {% endhint %}

Some graphics drivers and rendering backends may not support rendering transparent windows.

You can select the Vulkan or OpenGL graphics backend to render new Warp windows in the Settings menu, under `Features` > `System` > `Preferred graphics backend`.

You can also opt to render new Warp windows with an integrated GPU, under `Features` > `System` > `Prefer rendering new windows with integrated GPU (low power)`.


# Pane Dimming & Focus

Warp supports dimming inactive Panes as well as allowing the focus to follow the mouse. This helps you easily see which pane is active and maintain focus.

## How to use it

### Inactive Pane Dimming

The panes that aren't active will be dimmed to better indicate which pane is active. To access it, go to `Settings > Appearance > Panes`

* Toggle on `Dim inactive panes` to enable the feature.

{% hint style="info" %}
Split panes show a triangle indicator on the top left corner of the active pane.
{% endhint %}

### Mouse Focus

The pane with the mouse over it will become active. To access it, go to `Settings > Appearance > Panes`

* Toggle on `Focus follows mouse` to enable the feature.

## How it works

{% embed url="<https://www.loom.com/share/62b84d3c60b34cdbaa340fbe8ce8b1d1?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Inactive Pane Dimming Demo
{% endembed %}


# Blocks Behavior

Warp lets you customize your Blocks in a variety of ways such as enabling Compact mode, or disabling the Block Dividers for a more custom block experience, and more.

## Compact Mode

Warp offers the option to enable Compact mode, which condenses the spacing between [Blocks](https://docs.warp.dev/documentation/terminal/blocks), enabling more content to be in view.

### How to enable Compact Mode

Compact mode is disabled by default, but can be toggled in the following ways:

* Navigate to `Settings > Appearance > Blocks > Compact Mode`.
* Utilize the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), then search for "Compact mode" to toggle.

{% hint style="info" %}
Warp will open with the same compact settings in future sessions.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-9aa9ae8b6c35b85a591da228861e0ab6ccf7a154%2Fcompact_mode.gif?alt=media&#x26;token=5d7d5af4-d64f-442b-b884-e28f70d2184f" alt=""><figcaption><p>Compact Mode Demo</p></figcaption></figure>

## Block Dividers

Warp [Blocks](https://docs.warp.dev/documentation/terminal/blocks) are divided by horizontal lines that separate individual command input and output, they create a visual break between different commands that you run in a session.

### How to toggle Block Dividers

Block dividers are enabled by default, but can be toggled in the following ways:

* Navigate to `Settings > Appearance > Blocks > Show block dividers`.
* Utilize the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), then search for "Block Dividers".

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d8c59f3eb0fdbe4ca070339d914381434073d2d3%2Fblock-divider-demo.gif?alt=media" alt=""><figcaption><p>Block Divider Demo</p></figcaption></figure>


# Tabs Behavior

Warp lets you customize the Tabs behavior in a variety of ways such as setting the Tab indicators, or  hiding the Tab bar for a more personalized navigation experience, and more.

## Tab Indicators

Tab indicators provide visual cues in the tab bar under certain specific conditions: When the current pane is maximized, when panes or tabs are syncronized, and when a command exits with an error. These indicators serve as quick references.

### How to toggle Tab Indicators

* Navigate to `Settings > Appearance > Tabs`, and switch the "Show Tab Indicators" option.
* Utilize the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), then search for "Tab indicators" to toggle the tab indicators.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e15caaccd0a3cd50fde45eb6333367d7522289a9%2Ftab-indicator-demo.gif?alt=media" alt=""><figcaption><p>Tab Indicator Demo</p></figcaption></figure>

## Tab Bar

The tab bar provides easy navigation between open tabs. By default, the tab bar is visible in windowed mode but hides in fullscreen. To access the tab bar when hidden, hover near the top of the window. You can customize its visibility based on your preferences.

### How to configure the Tab Bar

* Navigate to `Settings > Appearance > Tabs > Show the tab bar` to toggle the visibility of the tab bar. Choose from the following options:
  * Always – Keeps the tab bar visible at all times.
  * Only on hover – Hides the tab bar in both modes.
  * When windowed – Displays the tab bar only in windowed mode.
* Block dividers

{% hint style="info" %}
On macOS, traffic lights will not be shown when in windowed mode if the tab bar is set to show only on hover.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-136a85d4addad0cd9dacd621aff494bce668fd5d%2Ftab-bar-demo.gif?alt=media" alt=""><figcaption><p>Tab Bar Demo</p></figcaption></figure>

## Tab Close Button

You can configure the position of the Tab close button to be either on the left or right side of the tab.

### How to configure the Tab Close Button

Navigate to `Settings > Appearance > Tabs > Tab close button position`, then choose from the following options:

* Left - the close button will be on the left side of the Tab (macOS style)
* Right – the close button will be on the right side of the tab (Windows | Linux style)\\

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-c01b6685d60d608e9f91e3da5b3406151fad8092%2Ftab-close-button-demo.gif?alt=media" alt=""><figcaption><p>Tab close button demo</p></figcaption></figure>

## Recommended AI prompts

Recommended prompts can be shown in new tabs to help get quick help from Agent Mode with installing, coding, deploying, or something else.

### How to toggle recommended AI prompts

* Navigate to `Settings > Features > General`, and switch the "Recommend AI Prompts on new tab" option.
* Utilize the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), then search for "Recommend AI Prompts" to toggle.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-213f314c29024b9314510347a1125c7962e721dc%2Fai-prompts-new-tab.png?alt=media" alt=""><figcaption><p>Recommended AI Prompts in new tab</p></figcaption></figure>


# App Icons

Warp supports a palette of built-in app icons.

{% hint style="info" %}
App icons are only available for Warp on macOS. The feature doesn't support custom dock icons.
{% endhint %}

## How to change the app icon

* Navigate to `Settings > Appearance > Icon > Customize your app icon`
* Select the desired dock icon from the drop down menu

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e6181d548a3118b4335fc5768734c77dcedba26f%2FScreenshot%202024-12-04%20at%201.13.50%E2%80%AFPM.png?alt=media" alt=""><figcaption><p>Icon customization drop-down menu</p></figcaption></figure>

## Dock icons

By default, Warp ships with these dock icons:

<table data-view="cards"><thead><tr><th align="center"></th><th align="center"></th></tr></thead><tbody><tr><td align="center"><div><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-52bddd7e3c22b8582ea27dfe3a49a429e60fc4b3%2Fmoody-dev-default-icon.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td align="center">Default</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5cd5e81553bc0e584229a4ddd15203e7d0cc0f79%2Fdefault-icon.png?alt=media" alt="" data-size="original"></td><td align="center">Warp 1.0</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ae6711476fed40481b7f47ea2b88ca3accbce3c0%2FCleanShot%202024-12-05%20at%2010.12.39.png?alt=media" alt="" data-size="original"></td><td align="center">Aurora</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8a3c52e68f21b2343acf9c76c4b4ca03314909ba%2FCleanShot%202024-12-05%20at%2010.13.15.png?alt=media" alt="" data-size="original"></td><td align="center">Classic 1</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6a59c1f0504ddee05f644f91de10e5b278b41186%2FCleanShot%202024-12-05%20at%2010.13.46.png?alt=media" alt="" data-size="original"></td><td align="center">Classic 2</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-555ebd06539dca482a9268f3074c5c9b73f3c117%2FCleanShot%202024-12-05%20at%2010.14.32.png?alt=media" alt="" data-size="original"></td><td align="center">Classic 3</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-04038586135b94210f82a34f386294e579333539%2FCleanShot%202024-12-05%20at%2010.14.59.png?alt=media" alt="" data-size="original"></td><td align="center">Comets</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6ede70bbf529f4c394070083ffaf7fb0ba475315%2FCleanShot%202024-12-05%20at%2010.15.31.png?alt=media" alt="" data-size="original"></td><td align="center">Glass Sky</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5864365a95a3758b55ccadaf48d8825fe5b49f19%2FCleanShot%202024-12-05%20at%2010.16.08.png?alt=media" alt="" data-size="original"></td><td align="center">Glitch</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6652a6541d17fa331ad89b201e127b1fb9384122%2FCleanShot%202024-12-05%20at%2010.16.58.png?alt=media" alt="" data-size="original"></td><td align="center">Glow</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d42a9b04c200fddca1c001fa0bc56bf2ba15051f%2FCleanShot%202024-12-05%20at%2010.17.45.png?alt=media" alt="" data-size="original"></td><td align="center">Holographic</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-42acf2b5f55bd27522e13d7249e453ed63a7c542%2FCleanShot%202024-12-05%20at%2010.18.17.png?alt=media" alt="" data-size="original"></td><td align="center">Mono</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d593827d3d09014e96a92de7c6c6d86c12c373f1%2FCleanShot%202024-12-05%20at%2010.18.45.png?alt=media" alt=""></td><td align="center">Neon</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bd370295a2b51f4773b3b77fbaa6e71f17afc120%2FCleanShot%202024-12-05%20at%2010.19.33.png?alt=media" alt="" data-size="original"></td><td align="center">Original</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6c51867c3cfbf2278fe841fa886b6dff5e79cc74%2FCleanShot%202024-12-05%20at%2010.20.09.png?alt=media" alt="" data-size="original"></td><td align="center">Starburst</td></tr><tr><td align="center"><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-c4485a41f670c9ffc6fb00fdcb6fff60d08d352f%2FCleanShot%202024-12-05%20at%2010.20.41.png?alt=media" alt="" data-size="original"></td><td align="center">Sticker</td></tr></tbody></table>


# Blocks

A Block groups commands and outputs into one atomic unit.

## What are Blocks?

Blocks enable us to easily:

* Copy a command
* Copy a command’s output
* Scroll directly to the start of a command’s output
* Re-input commands
* Share both a command and its output (with formatting!)
* Bookmark commands

{% hint style="info" %}
Interested in how we differentiate input and output, or how we implement blocks? Check out our blog post: [How Warp Works.](https://blog.warp.dev/how-warp-works/#implementing-blocks)
{% endhint %}

<figure><img src="broken-reference" alt="Blocks"><figcaption><p>Blocks</p></figcaption></figure>


# Block Basics

The basics of creating, selecting, and navigating between Blocks.

## The Basics

* Blocks group your command and command output
* The Input Editor can pin to the bottom, pin to the top, or start at the top.
* Blocks grow from the bottom to the top.
* Blocks are color-coded. Blocks that quit with a non-zero exit code have a red background and red sidebar.

{% hint style="info" %}
Try it yourself!\
Type `xyz` (or some other command that doesn’t exist) and hit `ENTER`
{% endhint %}

## Create A Block

1. Execute a command (type `ls` and hit `ENTER`) in the Input Editor at the bottom of the screen.
2. Your command and output are grouped into a Block.
3. Try executing a different command (type `echo hello` and hit `ENTER`).
4. Warp adds your newly created Block to the bottom (directly above the input editor).

{% embed url="<https://www.loom.com/share/4b435c78344d4dc0bb92af5d1da5e219?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Create a Block
{% endembed %}

## Select a Single Block

{% tabs %}
{% tab title="macOS" %}

* Using your mouse: click on a Block.
* Or using your keyboard: hit `CMD-UP` (or `CMD-DOWN` if input as pinned up top) to select the most recently executed Block and use the `UP ↑` and `DOWN ↓` arrow keys to navigate to the desired Block.
* For long Blocks:
  * You can click "Jump to the bottom of this block".
  * You can press `SHIFT-CMD-UP`/`SHIFT-CMD-DOWN` to Scroll to the top/bottom of the selected block.
  * From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), you can also "Scroll to the top/bottom of selected block".
    {% endtab %}

{% tab title="Windows" %}

* Using your mouse: Click on a Block.
* Or using your keyboard: hit `CTRL-UP` (or `CTRL-DOWN` if input as pinned up top) to select the most recently executed Block and use the `UP ↑` and `DOWN ↓` arrow keys to navigate to the desired Block.
* For long Blocks:
  * You can click "Jump to the bottom of this block".
  * You can press `CTRL-SHIFT-UP`/`CTRL-SHIFT-DOWN` to Scroll to the top/bottom of the selected block.
  * From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), you can also "Scroll to the top/bottom of selected block".
    {% endtab %}

{% tab title="Linux" %}

* Using your mouse: Click on a Block.
* Or using your keyboard: hit `CTRL-UP` (or `CTRL-DOWN` if input as pinned up top) to select the most recently executed Block and use the `UP ↑` and `DOWN ↓` arrow keys to navigate to the desired Block.
* For long Blocks:
  * You can click "Jump to the bottom of this block".
  * You can press `CTRL-SHIFT-UP`/`CTRL-SHIFT-DOWN` to Scroll to the top/bottom of the selected block.
  * From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), you can also "Scroll to the top/bottom of selected block".
    {% endtab %}
    {% endtabs %}

{% embed url="<https://www.loom.com/share/1cf8546daad548fbbe056c35edb23cdc?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Select a Single Block
{% endembed %}

## Select Multiple Blocks

{% tabs %}
{% tab title="macOS" %}

* Click another Block while holding `CMD` to toggle the selection of that Block, or
* Click another Block while holding `SHIFT` to select a range of Block, or
* Use `SHIFT-UP ↑` or `SHIFT-DOWN ↓` to expand the active selection (the Block with the thicker border) up or down, respectively.
  {% endtab %}

{% tab title="Windows" %}

* Click another Block while holding `CTRL-SHIFT` to toggle the selection of that Block, or
* Click another Block while holding `SHIFT` to select a range of Block, or
* Use `SHIFT-UP ↑` or `SHIFT-DOWN ↓` to expand the active selection (the Block with the thicker border) up or down, respectively.
  {% endtab %}

{% tab title="Linux" %}

* Click another Block while holding `CTRL-SHIFT` to toggle the selection of that Block, or
* Click another Block while holding `SHIFT` to select a range of Block, or
* Use `SHIFT-UP ↑` or `SHIFT-DOWN ↓` to expand the active selection (the Block with the thicker border) up or down, respectively.
  {% endtab %}
  {% endtabs %}

{% embed url="<https://www.loom.com/share/5058ab0dc3d244d4a2ce576331440821?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Select Multiple Blocks
{% endembed %}

## Navigate Blocks

* Either scroll using your mouse or the scrollbar or select a Block and use the `UP ↑` and `DOWN ↓` arrow keys.
* "Scroll Terminal output up/down one line" is also a way to navigate block output, and can be configured with a keyboard shortcut or accessed from the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).
* When the output of a command is cut off, Warp keeps the [Sticky Command Header](https://docs.warp.dev/documentation/terminal/blocks/sticky-command-header) pinned at the top that displays the command the Block corresponds to. Clicking the header will scroll the screen to the start of the Block.

{% embed url="<https://www.loom.com/share/21ebb0a79c1248a98846cba12a4b7020?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Navigate between Blocks
{% endembed %}


# Block Actions

All the cool features Blocks provide.

## Accessing Block Actions

There are 2 ways you can access Block actions.

1. Hover over a Block and click the kebab (three dots) button on the right-hand side.
2. Right-click a Block.

{% embed url="<https://www.loom.com/share/3dec25e548d4484aa3dd6437869e2bbf?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Accessing Block Actions
{% endembed %}

## Copy Input / Output of Block

For command blocks, you can `RIGHT-CLICK` on a Block or click the context menu and copy the Block command, output, or both.

For AI blocks, you can `RIGHT-CLICK` to copy the prompt, output, both or the entire conversation.

{% embed url="<https://www.loom.com/share/9ad67eca0a8d47afb82cc1acba617f3c?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Copy Block Actions
{% endembed %}

## Sharing a Block

Share a block easily with coworkers or teammates by creating a web permalink. This preserves formatting and makes debugging and sharing output easy. [See Block Sharing Page.](https://docs.warp.dev/documentation/terminal/blocks/block-sharing)

## Bookmarking a Block

Quickly navigate to important Blocks despite where they are in the terminal history.

{% tabs %}
{% tab title="macOS" %}
Ways to bookmark a Block:

1. Select `Toggle bookmark` in the block context menu
2. Use `CMD-B` keybinding to bookmark a selected block

Navigate to a bookmarked Block, by:

* Clicking on the indicator.\
  The indicator position reflects the approximate position of the Block in the Block history. Hovering over the indicator will give a snapshot of the Block including its prompt, command, and the last two lines of output.
* Pressing `OPTION-UP` and `OPTION-DOWN`
  {% endtab %}

{% tab title="Windows" %}
There are Ways to bookmark a Block:

1. Select `Toggle bookmark` in the block context menu
2. Use `CTRL-SHIFT-B` keybinding to bookmark a selected block

Navigate to a bookmarked Block, by:

* Clicking on the indicator.\
  The indicator position reflects the approximate position of the Block in the Block history. Hovering over the indicator will give a snapshot of the Block including its prompt, command, and the last two lines of output.
* Pressing `ALT-UP` and `ALT-DOWN`
  {% endtab %}

{% tab title="Linux" %}
Ways to bookmark a Block:

1. Click on the bookmark icon in the top right corner of a Block
2. Select `Toggle bookmark` in the block context menu
3. Use `CTRL-SHIFT-B` keybinding to bookmark a selected block

Navigate to a bookmarked Block, by:

* Clicking on the indicator.\
  The indicator position reflects the approximate position of the Block in the Block history. Hovering over the indicator will give a snapshot of the Block including its prompt, command, and the last two lines of output.
* Pressing `ALT-UP` and `ALT-DOWN`
  {% endtab %}
  {% endtabs %}

{% hint style="info" %}
Bookmarks only persist while the session is open, once you close the session they are lost. If you want to save the command and output for later use, [Share the Block](https://docs.warp.dev/documentation/terminal/blocks/block-sharing).
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ce03da65a5db101052441f0d7e2c54cd71439e4c%2Fblock-bookmarks.gif?alt=media" alt=""><figcaption><p>Bookmarking a Block</p></figcaption></figure>

## Search Within A Block

Quickly find important information within a Block. [See Find page](https://docs.warp.dev/documentation/terminal/blocks/find)

{% tabs %}
{% tab title="macOS" %}
With a Block selected, press "Find Within Block" or use `CMD-F` to search within a Block.
{% endtab %}

{% tab title="Windows" %}
With a Block selected, Press "Find Within Block" or use `CTRL-SHIFT-F` to search within a Block.
{% endtab %}

{% tab title="Linux" %}
With a Block selected, Press "Find Within Block" or use `CTRL-SHIFT-F` to search within a Block.
{% endtab %}
{% endtabs %}

{% embed url="<https://www.loom.com/share/7dda0e7a6ec144cfb6410d29a586ddd0?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Search within a Block
{% endembed %}

## Filtering a Block

Filter the output lines of a block natively in Warp to quickly focus on a subset of the block. [See Block Filtering Page](https://docs.warp.dev/documentation/terminal/blocks/block-filtering).

{% tabs %}
{% tab title="macOS" %}

* Using the keybinding `OPT-SHIFT-F` by default to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}

{% tab title="Windows" %}

* Using the keybinding `ALT-SHIFT-F` to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}

{% tab title="Linux" %}

* Using the keybinding `ALT-SHIFT-F` to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}
  {% endtabs %}


# Block Sharing

Share a block with your team or community.

{% hint style="info" %}
This action sends command information to our server and is explicitly opt-in. Read more about privacy at Warp on [our privacy page](https://www.warp.dev/privacy).
{% endhint %}

Share your blocks with a permalink or HTML embed. You can get started with shared blocks by opening the context menu and copying the command, output, or prompt.

## How to Share Blocks

{% tabs %}
{% tab title="macOS" %}
To share your blocks, follow these steps:

1. On a finished block, click the context menu and select `Share...` or select the block and hit `CMD-SHIFT-S`.
2. A modal will pop up that lets you title your block and customize it by selecting which parts of the block you want to share (e.g. command, output, prompt, etc.).
3. Click either "Create link" or "Get embed" depending on how you want to share your block.
4. The link or embed snippet will be copied to your clipboard.
   {% endtab %}

{% tab title="Windows" %}
To share your blocks, follow these steps:

1. On a finished block, click the context menu and select `Share...` or by setting up a key bind for Share Block in `Settings > Keyboard Shortcuts`.
2. A modal will pop up that lets you title your block and customize it by selecting which parts of the block you want to share (e.g. command, output, prompt, etc.).
3. Click either "Create link" or "Get embed" depending on how you want to share your block.
4. The link or embed snippet will be copied to your clipboard.
   {% endtab %}

{% tab title="Linux" %}
To share your blocks, follow these steps:

1. On a finished block, click the context menu and select `Share...` or by setting up a key bind for Share Block in `Settings > Keyboard Shortcuts`.
2. A modal will pop up that lets you title your block and customize it by selecting which parts of the block you want to share (e.g. command, output, prompt, etc.).
3. Click either "Create link" or "Get embed" depending on how you want to share your block.
4. The link or embed snippet will be copied to your clipboard.
   {% endtab %}
   {% endtabs %}

{% hint style="info" %}
If you experience any issues with block sharing, please see our known issues for [troubleshooting steps](https://docs.warp.dev/documentation/support-and-billing/known-issues#online-features-dont-work).
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a4fd4b700beedbbec7864cd4c309b53ff75461cb%2Fblock-sharing-embed.gif?alt=media&#x26;token=02f237e8-061c-42ee-93ae-cb6b1da9fdc6" alt=""><figcaption><p>Block Sharing &#x26; Embed Demo</p></figcaption></figure>

## Permalink

Create and share a permalink to your blocks to collaborate with teammates. Here is the [web permalink](https://app.warp.dev/block/vzFATak939iqGWfNh7wsAP) of the block depicted below.

![Shared Block](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-221d43e8629ad806343376b4647d9d7188c8ca86%2Fshared_block.png?alt=media\&token=8f429a14-bdaf-4e2e-8e19-92525657252b)

## Embedded Blocks

Create and embed your blocks on web pages to help your readers follow along with technical writing. Readers can interact with an embedded block as they would with a block in Warp, with a context menu and styling. When you click "Get embed", Warp will copy an `iframe` to your clipboard. Here's an example `iframe`:

```html
<iframe src="https://app.warp.dev/block/embed/qn0g1CqQnkYjEafPH5HCVT"
title="server script error" style="width: 712px; height: 397px; border:0;
overflow:hidden;" allow="clipboard-read; clipboard-write"></iframe>
```

#### Embedded Block Example on Web Page

![Embedded Block Example](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d9229fcb56841824629e982884ea5bb8aee0781f%2Fembed.png?alt=media\&token=15202210-1745-45a1-9b41-3a7244b0dfc4)

## Managing Shared Blocks

You can unshare a block by navigating to `Settings > Shared blocks`. Currently, shared blocks are accessible to anyone with the link.

## Link Previews

Shared permalinks will also display a preview of your code for quick context on each link.

{% hint style="info" %}
Compatible with any platform that supports Open Graph or Twitter meta tags. For example Slack, Twitter, Facebook, Telegram, Notion, and more ...
{% endhint %}

{% embed url="<https://www.loom.com/share/a78147fee8804c00b08a1decbc0d4e72?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Share and Unfurl a Block Preview
{% endembed %}


# Block Find

Find in Warp works unlike how you may have seen in other terminals. Instead of searching from the lowest point in view as with text editors or from the top as with terminals.

## What is it

Find searches for matches in all your Blocks from the bottom up and can even be isolated to a specific Block.

{% hint style="info" %}
Since command outputs are contained within Blocks, you can still use the input editor when invoking find.
{% endhint %}

## How to access it

{% tabs %}
{% tab title="macOS" %}

1. Hitting `CMD-F` opens the find view which searches across the terminal (scoped within the current pane).
2. Within the find modal, you can also enable the regex toggle, find on a selected Block, and or toggle case sensitive search.
   {% endtab %}

{% tab title="Windows" %}

1. Hitting `CTRL-SHIFT-F` opens the find view which searches across the terminal (scoped within the current pane).
2. Within the find modal, you can also enable the regex toggle, find on a selected Block, and or toggle case sensitive search.
   {% endtab %}

{% tab title="Linux" %}

1. Hitting `CTRL-SHIFT-F` opens the find view which searches across the terminal (scoped within the current pane).
2. Within the find modal, you can also enable the regex toggle, find on a selected Block, and or toggle case sensitive search.
   {% endtab %}
   {% endtabs %}

## How it works

![Find](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ae6ed470ebb4a9eb546165e6d92267a8098734a5%2Ffind.gif?alt=media\&token=75702056-0574-4056-bee3-604edda497fc)


# Block Filtering

Quickly filter and focus on a subset of a block.

Filter the output lines of a block in Warp to quickly focus on a subset of the block. You can filter by plaintext, regex, invert, or make your filter case-sensitive. You can also add context lines to view output around matches. Filtering does not delete any output lines, so you can clear the filter to go back to the original output.

## How to filter a block

To apply a filter to a block:

1. Click on the filter icon in the top right corner of a block. A filter editor will appear with a large input field with two buttons on the left and a smaller input field on the right.
2. Type in the input to filter the block in the left input field. Only lines containing text that matches the filter query will be shown.
3. (Optional) Click on the regex, case sensitive search, or invert filter buttons to enable.
4. (Optional) Type a number in the right input field to add context lines around matched lines.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5f6785698f91c37b77b73df65d4d4d93808bec3a%2Fblock_filtering_with_context_lines.gif?alt=media&#x26;token=1008c7bb-0679-40c8-a936-8acb60208eef" alt=""><figcaption><p>Filter a block's output, with the ability to add context lines.</p></figcaption></figure>

{% tabs %}
{% tab title="macOS" %}
You can also toggle a filter by:

* Using the keybinding `OPT-SHIFT-F` by default to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}

{% tab title="Windows" %}
You can also toggle a filter on/off by:

* Using the keybinding `ALT-SHIFT-F` to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}

{% tab title="Linux" %}
You can also toggle a filter on/off by:

* Using the keybinding `ALT-SHIFT-F` to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}
  {% endtabs %}

{% hint style="info" %}
Toggling a filter on a block without a filter applied will open the filter editor. If you toggle a filter off, the same filter will be applied if you toggle filtering on again.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6ef2a07dd1deac53be41c2fa3c8b9dcdb4a8bc42%2Fblock_filtering_toggle.gif?alt=media&#x26;token=4684807d-957c-43f0-90d5-7112a975a720" alt=""><figcaption><p>Toggle a block filter on/off.</p></figcaption></figure>


# Background Blocks

How Blocks interact with background process output.

## What is it

Commands can start background processes that continue even after they exit. You can also start a background process directly from the shell, such as by running it with `&`.

If Warp receives output that is likely from a background process, the output goes into a *background block*. Background blocks act like regular blocks, except that they don't have an associated command.

This lets you use all of Warp's block features with background output, such as sharing and bookmarking.

## How to use it

Background blocks are automatically created as needed, in between regular blocks running. If you run commands while a background process is still producing output, that output gets split into multiple blocks interleaved with your commands.

## How it works

{% embed url="<https://www.loom.com/share/55bbbd9a8cbf495189260756c717cfb2?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Create Background Blocks
{% endembed %}

## Troubleshooting Background Blocks

There are some limitations, because Warp doesn't know *which* process any given output came from:

* If a background process writes output while a foreground command is running in a regular block, the output goes into that block.
* If there are multiple background processes running at the same time, their output may be mixed together.

In addition, if you start entering a command while another one is running (typeahead), in some cases Warp will mistake the partial command for background output. The most common cause is editing typeahead when using bash versions older than 4.0 (for example, deleting and re-typing part of it).


# Sticky Command Header

Sticky Command Header shows you the command run for a large Block that is scrolled partially off-screen. This helps you see the command that was previously run or currently running jump to the top.

{% hint style="info" %}
For long-running commands that take up the full screen, the sticky header only shows after you start scrolling up. This is to prevent the header from blocking the top part of the output for commands like `git log` that simulate full-screen apps.
{% endhint %}

## How to access Sticky Command Header

{% tabs %}
{% tab title="macOS" %}

* Sticky Command Header is enabled by default.
* Toggle Sticky Command Header by going to `Settings > Features` > toggle “Show sticky command header”.
* Toggle by searching for “Sticky Command Header” within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or by pressing `CTRL-CMD-S`.
* You can also "Toggle the Sticky Command Header in the Active Pane" with `CTRL-S`. This won't disable the feature entirely, only minimize it on the active session.
  {% endtab %}

{% tab title="Windows" %}

* Sticky Command Header is enabled by default.
* Toggle the Sticky Command Header by going to `Settings > Features` > toggle “Show sticky command header”.
* Toggle by searching for “Sticky Command Header” within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or by setting up a key bind in `Settings > Keyboard Shortcuts`.
* You can also "Toggle the Sticky Command Header in the Active Pane" in the Command Palette or by setting up a key bind in `Settings > Keyboard Shortcuts`. This won't disable the feature entirely, only minimize it on the active session.
  {% endtab %}

{% tab title="Linux" %}

* Sticky Command Header is enabled by default.
* Toggle the Sticky Command Header by going to `Settings > Features` > toggle “Show sticky command header”.
* Toggle by searching for “Sticky Command Header” within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or by setting up a key bind in `Settings > Keyboard Shortcuts`.
* You can also "Toggle the Sticky Command Header in the Active Pane" in the Command Palette or by setting up a key bind in `Settings > Keyboard Shortcuts`. This won't disable the feature entirely, only minimize it on the active session.
  {% endtab %}
  {% endtabs %}

## How to use Sticky Command Header

* If a Block has a large output ( e.g. `seq 1 1000`), the header of the Block will show on the top of the active Window, Tab, or Pane.
* Click on the Sticky Command Header to quickly jump to the top of the Block.
* While active you can also minimize the Sticky Command Header on the active pane by clicking the UP/DOWN arrow in the middle of the header.

## How Sticky Command Header works

{% embed url="<https://www.loom.com/share/a86967c057e44ab4bee4860ba80538b9?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Sticky Command Header Demo
{% endembed %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-242f19a3d854b7d78baad1fbfab7eb39e99406c9%2Fsticky-header-toggle-active-demo.gif?alt=media&#x26;token=149d5628-3b7c-4548-ad83-03bb98f807d5" alt=""><figcaption><p>Toggle active header and Jump to bottom of block demo</p></figcaption></figure>


# Modern Text Editing

Unlike other terminals, Warp’s input editor operates out of the box like a modern IDE and the text editors we’re used to.

{% hint style="info" %}
Text Editor Input also works for [SSH sessions](https://docs.warp.dev/documentation/terminal/warpify/ssh).
{% endhint %}

### Soft Wrapping

Warp supports soft wrapping in the input editor. If an autosuggestion goes off-screen, the input editor will be horizontally scrollable to make it visible. Some operations treat soft-wrapped lines like a logical line (`TRIPLE-CLICK`) while other operations treat soft wrapped lines like visible different lines (`UP`/`DOWN`, `SHIFT-UP`/`SHIFT-DOWN`).

### Copy on Select

Warp supports copy on select for selectable text within [Blocks](https://docs.warp.dev/documentation/terminal/blocks).

* Toggle this feature `Settings > Features > General` or search for "Copy on select" in the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).

### Autocomplete Quotes, Parentheses, and Brackets

Warp can automatically complete quotes, brackets, and parentheses like you're used to in IDEs.

* Toggle this feature `Settings > Features > Editor` or search for "Autocomplete quotes" in the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).

## How to use it

{% tabs %}
{% tab title="macOS" %}

<table><thead><tr><th width="317">Keyboard binding</th><th>Shortcut description</th></tr></thead><tbody><tr><td><code>ESCAPE</code></td><td>Closes the input suggestions or history menu</td></tr><tr><td><code>CTRL-L</code></td><td>Clears the terminal</td></tr><tr><td><code>CTRL-H</code></td><td>Backspace</td></tr><tr><td><code>CTRL-C</code></td><td>Clear the entire editor buffer</td></tr><tr><td><code>CTRL-U</code></td><td>Copy and Clear the current line</td></tr><tr><td><code>CMD-SHIFT-K</code></td><td>Clear selected lines</td></tr><tr><td><code>CMD-C</code>, <code>CMD-X</code>, <code>CMD-V</code></td><td>Copy, cut, paste</td></tr><tr><td><code>CTRL-W</code> / <code>OPT-D</code></td><td>Cut the word to the left / right of the cursor</td></tr><tr><td><code>OPT-BACKSPACE</code> / <code>OPT-D</code></td><td>Delete the word to the left / right of the cursor</td></tr><tr><td><code>CTRL-K CMD-DELETE</code></td><td>Delete everything to the right of the cursor</td></tr><tr><td><code>OPT-LEFT</code> / <code>OPT-RIGHT</code></td><td>Move to the beginning of the previous / next word</td></tr><tr><td><code>CTRL-OPT-LEFT</code> / <code>CTRL-OPT-RIGHT</code></td><td>Move backward / forward by one subword</td></tr><tr><td><code>CMD-LEFT</code> <code>CTRL-A</code>/ <code>CTRL-E</code> <code>CMD-DOWN</code> <code>CMD-RIGHT</code></td><td>Move the cursor to the start / end of the line</td></tr><tr><td><code>SHIFT-LEFT</code> / <code>SHIFT-RIGHT</code></td><td>Select the character to the left / right of the cursor</td></tr><tr><td><code>OPT-SHIFT-LEFT</code> / <code>OPT-SHIFT-RIGHT</code></td><td>Select the word to the left / right of the cursor</td></tr><tr><td><code>CMD-SHIFT-LEFT</code> / <code>CMD-SHIFT-RIGHT</code></td><td>Select everything to the left / right of the cursor</td></tr><tr><td><code>SHIFT-UP</code> / <code>SHIFT-UP</code></td><td>Select everything above / below the cursor</td></tr><tr><td><code>CMD-A</code></td><td>Select the entire editor buffer</td></tr><tr><td><code>SHIFT-ENTER</code> <code>CTRL-ENTER</code> <code>OPT-ENTER</code></td><td>Insert newline</td></tr><tr><td><code>CTRL-R</code></td><td>Command Search</td></tr><tr><td><code>CMD-D</code></td><td>Split pane</td></tr></tbody></table>
{% endtab %}

{% tab title="Windows" %}

<table><thead><tr><th width="317">Keyboard binding</th><th>Shortcut description</th></tr></thead><tbody><tr><td><code>ESCAPE</code></td><td>Closes the input suggestions or history menu</td></tr><tr><td><code>CTRL-L</code></td><td>Clears the terminal</td></tr><tr><td><code>CTRL-H</code></td><td>Backspace</td></tr><tr><td><code>CTRL-C</code></td><td>Clear the entire editor buffer</td></tr><tr><td><code>CTRL-U</code></td><td>Copy and Clear the current line</td></tr><tr><td><code>CTRL-SHIFT-K</code></td><td>Clear selected lines</td></tr><tr><td><code>CTRL-C</code>, <code>CTRL-X</code>, <code>CTRL-V</code></td><td>Copy, cut, paste</td></tr><tr><td><code>CTRL-W</code> / <code>ALT-D</code></td><td>Cut the word to the left / right of the cursor</td></tr><tr><td><code>ALT-BACKSPACE</code> / <code>ALT-D</code></td><td>Delete the word to the left / right of the cursor</td></tr><tr><td><code>CTRL-K</code></td><td>Delete everything to the right of the cursor</td></tr><tr><td><code>ALT-LEFT</code> / <code>ALT-RIGHT</code></td><td>Move to the beginning of the previous / next word</td></tr><tr><td><code>CTRL-LEFT</code> / <code>CTRL-RIGHT</code></td><td>Move backward / forward by one subword</td></tr><tr><td><code>CTRL-A</code>/ <code>CTRL-E</code></td><td>Move the cursor to the start / end of the line</td></tr><tr><td></td><td>Select the character to the left / right of the cursor</td></tr><tr><td><code>META-SHIFT-B</code> / <code>META-SHIFT-F</code></td><td>Select the word to the left / right of the cursor</td></tr><tr><td></td><td>Select everything to the left / right of the cursor</td></tr><tr><td><code>SHIFT-UP</code> / <code>SHIFT-UP</code></td><td>Select everything above / below the cursor</td></tr><tr><td><code>CTRL-A</code></td><td>Select the entire editor buffer</td></tr><tr><td><code>SHIFT-ENTER</code> <code>CTRL-ENTER</code> <code>ALT-ENTER</code></td><td>Insert newline</td></tr><tr><td><code>CTRL-R</code></td><td>Command Search</td></tr><tr><td><code>CTRL-SHIFT-D</code></td><td>Split pane</td></tr></tbody></table>
{% endtab %}

{% tab title="Linux" %}

<table><thead><tr><th width="317">Keyboard binding</th><th>Shortcut description</th></tr></thead><tbody><tr><td><code>ESCAPE</code></td><td>Closes the input suggestions or history menu</td></tr><tr><td><code>CTRL-L</code></td><td>Clears the terminal</td></tr><tr><td><code>CTRL-H</code></td><td>Backspace</td></tr><tr><td><code>CTRL-C</code></td><td>Clear the entire editor buffer</td></tr><tr><td><code>CTRL-U</code></td><td>Copy and Clear the current line</td></tr><tr><td><code>CTRL-SHIFT-K</code></td><td>Clear selected lines</td></tr><tr><td><code>CTRL-C</code>, <code>CTRL-X</code>, <code>CTRL-V</code></td><td>Copy, cut, paste</td></tr><tr><td><code>CTRL-W</code> / <code>ALT-D</code></td><td>Cut the word to the left / right of the cursor</td></tr><tr><td><code>ALT-BACKSPACE</code> / <code>ALT-D</code></td><td>Delete the word to the left / right of the cursor</td></tr><tr><td><code>CTRL-K</code></td><td>Delete everything to the right of the cursor</td></tr><tr><td><code>ALT-LEFT</code> / <code>ALT-RIGHT</code></td><td>Move to the beginning of the previous / next word</td></tr><tr><td><code>CTRL-LEFT</code> / <code>CTRL-RIGHT</code></td><td>Move backward / forward by one subword</td></tr><tr><td><code>CTRL-A</code>/ <code>CTRL-E</code></td><td>Move the cursor to the start / end of the line</td></tr><tr><td></td><td>Select the character to the left / right of the cursor</td></tr><tr><td><code>META-SHIFT-B</code> / <code>META-SHIFT-F</code></td><td>Select the word to the left / right of the cursor</td></tr><tr><td></td><td>Select everything to the left / right of the cursor</td></tr><tr><td><code>SHIFT-UP</code> / <code>SHIFT-UP</code></td><td>Select everything above / below the cursor</td></tr><tr><td><code>CTRL-A</code></td><td>Select the entire editor buffer</td></tr><tr><td><code>SHIFT-ENTER</code> <code>CTRL-ENTER</code> <code>ALT-ENTER</code></td><td>Insert newline</td></tr><tr><td><code>CTRL-R</code></td><td>Command Search</td></tr><tr><td><code>CTRL-SHIFT-D</code></td><td>Split pane</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## How it Works

{% embed url="<https://loom.com/share/1517049fefc34227bf1abaf19cc7e6ea?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Text Editor Input Demo
{% endembed %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e80844ae06b894bf60fbb2baad6a1d8843095fcd%2Fsoft-wrapping.png?alt=media&#x26;token=b30c4a5a-0a7c-44d1-a194-2f789f48c546" alt="soft wrapping text in Warp terminal input editor"><figcaption><p>Soft Wrapping Demo</p></figcaption></figure>


# Alias Expansion

Warp will automatically expand your aliases as you type in the input editor.

## How to use it

{% tabs %}
{% tab title="macOS" %}
When Alias Expansion is enabled, type an alias and then hit `SPACE` will expand the alias.

To insert a space without expanding an alias, the default keybinding is `OPT-SPACE`.
{% endtab %}

{% tab title="Windows" %}
When Alias Expansion is enabled, type an alias and then hit `SPACE` will expand the alias.

To insert a space without expanding an alias, the default keybinding is `ALT-SPACE`.
{% endtab %}

{% tab title="Linux" %}
When Alias Expansion is enabled, type an alias and then hit `SPACE` will expand the alias.

To insert a space without expanding an alias, the default keybinding is `ALT-SPACE`.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Aliases will not be expanded when the command in the expanded form is the same as the alias itself. e.g. if you have an alias `ls='ls -G'`, `ls` will not be expanded in the input editor.
{% endhint %}

## How to access it

Alias expansion is disabled by default. There are two ways to toggle this on and off:

* From Settings: Navigate to `Settings > Features > Editor` and toggle “Expand aliases as you type”.
* From the [Command Palette](https://docs.warp.dev/documentation/command-palette#windows): Search for the “Enable/disable alias expansion” option and hit `ENTER`.

## How it works

{% embed url="<https://www.loom.com/share/2267657c033e482890eea75a8a6c5373?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Alias Expansion Demo
{% endembed %}


# Command Inspector

Command Inspector  (also known as Command X-Ray) surfaces documentation for sub-parts of your command, directly in Warp's Input Editor.

## How to access it

{% tabs %}
{% tab title="macOS" %}
Hover over the part of the command you want to inspect with your mouse or press `CMD-SHIFT-I` to inspect the cursor's current location.
{% endtab %}

{% tab title="Windows" %}
Hover over the part of the command you want to inspect with your mouse or press `CTRL-SHIFT-I` to inspect the cursor's current location.
{% endtab %}

{% tab title="Linux" %}
Hover over the part of the command you want to inspect with your mouse or press `CTRL-SHIFT-I` to inspect the cursor's current location.
{% endtab %}
{% endtabs %}

## How it works

{% embed url="<https://www.loom.com/share/a00259927ada41b2895fd5c4072a3dcc?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Command Inspector Demo
{% endembed %}


# Syntax & Error Highlighting

Syntax Highlighting differentiate between sub-commands, options/flags, arguments, and variables. Error Highlighting automatically underlines any invalid commands with a dashed red underline.

## What is Syntax Highlighting

Warp supports Syntax Highlighting in the [Input Editor.](https://docs.warp.dev/documentation/terminal/editor) It colors each part of a command to help differentiate between sub-commands, options/flags, arguments, and variables.

{% hint style="warning" %}
Newly installed apps or newly created aliases will not trigger syntax highlighting until you open a new Warp session (new window, tab, or pane), even if you `source` the RC files in the current session.
{% endhint %}

### How to access Syntax Highlighting

When Syntax Highlighting is enabled, Warp's [Input Editor](https://docs.warp.dev/documentation/terminal/editor) automatically recognizes each part of the command as you type it into the Input Editor, and syntactically highlight them.

### How to enable/disable Syntax Highlighting

Syntax highlighting is enabled by default, to toggle it:

* Through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), search for the "Syntax Highlighting" option and click it (or press enter) to enable/disable.
* Through `Settings > Features > Editor` , toggle "Syntax highlighting for commands"

### How Syntax Highlighting Works

{% embed url="<https://www.loom.com/share/87b15de13ee9407b98a24f1a31835784?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Syntax Highlighting Demo
{% endembed %}

## What is Error Underlining

Warp highlights errors in commands that are typed within the [Input Editor](https://docs.warp.dev/documentation/terminal/editor) e.g. if the binary for the command you've typed does not exist.

{% hint style="warning" %}
Newly installed apps or newly created aliases will trigger error underlining until you open a new Warp session (new window, tab, or pane), even if you `source` the RC files in the current session.
{% endhint %}

### How to access Error Underlining

When Error Underlining is enabled, Warp automatically underlines any invalid commands with a dashed red underline.

### How to enable/disable Error Underlining

Error underlining is enabled by default, to toggle it:

* Through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), search for the "Syntax Highlighting" option and click it (or press enter) to enable/disable.
* Through `Settings > Features > Editor` , toggle "Error underlining for commands"

### How Error Underlining works

{% embed url="<https://www.loom.com/share/7721e06ed4aa4e1380abae4f5827ef6f?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Error Underlining Demo
{% endembed %}


# Input Editor Vim Keybindings

Use Input Editor Vim keybindings (also known as Vim mode) to edit commands quickly in Warp.

## About Vim keybindings

The Vi family of programs (including Vim and Neovim) are modal text editors that allow for keyboard-driven text editing. Several shells, including `bash` and `zsh`, implement vi-style keybindings. Warp's input editor was built natively to support more modern text editing experiences, which means it replaces the shell's editor capabilities. Warp has its implementation of Vim keybindings (also known as Vim mode) you can use.

### How to enable Vim Keybindings

{% hint style="info" %}
With `bash` and `zsh`, Warp attempts to detect the shell's keybinding settings. If a shell vi mode is detected, Warp may suggest enabling Vim keybindings (also known as Vim mode).
{% endhint %}

To manually toggle Vim keybindings in Warp's input editor:

* Through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), search for "Vim Keybindings".
* Through `Settings > Features > Editor`, toggle "Edit commands with Vim keybindings".

As in `bash` and `zsh`'s vi mode implementations, the editor starts in insert mode. Pressing `CTRL-C` or `ENTER` clears any pending command state.

### Customizing Keybindings

At the moment, Warp only supports default Vim keybindings.

One exception is the keyboard shortcut for exiting insert mode, which can be rebound under `Settings > Keyboard Shortcuts > Exit Vim Insert Mode`, or through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) search for "Exit Vim Insert Mode".

## Supported Keybindings

Below is a list of the vim functionality implemented in Warp so far.

### Movement

See [Vim docs: motion](https://vimdoc.sourceforge.net/htmldoc/motion.html) for more information.

#### Basic

| Command(s)                   | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| `h`, `j`, `k`, `l`           | single-char movement                                |
| `<space>`, `<backspace>`     | single-char movement with line wrap                 |
| `w`, `W`, `b`, `B`, `e`, `E` | word movement                                       |
| `ge`, `gE`                   | end of previous word                                |
| `$`                          | end of line                                         |
| `0`                          | beginning of line                                   |
| `^`                          | first non-whitespace character of line              |
| `%`                          | jump to matching bracket                            |
| `[`, `]`                     | prev/next unmatched bracket                         |
| `_`                          | beginning of the current line                       |
| `+`                          | first non-whitespace character of the next line     |
| `-`                          | first non-whitespace character of the previous line |

#### Multi-line-related

| Command(s) | Description             |
| ---------- | ----------------------- |
| `gg`, `G`  | jump to first/last line |

### Editing

| Command(s) | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| `r`        | replace character under cursor                              |
| `d`, `D`   | delete a range or object                                    |
| `c`, `C`   | change a range or object (delete, then go to insert mode)   |
| `s`, `S`   | substitute (like change, but can only delete at the cursor) |
| `x`, `X`   | delete under cursor                                         |
| `y`, `Y`   | yank (copy) into the clipboard                              |
| `p`, `P`   | paste from the clipboard                                    |
| `u`, `⌃r`  | undo, redo                                                  |
| `~`        | toggle upper/lowercase under cursor                         |
| `gu`       | lowercase under cursor (`u` in visual mode)                 |
| `gU`       | uppercase under cursor (`U` in visual mode)                 |
| `J`        | join current and following lines                            |
| `.`        | repeat last edit                                            |

See [Vim docs: editing](https://vimdoc.sourceforge.net/htmldoc/editing.html) for more information.

#### Text Objects

| Command(s)       | Description                                |
| ---------------- | ------------------------------------------ |
| `i`              | inner (exclude delimiters in text object)  |
| `a`              | around (include delimiters in text object) |
| `w`, `W`         | whitespace-delimited string (word)         |
| `"`, `'`, \`\`\` | quote-delimited string                     |
| `(`, `{`, `[`    | parenthesized/bracketed string             |

See [Vim docs: text objects](https://vimdoc.sourceforge.net/htmldoc/motion.html#text-objects) for more information.

### Search

#### Character Search

| Command(s)         | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `t`, `T`, `f`, `F` | find next/prev matching character on line              |
| `;`                | repeat last character search in the same direction     |
| `,`                | repeat last character search in the opposite direction |

See [Vim docs: left-right motions](https://vimdoc.sourceforge.net/htmldoc/motion.html#f) for more information.

#### General Search

Unlike Vim, general search commands don't search within the buffer. Instead, they open Warp's native command search.

| Command(s)         | Description              |
| ------------------ | ------------------------ |
| `/`, `?`, `*`, `#` | open Warp command search |

### Mode Switching

| Command(s) | Description                                                       |
| ---------- | ----------------------------------------------------------------- |
| `i`        | insert text before the cursor                                     |
| `I`        | insert text before the first non-whitespace character in the line |
| `a`        | append text after the cursor                                      |
| `A`        | append text at the end of the line                                |
| `o`        | begin new line below the cursor and insert text                   |
| `O`        | begin new line above the cursor and insert text                   |
| `v`        | visual character mode                                             |
| `V`        | visual line mode                                                  |

See [Vim docs: insert](https://vimdoc.sourceforge.net/htmldoc/insert.html#insert) and [Vim docs: visual mode](https://vimdoc.sourceforge.net/htmldoc/visual.html#visual-mode) for more information.

### Registers

| Command(s) | Description     |
| ---------- | --------------- |
| `"`        | register prefix |

Warp currently supports the following registers:

| Register name    | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| `a`–`z`, `A`–`Z` | named registers                                                  |
| `+`              | system clipboard                                                 |
| `*`              | system clipboard                                                 |
| `"`              | unnamed register, containing the text of the last delete or yank |

See [Vim docs: registers](https://vimdoc.sourceforge.net/htmldoc/change.html#registers) for more information.

## Feedback

The best way to report bugs and request features is through Warp's [GitHub Issues](https://github.com/warpdotdev/Warp/issues) page. Please note that the issue or request is for Vim Keybindings.


# Command Entry

Warp's main features for Command Entry, History, Synchronized Inputs, YAML Workflows and More!

1. [Command Corrections](https://docs.warp.dev/documentation/terminal/entry/command-corrections) provides auto-correct suggestions on previously run commands to catch typos, and forgotten flags, and fix general console errors.
2. [Command Search](https://docs.warp.dev/documentation/terminal/entry/command-search) is a 3-in-1 panel that allows you to search across Command History, Workflows, Notebooks, and A.I. Command Search all at once.
3. [Command History](https://docs.warp.dev/documentation/terminal/entry/command-history) allows Warp to isolate the history of each shell session to make previously run commands easily accessible.
4. [Synchronized Inputs](https://docs.warp.dev/documentation/terminal/entry/synchronized-inputs) allow you to easily run the same command in multiple sessions at the same time.
5. [YAML Workflows](https://docs.warp.dev/documentation/terminal/entry/yaml-workflows) are easier to execute and share parameterized and searchable commands within Warp.

## Command Corrections

{% embed url="<https://www.loom.com/share/180e1dc8d1504ec39c00694d9fd71b7c?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Command Corrections Demo
{% endembed %}

## Command Search

{% embed url="<https://www.loom.com/share/21a6f58a33754ee7913edbff6d33d8d1?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Command Search Demo
{% endembed %}

## Command History

{% embed url="<https://www.loom.com/share/8119beca8d794b06859c5dea1b1377bb?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Command History Demo
{% endembed %}

## YAML Workflows

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e4870de99dab35a374dd44479208db26bf03e0b3%2Fyaml_workflows_demo.gif?alt=media" alt=""><figcaption><p>YAML Workflows Demo</p></figcaption></figure>


# Command Corrections

Command Corrections provides auto-correct suggestions on previously run commands to catch typos and forgotten flags, and fix general console errors.

## What is it

This feature was built on top of the open-source project [nvdn/thefuck](https://github.com/nvbn/thefuck). Here are some examples that the Warp team usually finds Command Corrections useful for:

* Misspelled commands
  * `gti checkout myBranchName` -> `git checkout myBranchName`
  * `cd ap/sorce/executtor` -> `cd app/source/executor`
* Missing flags
  * `git push` -> `git push –set-upstream myBranchName`
* Add permissions
  * `./script` -> `chmod +x ./script && ./script`

## How to access it

* Command Corrections is enabled by default. You can disable Command Corrections by going to `Settings > Features` > toggle “Suggest corrected commands”.
* After an incorrect command is run, a panel with the corrected command suggestion appears above the Input Editor. `CLICK` or press the `RIGHT` arrow to insert the suggestion.

## How it works

{% embed url="<https://www.loom.com/share/180e1dc8d1504ec39c00694d9fd71b7c?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Command Corrections Demo
{% endembed %}

#### Command Correction Rules:

| Command                                                       |
| ------------------------------------------------------------- |
| brew                                                          |
| cargo                                                         |
| cat                                                           |
| cd                                                            |
| chmod                                                         |
| conda                                                         |
| cp                                                            |
| docker                                                        |
| generic (command agnostic, e.g. mis-spelling executable name) |
| git                                                           |
| go                                                            |
| grep                                                          |
| java                                                          |
| ls                                                            |
| mkdir                                                         |
| npm                                                           |
| pip                                                           |
| python                                                        |
| sed                                                           |
| sudo                                                          |
| yarn                                                          |


# Command Search

The Command Search panel allows you to search across Command History, Workflows, Environment Variables, Notebooks, Prompts, and Agent Mode history simultaneously. Warp supports fuzzy search and tries

![Command Search Panel](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-0416002216ee3a4edba97329e81a7361cea64e2f%2FCleanShot%202024-05-15%20at%2015.31.06.png?alt=media)

{% hint style="info" %}
Tailor your Command Search experience by toggling off "Show Global Workflows" in `Settings > Features`. When disabled, your search will exclusively encompass YAML and Warp Drive Workflows.
{% endhint %}

## Quick Start

1. Press `CTRL-R` to open the Command Search Panel
2. Type your search query in the input box
3. Press `ENTER` to input the selected command into Warp's Input Editor

## Search Filters

You can filter your search results by prepending your search term with any of the following:

<table><thead><tr><th width="215.78436279296875">Filter</th><th>Shortcuts</th></tr></thead><tbody><tr><td>Command History</td><td><code>history:</code>, <code>h:</code>, or <code>H-TAB</code></td></tr><tr><td>Prompts</td><td><code>prompts:</code>, <code>p:</code>, or <code>P-TAB</code></td></tr><tr><td>Agent Mode History</td><td><code>ai_history:</code>, <code>a:</code>, or <code>A-TAB</code></td></tr><tr><td>Workflows</td><td><code>workflows:</code>, <code>w:</code>, or <code>W-TAB</code></td></tr><tr><td>Notebooks</td><td><code>notebooks:</code>, <code>n:</code>, or <code>N-TAB</code></td></tr><tr><td>Environment Variables</td><td><code>env_vars:</code>, <code>e:</code>, or <code>E-TAB</code></td></tr><tr><td>Generate</td><td><code>#:</code></td></tr></tbody></table>

{% hint style="info" %}
When a filter is activated, it will be bolded and italicized in the search panel.
{% endhint %}

## Additional Features

* You can expand the menu horizontally by dragging the right edge
* The panel supports fuzzy search and ranks results by relevance

## How it works

{% embed url="<https://www.loom.com/share/21a6f58a33754ee7913edbff6d33d8d1?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Command Search Demo
{% endembed %}


# Command History

Command History helps you quickly find previously run commands.

## What is it

While running, Warp isolates the history of each shell session e.g. if you have two Split Panes open, commands created in one pane do not populate the history of the other. Warp combines the history upon closing.

Command History also provides rich information like exit code, directory, thread, time to finish running, last run, etc.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-abf97bc8031534f9b5db2c988b486f5d69f10ba0%2Fcommand-history-rich.png?alt=media&#x26;token=f35f53a6-4b94-45c2-bc90-7ada463ccc41" alt=""><figcaption><p>Command History rich information</p></figcaption></figure>

## How to access it

* Hitting `UP` in the [Input Editor](https://github.com/warpdotdev/docs/blob/main/features/entry/editor/README.md) brings up your history and performs a prefix search based on input.
* Pressing `CTRL-R` opens the [Command Search](https://docs.warp.dev/documentation/terminal/entry/command-search) panel and initiates a search of your Command History. To navigate the Command Search panel:
  * Start typing and Warp will automatically filter using fuzzy search. Warp bolds matching text when filtering with fuzzy search.

## How it works

{% embed url="<https://www.loom.com/share/8119beca8d794b06859c5dea1b1377bb?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Command History Demo
{% endembed %}


# Synchronized Inputs

Synchronized Inputs allow you to sync your commands from one session to multiple similar panes as you’re typing, so you can easily run the same command in multiple sessions at the same time.

### Synchronized inputs vs. broadcast input

Synchronized inputs in Warp work similarly to “broadcast input” settings in other terminals, but there are some differences.

With Warp’s synchronized inputs, whatever command you enter in one session will sync to the other sessions in its entirety. Whereas, "broadcast input" typically allows you to "broadcast" individual keystrokes, which may be more suitable for editing parts of commands.

## How to access it

There are three ways to access controls to synchronize inputs:

* [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) in Warp: Search for “synchronize”
* Mac menus for the Warp app: `Edit > Synchronize Input`

## How to use it

{% tabs %}
{% tab title="macOS" %}
There are two modes available to scope how input is synchronized and one to stop any synchronization:

* Synchronize All Panes in All Tabs
* Synchronize All Panes in Current Tab `OPT-CMD-I`
* Stop Synchronizing Any Panes `OPT-CMD-I`
  {% endtab %}

{% tab title="Windows" %}
There are two modes available to scope how input is synchronized and one to stop any synchronization:

* Synchronize All Panes in All Tabs
* Synchronize All Panes in Current Tab `CTRL-ALT-I`
* Stop Synchronizing Any Panes `CTRL-ALT-I`
  {% endtab %}

{% tab title="Linux" %}
There are two modes available to scope how input is synchronized and one to stop any synchronization:

* Synchronize All Panes in All Tabs
* Synchronize All Panes in Current Tab `CTRL-ALT-I`
* Stop Synchronizing Any Panes `CTRL-ALT-I`
  {% endtab %}
  {% endtabs %}

When inputs are synchronized, you can start typing in one input editor and that same input will be entered into all of the input editors for all panes in your current tab or all tabs, depending on the scope you selected.

If you are working in an alternative editor mode (like vim), synchronized inputs will only apply to all tabs with that same editor type running.

When you get done, you can select “Stop Synchronizing Any Panes” to end the synchronization.

## How it works

<figure><img src="https://github.com/warpdotdev/gitbook/blob/main/docs/.gitbook/assets/Synchronized-Inputs.gif" alt="Demo showing synchronized inputs across panes and tabs"><figcaption><p>Synchronized Inputs Demo</p></figcaption></figure>


# YAML Workflows

Workflows are an easier way to execute and share commands within Warp.

{% hint style="danger" %}
You can continue to use YAML-based workflows, but we recommend using new [workflows in Warp Drive](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/workflows) instead for a better editing experience.
{% endhint %}

## What is it

Workflows are easily parameterized and searchable by name, description, or command arguments. [Common Workflows](https://github.com/warpdotdev/workflows) sourced by the Warp team and community are readily available within the app. Additionally, you can create and scope Workflows locally or to a git repository.

## How to use it

* Open the [Command Search](https://docs.warp.dev/documentation/terminal/entry/command-search) or Workflow Search `CTRL-SHIFT-R` panel to find Workflows.
* Once inside the menu, start typing in the search bar to filter the existing Workflows. (e.g. git, android, npm, etc.)
* When a Workflow is selected with `ENTER`, you can use `SHIFT-TAB` to cycle through the arguments.
* You can also expand the menu horizontally with the mouse by dragging it on the right edge.

{% hint style="info" %}
Tailor your [Command Search](https://docs.warp.dev/documentation/terminal/entry/command-search) experience by toggling off "Show Global Workflows" in `Settings > Features`. When disabled, your search will exclusively encompass YAML and Warp Drive Workflows.
{% endhint %}

## How it works

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-e4870de99dab35a374dd44479208db26bf03e0b3%2Fyaml_workflows_demo.gif?alt=media" alt="YAML Workflows Demo"><figcaption><p>YAML Workflows Demo</p></figcaption></figure>

### How is this Different from Aliases?

Workflows solve some major pain points with aliases, specifically the:

1. need to context switch
   1. leave vim, source dotfiles, or reset shell
2. difficulty with attaching documentation
3. inability to easily search or share
4. inability to easily parameterize

## Creating Custom Workflows

### How to create a workflow with YAML

You can store local workflows (scoped to your machine) in:

{% tabs %}
{% tab title="macOS" %}

```bash
$HOME/.warp/workflows/
```

{% endtab %}

{% tab title="Windows" %}

```powershell
$env:APPDATA\warp\Warp\data\workflows\
```

{% endtab %}

{% tab title="Linux" %}

```bash
${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/workflows/
```

{% endtab %}
{% endtabs %}

Or, you can share them with your team by saving them in `{{path_to_git_repo}}/.warp/workflows/`. Local and repository Workflows can be accessed under the "My Workflows" and "Repository Workflows" tab of the Workflows menu, respectively.

See the existing Workflow spec within the [Workflows repo](https://github.com/warpdotdev/Workflows/tree/main/specs) for examples. Additionally, we outline the file format below:

<details>

<summary><a href="https://github.com/warpdotdev/Workflows/blob/main/FORMAT.md">Workflow File Format</a></summary>

The Workflow file format is a [yaml](https://yaml.org/) file and must have either a \`.yml \` or \`yaml\` extension. If you're new to YAML and want to learn more, see [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/).

***

**`name`**

The name of the Workflow. Required.

**`command`**

The command that is executed when the Workflow is selected. Required.

**`tags`**

An array of tags that are useful to categorize the Workflow. Optional.

```yaml
tags: ["git", "GitHub"]
```

**`description`**

The description of the Workflow and what it does. Optional.

**`source_url`**

The URL from where the Workflow was originally generated from. This is surfaced in [commands.dev](https://www.commands.dev/) for attribution purposes. Optional.

**`author`**

The original author of the Workflow. For example, if this Workflow was generated from StackOverflow, the `author` would be the `author` of the StackOverflow post. This is surfaced in [commands.dev](https://www.commands.dev/) for attribution purposes. Optional.

**`author_url`**

The URL of original author of the Workflow. For example, if this Workflow was generated from StackOverflow, the `author_url` would be the StackOverflow author's profile page. This is surfaced in [commands.dev](https://www.commands.dev/) for attribution purposes. Optional.

**`shells`**

The list of shells where this Workflow is valid. If not specified, the Workflow is assumed to be valid in all shells. This must be one of `zsh`, `bash`, or `fish`.

**`arguments`**

A Workflow can have parameterized arguments to specify pieces of the Workflow that need to be filled in by the user.

You can specify which part of the Workflow command maps to an argument by surrounding it with two curly braces (`{{<argument>}}`).

For example the Workflow command:

```bash
for {{variable}} in {{sequence}}; do
  {{command}}
done
```

Includes 3 arguments: `variable`, `sequence`, and `command`.

**`arguments.name`**

The name of the argument. The argument name is used within the command to specify the ranges of the argument. Required.

```yaml
name: Example Workflow
command: echo {{string}}
arguments:
  - name: string
    description: The value to echo
```

**`arguments.description`**

The description of the argument. This is surfaced in both [commands.dev](https://www.commands.dev/) and Warp to help users fill in Workflow arguments. Optional

**`arguments.default_value`**

The default value for the argument. If specified, the `default_value` replaces the argument name within the command. Optional

***

</details>

### Where to save workflows

Local Workflows are scoped to your machine. Repository Workflows are scoped to a git repository and can be accessed by anyone who has cloned the repo. *Note:* Repository Workflows will not appear if you are ssh into a remote machine.

{% tabs %}
{% tab title="macOS" %}

```bash
# Local Workflow Path
$HOME/.warp/workflows/

# Repository Workflow Path
{{path_to_git_repo}}/.warp/workflows
```

{% endtab %}

{% tab title="Windows" %}

```powershell
# Local Workflow Path
$env:APPDATA\warp\Warp\data\workflows\

# Repository Workflow Path
{{path_to_git_repo}}\.warp\workflows
```

{% endtab %}

{% tab title="Linux" %}

```bash
# Local Workflow Path
${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/workflows/

# Repository Workflow Path
{{path_to_git_repo}}/.warp/workflows
```

{% endtab %}
{% endtabs %}

#### Local Workflows

To start, create a Workflow subdirectory within

{% tabs %}
{% tab title="macOS" %}

```bash
mkdir -p $HOME/.warp/workflows/
```

{% endtab %}

{% tab title="Windows" %}

```powershell
New-Item -Path "$env:APPDATA\warp\Warp\data\workflows\" -ItemType Directory
```

{% endtab %}

{% tab title="Linux" %}

```bash
mkdir -p ${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/workflows/
```

{% endtab %}
{% endtabs %}

Add your Workflow’s `.yaml` file to this directory; if the file format is valid Warp should automatically load it into the Workflows menu.

`cp ~/path/to/my_awesome_workflow.yaml {{path_to_local_workflow_folder}}`

#### Repository Workflows

You can add a repository Workflow similarly to how you added a local Workflow. Create a Workflows folder in a repository’s root directory and save your `.yaml` file like so:

```
cd {{repository_path}}
mkdir -p .warp/workflows/
cp ~/path/to/my_awesome_workflow.yaml {{path_to_local_workflow_folder}}
```

#### Global Workflows

You can contribute Workflows that will be made available to other Warp users by forking the [Workflows repo](https://github.com/warpdotdev/workflows/tree/main/specs) and opening a pull request. See the [Contributing](https://github.com/warpdotdev/workflows#contributing) section for more details.


# Command Completions

Warp's main features for command completions and autosuggestions.

1. [Completions](https://docs.warp.dev/documentation/terminal/command-completions/completions) will suggest commands, option names, and path parameters for you.
2. [Autosuggestions](https://docs.warp.dev/documentation/terminal/command-completions/autosuggestions) will automatically suggest commands as you type based on shell history and possible completions.

## Completions

{% embed url="<https://www.loom.com/share/92594c821ae341f69d5d1c1af56f2c69?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Completions Demo
{% endembed %}

## Autosuggestions

{% embed url="<https://www.loom.com/share/5e87c52ae855486ab88ffb2f89aeaf73?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Autosuggestion Demo
{% endembed %}


# Completions

Warp Tab Completions will suggest commands, option names, and path parameters for you. This feature works regardless of machine or directory (including SSH sessions).

## What is it

Completions feature fuzzy search capability that provides you with [approximate matches](https://en.wikipedia.org/wiki/Approximate_string_matching) for your queries. If you're unsure about the exact syntax or spelling, you'll be provided with suggestions based on your input, even if it's not an exact match.

## How to access it

* Type out the beginning of your command, then press `TAB`.
* To search for options and flags, you must type and press `TAB`.
* Forgo `TAB` by enabling "Open completions menu as you type" in `Settings > Features`

## How to use it

### Completions

1. Type `git checkout` (note the space) and then press `TAB`
2. A menu will show all of your local branches. You can select one using your mouse or the `UP ↑`/`DOWN ↓` arrow keys

### Completions on Aliases

* Shell aliases - This is an alias for an entire command. For example, if you have `gc=git checkout` in alias, typing `gc` and hitting `TAB` should give you the same completion options as for `git checkout` .
* Command aliases - This is an alias for a subcommand. For example, this could be setting `git status` to `git st`. With completions support, we could now suggest completions for `git status` even if you typed in `git st`.

{% hint style="info" %}
**Terminal Tip**\
The "Tab key behavior" setting under `Features > Editor` can change the action that `Tab` is bound to. If `Tab` is not bound to open the completions menu, `ctrl-space` will be assigned as the default keybinding. *Note: You can also enable the "Open completions menu as you type" in `Settings > Features` so that the completions menu opens automatically.*
{% endhint %}

## How it works

{% embed url="<https://www.loom.com/share/92594c821ae341f69d5d1c1af56f2c69?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Completions Demo
{% endembed %}

### Supported Completion Specs

| Command Name            | Level of Support |
| ----------------------- | ---------------- |
| act                     | Partial          |
| adb                     | Partial          |
| afplay                  | Partial          |
| aftman                  | Partial          |
| ag                      | Partial          |
| agrippa                 | Partial          |
| amplify                 | Partial          |
| ansible                 | Partial          |
| ansible-config          | Partial          |
| ansible-doc             | Partial          |
| ansible-galaxy          | Partial          |
| ansible-lint            | Partial          |
| ansible-playbook        | Partial          |
| appwrite                | Partial          |
| arch                    | Partial          |
| asdf                    | Partial          |
| assimp                  | Partial          |
| atlas                   | Partial          |
| autojump                | Partial          |
| aws                     | Partial          |
| babel                   | Partial          |
| banner                  | Partial          |
| base32                  | Partial          |
| base64                  | Partial          |
| basename                | Partial          |
| basenc                  | Partial          |
| bat                     | Partial          |
| bazel                   | Partial          |
| bc                      | Partial          |
| black                   | Partial          |
| blitz                   | Partial          |
| bosh                    | Full             |
| brew                    | Full             |
| build-storybook         | Partial          |
| bun                     | Partial          |
| bundle                  | Partial          |
| bw                      | Partial          |
| caffeinate              | Partial          |
| cargo                   | Full             |
| cat                     | Partial          |
| cd                      | Partial          |
| cdk                     | Partial          |
| checkov                 | Partial          |
| chmod                   | Partial          |
| chown                   | Partial          |
| circleci                | Partial          |
| clang                   | Partial          |
| clear                   | Partial          |
| clojure                 | Partial          |
| cloudflared             | Partial          |
| cmake                   | Partial          |
| code                    | Partial          |
| code-insiders           | Partial          |
| command                 | Partial          |
| composer                | Partial          |
| conda                   | Full             |
| copilot                 | Partial          |
| cordova                 | Partial          |
| cosign                  | Partial          |
| cot                     | Partial          |
| cp                      | Partial          |
| create-completion-spec  | Partial          |
| create-next-app         | Partial          |
| create-nx-workspace     | Partial          |
| create-react-app        | Partial          |
| create-react-native-app | Partial          |
| create-remix            | Partial          |
| create-t3-app           | Partial          |
| create-video            | Partial          |
| create-web3-frontend    | Partial          |
| croc                    | Partial          |
| curl                    | Partial          |
| cut                     | Partial          |
| dart                    | Partial          |
| date                    | Partial          |
| dateseq                 | Partial          |
| datree                  | Partial          |
| dbt                     | Partial          |
| dd                      | Partial          |
| defaults                | Full             |
| degit                   | Partial          |
| deno                    | Partial          |
| deployctl               | Partial          |
| deta                    | Partial          |
| df                      | Partial          |
| diff                    | Partial          |
| dig                     | Partial          |
| direnv                  | Partial          |
| dirname                 | Partial          |
| django-admin            | Partial          |
| do                      | Partial          |
| docker                  | Full             |
| docker-compose          | Partial          |
| doctl                   | Partial          |
| dog                     | Partial          |
| doppler                 | Partial          |
| dotenv                  | Partial          |
| dotnet                  | Partial          |
| dotslash                | Partial          |
| drush                   | Partial          |
| dtm                     | Partial          |
| du                      | Partial          |
| eb                      | Partial          |
| echo                    | Partial          |
| electron                | Partial          |
| eleventy                | Partial          |
| elif                    | Partial          |
| elixir                  | Partial          |
| elm                     | Partial          |
| elm-review              | Partial          |
| else                    | Partial          |
| emacs                   | Partial          |
| esbuild                 | Partial          |
| eslint                  | Partial          |
| exa                     | Partial          |
| exec                    | Partial          |
| exercism                | Partial          |
| expo                    | Partial          |
| expo-cli                | Partial          |
| export                  | Partial          |
| fastlane                | Partial          |
| fastly                  | Partial          |
| fd                      | Partial          |
| ffmpeg                  | Partial          |
| fig-teams               | Partial          |
| file                    | Partial          |
| find                    | Partial          |
| firebase                | Full             |
| fisher                  | Partial          |
| flutter                 | Full             |
| fly                     | Partial          |
| flyctl                  | Partial          |
| fmt                     | Partial          |
| fnm                     | Partial          |
| fold                    | Partial          |
| for                     | Partial          |
| forge                   | Partial          |
| fvm                     | Partial          |
| fzf                     | Partial          |
| fzf-tmux                | Partial          |
| ganache-cli             | Partial          |
| gatsby                  | Partial          |
| gcc                     | Partial          |
| gcloud                  | Partial          |
| gh                      | Full             |
| git                     | Full             |
| git-flow                | Partial          |
| github                  | Partial          |
| gltfjsx                 | Partial          |
| go                      | Full             |
| goctl                   | Partial          |
| googler                 | Partial          |
| goreleaser              | Partial          |
| gpg                     | Partial          |
| gradle                  | Partial          |
| graphcdn                | Partial          |
| grep                    | Partial          |
| grex                    | Partial          |
| hardhat                 | Partial          |
| hasura                  | Partial          |
| hb-service              | Partial          |
| head                    | Partial          |
| helm                    | Partial          |
| heroku                  | Full             |
| hexo                    | Partial          |
| hostname                | Partial          |
| htop                    | Partial          |
| http                    | Partial          |
| https                   | Partial          |
| httpy                   | Partial          |
| hub                     | Partial          |
| hugo                    | Partial          |
| hx                      | Partial          |
| hyper                   | Partial          |
| id                      | Partial          |
| iex                     | Partial          |
| if                      | Partial          |
| ignite-cli              | Partial          |
| install                 | Partial          |
| ionic                   | Partial          |
| j                       | Partial          |
| java                    | Partial          |
| jest                    | Partial          |
| join                    | Partial          |
| jq                      | Partial          |
| julia                   | Partial          |
| jupyter                 | Partial          |
| just                    | Partial          |
| keytool                 | Partial          |
| kill                    | Partial          |
| killall                 | Full             |
| kitty                   | Partial          |
| knex                    | Partial          |
| kool                    | Partial          |
| kubecolor               | Partial          |
| kubectl                 | Full             |
| kubectx                 | Full             |
| kubens                  | Full             |
| laravel                 | Partial          |
| lerna                   | Partial          |
| less                    | Partial          |
| lima                    | Partial          |
| limactl                 | Partial          |
| ln                      | Partial          |
| lp                      | Partial          |
| lpass                   | Partial          |
| ls                      | Partial          |
| lsd                     | Partial          |
| mackup                  | Partial          |
| make                    | Full             |
| man                     | Full             |
| mas                     | Partial          |
| mask                    | Partial          |
| mdfind                  | Partial          |
| meteor                  | Partial          |
| micro                   | Partial          |
| mikro-orm               | Partial          |
| minikube                | Partial          |
| mix                     | Partial          |
| mkdir                   | Partial          |
| mkfifo                  | Partial          |
| mknod                   | Partial          |
| mob                     | Partial          |
| molecule                | Partial          |
| mongocli                | Partial          |
| mongosh                 | Partial          |
| more                    | Partial          |
| mosh                    | Partial          |
| mv                      | Partial          |
| mvn                     | Partial          |
| mysql                   | Partial          |
| n                       | Partial          |
| nano                    | Partial          |
| nativescript            | Partial          |
| nc                      | Partial          |
| nest                    | Partial          |
| netlify                 | Partial          |
| networkQuality          | Partial          |
| newman                  | Partial          |
| next                    | Partial          |
| ng                      | Full             |
| nginx                   | Partial          |
| ngrok                   | Partial          |
| nhost                   | Partial          |
| ni                      | Partial          |
| nl                      | Partial          |
| nocorrect               | Partial          |
| node                    | Full             |
| noglob                  | Partial          |
| npm                     | Full             |
| npx                     | Partial          |
| nr                      | Partial          |
| nrm                     | Partial          |
| ns                      | Partial          |
| nu                      | Partial          |
| nuxi                    | Partial          |
| nuxt                    | Partial          |
| nvim                    | Partial          |
| nvm                     | Partial          |
| nx                      | Full             |
| nylas                   | Partial          |
| od                      | Partial          |
| oh-my-posh              | Partial          |
| okta                    | Partial          |
| okteto                  | Partial          |
| omz                     | Partial          |
| onboardbase             | Partial          |
| op                      | Partial          |
| opa                     | Partial          |
| open                    | Partial          |
| osascript               | Partial          |
| pageres                 | Partial          |
| pandoc                  | Partial          |
| pass                    | Partial          |
| paste                   | Partial          |
| pathchk                 | Partial          |
| pdfunite                | Partial          |
| pgcli                   | Partial          |
| php                     | Partial          |
| phpunit-watcher         | Full             |
| ping                    | Partial          |
| pip                     | Full             |
| pip3                    | Partial          |
| pipenv                  | Partial          |
| pm2                     | Partial          |
| pmset                   | Partial          |
| pnpm                    | Partial          |
| pnpx                    | Partial          |
| pod                     | Partial          |
| poetry                  | Partial          |
| pre-commit              | Partial          |
| preset                  | Partial          |
| prettier                | Partial          |
| prisma                  | Partial          |
| projj                   | Partial          |
| ps                      | Partial          |
| pscale                  | Partial          |
| psql                    | Partial          |
| publish                 | Partial          |
| pulumi                  | Partial          |
| pushd                   | Partial          |
| pwd                     | Partial          |
| pyenv                   | Full             |
| python                  | Partial          |
| python3                 | Partial          |
| qodana                  | Partial          |
| quickmail               | Partial          |
| r                       | Partial          |
| rails                   | Partial          |
| railway                 | Partial          |
| rake                    | Partial          |
| rancher                 | Partial          |
| rbenv                   | Partial          |
| rclone                  | Partial          |
| react-native            | Full             |
| readlink                | Partial          |
| redwood                 | Partial          |
| remix                   | Partial          |
| remotion                | Partial          |
| repeat                  | Partial          |
| rg                      | Partial          |
| rm                      | Partial          |
| rmdir                   | Partial          |
| robot                   | Partial          |
| rollup                  | Partial          |
| rscript                 | Partial          |
| rsync                   | Partial          |
| ruby                    | Partial          |
| rush                    | Partial          |
| rushx                   | Partial          |
| rustc                   | Partial          |
| rustup                  | Partial          |
| sam                     | Partial          |
| scc                     | Partial          |
| scp                     | Partial          |
| screen                  | Partial          |
| sed                     | Partial          |
| sequelize               | Partial          |
| serve                   | Partial          |
| serverless              | Partial          |
| sfdx                    | Partial          |
| sftp                    | Partial          |
| shopify                 | Partial          |
| shortcuts               | Partial          |
| shred                   | Partial          |
| sips                    | Partial          |
| softwareupdate          | Partial          |
| source                  | Partial          |
| splash                  | Partial          |
| split                   | Partial          |
| spotify                 | Partial          |
| sqlite3                 | Partial          |
| src                     | Partial          |
| ssh                     | Full             |
| st2                     | Partial          |
| start-storybook         | Partial          |
| stat                    | Partial          |
| steadybit               | Partial          |
| stepzen                 | Partial          |
| stripe                  | Partial          |
| su                      | Partial          |
| subl                    | Partial          |
| sudo                    | Partial          |
| swc                     | Partial          |
| swift                   | Partial          |
| sysctl                  | Partial          |
| tac                     | Partial          |
| tail                    | Partial          |
| tailscale               | Partial          |
| tailwindcss             | Partial          |
| tangram                 | Partial          |
| tar                     | Full             |
| task                    | Partial          |
| tccutil                 | Partial          |
| tee                     | Partial          |
| terraform               | Full             |
| terragrunt              | Partial          |
| tfenv                   | Partial          |
| tfsec                   | Partial          |
| then                    | Partial          |
| time                    | Partial          |
| tldr                    | Partial          |
| tmux                    | Full             |
| tmuxinator              | Full             |
| tns                     | Partial          |
| tokei                   | Partial          |
| top                     | Partial          |
| touch                   | Partial          |
| tr                      | Partial          |
| traceroute              | Partial          |
| trash                   | Partial          |
| trex                    | Partial          |
| trivy                   | Partial          |
| truffle                 | Partial          |
| truncate                | Partial          |
| trunk                   | Partial          |
| ts-node                 | Partial          |
| tsc                     | Partial          |
| tsh                     | Partial          |
| turbo                   | Partial          |
| twiggy                  | Partial          |
| twilio                  | Partial          |
| typeorm                 | Partial          |
| uname                   | Partial          |
| uniq                    | Partial          |
| until                   | Partial          |
| until                   | Partial          |
| unzip                   | Partial          |
| vale                    | Partial          |
| valet                   | Partial          |
| vapor                   | Partial          |
| vault                   | Partial          |
| vela                    | Partial          |
| vercel                  | Partial          |
| vi                      | Partial          |
| vim                     | Partial          |
| vimr                    | Partial          |
| vite                    | Partial          |
| vite                    | Partial          |
| volta                   | Partial          |
| vr                      | Partial          |
| vsce                    | Partial          |
| vtex                    | Partial          |
| vue                     | Partial          |
| vue                     | Partial          |
| vultr-cli               | Partial          |
| w                       | Partial          |
| w                       | Partial          |
| wasm-bindgen            | Partial          |
| wasm-pack               | Partial          |
| watson                  | Partial          |
| wc                      | Partial          |
| wc                      | Partial          |
| wd                      | Partial          |
| webpack                 | Partial          |
| wget                    | Partial          |
| whence                  | Partial          |
| where                   | Partial          |
| which                   | Partial          |
| while                   | Partial          |
| who                     | Partial          |
| whois                   | Partial          |
| wifi-password           | Partial          |
| wifi-password           | Partial          |
| wp                      | Partial          |
| wrangler                | Partial          |
| wrk                     | Partial          |
| wscat                   | Partial          |
| xargs                   | Partial          |
| xcode-select            | Partial          |
| xcodebuild              | Partial          |
| xcodeproj               | Partial          |
| xcrun                   | Partial          |
| xed                     | Partial          |
| yank                    | Partial          |
| yarn                    | Partial          |
| yo                      | Partial          |
| youtube-dl              | Partial          |
| z                       | Partial          |
| z                       | Partial          |
| zapier                  | Partial          |
| zapier                  | Partial          |
| zip                     | Partial          |
| zoxide                  | Partial          |


# Autosuggestions

Warp will automatically suggest commands as you type based on shell history and possible completions.

## How to access it

* From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), type in "Autosuggestions" to toggle.

{% hint style="info" %}
**Terminal Tip**

You can change the keybinding for accepting autosuggestions to `Tab`. Configure this in the "Tab key behavior" setting under Features > Editor. *Note: This will update the keybinding for opening the completions menu to `CTRL-SPACE`. You can also enable the "Open completions menu as you type" in Settings > Features so that the completions menu opens automatically.*
{% endhint %}

## How to use it

{% tabs %}
{% tab title="macOS" %}
There are several ways to accept autosuggestions, either completely or partially:

* Complete an autosuggestion using the `RIGHT` arrow or `CTRL-F`.
* `CTRL-E` also, completes the autosuggestion when your cursor is at the end of the buffer.
* `CTRL-RIGHT` can be used to partially complete the autosuggestion one component at a time.
  {% endtab %}

{% tab title="Windows" %}
There are several ways to accept autosuggestions, either completely or partially:

* Complete an autosuggestion using the `RIGHT` arrow or `CTRL-F`.
* `END` jumps to the last character in the Input Editor, then `RIGHT` completes the autosuggestion.
* `CTRL-SHIFT-RIGHT` can be used to partially complete the autosuggestion one component at a time.
  {% endtab %}

{% tab title="Linux" %}
There are several ways to accept autosuggestions, either completely or partially:

* Complete an autosuggestion using the `RIGHT` arrow or `CTRL-F`.
* `CTRL-E` jumps to the last character in the Input Editor, then `RIGHT` completes the autosuggestion.
* `CTRL-SHIFT-RIGHT` can be used to partially complete the autosuggestion one component at a time.
  {% endtab %}
  {% endtabs %}

## How it works

{% embed url="<https://www.loom.com/share/5e87c52ae855486ab88ffb2f89aeaf73?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Autosuggestion Demo
{% endembed %}


# Command Palette

Command Palette is a global search to quickly locate Workflows, Notebooks,  keyboard shortcuts, or other actions within Warp.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4c11592c5193014fb17df1dbdbd8670a118234f3%2FCleanShot%202024-05-15%20at%2015.36.39.png?alt=media" alt=""><figcaption><p>Command Palette Panel</p></figcaption></figure>

## How to access it

{% tabs %}
{% tab title="macOS" %}
You can access the Command Palette with the keyboard shortcut `CMD-P`.
{% endtab %}

{% tab title="Windows" %}
You can access the Command Palette with the keyboard shortcut `CTRL-SHIFT-P`.
{% endtab %}

{% tab title="Linux" %}
You can access the Command Palette with the keyboard shortcut `CTRL-SHIFT-P`.
{% endtab %}
{% endtabs %}

## How it works

* Start typing to search for workflows, notebooks, keyboard shortcuts, actions, toggles, etc.
* Activate a specific filter, by clicking on the filter buttons or prepending your search with the following:
  * `workflows:` or `w:` will filter for [Workflows](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/workflows).
  * `prompts:` or `p:` will filter for [Prompts](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/prompts).
  * `notebook:` or `n:` will filter for [Notebooks](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/notebooks).
  * `env_vars:` will filter for [Environment Variables](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/environment-variables).
  * `files:` will filter for local files.
  * `drive:` will filter for [Warp Drive](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive).
  * `actions:` will filter for Warp-specific actions like settings and features.
  * `sessions:` will filter for active sessions with [Session Navigation](https://docs.warp.dev/documentation/terminal/sessions/session-navigation).
  * `launch_configs:` will filter for [Launch Configurations](https://docs.warp.dev/documentation/terminal/sessions/launch-configurations).

{% embed url="<https://www.loom.com/share/0e6108b295234637a0bb20cc941976e9?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Command Palette Demo
{% endembed %}


# Session Management

Warp feature to manages sessions in multiple ways.

1. [Launch Configurations](https://docs.warp.dev/documentation/terminal/sessions/launch-configurations) supports saving a configuration of windows, tabs, and panes to open later.
2. [Session Navigation](https://docs.warp.dev/documentation/terminal/sessions/session-navigation) enables you to easily navigate to any session in Warp.
3. [Session Restoration](https://docs.warp.dev/documentation/terminal/sessions/session-restoration) automatically restores the window and tabs from your previous session.

## Launch Configuration

{% embed url="<https://www.loom.com/share/daa2a9e55c27458c8bbf722d90078880?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Launch Configuration Demo
{% endembed %}

## Session Navigation

{% embed url="<https://www.loom.com/share/2147adc6749c4f4ea5da432eadda7995>" %}
Session Navigation Demo
{% endembed %}

## Session Restoration

![Session Restoration Demo](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-eea5d549c432c9c124c175120bc2b901b1add9fb%2Fsessions-block_restoration.gif?alt=media\&token=56d16d7b-d27f-4d3d-b0af-a5ff017b5ead)


# Launch Configurations

Launch Configurations enables you to save your configuration of windows, tabs, and panes, so that you can reopen the same set of sessions per project quickly.

## What is it

With Launch configurations you can save in the app or by adding a yaml file.

## Creating a Launch Configuration

### From the UI

1. Set up the configuration of windows, tabs, and panes you would like to save.
2. Open the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), and type in `Save New Launch Configuration`.
3. Name the configuration file. The name field cannot be empty.
4. Click the Save configuration button.

### With a YAML File

* Launch Configurations files are generated when you create them with the UI and can also be created or modified manually.
* Please see the below for [Launch Configuration YAML file locations, format, and examples](#launch-configuration-yaml-format).

## Using a Launch Configuration

{% tabs %}
{% tab title="macOS" %}

* From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), enter `Launch Configuration` to open and select Launch Configuration.
* Right-clicking the new Tab **+** button to open a menu and select saved Launch Configuration.
* From the Mac Menu, `File > Launch Configurations`, where you can search through and open your saved Launch Configuration.
  * Single-window launch configs can be launched into the active window from the launch configuration palette using `CMD-ENTER` on Mac.
    {% endtab %}

{% tab title="Windows" %}

* From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), enter `Launch Configuration` to open and select Launch Configuration.
* Right-clicking the new Tab **+** button to open a menu and select saved Launch Configuration.
  * Single-window launch configs can be launched into the active window from the launch configuration palette using `CTRL-ENTER` on Linux.

To open a WSL tab with a Launch Configuration, you must first set WSL as your default shell in Warp:

* Go to `Settings > Features > Session > Startup shell for new sessions`.
* Select your desired WSL distribution (e.g., Ubuntu) as the default shell.

After this, any Launch Configuration you open will use WSL as the shell.
{% endtab %}

{% tab title="Linux" %}

* From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), enter `Launch Configuration` to open and select Launch Configuration.
* Right-clicking the new Tab **+** button to open a menu and select saved Launch Configuration.
  * Single-window launch configs can be launched into the active window from the launch configuration palette using `CTRL-ENTER` on Linux.
    {% endtab %}
    {% endtabs %}

{% hint style="success" %}
**Terminal Tip**\
You can open saved Launch Configurations via Alfred Workflow or [Raycast](https://docs.warp.dev/documentation/integrations/integrations-and-plugins#raycast) Extension. Learn more [here](https://blog.joe.codes/open-warp-launch-configurations-from-raycast-and-alfred). Credit to [@joetannenbaum](https://twitter.com/joetannenbaum/status/1633538768866009115)
{% endhint %}

## How it works

{% embed url="<https://www.loom.com/share/daa2a9e55c27458c8bbf722d90078880?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Launch Configuration Demo
{% endembed %}

## Launch Configuration YAML Format

All Launch Configuration yaml files are stored in the following location:

{% tabs %}
{% tab title="macOS" %}

```bash
$HOME/.warp/launch_configurations/
```

{% endtab %}

{% tab title="Windows" %}

```powershell
$env:APPDATA\warp\Warp\data\launch_configurations\
```

{% endtab %}

{% tab title="Linux" %}

```bash
${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/launch_configurations/
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
The `cwd:` value in the yaml code must contain an absolute path or `""`. Note that `~` or empty paths will result in the file not being visible on the list of options for Launch Configurations.
{% endhint %}

### Windows

Sample configuration that shows how windows are structured in launch configuration files.

```yaml
# Warp Launch Configuration
#
# This configuration has two windows, 
# each with one tab in different starting directories.

---
name: Example Windows
windows:
  - tabs:
      - title: Documents
        layout:
          cwd: /Users/warp-user/Documents
        color: blue
  - tabs:
      - title: Warp User
        layout:
          cwd: /Users/warp-user
        color: green
```

### Tabs

Here's a sample configuration that shows how tabs are structured in launch configuration files.

* Use the `title` field to set a custom tab name
* Use the `color` field to set the tab color
  * We currently support using the terminal colors (ANSI colors):

    `Red | Green | Yellow | Blue | Magenta | Cyan`

    The actual color values will be automatically derived from your Warp theme

```yaml
# Warp Launch Configuration
#
# This configuration has two tabs in the same window.

---
name: Example Tabs
windows:
  - tabs:
      - title: Documents 
        layout:
          cwd: /Users/warp-user/Documents
        color: blue
      - title: Warp User
        layout:
          cwd: /Users/warp-user
        color: green
```

### Panes

Launch Configurations support setting split panes in each tab. Note that Warp also supports nesting split panes in launch configuration files.

```yaml
# Warp Launch Configuration
#
# This configuration is two windows, each with split panes. 
# The first window contains a vertically split tab with two panes.
# The second window contains a horizontally split tab, 
# with a vertically split tab on the right.

---
name: Example Panes
windows:
  - tabs:
      - title: Downloads and Warp User
        layout:
          split_direction: vertical
          panes:
            - cwd: /Users/warp-user/Downloads
            - cwd: /Users/warp-user
        color: blue
  - tabs:
      - title: Desktop, Documents, and Warp User
        layout:
          split_direction: horizontal
          panes:
            - cwd: /Users/warp-user/Desktop
            - split_direction: vertical
              panes:
                - cwd: /Users/warp-user/Documents
                - cwd: /Users/warp-user
        color: green
```

### Active and Focus

Sample configuration that shows how a Window and Tab can be activated with a session in focus.

* Use the `active_window_index` and `active_tab_index`fields to set your active Window and Tab.
* Use the `is_focused` field to set which Pane is focused in each tab.

{% hint style="warning" %}
Not that when you use `- active_tab_index:` the `tabs:` field doesn't need the `-` prefix, as this can cause syntax issues.
{% endhint %}

```yaml
# Warp Launch Configuration
#
# This configurations has two tabs, with the second tab active.
# Two vertical split panes in the first tab and the top pane focused.
# Two horizontal split panes in the second tab and the right pane focused.
---
name: Example Active and Focus
active_window_index: 0
windows:
  - active_tab_index: 1
    tabs:
      - title: Tab 1
        layout:
          split_direction: vertical
          panes:
            - cwd: /Users/warp-user/Documents
              is_focused: true
            - cwd: /Users/warp-user/Documents/Projects
      - title: Tab 2
        layout:
          split_direction: horizontal
          panes:
            - cwd: /Users/warp-user/Downloads
            - cwd: /Users/warp-user
              is_focused: true
```

### Commands

Use the `commands` field to define a set of commands to run when a launch configuration in run.

{% hint style="warning" %}
You may need to use double quotes for commands with special characters. Commands in separate lines are chained together with `&&` when run, as such commands run after `ssh` commands may not execute.
{% endhint %}

```yaml
# Warp Launch Configuration
#
# This configuration has two windows,
# the first window executes two commands on start,
# the second window has a split pane that executes a command on start.

---
name: Example Commands
windows:
  - tabs:
      - title: Documents
        layout:
          cwd: /Users/warp-user/Documents
          commands:
            - exec: ls
            - exec: code .
        color: blue
  - tabs:
      - title: Downloads
        layout:
          split_direction: vertical
          panes:
            - cwd: /Users/warp-user/Downloads
              commands:
                - exec: curl http://example.com -o my.file
                - exec: cp my.file my.file2
            - cwd: /Users/warp-user
              commands:
                - exec: ssh user@remote.server.com
        color: green
```


# Session Navigation

The Session Navigation Palette helps you speed up your workflow by allowing you to quickly navigate using the keyboard or mouse to the terminal sessions you are looking for across Warp.

## How to access Session navigation

1. Open the Session Navigation palette with the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), click on **session >\_** or type in "sessions:".
2. Jump to a session by using your mouse or the `UP ↑`/`DOWN ↓` arrow keys and `ENTER`.
3. Refine the session results by searching for sessions by prompt, the currently running command, last run command, and command status (ex: “Running…”, “Completed 10 minutes ago”, “Empty Session”).

{% hint style="info" %}
Sessions are ordered by recency, so the most recently focused sessions show up first. The Session Navigation palette does not have **PS1** support and can only show Warp's native prompt.
{% endhint %}

### CTRL-TAB Behaviour

`CTRL-TAB` shortcut defaults to activate the previous / next [Tabs](https://docs.warp.dev/documentation/terminal/windows/tabs). You can configure the shortcut to cycle the most recent session, including any [Split Panes](https://docs.warp.dev/documentation/terminal/windows/split-panes), in `Settings > Features > Keys > Ctrl-Tab behavior`

## How Session Navigation Works

{% embed url="<https://www.loom.com/share/2147adc6749c4f4ea5da432eadda7995>" %}
Session Navigation Demo
{% endembed %}


# Session Restoration

The Session Restoration feature enables Warp to restore your session history, specifically windows, tabs, and panes, along with the last few Blocks in each pane.

## What is it

Session restoration allows you to quickly pick up where you left off in your previous terminal session.

## How to access Session Restoration

* Session Restoration comes enabled by default in Warp.

{% hint style="info" %}
On Linux, opening windows at a specific position is not supported in Wayland.
{% endhint %}

* You can disable Session Restoration by going to `Settings > Features`, then toggling off `Restore windows, tabs, and panes on startup`.

{% hint style="warning" %}
Toggling off Session Restoration will not clear the [SQLite database](#session-restoration-database); however, Warp will stop recording new output.
{% endhint %}

## How Session Restoration works

![Session Restoration Demo](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-eea5d549c432c9c124c175120bc2b901b1add9fb%2Fsessions-block_restoration.gif?alt=media\&token=56d16d7b-d27f-4d3d-b0af-a5ff017b5ead)

#### Session Restoration database

Warp saves the data from your previous session's windows, tabs, and panes to a SQLite database on your computer, and every time you quit the app, this data is overwritten by your latest session. You can open the database directly and inspect its full contents like so:

{% tabs %}
{% tab title="macOS" %}

```bash
sqlite3 "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite"
```

{% endtab %}

{% tab title="Windows" %}

```powershell
sqlite3 $env:LOCALAPPDATA\warp\Warp\data\warp.sqlite
```

{% endtab %}

{% tab title="Linux" %}

```bash
sqlite3 "${XDG_STATE_HOME:-$HOME/.local/state}/warp-terminal/warp.sqlite"
```

{% endtab %}
{% endtabs %}

**How to clear the Session Restoration database**

Sometimes, you may want to prevent a sensitive Block from being saved on your computer, or you may want to clear blocks from a machine entirely.

{% hint style="info" %}
This interferes with the running session's ability to save content and may require you close Warp before running the database removal commands.
{% endhint %}

{% hint style="danger" %}
The following guidance is destructive and will delete any sessions and block history.
{% endhint %}

There are two ways to do this:

{% tabs %}
{% tab title="macOS" %}

* Clear the blocks from your running Warp session with `CMD-K`.
* Delete the SQLite file entirely with the following command:

```bash
rm -f "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite"
```

{% endtab %}

{% tab title="Windows" %}

* Clear the blocks from your running Warp session with `CTRL-SHIFT-K`.
* Delete the SQLite file entirely with the following command:

```powershell
Remove-Item -Force $env:LOCALAPPDATA\warp\Warp\data\warp.sqlite
```

{% endtab %}

{% tab title="Linux" %}

* Clear the blocks from your running Warp session with `CTRL-SHIFT-K`.
* Delete the SQLite file entirely with the following command:

```bash
rm -f "${XDG_STATE_HOME:-$HOME/.local/state}/warp-terminal/warp.sqlite"
```

{% endtab %}
{% endtabs %}


# Window Management

Warp's features for Window Management.

1. [Global Hotkey](https://docs.warp.dev/documentation/terminal/windows/global-hotkey) is a configurable shortcut that can show/hide a dedicated window or all windows on your chosen desktop regardless of whether the app is focused.
2. [Tabs](https://docs.warp.dev/documentation/terminal/windows/tabs) allow you to organize a window into multiple terminal sessions.
3. [Split Panes](https://docs.warp.dev/documentation/terminal/windows/split-panes) allows you to divide a Tab into multiple rectangular *panes*, each of which is a unique terminal session.

## Global Hotkey

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-048acf9fd85b0fa2129bb90a1b3d8a2d1f911f5b%2FDedicated%20Window.gif?alt=media&#x26;token=39195b3a-16c6-44e5-b2e2-f4bb84677c30" alt=""><figcaption><p>Global Hotkey - Dedicated Window Demo</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-af6164e0085e8fa8f3d2ff3602178e4c9343332c%2FShow-Hide%20All%20Windows.gif?alt=media&#x26;token=e292ad67-f087-4b0b-a779-f5266be40a45" alt=""><figcaption><p>Global Hotkey - Show/Hide All Windows Demo</p></figcaption></figure>

## Tabs

{% embed url="<https://www.loom.com/share/84d15cc7eb5a4a668bb86be9e827f261?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Tabs Demo
{% endembed %}

## Split Panes

{% embed url="<https://www.loom.com/share/c1104b51cab848a9bef6792ec4fd8421?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Split Panes Demo
{% endembed %}


# Global Hotkey

Warp's Global Hotkey is a configurable shortcut that can show/hide a dedicated Warp window or all Warp windows on your chosen desktop regardless of whether the app is focused.

{% hint style="info" %}
On macOS, [system keyboard shortcuts](https://support.apple.com/en-us/HT201236) like `CMD-ESC`, `CMD-BACKTICK`, `CMD-TAB`, `CMD-PERIOD`, and `CMD-TILDE` need to be [unbound](https://support.apple.com/guide/mac-help/keyboard-shortcuts-mchlp2262/mac) before you can use them in Warp.
{% endhint %}

{% hint style="warning" %}
On Linux, the Global Hotkey may not work for some X11 window managers that do not implement [Extended Window Manager Hints](https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints). Some examples include: [sowm](https://github.com/dylanaraps/sowm), [catwm](https://github.com/pyknite/catwm), [Fvwm](https://www.fvwm.org/), [dwm](https://dwm.suckless.org/), [2bWM](https://github.com/venam/2bwm), [monsterwm](https://github.com/c00kiemon5ter/monsterwm), [TinyWM](https://github.com/mackstann/tinywm), [x11fs](https://github.com/sdhand/x11fs), [XMonad](https://xmonad.org/)
{% endhint %}

## How to access it

### Dedicated Window

Dedicated Window allows you to customize the windows' pinned position and its width and height ratio relative to your active screen size (also known as Quake Mode).

1. Open `Settings > Features > Keys` and select "Dedicated hotkey window" from the Global Hotkey dropdown to enable the feature.
2. Configure the keybinding, the windows position, screen, and relative size or uncheck "Autohides on the loss of keyboard focus" which will cause the dedicated Hotkey Window to stay on top when triggered regardless of mouse or keyboard focus.

{% hint style="warning" %}
On Linux and Windows, Warp does not support the "Autohides on the loss of keyboard focus" feature.
{% endhint %}

### Show/Hide All Windows

Show/Hide All Windows allows you to configure a shortcut to show/hide all Warp windows.

1. Open `Settings > Features > Keys` and select "Show/hide all windows" from the Global Hotkey dropdown to enable the feature.
2. Configure your preferred keybinding.

{% hint style="warning" %}
On Linux, hidden windows may not appear in your `ALT-TAB` window switcher menu. Furthermore, the ordering of windows beyond the top window may change after toggling.
{% endhint %}

## How it works

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-048acf9fd85b0fa2129bb90a1b3d8a2d1f911f5b%2FDedicated%20Window.gif?alt=media&#x26;token=39195b3a-16c6-44e5-b2e2-f4bb84677c30" alt=""><figcaption><p>Global Hotkey - Dedicated Window Demo</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-af6164e0085e8fa8f3d2ff3602178e4c9343332c%2FShow-Hide%20All%20Windows.gif?alt=media&#x26;token=e292ad67-f087-4b0b-a779-f5266be40a45" alt=""><figcaption><p>Global Hotkey - Show/Hide All Windows Demo</p></figcaption></figure>

## Troubleshooting Hotkey Dedicated Window

Review platform-specific instructions for troubleshooting the global hotkey below

{% tabs %}
{% tab title="macOS" %}
If the keybinding doesn't work, check under `System Preferences > Security & Privacy > Accessibility` and tick the checkbox to grant Warp access.
{% endtab %}

{% tab title="Windows" %}
On Windows, there are no known issues with Global Hotkey Dedicated Window. If you find an issue, please [send feedback](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback) to let us know.
{% endtab %}

{% tab title="Linux" %}
The hotkey window may appear on the incorrect monitor under certain window sizes. For example, with GNOME, if the hotkey window is supposed to show on a monitor having the taskbar (GNOME Panel), and the window height is 100%, causing an overlap, the hotkey window may fallback to showing on an external monitor if you have one. Try working around this by setting a window height to a lesser percentage, e.g. 90%.
{% endtab %}
{% endtabs %}


# Tabs

The Tabs feature allows you to organize a window into multiple terminal sessions. Tabs can be customized with a title and/or an ANSI color to help identify them.

{% hint style="info" %}
New Tabs will default to the active Tabs’ current [Working Directory](https://docs.warp.dev/documentation/terminal/more-features/working-directory) and the actual color values will be automatically derived from your Warp [Theme](https://docs.warp.dev/documentation/terminal/appearance/themes).
{% endhint %}

## How to use Tabs

{% tabs %}
{% tab title="macOS" %}

* Right-click on the new Tab button `+` to make a new tab, restore closed tab, or run a saved [Launch Configuration](https://docs.warp.dev/documentation/terminal/sessions/launch-configurations).
* Open a new Tab with `CMD-T` or by clicking on the `+` in the top bar.
* Close the current Tab with `CMD-W` or by clicking on the `X` on hover over a Tab.
* Reopen closed tabs with `SHIFT-CMD-T`.
* Move a Tab to the Left / Right with `CTRL-SHIFT-LEFT` / `CTRL-SHIFT-RIGHT` or by clicking and dragging a Tab.
* Activate the Previous / Next Tab with `SHIFT-CMD-{` / `SHIFT-CMD-}` or by clicking a Tab.
* Activate the first through eighth Tabs with `CMD-1` thru `CMD-8`.
* Switch to the last Tab with `CMD-9`.
* Double-click a Tab to rename it.
* Right-clicking on a Tab reveals more options you can explore within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or [Keyboard Shortcuts](https://docs.warp.dev/documentation/getting-started/keyboard-shortcuts#fundamentals).
  {% endtab %}

{% tab title="Windows" %}

* Right-click on the new Tab button `+` to make a new tab, restore closed tab, or run a saved [Launch Configuration](https://docs.warp.dev/documentation/terminal/sessions/launch-configurations).
* Open a new Tab with `CTRL-SHIFT-T` or by clicking on the `+` in the top bar.
* Close the current Tab with `CTRL-SHIFT-W` or by clicking on the `x` on hover over a Tab.
* Reopen closed tabs with `CTRL-ALT-T`.
* Move a Tab to the Left / Right with `CTRL-SHIFT-LEFT` / `CTRL-SHIFT-RIGHT` or by clicking and dragging a Tab.
* Activate the Previous / Next Tab with `CTRL-PGUP` / `CTRL-PGDN` or by clicking a Tab.
* Activate the first through eighth Tabs with `CTRL-1` thru `CTRL-8`.
* Switch to the last Tab with `CTRL-9`.
* Double-click a Tab to rename it.
* Right-clicking on a Tab reveals more options you can explore within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or [Keyboard Shortcuts](https://docs.warp.dev/documentation/getting-started/keyboard-shortcuts#fundamentals).
  {% endtab %}

{% tab title="Linux" %}

* Right-click on the new Tab button `+` to make a new tab, restore closed tab, or run a saved [Launch Configuration](https://docs.warp.dev/documentation/terminal/sessions/launch-configurations).
* Open a new Tab with `CTRL-SHIFT-T` or by clicking on the `+` in the top bar.
* Close the current Tab with `CTRL-SHIFT-W` or by clicking on the `x` on hover over a Tab.
* Reopen closed tabs with `CTRL-ALT-T`.
* Move a Tab to the Left / Right with `CTRL-SHIFT-LEFT` / `CTRL-SHIFT-RIGHT` or by clicking and dragging a Tab.
* Activate the Previous / Next Tab with `CTRL-PGUP` / `CTRL-PGDN` or by clicking a Tab.
* Activate the first through eighth Tabs with `CTRL-1` thru `CTRL-8`.
* Switch to the last Tab with `CTRL-9`.
* Double-click a Tab to rename it.
* Right-clicking on a Tab reveals more options you can explore within the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) or [Keyboard Shortcuts](https://docs.warp.dev/documentation/getting-started/keyboard-shortcuts#fundamentals).
  {% endtab %}
  {% endtabs %}

{% hint style="success" %}
**Terminal Tip**\
Using your `.zshrc` or `.bashrc` files on macOS or Linux, you can set a new Tab name:

{% code overflow="wrap" %}

```bash
# Set name, where MyTabName would be whatever you want to see in the Tab ( either a fixed string, $PWD, or something else )
function set_name () {
  echo -ne "\033]0;MyTabName\007"
}
# Add the function to the environment variable in either Zsh or Bash
if [ -n "$ZSH_VERSION" ]; then
  precmd_functions+=(set_name)
elif [ -n "$BASH_VERSION" ]; then
  PROMPT_COMMAND='set_name'
fi
```

{% endcode %}

Learn more about Tab names [here](https://learn.microsoft.com/en-us/windows/terminal/tutorials/tab-title#set-the-shells-title).
{% endhint %}

### Tab Restoration

Tab Restoration enables you to reopen recently closed tabs for up to 60 seconds. Configure this feature in `Settings > Features > Session > Enable reopening of closed sessions`

### CTRL-TAB Behavior

`CTRL-TAB` shortcut defaults to activate the previous / next Tab. You can configure the shortcut to cycle the most recent session, including any [Split Panes](https://docs.warp.dev/documentation/terminal/windows/split-panes), in `Settings > Features > Keys > Ctrl-Tab behavior`

### Tabs Behavior

Please see our [Appearance > Tabs Behavior](https://docs.warp.dev/documentation/terminal/appearance/tabs-behavior) docs for more Tab related settings.

### How Tabs work

{% embed url="<https://www.loom.com/share/84d15cc7eb5a4a668bb86be9e827f261?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Tabs Demo
{% endembed %}


# Split Panes

The Split Panes feature allows you to divide a tab into multiple rectangular panes, each of which is a unique terminal session.

## How to use Split Panes

{% tabs %}
{% tab title="macOS" %}

* Split Panes to the right / down with `CMD-D` / `SHIFT-CMD-D` or in any direction by right-clicking on any Pane.
* Activate the Previous / Next Pane with `CMD-[` / `CMD-]` or by clicking a pane.
* Navigate among Split Panes with `OPT-CMD-ARROW`, the active pane will be marked with a triangle in the top corner.
* Toggle Maximize Pane with `CMD-SHIFT-ENTER`.
* Close the active Pane with `CMD-W`.
* You can also drag and drop panes. Click and drag a Pane’s header around a given tab, drag the Pane to the tab bar to move it to another Tab, or make it into a Tab.
  {% endtab %}

{% tab title="Windows" %}

* Split Panes to the right / down with `CTRL-SHIFT-D` / `CTRL-SHIFT-E` or in any direction by right-clicking on any Pane.
* Activate the Previous / Next Pane with `CTRL-SHIFT-{` / `CTRL-SHIFT-}` or by clicking a pane.
* Navigate among Split Panes with `CTRL-ALT-ARROW`, the active pane will be marked with a triangle in the top corner.
* Toggle Maximize Pane with `CTRL-SHIFT-ENTER`.
* Close the active Pane with `CTRL-SHIFT-W`.
* You can also drag and drop panes. Click and drag a Pane’s header around a given tab, drag the Pane to the tab bar to move it to another Tab, or make it into a Tab.
  {% endtab %}

{% tab title="Linux" %}

* Split Panes to the right / down with `CTRL-SHIFT-D` / `CTRL-SHIFT-E` or in any direction by right-clicking on any Pane.
* Activate the Previous / Next Pane with `CTRL-SHIFT-{` / `CTRL-SHIFT-}` or by clicking a pane.
* Navigate among Split Panes with `CTRL-ALT-ARROW`, the active pane will be marked with a triangle in the top corner.
* Toggle Maximize Pane with `CTRL-SHIFT-ENTER`.
* Close the active Pane with `CTRL-SHIFT-W`.
* You can also drag and drop panes. Click and drag a Pane’s header around a given tab, drag the Pane to the tab bar to move it to another Tab, or make it into a Tab.
  {% endtab %}
  {% endtabs %}

{% hint style="info" %}
You can quickly find all the **pane** shortcuts by using the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette). You can also remap the shortcuts to your liking. See [Custom Keyboard Shortcuts](https://docs.warp.dev/documentation/getting-started/keyboard-shortcuts#custom-keyboard-shortcuts) for more details.
{% endhint %}

### CTRL-TAB Behaviour

`CTRL-TAB` shortcut defaults to activate the previous / next [Tabs](https://docs.warp.dev/documentation/terminal/windows/tabs). You can configure the shortcut to cycle the most recent session, including any Split Panes, in `Settings > Features > Keys > Ctrl-Tab behavior`

## How Split Panes work

{% embed url="<https://www.loom.com/share/c1104b51cab848a9bef6792ec4fd8421?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Split Panes Demo
{% endembed %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-44512f81f876be15ad0a63749dc0740ddcc2e9cd%2Fsplit-panes-dragging-demo.gif?alt=media" alt=""><figcaption><p>Split Panes Drag and Drop Demo</p></figcaption></figure>


# Warpify

Warp support for Warpifying, or enabling Warp's features, in local or remote sessions.

1. [Subshells](https://docs.warp.dev/documentation/terminal/warpify/subshells), Warp supports enabling Warp features in subshells for bash, zsh, and fish.
2. [SSH](https://docs.warp.dev/documentation/terminal/warpify/ssh), Warp supports a tmux powered wrapper that enables Warp features in remote (SSH) sessions.
3. [SSH Legacy](https://docs.warp.dev/documentation/terminal/warpify/ssh-legacy), Warp supports a legacy wrapper that enables Warp features in remote (SSH) sessions.

## Subshells

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bbd768d41f956ba63cc7410138fc2e5980c74d30%2Fsubshells-demo.gif?alt=media" alt=""><figcaption><p>Warpify Subshells Demo</p></figcaption></figure>

## SSH

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5cfba89554e738ad331b86151eae6b7bb819e306%2Fsubshell-ssh-demo.gif?alt=media&#x26;token=6af18eca-bfd1-4fd7-888a-2af3dd65dd51" alt=""><figcaption><p>Warpify SSH Demo</p></figcaption></figure>


# Subshells

Warp supports subshells for bash, zsh, and fish.

## What is a subshell?

Within the context of the Warp terminal, a "subshell" is defined as any nested interactive shell session that's spawned and running within the context of an existing, running shell. This might be a nested session running locally on your machine, a shell session running within a Docker container, or a remote server accessed through SSH. [See more on SSH Warpification](https://docs.warp.dev/documentation/terminal/warpify/ssh).

Note that Warp's definition of a subshell differs from the more common definition of a Unix subshell, which typically refers to any shell process spawned as a child of the interactive shell. For example, in bash, a command wrapped in parentheses is executed in a subshell with its own PID and addressable memory space.

## How to Warpify the subshell

By default, Warp automatically recognizes the following commands as **subshell-compatible**:

* bash, fish, zsh
* docker exec
* gcloud compute ssh
* eb ssh
* poetry shell

When you run a command that's subshell-compatible, Warp will prompt you and invite you to "Warpify" the subshell which makes all of the modern IDE features of Warp available in that subshell. The list of subshell-compatible commands is configurable in Subshell settings as described [below](#configuring-subshell-compatible-commands).

{% hint style="info" %}
bash, zsh, or fish (3.6 or above) must be set as the default shell within containers and ssh sessions for the Warpification of the subshells to work.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bbd768d41f956ba63cc7410138fc2e5980c74d30%2Fsubshells-demo.gif?alt=media" alt=""><figcaption><p>Subshells Demo</p></figcaption></figure>

### Configuring subshell-compatible commands

To configure subshell-compatible commands, navigate to the Settings > Subshells.

#### Adding compatible commands

You can add any command that spawns a bash, fish, or zsh subshell to ‘Added commands’ to make it eligible for "Warpification."

Furthermore, you can add regular expressions to the Added commands list. Any commands that match an added regex will be eligible for "Warpification."

#### Blocklisting commands

Some types of subshells are not compatible, and you may also want to control Warp so it never invites you to "Warpify" the subshells for specific commands. When you add commands to the Blocklist, Warp will never invite you to "Warpify" subshells spawned by those commands.

### Automatically "Warpify" subshells

To remember your preferences for a command and bypass the confirmation banner, you can manually paste the appropriate snippet to the end of the RC file corresponding to your subshell (bash, fish, or zsh).

```bash
# For zsh subshells, add to ~/.zshrc.
printf '\eP$f{"hook": "SourcedRcFileForWarp", "value": { "shell": "zsh"}}\x9c'

# For bash subshells, add to ~/.bashrc or ~/.bash_profile.
printf '\eP$f{"hook": "SourcedRcFileForWarp", "value": { "shell": "bash"}}\x9c'

# For fish subshells, add to ~/.config/fish/config.fish.
if status is-interactive
  printf '\eP$f{"hook": "SourcedRcFileForWarp", "value": { "shell": "fish"}}\x9c'
end
```

Once added, Warp will automatically "Warpify" subsequent subshell sessions for the corresponding shell on the machine with the newly updated RC file.

Under the hood, this snippet prints a Device Control String ([DCS](https://vt100.net/docs/vt510-rm/chapter4.html)) to be read by Warp, signaling that a subshell session has started and is ready to be "Warpified." In turn, Warp executes a setup script in the session that enables the full suite of Warp features like blocks, completions, and the input editor.

For this reason, it’s best to ensure the snippet is added to the end of the RC file, so Warp does not attempt to execute the setup script before the shell has finished sourcing your RC file.

To disable automatic integration, simply remove the snippet from the corresponding RC file.

If you happen to encounter issues in subshell sessions where the RC file is sourced, don’t hesitate to [file a GitHub issue](https://github.com/warpdotdev/Warp/issues/new/choose).

## Background commands

Warp runs background commands to power useful features like completions, syntax highlighting, and command corrections. For example, in order to provide completions for git checkout, Warp runs a background command that lists all git branches in the current repo.

In local subshell sessions, these commands are run in forked shell processes, isolated from your interactive shell session. This is the same implementation used for any non-subshell session.

In remote sessions, however, Warp takes a different approach – while a forked shell process is running on your local machine (where the Warp app is running), your remote session might be running on a server elsewhere. In these cases, Warp takes advantage of the session’s “idle time” – when no command is currently running – to run background commands directly in the session itself. These commands are executed in a non-interactive subshell process to prevent modifications to the session state (they cannot modify an environment variable, for instance).

### Show/hide background blocks

By default, blocks for background commands are hidden. To show background command blocks, select ‘Show background blocks’ in the ‘Blocks’ menu of the macOS menu bar.

### Disable background commands in remote sessions

We understand that some developers may want to disable background commands for certain or all environments.

To disable background commands in remote subshell sessions, you can execute the following command in a top-level terminal session:

{% tabs %}
{% tab title="macOS" %}
Update the settings defaults located in `dev.warp.Warp-Stable` to include the following name-value pair: `"DisableInBandCommands": "true"`.

```bash
defaults update dev.warp.Warp-Stable DisableInBandCommands true
```

{% endtab %}

{% tab title="Windows" %}
Update the settings registry located at `HKCU:\Software\Warp.dev\Warp` to include the following name-value pair: `"DisableInBandCommands": "true"`.

```powershell
Set-ItemProperty -Path "HKCU:\SOFTWARE\Warp.dev\Warp" -Name DisableInBandCommands -Value true
```

{% endtab %}

{% tab title="Linux" %}
Update the settings file located at `~/.config/warp-terminal/user_preferences.json` to include the following name-value pair: `"DisableInBandCommands": "true"`.

```bash
cd ~/.config/warp-terminal/
jq '.prefs += {"DisableInBandCommands": "true"}' user_preferences.json > tmp.json && mv tmp.json user_preferences.json
```

{% endtab %}
{% endtabs %}

This will effectively disable tab completions, syntax highlighting, command corrections, and the git status prompt indicator in remote subshells.


# SSH

SSH wrapper that enables Warp features in remote sessions.

{% hint style="warning" %}
This page is dedicated to the SSH features powered by `tmux`.

If you are looking to troubleshoot the legacy SSH implementation, see the [SSH (Legacy)](https://docs.warp.dev/documentation/terminal/warpify/ssh-legacy).
{% endhint %}

Warpifying your SSH session gives you all the features of Warp while connected to a remote machine: the input editor, auto-completions, history search, and more. We achieve this by running commands like `ls` on the remote machine on your behalf.

**Warpifying a remote SSH Session** [**will never make lasting changes to the remote machine without your explicit consent**](#will-warpifying-a-remote-ssh-session-make-changes-to-the-remote-machine)**.**

![SSH](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d750cd2460fe3cc59aef6a301b61fdccc4970088%2Fwarpify_ssh_prompt.png?alt=media)

## FAQs

#### Will Warpifying a remote SSH session make changes to the remote machine?

Only to install [`tmux`](#why-do-i-need-tmux-on-the-remote-machine) (a popular open source terminal multiplexer) and only with your explicit permission. If `tmux` is not installed, Warp will offer to install it for you and will show you the list of commands that will be run. You can always decline and continue to use your ssh session without some of Warp's features (or install `tmux` yourself and re-run Warpification [via the command palette](#what-if-warp-fails-to-detect-my-ssh-session)).

#### Why do I need `tmux` on the remote machine?

`tmux` is used to asynchronously run commands on the remote machine without disrupting your interactive session. [tmux](https://github.com/tmux/tmux/wiki) is a popular open source terminal multiplexer, which lets you run multiple sessions within one ssh connection. It requires minimal permissions and is widely adopted (⭐ 35k+ on GitHub). Warpifying a remote SSH session uses [tmux Control Mode](https://github.com/tmux/tmux/wiki/Control-Mode) to run adhoc background tasks (like those required to autocomplete a `cd` command, or populate the contents of a custom prompt).

#### Can I ssh to remote machines that I don't want to Warpify?

Yes! You can always cancel Warpification and continue to use SSH, just without some of Warp's additional features. You can also explicitly add hosts to the Denylist to ensure you’re never asked to Warpify that host again.

### Do I have to manually Warpify every time?

After you successfully Warpify an SSH connection manually, we provide a brief script you can run to append a message at the end of your shell's rcfile. This allows us to know when your shell is ready to be Warpified, and be found at the bottom of your rcfile for the best results.

![Setting up Auto-Warpify](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b2a6821c94e4894c2e0313ccc5b328897106949d%2Fwarpify_ssh_auto_script.png?alt=media)

#### What shells and operating systems are supported?

At the time of writing, we support macOS and most flavors of Linux as remote hosts. Supported shells are `bash` and `zsh`.

#### What if Warp fails to detect my SSH session?

If you are ever in a remote SSH Session and would like to manually Warpify, you can do so by using the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) and searching for "Warpify SSH Session".

#### What triggers SSH Session Detection for Warpification?

If SSH Session Detection is enabled, Warp will detect when you run an `ssh` command with arguments that suggest it's starting an interactive session. If you've aliased `ssh` or are running it as part of a script, we will not perform SSH Session Detection.

Once we have confidence you have successfully authenticated (by detecting `Last login:` or something resembling a basic prompt) we will prompt you to Warpify your active SSH session.

If SSH Session Detection does not detect your session, you can still [Warpify manually](#what-if-warp-fails-to-detect-my-ssh-session).


# SSH Legacy

SSH wrapper that enables Warp features in remote sessions.

{% hint style="info" %}
If you are looking to troubleshoot the TMUX SSH feature, see the [SSH](https://docs.warp.dev/documentation/terminal/warpify/ssh).
{% endhint %}

When you SSH into a remote box, you get all the features of Warp without any configuration on your part. The input editor, auto-completions, and history search work the same, regardless of machine.

{% hint style="warning" %}
[Limitations of SSH](https://github.com/warpdotdev/Warp/issues/578) (as of May 2024):

* The SSH Wrapper only supports `bash`or `zsh` shells in remote sessions.
* If you're using a different shell, you'll want to use `command ssh` directly (see below for more details).
* For zsh, xxd is required to bootstrap warp.
* For Windows, [Cygwin](https://www.cygwin.com/) is required to bootstrap the SSH Wrapper.
* RemoteCommand causes the ssh wrapper to fail.
* [Tmux is not currently supported.](https://github.com/warpdotdev/Warp/discussions/501)
  {% endhint %}

{% hint style="info" %}
If you're using zsh on the remote host, Warp creates a temp folder to act as the ZDOTDIR during the bootstrapping process and removes it when the shell is set up.
{% endhint %}

<figure><img src="broken-reference" alt="SSH"><figcaption><p>SSH</p></figcaption></figure>

## Implementation

We create a wrapper (around `/usr/bin/ssh`) to set up the shell for Warp's feature set. We authenticate normally using `/usr/bin/ssh`, and bootstrap the remote shell to work with Warp Blocks and the Input Editor. You can opt out of this functionality by invoking `command ssh` directly.

* Warp takes over the prompt which enables us to build a modern input editor.
* Warp configures histcontrol to ignore commands with leading spaces. We do this so our bootstrapping code does not clutter the history.

You can see the SSH wrapper by using `which warp_ssh_helper` in zsh, `type warp_ssh_helper` in bash.

*Note:* The ssh wrapper is only *initialized* on your local machine. We don’t currently support bootstrapping nested ssh sessions.

{% hint style="info" %}
Warp [Completions](https://docs.warp.dev/documentation/terminal/command-completions/completions) for ssh show entries in `~/.ssh/config` and `~/.ssh/known_hosts`
{% endhint %}

## Troubleshooting SSH

### channel 2: open failed: connect failed: open failed

If you're seeing these errors, you may have some config on your server (usually in `/etc/ssh/sshd_config`) preventing Warp's ControlMaster connection from working. In this state, completions that require information from your remote host won't work and your history also won't work.

You should ensure that `MaxSessions` is either commented out or is at least `2`.

Write access in `/etc/ssh/` typically requires sudo access. After any edits, you'd also need to restart the `sshd` daemon.

### SSH Wrapper fails

There are several [known issues with SSH Wrapper](https://github.com/warpdotdev/Warp/issues?q=is%3Aissue+is%3Aopen+sort%3Acreated-desc+label%3ABugs+label%3ASSH). As a workaround to the SSH Wrapper, you can add `command ssh` to your `Settings > Subshells > Added commands`, then run `command ssh <user@server>` to connect to a remote session, this will attempt to enable Warp features as a [subshell](https://docs.warp.dev/documentation/terminal/warpify/subshells).

{% hint style="info" %}
If the subshell workaround helps, we recommend you disable the SSH Wrapper in `Settings > Features.`You'll need to start a new session before a change is reflected or try invoking the SSH binary directly with `command ssh`.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5cfba89554e738ad331b86151eae6b7bb819e306%2Fsubshell-ssh-demo.gif?alt=media&#x26;token=6af18eca-bfd1-4fd7-888a-2af3dd65dd51" alt="Command SSH subshell workaround"><figcaption><p>Warpify SSH Demo</p></figcaption></figure>


# More Features


# Accessibility

Our mission is to make Warp the most accessible terminal for all developers. It includes fixing the UI, making it easier to use for experts and new engineers who are starting to use the command line.

{% hint style="info" %}
Note that currently, these instructions are for macOS only. Warp doesn't support screen readers on Linux or Windows and it's being tracked here: <https://github.com/warpdotdev/Warp/issues/3847>
{% endhint %}

We recognize the need to improve the experience for those visually impaired, as - to our best knowledge - other terminal emulator apps didn't do a good job in this area. This doc summarizes what we've done so far, how Warp works with VoiceOver, and outlines the main changes from the typical workflow. For the features documentation and its keyboard shortcuts, please go to the feature-specific page in the documentation.

**Keep in mind that this is a work-in-progress and the current state is not a final state of accessibility in Warp**.

## How to use Warp with Voice Over?

The best way to start working with Warp & VoiceOver is to install it using Homebrew:

`brew install warp`

This will ensure that you can receive all future updates automatically, without the need to go through a macOS standard drag-and-drop installation process.

From there, Warp should seamlessly work with VoiceOver and start announcing what's happening on the screen and what actions you can take. This may be a major difference from other apps - as Warp announces stuff on its own, letting you know what's going on. There's currently no way to navigate between different UI elements using VO key combinations.

Once installed, it will ask you to log in. Warp also sends telemetry that we use to improve the overall user experience. You can find out more about that in the [privacy section](https://docs.warp.dev/documentation/privacy/privacy).

The login flow will require you to navigate between the app and your browser. The last step before you can start enjoying our new terminal app is filling up the onboarding survey.

The main terminal window is not that different from other terminals - there's a place to type commands (Command Input) and a list of the previously executed commands and their outputs. Warp groups those together - each command and output create a Block. You can navigate blocks with your keyboard to easily check what was the command, learn whether it was successful or not, and what was the output, as well as more easily copy the command, output, or both for further processing.

A main entry point for discovering new features and actions is our Command Palette, which you can access by executing the cmd-p shortcut.

## Differences from the regular VoiceOver workflow

As you may notice, typical Voice Over navigation keys or settings do not currently work in Warp. In short - it's related to how our UI Framework is currently implemented and that as of now we don't yet offer a keyboard-accessible way to navigate the UI elements.

Instead, whenever you perform an action and/or something happens in the background, Warp announces it to you, letting you know what's going on and what possible actions you can take. Since it's a terminal, we care about all user actions being keyboard accessible from the start, so pretty much all our features have the assigned keybindings already. You can adjust the default keybindings following the guide from this GitHub repository: <https://github.com/warpdotdev/keysets>. You can also always fall back to using cmd-p to check the keybinding or execute the specific action.

### A11y specific actions

Some a11y-specific settings are available through the command palette. For example, you can adjust the verbosity level of messages. Simply enter the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) and type "a11y" to discover related options and their keybindings.

### Voice Input

Warp supports voice input as an alternative way to interact with your terminal. This can be especially helpful for users who prefer or require voice commands over typing. You can use voice input to:

* Issue terminal commands
* Ask questions about command usage
* Perform complex multi-step operations

Voice input can be enabled in `Settings > AI > Voice`. For detailed information about voice features and setup, see our [Voice documentation](https://docs.warp.dev/documentation/agents/voice).

## Future work

While not all Warp features are accessible yet, we've implemented a process around releasing new features and changes to the main app, to ensure that all new code provides proper a11y announcements.

This is not the ideal and final implementation. We're happy to hear your thoughts and ideas on how we can improve. The biggest milestone for this work is to add support for navigating the UI elements using the keyboard. Give Warp a try, and please, do not hesitate to [share your feedback](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback).


# Files, Links, & Scripts

Quickly open links and files or run scripts with your mouse.

## Files & Links

Warp supports opening files, folders, and URL links that are within Blocks. Multiple URL protocols are supported e.g. `https`, `ftp`, `file`, etc. Warp can open files and folders in a variety of editors and opens web links directly in your default browser. Warp can also open markdown files directly with a [Markdown Viewer](https://docs.warp.dev/documentation/terminal/more-features/markdown-viewer).

{% hint style="info" %}
Warp also supports iTerm2 and Kitty Image protocols on macOS and Linux. You will need to use a cli tool to view images, in some cases the tools expect `$TERM=kitty`, so you may need to workaround this by setting `TERM=kitty` before the command. We're working on updating the popular tools to recognize Warp natively.
{% endhint %}

Warp parses relative and absolute file paths. Warp also tries to capture line and column numbers attached to the file path, supported formats include:

* `file_name:line_num`
* `file_name:line_num:column_num`
* `file_name[line_num, column_num]`
* `file_name(line_num, column_num)`
* `file_name, line: line_num, column: column_num`
* `file_name, line: line_num, in`

{% tabs %}
{% tab title="macOS" %}

1. After hovering over a link, open it directly by holding down `CMD` while clicking it.
2. Clicking a link normally will open a clickable tooltip that says “Open File/Folder/Link”.
3. Right-clicking a link will open a context menu that supports copying the absolute file path or URL to the clipboard.
   {% endtab %}

{% tab title="Windows" %}

1. After hovering over a link, open it directly by holding down `CTRL` while clicking it.
2. Clicking a link normally will open a clickable tooltip that says “Open File/Folder/Link”.
3. Right-clicking a link will open a context menu that supports copying the absolute file path or URL to the clipboard.
   {% endtab %}

{% tab title="Linux" %}

1. After hovering over a link, open it directly by holding down `CTRL` while clicking it.
2. Clicking a link normally will open a clickable tooltip that says “Open File/Folder/Link”.
3. Right-clicking a link will open a context menu that supports copying the absolute file path or URL to the clipboard.
   {% endtab %}
   {% endtabs %}

* You can also Drag and drop a folder or file onto the Warp dock icon to open a new tab in this directory.
* You can also right-click on a folder or file in Finder, then select Services, and "Open new Warp Tab | Window here".
* Configure the default editor to open files by navigating to `Settings > Features > Choose an editor to open file links`.
  * Selecting "Default App" uses your system's default application for the file type.

#### List of supported editors

Non exhaustive list of editors, please submit new ones on our GitHub, see [Sending Feedback](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback#sending-warp-feedback).

1. `$EDITOR`
2. Visual Studio Code
3. JetBrains IDEs
   * WebStorm
   * PhpStorm
   * GoLand
   * PyCharm
   * DataGrip
   * DataSpell
   * Rider
   * RubyMine
4. Zed and Zed Preview
5. Cursor
6. Windsurf
7. Sublime Text
8. Android Studio

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4b35a52c9e42ce96877811f1ce788c85411727f5%2Ffiles-links-demo.gif?alt=media" alt=""><figcaption><p>Files &#x26; Links Demo</p></figcaption></figure>

## Scripts

Warp can open `.command` and Unix Executable files from the finder directly.

1. Find a `.command` or Shell script you'd like to open in Finder.
2. Right-click and open the script with Warp.

{% hint style="warning" %}
Make sure the file has the appropriate executable permissions before you can run it in Warp. (e.g. `chmod +x script.command`)
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f7a1e04f36dc80e8840fd8b556d1e2ab92d933be%2Fscript-demo.gif?alt=media" alt=""><figcaption><p>Scripts Demo</p></figcaption></figure>


# Markdown Viewer

Open Markdown files in your terminal and run commands.

Warp can be used for both editing and viewing rendered Markdown files in a [split pane](https://docs.warp.dev/documentation/terminal/windows/split-panes). Any local file with the `.md` or `.markdown` extension is treated as a Markdown file. Remote files are currently not supported. Turning on `Settings > Features > General > Open Markdown files in Warp's Markdown viewer by default` will make the Markdown viewer default, otherwise Markdown files will open in Warp's editor.

### Opening a file link within a block

{% tabs %}
{% tab title="macOS" %}
For any link to a Markdown file within a block, you can open the file in Warp by `CMD`-clicking on the link, from the link tooltip, or the right-click context menu on the link.
{% endtab %}

{% tab title="Windows" %}
For any link to a Markdown file within a block, you can open the file in Warp by `CTRL`-clicking on the link, from the link tooltip, or the right-click context menu on the link.
{% endtab %}

{% tab title="Linux" %}
For any link to a Markdown file within a block, you can open the file in Warp by `CTRL`-clicking on the link, from the link tooltip, or the right-click context menu on the link.
{% endtab %}
{% endtabs %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-838cc78bfe78ea51475f75bfdb58e8ac59893755%2Fopen-markdown-viewer.gif?alt=media" alt="Clicking a Markdown file link in the output of ls to open it in Warp"><figcaption><p>Opening a Markdown file in Warp using the link tooltip</p></figcaption></figure>

### Markdown-viewing commands

If you run a Markdown-viewing command like `cat myfile.md`, Warp will show a banner with a button to open the Markdown file.

The following commands are considered Markdown viewers:

* `cat`
* `glow`
* `less`

### Opening a Markdown file from Finder

From Finder, you can open a Markdown file in Warp from the “Open With” menu that appears when right-clicking on the file.

### Toggling between editor and viewer

You can toggle between the Markdown editor and viewer via the pane overflow menu.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-27a4d58bd65e92e65b65913c77a92b2381effc14%2Fmarkdown-raw-rendered-toggle.gif?alt=media" alt="Clicking a Markdown file link in the output of ls to open it in Warp"><figcaption><p>Toggling between editor and viewer</p></figcaption></figure>

## Shell commands in Markdown files

Warp can run shell commands from Markdown code blocks in your active terminal session. Click the run icon `>_` to insert a command into the terminal input.

{% hint style="info" %}
The shell command must be in a code block with three backticks ` ``` ` and not inline code for Warp to treat the code like a runnable command.
{% endhint %}

Markdown shell blocks also support keyboard navigation. There are two ways to enter the keyboard navigation mode:

{% tabs %}
{% tab title="macOS" %}

* Clicking on a shell block.
* Pressing `CMD-UP` or `CMD-DOWN`.

Once a shell block is selected, press `CMD-ENTER` to insert it into the terminal input. You can also use `UP`, `DOWN`, `CMD-UP`, and `CMD-DOWN` to navigate between shell blocks. While the Markdown file is focused, press `CMD-L` to switch focus back to the terminal without inserting a command.
{% endtab %}

{% tab title="Windows" %}

* Clicking on a shell block.
* Pressing `CTRL-UP` or `CTRL-DOWN`.

Once a shell block is selected, press `CTRL-ENTER` to insert it into the terminal input. You can also use `UP`, `DOWN`, `CTRL-UP`, and `CTRL-DOWN` to navigate between shell blocks. While the Markdown file is focused, press `CTRL-SHIFT-L` to switch focus back to the terminal without inserting a command.
{% endtab %}

{% tab title="Linux" %}

* Clicking on a shell block.
* Pressing `CTRL-UP` or `CTRL-DOWN`.

Once a shell block is selected, press `CTRL-ENTER` to insert it into the terminal input. You can also use `UP`, `DOWN`, `CTRL-UP`, and `CTRL-DOWN` to navigate between shell blocks. While the Markdown file is focused, press `CTRL-SHIFT-L` to switch focus back to the terminal without inserting a command.
{% endtab %}
{% endtabs %}

If the command contains any arguments using the curly brace `{{param}}` syntax, they will be treated as Workflow arguments. Learn more about [Workflows](https://docs.warp.dev/documentation/knowledge-and-collaboration/warp-drive/workflows).

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b8c067eeb9cd819702a18393daf9ac863140d279%2Frun-markdown-file-command.gif?alt=media&#x26;token=5f339436-e7a8-4e5e-9470-e66b380ed629" alt="Demo of running two commands from a Markdown file in Warp"><figcaption><p>Navigating between and running commands in a Markdown file</p></figcaption></figure>

In addition, all shell and code blocks have a copy button to quickly copy the block’s text to the clipboard.

Code blocks without a set language, or one of the following languages, are treated as shell commands: `sh`, `shell`, `bash`, `fish`, `zsh`, `warp-runnable-command`.


# Working Directory

## What is it

Warp's working directory feature is designed to enhance your workflow by enabling you to set up a default directory for new sessions. This feature helps you save time and quickly access your preferred directories when starting new sessions. You have the flexibility to set up a working directory for all new sessions or customize it individually for Windows, Tabs, and Panes, based on your specific needs.

## How to access it

* Open `Settings > Features > Session` and go to "Working directory for new sessions".
* The drop-down for this feature provides several options discussed below:
  * Home Directory, is the default option for new sessions and opens new sessions in the currently logged-in users home folder `~/`.
  * Previous session's directory, opens new sessions in your active sessions' current directory.
  * Custom directory, opens new sessions in a file path you specify.
  * Advanced, allows you to select from the three options for new sessions in Windows, Tabs, and Panes.

## How to use it

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-28df13a68133e6b8616525cff46242da198f7ce9%2Fworking-directory-demo.gif?alt=media&#x26;token=cb629cc7-397a-4bb7-b9c5-d2346533694e" alt="Working Directory Demo"><figcaption><p>Working Directory Demo</p></figcaption></figure>


# Text Selection

Warp supports both smart selection and rectangular (column) selection, making it easier to quickly highlight the text you need without tedious dragging or cleanup.

## Smart Selection

**Smart selection** goes beyond the typical double-click selection, which only highlights a single word. Instead, it uses semantic rules to treat common patterns (like URLs or file paths) as one unit, even when separated by punctuation or whitespace.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-193352c4cee174eebbcff3d530b604da8c917e52%2Fsmart-selection.png?alt=media" alt=""><figcaption><p>Using smart selection to select a file path by double clicking.</p></figcaption></figure>

Double-click on text in the input or blocklist. The following patterns are recognized:

1. URLs
2. File paths
3. Email addresses
4. IP addresses
5. Floating point numbers, including scientific notation.

You can toggle smart selection on the `Settings > Features > Terminal > Double-click smart selection`. If disabled, you can instead manually select specific punctuation characters to be included within word boundaries.

## Rectangular Selection

**Rectangular selection** lets you highlight text in a clean vertical block (also called *column* or *box* selection). This is especially useful for copying command output, logs, or prefixed text without grabbing unwanted characters.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-98d2d2b41c2b0e0cc6cd62bf31087c63f1643a0a%2Frectangular-selection.png?alt=media" alt=""><figcaption><p>Using rectangular selection to select by columns in the block output.</p></figcaption></figure>

Hold the modifier keys while dragging your mouse:

* macOS: `CMD-OPT`
* Windows and Linux: `CTRL-ALT`


# Full-screen Apps

Warp runs alt-grid apps like Vim and Emacs in full-screen mode. Warp also supports sending mouse and scroll events directly to the alt-grid or adjusting the padding surrounding the apps.

## Mouse and Scroll Reporting

Warp supports configuring how to handle mouse and scroll events. They can be sent to the currently running app, e.g. `vim`, or kept and handled by Warp.

{% hint style="info" %}
Mouse reporting must be enabled to also toggle scroll reporting.
{% endhint %}

Once mouse reporting is enabled, Warp will use ANSI escape sequences to communicate mouse events to the running app.

{% hint style="info" %}
If you want a mouse event to go to Warp instead (for example, for text selection) without disabling mouse reporting, you can hold the `SHIFT` key.
{% endhint %}

### How to access it

* From the Settings panel, `Settings > Features > Enable Mouse Reporting`
  * Scroll Reporting can be enabled after toggling `Enable Mouse Reporting`
* From the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), search for "Toggle Mouse Reporting"
* From the macOS Menu, `View > Toggle Mouse Reporting`

### How it works

{% embed url="<https://www.loom.com/share/a918696b002148d3beafd545b233c1be?hideEmbedTopBar=true&hide_owner=true&hide_share=true&hide_title=true>" %}
Mouse and Scroll Reporting Demo
{% endembed %}

## Padding

Warp supports configuring how much padding surrounds full-screen apps. The default is 0 pixel padding, but this can be changed to a custom padding amount or to match the padding in the Blocklist.

{% hint style="info" %}
Warp allows you to scale your terminal by fractions of a cell width | height. When your terminal size is not perfectly aligned to a cell width | height, the extra space appears as padding on the right | bottom.
{% endhint %}

### How to access it

* Go to `Settings > Appearance > Full Screen Apps` or from the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) search for "Appearance"
  * `Use custom padding in alt-screen` is enabled by default, you can disable it to match the Blocklist padding
    * Set the desired uniform padding (px) pixels, which is set to 0px by default

{% hint style="warning" %}
Some full-screen applications don't behave well when resizing. If you are experiencing rendering issues with full screen apps, try turning this setting off. This will ensure that full-screen apps don't need to resize when starting up.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f389a59e0d72e737fdf978fe65e59ef32ad2ceeb%2Fpadding-settings.png?alt=media" alt="alt-screen padding setting"><figcaption><p>Alt-screen padding setting</p></figcaption></figure>


# Desktop Notifications

Warp can send you customizable desktop notifications when you are away from the app and quickly re-focus when something meaningful happens in your terminal sessions.

## What is it

Notifications can be sent when a command completes after a configurable number of seconds or when a running command needs you to enter a password to proceed. For either of these triggers, Warp will only send you a desktop notification if you are using a different app at the time the trigger is fired.

## How to access it

### Notifications

* Notifications are enabled by default and require system permissions to appear.
* If you've turned Notifications off before, toggle it back on by going to `Settings > Features > Session`, or quickly toggle Notifications with the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette).
* Customize Notification triggers for long-running commands or password prompts by going to `Settings > Features`.

{% hint style="info" %}
On macOS, you will want to **Allow** or **Accept** the request so that Warp can send you desktop notifications. If you accidentally denied it or would like to re-enable Notifications later, check the [troubleshooting guide below](#troubleshooting-notifications).
{% endhint %}

## How it works

{% embed url="<https://www.loom.com/share/65967f43a7fa432b98cf3e94766a8e79?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Notifications Demo
{% endembed %}

## Troubleshooting Notifications

{% tabs %}
{% tab title="macOS" %}
Warp requires two distinct notification settings to work. Mac system settings found in `Mac > System Preferences > Notifications & Focus` and Warp app settings found in `Settings > Features > Session` must both be enabled for Notifications to show.\
\
If you have Notifications enabled in the system and Warp, but you still aren't receiving desktop notifications, try the following:

* Make sure that you are navigated away from Warp when you expect to receive the notification.
* Make sure the **Do Not Disturb** mode is turned off in `Mac > System Preferences > Notifications > Notifications & Focus > Focus`.
* Go to `Mac > System Preferences > Notifications & Focus > Notifications` and select Warp in the list. Make sure either banner style or alert style notifications are selected, then quit and restart Warp.
* To get the MacOS notification prompt to show again for Warp, run `defaults delete dev.warp.Warp-Stable Notifications`, then restart Warp and toggle on the `Settings > Features > Receive desktop notifications from Warp`.
* Once all of the above is done, please Restart MacOS to apply the changes and that should help with restoring notifications in Warp.
  {% endtab %}

{% tab title="Windows" %}
Warp requires two distinct notification settings to work. Windows system settings found in `Settings > System > Notifications > Warp` and Warp app settings found in `Settings > Features > Session` must both be enabled for Notifications to show.

If you have Notifications enabled in the system and Warp, but you still aren't receiving desktop notifications, try the following:

* Make sure that you are navigated away from Warp when you expect to receive the notification.
* Make sure the **Do Not Disturb** mode or **Focus** is turned off.
* Go to `System > Notifications` and select Warp in the list. Make sure notifications are turned on, then quit and restart Warp.
  {% endtab %}

{% tab title="Linux" %}
Warp requires two distinct notification settings to work. Linux system settings found in `Settings > Notifications > Warp` and Warp app settings found in `Settings > Features > Session` must both be enabled for Notifications to show.

If you have Notifications enabled in the system and Warp, but you still aren't receiving desktop notifications, try the following:

* Make sure that you are navigated away from Warp when you expect to receive the notification.
* Make sure the **Do Not Disturb** mode (if your distribution supports it) is turned off.
* Go to `Settings > Notifications` and select Warp in the list. Make sure notifications are turned on, then quit and restart Warp.
  {% endtab %}
  {% endtabs %}

Please [reach out to us](https://docs.warp.dev/documentation/support-and-billing/sending-us-feedback#sending-warp-feedback) if any other issues.


# Audible Bell

Warp allows you to enable an audible terminal bell (disabled by default) that can be triggered by a variety of CLI tools (for example, `ping -a`).

* In Settings, enable an Audible terminal bell in `Settings > Features > Terminal`.
* In [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), “Enable/Disable Audible Terminal Bell”.


# Settings Sync (Beta)

Settings Sync is a cloud feature in Warp that makes it convenient to use Warp on multiple devices or on a single device using both the Desktop and Web versions of Warp.

{% hint style="info" %}
Settings Sync is an experimental (Beta) feature. We will post updates on github request [#2561](https://github.com/warpdotdev/Warp/issues/2561). Please note that it sends your settings information to Warp’s servers. Read more about privacy for cloud features in the [privacy overview](https://www.warp.dev/privacy/overview).

Starting January 9, 2025, we will be enabling Settings Sync gradually for a percentage of Warp users. New users who are included in this percentage rollout will have Settings Sync on by default; existing users in the percentage rollout will need to opt-in to Settings Sync in Settings > Account.
{% endhint %}

## How to toggle settings sync

* You can toggle Settings Sync within the `Settings > Account` pane
* Through the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette) by searching for “Settings Sync”

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-662986453e3d04b84693ebfa18afc07802c85cdf%2Fsettings-sync-account.png?alt=media" alt=""><figcaption><p>Settings Sync in Account pane</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-15ccabe97d60491d7005c4f1c7fd8243bf48d542%2Fsettings-sync-palette.png?alt=media" alt=""><figcaption><p>Settings Sync in Command Palette</p></figcaption></figure>

## How settings sync works

Settings Sync works by syncing the state of most of your Warp settings to our cloud servers.

When you log in to Warp on another device or through the browser if you have Settings Sync enabled, most of your settings will be the same as they were when you were logged in before.

That means your themes, most features, privacy settings, ai settings, are all the same everywhere you use Warp, saving you the time from having to set them up again.

When you first enable Settings Sync, the settings from the computer you enabled it on become the default settings for all devices. This is true if you toggle Settings Sync off and on as well - the synced settings are always from the last device you enabled Settings Sync on, so toggling effectively causes all of your devices to have settings from the current logged in instance.

### Non-synced settings

Not all settings are synced, however. Notably, Warp does not sync:

* Custom keybindings (we may in the future). Alhough, you can set [custom keybinds with a file](https://docs.warp.dev/documentation/getting-started/keyboard-shortcuts#custom-keyboard-shortcuts)
* Custom themes (we may in the future)
* Device specific settings (e.g. what editor you prefer using, startup shell)
* Platform-specific settings are synced across devices on the same platform (e.g. your settings for how to interact with the Linux clipboard are synced across all Linux devices, but not on Mac, Windows or Web).

You can tell when a setting is not synced because it will have a special cloud strikethrough icon in the settings panel.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-697734a14c0718b40ea2513bfdbe2d6ce8d1ea82%2Fsettings-not-synced.png?alt=media" alt=""><figcaption><p>Settings not synced</p></figcaption></figure>


# Quit Warning

Warp's quit warning feature is a valuable precaution to prevent unintentional data loss or lost progress on long-running jobs.

## What is it

The quit warning feature ensures that you receive a warning before quitting the app with a running process, allowing you to save your work and avoid any unintended data loss.\
If you quit the app or close a window containing a session with a running process, you'll see the alert and need to confirm the action before proceeding. If you aren't sure which processes you have running, there is also an option to show those processes.

## How to access it

* Open `Settings > Features > General`, there you can toggle the "Show warning before quitting".
* You can also toggle the quit warning feature in the [Command Palette](https://docs.warp.dev/documentation/terminal/command-palette), by searching for \`Quit Warning'.
* If enabled, when you try and close Warp you will see a pop-up window with a few options listed below:
  * Yes, quit, which will close all the Warps sessions and running processes.
  * Show running processes, which will bring up the [Session Navigation](https://docs.warp.dev/documentation/terminal/sessions/session-navigation) panel with a filter for running processes.
  * Cancel, which will prevent Warp from closing.
  * Don't ask again, which is a box you can check to disable the quit warning feature.

## How it Works

{% embed url="<https://www.loom.com/share/bacb9d1c1e3947dca8365e15231cfcd3?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Quit Warning Modal Demo
{% endembed %}


# URI Scheme

Warps URI scheme enables you to programmatically open new windows, tabs, or launch configurations with ease.

## How to use it

There are several ways to use the URI scheme:

* Open new window `warp://action/new_window?path=<path_to_folder>`
* Open new tab `warp://action/new_tab?path=<path_to_folder>`
* Open Launch Configuration `warp://launch/<launch_configuration_path>`

{% hint style="info" %}
[Warp Preview](https://docs.warp.dev/documentation/community/warp-preview-and-alpha-program) uri scheme begins with `warppreview://`
{% endhint %}

## How it works

Example of Warp [URIs in use in Warp + Raycast Extension](https://github.com/raycast/extensions/blob/74521b70b62355004b0958393a64f9417b1ff3a6/extensions/warp/src/uri.ts).

{% embed url="<https://twitter.com/i/status/1678432353461637121>" %}
Warp + Raycast Extension Demo made using URIs
{% endembed %}




---

[Next Page](/llms-full.txt/1)

