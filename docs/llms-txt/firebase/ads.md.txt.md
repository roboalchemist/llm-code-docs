# Source: https://firebase.google.com/docs/ads.md.txt

# Google Ads

Reach potential customers with online ads.
Drive installs, gain deep insights into ad conversions, and run targeted ad campaigns using Google Analytics audiences to engage your user base. When you link Firebase and Google Ads, you get access to powerful tools that help you see how your Ads investment drives app installs and in-app actions. With Firebase and Ads, you can export audience lists to Ads and import events from Analytics into Ads.

<br />

## Key capabilities

|---|---|
| Analytics audience segmentation | You can define custom audiences in the Firebase console based on device data, custom events, or user properties. |
| Export audience lists to Ads | A Firebase project can connect to multiple Ads accounts, each with access to audiences created in Firebase. |
| Import events from Analytics into Ads | After you link Firebase and Ads, you can choose which Google Analytics events to track as conversion actions in Ads. |

## How does it work?

When you link your Ads account to a Firebase project, you can create
mobile app marketing lists based on Analytics audiences. By
default, these audiences include the following:

- **Purchasers:** Users who have purchased an app or made an in-app purchase.
- **All users:** Users who have installed your app.

You can create audiences in Firebase using any combination of events and user
properties, and then use those audiences to run targeted ad campaigns. For
example, you can create an audience of "Android users who live in Canada", and
then run ad campaigns directed at the users included in this audience.

Note that lists based on Analytics data can only be used by Display Network
campaigns.

## Implementation path

|---|---|---|
|   | Create an Ads account. | Create an Ads account, if you don't have one already. |
|   | Add Google Analytics to your app | You can use Analytics by adding just a few lines of code to an app built using the Firebase SDK. |
|   | Link your Ads account with Firebase. | Use a Google Account that has administrator permissions in your Ads account, and the Owner role in the Firebase project that you want to link to your Ads account. |

## Next steps

- [Create a Google Ads account](https://ads.google.com).
- Add Google Analytics to your [Apple platforms](https://firebase.google.com/docs/analytics/get-started?platform=ios) or [Android](https://firebase.google.com/docs/analytics/get-started?platform=android) app.
- [Link Ads with Firebase](https://support.google.com/firebase/answer/6383833).
- [Track mobile app conversions with Firebase](https://support.google.com/google-ads/answer/6366292).