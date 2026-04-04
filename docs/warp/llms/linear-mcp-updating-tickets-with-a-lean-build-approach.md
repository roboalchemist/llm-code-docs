# Source: https://docs.warp.dev/university/mcp-servers/linear-mcp-updating-tickets-with-a-lean-build-approach.md

# Linear MCP: Updating Tickets with a Lean Build Approach

Learn how to use Warp’s Linear MCP integration to update tickets programmatically while maintaining a lean build strategy.

{% embed url="<https://www.youtube.com/watch?v=hqleW6jDCbY>" %}

***

## Overview

This walkthrough demonstrates:

* Updating Linear tickets via Warp’s MCP integration
* Structuring tasks around a lean development stack
* Observing real-time synchronization of ticket data
* Testing agent autonomy when editing related subtasks

{% stepper %}
{% step %}
**Setting Up the Scenario**

The goal is to use Warp’s agent to update a Linear epic with a new, leaner build approach and reflect the changes in related subtasks.

First, open your Linear project and locate the target epic.\
Copy the **ticket ID** (e.g. “Empty Studio 36”).
{% endstep %}

{% step %}
**Define the Update Prompt**

Within Warp, run the MCP command to edit the Linear issue.

**Prompt**

{% code title="Prompt" overflow="wrap" %}

```
Use the warp-server-staging gcloud project and pull logs for the last 10 minutes from the warp-server Cloud Run instance.
Organize them by info, warning, and error levels.
Create a histogram across message types, and highlight the most concerning errors to investigate.
```

{% endcode %}

Warp parses the issue context and updates the ticket’s fields accordingly.
{% endstep %}

{% step %}
**Observing the Changes**

After execution:

* The Linear ticket reflects the new **Next.js + Supabase** stack.
* Tasks like *Build Foundation*, *Implement AI-powered PRD Generation*, and *Set up Development Environment* are updated.
* Time estimates automatically adjust from *4–6 weeks* to *2–3 weeks*.
* Complex integrations (AI and Linear App) are deferred to a future phase.
  {% endstep %}

{% step %}
**Propagating Updates to Child Tasks**

Warp’s agent can cascade changes to linked subtasks.\
If it begins editing other epics unexpectedly, you can constrain its scope by specifying task IDs in the prompt:

{% code title="Scope Constraint" %}

```
Only update the ticket with ID <ticket_number>.
Do not modify other epics or related tickets.
```

{% endcode %}
{% endstep %}

{% step %}
**Review and Verification**

Re-open the Linear epic to confirm updates:

* **Frontend specs** reflect the lean stack.
* **Child tasks** align with phase 1 deliverables.
* **Deferred features** (e.g., advanced integrations) are pushed to phase 2.

{% hint style="info" %}
This demonstrates Warp’s ability to *maintain and modify tickets intelligently*, not just create them.
{% endhint %}
{% endstep %}
{% endstepper %}
