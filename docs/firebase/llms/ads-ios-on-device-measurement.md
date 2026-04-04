# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement.md.txt

Implementing durable measurement strategies is crucial for understanding the impact of your marketing efforts and optimizing your investments. Google's on-device conversion measurement improves the amount of observable conversions to enhance campaign optimization and reporting for your iOS App campaigns in a privacy-preserving manner.

In these tutorials, you'll learn how these solutions work and follow along with the steps needed to implement them.

## How does this work?

On-device conversion measurement helps measure app installs and in-app actions from your iOS App campaigns while keeping user data private. There are two variants of this solution: using first-party data and using de-identified, temporary app event data.

To learn more about the privacy-preserving benefits of on-device conversion measurement, view the[Google Ads Help Center article](https://support.google.com/google-ads/answer/12119136).

## How will my team implement it?

On-device measurement works on devices running iOS 12+. Each variant of this solution has specific implementation requirements. In order to activate each, you will need to verify your app's build includes the`GoogleAdsOnDeviceConversion`library:

- For**first-party data**, you need a consented, user-provided email address or phone number. Through the API, the email address or phone number is used by the Google Analytics for Firebase SDK for attribution such that this personal data is never sent off the device in a way that can identify the user or device.

  You can use Firebase Authentication to allow users to sign in to your app using one or more sign-in methods. Once integrated with Firebase Authentication, you can get the signed-in user's email or phone number to initiate on-device conversion measurement.
- For**event data** , verify that the latest version of theGoogle Analyticsfor Firebase SDK is configured in your app, and if applicable, that any selected custom events are logged. These[key events](https://support.google.com/analytics/answer/9267568)should align with the most important actions or conversions you want to measure for your iOS campaigns.

## Can I use both techniques?

Absolutely! These approaches are not mutually exclusive. For advertisers running iOS app campaigns, we recommend implementing both variants of this solution to maximize performance and reporting benefits.

Combining both methods provides a more comprehensive approach to measurement while respecting user privacy.

## What's next?

Follow along in the step-by-step tutorials:

- On-device conversion measurement[using first-party data](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/index-first-party)
- On-device conversion measurement[using event data](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/index-event-driven)