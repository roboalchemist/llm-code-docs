# Source: https://www.courier.com/docs/welcome.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Courier?

> Courier is infrastructure for product-to-user communication. Send notifications across email, SMS, push, chat, and in-app channels through one API.

Courier is infrastructure that powers product-to-user communication. It provides a unified system for designing, sending, and managing notifications across email, SMS, push, chat, and in-app channels.

Your app triggers an event, Courier determines the right channels and providers, renders the message, enforces user preferences, and delivers it in real time. One API, every channel.

## How Courier Works

Courier combines APIs, infrastructure, and UI tools to power every stage of the notification lifecycle:

1. **Send multichannel messages** through one API that manages routing, failover, and retries.
2. **Power in-app notification centers** with Courier Inbox for web and mobile.
3. **Design notifications** visually in the Designer, programmatically with Elemental, or embed a design experience in your product with Courier Create.
4. **Automate workflows** with time-based or event-driven triggers using the Automation Platform.
5. **Manage user preferences** with a hosted preferences center and Preferences API.

***

## Understand Courier

<CardGroup cols={2}>
  <Card title="How does sending work?" href="/platform/sending/sending-overview" icon="paper-plane">
    Your app calls the Send API. Courier routes to the right channels, renders templates, handles retries and failover, and delivers across email, SMS, push, chat, and in-app.
  </Card>

  <Card title="What are notification templates?" href="/platform/content/content-overview" icon="page">
    Templates define what your notifications look like. Build them visually in the Designer, define them in code with Elemental JSON, or pass content directly through the API.
  </Card>

  <Card title="How do user preferences work?" href="/platform/preferences/preferences-overview" icon="list">
    Users control which channels and categories they receive. You configure topics and defaults; Courier enforces opt-outs automatically at send time.
  </Card>

  <Card title="What is Courier Inbox?" href="/platform/inbox/inbox-overview" icon="inbox">
    A real-time in-app notification center you drop into your product. Web and mobile SDKs with read state, archiving, and per-user history, all on the same delivery system as your other channels.
  </Card>

  <Card title="How do automations work?" href="/platform/automations/automations-overview" icon="arrow-progress">
    Orchestrate multi-step notification workflows with triggers, delays, conditions, and branching. Power digests, reminders, and onboarding sequences without managing backend logic.
  </Card>

  <Card title="What are tenants?" href="/platform/tenants/tenants-overview" icon="building">
    Organize users by customer or organization. Each tenant can have its own branding, preferences, and metadata for B2B notification scenarios.
  </Card>
</CardGroup>

## Start Building

<CardGroup cols={2}>
  <Card title="Send your first notification" href="/getting-started/quickstart" icon="bolt">
    Install the SDK, grab your API key, and send a message in under 5 minutes. Includes curl, Node, Python, Ruby, and Go examples.
  </Card>

  <Card title="Design a notification template" href="/tutorials/content/how-to-design-your-first-notification" icon="palette">
    Create a template in the Designer, add content blocks, preview, publish, and send a test message.
  </Card>

  <Card title="Add an in-app inbox" href="/tutorials/inbox/how-to-implement-inbox" icon="inbox">
    Drop the Inbox component into your web or mobile app and start delivering in-app notifications.
  </Card>

  <Card title="Set up user preferences" href="/tutorials/preferences/how-to-set-up-hosted-preference-center" icon="sliders">
    Deploy a hosted preference page so users can control their notification channels and topics.
  </Card>

  <Card title="Configure multi-channel routing" href="/tutorials/sending/how-to-configure-multi-channel-routing" icon="list-tree">
    Set channel priority and fallback rules so messages reach users on the right channel.
  </Card>

  <Card title="Browse all tutorials" href="/tutorials/tutorials-overview" icon="graduation-cap">
    Step-by-step guides for sending, content, automations, inbox, and preferences.
  </Card>
</CardGroup>

## Reference & Tools

<CardGroup cols={3}>
  <Card title="API Reference" href="/reference/get-started" icon="book">
    REST API docs for sending, users, preferences, automations, and more.
  </Card>

  <Card title="SDKs" href="/sdk-libraries/sdks-overview" icon="code">
    Server and client libraries for Node, Python, Go, Ruby, Java, React, iOS, and Android.
  </Card>

  <Card title="Integrations" href="/external-integrations/integrations-overview" icon="plug">
    Connect email, SMS, push, and chat providers like SendGrid, Twilio, Firebase, Slack, and 50+ others.
  </Card>
</CardGroup>
