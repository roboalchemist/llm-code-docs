# Source: https://humanloop.com/docs/sdk/decorators.md

# Decorators Overview

> Overview of the decorator system in the Humanloop SDK


## Introduction

Humanloop provides a set of decorators that help you instrument your AI features with minimal code changes. These decorators automatically create and manage Logs on the Humanloop platform, enabling monitoring, evaluation, and improvement of your AI applications.

| Decorator | Purpose | Creates | Documentation |
|-----------|---------|---------|---------------|
| `prompt` | Instrument LLM provider calls | Prompt Logs | [Learn more â](/docs/v5/sdk/decorators/prompt) |
| `tool` | Define function calling tools | Tool Logs | [Learn more â](/docs/v5/sdk/decorators/tool) |
| `flow` | Trace multi-step AI features | Flow Log with traces | [Learn more â](/docs/v5/sdk/decorators/flow) |

## Common Patterns

All decorators share these common characteristics:

- **Path-based organization**: Each decorator requires a `path` parameter that determines where the File and its Logs are stored in your Humanloop workspace.
- **Automatic versioning**: Changes to the decorated function or its parameters create new versions of the File.
- **Error handling**: Errors are caught and logged, making debugging easier.
- **Minimal code changes**: Decorate existing code and adopt the Humanloop SDK gradually.
