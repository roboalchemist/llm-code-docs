# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/logics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Logics

> Logic Nodes enable you to control the flow of a conversation by defining conditions

**Logic Nodes** are essential for building dynamic and intelligent workflows in your AI agent. These nodes allow you to set rules for how conversations progress based on user input, agent responses, or specific conditions, giving you complete control over the conversational flow.

## Types of Logic Nodes

### 1. **Rule Branching Node**

The Rule Branching Node enables you to define multiple conditions and determine which path the flow will take based on whether specific criteria are met.

**Configuration Options**:

* **Conditions**: Define conditions based on user input, agent responses, or variables in the conversation.
* **Pathways**: Create different paths for the flow, determining how the conversation will progress depending on whether the conditions are met.

**Use Case**:\
If a customer asks for product details, route them to the product information flow. If they ask for support, direct them to the support team instead.

### 2. **Counter Node**

The **Counter Node** tracks the number of times a path is taken or a condition is met during a conversation. This node doesn't impact the conversation flow but is useful for analytics or triggering actions based on the count.

**Configuration Options**:

* **Counter Variable**: Define a variable to keep track of the count.
* **Condition**: Set conditions that will increment the counter each time they are met (e.g., if the user asks a specific question multiple times).

**Use Case**:\
Track how many times a user asks about a specific product feature and use this data to adjust your agent’s responses or trigger follow-up actions after a certain threshold.
