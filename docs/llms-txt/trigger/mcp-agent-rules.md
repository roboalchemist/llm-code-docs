# Source: https://trigger.dev/docs/mcp-agent-rules.md

# Agent rules

> Learn how to use the Trigger.dev agent rules with the MCP server

## What are Trigger.dev agent rules?

Trigger.dev agent rules are comprehensive instruction sets that guide AI assistants to write optimal Trigger.dev code. These rules ensure your AI assistant understands best practices, current APIs, and recommended patterns when working with Trigger.dev projects.

## Installation

Install the agent rules with the following command:

```bash  theme={null}
npx trigger.dev@latest install-rules
```

## Available rule sets

We provide five specialized rule sets, each optimized for different aspects of Trigger.dev development:

| Rule set            | Tokens | Description                                                                                  | GitHub                                                                                        |
| :------------------ | :----- | :------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Basic tasks**     | 1,200  | Essential rules for writing basic Trigger.dev tasks and fundamental patterns                 | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/basic-tasks.md)     |
| **Advanced tasks**  | 3,000  | Comprehensive rules for complex workflows, error handling, and advanced task patterns        | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/advanced-tasks.md)  |
| **Scheduled tasks** | 780    | Specialized guidance for cron jobs, scheduled workflows, and time-based triggers             | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/scheduled-tasks.md) |
| **Configuration**   | 1,900  | Complete guide for trigger.config.ts setup, environment configuration, and project structure | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/config.md)          |
| **Realtime**        | 1,700  | Using Trigger.dev Realtime features and frontend integration patterns                        | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/realtime.md)        |

## Claude Code subagent

For Claude Code users, we provide a subagent called `trigger-dev-expert` that's an expert at writing well-structured Trigger.dev code.

### Installation

The subagent is available as an option when running the rules installation command. Select "Claude Code" as your client and choose to include the subagent when prompted.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b7f4183abcbb79c59c90c237785698e6" alt="Claude Code subagent installation" data-og-width="1266" width="1266" data-og-height="453" height="453" data-path="images/claude-code-subagent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=12592c023c19a48eee359bd1183224f4 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=2795072f21c5476d692131c412f96e63 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fc4edc5a38551eb12ee4a648532789a2 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=84c3a2320c38582ddf77c63f0dfe0436 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=26e679c491757b7752fd5a32829d5c04 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/claude-code-subagent.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9f3a4c7f02920316780502de6b643449 2500w" />

### Usage

Activate the subagent in your prompts by requesting it explicitly:

```markdown  theme={null}
use the trigger-dev-expert subagent to create a trigger.dev job that accepts a video url, processes it with ffmpeg to extract the audio, runs the audio through a text-to-speech API like openai, and then uploads both the transcription and the audio to s3
```

The subagent works best when combined with the appropriate rule sets installed alongside it, providing both high-level architectural guidance and detailed implementation knowledge.

## Supported AI clients

The Trigger.dev rules work across a wide range of AI coding assistants and editors:

| Client              | Rule activation                                          | Docs                                                              |
| :------------------ | :------------------------------------------------------- | :---------------------------------------------------------------- |
| **Cursor**          | Automatic when working in trigger directories            | [Link](https://docs.cursor.com/en/context/rules#rules/)           |
| **Claude Code**     | Context-aware activation + custom subagent               | [Link](https://docs.anthropic.com/en/docs/claude-code)            |
| **VSCode Copilot**  | Integration with GitHub Copilot chat                     | [Link](https://code.visualstudio.com/docs/copilot/overview)       |
| **Windsurf**        | Automatic activation in Trigger.dev projects             | [Link](https://docs.windsurf.com/windsurf/cascade/memories#rules) |
| **Gemini CLI**      | Command-line integration                                 | [Link](https://ai.google.dev/gemini-api/docs)                     |
| **Cline**           | Automatic context detection                              | [Link](https://github.com/cline/cline)                            |
| **Sourcegraph AMP** | Code intelligence integration                            | [Link](https://sourcegraph.com/docs)                              |
| **Kilo**            | Custom rule integration                                  | [Link](https://kilocode.ai/docs/advanced-usage/custom-rules)      |
| **Ruler**           | Rule management                                          | [Link](https://github.com/intellectronica/ruler)                  |
| **AGENTS.md**       | Universal format for OpenAI Codex, Jules, OpenCode, etc. |                                                                   |

### Rule activation behavior

Different AI tools handle rules differently:

* **Automatic Activation**: Cursor, Windsurf, VSCode Copilot, and Cline automatically apply relevant rules when working in Trigger.dev projects or when `trigger.config.ts` is detected
* **Context-Aware**: Claude Code intelligently applies rules based on the current context and file types
* **Manual Integration**: AGENTS.md clients and others append rules to configuration files for manual activation

## Keeping rules updated

Trigger.dev rules are regularly updated to reflect new features, API changes, and best practices. The CLI includes automatic update detection.

### Automatic update notifications

When running `npx trigger.dev@latest dev`, you'll receive notifications when newer rule versions are available with a simple update command.

### Manual updates

Update rules anytime with:

```bash  theme={null}
npx trigger.dev@latest install-rules
```

The update process replaces existing rules without creating duplicates, keeping your configuration files clean and organized.

### Why updates matter

* **Current API patterns**: Access the latest Trigger.dev APIs and features
* **Performance optimizations**: Benefit from improved patterns and practices
* **Deprecated pattern avoidance**: Prevent AI assistants from generating outdated code
* **New feature support**: Immediate access to newly released capabilities

## Getting started

1. Install the rules:

```bash  theme={null}
npx trigger.dev@latest install-rules
```

2. Follow the prompts to install the rules for your AI client.

3. Consider installing the `trigger-dev-expert` subagent if using Claude Code.

## Next steps

* [Install the MCP server](/mcp-introduction) for complete Trigger.dev integration
* [Explore MCP tools](/mcp-tools) for project management and task execution
