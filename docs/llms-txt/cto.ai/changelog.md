# Source: https://docs.cto.new/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cto.new/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

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


Built with [Mintlify](https://mintlify.com).