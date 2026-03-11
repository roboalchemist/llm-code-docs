# Source: https://www.courier.com/docs/platform/analytics/analytics-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics Overview

> Track notification delivery, monitor status across channels, and debug issues with message logs, template analytics, and audit trails.

Courier tracks every notification from API request through routing, rendering, provider handoff, and delivery. Use message logs to debug individual sends, template analytics to compare channel performance, and audit trails to review workspace changes.

## Key Concepts

### Message Statuses

Every notification moves through a lifecycle: **Enqueued** (received by Courier), **Routed** (channel selected), **Sent** (handed to provider), **Delivered** (provider confirmed delivery), **Opened/Clicked** (user engaged). If something goes wrong, you'll see **Undeliverable** or **Unroutable** with a reason.

### Environment Isolation

Logs and analytics are scoped to the environment (Production or Test) of the API key used to send. Sends made with a test key only appear in the Test dashboard, and vice versa.

### Retention

Message logs are retained based on your plan tier. Check your plan details or contact support for specific retention windows.

## Common Workflows

**Debug a failed send**: Open [Message Logs](/platform/analytics/message-logs) and filter by recipient, status, or time range. Each log entry shows a timeline of events (enqueued, routed, sent, delivered) plus the rendered content that was sent to the provider. If a send failed, the log tells you exactly where and why.

**Compare channel performance**: Open [Template Analytics](/platform/analytics/analytics) to see send volume, delivery rates, opens, and clicks broken down by channel and provider. Use this to decide whether to prioritize email over push for a given template, or to spot a provider with an unusually high error rate.

**Audit workspace changes**: The [Audit Trail](/platform/analytics/audit-trail) records who changed what and when; API key rotations, user invitations, integration updates, and template publications. Use it for compliance reporting or to trace unexpected configuration changes.

**Track engagement with custom domains**: If you use a custom domain for email tracking links, configure it in [Custom Domain Tracking](/platform/analytics/custom-domain-tracking) so open and click events resolve to your brand instead of Courier's default domain.

## Next Steps

<CardGroup cols={2}>
  <Card title="Message Logs" href="/platform/analytics/message-logs" icon="list">
    Debug individual sends with delivery timelines
  </Card>

  <Card title="Template Analytics" href="/platform/analytics/analytics" icon="chart-line">
    Compare channel and provider performance
  </Card>

  <Card title="Audit Trail" href="/platform/analytics/audit-trail" icon="clock-rotate-left">
    Track workspace configuration changes
  </Card>

  <Card title="Custom Domain Tracking" href="/platform/analytics/custom-domain-tracking" icon="globe">
    Brand your email tracking links
  </Card>
</CardGroup>
