# Source: https://documentation.onesignal.com/docs/en/channel-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Channel setup

> Set up push notifications, in-app messages, email, SMS, RCS, and Live Activities in OneSignal to reach Users across every channel.

OneSignal supports multiple messaging channels, each with different capabilities and setup requirements. Choose the channels that match your goals, or combine several to build a multi-channel experience with [Journeys](./journeys-overview).

<Tip>
  Email and SMS can be configured without a developer. Push notifications, in-app messages, and Live Activities require SDK integration — see the [Developer guide](./developers) or [invite a developer](./manage-team-members) to your team.
</Tip>

***

## Messaging channels

<Columns cols={3}>
  <Card title="Mobile push" icon="mobile" href="./mobile-push-setup">
    Alert-style notifications on iOS, Android, Huawei, and Amazon — even when the app isn't open.
  </Card>

  <Card title="Web push" icon="globe" href="./web-push-setup">
    Browser-based notifications that reach Users even when your site isn't open.
  </Card>

  <Card title="Email" icon="envelope" href="./email-setup">
    Marketing and transactional emails with built-in deliverability tools.
  </Card>

  <Card title="In-app messages" icon="window-maximize" href="./in-app-messages-setup">
    Rich, interactive messages displayed while Users are active in your app.
  </Card>

  <Card title="SMS" icon="comment-sms" href="./sms-setup">
    Direct text messages for urgent or time-sensitive communication.
  </Card>

  <Card title="RCS" icon="message" href="./rcs-messaging">
    Rich messaging with branded content and read receipts on Android.
  </Card>

  <Card title="Live Activities" icon="tower-broadcast" href="./live-activities">
    Real-time updates on the iOS lock screen. Similar capabilities available for Android.
  </Card>
</Columns>

***

## Channel comparison

| Channel         | Developer required? | Setup time | Best for                                                 |
| --------------- | ------------------- | ---------- | -------------------------------------------------------- |
| Email           | No                  | 15–60 min  | Marketing campaigns, transactional messages, newsletters |
| SMS             | No                  | 15–60 min  | Time-sensitive alerts, OTPs, appointment reminders       |
| Web push        | Yes                 | 15–45 min  | Re-engaging website visitors, announcements              |
| Mobile push     | Yes                 | 30–60 min  | App re-engagement, real-time alerts, promotions          |
| In-app messages | Yes (SDK)           | 30–45 min  | Onboarding, feature announcements, surveys               |
| RCS             | No                  | Varies     | Rich branded messaging on Android with read receipts     |
| Live Activities | Yes (SDK)           | 45–60 min  | Live scores, delivery tracking, event countdowns         |

***

## Next steps

After setting up a channel, continue with the rest of your OneSignal implementation.

<Columns cols={2}>
  <Card title="Quickstart guide" icon="rocket" href="./quickstart-guide">
    Full implementation walkthrough: Users, segments, sending messages, and analytics.
  </Card>

  <Card title="Developer guide" icon="code" href="./developers">
    SDK reference, API docs, User identity, and testing for engineering teams.
  </Card>

  <Card title="Send messages" icon="paper-plane" href="./push">
    Compose and send your first message after setting up a channel.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Automate multi-channel flows based on User behavior.
  </Card>
</Columns>

***

## FAQ

### Which channel should I set up first?

Start with the channel that matches your most immediate goal. **Email** and **SMS** are the fastest to configure and don't require a developer. If you already have a mobile app, **push notifications** provide the highest visibility for re-engagement.

### Can I use multiple channels in the same OneSignal app?

Yes. A single OneSignal app supports all channels. Adding multiple channels lets you use [Journeys](./journeys-overview) to automate multi-channel flows — for example, sending a push notification, then following up with an email if the User doesn't engage.

### Do I need separate apps for testing and production?

Yes, this is strongly recommended. Use separate OneSignal apps for development, staging, and production to avoid sending test messages to real Users. See [Apps, Organizations, and accounts](./apps-organizations) for details.

Built with [Mintlify](https://mintlify.com).
