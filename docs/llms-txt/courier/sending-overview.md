# Source: https://www.courier.com/docs/platform/sending/sending-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Sending Works

> Learn how message sending works with Courier. See how notifications move from your app through the Courier API to channels like email, SMS, in-app, push, with built-in routing, preferences, and observability.

A send begins when your application calls the Courier API to send a message. Courier renders your content, determines which channels to use, and sends through your configured providers.

Each message is tracked from request to delivery so you can monitor outcomes in real time. Courier provides a single source of truth for message observability across all channels.

<div align="center">
  **Your App   →   Courier API   →   Providers   →   User**
</div>

You decide **what** to send and **who** should receive it. Courier manages **how** it gets there. It handles routing, preferences, retries, and logging automatically.

A single API call is all it takes to send a notification. One request handles rendering, routing, preferences, and delivery across every channel. See [Send a Message](/platform/sending/send-message) for code examples in every supported language.

## Core Concepts

Every send request is built around a few core ideas:

**Recipients**\
You can include contact details (email, phone, push token) directly in your request or reference a `user_id` linked to a stored [user profile](/platform/users/users-overview).

**Templates**\
Define content inline or reference a saved [template](/platform/content/template-designer/template-designer-overview) that your team manages visually. Templates keep messaging consistent across channels and editable without code changes.

**Data**\
Pass [dynamic variables](/platform/content/variables/inserting-variables) like `{{name}}` or `{{order_id}}` to personalize content at send time.

**Routing**\
Deliver messages using [priority routing](/platform/sending/channel-priority) through a single channel or by broadcasting across multiple channels at once. Courier automatically selects the optimal route for each message.

**User Preferences**\
Courier automatically enforces each user's [notification preferences](/platform/preferences/preferences-overview) at send time, respecting channel choices, frequency settings, and opt-outs without extra logic in your code.

***

## Beyond Single Sends

The Send API handles the majority of notification use cases on its own. When your product needs more, Courier provides a natural path forward without requiring you to rearchitect.

**[Templates](/platform/content/content-overview)** let you move content out of your code so PMs and designers can update messaging independently. Your send call stays the same; you just reference a template ID instead of inline content.

**[Automations](/platform/automations/automations-overview)** add timing, sequencing, and conditional logic on top of sending. Use them for digest summaries, onboarding sequences, reminder chains, or any notification that depends on user behavior or elapsed time. Automations use the same templates, users, and preferences as direct sends.

You start simple and layer on complexity only when you need it. See [Choose a Sending Strategy](/platform/sending/choosing-your-sending-strategy) for a detailed comparison of when to use each approach.

## FAQ

<AccordionGroup>
  <Accordion title="Can I send to multiple users at once?">
    Yes. Pass an array of recipients in the `to` field to send a single message to multiple users. You can also send to a [List](/platform/users/lists) or [Audience](/platform/users/audiences) to target dynamic groups. For larger volumes, use the [Bulk API](/api-reference/bulk/create-a-bulk-job) to create a job, add users, and run the job asynchronously.
  </Accordion>

  <Accordion title="What happens if a channel or provider fails?">
    Courier automatically fails over based on your routing configuration. If the primary provider for a channel is unavailable, Courier tries the next configured provider. If the entire channel fails (e.g. the user has no email address), Courier moves to the next channel in priority order. See [Automated Failover](/platform/sending/failover) for details.
  </Accordion>

  <Accordion title="How does Courier handle retries?">
    Courier retries failed sends automatically using exponential backoff. Transient errors from providers (rate limits, temporary outages) are retried before the send is marked as failed. You can monitor retry attempts and final delivery status in [Message Logs](/platform/analytics/message-logs).
  </Accordion>

  <Accordion title="Can I prevent duplicate sends?">
    Yes. Include an `idempotency_key` in your send request header. If Courier receives a second request with the same key, it returns the original response without sending again. This is useful for safely retrying requests after network failures.
  </Accordion>

  <Accordion title="Can I schedule or delay a send?">
    Yes. Use the `delay` object in your send request to hold a message for a specified duration or until a specific time. See [Delays & Delivery Windows](/platform/sending/delay) for configuration options.
  </Accordion>
</AccordionGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Choose a Sending Strategy" href="/platform/sending/choosing-your-sending-strategy" icon="route">
    Inline sends, templates, or automations; pick the right level
  </Card>

  <Card title="Send a Message" href="/platform/sending/send-message" icon="paper-plane">
    Code examples for every supported language
  </Card>

  <Card title="Automations Overview" href="/platform/automations/automations-overview" icon="arrow-progress">
    Multi-step workflows, digests, and conditional logic
  </Card>

  <Card title="Automated Failover" href="/platform/sending/failover" icon="shield">
    Automatic provider and channel failover
  </Card>
</CardGroup>
