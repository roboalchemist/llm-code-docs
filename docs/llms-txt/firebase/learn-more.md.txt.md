# Source: https://firebase.google.com/docs/ios/learn-more.md.txt

As you're developing your Apple app using Firebase, you might discover concepts
that are unfamiliar or specific to Firebase. This page aims to answer those
questions or point you to resources to learn more.

If you have questions about a topic not covered on this page, feel free to visit
one of our online communities. We'll also update this page with new topics
periodically, so check back to see if we've added the topic you want to learn
about!

## Firebase library support by platform

The following table describes which Firebase libraries are compatible with which
Apple platforms. For the time being, visionOS and watchOS are
community-supported only. See the
[Firebase Apple platforms SDK GitHub repository](https://github.com/firebase/firebase-ios-sdk)
for installation instructions and known issues.

| Library | iOS | macOS | Mac Catalyst | tvOS | visionOS | watchOS |
|---|---|---|---|---|---|---|
| A/B Testing | Yes | Yes | Yes | Yes | Yes | Yes |
| Firebase AI Logic ^1^ | iOS 15+ | macOS 12+ | Catalyst 15+ | tvOS 15+ (Community support only) | Yes | watchOS 8+ |
| Analytics | Yes | v8.9.0+ | v8.9.0+ | v8.9.0+ |   |   |
| Analytics without Ad ID | Yes | v8.9.0+ | v8.9.0+ | v8.9.0+ |   |   |
| Analytics on-device conversion | Yes |   |   |   |   |   |
| App Check DeviceCheck provider | Yes | Yes | Yes | Yes | Yes | watchOS 9+ |
| App Check App Attest provider | iOS 14+ | macOS 11+ | Catalyst 14+ | tvOS 15+ | Yes | watchOS 9+ |
| App Check custom and debug providers | Yes | Yes | Yes | Yes | Yes | Yes |
| App Distribution | Yes |   |   |   |   |   |
| Authentication | Yes | partial | partial | partial | partial | partial |
| Cloud Firestore | Yes | Yes | Yes | Yes | Source distros only |   |
| Cloud Functions | Yes | Yes | Yes | Yes | Yes | Yes |
| Cloud Messaging | Yes | Yes | Yes | Yes | Yes | Yes |
| Cloud Storage | Yes | Yes | Yes | Yes | Yes | Yes |
| Crashlytics | Yes | Yes | Yes | Yes | Yes | Yes |
| Data Connect | Yes | Yes | Yes | Yes |   | Yes |
| Dynamic Links | Yes |   |   |   |   |   |
| Firebase installations | Yes | Yes | Yes | Yes | Yes | Yes |
| Firebase ML Model Downloader | Yes | Yes | Yes | Yes | Yes | Yes |
| In-App Messaging | Yes |   |   | Yes |   |   |
| Performance Monitoring | Yes |   |   | Yes |   |   |
| Realtime Database | Yes | Yes | Yes | Yes | Yes |   |
| Remote Config | Yes | Yes | Yes | Yes | Yes | Yes |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase".*^

> [!NOTE]
> **Note:** Though [Test Lab](https://firebase.google.com/docs/test-lab/ios/get-started) has no client SDK, it does support iOS. Test Lab does not support other non-iOS Apple platforms.

### App Clips

Most Firebase libraries will build and run in an App Clip target, however, many
are restricted as a result of underlying OS restrictions. Known issues include:

- Dynamic Links cannot send users to an App Clip if they tap a link without the app installed.
- Firestore and Realtime Database cannot load data in App Clips due to an underlying CFStream dependency.

See the
[Firebase GitHub repository](https://github.com/firebase/firebase-ios-sdk/labels/app-clips)
for a full list of known App Clip issues.

## GoogleService-Info.plist

As part of adding Firebase to your Apple project, you need to add the
`GoogleService-Info.plist` configuration file to your project. If you want to
use multiple Firebase projects in a single app, visit the documentation for
[configuring multiple projects](https://firebase.google.com/docs/projects/multiprojects).

> [!NOTE]
> **Note:** The `GoogleService-Info.plist` config file contains unique but non-secret identifiers for your project. To learn more about this config file, visit [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects).

See the
[Swift reference documentation](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)configure)
to learn about the Firebase app initialization process in more detail.

## Swift Package Manager

Learn more about Swift Package Manager integration in
[our guide](https://firebase.google.com/docs/ios/swift-package-manager).

## Swift Extensions

Firebase Apple platform SDK Swift extensions were formerly small, open source
add-ons to the existing Firebase Apple platform libraries that enable your code
to use Swift language-specific features. These APIs have since been added
directly to the main libraries and don't need to be included separately. If you
formerly had a Swift extension SDK in your codebase, see the
[migration guide](https://firebase.google.com/docs/ios/swift-migration)
for upgrade instructions.

## SwiftUI

Firebase fully supports SwiftUI, though the setup will be slightly different
from UIKit apps in order for Firebase to function correctly in a fully SwiftUI
environment. Take a look at this
[blog post](https://peterfriese.dev/swiftui-new-app-lifecycle-firebase/)
by Peter Friese for more details.

SwiftUI applications must disable swizzling due to a
[known issue](https://github.com/firebase/firebase-ios-sdk/issues/10417).
See the [app delegate swizzling](https://firebase.google.com/docs/ios/learn-more#app_delegate_swizzling)
section for more details.

## App delegate swizzling

Firebase swizzles some methods in your app's app delegate class to
automatically connect certain Firebase services to OS callbacks, like
FCM and the APNs token. You can disable swizzling in your app by
adding the flag `FirebaseAppDelegateProxyEnabled` in the app's `Info.plist` file
and setting it to `NO`.

Four Firebase products use App Delegate swizzling: Analytics,
App Distribution, Authentication, and FCM.
If you've disabled swizzling in your application and you use any of the
following products, refer to the product-specific guide to learn about how to
use the product without swizzling:

- [Analytics](https://firebase.google.com/docs/analytics/screenviews#manually_track_screens)
- [App Distribution](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=ios#add-appdistro)
- [Authentication](https://firebase.google.com/docs/auth/ios/phone-auth#appendix:-using-phone-sign-in-without-swizzling)
- [FCM](https://firebase.google.com/docs/ios/docs/cloud-messaging/ios/client#method_swizzling_in)

## Supporting iOS 14

iOS 14 includes new changes to user permissions surrounding the user's
advertising identifier. See the
[preparing for iOS 14 guide](https://firebase.google.com/docs/ios/prepare-for-ios-14)
for more details on whether or not your app may be affected.

## Ongoing support for Objective-C

To ease maintenance of our Apple platforms documentation, Firebase has decided
to concentrate on Swift snippets and code samples in our guides and other
developer materials. Objective-C snippets will be removed from our guides
starting January 1, 2024. We will continue to maintain up-to-date
[reference documentation](https://firebase.google.com/docs/reference/ios/modules) for
Objective-C for all Firebase products.

## Open source resources for Firebase Apple platform SDKs

Firebase supports open source development, and we encourage community
contributions and feedback.

### Firebase Apple platform SDKs

All Firebase SDKs for Apple platforms except Analytics are developed as
open source libraries in our public
[Firebase GitHub repository](https://github.com/firebase/firebase-ios-sdk).

### FirebaseUI

FirebaseUI is a set of utility libraries built on Firebase, including a drop-in
UI flow for authentication and data utilities for Cloud Firestore and
Realtime Database. See more details about FirebaseUI on our
[GitHub page](https://github.com/firebase/FirebaseUI-iOS).

### Quickstart samples

Firebase maintains a collection of quickstart samples for most Firebase APIs on
iOS. Find these quickstarts in our public Firebase GitHub
[quickstart repository](https://github.com/firebase/quickstart-ios/).

You can open each quickstart in Xcode, then run them on a mobile device or
simulator. Or you can use these quickstarts as example code for using Firebase
SDKs.