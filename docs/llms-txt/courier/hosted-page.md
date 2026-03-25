# Source: https://www.courier.com/docs/platform/preferences/hosted-page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hosted Preference Center

> Deploy a customizable, Courier-hosted page where users can manage notification preferences, delivery channels, and unsubscribe settings.

## Overview

The Hosted Preference Center provides a turnkey solution for user preference management without any development effort required. Courier hosts and maintains the preference interface, handling user authentication, preference updates, and data persistence while you focus on your core application. Users access their preferences through a branded, responsive interface that seamlessly integrates with your notification workflow.

<Frame caption="Hosted Preference Center">
  <img src="https://mintcdn.com/courier-4f1f25dc/LOc9porYE6seha13/assets/platform/preferences/preferences-hosted-page.png?fit=max&auto=format&n=LOc9porYE6seha13&q=85&s=95a1b3746858ef3bb66ec549aa394e56" alt="Hosted Preference Center" width="1003" height="972" data-path="assets/platform/preferences/preferences-hosted-page.png" />
</Frame>

## Key Features

* **Zero Development Required** - Fully hosted solution with automatic updates and maintenance
* **Custom Branding** - Match your brand colors, logos, and styling for consistent user experience
* **Subscription Management** - Users can opt in/out of notification topics you've configured
* **Channel Selection** - Enterprise customers can enable user choice of delivery channels (email, SMS, push, chat)
* **Unsubscribe Handling** - Built-in compliance with one-click unsubscribe and confirmation pages
* **Mobile Responsive** - Optimized interface that works across all devices and screen sizes

## Core Components

#### Preference Center URLs

Insert preference center URL variables in your notification templates to provide users with secure, auto-generated links to their preference management interface.

**Variable Format by Context:**

* **Content Blocks** (Text, Markdown, Quote, List): `{$.urls.preferences}`
* **Handlebars Templates** (Template blocks, Email templates, Brand templates): `{{var "urls.preferences"}}`
* **Elemental JSON** (Action buttons, link elements): `"href": "{$.urls.preferences}"`

**Elemental Example:**

```json  theme={null}
{
  "type": "action",
  "content": "Manage Preferences",
  "href": "{$.urls.preferences}",
  "style": "button"
}
```

<Note>
  **User ID Required**: Include `to.user_id` in your [Send request](/api-reference/send/send-a-message) for preference links to work correctly. The user ID maps recipients to their preference profiles.

  **Variable Context Matters**: Using the wrong format will prevent the URL from rendering correctly. For comprehensive variable documentation, see [Inserting Variables](/platform/content/variables/inserting-variables).
</Note>

#### Implementation Options

**In Notification Content**

Add preference links directly within notification body content for contextual access to settings.

<Frame caption="Preference Link in Notification">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-hyperlink.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=cce81c10dc51755c514b979daf563514" alt="Preference Link in Notification" width="1842" height="1086" data-path="assets/platform/preferences/preferences-hyperlink.png" />
</Frame>

**In Brand Footer**

Include preference links in your brand footer for consistent access across all notifications.

<Frame caption="Preference Link in Brand Footer">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-brand-with-link.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=bd67eab421b0d2821c2061fcd3303ebf" alt="Preference Link in Brand Footer" width="1376" height="1054" data-path="assets/platform/preferences/preferences-brand-with-link.png" />
</Frame>

<Note>
  **Preview Behavior**: Preview emails show mock URLs instead of functional preference links since they're not sent to actual users.
</Note>

### Unsubscribe Management

#### Quick Unsubscribe Links

Provide users with one-click unsubscribe functionality using unsubscribe URL variables. This link removes users from the specific subscription topic associated with the notification.

**Variable Format by Context:**

* **Content Blocks** (Text, Markdown, Quote, List): `{$.urls.unsubscribe}`
* **Handlebars Templates** (Template blocks, Email templates, Brand templates): `{{var "urls.unsubscribe"}}`
* **Elemental JSON** (Action buttons, link elements): `"href": "{$.urls.unsubscribe}"`

**Elemental Example:**

```json  theme={null}
{
  "type": "action",
  "content": "Unsubscribe",
  "href": "{$.urls.unsubscribe}",
  "style": "link"
}
```

