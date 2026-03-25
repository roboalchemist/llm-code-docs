# Source: https://www.courier.com/docs/platform/sending/channel-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Channel Settings

> Channel Settings let you configure delivery rules, priorities, and integrations per channel—enabling conditional logic, advanced email options, and precise control over notification behavior.

## Overview

Channel Settings provide granular control over how each notification channel behaves. You can configure delivery rules, set conditions for when channels should send, and manage provider integrations—all from a centralized interface within each template.

## Key Configuration Areas

Channel Settings are organized into three main sections:

* **General**: Basic channel behavior, naming, and send logic
* **Conditions**: Rules that determine when a channel should or shouldn't send
* **Integrations**: Provider configuration and send priority settings

## Opening the Channel Settings

To view the Channel Settings, open the Template in the designer list, then click the settings icon next to the channel's name.

<Frame caption="Channel Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/channel-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=8412d9db61ac248b6b72b95d40b6595f" alt="Channel Settings" width="648" height="572" data-path="assets/platform/sending/channel-settings.png" />
</Frame>

## General Settings

<Frame caption="General Template Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/channel-general-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=6cd3851ea5750982efec37011e95b65d" alt="General Template Settings" width="964" height="654" data-path="assets/platform/sending/channel-general-settings.png" />
</Frame>

### Always Send To

This setting controls how the channel behaves in relation to other channels:

* **"Best Of"**: The channel only sends if higher-priority channels fail. This is ideal for fallback scenarios (e.g., SMS as backup when email fails).

* **"Always"**: The channel sends to every recipient regardless of other channels' success. Use this when you want guaranteed delivery through multiple channels (e.g., both email and push for important notifications).

<Note>
  **Channel Priority**: The "Best Of" setting works with the [channel priority hierarchy](/platform/sending/channel-priority) to create configurable fallback logic. Higher-priority channels attempt delivery first.
</Note>

### Disable

* When set to Disabled, the Channel will not send under any conditions and will be skipped in the "Best of" Channel send hierarchy.

### Email-Specific Settings

Email channels include additional configuration options for sender information and recipients:

* **From address**: Set the sender email address and display name using the format `"FirstName LastName <email@domain.com>"`
* **Reply-To address**: Specify where replies should be directed
* **CC/BCC addresses**: Add additional recipients using [replacement variables](/platform/content/variables/inserting-variables) for dynamic values

<Note>
  **Complete Email Configuration**: For detailed guidance on email address configuration, including provider defaults, override hierarchy, and advanced formatting options, see [Customizing Email Address Fields](/platform/content/template-settings/email-fields).
</Note>

<Frame caption="Email Specific Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/channel-email-specific.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=9233f6b177d90730ed3d758747ade874" alt="Email Specific Settings" width="1224" height="811" data-path="assets/platform/sending/channel-email-specific.png" />
</Frame>

## Conditions

Channel conditions allow you to prevent a specific channel from sending based on data or profile properties, while other channels in the same notification can still deliver successfully.

### How Channel Conditions Work

Unlike template-level conditions that disable entire notifications, channel conditions only affect the specific channel where they're configured:

* **Template conditions**: Stop the entire notification from sending
* **Channel conditions**: Skip only this channel, other channels continue normally

### Setting Channel Conditions

<Note>
  **Detailed Implementation**: For step-by-step instructions on setting up channel conditions, including operators, multiple conditions, and UI guidance, see [Using Send Conditions](/platform/content/template-settings/send-conditions).
</Note>

1. Open the channel settings and navigate to the **Conditions** tab
2. Select the **source** (data or profile) for your condition
3. Set the **property name**, **operator**, and **value**
4. Add multiple conditions if needed (choose from or / and operators)

<Frame caption="Channel Conditions Configuration">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/channel-conditions.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=10bb807917f3982ccdb0677ea78bdb4e" alt="Channel conditions interface showing data source selection, property name field, operator dropdown, and value input" width="2030" height="1185" data-path="assets/platform/sending/channel-conditions.png" />
</Frame>

<Note>
  **Multiple Conditions**: When you set multiple AND conditions, **all** conditions must be met to disable the channel. Use this for complex logic like "skip SMS if user is premium AND in Europe."
</Note>

