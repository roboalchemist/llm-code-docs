# Cto.Ai Documentation

Source: https://docs.cto.new/llms-full.txt

---

# Blank Project
Source: https://docs.cto.new/blank-project



Projects help you manage your work in cto.

They can include chat sessions, repositories, coding tasks and bits of infrastructure.

A blank project or connected codebase is best for starting completely from scratch or connecting an existing codebase.

These projects have few guardrails or assumptions on what you're building, your development environment, or how you want to deploy it.

You can start with a connected repo or a blank project where you can then connect your own repos or create repos managed by cto.

<Note>
  You can add an unlimited number of repos to a blank project!
</Note>

Best for users with at least some technical experience.

# Chat

Blank projects can have several parallel chats that are able to create sub-agents to plans and write code.

Chat has context across your whole codebase, tools and connected MCPs.

<Note>
  Try asking [cto.new](http://cto.new) what you should work on
</Note>

[cto.new](http://cto.new) chat can help you figure out what to work on, plan tasks, and write code.

<Check>
  Chat sessions are private to each user
</Check>

### Sub-agents

Chat can create planning and coding sub agents [cto](http://cto.new) creates planning and coding agents (tasks) from a chat session.

Since [cto](http://cto.new) can spin up coding agents which work on tasks, there's a page to see all tasks for your project.

# Tasks

You can get [**cto**](http://cto.new) to work on your code by starting a task. The result of a task is usually a pull request.

### Start a Task

* Let [**cto.new**](http://cto.new) start a task from a chat
* Enter a task description directly in the tasks page
* Add a repo specific label to an issue (find this on the repositories page)
* Tag @cto anywhere in a **ticket** (except Linear) or **pull request**
* Assign an issue to [cto.new](http://cto.new) (Linear only)

### Task Runners

Tasks are complete inside a task runner. This is a cloud based virtual machine where [**cto.new**](http://cto.new) works on your task.

<Info>
  For best results make your the task runner is configured for each repo. Our set-up agent can do this for you
</Info>

### Manage Tasks

Go to the tasks page to view all running and past tasks. You can also review, merge, and close pull requests from here.

# API Integrations

This project type works with API workflow integrations.

Learn more about [API integerations](/integrations/API).


# Changelog
Source: https://docs.cto.new/changelog



# March 3rd 2026

### Web app projects

* Added web apps as a project type. Includes a live preview and interactive chat for vibe coding
* Provides Convex for backend services
* Sensible default development environment and settings for ease of use
* Automatically deploys and configures TanStack codebase

### Product and UX

* **Projects & workspaces:** Organize repos and apps into projects, with improved onboarding and nicer defaults.
* **Chat quality:** Better long-chat handling via compaction so sessions can continue without hitting context limits.
* **MCPs:** Manage MCP connections from the web UI, with clearer re-auth prompts when needed.

### Billing & limits

* Increased monthly usage limits across all paid tiers.

### Models

* Added/updated models including Claude Opus 4.6, Gemini 3.1 Pro, GLM-5.
* Allow model selection for free users.

# February 6th 2026

## Product and UX

* Start building without linking a git provider.
* Better handling of common failure modes.
* Chats are now “agent sessions” with clearer scoping between sessions.
* Cleaner task logs with improved tool-call rendering and live status.
* Tasks started from chat now stay scoped to the current session.
* Prevent duplicate messages while a chat run is already in progress.
* Automatic team naming.

## Infrastructure

* Migrated sandboxes to Daytona for faster startup and responsiveness.

## Integrations

* Added Supabase and Vercel MCP presets.
* Improved MCP auth/setup reliability.

## Models

* Added GPT‑5.2 Codex.
* Added Kimi K2.5.

# December 23rd 2025 ☃️

## Live Previews (beta)

* Live preview available in beta to all users.
* Start new template project from cto.new.
* Add build and run commands to task runner.
* Setup agent attempts build and run commands.

## Smarter model selection

* Route tasks based on quality, speed, capacity, and cost.
* Expanded model support, including:
  * GPT-5.2
  * Sonnet 4.5 - GPT 5.2 alloy
  * Claude Opus 4.5
  * Gemini 3 Flash preview)
  * GLM-4.7
  * MiniMax M2.1
  * Devstral 2

## Engine-agent chat improvements

* Faster, more reliable task planning.
* Better visibility into tool usage during runs.
* Tasks started from chat are now properly scoped and isolated.
* Simplified planning and draft task UX.

## MCP overhaul

* Unified MCP system with clearer setup and fewer edge cases.
* Global MCPs can now be configured once and reused in agents and chats.
* Per-chat MCP selection for more control.
* Improved support for HTTP, SSE, and stdio MCPs.
* Better error handling and clearer tool naming.

## Reliability & performance

* Faster VM startup times.
* More robust VM lifecycle handling.
* Better handling of temporary provider outages.

## Benchmark

* Introduced cto bench, measuring real-world task success rates across models.
* Live chart and leaderboard updated every day.

## UI & UX polish

* Mobile improvements.
* Keyboard shortcut: ⌘ + Enter throughout the app.
* Create empty repo from cto.new.
* Clearer task and preview states.
* General responsiveness and stability improvements.

# November 26th 2025

## Product & UX

* Add "get code" buttons for easily copyable git checkout commands for a task.
* Add task preview in alpha.
* Clearer draft PR/MR status.
* Chats moved to their own page.
* Add privacy mode for zero data use.

## Models & Routing

* Added GPT-5.1 and GPT-5.1 Codex and removed GPT-5 and GPT-5 Codex.
* Added GPT-5.1 Codex Mini.
* Added Gemini 3 Pro Preview.
* Added Kimi K2 Thinking.
* Added MiniMax M2.
* Improved and updated auto model routing.

## Infra, Events & Git

* Harden events queueing and retries.
* Update GitHub webhooks and improve git reliability.
* Status page: [status.cto.new](http://status.cto.new).

# November 15th 2025

## Models

* Added auto-model selection.
* Haiku set as chat default for improved speed and tool calling.
* Tasks started from drafts use preferred model.

## Chat

* Optimistic send for chat messages.
* Cancel chat messages.
* 20k character message limit.

## UI/UX

* Git checkout command in task view.
* Fix chat text area resizing, mobile fixes, dark-mode tweaks.
* Surfaced secrets error messages.

## Auth and Invites

* Update invite eligibility to prevent abuse.
* Google sign-in restored.

## Reliability and Bugfixes

* Fix diff saving.
* Race fix on user/org creation.
* Validate env/secret format.
* Fix “ghost queued” tasks.

# October 31st 2025 🎃

## Chat & UX

* Fixed chat text area resize.
* Optimistic send - show user messages instantly.
* Chat summaries: agent can now reference last 10 chats.

## Models & Memory

* Added memory to chat agent.
* Improved chat label generation.
* Added Haiku, improved Anthropic prompt caching.

# October 29th 2025

## Tasks & Workflow

* Shorter draft titles.
* Chat agent now aware of tasks.

## Models & Execution

* Anthropic fully restored (incl. Alloy).
* Add GLM-4.6.
* Improve prompt caching.

## Abuse & Rate Limits

* 20k-char cap on first chat message.
* Domain blocks for obvious botting.
* Added CAPTCHA and bot blocks.

## Git & Repos

* Hardened git token fetching/retries.

## Reliability & Ops

* Removed legacy ticket plans/speculative mode; removed context7 MCP and Anthropic web\_search tool.
* Start routing tasks to Northflank for scalability.

## UI

* Dark mode.
* Text area resize fixes.

# October 22nd 2025

## Access & onboarding

* Invite UX: add invite button; generate all available codes.
* Team invites: invited team members no longer need codes.
* Sign-up protections to block bots.

## Draft tasks & task UX

* Prevent multiple tasks per draft.
* Save draft edits on start; show actionable controls only when valid.

## Models & routing

* Add AWS Bedrock for Anthropic model failover.
* Better labels & long-chat handling; include model name in system prompt.

## GitHub & repos

* Fix Start GitHub issue from @cto tag.
* Branch selector no longer crashes if branch deleted.

## Reliability & safety

* Fewer flaky runs: increase events timeout; harden Git token fetching/retries; empty-repo/default-branch fixes.
* Auto-ban abusive agent chat calls (unknown adapter/invalid schema).


# Repositories
Source: https://docs.cto.new/essentials/repos



Depending on the type of project you're working on, cto can connect to existing repos in GitHub or GitLab, create new repos in your own connected git accounts, or manage your repos for you without linking to a git provider.

## Task runner

Make sure to configure the task runner environment for connected repos. This is the virtual environment where the agent works on your code.

You can run system setup steps, install project dependencies, and define code checks steps. This allows [cto.new](http://cto.new) to do things like build, run, test, lint, and format your code.

<Note>
  Try the setup agent which can configure most of this for you
</Note>

Once you have completed setup, run a test so that you know everything works as it should. If you used the setup agent it will do this for you.

## Permissions

In order to create repos in your linked git account, cto needs admin permissions.


# Free Tier
Source: https://docs.cto.new/fair-use

Get the most out of cto for free

Use cto completely free. Get access to the best value models with generous usage limits that reset every day.

<Tip>
  Use auto router to automatically pick the best available model and maximise your usage
</Tip>

Hints to maximise your free use allowance:

* Assign well defined tasks and avoid including lots of unecessary context
* Use task appropriate models. Auto model router does this for you!

<Note>
  Switch to premium to get more out of cto
</Note>


# API Integrations
Source: https://docs.cto.new/integrations/API



API integrations have wide workflow compatibility with cto.new.

API in integrations can be used with [blank projects or connected codebases](/blank-project).

For example, you can trigger actions outside [cto](http://cto.new) inside tools you already use by assigning a task, adding a label, or tagging @cto.

[cto](http://cto.new) works with git:

* GitHub
* GitLab (legacy)

<Warning>
  We **strongly** recommend that you add branch protection rules whenever you allow AI to access to your codebase.
</Warning>

You can also connect with popular workflow tools.

* Linear
* GitHub issues
* Jira
* Trello
* Slack (notification only)


# MCP Integrations
Source: https://docs.cto.new/integrations/MCP



MCPs allow [cto](http://cto.new) to gather context and take action across a wide range of tools and services. You can interact with them from the [cto](http://cto.new) chat.

MCPs can be added from the chat sidebar.

* Sentry
* Cloudflare Observability
* Notion
* Neon
* Linear
* Prisma
* Render
* Webflow

We are adding new MCP integrations all the time!

## Custom MCPs

You can also add any custom local or remote MCP servers to the task runner's tool set. These MCPs will be availble to planning and coding agent sessions. Find this in your repository settings page.


# MCP Server
Source: https://docs.cto.new/integrations/cto-MCP

Connect to cto from other tools via MCP

## Functionality

The MCP server lets you access select cto.new functionality. Currently you can:

* List repos/projects configured with cto.new
* List tasks previously run (overview of 10 most recent tasks with status, PR, etc)
* Start a task (provide a prompt to start a remote task in cto.new)

<Warning>
  The MCP server is in beta
</Warning>

## Auth

Authentication is done via OAuth which your client must support. Clients with this support include:

* Cursor
* VSCode
* Claude

## Setup

Our MCP sever supports streamable HTTP transport only.

You can access the MCP server here:

`https://mcp.enginelabs.ai/mcp`

Here is an example `.cursor/mcp.json` file:

```
{
  "mcpServers": {
    "cto.new": {
      "url": "https://mcp.enginelabs.ai/mcp"
    }
  }
}
```

Our MCP server is remote only.

For clients that do not natively support OAuth with HTTP transport MCP servers, you can use the `mcp-remote` package to wrap the MCP server:

```
{
  "mcpServers": {
    "cto.new": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.enginelabs.ai/mcp"]
    }
  }
}
```


# Introducing cto
Source: https://docs.cto.new/introduction



[cto](http://cto.new) is an AI code agent that works with any code base or project.

cto runs on the best frontier LLMs and with all the tools you already use.

Just chat to start building.

<Check>
  You can use [cto.new](http://cto.new) for free forever!
</Check>

## About Engine Labs

Engine Labs is based in London and San Francisco building delightful AI powered tools for builders.

Engine Labs has achieved leading scores on SWE-Bench and Terminal Bench.


# Mobile App
Source: https://docs.cto.new/mobile-app



Mobile app projects are coming soon!


# OpenClaw
Source: https://docs.cto.new/open-claw



OpenClaw projects are coming soon!


# Premium
Source: https://docs.cto.new/pricing



Get more out of [cto](http://cto.new).

Premium users get loads more tokens, have access to a wider range of high-performance models and get no ads to build without distraction.

Plans have rolling 24 hour and 7 day usage limits. See plan details and upgrade at [cto.new/billing](https://cto.new/billing).

You can view token usage for any request in your account settings. Here's a guide for how much comparative usage you'll get with various models.

| **Model**                    | **Input /1M**        | **Cached input /1M**   | **Output /1M**         |
| :--------------------------- | :------------------- | :--------------------- | :--------------------- |
| OpenAI GPT-5.2 Codex         | \$1.75 / 175 credits | \$0.175 / 17.5 credits | \$14.00 / 1400 credits |
| Claude Opus 4.5              | \$5.00 / 500 credits | \$0.50 / 50 credits    | \$25.00 / 2500 credits |
| Claude Sonnet 4.6            | \$3.00 / 300 credits | \$0.30 / 30 credits    | \$15.00 / 1500 credits |
| Z GLM 4.7 (max price)        | \$0.60 / 60 credits  | \$0.11 / 11 credits    | \$2.20 / 220 credits   |
| Google Gemini 3 Pro (\<200K) | \$2.00 / 200 credits | \$0.20 / 20 credits    | \$12.00 / 1200 credits |
| Kimi K2.5                    | \$0.60 / 60 credits  | \$0.10 / 10 credits    | \$3.00 / 300 credits   |
| MiniMax M2.5                 | \$0.30 / 30 credits  | \$0.03 / 3 credits     | \$1.20 / 120 credits   |


# Your Data
Source: https://docs.cto.new/privacy



We're able to offer the most usage at every tier because we use anonymized user data for model training and other purposes.

Your data is never personally identifiable, and [cto.new](http://cto.new) is SOC 2 compliant.

Your secrets never leave cto.new and are encrypted in transit and at rest.

Your codebase always belongs to you and we do not train on any data that could be identified as IP. Your codebase is always private to you.

For more detailed information, refer to our terms of service.


# Environment Variables
Source: https://docs.cto.new/settings-config/env-vars

Add secure environment variables to cto.new's development environment

Environment variables can be added to cto.new for each repo you link.

<Info>
  Environment variables are encrypted at rest using 256-bit AES encryption and scrubbed from all logs
</Info>

You can add environment varibales individually, by copy and pasting a list, or by uploading a .env file.


# Models
Source: https://docs.cto.new/settings-config/models



cto.new works with the best frontier LLMs for chat and code generation.

Auto model automatically routes your task to the best frontier LLM, balancing performance, cost, speed, and capacity.

<Warning>
  Be prepared to experiment with settings when choosing your own model. Performance may vary.
</Warning>

cto.new supports:

* Claude Opus 4.5
* Claude Opus 4.6
* Claude Sonnet 4.6
* Devstral 2
* Gemini 3 Flash Preview
* Gemini 3 Pro Preview
* Gemini 3.1 Pro Preview
* GLM 4.7
* GLM 5
* GPT 5.2 Codex
* Grok 4.1 Fast
* Kimi K2.5
* MiniMax M2.5


# Prompt & Memory
Source: https://docs.cto.new/settings-config/prompt-memory



### System Prompt

The system prompt is automatically optimised for each repo.

You can re-run prompt optimisation from the prompt settings page. You might like to do this if, for example, you make substantial changes to your repo outside of cto.new.

You can manually update the system prompt. This can help if you add MCP servers or have specific requirements of cto.new for every task you assign.

### Memory

cto.new has long term memory for each repo it works on. This is added to the model's context alongside the system prompt for each task.

Memory is automatically maintained as you go. You can also edit it yourself.

The code writing agent decides to save bits of advice or guidance from comments in tickets and code reviews or as the agent works and learns about the codebase.


# Repository Settings
Source: https://docs.cto.new/settings-config/repo-settings

Description of your new file.

There are configuration options that can be set on a per repo basis, depending on project type.

### Default model

You can set the default model for planning and coding for each repo. This will be overriden if you explicitly choose a model for a particular task.

### Plan mode

Individual repos can be set to plan mode.

Plan mode adds a comment to issues assigned from workflow tools describing cto.new's planned implementation and any clarifying questions before writing any code.

### Setting the Base Branch

You can set the base branch for cto.new to work off for each repository in the repository settings page.


# Setup Agent
Source: https://docs.cto.new/settings-config/setup-agent

cto.new can attempt to configure its own environment

Using the setup Agent, cto can attempt to automatically configure and test its development environment for your repo.

The setup agent will run automatically when a new repo is connected and can be re-run from the repositories VM settings page.

<Warning>
  You may be required to edit the task runner setup!
</Warning>

This can take several minutes depending on the size and complexity of your repo and workflow.

Once the setup agent has finished it will test your configuration and fix any errors if required.


# Teams
Source: https://docs.cto.new/settings-config/teams



All users can add unlimited team members. Team members have access to all the same resources. Only chats are private for each user.

You can invite and manage team members from the team page in the cto.new app.

Contact us to update you organisation’s admin user and team name.


# Task Runner (VM)
Source: https://docs.cto.new/settings-config/vm

cto.new's development environment

For connected repos, cto.new works in a cloud virtual machine that we call a **'task runner'**.

Properly configuring the task runner with system setup, project dependencies, and code checks will significantly improve the agent's work.

<Check>
  cto.new can attempt to configure its own task runner using the setup agent
</Check>

cto.new will automatically resize your VM's memory to meet the needs of your project.

### System Setup

Install and configure software, tools, and packages required at the system level.

For example, this system setup configuration installs Node 18 and configures a database to run tests:

```[expandable] theme={null}
# Downgrade to Node v18
sudo apt-get remove -y nodejs && curl -fsSL https://deb.nodesource.com/setup_18.x | sudo bash - && sudo apt-get install -y nodejs

# Create test database
export PGPASSWORD=postgres && psql -U postgres -c "CREATE DATABASE test_db;"

# Run database migrations
npm run migrate
```

Every VM has the following base system specification by default.

<Accordion icon="notes" title="VM base specifications">
  ```
  ## Base Operating System

  - **Image**: `ubuntu:24.04` (default, configurable via `config.image`)
  - **Architecture**: follows `dpkg --print-architecture` (typically amd64)
  - **Environment variables at build**:
    - `DEBIAN_FRONTEND=noninteractive`
    - `CI=true`

  ## APT Packages

  Installed via `apt-get install -y` (from `config.ts`):

  | Package | Purpose |
  |---------|---------|
  | apt-utils | APT utilities |
  | bash-completion | Shell completion |
  | build-essential | gcc, g++, make |
  | ca-certificates | TLS certificates |
  | cmake | Build system |
  | curl | HTTP client |
  | dnsutils | dig, nslookup |
  | expect | Scripted interaction |
  | file | File type detection |
  | git | Version control |
  | gnupg | GPG for package verification |
  | htop | Process viewer |
  | iputils-ping | ping |
  | jq | JSON processor |
  | less | Pager |
  | libblas-dev | BLAS (linear algebra) |
  | libhdf5-dev | HDF5 scientific data |
  | liblapack-dev | LAPACK (linear algebra) |
  | libopenblas-dev | OpenBLAS |
  | libsqlite3-dev | SQLite development |
  | libssl-dev | OpenSSL development |
  | lsb-release | LSB release info |
  | lsof | List open files |
  | netcat-openbsd | netcat |
  | openssh-client | ssh, scp, sftp |
  | pkg-config | Package config |
  | procps | ps, top, etc. |
  | python3 | Python runtime |
  | python3-dev | Python headers |
  | python3-pip | pip |
  | python3-venv | venv |
  | ripgrep | rg |
  | rsync | File sync |
  | software-properties-common | add-apt-repository |
  | sqlite3 | SQLite CLI |
  | strace | System call tracer |
  | sudo | Privilege elevation |
  | tmux | Terminal multiplexer |
  | tree | Directory tree |
  | unzip | Unzip archives |
  | wget | HTTP downloader |

  ## Symlinks

  - `/usr/bin/python` → `/usr/bin/python3`

  ## Third-Party Software

  ### GitHub CLI (gh)

  - Source: https://cli.github.com/packages (official apt repo)
  - Installed via apt after adding keyring and sources.list entry

  ### Docker

  - Source: https://get.docker.com (official convenience script)
  - Includes: Docker Engine, CLI, containerd, Docker Compose plugin
  - `engine` user is in the `docker` group

  ### Node.js (via NVM)

  - Source: nvm-sh/nvm v0.40.2
  - Install: `nvm install --lts` (Node.js LTS)
  - Aliases: `default` → `lts/*`
  - Corepack: enabled with `yarn@stable` prepared

  ### Bun

  - Source: https://bun.sh/install
  - Install path: `/home/engine/.bun`

  ### UV (Python)

  - Source: https://astral.sh/uv/install.sh
  - Python package manager from Astral

  ### Playwright

  - CLI: `@playwright/cli@latest` (global npm)
  - Browser: Chromium
  - System deps: installed via `playwright install-deps chromium`
  - Skills: installed via `playwright-cli install --skills` in `/home/engine`

  ## User and Environment

  ### User

  - **Username**: `engine`
  - **Home**: `/home/engine`
  - **Shell**: `/bin/bash`
  - **Sudo**: passwordless (`NOPASSWD:ALL` in `/etc/sudoers.d/engine`)
  - **Groups**: `engine`, `docker`

  ### Environment Variables (engine user)

  | Variable | Value |
  |----------|-------|
  | HOME | /home/engine |
  | USER | engine |
  | SHELL | /bin/bash |
  | NVM_DIR | /home/engine/.nvm |
  | BUN_INSTALL | /home/engine/.bun |
  | PATH | /home/engine/.local/bin:/home/engine/.bun/bin:... |
  | PLAYWRIGHT_MCP_BROWSER | chromium |
  | WORKDIR | /home/engine |

  ## Directories

  | Path | Purpose |
  |------|---------|
  | /home/engine | User home, default WORKDIR |
  | /home/engine/project | Project directory |
  | /home/engine/.claude/skills | System skills (Playwright, Convex for vibe) |
  ```
</Accordion>

### Project Dependencies

Install repo specific dependencies like libraries, frameworks and packages.

For example, use npm to install project dependencies:

```[expandable] theme={null}
# Install deps
npm install
```

### Code Checks

Code checks are commands cto.new runs before committing your code, to ensure it passes and pre commit or pipeline steps.

Use code checks to lint, test and build your code, for example:

```[expandable] theme={null}
# Run lint
npm run lint

# Run build
npm run build

# Run tests
npm run test
```

### Task Runner Test

Run a test to verify your task runner is configured properly and cto.new can successfully make commits.

Running a test can take several minutes but can be manually stopped.

If your pipeline changes or you make any changes to cto.new's VM you should re-run the tests to ensure cto.new can work effectively.


# Workspace Settings
Source: https://docs.cto.new/settings-config/workspace-settings



These settings are applied across repos and workflows, depending on project type.

### Branch naming

You can configure the branch naming template.

cto.new provides several common variables you can include using handlebar notation.

### **Pull request configuration**

Configure how cto.new opens PRs, including commit message, title, and description by defining rules in natural language.

### Change Git Committer

By default, cto.new will commit as `cto-new` but you can change this from the git provider settings menu.

### Ignore git users

You can ignore git users (such as bots) meaning triggers from these users will not start new tasks.


# SOC 2
Source: https://docs.cto.new/soc2



[cto.new](http://cto.new) is SOC 2 type I and II compliant.

Details are available on our [trust page](https://trust.delve.co/engine-labs).


# Support
Source: https://docs.cto.new/support



The best way to get help is to on our Discord community!

<Tip>
  Join the [Discord](https://discord.gg/cto) community to connect and get help fast.
</Tip>

You can also reach out to us on Twitter [https://x.com/ctodotnew](https://x.com/ctodotnew) where we are always happy to help!

Email support is available at [support@enginelabs.ai](mailto:support@enginelabs.ai) but it may take a while to recieve a response.


# Web App
Source: https://docs.cto.new/web-app



Projects help you manage your work in cto.

They can include chat sessions, repositories, coding tasks and bits of infrastructure.

A web app project helps you build a web app fast.

Everything is configured automatically so you can start building, no experience required.

Get a built in preview of your running app alongside your chat session.

# Chat

Web app projects run a chat that can directly run commands and edit your code.

Chat has context across your whole codebase, all your infrastructure, and connected MCPs.

<Warning>
  Web apps do not yet support parallel chat sessions
</Warning>

# AI Apps

Every web app project comes with \$1 free in-app AI usage. You can add your own API key to get more.

We will soon offer automatic in-app AI usage top-ups.

# Stack

Web apps come with a pre configured stack optimised for building with AI.

### Convex

Web apps come with [Convex](https://www.convex.dev/) built-in.

Convex provides a database, auth, file storage, functions, scheduled tasks, logs, and more.

See Convex resources by selecting the Convex tab in the preview pane.

### TanStack

Under the hood, your app runs on TanStack.

# Deployment

Built in deployment is coming soon.

For now, you can try using the vercel MCP and Convex cloud to deploy your app.


