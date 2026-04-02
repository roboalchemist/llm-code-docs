Source: https://docs.slack.dev/changelog/2020/11/01/app-unfurls-everywhere

# App unfurls everywhere

November 1, 2020

Until now, it's often been confusing to understand when and where an app may provide customized unfurl behavior for links appearing in conversations. We're gradually rolling out changes that will make this behavior consistent and easily understood. Read on to learn more.

## What's changing? {#why}

**Note: These changes only apply to apps that use [granular bot permissions](/authentication/tokens#bot).**

Previously, Slack would only deliver [`link_shared`](/reference/events/link_shared) events for conversations your app had channel membership for. Now apps will be sent `link_shared` events for all conversation types (pubic, private, direct message, or multi-party direct message), regardless of your app or the installing user's channel membership. Your app will see more `link_shared` events than you’re used to and can use [`chat.unfurl`](/reference/methods/chat.unfurl) to act on all of them.

## When is it changing? {#when}

This new capability has been released to free teams and will gradually be released to paid teams. This change will also be active for all net new installs and reinstalls of your app.

## What happens if I do nothing? {#nothing}

If your app is subscribed to `link_shared` events and users actively mention domains your app is associated with, you will likely receive more `link_shared` events than usual. If your app runs `chat.unfurl` for every `link_shared` event, your app will unfurl more links for users. If you aren't subscribed to `link_shared` events and you do nothing, nothing happens. This change doesn't affect you but thank you for reading just the same.

## How should I prepare? {#how}

Ensure that your app is prepared for the possible uptick in event payloads from Slack. Review your app's unfurling behavior is appropriate in all conversation contexts. Remember, in order for this change to take place your app needs to use granular bot permissions.

**Tags:**

* [Announcement](/changelog/tags/announcement)
