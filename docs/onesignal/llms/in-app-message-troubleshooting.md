# Source: https://documentation.onesignal.com/docs/en/in-app-message-troubleshooting.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app troubleshooting

> Common questions and troubleshooting steps about in-app messages.

This guide covers common questions and troubleshooting steps about in-app messages.

## Advanced design troubleshooting

How to check the in-app design across different devices while using the browser. These steps use Chrome version 138 on macOS.

1. Open the in-app message block editor.
2. In the preview, right click any in-app message block and select "Inspect".
3. In the Elements tab, go up the DOM tree to find the `#document` element.

<Frame caption="The #document element in the Elements tab of the in-app message block editor">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/inspect-iam-block-editor.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=26dcab4bc1031fafef7dacb14031a820" alt="The #document element in the Elements tab of the in-app message block editor" width="2844" height="1498" data-path="images/iam/inspect-iam-block-editor.png" />
</Frame>

1. Right click the link in the `#document` element and select "Open in new tab".
2. You will see the in-app message design in a new tab.
3. Right click the new tab's in-app message design and select "Inspect" again.
4. In the Elements tab, select the "Toggle device toolbar" button.

<Frame caption="The Toggle device toolbar button in the Elements tab of the in-app message block editor">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/inspect-iam-device-toggle.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=944c8b5d5a2fbfb575e18a5fb9b131b2" alt="The Toggle device toolbar button in the Elements tab of the in-app message block editor" width="2864" height="1408" data-path="images/iam/inspect-iam-device-toggle.png" />
</Frame>

1. Update the dimensions to see how it would look on different devices. We recommend testing on the `iPhone SE` (375x667) and `iPad Pro` (1024x1366).

<Frame caption="Test different device dimensions from within Chrome DevTools">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/inspect-iam-device-test.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=74f62633c6bd843a7e6e5cd8b3209b06" alt="Test different device dimensions from within Chrome DevTools" width="1258" height="1548" data-path="images/iam/inspect-iam-device-test.png" />
</Frame>

## What are the minimum Android and iOS versions that can receive in-app messages?

The minimum Android version that can receive in-app messages is 4.4. If a device is under this version the in-app message will not show.

The minimum iOS version that can receive in-app messages is 10.0. If a device is under this version the in-app message will not show.

## What are the recommended image dimensions?

We show In-App messages based on the dimensions of the phone currently being displayed on. There are a few common aspect ratios for devices and resolutions (especially for Android) which could all affect the viewing of the In-App messages.

A `16:9` aspect ratio is the most common for devices, but `4:3` and `3:2` aspect ratios are close compromises.

## Can I create an in-app via the API?

Currently all In-App messages need to be created through the OneSignal dashboard.

On each page of your app, you can set our `addTrigger` method and through your own API requests to your app, feed in the trigger `key:value` set within the dashboard to trigger the IAM based on your own network requests.

## I've updated my in-app, when do in-app changes take effect?

Once you update an In-App messages from the dashboard. The changes will go into effect immediately and end-users will see the updated message after the app has been closed for 30 seconds before re-opened.

More details, see: [Why is IAM Data Not Updating?](#why-are-in-app-messages-data-not-updating).

## Is tag substitution or message personalization available?

Yes, Tag Substitution will be supported only on iOS SDK version 2.16.4+ and Android SDK version 3.16.0+

You can use data tags to personalize the content and click action behavior of your users.

## How do I send in-apps with message localization?

Currently, you can set up different in-app messages for different languages and target a [Segment](./segmentation) based on the device language filter.

## Why are my in-app messages showing blank or all white?

In-app messages use webviews to display the content. If you are sending content within the message but it shows blank, then you may be changing the layout constraints. Check your app's custom webview settings. A common example to check on Android is the `WindowManager.LayoutParams`.

## Why are in-app messages' data not updating?

### Design updates

Changes made to the In-App Message within the OneSignal dashboard will reflect in the app once the app has been closed for 30 seconds. Make sure after you save any changes to the IAM, you have the app closed or put into the background for 30 seconds, then when you open it, you will see the changes upon the next time it is triggered.

Using the **Send to Test Device** button does not reflect any Tag Substitutions. You must trigger the IAM normally to see Tag Substitution Personalizations.

### Analytics, clicks, impressions updates

Using the **Send to Test Device** button does not contribute to the IAM analytics. You must trigger the IAM without using this button to see stats updates.

If you are not using the **Send to Test Device** button then you can troubleshoot the issue following this guide on [Capturing a Debug Log](./capturing-a-debug-log). If you still need assistance, share the full logs from app start till the end of reproduction as a .txt file with our support team at `support@onesignal.com`.

## Duplicated in-app messages

Common reasons In-App Messages may appear duplicated on the device are:

* Multiple IAMs that look the same are active.
* The message is being triggered too frequently. Check the [How to add Triggers](./iam-triggers) and [How often do you want to show this message?](./in-app-messages-setup) options.

If you are seeing this on Android only, then this can happen when clicking the back button or transitioning Activity's while the IAM is showing. Both will cause the IAM to appear again.

This is being caused by the IAM `View` being a child of the current `Activity`. Whenever intents between activities occur, the IAM will mimic the life-cycle of the current `Activity` and in some cases will cause flickering. The most common case is the IAM will hide itself and then reshow once in the new Activity.

Unfortunately this functionality is the closest available without needing any permissions to show the IAM on an `Application` level. More details in this open [GitHub issue](https://github.com/OneSignal/OneSignal-Android-SDK/issues/952). Feel free to respond to our Engineers directly on the Github issue. Also, our SDKs are Open Source, so if you had some ideas for a fix or other solution, we would gladly look into any PRs submitted!

If you are still having this issue and it is not one of the reasons above, please share the following details with our support team:

* Version of the OneSignal SDK(s) used
* Device OS version(s)
* Xcode log or Android Studio logcat from the app starting and the problem point
* Any other libraries or plugins in your app
* Details on reproducing your problem.

***

Built with [Mintlify](https://mintlify.com).
