# Source: https://docs.warp.dev/agent-platform/agent/using-agents/agent-context.md

# Agent Context

In Warp, you can pass different types of input directly to the Agent to guide its behavior and improve response quality. These inputs are known as **Agent Context**: ad-hoc pieces of information you manually supply during a session.

**You can attach context in several ways:**

* [Blocks as Context](https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/blocks-as-context) - share output from your terminal to help the Agent understand errors, logs, or previous commands.
* [Images as Context](https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/images-as-context) - include screenshots, diagrams, or other visuals to provide additional clarity.
* [URLs as Context](https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/urls-as-context) - attach public webpages so the Agent can extract and reference their content.
* [Selection as Context](https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/selection-as-context) - attach code snippets from the editor or review panel to enrich your prompts with precise context.
* [Using @ to Add Context](https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/using-to-add-context) - reference files, folders, code symbols, or Warp Drive objects directly in your prompts.

***

This is distinct from other persistent or automatic sources of context, such as [Rules](https://docs.warp.dev/knowledge-and-collaboration/rules), [Warp Drive as Agent Mode Context](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/warp-drive-as-agent-mode-context), and [Model Context Protocol (MCP)](https://docs.warp.dev/knowledge-and-collaboration/mcp), which the Agent also uses when available.
