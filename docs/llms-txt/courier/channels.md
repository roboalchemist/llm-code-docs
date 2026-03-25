# Source: https://www.courier.com/docs/platform/journeys/channels.md

# Source: https://www.courier.com/docs/platform/content/design-studio/channels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Channels

> Understand channel-specific behavior in Design Studio.

Design Studio supports multiple notification channels, each with different capabilities and content block support.

## Channel overview

| Channel      | Description                     | Block support |
| ------------ | ------------------------------- | ------------- |
| **Email**    | HTML email with full formatting | Full          |
| **SMS**      | Plain text messages             | Limited       |
| **Push**     | Mobile push notifications       | Limited       |
| **In-App**   | Courier Inbox notifications     | Limited       |
| **Slack**    | Slack workspace messages        | Partial       |
| **MS Teams** | Microsoft Teams messages        | Partial       |

## Channel-specific behavior

### Email

Email has the richest formatting options with full support for all content blocks.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-email.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=1c80f23e07e88094f4b64ea1c9ac8776" alt="Email channel editor" width="3446" height="1980" data-path="assets/platform/content/designer-v2/designer-v2-email.png" />
</Frame>

* Full HTML rendering
* All text formatting options (bold, italic, underline, strikethrough, links)
* Image embedding and linking
* Custom markup via HTML blocks
* Brand header and footer support

### SMS

SMS is plain text only. The Text block is the only supported block type.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-sms.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=d24b6d836c713040af0aad9e383a9388" alt="SMS channel editor" width="3452" height="1988" data-path="assets/platform/content/designer-v2/designer-v2-sms.png" />
</Frame>

* No formatting (bold, italic, etc.)
* Variables supported via `{{variable}}` syntax
* Character limits apply based on carrier
* Links are sent as plain URLs

### Push

Push notifications have limited content space. Only the Text block is supported.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-push.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=2dc60818fdc0eab8715bdc1d53fd3c5d" alt="Push channel editor" width="3454" height="1992" data-path="assets/platform/content/designer-v2/designer-v2-push.png" />
</Frame>

* Title and body text
* Variables supported
* Length limits vary by platform (iOS, Android, Web)
* No rich formatting

### In-App (Inbox)

In-App notifications via [Courier Inbox](/platform/inbox/inbox-overview) support text content.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-in-app.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=4b47a93318551fdff9f592d0dd1e873f" alt="In-App channel editor" width="3450" height="1988" data-path="assets/platform/content/designer-v2/designer-v2-in-app.png" />
</Frame>

* Title and body text
* Variables supported
* Click actions can be configured (enable button, action URL)
* No rich formatting in the designer

### Slack

Slack supports a subset of blocks with Slack-specific formatting.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-slack.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=64a1adf3981724630c7600b6747398f0" alt="Slack channel editor" width="3456" height="1990" data-path="assets/platform/content/designer-v2/designer-v2-slack.png" />
</Frame>

* Text with Slack markdwn formatting (bold, italic, strikethrough, links)
* Buttons as interactive elements
* Dividers between content sections

### MS Teams

MS Teams has similar capabilities to Slack with Adaptive Card formatting.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-msteams.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=a0c0413fe96322e0b66aad5559585773" alt="MS Teams channel editor" width="3452" height="1990" data-path="assets/platform/content/designer-v2/designer-v2-msteams.png" />
</Frame>

* Text with basic formatting
* Dividers

## Switching between channels

In Design Studio, each channel has its own content editor. Channel tabs appear at the top of the editor.

* Click a channel tab to edit that channel's content
* Each channel maintains its own set of blocks
* Content is not automatically synced between channels

<Tip>
  Design your email content first (richest options), then adapt for other channels as needed.
</Tip>

## Related

<CardGroup cols={2}>
  <Card title="Content Blocks" icon="cube" href="/platform/content/design-studio/design-studio-block-basics">
    Working with content blocks
  </Card>

  <Card title="Routing" icon="route" href="/platform/content/template-designer/routing-configuration">
    Configure channel routing
  </Card>
</CardGroup>
