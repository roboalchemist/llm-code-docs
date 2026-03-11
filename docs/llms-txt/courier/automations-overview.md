# Source: https://www.courier.com/docs/platform/automations/automations-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automation Overview

> Courier's automation engine for building notification workflows with triggers, actions, batching, digests, and conditional logic.

Courier's automation engine lets you build notification workflows that go beyond simple message delivery. Create sequences that adapt to user behavior, batch notifications, coordinate across channels, and implement business logic.

## When to Use Automations

If you're sending straightforward transactional messages, you don't need automations. The [Send API](/platform/sending/send-message) handles rendering, routing, preferences, and delivery in a single call, and that's the right choice for most notifications.

Automations are for when your notification logic involves:

* **Timing** - delays, scheduled delivery, or waiting for business hours
* **Sequences** - multi-step flows like onboarding or reminder chains
* **Batching and digests** - grouping events into a single notification
* **Conditional logic** - branching based on user data, delivery status, or external conditions
* **Cancellation** - aborting a flow when conditions change (e.g., user completes the action before a reminder fires)

Automations use the same templates, users, and preferences as direct sends. Moving a notification into an automation doesn't require changing your content or user setup. See [Choose a Sending Strategy](/platform/sending/choosing-your-sending-strategy) for a full comparison.

## Automation Components

Automations are built from three types of nodes: **triggers** that start workflows, **actions** that perform tasks, and **control flow** that adds logic.

### Trigger Nodes

Triggers define how an automation starts. Every automation has one entry point.

| Trigger           | Description                                                                     |
| ----------------- | ------------------------------------------------------------------------------- |
| **API Invoke**    | Start via `POST /automations/:template_id/invoke`. Default trigger type.        |
| **Schedule**      | Run at specific times using cron expressions, recurrence rules, or fixed dates. |
| **Segment**       | React to Segment `identify`, `group`, or `track` events.                        |
| **Audience**      | Fire when users match or unmatch an audience.                                   |
| **Inbound Event** | Respond to events from connected sources.                                       |
| **Webhook**       | Start from external webhook calls.                                              |
| **Digest**        | Release accumulated digest events on schedule.                                  |

See [Webhook Trigger](/platform/automations/webhook-trigger), [Scheduling](/platform/automations/scheduling), and [Segment Integration](/platform/automations/segment) for configuration details.

### Action Nodes

Actions perform tasks in your workflow.

| Action             | Description                                                    |
| ------------------ | -------------------------------------------------------------- |
| **Send**           | Deliver a notification to a user via any channel.              |
| **Send to List**   | Send to all subscribers of a Courier list.                     |
| **Delay**          | Pause execution for a duration or until a specific time.       |
| **Fetch Data**     | Make HTTP requests and merge response into automation context. |
| **Update Profile** | Modify a user's Courier profile.                               |
| **Get Profile**    | Load a user profile into the automation context.               |
| **Invoke**         | Call another automation template.                              |
| **Cancel**         | Cancel a running automation by its cancellation token.         |
| **Add to Batch**   | Accumulate events for batched delivery.                        |
| **Add to Digest**  | Add events to a user's digest.                                 |
| **Throttle**       | Rate-limit notifications per user or globally.                 |

See [Steps](/platform/automations/steps), [Batching](/platform/automations/batching), and [Digests](/platform/automations/digest) for details.

### Control Flow Nodes

Control flow adds conditional logic and branching.

| Node       | Description                                                |
| ---------- | ---------------------------------------------------------- |
| **If**     | Branch based on a single condition (true/false paths).     |
| **Switch** | Route to the first matching condition from multiple cases. |
| **Branch** | Multi-path routing with condition groups (V3).             |

Conditions can evaluate:

* **Data** fields from the automation context
* **Profile** fields from the user profile
* **Step Ref** status of previous send steps (e.g., `CLICKED`, `DELIVERED`)
* **JS Expression** for complex logic

See [If / Switch](/platform/automations/control-flow) for operators and examples.

## Common Use Cases

### User Onboarding

Create onboarding sequences that adapt to user progress:

1. Send welcome email immediately after signup
2. Wait 24 hours, then check if user completed first action
3. If not, send a reminder via push notification
4. If completed, send a congratulations message

### Batched Activity Notifications

Reduce notification fatigue by batching activity:

1. Collect events (likes, comments, mentions) as they occur
2. After 1 hour of inactivity (or max 24 hours), release the batch
3. Send a single notification summarizing all activity

See [Batching](/platform/automations/batching) for configuration.

### Scheduled Digests

Send periodic summaries to users:

1. Configure a digest schedule in [Preferences Editor](https://app.courier.com/settings/preferences)
2. Add events to the digest throughout the period
3. Automation triggers at schedule time with accumulated events
4. Send personalized digest notification

See [Digests](/platform/automations/digest) for setup.

### Agent-Human Collaboration

Build human-in-the-loop patterns for AI agents and automated systems:

1. Agent triggers an automation requesting human approval
2. Send an actionable notification to Inbox (approve/reject buttons)
3. Wait for user response via webhook or inbound event
4. Branch on the response: proceed, escalate, or cancel

The same pattern works for escalation with timeouts (delay, check delivery status via step ref, escalate if no response) and confirmation flows. Automations provide the timing, branching, and cancellation logic; the Send API and Inbox handle the human interaction.

## Getting Started

1. Navigate to [Automations](https://app.courier.com/automations) in the Courier app
2. Click **New Automation** to create a template
3. Add a trigger node to define how the automation starts
4. Add action nodes for each step in your workflow
5. Add control flow for conditional logic
6. **Publish** the automation to activate it
7. Invoke via API or wait for trigger conditions

For the visual designer interface, see [Designer](/platform/automations/designer).

## Next Steps

<CardGroup cols={2}>
  <Card title="Designer" href="/platform/automations/designer" icon="pen-ruler">
    Build workflows visually
  </Card>

  <Card title="Steps Reference" href="/platform/automations/steps" icon="list">
    All automation actions
  </Card>

  <Card title="Batching" href="/platform/automations/batching" icon="layer-group">
    Group notifications
  </Card>

  <Card title="Digests" href="/platform/automations/digest" icon="calendar">
    Scheduled summaries
  </Card>
</CardGroup>
