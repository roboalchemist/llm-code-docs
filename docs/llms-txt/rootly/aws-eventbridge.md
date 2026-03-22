# Source: https://docs.rootly.com/integrations/aws-eventbridge.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS EventBridge

> Stream incident and alert lifecycle events from Rootly to AWS EventBridge for real-time event-driven integrations.

## Overview

The AWS EventBridge integration allows Rootly to publish incident and alert lifecycle events directly to your AWS account through the [EventBridge partner event source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html) model. Events are delivered in near real-time as incidents and alerts progress through their lifecycle, enabling you to build event-driven automations entirely within AWS.

Once configured, Rootly creates a partner event source in your AWS account. You associate this event source with an event bus in the EventBridge console, then create rules to route events to any EventBridge target — Lambda functions, Step Functions, SQS queues, SNS topics, API Gateway endpoints, and more.

<Info>
  This integration uses the AWS EventBridge partner event source model. Rootly pushes events to your account — no polling or webhook configuration is required on your side.
</Info>

## Supported Event Types

You can subscribe to any combination of the following event types per integration:

**Alert Events:**

| Event Type           | Description                              |
| -------------------- | ---------------------------------------- |
| `alert.created`      | A new alert was created                  |
| `alert.updated`      | Alert properties were changed            |
| `alert.acknowledged` | An alert was acknowledged by a responder |
| `alert.resolved`     | An alert was resolved                    |

**Incident Events:**

| Event Type           | Description                      |
| -------------------- | -------------------------------- |
| `incident.created`   | A new incident was started       |
| `incident.updated`   | Incident properties were changed |
| `incident.mitigated` | An incident was mitigated        |
| `incident.resolved`  | An incident was resolved         |

<Tip>
  If no event subscriptions are selected, all event types are published. This is useful when you want to receive everything and filter using EventBridge rules instead.
</Tip>

## Prerequisites

Before configuring the integration, ensure that you have:

* A Rootly account with admin or owner permissions
* An AWS account ID (12-digit number)
* Access to the AWS EventBridge console in your target region

## Setup Instructions

