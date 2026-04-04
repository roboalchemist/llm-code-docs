# Source: https://www.courier.com/docs/platform/sending/channel-priority.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Channel Priority

> Configure Courier's channel and integration priority to control notification routing, fallbacks, and overrides—ensuring delivery via the best available method based on user data and preferences.

## Overview

Channel priority controls the order in which Courier attempts to deliver notifications across different channels and provider integrations. This configurable routing system handles message delivery to users through their most accessible channel while providing fallback options for reliable delivery.

## Key Concepts

### Priority Hierarchy

Channels and integrations are arranged in a **top-to-bottom hierarchy**. Courier attempts delivery starting from the highest priority option and moves down the list until successful delivery or all options are exhausted. However, user preferences will supersede these configurations, resulting in the following rule order:

1. **User Preferences**: Individual recipient settings override all other routing rules
2. **Channel Priority**: Order of channels (email, SMS, push, etc.)
3. **Integration Priority**: Order of providers within each channel (e.g., SendGrid vs Mailgun for email)

### Routing Methods

* **"Best Of"**: Try channels in priority order until one succeeds
* **"Always Send"**: Send through specific channels regardless of priority hierarchy

## Configuring Priority

### Setting Channel and Integration Priority

Priority is managed through a simple drag-and-drop interface. Channels and integrations are arranged in a top-to-bottom hierarchy:

<Frame caption="Priority Settings">
    <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/sending/priority-settings.gif?s=98bd825761abc12828d20594ec6bfd36" alt="Always Send Routing" width="714" height="378" data-path="assets/platform/sending/priority-settings.gif" />
</Frame>

## How Priority Works

### Priority Logic Flow

Courier follows this decision process for each recipient:

1. **Check highest priority channel** - Does the user have the required contact info (email address, phone number, device token, etc.)?
2. **Attempt delivery** - Try the preferred integration for that channel
3. **Handle failures** - If delivery fails, try the next integration if available or move on to next channel
4. **Continue until success** - Stop when message is successfully delivered

### Integration Priority Within Channels

Within each channel, you can configure multiple provider integrations with their own priority order:

<Frame caption="Integration Priority">
    <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/sending/priority-integrations.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=9504be119df662bf569819ff9eadd31a" alt="Integration Priority" width="2028" height="1270" data-path="assets/platform/sending/priority-integrations.png" />
</Frame>

**Integration Fallback Logic:**

* **Primary**: SendGrid attempts delivery first
* **Fallback**: If SendGrid fails, Mailgun attempts delivery

Using multiple providers can help increase reliability and delivery rates.

<Info>
  **Cost Optimization Tip**: You can combine multiple providers with condition rules around location to help control costs for a channel by using the best provider for that location.
</Info>

## Always Send Rule

The "Always Send" option overrides priority hierarchy to guarantee delivery through specific channels. This is useful for critical notifications that must reach users through multiple channels.

#### How Always Send Works

**Example**: Notification configured for **SMS → Slack → Email** with **Email set to "Always Send"**

**Result for each user:**

* **User with phone + Slack + email** → Gets Email + SMS ✅
* **User with Slack + email only** → Gets Email + Slack ✅
* **User with email only** → Gets Email ✅
* **User with no email** → No delivery ❌

#### Configuring Always Send

Set the "Always Send" option in the Channel Settings for any channel:

<Frame caption="Channel Settings">
    <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/priority-channel-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=376cf511d0203ef4391d2a7faf48d485" alt="Channel Settings" width="982" height="354" data-path="assets/platform/sending/priority-channel-settings.png" />
</Frame>

<Frame caption="Always Send Routing">
    <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/sending/priority-always.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=12bd6c495447b0f08c5b332bf1fc0883" alt="Always Send Routing" width="1936" height="1224" data-path="assets/platform/sending/priority-always.png" />
</Frame>

## User Preferences Override

You can let your users override all priority and always send rules through preference centers. Users can set their preferred notification channels using either Courier's [hosted preference center](/platform/preferences/hosted-page) or a custom preference center you build using the [Preferences API](/api-reference/user-preferences/get-users-preferences). When users have specific channel preferences configured, Courier respects these choices above all other routing rules.

### Priority Override Hierarchy

1. **User Preferences** (highest priority)
2. **Always Send rules**
3. **Channel Priority hierarchy** (lowest priority)

This allows users to maintain control over how they receive notifications while providing defaults for users who haven't set preferences.

<Note>
  **User Control**: User preferences take precedence over all other routing configurations. This gives recipients final control over their notification delivery experience.
</Note>

## Putting It All Together

### Example: Multi-Channel Fallback

Consider a notification configured to send via **SMS → Slack → Email** in priority order:

<Frame caption="Priority Routing Overview">
    <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/sending/priority-routing-overview.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=ed2322e59adb6e2e0a7e22ed2dea08b8" alt="Priority Routing Overview" width="1236" height="758" data-path="assets/platform/sending/priority-routing-overview.png" />
</Frame>

**Delivery Logic:**

* **User has phone number** → Sends via SMS (Twilio) ✅ Done
* **User has no phone, but has Slack** → Sends via Slack ✅ Done
* **User has no phone or Slack, but has email** → Sends via Email ✅ Done
* **User has none of the above** → Delivery fails ❌
* **User has phone and Slack, but turned off phone notifications in their preferences** → Sends via Slack, logs reflect unsubscribed from text notifications ✅ Done

This example demonstrates how all three priority concepts work together: user preferences override everything, then channel priority determines the fallback order, and integration priority handles provider-level routing within each channel.

## Use Cases

### When to Use Each Approach

* **Channel Priority**: Standard fallback logic for reliable delivery
* **Always Send**: Critical notifications that must reach users through multiple channels
* **User Preferences**: Let users customize their notification experience

### Best Practices

* **Start with priority hierarchy** for most notifications
* **Use always send sparingly** for truly critical messages only
* **Respect user preferences** to maintain good user experience
* **Test with multiple provider integrations** to improve delivery rates

## Related Resources

<CardGroup cols={2}>
  <Card title="Channel Settings" href="/platform/sending/channel-settings" icon="gear">
    Configure individual channel behavior and routing rules
  </Card>

  <Card title="User Preferences" href="/platform/preferences/hosted-page" icon="user">
    Learn how users can control their notification preferences
  </Card>
</CardGroup>
