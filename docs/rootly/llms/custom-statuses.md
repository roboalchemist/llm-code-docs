# Source: https://docs.rootly.com/configuration/custom-statuses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Statuses

> Define custom incident lifecycle stages beyond the default Active, Mitigated, and Resolved statuses to match your organization's response processes.

Custom Statuses allow you to fully customize the statuses that represent your incident's lifecycles. By default, Rootly incidents progress through Active > Mitigated > Resolved. However, some organizations have much more granular statuses to represent key moments in the incident's lifecycle.

Custom Statuses allow you to add, reorder, and capture key information on the incident throughout the incident lifecycle.

# Adding and editing statuses

Navigate to **Configuration > Lifecycle** to begin customizing your Rootly statuses.

Each substatus requires a name and description to give your responders context on what the lifecycle stage represents. When an incident's status is updated to reflect a new status, we will mark the date and time of the status change and store it in the status' `Marked At` field to support any postmortem analyses.

When a new status is added, Rootly will generate a new substatus form for you to customize in the Form configuration section. This allows you to capture incident data at any phase of the incident's lifecycle.

# Lifecycle preferences

Rootly gives you full control over how your incidents progress through the Lifecycle statuses. Control if your responders are able to move an incident across many statuses at once, or if incidents must progress through every status in a defined order.

Navigate to **Configuration > Lifecycle > Preferences** to update these settings.

<img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/configuration/custom-lifecycle-preferences.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=9b363d90a7d6c8f56b949941f19cd098" alt="Clean Shot2025 04 14at12 10 46@2x Pn" width="1780" height="790" data-path="images/configuration/custom-lifecycle-preferences.webp" />

If your Rootly instance requires incidents to progress through Active or Resolved in order, your responders will only be able to update the incident's status to the next status defined in your Lifecycle configuration.

**Note:** Responders are able to move an incident backward to any previous status. If they do so, they'll have to progress the incident through each status again.

Get started with Custom Statuses by reaching out to your Rootly account representative today.


Built with [Mintlify](https://mintlify.com).