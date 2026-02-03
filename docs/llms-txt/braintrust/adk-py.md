# Source: https://braintrust.dev/docs/reference/integrations/adk-py/0.2.4/adk-py.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google ADK Integration

> Braintrust integration for Google ADK v0.2.4

The `braintrust-adk` package provides automatic tracing for Google ADK agents, runners, flows, and MCP tools.

## Installation

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust-adk
```

## Quick start

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust_adk import setup_adk

# Automatically patch all ADK components
setup_adk(project_name="my-project")
```

## API Reference

### setup\_adk

Setup Braintrust integration with Google ADK. Will automatically patch Google ADK agents, runners, flows, and MCP tools for automatic tracing.

### wrap\_mcp\_tool

Wrap McpTool to trace MCP tool invocations.

## Source Code

For the complete source code and additional examples, visit the [braintrust-sdk repository](https://github.com/braintrustdata/braintrust-sdk/tree/main/integrations/adk-py).
