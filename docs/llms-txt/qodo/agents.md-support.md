# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/agents.md-support.md

# AGENTS.md Support

Qodo automatically detects and reads an **AGENTS.md** file in your repository as part of the project context.\
This file helps guide the agent’s behavior — for example, defining build and test commands, coding conventions, or project-specific instructions.

If your project contains multiple `AGENTS.md` files (e.g., in a monorepo), Qodo will use the one closest to the file or folder you’re working with.

The format and purpose of this file follow the open standard described at [**agents.md**](https://agents.md/?utm_source=chatgpt.com).

> 💡 Tip: You can use AGENTS.md to share best practices, style guides, or testing rules so every agent working in your project behaves consistently.
