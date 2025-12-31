# Source: https://docs.warp.dev/agents/using-agents/agent-context.md

# Agent Context

In Warp, you can pass different types of input directly to the Agent to guide its behavior and improve response quality. These inputs are known as **Agent Context**: ad-hoc pieces of information you manually supply during a session.

**You can attach context in several ways:**

* [blocks-as-context](https://docs.warp.dev/agents/using-agents/agent-context/blocks-as-context "mention") - share output from your terminal to help the Agent understand errors, logs, or previous commands.
* [images-as-context](https://docs.warp.dev/agents/using-agents/agent-context/images-as-context "mention") - include screenshots, diagrams, or other visuals to provide additional clarity.
* [urls-as-context](https://docs.warp.dev/agents/using-agents/agent-context/urls-as-context "mention") - attach public webpages so the Agent can extract and reference their content.
* [selection-as-context](https://docs.warp.dev/agents/using-agents/agent-context/selection-as-context "mention") - attach code snippets from the editor or review panel to enrich your prompts with precise context.
* [using-to-add-context](https://docs.warp.dev/agents/using-agents/agent-context/using-to-add-context "mention") - reference files, folders, code symbols, or Warp Drive objects directly in your prompts.

***

This is distinct from other persistent or automatic sources of context, such as [rules](https://docs.warp.dev/knowledge-and-collaboration/rules "mention"), [warp-drive-as-agent-mode-context](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/warp-drive-as-agent-mode-context "mention"), and [mcp](https://docs.warp.dev/knowledge-and-collaboration/mcp "mention"), which the Agent also uses when available.
