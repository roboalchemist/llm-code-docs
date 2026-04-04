# Source: https://firebase.google.com/docs/functions/1st-gen/analytics-events.md.txt

Google Analytics provides event reports that help you understand
how users interact with your app. With Cloud Functions (1st gen), you
can access conversion events you have logged from Apple and Android devices
and trigger functions based on those events.

> [!CAUTION]
> Only Apple platform and Android events marked as conversion events are currently supported by Cloud Functions; Web conversion events are not currently available. You can specify which events are conversion events in the [Events](https://console.firebase.google.com/project/_/analytics/events) tab of the Firebase console **Analytics** pane.

> [!NOTE]
> **Note:** Cloud Functions for Firebase (2nd gen) does not provide support for the events and triggers described in this guide. Because 1st gen and 2nd gen functions can coexist side-by-side in the same source file, you can still develop and deploy this functionality together with 2nd gen functions.

## Trigger a Google Analytics function

Cloud Functions supports the Google Analytics
[`AnalyticsEvent`](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent).
This event is triggered whenever user activity generates a conversion event.
For example, you could write a function that
triggers when the `in_app_purchase` event is generated, indicating that an
in-app purchase has occurred.
You must specify the Analytics event that
you want to trigger your function using the
[`functions.analytics.event()`](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent)
method, and handle the event within the
[`onLog()`](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder#analyticsanalyticseventbuilderonlog)
event handler:

<br />

```
exports.sendCouponOnPurchase = functions.analytics.event('in_app_purchase').onLog((event) => {
  // ...
});
```

<br />

## Access event attributes

With each Analytics event, you have access to all relevant
parameters and user properties. These include information about the user, the
device, the app, and geographical information for the event.
For the complete list of parameters and user properties, see the
[`functions.analytics`](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics) reference.

For a purchase-triggered function as illustrated in
[this sample](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/coupon-on-purchase),
you might want to access user attributes such as the user's language and the
event's value ([`valueInUSD`](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent#analyticsanalyticseventvalueinusd)).
This second attribute allows the sample function to test whether this is a
high-value conversion event, in order to send a higher-value coupon to valuable customers.

<br />

```
/**
 * After a user has completed a purchase, send them a coupon via FCM valid on their next purchase.
 */
exports.sendCouponOnPurchase = functions.analytics.event('in_app_purchase').onLog((event) => {
  const user = event.user;
  const uid = user.userId; // The user ID set via the setUserId API.
  const purchaseValue = event.valueInUSD; // Amount of the purchase in USD.
  const userLanguage = user.deviceInfo.userDefaultLanguage; // The user language in language-country format.

  // For purchases above 500 USD, we send a coupon of higher value.
  if (purchaseValue > 500) {
    return sendHighValueCouponViaFCM(uid, userLanguage);
  }
  return sendCouponViaFCM(uid, userLanguage);
});
```

<br />

## Next steps

To learn more about handling Analytics events in Cloud Functions,
see the [Google Analytics documentation](https://firebase.google.com/docs/analytics) and the
[`functions.analytics`](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics) reference,
and try running the code sample
[coupon-on-purchase](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/coupon-on-purchase).