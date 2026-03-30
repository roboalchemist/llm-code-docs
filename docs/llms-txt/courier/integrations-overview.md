# Source: https://www.courier.com/docs/external-integrations/integrations-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrations Overview

> Connect Courier to your email, in-app, SMS, push, and chat providers to enable multichannel delivery.

## Integration Platform

Courier integrates with 50+ notification providers across **email**, **in-app**, **SMS**, **push**, and **chat** channels. You can connect the providers your system already uses—like SendGrid, Twilio, Firebase, Slack, and others—and send notifications through them with a single API call.

Using Courier allows you to:

* Route messages through preferred or region-specific providers
* Automatically fail over to backups when a provider is unavailable
* Track delivery performance and error rates in real time
* Enable full message log observability for engineering and support teams

After setup, Courier handles message delivery through your connected providers, managing routing, retries, and rate limits automatically.

***

## Setting Up Your First Provider

### Provider Configuration

To connect a provider:

1. **Get API credentials** — Obtain your API key or authentication token from the provider.
2. **Add the provider in Courier** — In your Courier workspace, open the [Integrations Catalog](https://app.courier.com/integrations/catalog) and add a new provider from the available list.
3. **Test the connection** — Verify your credentials and confirm that Courier can successfully send through the provider.
4. **Configure routing** — Decide how Courier uses this provider for message delivery and define channel priorities or fallbacks.

For detailed setup steps, see [Channel Settings](/platform/sending/channel-settings).

<Warning>
  Provider API keys are configured **per environment**. If you set up SendGrid in your Production environment, you must also add the API key in your Test environment to send test messages. A missing provider configuration results in a `MISSING_CONFIGURATION` error in your message logs.
</Warning>

***

### Provider Categories

Courier supports providers across five main channel types:

* **Email** — [SendGrid](/external-integrations/email/sendgrid), [Mailgun](/external-integrations/email/mailgun), [AWS SES](/external-integrations/email/aws-ses), and more
* **In-App** — Courier’s built-in [Inbox](/platform/inbox/inbox-overview) for web and mobile applications
* **SMS** — [Twilio](/external-integrations/sms/twilio), [MessageBird](/external-integrations/sms/messagebird), [Plivo](/external-integrations/sms/plivo), and more
* **Push** — [Firebase FCM](/external-integrations/push/firebase-fcm), [Airship](/external-integrations/push/airship), [OneSignal](/external-integrations/push/onesignal-push), and more
* **Chat** — [Slack](/external-integrations/direct-message/slack), [Microsoft Teams](/external-integrations/direct-message/microsoft-teams), [WhatsApp](/external-integrations/direct-message/whatsapp), and more

Each integration page includes detailed setup steps and configuration options.

<Info>
  [**Courier Inbox**](/platform/inbox/inbox-overview) provides a ready-to-use, in-app notification center that syncs with other channels automatically.  You can customize its appearance, handle read states, and track engagement—all without building a notification UI from scratch.
</Info>

***

## Monitoring Provider Performance

### Provider Metrics

Track provider health and performance directly in Courier’s **Analytics Dashboard**.\
Monitor delivery rates, latency, and error rates to quickly detect issues and optimize routing.

For details on monitoring and analytics, see [Analytics Overview](/platform/analytics/analytics).

***

## Integration Features

### Fallback and Routing

Courier automatically retries or switches to backup providers when a primary provider fails. You can define custom routing logic to control which providers are used and in what order.

Learn more in [Channel Priority](/platform/sending/channel-priority).

***

### Rate Limit Management

When a provider returns a rate limit error (HTTP 429), Courier automatically queues the message and retries using exponential backoff:

| Attempt | Delay      |
| ------- | ---------- |
| 1       | 5 seconds  |
| 2       | 10 seconds |
| 3       | 20 seconds |
| 4       | 40 seconds |
| 5       | 60 seconds |
| 6       | 2 minutes  |
| 7       | 4 minutes  |
| 8       | 8 minutes  |
| 9       | 12 minutes |
| 10+     | 15 minutes |

Retries continue for up to **24 hours** (approximately 104 total attempts). If the provider includes a `Retry-After` header, Courier respects that timing instead of the default backoff schedule.

After exhausting retries, Courier attempts [failover](/platform/sending/failover) to an alternative provider or channel if one is configured. If no alternatives exist, the message is marked as `UNDELIVERABLE`.

For a full overview of retry strategies across message delivery, status tracking, and webhooks, see [Delivery Reliability & Retries](/platform/sending/delivery-pipeline-resilience).

***

## Available Providers

Browse the integration categories below for provider-specific setup guides and configuration options.

<CardGroup cols={2}>
  <Card title="Email Providers" href="/external-integrations/email/intro-to-email" icon="envelope">
    Configure email delivery
  </Card>

  <Card title="SMS Providers" href="/external-integrations/sms/intro-to-sms" icon="message">
    Configure SMS delivery
  </Card>

  <Card title="Push Providers" href="/external-integrations/push/intro-to-push" icon="mobile">
    Configure push delivery
  </Card>

  <Card title="Chat & DM Providers" href="/external-integrations/direct-message/intro-to-direct-message" icon="comments">
    Configure chat and direct message delivery
  </Card>

  <Card title="CDP Integrations" href="/external-integrations/cdp/intro-to-cdp" icon="database">
    Sync user data from Segment and Rudderstack
  </Card>

  <Card title="Observability" href="/external-integrations/observability/intro-to-observability" icon="chart-line">
    Monitor delivery with Datadog and New Relic
  </Card>
</CardGroup>
