# Source: https://www.courier.com/docs/platform/sending/delivery-pipeline-resilience.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delivery Reliability & Retries

> Courier uses exponential backoff retry strategies to ensure reliable message, webhook delivery, and status tracking over 72 hours despite temporary network or integration failures.

## Overview

Courier's delivery pipeline automatically retries failed delivery attempts when temporary issues occur. This includes handling provider outages, network failures, rate limiting, and other transient errors through exponential backoff retry strategies.

## How Resilience Works

### Automatic Retry System

Courier monitors three key areas and automatically retries when issues occur:

1. **Message Delivery**: Retrying notification sends when providers are unavailable
2. **Status Tracking**: Checking delivery status when providers can't respond immediately
3. **Webhook Delivery**: Ensuring your application receives delivery updates

### Retry Behavior

When temporary failures occur:

* **Message delivery**: Attempts continue for up to 24 hours before marking as failed
* **Status tracking**: Delivery status checks continue for up to 72 hours
* **Webhook delivery**: Status update delivery to your endpoints retries for 24 hours
* **Automatic resumption**: Normal processing resumes when provider services recover

## Retry Strategies

### Message Delivery Retries

**When Retries Happen:**

* Provider network outages or timeouts
* Rate limiting from email/SMS providers
* Temporary server overload at providers
* Transient Courier system issues

**Retry Timeline:**

* **First 10 attempts**: Exponential backoff (5 seconds to 15 minutes)
* **Remaining attempts**: 15-minute intervals
* **Maximum duration**: 24 hours (up to 104 total attempts)

<Note>
  **Smart Backoff**: The exponential delay prevents overwhelming struggling providers while ensuring quick recovery when services restore.
</Note>

### Status Tracking Retries

Even when messages are sent successfully, Courier continues tracking delivery status (delivered, opened, clicked) for up to 72 hours.

**Retry Timeline:**

* **First 10 attempts**: Immediate retries
* **11th attempt**: 1-hour delay
* **12th attempt**: 2-hour delay
* **Remaining attempts**: 3-hour intervals for up to 72 hours

### Webhook Delivery Retries

Courier ensures your application receives delivery status updates by retrying webhook deliveries when your endpoints are temporarily unavailable.

**Retry Timeline:**

* **Same as message delivery**: 24-hour retry window
* **Exponential backoff**: 5 seconds to 15-minute intervals
* **Handles common issues**: Network errors, temporary server downtime, rate limits

<Info>
  **Webhook Reliability**: Configure multiple webhook endpoints in your workspace settings to ensure delivery status updates reach your application even during maintenance windows.
</Info>

## Monitoring & Troubleshooting

### Behavior During Outages

When provider outages or network issues occur:

* **Message queuing**: Failed sends are queued and retried automatically
* **Delivery resumption**: Processing continues when providers become available
* **Status tracking**: Delivery status checks resume with full history maintained
* **Webhook processing**: Missed delivery events are sent when endpoints are reachable

### Tracking Resilience in Action

Monitor retry behavior through:

* **[Message Logs](/platform/analytics/message-logs)**: View retry attempts and final delivery status
* **[Outbound Webhooks](/platform/workspaces/outbound-webhooks)**: Configure reliable status update delivery
* **[Courier Status Page](https://status.courier.com/)**: Check service health and planned maintenance

### Implementation Considerations

* **Asynchronous delivery**: Notification delivery timing varies based on retry attempts
* **Webhook idempotency**: Endpoints should handle duplicate delivery status events
* **Retry monitoring**: Message logs show retry attempts and final delivery status
* **Endpoint redundancy**: Multiple webhook URLs reduce delivery status update failures

## Related Resources

<CardGroup cols={2}>
  <Card title="Message Logs" href="/platform/analytics/message-logs" icon="chart-line">
    Monitor delivery attempts and track retry behavior
  </Card>

  <Card title="Outbound Webhooks" href="/platform/workspaces/outbound-webhooks" icon="webhook">
    Configure reliable delivery status updates for your application
  </Card>

  <Card title="Channel Priority" href="/platform/sending/channel-priority" icon="route">
    Set up intelligent fallback routing to complement automatic retries
  </Card>

  <Card title="Courier Status Page" href="https://status.courier.com/" icon="signal">
    Check real-time service health and planned maintenance
  </Card>
</CardGroup>
