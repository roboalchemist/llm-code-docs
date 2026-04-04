# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.transfer.md

# Agent.transfer

**Syntax**:

Agent.transfer();

**Example**: To display a message in the agent after an agent transfer:

Agent.transfer();

return "Transferring to Agent" ;

{% hint style="info" %}
**Notes**: When you are using Agent.transfer() in JS node to transfer to a live agent, then

* It gives you enhanced control of when to transfer to a live agent and what must be done once the transfer is completed.&#x20;
* Since it gives you more flexibility, you can set conditions required before transferring to a live agent. Hence, working hours set in the Live agent page is no longer applicable. If any working hours is required before transferring to a live agent, it must be handled within the JS code itself before using Agent.transfer().
  {% endhint %}

See [Live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent), for more information on how to transfer to a live agent in the UI.
