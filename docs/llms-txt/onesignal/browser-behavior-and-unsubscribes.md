# Source: https://documentation.onesignal.com/docs/en/browser-behavior-and-unsubscribes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web push browser behavior

> Learn how to unsubscribe from notifications and understand how browsers handle web push subscriptions.

This guide explains how to manage web push [subscriptions](./subscriptions) and how subscription status is affected by both user action and browser behavior.

***

## Understand push permissions

Users must give your website permission to send them push notifications. It is not possible to receive push notifications without explicitly granting the site permission using the system-level permission prompt.

<Frame caption="Example of the Chrome required system-level permission prompt that you must click 'Allow' on to receive push notifications for this site.">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/60324a7f57f452db6054d4442689b8fb7f269f8dc123cc5b4154481ae8b89db4-Screenshot_2025-04-07_at_12.08.33_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=6d9631d8e6c3fb165068b20259df4457" width="1578" height="974" data-path="images/docs/60324a7f57f452db6054d4442689b8fb7f269f8dc123cc5b4154481ae8b89db4-Screenshot_2025-04-07_at_12.08.33_PM.png" />
</Frame>

Permissions can be either:

* **Default**: permission has not been granted to denied.
* **Granted**: you allowed the website to send you notifications.
* **Denied**: you blocked the website to send you notifications. This can be a temporary block if you clicked the **x** to close the prompt repeatedly or a permanent block if you clicked **Block** or toggled off permission in the browser settings.

<Note>
  For more details on the native system-level permission prompt and/or any of the OneSignal prompts, see [Web permission prompts](./permission-requests).
</Note>

***

## How to unsubscribe from web notifications

You can unsubscribe from web push notifications in three ways:

### Unsubscribe within browser settings

You can manage or remove notification permissions directly in browser settings. Here are quick-access URLs and official docs to learn more:

