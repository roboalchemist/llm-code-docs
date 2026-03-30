# Source: https://www.courier.com/docs/tutorials/tutorials-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tutorials

> Step-by-step guides for designing, sending, and managing notifications with Courier.

## Send

<CardGroup cols={2}>
  <Card title="Send Your First Message" icon="mailbox-flag-up" href="/tutorials/sending/how-to-send-your-first-message">
    Send a notification using the Courier API in minutes
  </Card>

  <Card title="Configure Multi-Channel Routing" icon="list-tree" href="/tutorials/sending/how-to-configure-multi-channel-routing">
    Set up channel priority and failover rules
  </Card>

  <Card title="Send Bulk Notifications" icon="envelopes-bulk" href="/tutorials/sending/how-to-send-bulk-notifications">
    Send notifications to many recipients at once
  </Card>

  <Card title="Send to Lists and Patterns" icon="list" href="/tutorials/sending/how-to-send-to-a-list-or-list-pattern-using-wildcarding">
    Use lists and wildcarding to target groups of recipients
  </Card>

  <Card title="Send Digests" icon="envelope" href="/tutorials/sending/how-to-send-digests">
    Batch notifications into periodic digest messages
  </Card>

  <Card title="Send Notifications with Segment" icon="sitemap" href="/tutorials/sending/how-to-send-notifications-with-segment">
    Trigger automations from Segment events
  </Card>
</CardGroup>

## Design

<CardGroup cols={2}>
  <Card title="Design and Send Your First Notification" icon="palette" href="/tutorials/content/how-to-design-your-first-notification">
    Create a template, add content, preview, publish, and send
  </Card>

  <Card title="Brand Your Notifications" icon="copyright" href="/tutorials/content/how-to-create-and-use-brands">
    Apply logos, colors, and footers with Courier Brands
  </Card>

  <Card title="Use Test Events" icon="magnifying-glass" href="/tutorials/content/how-to-preview-notification">
    Preview and validate notifications with test data
  </Card>

  <Card title="Internationalize Notifications" icon="globe" href="/tutorials/content/internationalizing-notifications">
    Send multi-language notifications using conditions, templates, or variables
  </Card>

  <Card title="Build Notifications with Elemental" icon="file-code" href="/tutorials/content/how-to-use-elemental">
    Define notification content as JSON with conditionals, loops, and channel overrides
  </Card>
</CardGroup>

## Journeys

<CardGroup cols={2}>
  <Card title="Create Your First Journey" icon="route" href="/tutorials/journeys/how-to-create-your-first-journey">
    Choose a trigger, define a schema, add a send node, design a message, publish, and invoke
  </Card>

  <Card title="Build a Multi-Step Onboarding Journey" icon="arrow-progress" href="/tutorials/journeys/how-to-build-a-multi-step-onboarding-journey">
    Build an onboarding sequence with delays, branching, fetch nodes, and multiple send nodes
  </Card>
</CardGroup>

## Automate

<CardGroup cols={2}>
  <Card title="Build Your First Automation" icon="sitemap" href="/tutorials/automations/how-to-automate-message-sequences">
    Create a multi-step workflow in the visual Automations Designer
  </Card>

  <Card title="Send Automations via API" icon="robot" href="/tutorials/automations/how-to-send-an-automation">
    Invoke saved or ad-hoc automations programmatically
  </Card>

  <Card title="Send Automations with Tenants" icon="building" href="/tutorials/automations/how-to-send-automations-with-tenants">
    Use tenant context in automation workflows
  </Card>

  <Card title="Cancel an Automation" icon="ban" href="/tutorials/automations/how-to-cancel-an-automation">
    Stop in-flight automations with cancellation tokens
  </Card>
</CardGroup>

## Inbox & Preferences

<CardGroup cols={2}>
  <Card title="Implement Courier Inbox" icon="inbox" href="/tutorials/inbox/how-to-implement-inbox">
    Add an in-app notification inbox to your application
  </Card>

  <Card title="Send a JWT from Your Backend" icon="key" href="/tutorials/inbox/how-to-send-jwt">
    Authenticate embedded components with JWT tokens
  </Card>

  <Card title="Set Up Hosted Preference Center" icon="globe" href="/tutorials/preferences/how-to-set-up-hosted-preference-center">
    Deploy a Courier-hosted preference page for your users
  </Card>

  <Card title="Embed Preferences in React" icon="react" href="/tutorials/preferences/how-to-embed-preferences-in-react">
    Build an in-app preference center with React components
  </Card>

  <Card title="Configure Preferences via API" icon="code" href="/tutorials/preferences/how-to-configure-user-preferences">
    Read and update preferences programmatically
  </Card>
</CardGroup>

## Ops

<CardGroup cols={2}>
  <Card title="Debug Email Delivery Issues" icon="magnifying-glass-chart" href="/tutorials/monitoring/how-to-debug-delivery-issues">
    Troubleshoot delivery problems using message logs, statuses, and provider tools
  </Card>

  <Card title="Safe Notification Deployment" icon="shield-check" href="/tutorials/ops/safe-notification-deployment">
    Move templates from test to production with draft keys, approvals, and verification
  </Card>

  <Card title="Send Webhook Notifications" icon="webhook" href="/tutorials/ops/how-to-send-webhook-notifications">
    Deliver notification payloads to any HTTP endpoint
  </Card>

  <Card title="Manage User Profiles" icon="user" href="/tutorials/sending/how-to-manage-user-profiles">
    Create, update, and use profiles for personalized notification delivery
  </Card>
</CardGroup>

## Migrate to Courier

<CardGroup cols={2}>
  <Card title="Migrate from Knock" icon="arrow-right-arrow-left" href="/tutorials/migrate/from-knock">
    Move your notification infrastructure from Knock to Courier
  </Card>

  <Card title="Migrate from SuprSend" icon="arrow-right-arrow-left" href="/tutorials/migrate/from-suprsend">
    Move your notification infrastructure from SuprSend to Courier
  </Card>

  <Card title="Migrate from Novu" icon="arrow-right-arrow-left" href="/tutorials/migrate/from-novu">
    Move your notification infrastructure from Novu to Courier
  </Card>

  <Card title="Migrate from OneSignal" icon="arrow-right-arrow-left" href="/tutorials/migrate/from-onesignal">
    Move your notification infrastructure from OneSignal to Courier
  </Card>

  <Card title="Migrate from Braze" icon="arrow-right-arrow-left" href="/tutorials/migrate/from-braze">
    Move your transactional notification flows from Braze to Courier
  </Card>
</CardGroup>
