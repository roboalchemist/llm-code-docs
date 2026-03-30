# Source: https://docs.rootly.com/integrations/aws-cloudwatch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS CloudWatch

> Receive alerts from AWS CloudWatch to trigger incidents, route notifications, and automatically resolve alerts in Rootly.

## Overview

The AWS CloudWatch integration allows Rootly to treat CloudWatch alarms as a native alert source. The integration uses Amazon Simple Notification Service (SNS) to deliver CloudWatch alarm state change events to Rootly via HTTPS webhooks.

When a CloudWatch alarm transitions into the `ALARM` state, Rootly creates a new alert or updates an existing unresolved alert. When the same alarm transitions back into the `OK` state, Rootly automatically resolves the corresponding alert. This behavior enables CloudWatch alarms to participate fully in Rootly’s alert routing, on-call, and incident management workflows.

Alerts created from CloudWatch can be routed to services, escalation policies, or teams, enriched with labels derived from CloudWatch alarm tags, and customized using alert templates.

<Callout icon="repeat" color="#DBEAFE">
  CloudWatch alerts are stateful. Rootly creates alerts when alarms enter the ALARM state and resolves them automatically when the same alarms return to OK.
</Callout>

## How the Integration Works

CloudWatch alarms publish state change notifications to an SNS topic. Rootly subscribes to this SNS topic using an HTTPS webhook endpoint generated when you create a CloudWatch alert source in Rootly.

Each SNS notification contains information about the alarm, including its name, ARN, state, reason for the state change, and timestamp. Rootly uses the alarm ARN as the external identifier for the alert, ensuring that repeated alarm triggers update the same alert and that alerts are resolved when the alarm returns to an OK state.

## Prerequisites

Before configuring the integration, ensure that you have access to an AWS account with permissions to manage CloudWatch alarms and SNS topics. You must also have a Rootly account with access to Alert Sources.

## Setup Instructions

<Steps>
  <Step title="Create an Alert Source in Rootly">
    Begin by creating a CloudWatch alert source in Rootly. Navigate to **Settings** → **Alert Sources** and click **Add Alert Source**. Select **CloudWatch** and provide a descriptive name, such as “Production CloudWatch Alarms.”

    You may optionally configure default alert urgency, assign owner groups, or define an alert template. Once the alert source is saved, copy the webhook URL provided by Rootly.

    ```txt  theme={null}
    https://webhooks.rootly.com/webhooks/incoming/cloud_watch_webhooks?secret=YOUR_SECRET_KEY
    ```

    <Callout icon="key" color="#DBEAFE">
      The webhook secret authenticates incoming requests from Amazon SNS. Treat this value as sensitive and rotate it if it is exposed.
    </Callout>
  </Step>

  <Step title="Create an SNS Topic">
    Create an Amazon SNS topic to receive CloudWatch alarm notifications. In the AWS SNS Console, create a new topic using the **Standard** topic type and give it a clear, descriptive name such as `rootly-cloudwatch-alerts`.

    This SNS topic acts as the delivery mechanism between CloudWatch and Rootly.
  </Step>

  <Step title="Subscribe Rootly to the SNS Topic">
    Open the SNS topic and navigate to the **Subscriptions** tab. Create a new subscription using the **HTTPS** protocol and paste the Rootly webhook URL into the endpoint field.

    AWS sends a subscription confirmation request to the webhook endpoint. Rootly automatically attempts to confirm this request, and the subscription typically transitions to **Confirmed** within a few seconds.

    <Info>
      If the subscription remains in a pending state, verify that the webhook endpoint is reachable and that no network restrictions are blocking AWS SNS traffic.
    </Info>
  </Step>

  <Step title="Configure a CloudWatch Alarm">
    In the CloudWatch Console, navigate to **All alarms** and create a new alarm. Select the metric to monitor and define the alarm conditions, including thresholds and evaluation periods.

    Configure the alarm to send notifications to the SNS topic for both the **In alarm** and **OK** states. This ensures alerts are created and resolved automatically in Rootly.
  </Step>

  <Step title="Test the Integration">
    Trigger the CloudWatch alarm or allow it to trigger naturally. Verify that a new alert appears in Rootly with the source set to CloudWatch.

    When the alarm returns to the `OK` state, confirm that the alert is automatically resolved.
  </Step>
</Steps>

## Alert Mapping and Behavior