<Note>
  **Variable Context Matters**: Using the wrong format will prevent the URL from rendering correctly. For comprehensive variable documentation, see [Inserting Variables](/platform/content/variables/inserting-variables).
</Note>

<Frame caption="Unsubscribe Link">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-unsubscribe.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=bb9cec4eab6e5b54c62f627a33f882f4" alt="Unsubscribe Link" width="2332" height="1242" data-path="assets/platform/preferences/preferences-unsubscribe.png" />
</Frame>

#### Unsubscribe Confirmation

Users who click unsubscribe links are redirected to a confirmation page that clearly indicates their subscription status and provides options for preference management.

<Frame caption="Unsubscribe Confirmation Page">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-unsubscribe-page.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=a60e718007d96eb8933c7e298de2b817" alt="Unsubscribe Confirmation Page" width="846" height="462" data-path="assets/platform/preferences/preferences-unsubscribe-page.png" />
</Frame>

<Note>
  **Scope**: Unsubscribe links remove users from the entire subscription topic, including all associated notification templates and delivery channels.
</Note>

### Customization Options

#### Brand Integration

The hosted preference center automatically applies your [brand styling](/platform/content/brands/brands-overview) including logos, colors, and typography from your [default brand configuration](https://app.courier.com/database/brands).

#### Channel Selection

<Note>
  **Availability**: Delivery Channel customization is available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) for access or [Request a Demo](https://www.courier.com/request-demo) to learn more about how Courier could help you.
</Note>

Enterprise customers can enable users to select their preferred delivery channels for each subscription topic. User selections are reflected in the `custom_routing` array when querying the [User Preferences API](/api-reference/user-preferences/get-user-subscription-topic).

```json  theme={null}
{
  "topic": {
    "custom_routing": [
      "email"
    ],
    "has_custom_routing": true,
    "default_status": "OPTED_IN",
    "section_id": "_ysuowndfnousd",
    "section_name": "Notifications",
    "status": "OPTED_IN",
    "topic_id": "TOPIC_ID",
    "topic_name": "Tips and Tricks"
  }
}
```

<Warning>
  **Channel Conditions**: Template-level [send conditions](/platform/content/template-settings/send-conditions) will not override user `custom_routing` preferences. Use [variable guardrails](/platform/content/template-settings/variable-not-found) to disable channels when required data is missing.
</Warning>

## Implementation Workflow

### Setup and Configuration

1. **Configure Subscription Topics** - Use the [Preferences Editor](/platform/preferences/preferences-editor) to create notification categories
2. **Map Templates** - Associate notification templates with subscription topics for automatic preference enforcement
3. **Add Preference Links** - Insert `{$.urls.preferences}` variables in templates or brand footers
4. **Test User Flow** - Preview the preference center and verify user experience

### Preview and Testing

Preview your hosted preference center before deploying:

<Frame caption="Preference Center Preview">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/preferences/preferences-preview-page.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=b2c41a0d3626e8af7c9117d1adfd00d9" alt="Preference Center Preview" width="1564" height="524" data-path="assets/platform/preferences/preferences-preview-page.png" />
</Frame>

Access preview functionality through the [Preferences Editor](https://app.courier.com/settings/preferences) to validate styling, content, and user workflow.

<Tip>
  **Best Practice**: Test preference changes with real user data to ensure notifications respect user choices and custom routing works as expected.
</Tip>

## Next Steps

<CardGroup cols={2}>
  <Card title="Preferences Editor" href="/platform/preferences/preferences-editor" icon="gear">
    Configure subscription topics and preference sections for your hosted center
  </Card>

  <Card title="Embedding Preferences" href="/platform/preferences/embedding-preferences" icon="react">
    Compare with embedded preference components for in-app integration
  </Card>

  <Card title="User Preferences API" href="/api-reference/user-preferences/get-users-preferences" icon="code">
    Programmatically query and manage user preference data
  </Card>

  <Card title="Brand Management" href="/platform/content/brands/brands-overview" icon="paintbrush">
    Customize the visual styling of your hosted preference center
  </Card>
</CardGroup>
