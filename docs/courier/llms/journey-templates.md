# Source: https://www.courier.com/docs/platform/journeys/journey-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Journey Templates

> Create and edit notification templates scoped to a journey. Journey templates are distinct from regular Courier templates and live exclusively within the journey where they're created.

Every [send node](/platform/journeys/channels) in a journey is linked to a **journey template** that defines the notification content. Journey templates are created and edited directly inside the journey editor; they are scoped to the journey where they're created and are not shared with other journeys or accessible from regular Courier sends.

<Note>
  Journey templates are separate from templates you create in the Courier template designer (the ones used with the Send API). You cannot reference a journey template from a regular send, and you cannot import an existing template into a journey. Each journey manages its own set of templates.
</Note>

## Creating a Template

When you add a send node and select a channel, click **+ Create** to provision a new message template. Courier creates the template, links it to the send node, and opens the template designer in a full-screen overlay.

<Frame caption="The inline template designer opened from a send node, showing the email content editor">
  <img src="https://mintcdn.com/courier-4f1f25dc/Dtl1DGeq8V31J3OW/assets/platform/journeys/inline-template-designer.png?fit=max&auto=format&n=Dtl1DGeq8V31J3OW&q=85&s=25418b6444cbcc0e7aac6e5b41469f0f" width="3452" height="1920" data-path="assets/platform/journeys/inline-template-designer.png" />
</Frame>

The template starts as a blank draft titled "Untitled." You can rename it, add content blocks, and use variables from your journey's data context.

## Editing a Template

To edit an existing template, click **Edit** in the send node's configuration panel. The template designer opens in the same full-screen overlay, and any changes are saved to the template's draft.

Templates are versioned alongside the journey. When you publish the journey, the current draft of each linked template becomes the active version.

## Using Variables

Templates can reference any data available in the journey context using double-brace syntax: `{{variable_name}}`. Available variables include:

* **Trigger schema fields** defined on the API trigger (e.g., `{{order_id}}`, `{{order_total}}`)
* **Profile fields** from the user's stored profile or the invocation payload (e.g., `{{first_name}}`, `{{email}}`)
* **Fetch response fields** from upstream [fetch data](/platform/journeys/nodes/fetch-data) nodes

The template designer shows a list of available fields so you don't need to remember field names.

## Template Lifecycle

| State         | Description                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| **Draft**     | Created when you click "+ Create." Editable in the designer. Not yet active. |
| **Published** | Becomes active when you publish the journey. Used for all new invocations.   |

Templates follow the same publish cycle as the journey itself. Editing a template after publishing creates a new draft; you need to re-publish the journey for changes to take effect.

Existing runs in progress continue using the template version that was active when the run started.

## What's Next

<CardGroup cols={2}>
  <Card title="Channels & Send" href="/platform/journeys/channels" icon="paper-plane">
    Configure recipients, conditions, and send windows
  </Card>

  <Card title="Starting a Journey" href="/platform/journeys/invocation" icon="bolt">
    Set up triggers and invoke journeys
  </Card>

  <Card title="Building Your Journey" href="/platform/journeys/building-journeys" icon="arrow-progress">
    Add branching, delays, and data enrichment
  </Card>

  <Card title="Version History" href="/platform/journeys/version-history" icon="clock-rotate-left">
    Track changes and revert to previous versions
  </Card>
</CardGroup>
