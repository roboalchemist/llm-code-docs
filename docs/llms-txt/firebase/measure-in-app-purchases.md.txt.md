# Source: https://firebase.google.com/docs/analytics/android/measure-in-app-purchases.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/measure-in-app-purchases) [Android](https://firebase.google.com/docs/analytics/android/measure-in-app-purchases) |

In-app purchases (IAP) are digital content or features that you can sell in a
mobile app through Google Play so your app doesn't
have to process financial transactions. Examples of in-app purchases include
subscription-based content or special game pieces.

Analytics shows IAP events in the
[In-app purchases report](https://support.google.com/analytics/answer/12923440).

For Android apps, the Analytics SDK integrates with Google Play.

In most cases, the Analytics SDK automatically collects IAP events without
requiring API calls in your app.

## Before you begin

- Set up your Firebase project and your app's codebase as described in
  [Get Started with Google Analytics](https://firebase.google.com/docs/analytics/android/get-started).

- [Link your Firebase project to a Google Analytics 4 property.](https://support.google.com/firebase/answer/9289399)

- Make sure that your app is using the Analytics SDK v17.3.0+
  (or Firebase Android BoM v25.2.0+).

- [Link your Firebase apps to Google Play](https://support.google.com/firebase/answer/6392038).

  > [!NOTE]
  > **Note:** For Android apps, you can measure IAP events as soon as you link to Google Play. The remainder of this guide is focused on Apple platform apps.

## Implementation

In most cases, the Analytics SDK automatically logs IAP events without requiring
additional code.

For Android apps, you can measure IAP events as soon as you
[link to Google Play](https://support.google.com/analytics/answer/11548051).