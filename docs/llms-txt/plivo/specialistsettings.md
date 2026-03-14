# Source: https://plivo.com/docs/aiagent/human/specialistsettings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Human Specialist Settings

> Optimize how human specialists handle conversations across various channels.

**Human Specialist Settings** allow you to control key aspects of agent capacity, availability, and the rules that govern how incoming tasks and conversations are assigned. These settings help ensure agents are not overloaded and that conversations are routed efficiently based on their real-time status and workload.

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/humansettings.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=c49da577c629d980b9cc3690a40ad180" width="1138" height="1374" data-path="aiagent/images/humansettings.png" />
</Frame>

## Key Settings

### **Agent Reservation**

**Agent Reservation** defines the duration for which a contact assignment request is shown to an agent. If the agent does not respond within the specified time, the system will either move the request to another available agent or handle it in another way.

These timeouts can be customized per channel, allowing you to adjust the duration based on the type of interaction and expected response times.

### **Agent Capacity**

**Agent Capacity** controls the maximum number of concurrent interactions an agent can handle across different channels. This prevents agents from becoming overwhelmed and ensures a balanced workload.

You can configure how many calls, chats, messages, or tasks an agent can manage at once for each channel. Additionally, you can enable the **Release Agent Capacity during ACW** (After Contact Work), which frees up the agent’s capacity once a conversation is completed.

### **Sticky Routing**

**Sticky Routing** ensures that once an agent is assigned a conversation, they will remain the primary point of contact for that customer, even for follow-up interactions.

* **Enable Agent Stickiness based on Outbound Conversations**: When enabled, any follow-up (e.g., callback or message) is routed to the same agent who handled the initial contact.
* **Expiry of Outbound Agent Information**: You can set how long the agent's assignment data will persist (e.g., for a specific number of days or with **No Expiry** if you prefer to keep the agent assigned indefinitely).

## Example Use Case

For example, if you have agents handling multiple channels:

* Agents can handle several live chats and messages at once.
* Once a call is completed, the system can release the agent’s capacity, allowing them to pick up new tasks like chats or messages.

If a customer returns for a follow-up conversation, **Sticky Routing** ensures they are directed to the same agent who initially handled their case, ensuring continuity and context.

***
