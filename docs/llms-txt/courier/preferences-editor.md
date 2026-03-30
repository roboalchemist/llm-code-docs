# Source: https://www.courier.com/docs/platform/preferences/preferences-editor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Preferences Editor

> Configure subscription topics, preference sections, and channel settings to give users control over their notification experience.

## Overview

The Preferences Editor is your central configuration hub for building user-controlled notification experiences. Create subscription topics that users can opt in/out of, organize them into logical sections, and configure channel-specific delivery options. The editor provides a visual interface for setting up preference hierarchies that respect user choice while maintaining your notification strategy.

<Frame caption="Preferences Editor">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-editor-zoomed-in.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=65e7064c87b2154af9a0f31f1cb30db6" alt="Preferences Editor" width="1564" height="1288" data-path="assets/platform/preferences/preferences-editor-zoomed-in.png" />
</Frame>

## Key Features

* **Subscription Topics** - Create notification categories users can control independently (marketing, security, product updates)
* **Preference Sections** - Group related topics together with shared channel and delivery settings
* **Channel Customization** - Let users choose preferred delivery channels for each topic or section
* **Default State Management** - Configure whether topics start opted-in, opted-out, or required
* **Channel Aliasing** - Customize how channel names appear to match your brand voice
* **Template Mapping** - Connect notification templates to subscription topics for automatic preference enforcement

## Core Components

### Subscription Topics

**Subscription Topics** are notification categories that users can control independently. Each topic represents a logical grouping of related notifications that users might want to receive or skip.

<Frame caption="Subscription Topic Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-topic-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=22e1a54bfd6dced7ade4af0d29859145" alt="Subscription Topic Settings" width="1626" height="1016" data-path="assets/platform/preferences/preferences-topic-settings.png" />
</Frame>

#### Topic Configuration

Configure essential topic properties:

* **Name** - User-facing label for the notification category
* **Section** - Which preference section contains this topic
* **Default State** - Whether users start opted-in, opted-out, or cannot opt-out

#### Default States

Control how users initially interact with each topic:

* **On** - Users automatically receive these notifications unless they opt out
* **Off** - Users must explicitly opt in to receive these notifications
* **Required** - Users cannot opt out of these critical notifications

<Note>
  **Template Mapping**: Each notification template can only be mapped to a single subscription topic for clear preference enforcement.
</Note>

#### Topic Data

