# Source: https://firebase.google.com/docs/analytics/ios/configure-data-collection.md.txt

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

### Temporarily disable collection

If you wish to temporarily disable Analytics collection, such as to get
end-user consent before collecting data, you can set the value of
`FIREBASE_ANALYTICS_COLLECTION_ENABLED` to `NO` (Boolean) in your app's
`Info.plist` file. For example, viewed in the source XML:

    <key>FIREBASE_ANALYTICS_COLLECTION_ENABLED</key><false/>

To re-enable collection, such as after an end-user provides consent, call the
[`setAnalyticsCollectionEnabled`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#setanalyticscollectionenabled_:)
instance method of `Analytics`. For example:

### Swift


**Note:** This Firebase product is not available on the macOS target.

    Analytics.setAnalyticsCollectionEnabled(true)

### Objective-C


**Note:** This Firebase product is not available on the macOS target.

    [FIRAnalytics setAnalyticsCollectionEnabled:YES];

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetAnalyticsCollectionEnabled(true);

If you need to suspend collection again for any reason, you can call the
following and collection is suspended until you re-enable it.

### Swift


**Note:** This Firebase product is not available on the macOS target.

    Analytics.setAnalyticsCollectionEnabled(false)

### Objective-C

    [FIRAnalytics setAnalyticsCollectionEnabled:NO];

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetAnalyticsCollectionEnabled(false);

The value set by the `setAnalyticsCollectionEnabled` method persists across app
executions and overrides the value for `FIREBASE_ANALYTICS_COLLECTION_ENABLED`
in your app's `Info.plist` file. Once you set a value for
`setAnalyticsCollectionEnabled`, Analytics collection remains in that state
until `setAnalyticsCollectionEnabled` is called again, even if a user closes
and re-opens your app.

### Permanently deactivate collection

If you need to deactivate Analytics collection permanently in a version of your
app, set `FIREBASE_ANALYTICS_COLLECTION_DEACTIVATED` to `YES` (Boolean) in your
app's `Info.plist` file. Setting `FIREBASE_ANALYTICS_COLLECTION_DEACTIVATED` to
`YES` (Boolean) takes priority over any values for
`FIREBASE_ANALYTICS_COLLECTION_ENABLED` in your app's `Info.plist` as well as any
values set with `setAnalyticsCollectionEnabled`.

To re-enable collection, remove `FIREBASE_ANALYTICS_COLLECTION_DEACTIVATED` from
your `Info.plist`. Setting `FIREBASE_ANALYTICS_COLLECTION_DEACTIVATED` to `NO`
(Boolean) has no effect and results in the same behavior as not having
`FIREBASE_ANALYTICS_COLLECTION_DEACTIVATED` set in your `Info.plist` file.

### Disable IDFA collection

If you installed the `FirebaseAnalytics` module to your app through SPM or
CocoaPods and want to disable collection of the IDFA (a device's advertising
identifier) in your Apple app, ensure that the AdSupport framework is not
included in your app.

To install Firebase without any IDFA collection capability, use the following
instead of the `FirebaseAnalytics` dependency:

### Swift Package Manager

      .target(
        name: "MyTargetName",
        dependencies: [
          .product(name: "FirebaseAnalyticsCore", package: "Firebase"),
          // ...
        ]
      ),

### CocoaPods

    pod 'FirebaseAnalytics/Core'

Learn more about IDFA in Apple's documentation:

- [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
- [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)

### Disable IDFV collection

If you wish to disable collection of the IDFV (Identifier for Vendor) in your
Apple app, set the value of `GOOGLE_ANALYTICS_IDFV_COLLECTION_ENABLED` to `NO`
(Boolean) in your app's `Info.plist` file.

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
  [Control ad personalization as a user property](https://firebase.google.com/docs/analytics/ios/configure-data-collection#disable-personalization-as-user-property).

- Enable or disable ad personalization at the Analytics property level:
  [Disable ads personalization per geographical region in your Analytics property](https://support.google.com/analytics/answer/9626162).

### Disable personalized advertising features via a user property

[Google's consent mode API](https://developers.google.com/tag-platform/security/guides/app-consent?platform=ios)
is the recommended way to enable and disable personalized advertising.

However, if your app doesn't use consent mode yet, you can control
personalization with the following option.

To disable personalized advertising behavior by default, set the value of
`GOOGLE_ANALYTICS_DEFAULT_ALLOW_AD_PERSONALIZATION_SIGNALS` to `NO` (Boolean)
in your app's `Info.plist` file.

> [!NOTE]
> **Note:** In certain circumstances, Google may disable personalized advertising for Analytics data collected from an end user, even when you have not done so, where Google has information that the respective end user is not eligible for personalized advertising (for example, [the end user on an Android device is under the applicable age per our advertising policies](https://support.google.com/adspolicy/answer/143465)).

### Re-enable personalized advertising features via a user property

If you use the `AnalyticsUserPropertyAllowAdPersonalizationSignals` parameter
to control ad personalization, you can re-enable ad personalization with the
[`setUserProperty`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#setuserproperty_:forname:)
method as shown below:

### Swift


**Note:** This Firebase product is not available on the macOS target.

    Analytics.setUserProperty("true", forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)

### Objective-C


**Note:** This Firebase product is not available on the macOS target.

    [FIRAnalytics setUserPropertyString:@"YES" forName:kFIRUserPropertyAllowAdPersonalizationSignals];

### Unity

    Firebase.Analytics.FirebaseAnalytics.SetUserProperty(FirebaseAnalytics.UserPropertyAllowAdPersonalizationSignals, true);

If you have chosen to temporarily disable analytics collection (for example,
until an end-user provides consent), and you want to control personalized
advertising features upon re-enabling analytics collection for a user, ensure
that your call to specify this setting precedes your call to re-enable analytics
collection. For example:

### Swift


**Note:** This Firebase product is not available on the macOS target.

    Analytics.setUserProperty(..., forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)
    Analytics.setAnalyticsCollectionEnabled(true)

### Objective-C


**Note:** This Firebase product is not available on the macOS target.

    [FIRAnalytics setUserPropertyString:... forName:kFIRUserPropertyAllowAdPersonalizationSignals];
    [FIRAnalytics setAnalyticsCollectionEnabled:YES];

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
> **Note:** If a user withdraws their previously given consent for Analytics or Ad storage, Google Analytics deletes all user properties, including consent for [`ad personalization`](https://developers.google.com/tag-platform/security/concepts/consent-mode#consent-type). To preserve the user's consent choice for ad personalization, restore the previous value for ad personalization using `setConsent` ([Swift](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Categories/FIRAnalytics(Consent)#setconsent_:) \| [Obj-C](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#+setconsent:)).

## See your configuration changes

Once you've made changes to your Google Analytics settings, the SDK
downloads the changes. The process is fast and seamless, so you can quickly test
your changes. When you make changes in Analytics, it may take a few minutes
to deploy in your app. If your app is live, the full deployment process may take
up to one hour to complete.