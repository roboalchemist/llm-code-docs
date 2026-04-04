# Source: https://www.courier.com/docs/platform/journeys/journeys-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Journeys Overview

> Build customer messaging experiences with a visual workflow editor, typed data contracts, and step-by-step run inspection.

Journeys give you a visual, opinionated interface for building customer messaging experiences. Define your data contract, design your workflow, and let Courier handle the execution logic; timing, branching, enrichment, and delivery across every channel.

You define the shape of the data your journey expects. Courier uses that contract to power autofill and variable hints throughout the editor, and makes the data available to every node in the workflow. When something goes wrong, you can step through an individual run against real production data and see exactly what happened at every node.

## How Journeys Work

A journey is a directed graph of nodes that executes when triggered. You build it visually in the journey editor, publish it, and invoke it from your application or an event stream.

<p align="center"><strong>Trigger → Node → Node → Node → ...</strong></p>

Every journey starts with a **trigger** that defines how users enter the workflow. From there, nodes execute in sequence. Branch nodes can split the flow into multiple paths. The journey continues until all paths reach their end.

## Core Concepts

<CardGroup cols={3}>
  <Card title="Send Node" href="/platform/journeys/channels" icon="paper-plane">
    Deliver messages through email, SMS, push, or inbox
  </Card>

  <Card title="Journey Templates" href="/platform/journeys/journey-templates" icon="file-lines">
    Create notification content inline, scoped to the journey
  </Card>

  <Card title="Branch" href="/platform/journeys/nodes/branch" icon="code-branch">
    Split execution into conditional paths at runtime
  </Card>

  <Card title="Delay" href="/platform/journeys/nodes/delay" icon="clock">
    Pause execution for a duration or until a specific time
  </Card>

  <Card title="Fetch Data" href="/platform/journeys/nodes/fetch-data" icon="cloud-arrow-down">
    Pull data from external services during execution
  </Card>

  <Card title="Throttle" href="/platform/journeys/nodes/throttle" icon="gauge-high">
    Limit how often a user passes through a point in the journey
  </Card>
</CardGroup>

## Journeys vs Send API

The [Send API](/platform/sending/send-message) is the right choice for most notifications. It handles rendering, routing, preferences, and delivery in a single call. You don't need journeys for straightforward transactional messages.

Journeys are for when your messaging involves:

* **Multi-step sequences** with timing between steps (onboarding flows, reminder chains)
* **Conditional logic** that routes users down different paths based on their data or behavior
* **Data enrichment** from external services during execution
* **Rate limiting** to prevent notification fatigue
* **Auditability** where you need to step through exactly what happened for a specific user

|                       | Send API                            | Journeys                          |
| --------------------- | ----------------------------------- | --------------------------------- |
| **Complexity**        | Single call                         | Multi-step workflows              |
| **Data contract**     | None (accepts any payload)          | Typed schema with editor autofill |
| **Timing**            | Immediate (or with delay parameter) | Built-in delays and scheduling    |
| **Conditional logic** | In your code                        | Built-in branching                |
| **Debugging**         | Message logs                        | Step-by-step run inspection       |
| **Best for**          | Transactional messages              | Complex messaging experiences     |

## Getting Started

1. Navigate to [Journeys](https://app.courier.com/journeys) in the Courier app
2. Click **New Journey** and choose a trigger type
3. Add nodes to define your workflow
4. **Publish** the journey to activate it
5. Invoke via API or wait for a Segment event

For a hands-on walkthrough, see [Create Your First Journey](/tutorials/journeys/how-to-create-your-first-journey).

## What's Next

<CardGroup cols={2}>
  <Card title="Starting a Journey" href="/platform/journeys/invocation" icon="bolt">
    Configure API and Segment triggers
  </Card>

  <Card title="Building Your Journey" href="/platform/journeys/building-journeys" icon="arrow-progress">
    Add branching, delays, enrichment, and more
  </Card>

  <Card title="Run Inspection" href="/platform/journeys/run-inspection" icon="magnifying-glass">
    Step through individual runs to debug issues
  </Card>

  <Card title="Multi-Step Onboarding Journey" href="/tutorials/journeys/how-to-build-a-multi-step-onboarding-journey" icon="circle-play">
    Build a journey with branching, delays, and external data
  </Card>
</CardGroup>
