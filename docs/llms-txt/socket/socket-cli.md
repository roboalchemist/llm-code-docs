# Source: https://docs.socket.dev/docs/socket-cli.md

# Guide to Socket CLI

Introduction to Socket CLI

The Socket CLI is a collection of tools that works with the Socket API.

![Default help output of socket command](https://files.readme.io/7a14214ebe01294db39dad483d91715e1953686398e15fdf99512a4b595d5d21-image.png)

## Main features

Control Socket from your terminal and your code!

* Create **Socket Security Scans** from your terminal with [`socket scan create`](https://docs.socket.dev/docs/socket-scan)
* Get information on the **security score** of a package through [`socket package score`](https://docs.socket.dev/docs/socket-package)
* Check if your PR passes your **security/license policy** by [`socket scan --report`](https://docs.socket.dev/docs/socket-scan)
* OR take control and **automate your workflow** through [ `socket ci`](https://docs.socket.dev/docs/socket-ci)
* **Protect your workspace** with [`socket wrapper on`](https://docs.socket.dev/docs/socket-wrapper)  or run npm through [`socket npm`](https://docs.socket.dev/docs/socket-npm-socket-npx)
* View **security health history dashboards** in your terminal with [`socket analytics`](https://docs.socket.dev/docs/socket-analytics)
* Easy access to our **real time threat feed** through [`socket threat-feed`](https://docs.socket.dev/docs/socket-threat-feed)
* Apply **security updates** to packages through [`socket fix`](https://docs.socket.dev/docs/socket-fix)
* Apply **enhanced package overrides** with [`socket optimize`](https://docs.socket.dev/docs/socket-optimize)
* Control **account details** on Socket
* Most commands support `--json` and `--markdown` for automation
* Interactive terminal experience for setup and dashboards

See sidebar for overview of commands. Or run `socket --help` to see the available commands.

## What's in a Scan report?

A Socket Scan contains a full listing of all package issues present in the project, as well as individual health scores for each package and average scores for the whole project.

There's a lot of incredible information about your packages in here:

![](https://files.readme.io/e4746b6-Screenshot_2022-11-17_at_10.58.45_AM.png "Screenshot 2022-11-17 at 10.58.45 AM.png")

## How does the CLI work?

`socket` is a *multi-command* CLI tool.

The basic `socket` command does nothing more than giving you some help information, the rest of the magic is in the individual commands.

All commands describe themselves if you ask them using `--help`. There are a few categories of commands:

### Commands leveraging the Socket API

These commands give you easy access to our Socket API. This gives you access to organization information, repository management, scan management, analytics, audit logs, and thread feed.

Most of these commands require an API Token for access with the proper scope depending on the task. Commands will inform you when this is the case. You can generate API Tokens from your Socket dashboard.

### Commands running local tools

There are some things we can't do on the server. We don't have access to your full source code and in some purposes or ecosystems we would need that in order to complete our analysis. We also have a few tools that work on your source code.

Local tools are kind of what it sounds like: commands that are expected to run locally. They may generate an artifact that you can upload or commit. But it's something we can't ordinarily do on our servers. As such these commands do not require an API Token.

Concretely, this includes generating manifest files for certain ecosystems (gradle, sbt), fixing or optimizing your `package.json`, or computing tier 1 reachability.

### Commands for CLI configuration

There are also a few commands created for management of the CLI itself or its environment.

You can configure all its persisted settings. You can install the tab-completion script in case you didn't do this when logging int. You can login, which sets up a few things for you. You can logout or uninstall the tab completion script. You can toggle the wrapper.

## Flags

Every individual (sub-)command supports a few command flags. To find out what flags are supported by a (sub-)command and what they do, see the individual `--help` page of that command.

### Output

The CLI was designed to be able to be used with other tools in mind. You should be able to "pipe" (*send*) the result (*of stdout*) of the CLI to another command to work on that result. Most commands that don't *require* interactivity or calling another tool will support a `--json` and `--markdown` flag. When they do, we try really hard to always return a proper response, even if things fall apart.

* `--json` – outputs result as json which you can then pipe into [`jq`](https://stedolan.github.io/jq/) and other tools
* `--markdown` – outputs result as markdown which you can then copy into an issue, PR or even chat

### Generic flags

These flags are supported by every (sub-) command but they are not mentioned in their individual help page.

* `--config` – Overrides the internal config object with the result of this JSON for the duration of this call. Mostly helpful for debugging and tests. Persisting config changes will be disabled when this is used.
* `--dry-run` – validate inputs without starting on the actual task. This starts a command and will stop after the input validation.
* `--help` – prints the help for the current command. All (sub-) commands have their own help page.
* `--version` – prints the version of the tool. The version information is also printed as part of the banner at the top of every command.

## How can I get my hands on this?

Install it like this:

```
npm install -g socket
```

Then run it using commands like:

```
socket --help
socket package score npm webpack@5.75.0 --markdown
socket scan create ./proj
socket login
```

If you don't like to be asked for an API token all of the time you can do `socket login` to store the token locally. This command also helps you to set up the CLI with interactive questions.

Alternatively you can supply an API Token when running a command by setting it as an environmental variable:

```
SOCKET_SECURITY_API_TOKEN=xyz socket scan list
```

If you want to add the environment variable for a local project but not globally, then use a tool like [`direnv`](https://direnv.net/).

### Is the CLI distributed without using the npm registry?

Not as a fully built artifact. The ability to install software from the npm registry is a normal and generally accepted practice at the time of writing.

The code is open source, though. You can find the repository in its [GitHub repository](https://github.com/SocketDev/socket-cli-js) and you can build it manually.