<Steps>
  <Step title="Create the integration in Rootly">
    Navigate to **Settings** → **Integrations** → **AWS EventBridge** and click **Add Integration**.

    Fill in the following fields:

    * **Integration Name**: A friendly name (e.g., "Production Events")
    * **AWS Account ID**: Your 12-digit AWS account ID
    * **AWS Region**: The region where your event bus will be created
    * **Event Source Name**: A unique identifier (e.g., "production", "staging")
    * **Event Subscriptions**: Select which event types to stream (leave empty for all)

    Click **Create Integration**. Rootly creates a partner event source in your AWS account.

    Your new integration will appear on the index page with a **Pending** status until you complete the AWS setup.

    <Frame caption="EventBridge integrations index page showing a pending integration">
      <img src="https://mintcdn.com/rootly/OchwmG0x0Qh2aOLD/images/integrations/aws-eventbridge/eventbridge-2.png?fit=max&auto=format&n=OchwmG0x0Qh2aOLD&q=85&s=10f73f4334906106722f6f3b9a6a8407" alt="EventBridge integrations index" width="1492" height="241" data-path="images/integrations/aws-eventbridge/eventbridge-2.png" />
    </Frame>

    <Warning>
      The AWS Account ID, Region, and Event Source Name cannot be changed after creation. A new integration must be created if these values need to change.
    </Warning>
  </Step>

  <Step title="Associate the event source in AWS">
    Open the [AWS EventBridge console](https://console.aws.amazon.com/events/) in the region you selected.

    1. Go to **Partner event sources** in the left navigation
    2. Find your event source — it will be named `aws.partner/rootly.com/<your-team-slug>/<event-source-name>`
    3. Select the event source and click **Associate with event bus**
    4. Confirm the association

    <Frame caption="AWS EventBridge console showing the Rootly partner event source">
      <img src="https://mintcdn.com/rootly/OchwmG0x0Qh2aOLD/images/integrations/aws-eventbridge/eventbridge-3.png?fit=max&auto=format&n=OchwmG0x0Qh2aOLD&q=85&s=a5df03db924a7e3f70bd53bbdb226c3f" alt="AWS EventBridge partner event sources console" width="1934" height="515" data-path="images/integrations/aws-eventbridge/eventbridge-3.png" />
    </Frame>

    This creates a partner event bus in your account that receives events from Rootly.
  </Step>

  <Step title="Activate the integration in Rootly">
    Return to Rootly and edit your EventBridge integration. Check **Mark as Active** and save.

    You can also configure **Event Subscriptions** to select which event types to stream.

    <Frame caption="Edit integration form with event subscriptions and Event Source ARN">
      <img src="https://mintcdn.com/rootly/OchwmG0x0Qh2aOLD/images/integrations/aws-eventbridge/eventbridge-1.png?fit=max&auto=format&n=OchwmG0x0Qh2aOLD&q=85&s=b1b3d7dd993f008415e46f6b34df086d" alt="Edit AWS EventBridge integration form" width="639" height="846" data-path="images/integrations/aws-eventbridge/eventbridge-1.png" />
    </Frame>

    <Info>
      The integration must be activated after associating the event source in AWS. Events are only published to active integrations.
    </Info>
  </Step>

  <Step title="Create EventBridge rules">
    In the AWS EventBridge console, navigate to **Rules** and select your partner event bus.

    Create rules to route events to your targets. Use event patterns to filter by event type:

    ```json  theme={null}
    {
      "detail-type": ["incident.created", "incident.resolved"]
    }
    ```

    Or match all Rootly events:

    ```json  theme={null}
    {
      "source": [{
        "prefix": "aws.partner/rootly.com"
      }]
    }
    ```
  </Step>

  <Step title="Test the integration">
    Create a test incident in Rootly and verify that events appear in your EventBridge targets. Check the EventBridge monitoring tab for delivery metrics.
  </Step>
</Steps>

## Event Payload Structure

Events are published using the [EventBridge event format](https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html). Each event contains:

| Field         | Description                                        |
| ------------- | -------------------------------------------------- |
| `source`      | The full partner event source name                 |
| `detail-type` | The event type (e.g., `incident.created`)          |
| `detail`      | JSON object containing the entity data             |
| `time`        | ISO 8601 timestamp of when the event was published |
| `resources`   | Array containing the resource ARN                  |

### Incident Event Detail

```json  theme={null}
{
  "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "sequential_id": 42,
  "title": "Database outage in us-east-1",
  "slug": "database-outage-in-us-east-1",
  "summary": "Production database is experiencing connection timeouts",
  "status": "started",
  "kind": "normal",
  "private": false,
  "detected_at": "2026-01-15T10:30:00Z",
  "acknowledged_at": null,
  "started_at": "2026-01-15T10:30:00Z",
  "mitigated_at": null,
  "resolved_at": null,
  "cancelled_at": null,
  "created_at": "2026-01-15T10:30:00Z",
  "updated_at": "2026-01-15T10:30:00Z",
  "services": [
    { "id": "abc-123", "name": "API Service", "slug": "api-service" }
  ],
  "environments": [
    { "id": "def-456", "name": "Production", "slug": "production" }
  ],
  "functionalities": [
    { "id": "ghi-789", "name": "Authentication", "slug": "authentication" }
  ],
  "severity": {
    "id": "jkl-012", "name": "Critical", "slug": "critical", "color": "#FF0000"
  }
}
```

### Alert Event Detail

```json  theme={null}
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "source": "pagerduty",
  "summary": "High CPU usage on web-server-01",
  "status": "triggered",
  "labels": { "env": "production", "service": "web" },
  "started_at": "2026-01-15T10:30:00Z",
  "ended_at": null,
  "created_at": "2026-01-15T10:30:00Z",
  "updated_at": "2026-01-15T10:30:00Z",
  "services": [
    { "id": "abc-123", "name": "Web Service", "slug": "web-service" }
  ],
  "environments": [
    { "id": "def-456", "name": "Production", "slug": "production" }
  ]
}
```

## Multiple Integrations

You can create multiple EventBridge integrations for the same team. This is useful for:

* **Multi-region delivery**: Stream events to different AWS regions
* **Multi-account delivery**: Send events to separate AWS accounts (e.g., production vs. staging)
* **Selective subscriptions**: Send only alert events to one bus and only incident events to another

Each integration operates independently with its own event source, subscriptions, and active status.

## Managing Integrations

### Editing

You can update the integration name, event subscriptions, and active status at any time. AWS Account ID, Region, and Event Source Name are locked after creation.

### Deleting

Deleting an integration in Rootly stops event delivery. The partner event source remains in your AWS account and can be cleaned up from the EventBridge console.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Events are not appearing in EventBridge" icon="circle-exclamation">
    1. Verify the integration is marked as **Active** in Rootly
    2. Confirm the partner event source is **Associated** in the AWS EventBridge console
    3. Check that the event type is included in the integration's subscriptions (or that subscriptions are empty for all events)
    4. Verify your EventBridge rules are targeting the correct partner event bus
  </Accordion>

  <Accordion title="Partner event source not found in AWS" icon="magnifying-glass">
    Ensure you are looking in the correct AWS region. The event source is created in the region selected when configuring the integration. Also verify the AWS Account ID is correct.
  </Accordion>

  <Accordion title="Some event types are missing" icon="filter">
    Check the **Event Subscriptions** setting on your integration. If specific events are selected, only those events will be published. Clear all subscriptions to receive all event types.
  </Accordion>

  <Accordion title="Events are delayed" icon="clock">
    Events are published asynchronously via background jobs. Under normal conditions, events are delivered within a few seconds. If you observe persistent delays, contact Rootly Support.
  </Accordion>
</AccordionGroup>

## Best Practices

* **Use event subscriptions** to limit events to only what you need, reducing noise and cost
* **Create separate integrations** for different environments or AWS accounts
* **Use EventBridge rules** for fine-grained filtering beyond what subscriptions provide
* **Monitor delivery** using EventBridge metrics in CloudWatch
* **Test in staging first** by creating a separate integration pointed at a non-production AWS account


Built with [Mintlify](https://mintlify.com).