# Source: https://firebase.google.com/docs/phone-number-verification/carrier_specs/privacy.md.txt

# Firebase PNV Privacy Considerations

<br />

*Last Modified Date: Feb 9, 2026*

This page describes the privacy considerations for Firebase Phone Number
Verification. The developer documentation will have the step-by-step
instructions, while this page summarizes the overall process. If you have any
questions, get in touch with your contact at Google.

## Developer onboarding

Firebase requires developers to go through brand verification and privacy policy
review before they can use the Firebase PNV API in production. Until they
complete this review, they are able to use the API only for local developer
testing, which does not result in any traffic sent to the carrier. Developer
onboarding is comprised of two phases:

### Initial onboarding

For initial onboarding, the developer must prove they are the owner of their
brand, and that their privacy policy describes how they will use phone
numbers. Developers will also be reminded of the [service specific terms](https://cloud.google.com/terms/service-terms)
(#41 under Service Terms) for Firebase PNV before using the service.

### Periodic auditing

Once a developer is onboarded, Firebase will periodically review the app's privacy
policy to ensure continued compliance. If an app's privacy policy is found to no
longer describe how they will use phone numbers, the developer's access to
Firebase PNV will be disabled until they rectify the issue.

## User Consent

Firebase PNV will present the following user consent on all Android devices in
the aggregator section (with Google Managed Services) every time an app requests
a phone number:

![Mockup of Firebase PNV consent screen on Android](https://firebase.google.com/static/docs/phone-number-verification/carrier_specs/consent-screen-android.png)

> [!NOTE]
> **Note:** Variables are in `<angled brackets>`. The app privacy policy link will map to the link provided during developer onboarding.