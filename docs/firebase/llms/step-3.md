# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-3.md.txt

## Step 3: Troubleshoot and handle common issues

<br />

|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Introduction:[Measure iOS Ads conversions](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/index-event-driven) |
| Step 1:[Link Your Ads Account withGoogle Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-1)    |
| Step 2:[IntegrateGoogle Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-2)                     |
| **Step 3: Troubleshoot and handle common issues**                                                                                                  |

<br />

Support is available if you have any problems with on-device conversion measurement with event data.

### Troubleshoot iOS on-device measurement with event data

#### Google Analytics

Are you having trouble implementingGoogle Analytics? Use the help resources and contact information provided by the[Google Analyticsteam](https://support.google.com/analytics).

There are a few troubleshooting cases you can investigate before you consult help resources.
| **Note:** Since v11.14.0, TheGoogle Analyticsfor Firebase SDK was restructured and as a result some modules were deprecated. See the newest modules in`FirebaseAnalytics`[in the Firebase FAQ](https://firebase.google.com/support/faq#analytics-odm2-sdk-refactor-ios).

##### Deprecated frameworks linked

If you link both the`GoogleAppMeasurementOnDeviceConversion`(deprecated) framework as well as the`GoogleAdsOnDeviceConversion`frameworks into your app, an exception will be raised with the following message. To avoid the exception, remove the`GoogleAppMeasurementOnDeviceConversion`(deprecated) framework.  

    GoogleAppMeasurementOnDeviceConversion (deprecated) framework and
    GoogleAdsOnDeviceConversion framework are both linked into the app. Remove the
    GoogleAppMeasurementOnDeviceConversion (deprecated) framework, which is no
    longer recommended for new development.

| **Note:** `GoogleAppMeasurementOnDeviceConversion`printed in the logs is a dependency of`FirebaseAnalyticsOnDeviceConversion`.

##### `GoogleAdsOnDeviceConversion`framework not linked

If the`_psmvalue_gads`message doesn't appear in the Xcode debug console:

1. Verify this message appears that shows debug mode is enabled:

       [FirebaseAnalytics][I-ACS023009] Debug logging enabled

   This message means`GoogleAdsOnDeviceConversion.xcframework`is not linked:  

       [FirebaseAnalytics][I-ACS023279] Conversion service disabled. GoogleAdsOnDeviceConversion framework is not linked.

2. Verify this message appears that shows`GoogleAdsOnDeviceConversion.xcframework`is linked:

       [FirebaseAnalytics][I-ACS023278] Conversion service GoogleAdsOnDeviceConversion framework is linked

#### Firebase SDKs

Are you having trouble implementing Firebase SDKs? If you are a Google Cloud customer, reach out to your paid support through Google Cloud. If you are not a paid Google Cloud customer, reach out to no-cost[Firebase Support](https://firebase.google.com/support).

#### Google Ads

Are you having trouble measuring your ad campaign with this feature? Use the help resources and contact information provided by the Google Ads team.

#### Google Analytics

Are you having trouble implementing Google Analytics? Use the help resources and contact information provided by the[Google Analytics team](https://support.google.com/analytics).

<br />

*** ** * ** ***

<br />

[arrow_back_ios**Step 2** IntegrateGoogle Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-2)

<br />

*** ** * ** ***