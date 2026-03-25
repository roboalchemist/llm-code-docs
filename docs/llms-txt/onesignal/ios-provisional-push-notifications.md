# Source: https://documentation.onesignal.com/docs/en/ios-provisional-push-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS provisional push notifications

> Provisional push notifications on iOS let your app send notifications without an upfront permission prompt, but with reduced visibility.

Provisional push notifications (also known as Direct-to-History) are an iOS 12+ feature that lets your app send push notifications without first requesting explicit permission. Users receive these notifications silently in the Notification Center, giving them a chance to decide whether to keep or turn off notifications from your app.

Because these notifications are provisional, they have reduced visibility compared to standard push notifications:

* No banner displayed
* No sound played
* No lock-screen alert
* Delivered directly to the Notification Center

<Frame caption="Provisional notification prompting the user to keep or turn off notifications">
  <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/ios-provisional-push-notifications.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=7c07a624b367b7c4cbf0572a7464311c" alt="iOS provisional push notification with Keep and Turn Off options" width="1062" height="585" data-path="images/push/ios-provisional-push-notifications.jpg" />
</Frame>

## How users interact with provisional notifications

When a user receives a provisional notification, they can select **Keep...** to see these options:

* **Deliver Quietly** — Keeps notifications silent and only visible in the Notification Center. This also removes the "Keep..." and "Turn Off..." prompts from future notifications.
* **Turn Off** — Unsubscribes the user from all notifications from your app.

<Frame caption="Options shown when a user taps Keep on a provisional notification">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/e9db683-example-notification2_1.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=aa1d5f60ea23667b74a603406b4ca78d" alt="iOS prompt showing Deliver Quietly, Turn Off, and Settings options" width="2460" height="2172" data-path="images/docs/e9db683-example-notification2_1.png" />
</Frame>

You can still prompt users for standard push permission even after they choose Deliver Quietly or Turn Off. However, if you prompt for regular push permission and the user denies it, they will not receive any further push notifications — including provisional ones.

***

## Enable or disable provisional authorization

To toggle provisional authorization, go to your OneSignal dashboard: **Settings > Apple iOS > Advanced Configuration** and check or uncheck the **Enable iOS 12 direct to history** option. This is unchecked by default.

<Note>
  Provisional authorization requires OneSignal SDK 2.9.0 or newer.
</Note>

<Frame caption="OneSignal dashboard setting for iOS 12 provisional push authorization">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/402336e-Screenshot_2024-02-20_at_6.13.14_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=1fa68a726a6100f95c00e2c419696b64" alt="OneSignal Advanced Configuration panel with the iOS 12 direct to history checkbox" width="1608" height="804" data-path="images/docs/402336e-Screenshot_2024-02-20_at_6.13.14_PM.png" />
</Frame>

***

## FAQ

### What is the difference between provisional and normal authorization?

With provisional authorization enabled, iOS 12+ subscribers automatically receive push notification permissions the next time they open your app — no permission prompt is shown. Your app can still request standard push permissions separately, which displays the native iOS permission prompt. If the user denies that standard prompt, provisional notifications are also turned off.

For details on configuring your permission prompting flow, see [Prompt for push permissions](./prompt-for-push-permissions).

### What happens if a user denies the regular push prompt?

Denying the standard iOS push permission prompt turns off all push notifications for your app, including provisional notifications. The user would need to re-enable notifications manually through iOS Settings.

***

<Card title="Prompt for push permissions" icon="bell" href="./prompt-for-push-permissions">
  Configure when and how your app requests standard push notification permissions from users.
</Card>

Built with [Mintlify](https://mintlify.com).
