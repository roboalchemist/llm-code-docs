# Source: https://www.courier.com/docs/platform/content/template-settings/send-conditions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Send Conditions

> Courier allows you to conditionally disable entire notifications, channels, or content blocks using data or profile properties—configured via Notification or Channel settings with customizable logic filters.

> How to set conditional send rules to disable Notifications or Channels using properties from the Send API data object or User Profile.

Using the `Conditions` functionality in the Notification and Channel settings allows you to use properties from the data or profile objects provided by the [Send API](/api-reference/send/send-a-message) call or [User Profile](/api-reference/user-profiles/get-a-profile) to prevent the notification from sending when specific conditions are met.

If you want to disable the *entire* notification, set your conditions in the [Template Settings](/platform/content/template-settings/general-settings). To disable specific Channels within the Notification, set your condition in the [Channel settings](/platform/sending/channel-settings).

<Note>
  **Channel vs Template Conditions**: For a conceptual overview of when to use channel conditions vs template conditions and how they fit into your overall channel configuration, see the [Channel Settings](/platform/sending/channel-settings#conditions) documentation.
</Note>

<Info>
  **NOTE**

  * Channel conditions only apply to the channel where you set them.
  * [User preferences](/api-reference/user-preferences/get-users-preferences) will take precedence over channel conditions. If a user has `custom_routing` configured, only channels they've selected will be considered. Channel conditions will still be evaluated for those selected channels, but cannot override the user's channel selection.
  * A channel can be disabled by using [missing variable guardrails](/platform/content/template-settings/variable-not-found).
</Info>

## Setting Send Conditions

### For Notifications and Channels

Open the Notification / Block Settings and select the Conditions tab.

<Frame caption="Template Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-conditions-settings.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=47f16c4b3bba847aa10bf62366ae3d02" alt="Template Settings" width="466" height="298" data-path="assets/platform/content/send-conditions-settings.png" />
</Frame>

<br />

<Frame caption="Channel Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-conditions-channel-settings.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=c20e31ae655536ebca1167af70df8374" alt="Channel Settings" width="1224" height="738" data-path="assets/platform/content/send-conditions-channel-settings.png" />
</Frame>

### For Content Blocks

Open the conditional settings modal from the content block you wish to set conditions to.

<Frame caption="Content Block Conditions">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-conditions-filter.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=2565c30d8bc0c131e03328f286369b57" alt="Content Block Conditions" width="1082" height="456" data-path="assets/platform/content/send-conditions-filter.png" />
</Frame>

## Setting Conditions

1. Select the `source` of the `property` and `values` to either render or hide when certain conditions are met.

<Tip>
  **TIP**

  You can access nested values using dot notation.
</Tip>

<Frame caption="Conditions Source">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-conditions-condition-filter.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=fc89797ba03211f82575c324b9a9cb5d" alt="Conditions Source" width="686" height="286" data-path="assets/platform/content/send-conditions-condition-filter.png" />
</Frame>

2. Set the property name, operator and value that you want to disable/enable the notification, channel, or content block.

<Frame caption="Condition Operators">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-conditions-operator.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=d85e07ff463db2eb83a04289cefe9637" alt="Condition Operators" width="692" height="506" data-path="assets/platform/content/send-conditions-operator.png" />
</Frame>

<Warning>
  **IMPORTANT**

  If you set multiple conditions, **all** conditions must be met to disable the message.
</Warning>

<Frame caption="Multiple Conditions">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-conditions-double.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=998109dd42a102131076e2006f1285b1" alt="Multiple Conditions" width="688" height="309" data-path="assets/platform/content/send-conditions-double.png" />
</Frame>

## Channel Conditions in JSON

Channel conditions can also be configured directly in the Send API using the `message.channels` object. Each channel can include an `if` property containing a JavaScript conditional expression.

### Basic Example

Skip SMS for premium users in Europe:

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

### Custom Routing with Channel Conditions

When using custom routing, channel conditions must be explicitly provided in `message.channels`. Conditions from the template's default routing are not automatically preserved.

<Warning>
  **Important**: When you specify a `routing` object in your message, channel conditions from the template's default routing strategy are not automatically included. You must explicitly provide channel conditions in `message.channels` if you want them evaluated.
</Warning>

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
      }
    }
  }
}
```

For more examples and details, see [Channel Settings - Channel Conditions in JSON](/platform/sending/channel-settings#channel-conditions-in-json).