<Info>
  **User Preferences Override**: User preferences take precedence over channel conditions. If a user has `custom_routing` configured in their preferences, only the channels they've selected will be considered for delivery. Channel conditions will still be evaluated for those selected channels, but cannot override the user's channel selection.
</Info>

### Channel Conditions in JSON

Channel conditions can be configured in the Send API using the `message.channels` object. Each channel can include an `if` property containing a JavaScript conditional expression that evaluates against `data` and `profile` objects.

#### Basic Channel Condition Example

Skip SMS for premium users who are in Europe:

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-confirmation",
    "data": {
      "order_id": "ORD-12345",
      "region": "europe"
    },
    "channels": {
      "sms": {
        "if": "profile.custom.subscription_tier === 'premium' && data.region === 'europe'"
      }
    }
  }
}
```

In this example, the SMS channel will be skipped if the user's subscription tier is "premium" AND the order region is "europe". Email and other channels will continue to send normally.

#### Multiple Channel Conditions

Apply different conditions to multiple channels:

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-confirmation",
    "data": {
      "order_id": "ORD-12345",
      "urgency": "high",
      "region": "europe"
    },
    "channels": {
      "sms": {
        "if": "data.urgency !== 'high'"
      },
      "push": {
        "if": "profile.custom.notifications_enabled === true"
      },
      "email": {
        "if": "data.region !== 'europe' || profile.custom.email_opt_in === true"
      }
    }
  }
}
```

#### Channel Conditions with Custom Routing

When using custom routing, channel conditions must be explicitly provided in `message.channels`. Channel conditions configured in the template's default routing strategy are not automatically included when custom routing is specified.

<Warning>
  **Important**: When you specify a `routing` object in your message, channel conditions from the template's default routing are not preserved. You must explicitly include channel conditions in `message.channels` if you want them evaluated.
</Warning>

Example combining custom routing with channel conditions:

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-confirmation",
    "data": {
      "order_id": "ORD-12345",
      "urgency": "high"
    },
    "routing": {
      "method": "single",
      "channels": ["email", "sms", "push"]
    },
    "channels": {
      "sms": {
        "if": "data.urgency === 'high'"
      },
      "push": {
        "if": "profile.custom.push_enabled === true"
      }
    }
  }
}
```

In this example:

* Custom routing is set to `single` method with email, SMS, and push channels
* SMS will only send if `data.urgency === 'high'`
* Push will only send if the user has push notifications enabled in their profile
* Email will send regardless (no condition specified)

#### Channel Conditions with User Custom Routing

When a user has `custom_routing` configured in their preferences, those preferences take precedence over channel conditions. However, you can still apply channel conditions to channels that are included in the user's custom routing:

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-confirmation",
    "data": {
      "order_id": "ORD-12345",
      "time_of_day": "night"
    },
    "channels": {
      "push": {
        "if": "data.time_of_day !== 'night'"
      },
      "sms": {
        "if": "data.urgency === 'high'"
      }
    }
  }
}
```

<Info>
  **User Preferences Priority**: If a user has `custom_routing` configured (e.g., they only want email), channel conditions will not override their preference. The user's selected channels in `custom_routing` take precedence.
</Info>

## Integrations

Each channel can use multiple provider integrations for redundancy and performance. The integrations section lets you:

* **View existing integrations** that are already configured for this channel
* **Add new providers** to expand your delivery options
* **Set send priority** to determine which provider to use first
* **Configure provider-specific settings** like API keys and delivery parameters

<Frame caption="Channel Integrations">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/channel-integrations.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=5556d80c29851e5406d8ec686bf50145" alt="Channel Integrations" width="1196" height="488" data-path="assets/platform/sending/channel-integrations.png" />
</Frame>

<br />

<Frame caption="Channel Integration Configs">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/channel-integration-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=18d44e82d1563871c9cbee3bb32bad63" alt="Channel Integration Configs" width="1224" height="811" data-path="assets/platform/sending/channel-integration-settings.png" />
</Frame>

## Related Resources

<CardGroup cols={2}>
  <Card title="Channel Priority" href="/platform/sending/channel-priority" icon="route">
    Learn how to set up configurable fallback logic between channels
  </Card>

  <Card title="Send Conditions" href="/platform/content/template-settings/send-conditions" icon="filter">
    Step-by-step guide for implementing channel and template conditions
  </Card>
</CardGroup>
