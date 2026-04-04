# Source: https://docs.buildnatively.com/guides/troubleshooting.md

# Troubleshooting

<details>

<summary>Push Notification doesn't work in the Android/iOS app</summary>

The first thing you must go through this checklist:&#x20;

* [ ] If you're using the **Natively Preview** app, you must [set the 'preview' tag in plugin](https://docs.buildnatively.com/natively-platform/preview) settings. **IF NOT,** you need to leave it blank.
* [ ] [After you've enabled and set up Push, you need to rebuild your app.](https://docs.buildnatively.com/natively-platform/app-info)
* [ ] [Make sure you've enabled](https://docs.buildnatively.com/natively-platform/features/notifications/onesignal-notifications#enable-push-notifications) & [set up Push for your app.](https://docs.buildnatively.com/setup-one-signal-app#video-guide)
* [ ] [Double-check your bubble app setup](https://docs.buildnatively.com/integration/push-notifications-onesignal#bubble-setup-push-example)
* [ ] [Network issue](https://documentation.onesignal.com/docs/notifications-show-successful-but-are-not-being-shown#network-issues)
* [ ] [Not targeted push (missing/wrong PlayerID)](https://documentation.onesignal.com/docs/notifications-show-successful-but-are-not-being-shown#not-targeted-in-the-push)
* [ ] [App Push Permission](https://documentation.onesignal.com/docs/notifications-show-successful-but-are-not-being-shown#app-push-permissions-disabled---device-not-subscribed)
* [ ] [Android Category](https://documentation.onesignal.com/docs/notifications-show-successful-but-are-not-being-shown#android-categories-disabled)
* [ ] [Low power mode](https://documentation.onesignal.com/docs/notifications-show-successful-but-are-not-being-shown#low-power-energy-saving)
* [ ] [Do not disturb mode](https://documentation.onesignal.com/docs/notifications-show-successful-but-are-not-being-shown#do-not-disturb-mode)
* [ ] (For iOS) [Sometimes you need to re-generate the PUSH certificate](https://docs.buildnatively.com/guides/generate-ios-push-key) and re-upload it to OneSignal
* [ ] (For Android) Sometimes, Android pushes are not coming. You need to delete the app and install it one more time. (This issue will not appear after release to Store)

</details>

<details>

<summary>Deeplinks doesn’t work in the Android/iOS app</summary>

The first thing you must go through this checklist:&#x20;

* [ ] Your custom links are **not supported** in the **Natively Preview** app, you need to build & setup your own app.
* [ ] [After you've enabled and set up Deeplinks, you need to rebuild your app.](https://docs.buildnatively.com/natively-platform/app-info)
* [ ] [Make sure you've enabled ](https://docs.buildnatively.com/natively-platform/features/deeplinks)& [set up Deeplinks for your app.](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks)
* [ ] [Double-check your bubble app setup](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks)
* [ ] (For iOS) Validate your website [here](https://branch.io/resources/aasa-validator/)
* [ ] [(For Android) Make sure you have added assetlinks.json](https://docs.buildnatively.com/setup-website-universal-links-deeplinks#setup-your-bubble.io-website)
* [ ] Make sure file is available by 'yourdomain.com / .well-known / yourfile' (it shouldn't be anywhere else)
* [ ] Make sure you're opening a link that is associated with your domain, sometimes services like [SendGrid have a redirect URL system](https://stackoverflow.com/a/40687167)
* [ ] Sometimes Apple/Google takes up to 48h to update the associated domain
* [ ] Sometimes reinstalling the app helps (Delete app → Reboot phone → Install app)

</details>

<details>

<summary>In-App Purchases doesn’t work in the Android/iOS app</summary>

The first thing you must go through this checklist:&#x20;

* [ ] In-App Purchases are **not supported** in the **Natively Preview** app, you need to build & set up your own app.
* [ ] [After you've enabled and set up In-App purchases, you need to rebuild your app.](https://docs.buildnatively.com/natively-platform/app-info)
* [ ] [Make sure you've enabled](https://docs.buildnatively.com/natively-platform/features/purchases#how-to-set-up-purchases) & [set up In-App for your app.](https://docs.buildnatively.com/setup-revenuecat-app#video-guides)
* [ ] [Double-check your bubble app setup](https://docs.buildnatively.com/integration/in-app-purchases#bubble-setup-example)
* [ ] [Check the **Latest Error** value from **Natively Purchases** element.](https://docs.buildnatively.com/guides/integration/in-app-purchases)
* [ ] [Make sure Google/Apple products are Active / Ready to submit test](https://community.revenuecat.com/sdks-51/why-are-offerings-or-products-empty-124)&#x20;
* [ ] Sometimes Apple/Google takes up to 24h to update the purchases setup
* [ ] Sometimes reinstalling the app helps (Delete app → Reboot phone → Install app)

</details>

<details>

<summary>I have a problem with a different Native feature</summary>

If you are faced with a problem related to a different native feature, go through this checklist:

* [ ] Almost all elements in the Natively bubble plugin have a **Latest Error** state, try to check its value. Usually, it helps to describe a problem.
* [ ] Join our [community in Discord](https://discord.gg/KwtHeTAsjN) and ask your question at the #general-questions channel.
* [ ] Check out our [editor test/example app](https://bubble.io/page?type=page\&name=purchases\&id=nativelyqa\&tab=tabs-1) on bubble. It has a separate page for each native feature.

</details>

## FAQ

### I'm seeing an error related to the Natively plugin when I try to use an action.

This usually happens when the plugin can't find the element it needs to trigger the action. Here are a few things to check:

* **Visibility:** Make sure the element associated with the action is placed on the page and is **visible**.
* **Element Location:** Don't place the element inside another element that might be hidden when you need to use the action (like a floating group, popup, focus group, or repeating group).
* **Required Fields:** Ensure all the required fields for the action are filled in. If you're using dynamic data, double-check that the values are not empty.

### My app was rejected by App Store / Google Play

Often some apps are got rejected by App Store or Google Play. It's normal.

First, you need to read the reason for the rejection message and apply the action steps.

Many rejections from Apple/Google teams are related to inaccurate descriptions. It might be related to unclear permission texts, In-App purchases product descriptions, or event application descriptions in a store. Here you can find a few useful links that can help you fix the problem:

1. [Release guide](https://docs.buildnatively.com/guides/testing-and-submitting-your-app)
2. [In-App purchases rejection](https://www.revenuecat.com/docs/app-store-rejections)
3. [Google Policy violation](http://www.androidb.com/2015/11/your-app-was-rejected-for-violating-googles-policy-now-what/)<br>

### After I close the app and then open it, data in RG are not updated (Chat case)

Unfortunately, we cannot handle this since it's a bubble socket issue. Check [this](https://forum.bubble.io/t/data-on-page-not-getting-updated/183223/29) thread on the bubble forum.

### I'm seeing an error when I try to rebuild my app - new agreement is missing

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F0YlTSyqOPYSPHl1c8pWx%2Ferror_agreement.png?alt=media&#x26;token=21f16d79-def4-446b-a5da-f1f2e22532d1" alt=""><figcaption></figcaption></figure>

Go to your [App Store Connect](https://appstoreconnect.apple.com) and follow the instructions provided in the yellow banner at the top of the page.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPp1MpXfji2BSQekSchom%2FScreenshot%20from%202025-01-08%2011-28-46.png?alt=media&#x26;token=31e82668-8163-4c3c-bdd5-1e32a107c864" alt=""><figcaption></figcaption></figure>

### I'm seeing an error when I try to rebuild my app - app version

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FgoWgu1tGUrdlYKXiIpvf%2Ferror_version.png?alt=media&#x26;token=3ffbe3b3-8b41-4a5b-b07f-833784695cf9" alt=""><figcaption></figcaption></figure>

This error appears when the app version in your Natively dashboard is lower then the app version in your App Store Connect > TestFlight. Or if the current version in your TestFlight is closed for new builds. \
If the app's version in TestFlight is 1.0.0, please provide version 1.0.1 (or higher) for a new build in your Natively dashboard. \
\
You can find more about app versioning in this article: <https://semver.org/>

### Why am I seeing an error when I try to add my iOS credentials?

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FNbCe5hVtN8illhLla7FN%2F403.png?alt=media&#x26;token=de24ff62-f4d8-4e57-b02e-dbd39c2cf6a8" alt=""><figcaption></figcaption></figure>

This error appears when some of the data you've provided is invalid or mismatched. The most common reasons for this are:

* The AuthKey either has an incorrect role (it must be App Manager), has been revoked, or is not associated with the provided Issuer ID.
* The Bundle ID you entered does not exist or is not associated with the Apple account the AuthKey is for.
* The Bundle ID is not correctly linked to the App Store App ID you provided.

Follow our guide on how to provide iOS credentials for a new app here: [ios-build](https://docs.buildnatively.com/natively-platform/app-info/ios-build "mention")

### My app opens a new tab of the internal browser on launch

This can occur when the website's actual domain doesn't match the App URL you provided in the Natively dashboard.

For example, if you set your App URL as `https://subdomain.domain.com`, but the website redirects to `https://example.com` upon opening, the app will recognize `https://example.com` as an external website. Since this domain isn't the one you initially specified as your App URL, it will open in a new tab within the app.

To resolve this, update the App URL in your Natively dashboard to reflect the actual domain your website uses. After saving this change, rebuild your app.

{% hint style="info" %}
If you still have any issues, contact us on support chat or by email at <help@buildnatively.com>
{% endhint %}

### Why is my app screen horizontally scrollable?

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FOTp2pzy8Ba2OeF2Ippte%2Fios_horizontal_scrolling.gif?alt=media&#x26;token=0e2b69b6-dd64-4693-b29b-530e067525b4" alt="" width="230"><figcaption></figcaption></figure>

This behavior occurs because there is an element on your webpage that is wider than the device's screen width.

For example, if the screen size is 390 pixels, but an element's minimum width is set to 391 pixels, the entire page will be forced to scroll horizontally.

Solution: You need to review the elements on your page to ensure they are fully responsive and correctly sized for smaller screens. This behavior originates within your website's design, not the app.

### Why are users being logged out over time, or why do they keep seeing the login screen?

Natively does not manage user sessions, cookies, or login persistence; it simply renders your website and respects your website's settings. These issues are tied directly to the session management logic within your website.

**1. Automatic Logout (Session Expiration)**

If users are being logged out after a period of time, the issue is typically caused by your website's default session expiration settings. This needs to be adjusted within your website's settings.

**2. Persistent Login Screen**

If logged-in users keep seeing the login page on app launch:

* This happens if your app's main URL points directly to the login page.
* Solution: You must verify the user's session status on the login page. If the user is authenticated, set up an automatic redirect in your workflow to immediately send them to the home page.

### The payment provider is not returning the user to the app via the Return URL

Please verify if your payment provider supports Universal Links for redirects. Some providers, such as Stripe, do not support this functionality (see [Stripe Docs](https://docs.stripe.com/payments/mobile/accept-payment?platform=ios\&type=payment\&locale=en-GB#set-up-return-url)).

The Solution: The "Landing Page" Pattern Since standard HTTP redirects often fail to trigger Universal Links on iOS/Android, you need to create a landing page:

1. Set the payment provider's return URL to a specific page on your website (e.g., `/success` or `/cancel`).
2. On this page, place a button/link (e.g., "Return to App") that points to your Universal Link.

Note: The user must manually click this link. Browsers usually block automatic scripts attempting to open Universal Links without a user gesture.
