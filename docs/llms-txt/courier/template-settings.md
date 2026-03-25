# Source: https://www.courier.com/docs/platform/content/design-studio/template-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Settings

> Configure template settings in Design Studio, including name, alias, conditions, subscription topics, and channel settings.

Access template settings by clicking the **gear icon** in the template editor toolbar. The settings panel includes template-level configuration and per-channel settings.

<Frame caption="Template Settings Panel">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-settings.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=51d718dc28400e932d5e147f1f6366ff" alt="Template settings panel in Design Studio" width="1960" height="1518" data-path="assets/platform/content/designer-v2/designer-v2-settings.png" />
</Frame>

## Template settings

### General

| Setting                | Description                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Template Name**      | Display name for the template in your template list                                                                                                                               |
| **Template ID**        | Unique identifier used when sending notifications via API. Click the copy icon to copy.                                                                                           |
| **Subscription Topic** | Group templates under a subscription topic to let end users manage preferences for multiple notifications at once. See [Preferences](/platform/preferences/preferences-overview). |
| **Message Tags**       | Tags applied to all messages sent from this template. Useful for filtering in logs and analytics. Tags cannot be changed after messages are sent.                                 |
| **Delete Template**    | Permanently delete the template. This action cannot be undone.                                                                                                                    |

### Alias

Create aliases for your template to use in API calls instead of the Template ID. Aliases make your API calls more readable and let you change the underlying template without updating your application code.

<Frame caption="Template Aliases">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-alias.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=ab1e3d71009b504b2f6c55e3f4cb03b9" alt="Template alias configuration" width="1600" height="698" data-path="assets/platform/content/designer-v2/designer-v2-alias.png" />
</Frame>

For example, if you create an alias `order-confirmation`, you can reference it in your Send API call:

```json  theme={null}
{
  "message": {
    "template": "order-confirmation",
    "to": { "user_id": "user_123" }
  }
}
```

<Note>
  Each alias can only be mapped to one template at a time.
</Note>

### Conditions

Enable or disable the entire template based on conditions evaluated at send time. These conditions apply to all channels in the template, not to a specific channel or integration.

<Frame caption="Template Conditions">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-conditions.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=8d1cc9ab72206cb6df619f0a34d71bc5" alt="Template conditions configuration" width="1610" height="644" data-path="assets/platform/content/designer-v2/designer-v2-conditions.png" />
</Frame>

* **Conditions role**: Toggle between Enable (send if conditions match) or Disable (skip if conditions match)
* **Add condition**: Click to add conditions based on data passed in your API request

## Channel settings

Each channel configured in your template has its own settings section. Click a channel in the sidebar to configure channel-specific options.

Channel settings vary by channel type but may include:

* **Provider configuration** - Which integration to use for sending
* **Channel-specific conditions** - Send conditions that apply only to this channel
* **Formatting options** - Channel-specific formatting like email subject lines

<Note>
  For the classic designer settings documentation, see [General Settings](/platform/content/template-settings/general-settings).
</Note>

## Related

<CardGroup cols={2}>
  <Card title="Routing" icon="route" href="/platform/content/template-designer/routing-configuration">
    Configure channel routing
  </Card>

  <Card title="Preferences" icon="bell" href="/platform/preferences/preferences-overview">
    User notification preferences
  </Card>
</CardGroup>
