# Source: https://firebase.google.com/docs/ads.md.txt

# Google Ads

Reach potential customers with online ads.
Drive installs, gain deep insights into ad conversions, and run targeted ad campaigns usingGoogle Analyticsaudiences to engage your user base. When you link Firebase andGoogle Ads, you get access to powerful tools that help you see how yourAdsinvestment drives app installs and in-app actions. With Firebase andAds, you can export audience lists toAdsand import events fromAnalyticsintoAds.

<br />

## Key capabilities

|------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Analyticsaudience segmentation     | You can define custom audiences in theFirebaseconsole based on device data, custom events, or user properties.   |
| Export audience lists toAds        | A Firebase project can connect to multipleAdsaccounts, each with access to audiences created in Firebase.        |
| Import events fromAnalyticsintoAds | After you link Firebase andAds, you can choose whichGoogle Analyticsevents to track as conversion actions inAds. |

## How does it work?

When you link yourAdsaccount to a Firebase project, you can create mobile app marketing lists based onAnalyticsaudiences. By default, these audiences include the following:

- **Purchasers:**Users who have purchased an app or made an in-app purchase.
- **All users:**Users who have installed your app.

You can create audiences in Firebase using any combination of events and user properties, and then use those audiences to run targeted ad campaigns. For example, you can create an audience of "Android users who live in Canada", and then run ad campaigns directed at the users included in this audience.

Note that lists based onAnalyticsdata can only be used by Display Network campaigns.

## Implementation path

|---|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Create anAdsaccount.               | Create anAdsaccount, if you don't have one already.                                                                                                            |
|   | AddGoogle Analyticsto your app     | You can useAnalyticsby adding just a few lines of code to an app built using the Firebase SDK.                                                                 |
|   | Link yourAdsaccount with Firebase. | Use a Google Account that has administrator permissions in yourAdsaccount, and the Owner role in the Firebase project that you want to link to yourAdsaccount. |

## Next steps

- [Create aGoogle Adsaccount](https://ads.google.com).
- AddGoogle Analyticsto your[Apple platforms](https://firebase.google.com/docs/analytics/get-started?platform=ios)or[Android](https://firebase.google.com/docs/analytics/get-started?platform=android)app.
- [LinkAdswith Firebase](https://support.google.com/firebase/answer/6383833).
- [Track mobile app conversions with Firebase](https://support.google.com/google-ads/answer/6366292).