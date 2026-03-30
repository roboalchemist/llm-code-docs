# Predictive state updates

Stream in-progress agent state updates to the frontend.

This video shows the [coagents starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter) repo with the [implementation](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#implementation) section applied to it!

## [What is this?](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#what-is-this)

A LangGraph agent's state updates discontinuosly; only across node transitions in the graph.
But even a _single node_ in the graph often takes many seconds to run and contain sub-steps of interest to the user.

**Agent-native applications** reflect to the end-user what the agent is doing **as continuously possible.**

CopilotKit enables this through its concept of **_predictive state updates_**.

## [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#when-should-i-use-this)

You can use this when you want to provide the user with feedback about what your agent is doing, specifically to:

- **Keep users engaged** by avoiding long loading indicators
- **Build trust** by demonstrating what the agent is working on
- Enable **agent steering** \- allowing users to course-correct the agent if needed

## [Important Note](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#important-note)

When a node in your LangGraph finishes executing, **its returned state becomes the single source of truth**. While intermediate state updates are great for real-time feedback, any changes you want to persist must be explicitly included in the node's final returned state. Otherwise, they will be overwritten when the node completes.

## [Implementation](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#implementation)

### [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#install-the-copilotkit-sdk)

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic
experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

Poetrypipconda

```
poetry add copilotkit