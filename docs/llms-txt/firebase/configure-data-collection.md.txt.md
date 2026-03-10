# Source: https://firebase.google.com/docs/analytics/android/configure-data-collection.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/configure-data-collection) [Android](https://firebase.google.com/docs/analytics/android/configure-data-collection) |

This page describes the features that Google Analytics offers which allow
you to control the collection and use of Analytics data.

## Disable Analytics data collection

In some cases, you may want to temporarily or permanently disable collection of
Analytics data, such as to collect end-user consent or to fulfill legal
obligations. Google Analytics offers multiple options for disabling
and deactivating Analytics collection. Used together, they support many
typical use cases.

> [!NOTE]
> **Note:** If you're using Unity to build an Android app, either [Override the Android App Manifest](https://docs.unity3d.com/Manual/overriding-android-manifest.html) or [Export an Android project](https://docs.unity3d.com/Manual/android-export-process.html) and then build it from there.

### Temporarily disable collection

If you want to temporarily disable Analytics collection, such as to get
end-user consent before collecting data, you can set the value of
`firebase_analytics_collection_enabled` to `false` in your app's
`AndroidManifest.xml` in the `application` tag. For example:

    <meta-data android:name="firebase_analytics_collection_enabled" android:value="false" />

To re-enable collection, such as after an end-user provides consent, call the
[`setAnalyticsCollectionEnabled()`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean))
method of the `FirebaseAnalytics` class. For example:

### Kotlin

    setAnalyticsCollectionEnabled(true);

### Java

    setAnalyticsCollectionEnabled(true);

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetAnalyticsCollectionEnabled(true);

If you need to suspend collection again for any reason, you can call the
following and collection is suspended until you re-enable it.

### Kotlin

    setAnalyticsCollectionEnabled(false);

### Java

    setAnalyticsCollectionEnabled(false);

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetAnalyticsCollectionEnabled(false);

### Permanently deactivate collection

If you need to deactivate Analytics collection permanently in a version of
your app, set `firebase_analytics_collection_deactivated` to true in your app's
AndroidManifest.xml in the `application` tag. For example:

    <meta-data android:name="firebase_analytics_collection_deactivated" android:value="true" />

### Disable Advertising ID collection

If you wish to disable collection of the
[Advertising ID](https://support.google.com/googleplay/android-developer/answer/6048248)
in your Android app, you can set the value of
`google_analytics_adid_collection_enabled` to `false` in your app's
`AndroidManifest.xml` in the `application` tag. For example:

    <meta-data android:name="google_analytics_adid_collection_enabled" android:value="false" />

## Control data collection for personalized advertising

If you have linked your Google Analytics project to an ads account or
otherwise enabled an ads integration, or opted into
[data sharing](https://support.google.com/firebase/answer/6383877),
your Analytics data may be eligible for use in personalized advertising.
This means for instance, that you may use collected events such as `first_open`
to create and deploy audience lists for remarketing unless you indicate that
such data is not available for personalized advertising.

You can programmatically control whether a user's Analytics data should be used
for personalized advertising using any of the following options:

- **Recommended** : Dynamically enable or disable ad personalization by
  honoring the user's consent choice.
  [Implement Google's consent mode API](https://developers.google.com/tag-platform/security/guides/app-consent).

- Enable or disable ad personalization at the user level:
  [Control ad personalization as a user property](https://firebase.google.com/docs/analytics/android/configure-data-collection#disable-personalization-as-user-property).

- Enable or disable ad personalization at the Analytics property level:
  [Disable ads personalization per geographical region in your Analytics property](https://support.google.com/analytics/answer/9626162).

### Disable personalized advertising features using a user property

[Google's consent mode API](https://developers.google.com/tag-platform/security/guides/app-consent?platform=android)
is the recommended way to enable and disable personalized advertising.

However, if your app doesn't use consent mode yet, you can control
personalization with the following option.

To disable personalized advertising behavior by default, specify the following
field in your app's `AndroidManifest.xml` in the `application` tag:

    <meta-data android:name="google_analytics_default_allow_ad_personalization_signals" android:value="false" />

> [!NOTE]
> **Note:** In certain circumstances, Google may disable personalized advertising for Analytics data collected from an end user, even when you have not done so, where Google has information that the respective end user is not eligible for personalized advertising (for example, [the end user on an Android device is under the applicable age per our advertising policies](https://support.google.com/adspolicy/answer/143465)).

### Re-enable personalized advertising features via a user property

If you use the `google_analytics_default_allow_ad_personalization_signals`
parameter to control ad personalization, you can re-enable ad personalization
with the [`setUserProperty`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserProperty(java.lang.String,%20java.lang.String))
method as shown below:

### Kotlin

    setUserProperty( ALLOW_AD_PERSONALIZATION_SIGNALS, "true" );

### Java

    setUserProperty( ALLOW_AD_PERSONALIZATION_SIGNALS, "true" );

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetUserProperty(FirebaseAnalytics.UserPropertyAllowAdPersonalizationSignals, true);

If you have chosen to temporarily disable analytics collection (for example,
until an end-user provides consent), and you want to control personalized
advertising features upon re-enabling analytics collection for a user, ensure
that your call to specify this setting precedes your call to re-enable analytics
collection. For example:

### Kotlin

    setUserProperty( ALLOW_AD_PERSONALIZATION_SIGNALS, ... );
    setAnalyticsCollectionEnabled(true);

### Java

    setUserProperty( ALLOW_AD_PERSONALIZATION_SIGNALS, ... );
    setAnalyticsCollectionEnabled(true);

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetUserProperty(FirebaseAnalytics.UserPropertyAllowAdPersonalizationSignals, ...);
    Firebase.Analytics.FirebaseAnalytics.SetAnalyticsCollectionEnabled(true);

### Confirm your settings

When ad personalization signals have been disabled for a user via one of the
mechanisms defined above, subsequent event bundles logged from that user's
device will contain a user property named `non_personalized_ads` with a value of
1 to indicate that events in that bundle are not available for personalized
advertising. Disabling personalized advertising does not affect the use of the
data for measurement purposes, including reporting and attribution.

> [!NOTE]
> **Note:** If a user withdraws their previously given consent for Analytics or Ad storage, Google Analytics deletes all user properties, including consent for [`ad personalization`](https://developers.google.com/tag-platform/security/concepts/consent-mode#consent-type). To preserve the user's consent choice for ad personalization, restore the previous value for ad personalization using `setConsent` ([Kotlin](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)) \| [Java](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map%3Ccom.google.firebase.analytics.FirebaseAnalytics.ConsentType,%20com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus%3E))).

## See your configuration changes

Once you've made changes to your Google Analytics settings, the SDK
downloads the changes. The process is fast and seamless, so you can quickly test
your changes. When you make changes in Analytics, it may take a few minutes
to deploy in your app. If your app is live, the full deployment process may take
up to one hour to complete.