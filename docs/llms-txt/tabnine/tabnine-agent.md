# Source: https://docs.tabnine.com/main/getting-started/tabnine-agent.md

# Tabnine Agent

{% hint style="success" %}
Tabnine Agent is currently available for Visual Studio Code, Visual Studio 2022/2026 and all JetBrains IDEs.\
\
It is not available for Eclipse.
{% endhint %}

## Introduction

**Tabnine Agent** extends the capabilities of Tabnine beyond inline code completion and conversational chat by introducing an **autonomous, task-oriented AI assistant** that can act directly within the developer’s environment.

Unlike Tabnine Chat, which provides on-demand natural language conversations with underlying models (such as explaining code, generating snippets, or answering documentation queries), **Tabnine Agent** **operates autonomously to achieve the user’s specified goal** and can perform higher-order development tasks. These tasks can include codebase-wide refactoring, automated test generation, documentation synthesis, and policy validation.

### What is Tabnine Agent?

Tabnine Agent can be seen as an initiative-enhanced version of Tabnine Chat. On top of that, Tabnine Agent adds and explains more of its reasoning to the user.

Unlike other agentic approaches, Tabnine Agent maintains a tight feedback loop with the developer. It independently determines when to check in for input or approval, such as requesting to *Proceed* with a complex agentic workflow.

This ensures that the agent remains aligned with user intent and minimizes introducing redundant or conflicting code within large, enterprise codebases.

Agent will take into account the current state of a project as well as context to make its decisions. It will in turn respond to state changes, take dependencies into account, break down complex tasks for better processing (and clearer explanations to users), and respond to user feedback to make project code edits.