Rootly extracts key fields from CloudWatch alarm notifications and maps them to alert attributes. The alarm ARN is used as the external identifier, which allows Rootly to deduplicate alerts and correctly match resolve events. The alarm name, metric name, and state change reason are included in the alert summary, while alarm tags are converted into alert labels.

The alert summary is generated automatically and typically follows the format shown below.

```txt  theme={null}
{MetricName} - {NewStateReason}
```

For example:

```txt  theme={null}
CPUUtilization - Threshold Crossed: 1 datapoint [85.5] was greater than the threshold (80.0).
```

If no tags are present on the CloudWatch alarm, Rootly applies default labels to ensure consistent alert metadata.

## Advanced Configuration

### Alert Templates

Alert templates allow you to control how CloudWatch alerts appear in Rootly. Templates are configured from the Alert Source settings and support Liquid templating, which makes it possible to dynamically generate alert content from the CloudWatch alarm payload.

Commonly used template variables include the alarm name, alarm ARN, metric name, state change reason, and timestamp. These variables can be combined to produce descriptive alert titles, detailed descriptions, and direct links back to the AWS Console.

### Alert Routing

CloudWatch alerts can be routed automatically using Rootly alert routes. Routing rules may be defined using alarm names, metric names, tags, or any other field included in the CloudWatch alarm payload. Routes can target services, escalation policies, or teams, ensuring that alerts are delivered to the appropriate responders without manual intervention.

### Deduplication and Resolution

Rootly deduplicates CloudWatch alerts using the alarm ARN as the external identifier. If an alarm triggers multiple times while an alert remains unresolved, Rootly updates the existing alert instead of creating duplicates. When the alarm transitions back to the `OK` state, Rootly automatically resolves the corresponding alert.

### Notification Targets

In addition to default routing rules, CloudWatch alarms can be sent directly to specific notification targets using a specialized webhook endpoint.

```txt  theme={null}
https://webhooks.rootly.com/webhooks/incoming/cloud_watch_webhooks/notify/{notification_target_type}/{notification_target_id}?secret=YOUR_SECRET_KEY
```

The notification target type must be one of `Service`, `EscalationPolicy`, or `Group`. The notification target ID must be replaced with the UUID of the corresponding resource.

### Webhook Payload Structure

CloudWatch delivers alarm notifications to Amazon SNS, which then forwards them to Rootly. The SNS payload includes metadata about the message and a `Message` field containing a JSON-encoded representation of the CloudWatch alarm state change. Rootly automatically parses this message and extracts the relevant alarm data for alert creation and resolution.

### Security Considerations

Rootly webhook endpoints require HTTPS and use a secret key to authenticate incoming requests. SNS message signatures are verified to ensure authenticity. If IP allowlisting is enabled for your Rootly instance, ensure that AWS SNS IP ranges are permitted.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Why are CloudWatch alerts not being created in Rootly?" icon="circle-exclamation">
    Verify that the SNS subscription is confirmed and that the webhook URL configured in SNS exactly matches the one provided by Rootly. Ensure that the CloudWatch alarm is actively entering the `ALARM` state and review the alert source status in Rootly to confirm whether recent events have been received.
  </Accordion>

  <Accordion title="Why are CloudWatch alerts not being resolved automatically?" icon="rotate">
    Ensure that the CloudWatch alarm is configured to send `OK` notifications to the same SNS topic used for alarm notifications. Rootly relies on the alarm ARN to match resolve events, so confirm that the alarm ARN has not changed since the alert was created.
  </Accordion>

  <Accordion title="Why is the SNS subscription stuck in Pending confirmation?" icon="signal">
    Confirm that the webhook endpoint is reachable over HTTPS and that no firewall rules or IP allowlisting restrictions are blocking AWS SNS traffic. Also verify that the webhook URL is correctly formatted and includes the required secret parameter.
  </Accordion>
</AccordionGroup>

## Best Practices

* Use clear and descriptive alarm names to make alerts easier to interpret.
* Apply CloudWatch tags consistently, as these tags are converted into alert labels and can be used for routing and filtering.
* Configure alert routing rules to ensure alerts reach the appropriate teams.
* Periodically test alarms to validate that the integration continues to function as expected.

For additional assistance, consult the Rootly documentation or contact Rootly Support. You may also refer to AWS CloudWatch and Amazon SNS documentation for more information about alarm and notification configuration.


Built with [Mintlify](https://mintlify.com).