# Source: https://docs.livekit.io/agents/logic.md

LiveKit docs › Logic & Structure › Overview

---

# Logic and structure overview

> Learn how to structure agent logic with sessions, workflows, tasks, tools, and other components for building voice AI applications.

## Overview

LiveKit Agents provides modular components for structuring agent logic into focused, maintainable units that perform accurately and consistently in complex real-world scenarios. Use sessions, workflows, tasks, and tools to break down agent behavior, enabling reliable production applications that handle nuanced conversations, multi-step processes, and external integrations with precision.

## Logic and structure components

Use core components to structure your agent logic, including sessions, workflows, customization points, and external integrations. Build simple single-agent applications, or combine these components for complex, multi-agent workflows.

| Component | Description | Use cases |
| **Agent sessions** | Orchestrate input collection, pipeline management, and output delivery. The main orchestrator for your voice AI app. | Single-agent apps, session lifecycle management, and room I/O configuration. |
| **Tasks & task groups** | Create focused, reusable units that perform specific objectives and return typed results. Tasks run inside agents and take temporary control until completion. | Consent collection, structured data capture, and multi-step processes with task groups. |
| **Workflows** | Model repeatable patterns with agents, handoffs, and tasks for complex voice AI systems. | Multi-persona systems, conversation phase management, and specialized agent routing. |
| **Tool definition & use** | Extend agent capabilities with custom functions callable by the LLM for external actions and data access. | API integrations, frontend RPC calls, and triggering agent handoffs. |
| **Pipeline nodes & hooks** | Customize agent behavior at pipeline processing points with custom STT, LLM, TTS, and lifecycle hooks. Override nodes to modify input, output, or add custom logic. | Custom providers, output modification, and pronunciation control. |
| **Turn detection & interruptions** | Manage conversation flow with turn detection, interruption handling, and manual turn control. | Natural conversation timing, interruption management, and push-to-talk interfaces. |
| **Agents & handoffs** | Define distinct reasoning behaviors and transfer control between agents when different capabilities are needed. | Role-based agents, model specialization, and permission management. |
| **External data & RAG** | Connect agents to external data sources, databases, and APIs for RAG and data operations. Load initial context, perform RAG lookups, and integrate with external services. | Knowledge base search, user profile loading, and database operations. |

## In this section

Read more about each component.

- **[Agent sessions](https://docs.livekit.io/agents/logic/sessions.md)**: Main orchestrator for input collection, pipeline management, and output delivery.

- **[Tasks & task groups](https://docs.livekit.io/agents/logic/tasks.md)**: Focused units that perform specific objectives and return typed results.

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Model repeatable patterns with agents, handoffs, and tasks.

- **[Tool definition & use](https://docs.livekit.io/agents/logic/tools.md)**: Custom functions callable by the LLM for external actions.

- **[Pipeline nodes & hooks](https://docs.livekit.io/agents/logic/nodes.md)**: Customize behavior at pipeline processing points.

- **[Turn detection & interruptions](https://docs.livekit.io/agents/logic/turns.md)**: Manage conversation flow with turn detection and interruption handling.

- **[Agents & handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)**: Define distinct agents and transfer control between them.

- **[External data & RAG](https://docs.livekit.io/agents/logic/external-data.md)**: Connect to external data sources, databases, and APIs.

---

This document was rendered at 2025-12-31T18:29:33.179Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic.md](https://docs.livekit.io/agents/logic.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).