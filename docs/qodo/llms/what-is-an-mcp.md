# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/what-is-an-mcp.md

# What is an MCP?

MCP stands for **Model Context Protocol.** It's an open protocol that standardizes how tools and services expose structured context to AI models.

It defines a consistent way for applications to communicate with AI, making it easier to integrate external systems like version control, issue trackers, or shell environments into your workflow.

### How does Qodo use MCPs?

Qodo uses MCPs to let agents interact with your real tools and data safely, contextually, and intelligently.

For example, if a Jira MCP is configured, you can ask:

**“Find any Jira tickets about the authentication flow assigned to me.”**

The agent will query Jira directly and respond with filtered, relevant results—no copy-pasting or tab switching needed.

Common examples of MCPs include:

* Git, for version control operations
* Filesystem, for reading and editing code
* Shell, for running terminal commands
* Third-party services like GitHub, Jira, and CI/CD platforms.

MCPs are a core part of how [Qodo agents (modes and workflows)](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent) understand and act on your codebase and development environment.

### Learn More

You can learn more about MCPs in [Anthropic's MCP documentation](https://modelcontextprotocol.io/introduction).