* **Chrome**: `chrome://settings/content/notifications` ([Learn more on Chrome's docs](https://support.google.com/chrome/answer/3220216?hl=en\&co=GENIE.Platform%3DDesktop\&sjid=12874758545589453111-NA))
* **Edge**: `edge://settings/content/notifications` ([Learn more on Microsoft's docs](https://www.microsoft.com/en-us/edge/learning-center/how-to-turn-off-block-browser-notifications?form=MA13I2))
* **Firefox**: `about:preferences#privacy` scroll to Permissions > Notifications > Settings ([Learn more on Mozilla's docs](https://support.mozilla.org/en-US/kb/push-notifications-firefox))
* **Safari**: Settings > Websites > Notifications ([Learn more on Safari's docs](https://support.apple.com/guide/safari/customize-website-notifications-sfri40734/16.1/mac/13.0))

On these pages, just click the options to remove or block the website(s) you don't want notifications from.

### Unsubscribe while on the website

**Reset permission**

Most browsers have a "lock" or "settings" icon next to the URL. Clicking it reveals site-specific permissions where users can disable push notifications.

<Frame caption="Example shows Chrome browser where you can toggle of push permissions for the site completely or reset permissions which will allow the site to prompt you again.">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/6264e883e1d4c19f71712be79859cf48e26a47d4283571846d3e585ca2d26d6b-Screenshot_2025-04-07_at_10.56.32_AM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=38fbcf821abf6b7077e5e4b1e736ecb9" width="1636" height="974" data-path="images/docs/6264e883e1d4c19f71712be79859cf48e26a47d4283571846d3e585ca2d26d6b-Screenshot_2025-04-07_at_10.56.32_AM.png" />
</Frame>

**OneSignal prompts**

If the website contains the OneSignal [Bell Prompt](./permission-requests) or [Custom Link prompt](./permission-requests) users can unsubscribe directly via those UI elements and be able to resubscribe using the same as desired.

<Frame caption="Example shows the OneSignal Bell Prompt.">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/400a59de59dcc7ec2cb46e09a29f99bbd1da11861bba418e76e7a0b90f86ed4d-Screenshot_2025-04-07_at_10.59.38_AM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=3226ef886346ee6abbc25ebb17abf36b" width="1636" height="974" data-path="images/docs/400a59de59dcc7ec2cb46e09a29f99bbd1da11861bba418e76e7a0b90f86ed4d-Screenshot_2025-04-07_at_10.59.38_AM.png" />
</Frame>

### Deleting browser data, clearing cookies and site data

If you delete history and/or delete your cookies and site data, it will temporarily prevent notifications from showing. However, if you don't remove push permissions from the site, you may be automatically re-subscribed and start getting notifications again upon returning to the site.

<Frame caption="Example shows clearing browser history and site data.">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5e463a765566c11fee159b98a88f0a66314be75e16d7963296b53cfb880d0640-Screenshot_2025-04-07_at_11.56.43_AM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=c133664ca1396ee6ed0dcc03c20f9c9b" width="2962" height="1458" data-path="images/docs/5e463a765566c11fee159b98a88f0a66314be75e16d7963296b53cfb880d0640-Screenshot_2025-04-07_at_11.56.43_AM.png" />
</Frame>

<br />

<Frame caption="Example shows clearing site data.">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9e18eb2c46e65b05e98bfe488268daaf8e1cb3d958767393b9e935de3189327c-Screenshot_2025-04-07_at_11.56.34_AM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=56d550b0d11955804d5b7f6a71544125" width="2962" height="1458" data-path="images/docs/9e18eb2c46e65b05e98bfe488268daaf8e1cb3d958767393b9e935de3189327c-Screenshot_2025-04-07_at_11.56.34_AM.png" />
</Frame>

***

## How to test your permission prompts

These steps explain how to test your prompt and subscription flow like a first time visitor.

<Steps>
  <Step title="Visit your site with the OneSignal SDK setup.">
    **Do not use an incognito, private, or guest browser setting.** This example uses Chrome version 135 on macOS but the flow should be relatively the same for most browsers.
  </Step>

  <Step title="Reset push permissions">
    Click the site settings or lock icon next to the site URL and select **Reset permission** or remove permissions for Notifications.
    Skip to the next step if you don't see this permission option.

    <Frame caption="Chrome site settings menu > Resetting permissions for Notifications.">
      <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0caa8967d5d339eb83795e9c8aae6fd58dfb370e7937eec2689286bc37b7d3ad-Screenshot_2025-04-07_at_1.15.10_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=cc627d94184116ba58ab88a9ebd192b3" width="1642" height="1038" data-path="images/docs/0caa8967d5d339eb83795e9c8aae6fd58dfb370e7937eec2689286bc37b7d3ad-Screenshot_2025-04-07_at_1.15.10_PM.png" />
    </Frame>
  </Step>

  <Step title="Delete site data.">
    Click **Cookies and site data > Manage on-device site data** or follow the browser's flow to see your site's data option.

    <Frame caption="Chrome's On-device site data screen.">
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3ddc97a656d2a7e72851bb723c3ef6bb7cf451f43f2980b6e16326b34ad0694d-Screenshot_2025-04-07_at_1.17.51_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=cc96365a817a37b63a008bf300dba8b2" width="1642" height="1264" data-path="images/docs/3ddc97a656d2a7e72851bb723c3ef6bb7cf451f43f2980b6e16326b34ad0694d-Screenshot_2025-04-07_at_1.17.51_PM.png" />
    </Frame>

    Delete the data for your site and exit the settings to get back to your site.

    <Frame caption="Example shows clearing your site cookies.">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/14356bf800a63a9cb7ce3396c86ab636720ff152d65f266cb253142266b246d2-Screenshot_2025-04-07_at_1.22.02_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=61dcb2f2c4967bf79dfd609b820a2507" width="1554" height="1216" data-path="images/docs/14356bf800a63a9cb7ce3396c86ab636720ff152d65f266cb253142266b246d2-Screenshot_2025-04-07_at_1.22.02_PM.png" />
    </Frame>
  </Step>

  <Step title="Open your developer tools.">Usually you can just right click the screen and press **Inspect**.</Step>

  <Step title="Follow the steps needed to prompt for push notifications and on the required system-level permission prompt, select &#x22;Allow&#x22;.">
    If you do not see the prompt or don't know the steps, see [Web permission prompts](./permission-requests).

    <Frame caption="Example shows the Chrome required system-level prompt.">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/99abfc40c2cbce6d99a32295716ba683e77a1ef4c3d8e26736d1448a62513703-Screenshot_2025-04-07_at_1.22.55_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=d522e924e8cf68c5e2e331705571159b" width="1642" height="1038" data-path="images/docs/99abfc40c2cbce6d99a32295716ba683e77a1ef4c3d8e26736d1448a62513703-Screenshot_2025-04-07_at_1.22.55_PM.png" />
    </Frame>
  </Step>

  <Step title="Check the console for any errors.">
    If you see anything in red related to OneSignal, see our [Web SDK troubleshooting](./troubleshooting-web-push) docs.
  </Step>

  <Step title="Get subscription ID">
    In the **Console** type or copy-paste this code: `OneSignal.User.PushSubscription.id`

    1. This will log your OneSignal subscription ID. Copy-paste this into your OneSignal Dashboard Audience > Subscriptions tab.
    2. If a subscription ID was not logged in the console, then you are not successfully subscribed. Please see [Web SDK troubleshooting](./troubleshooting-web-push) for details.

    <Frame caption="Getting the push subscription ID using the Console.">
      <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0585c363af7bf9154c7cd204b9ce4636049694af313c80564ab94c75dc898da3-Screenshot_2025-04-07_at_1.35.26_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=96e4c0b9515e7e62cb3e29ed0afdc8a5" width="1642" height="1038" data-path="images/docs/0585c363af7bf9154c7cd204b9ce4636049694af313c80564ab94c75dc898da3-Screenshot_2025-04-07_at_1.35.26_PM.png" />
    </Frame>

    <Frame caption="Viewing the subscription ID in the OneSignal dashboard Subscriptions page.">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/97de08625efcb3ae048d8db0ce79ab6400d4edb1e32fb586ee2ccfdec64ef533-Screenshot_2025-04-07_at_1.35.39_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=f0e59d2577e9301240efca039c941212" width="2268" height="1320" data-path="images/docs/97de08625efcb3ae048d8db0ce79ab6400d4edb1e32fb586ee2ccfdec64ef533-Screenshot_2025-04-07_at_1.35.39_PM.png" />
    </Frame>
  </Step>

  <Step title="Next to the subscription, select the 3-dot options button and &#x22;Add to Test Subscriptions&#x22;. Then name and date the test user so it is recognizable.&#x22;">
    <Frame caption="Add your subscription as a test subscription.">
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/daee83f7f444a1361390186abfd493252ae59b8ffbdb42f4a14fd979f2f9e268-Screenshot_2025-04-07_at_1.35.46_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=65ddc58a9861c912ccc19abe1225c6aa" width="2268" height="1320" data-path="images/docs/daee83f7f444a1361390186abfd493252ae59b8ffbdb42f4a14fd979f2f9e268-Screenshot_2025-04-07_at_1.35.46_PM.png" />
    </Frame>
  </Step>

  <Step title="Navigate to Messages > Push > New Message > New Push and on the Push create form add a Message.">
    See [Push](./push) for more details if needed.

    <Frame caption="Create a new push to send to your test subscription.">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2b9d9a6022f8c8566fe9ab63dde56ef8a6dc5bca9e4a1902c5b939748eea696a-Screenshot_2025-04-07_at_1.39.55_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=c153b7d978104a1639d5b2269871c7ce" width="2268" height="1320" data-path="images/docs/2b9d9a6022f8c8566fe9ab63dde56ef8a6dc5bca9e4a1902c5b939748eea696a-Screenshot_2025-04-07_at_1.39.55_PM.png" />
    </Frame>
  </Step>

  <Step title="Select &#x22;Test & Preview&#x22;, find and check your test subscription, then click &#x22;Send Test Push&#x22;.">
    <Frame caption="Send yourself a test push.">
      <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7829f46df767772414b32b05edb166a59b3d853b054263057dbb3042c1f13606-Screenshot_2025-04-07_at_1.41.19_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=b6efff85cdd63ce7b1ebfd41394d8f49" width="2268" height="1320" data-path="images/docs/7829f46df767772414b32b05edb166a59b3d853b054263057dbb3042c1f13606-Screenshot_2025-04-07_at_1.41.19_PM.png" />
    </Frame>
  </Step>

  <Step title="You should receive the push you tested.">
    If you did not receive a push, see [Web push: Notifications not shown](./notifications-not-shown-web-push) for further debugging.

    <Frame caption="Test push received.">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/81a55eefc69a1cc6e4aba2bc240e780bb8cb5bdcafac2891862e3c11f1d45591-Screenshot_2025-04-07_at_1.43.07_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=c779697abc1576141e9a542bec927be2" width="740" height="198" data-path="images/docs/81a55eefc69a1cc6e4aba2bc240e780bb8cb5bdcafac2891862e3c11f1d45591-Screenshot_2025-04-07_at_1.43.07_PM.png" />
    </Frame>
  </Step>
</Steps>

<Check>
  You have successfully setup web push with OneSignal. Next steps:

* [Web push setup](./web-push-setup) - additional non-developer web setup steps.
* [Web SDK setup](./web-sdk-setup) - developer web SDK setup steps.
* [Web SDK troubleshooting](./troubleshooting-web-push) - troubleshooting if you see errors in the console or not getting a subscription ID.
* [Web push: Notifications not shown](./notifications-not-shown-web-push) - troubleshooting notifications not displaying on your device.
</Check>

***

### Receiving Notifications When the Browser is Closed

Browsers behave differently across platforms. Please refer to the table below for support for receiving notifications even when the browser is closed.

| Browser Name      | Android | Windows | macOS |
| ----------------- | ------- | ------- | ----- |
| Chrome / Chromium | Yes     | Yes     | No    |
| Firefox           | Yes     | Yes     | No    |
| Safari            | N/A     | N/A     | Yes   |
| Opera             | Yes     | Yes     | No    |
| Edge              | Yes     | Yes     | No    |

**Chrome** - Chrome runs as a background process by default even when all the windows are closed. As long as the background process is running, notifications will still be received. If the Chrome background process is not running, notifications will not be received.

**Firefox** - On Mac OS X, the process still exists even if windows are closed, and a notification can be received if all windows are closed (as long as there is still a dot in the dock showing Firefox is still running). On Windows, the process exits after all windows are closed so notifications cannot be received unless a Firefox window is still open.

**Safari** - Safari does not have to be running to receive notifications, as they are sent directly to the operating system. The user still has to sign up for Safari web notifications, but after that they will be received even when Safari is completely closed.

Subscribers have up to 3 days to retrieve the last known missing notification before messages expire permanently.

For example, suppose a subscriber was supposed to receive a Firefox web push notification, but Firefox was closed. If the subscriber opens Firefox within 3 days, the subscriber will receive only the last known web push notification that didn't expire. If the subscriber opens Firefox after 3 days, the web push notification sent more than 3 days ago will not be received.

***

Built with [Mintlify](https://mintlify.com).
