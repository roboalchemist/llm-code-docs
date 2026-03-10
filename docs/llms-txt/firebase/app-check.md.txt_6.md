# Source: https://firebase.google.com/docs/app-check.md.txt

# Firebase App Check

[Video](https://www.youtube.com/watch?v=LFz8qdF7xg4)

App Check helps protect your app backends from abuse by preventing
unauthorized clients from accessing your backend resources. It works with
both Google services (including Firebase and Google Cloud services) and your
own custom backends to keep your resources safe.

With App Check, devices running your app will use an app or device
attestation provider that attests to one or both of the following:

- Requests originate from your authentic app
- Requests originate from an authentic, untampered device

This attestation is attached to every request your app makes to the APIs you
specify. When you enable App Check enforcement, requests from
clients without a valid attestation will be rejected, as will any request
originating from an app or platform you haven't authorized.

App Check has built-in support for using the following services as
attestation providers:

- [DeviceCheck](https://developer.apple.com/documentation/devicecheck) or [App Attest](https://developer.apple.com/documentation/devicecheck/establishing_your_app_s_integrity) on Apple platforms
- [Play Integrity](https://developer.android.com/google/play/integrity) on Android
- [reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise) on web apps.

If these are insufficient for your needs, you can also implement your own
service that uses either a third-party attestation provider or your own
attestation techniques.

App Check works with the following Google services:

| Supported Firebase and Google Cloud services |
|---|
| Firebase Authentication (Preview) |
| Firebase Data Connect |
| Cloud Firestore |
| Firebase Realtime Database |
| Cloud Storage for Firebase |
| Cloud Functions for Firebase (callable functions only) |
| Firebase AI Logic |
| [Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview) (Preview) |
| [Places API (New)](https://developers.google.com/maps/documentation/places/web-service/overview) (Preview) |
| [Google Identity for iOS](https://developers.google.com/identity/sign-in/ios/appcheck) |

You can also use App Check to protect your non-Google custom backend
resources, like your own self-hosted backend.

[Learn how to get started](https://firebase.google.com/docs/app-check#get_started)

## How does it work?

When you enable App Check for a service and include the client SDK
in your app, the following happens periodically:

1. Your app interacts with the provider of your choice to obtain an attestation of the app or device's authenticity (or both, depending on the provider).
2. The attestation is sent to the App Check server, which verifies the validity of the attestation using parameters registered with the app, and returns to your app an App Check token with an expiration time. This token might retain some information about the attestation material it verified.
3. The App Check client SDK caches the token in your app, ready to be sent along with any requests your app makes to protected services.

A service protected by App Check only accepts requests accompanied
by a current, valid App Check token.

## How strong is the security provided by App Check?

App Check relies on the strength of its attestation providers to determine
app or device authenticity. It prevents some, but not all, abuse vectors
directed towards your backends. Using App Check does not guarantee
the elimination of all abuse, but by integrating with App Check, you are
taking an important step towards abuse protection for your backend resources.

## How is App Check related to Firebase Authentication?

App Check and Firebase Authentication are complementary parts of your app security
story. Firebase Authentication provides user authentication, which protects your
users, whereas App Check provides attestation of app or device authenticity,
which protects you, the developer. App Check guards access to your Google
backend resources and custom backends by requiring API calls to contain a valid
App Check token. These two concepts work together to help secure your app.

## Quotas \& limits

Your use of App Check is subject to the quotas and limits of the attestation
providers you use.

- DeviceCheck and App Attest access is subject to any quotas or limitations set
  by Apple.

- Play Integrity has a daily quota of 10,000 calls for its Standard API usage
  tier. For information on raising your usage tier, see the
  [Play Integrity documentation](https://developer.android.com/google/play/integrity/overview#usage-tiers).

- reCAPTCHA Enterprise is no-cost for 10,000 assessments each month, and has a
  cost beyond that. See [reCAPTCHA pricing](https://cloud.google.com/security/products/recaptcha#pricing).

In addition, the App Check service has
[quotas](http://console.cloud.google.com/apis/api/firebaseappcheck.googleapis.com/quotas)
on the volume of requests it will handle from a single project; however, these
quotas are not typically depleted through normal usage. If your traffic volume
is anticipated to exceed these quotas, [contact Firebase support](https://firebase.google.com/support/troubleshooter/contact)
to request an increase.

## Get started

Ready to get started?

#### Apple platforms

[DeviceCheck](https://firebase.google.com/docs/app-check/ios/devicecheck-provider)
[App Attest](https://firebase.google.com/docs/app-check/ios/app-attest-provider)

#### Android

[Play Integrity](https://firebase.google.com/docs/app-check/android/play-integrity-provider)

#### Web

[reCAPTCHA Enterprise](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider)

#### Flutter

[Default providers](https://firebase.google.com/docs/app-check/flutter/default-providers)

#### Unity

[Default providers](https://firebase.google.com/docs/app-check/unity/default-providers)

#### C++

[Default providers](https://firebase.google.com/docs/app-check/cpp/default-providers)

#### Learn how to implement a custom App Check provider

[Custom providers](https://firebase.google.com/docs/app-check/custom-provider)

#### Learn how to use App Check to protect your custom backend resources

Select your platform:

[iOS+](https://firebase.google.com/docs/app-check/ios/custom-resource)
[Android](https://firebase.google.com/docs/app-check/android/custom-resource)
[Web](https://firebase.google.com/docs/app-check/web/custom-resource)
[Flutter](https://firebase.google.com/docs/app-check/flutter/custom-resource)
[Unity](https://firebase.google.com/docs/app-check/unity/custom-resource)
[C++](https://firebase.google.com/docs/app-check/cpp/custom-resource)