<Note>
  **Availability**: Topic Data is available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) for access or [Request a Demo](https://www.courier.com/request-demo) to learn more about how Courier could help you.
</Note>

For a subscription topic, you can provide arbitrary metadata to our API, which allows you to make custom preferences pages. Use cases include:

* Filter subscription topics by metadata
* Create custom logic for controlling preferences
* Maintain custom topic descriptions

### Preference Sections

**Preference Sections** group related subscription topics together and define shared delivery channel options. Sections provide organizational structure and determine which channels users can customize for grouped topics.

<Frame caption="Preference Section Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-channel-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=e01655e6fdc41a098a3599b108d66c38" alt="Preference Section Settings" width="1630" height="1018" data-path="assets/platform/preferences/preferences-channel-settings.png" />
</Frame>

#### Channel Selection

<Note>
  **Availability**: Delivery Channel Selection is available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) for access or [Request a Demo](https://www.courier.com/request-demo) to learn more about how Courier could help you.
</Note>

Enable users to choose their preferred delivery channels for notifications within each section. When enabled, users can select from available channels (email, SMS, push, chat) based on your configuration. In the API, channel values use the `custom_routing` enum: `direct_message`, `email`, `inbox`, `push`, `sms`, `webhook`. The UI may show friendlier labels (e.g. "chat" for inbox or direct message).

<Frame caption="User Channel Selection">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/channel-selection.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=d0bc9b989fcb4cb9279edf28b30e0f72" alt="User Channel Selection" width="1546" height="626" data-path="assets/platform/preferences/channel-selection.png" />
</Frame>

#### Custom Routing API

When users customize their delivery channels, their preferences are reflected in the `custom_routing` array when calling the user preferences API:

<Warning>
  **Important**: Channel Delivery Customization must be enabled for the `custom_routing` array to populate in API responses. If your workspace plan does not support it, the API returns `402 Payment Required` when you send `custom_routing` in an update.
</Warning>

```json  theme={null}
{
  "topic": {
    "custom_routing": [
      "email",
      "push",
      "webhook"
    ],
    "has_custom_routing": true,
    "default_status": "OPTED_IN",
    "section_id": "5p8ROfompcN6Sg_2WR92A",
    "section_name": "Notifications",
    "status": "OPTED_IN",
    "topic_id": "FPPGTQRQTRM8TSPZGZAY9296WB37",
    "topic_name": "Product Updates"
  }
}
```

#### Unsubscribe Headers

When users opt-out of a subscription topic, Courier can automatically include an `List-Unsubscribe` header in outgoing emails that maps to the connected topic. This allows users to manage their preferences directly from their email client or other channels that support this standard.

<Note>Enabling unsubscribe headers requires email-provider-level configurations. For example, [Mailgun offers unsubscribe headers](https://help.mailgun.com/hc/en-us/articles/203306610-Unsubscribe-Handling-Links#01HNZH48NP73S3Q0KVR9B40SV5) in their email configuration settings. Courier will include these in outgoing emails when enabled.</Note>

### Channel Customization

#### Channel Aliases

Customize how notification channels appear to users to match your brand voice and terminology. Instead of generic labels like "Email" or "SMS", use terms that resonate with your audience like "Newsletter" or "Text Alerts".

<Frame caption="Channel Name Customization">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preference-alias.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=edbdbae3633a25db2675b628ba793f93" alt="Channel Name Customization" width="2624" height="1608" data-path="assets/platform/preferences/preference-alias.png" />
</Frame>

Channel aliasing helps create a cohesive user experience where preference options feel integrated with your application's language and design system.

## Template Integration

Connect your notification templates to subscription topics through three different approaches:

### Configure in Topic Settings

Select notification templates directly within subscription topic configuration to establish the preference relationship.

<Frame caption="Linked Templates in Topic Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-linked-notifications.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=fc780b0abd07d93edf8653051d29c7f7" alt="Linked Templates in Topic Settings" width="1632" height="1020" data-path="assets/platform/preferences/preferences-linked-notifications.png" />
</Frame>

### Set During Template Creation

Choose a subscription topic when [creating new notification templates](/platform/content/template-designer/template-designer-overview) to automatically establish the preference mapping.

<Frame caption="Topic Selection in Template Creation">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-new-notification.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=e2d2fa94add2538970e4106530fafeaf" alt="Topic Selection in Template Creation" width="1788" height="1206" data-path="assets/platform/preferences/preferences-new-notification.png" />
</Frame>

### Update in Template Designer

Modify subscription topic assignments within the Template Designer to adjust preference enforcement for existing templates.

<Frame caption="Topic Assignment in Template Designer">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-topic-dropdown.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=fd07bf1ca133e62c196c8facd7e612e0" alt="Topic Assignment in Template Designer" width="1516" height="954" data-path="assets/platform/preferences/preferences-topic-dropdown.png" />
</Frame>

<Tip>
  **Best Practice**: Establish subscription topics before creating templates to streamline your preference management workflow.
</Tip>

## Publishing Changes

Changes you make in the Preferences Editor are saved as a **draft** and are not visible to users until you publish. Click the **Publish** button in the editor to push your changes live.

<Warning>
  If you update topics, sections, or template mappings and don't publish, the hosted preference page and embedded components will continue showing the previous published configuration. This applies to both the hosted page and React `PreferencesV4` component.
</Warning>

You can preview draft preferences before publishing by passing `draft={true}` to the `PreferencesV4` component, or by querying `draftPreferencePage` via the GraphQL API.

## Next Steps

<CardGroup cols={2}>
  <Card title="Hosted Preference Center" href="/platform/preferences/hosted-page" icon="globe">
    Deploy turnkey hosted pages for user preference management
  </Card>

  <Card title="Embedding Preferences" href="/platform/preferences/embedding-preferences" icon="react">
    Integrate preference components directly into your application
  </Card>

  <Card title="User Preferences API" href="/api-reference/user-preferences/get-users-preferences" icon="code">
    Programmatically manage user preferences and custom routing
  </Card>

  <Card title="Template Designer" href="/platform/content/template-designer/template-designer-overview" icon="paintbrush">
    Create notification templates with preference integration
  </Card>
</CardGroup>
