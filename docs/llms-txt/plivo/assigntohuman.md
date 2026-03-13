# Source: https://plivo.com/docs/aiagent/human/assigntohuman.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Assign to Human

> Transfer conversations from AI to human agents

The **Assign to Human** node lets you transition a conversation from an AI Agent to a human specialist at the right moment in the flow. It’s one of the most powerful tools for implementing hybrid automation—blending AI efficiency with human empathy and expertise.

Whether the customer is stuck, asking for a live agent, or reaching a decision point, this node helps route the conversation to the appropriate person or team using configurable logic.

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/assigntohuman.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=6cfaf1ce4fca7f28ce958b07fb2ae61a" width="2352" height="984" data-path="aiagent/images/assigntohuman.png" />
</Frame>

## Key Use Cases

* Escalate complex queries from AI to support agents
* Route premium leads directly to sales teams
* Distribute tasks like call scheduling or follow-ups to the right queue

## Configuration Options

### 1. **Assign To**

Choose the destination for the handoff:

* **Agent**: Directly assign to specific agents from your team.
* **Team**: Route to all available members of a defined team.
* **Variable**: Use flow logic to dynamically assign based on context or data.

You can select multiple agents or teams if you want to broaden eligibility.

### 2. **Queue**

Select a **Queue** that defines the routing logic, agent capacity, and channel-specific behavior. This ensures structured handoff with fallback, idle balancing, and assignment control.

*Note: A Queue must be created and configured prior to use in this step.*

### 3. **Skill Filter (Optional)**

Apply one or more skill filters to ensure only agents with relevant expertise are considered for assignment (e.g., "Spanish", "Product Support", or "Tier 2").

## Advanced Settings

Expand the **Advanced Settings** section to fine-tune assignment behavior:

* **Routing Strategy**\
  Choose how agents are prioritized for assignment:
* **Simultaneous Conversation Recipients**\
  Number of agents to offer the conversation to at once. Useful for fast assignment.
* **Conversation Assignment Retry**\
  Retry count if initial assignment fails or times out.
* **Sticky Routing**\
  Retain the same agent for repeat conversations from the same user
* **Sticky Routing Expiry**\
  Set how long (in days) the sticky routing remains active. You can also set to *No Expiry*. |

## Example Scenario

You have a flow that handles support chats. If the customer types “talk to someone,” the AI Agent routes them to a Queue using the **Assign to Human** node. You configure:

* Routing strategy: *Highest Idle Time*
* Max 3 agents to receive it simultaneously
* Retry if no agent picks up
* Sticky routing for 1 day

This ensures:

* A quick assignment to an available agent
* Return users are routed to the same specialist
* No overload on a single agent
