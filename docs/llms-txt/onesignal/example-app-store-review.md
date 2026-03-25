# Source: https://documentation.onesignal.com/docs/en/example-app-store-review.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get more app store reviews

> One powerful use of in-app messages is to increase App Store reviews from users who enjoy using your app, while simultaneously reducing friction.

This guide explains how to create a customized message encouraging users to review your app using the native AppStore review prompt.

<Frame caption="App Store Review Prompt Example">
    <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/8c81fd3f2381baae2ac9176c24fb1e5684df33e991e0726c64a459ed798c7148-Screenshot_2024-11-12_at_12.00.20_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=df73e58df4a1b6610f1cfffd84bd25d4" alt="" width="1016" height="617" data-path="images/docs/8c81fd3f2381baae2ac9176c24fb1e5684df33e991e0726c64a459ed798c7148-Screenshot_2024-11-12_at_12.00.20_PM.png" />
</Frame>

## Recommendations

* Android and iOS provide features to display an App Store review modal directly within the app. We will show you how to ask for reviews with or without this:
  * [Apple's Requesting App Store reviews docs](https://developer.apple.com/documentation/storekit/requesting_app_store_reviews)
  * [Google Play In-App Reviews API](https://developer.android.com/guide/playcore/in-app-review)
  * If running non-native apps, you may need to add a plugin or package to display the app store review directly in your app (example for [Flutter](https://pub.dev/packages/in_app_review) or [Expo](https://docs.expo.dev/versions/latest/sdk/storereview/)).
* You may want to use the OneSignal SDK `addTrigger` method to programmatically display the message, but we will also show a way to do this without code.

## Setup

### 1. Create the message

Navigate to **Messages > In-App > New In-App** or open the existing App Store Rating template.

Add an Action ID to your review button as shown below:

<Frame caption="Add Action ID for Review Button">
    <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/293839ca5534557c35929fdaa6eb5581c7218da770f2601bd3e7d819164430b8-Screenshot_2024-11-12_at_12.13.39_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=c88fe293c4f381dd0e44c686c54af348" alt="" width="1211" height="685" data-path="images/docs/293839ca5534557c35929fdaa6eb5581c7218da770f2601bd3e7d819164430b8-Screenshot_2024-11-12_at_12.13.39_PM.png" />
</Frame>

### 2. Add the trigger

The trigger is when the message should display. We provide no-code trigger options and code-required options.

If you go the no-code route, you can setup the Audience in step 1 to be a group of users you want reviews from, like users that have a lot of sessions and have used the app for a long time.

If you go the code route, you can programmatically decide when to ask for the review based on user actions. This should happen when the user is not doing something important or interrupt them using your app.

In this example, we set the **In-App Trigger** key to be `ask_for_review` with a value of `show`. The actual key and value doesn't need to be these exact things, but needs to match what you set in the `addTrigger` method.

For Example: `OneSignal.InAppMessages.addTrigger("ask_for_review", "show");`

<Frame caption="Example shows the same key-value used in the addTrigger method.">
    <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/459e14e99af52793454464b3e52ddc518f7a8c73021c16aae24b3389532c012a-Screenshot_2024-11-12_at_12.24.08_PM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=0a50f0c58f47de1b1ad7d478fea5ea77" alt="" width="825" height="236" data-path="images/docs/459e14e99af52793454464b3e52ddc518f7a8c73021c16aae24b3389532c012a-Screenshot_2024-11-12_at_12.24.08_PM.png" />
</Frame>

### 3. Handle the app store rating prompt

Similar to the trigger options above, you can direct users to write the review with a no-code and code-required options.

<Accordion title="No-code option">
  If you go the no-code route, there are a couple steps to follow:

  1. Update the segment to use "Device Type is Android" filter.
  2. Duplicate the in-app message and in the duplicated message, update the segment to use "Device Type is iOS" filter. - You should have 2 different in-app messages and 2 different segments (one for iOS and another for Android).
  3. Add the [URL Click Action](./iam-click-actions) within the "Review Now" button to be the link to your app store listing based on the iOS and Android listing.

* [Android's documentation](https://developer.android.com/distribute/marketing-tools/linking-to-google-play.html) shows how to link to the app store. Here is an example URL: `https://play.google.com/store/apps/details?id=<package_name>`
* [Apple's documentation](https://developer.apple.com/documentation/storekit/requesting_app_store_reviews) shows the following URL scheme: `https://apps.apple.com/app/id<#Your App Store ID#>?action=write-review`
</Accordion>

<Accordion title="Code-required option">
  Within our SDK's `InAppMessages.addClickListener` method, you can listen for when the message is clicked and handle it differently based on the `action ID` set above.

  Within this listener method, you can then programmatically call the iOS or Android options to present the app store review modal.
</Accordion>

<CodeGroup>
  ```javascript Example theme={null}
  OneSignal.InAppMessages.addClickListener((event) async {

    if (actionId == 'review') {
       (await inAppReview.isAvailable()) {
        inAppReview.requestReview();
      }
    }
  });

  ```
</CodeGroup>

### 4. Schedule and enable

Apple restricts review prompts to three times per year per user and Google recommends less than once per month but doesn't say an exact quota.

To make sure that you don’t over-show the in-app, you can set your in-app schedule to display once every 17 weeks as shown below:

<Frame caption="These settings will show the in-app up to 40 times total spaced out 17 weeks apart. Increase the amount of times if you want to ask more than 40 times total.">
    <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5c63bb89120c9fcffa5c3836f3f13de2db38952bc61c56d2f8d18c0bf450986f-Screenshot_2024-11-19_at_11.49.26_AM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=690b7ecb27ab452252390d5511f6f821" alt="" width="898" height="187" data-path="images/docs/5c63bb89120c9fcffa5c3836f3f13de2db38952bc61c56d2f8d18c0bf450986f-Screenshot_2024-11-19_at_11.49.26_AM.png" />
</Frame>

**Increasing positive reviews on Apple AppsStore.**

1. Set tags on users who had a great experience with your app. This can be monitored using number of sessions, adding tags to indicate their experience with your app, or collecting feedback with IAM and assigning a data tag to those who left a great review.
2. Create a Segment, then use this segment as the Audience for the Native Review Prompt IAM.

<Check>
  You are now done. Your users will get asked for a review without the need to leave your app. Drastically removing friction points.
</Check>

***


Built with [Mintlify](https://mintlify.com).
