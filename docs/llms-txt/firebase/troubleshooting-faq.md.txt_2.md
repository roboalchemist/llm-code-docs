# Source: https://firebase.google.com/docs/ios/troubleshooting-faq.md.txt

This page offers tips and troubleshooting for Apple platform-specific issues
that you might encounter when using Firebase.

Have other challenges or don't see your issue outlined below? Make sure to check
out the [main Firebase FAQ](https://firebase.google.com/support/faq) for more pan-Firebase or
product-specific FAQ.

You can also check out the
[Firebase Apple platforms SDK GitHub repo](https://github.com/firebase/firebase-ios-sdk/issues)
for an up-to-date list of reported issues and troubleshooting. We encourage you
to file your own Firebase Apple platforms SDK related issues there, too!

#### What versions of Xcode does Firebase support?

Firebase supports up to two major versions of Xcode, not including versions
of Xcode that Apple no longer supports. For example, starting in March 2019,
Apple required at least iOS 12 on all apps, meaning Xcode 9 support was
dropped and Xcode 10 was the only major version supported.

Changes to support for specific minor or patch versions of Xcode
(for example, 9.2.0 to 9.4.1) are determined based on the needs of the
Firebase Apple platforms SDK and a survey of developer usage. These changes
are reflected in the
[Firebase Apple platforms SDK release notes](https://firebase.google.com/support/release-notes/ios)
and on the [Firebase Apple platforms SDK setup page](https://firebase.google.com/docs/ios/setup).

To see the minimum Xcode version supported by the SDK, check
the requirements listed in
[Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).

Firebase support for Beta releases of Xcode is available on a "best effort"
basis. Developers can track and submit issues in the
[Firebase Apple platforms SDK repository on GitHub](https://github.com/firebase/firebase-ios-sdk/issues).

#### My app prompts the user for their password to access Keychain items on macOS. How do I fix this?

Upgrade your Firebase dependency to version 9.6.0 or higher and add the
\[Keychain Sharing capability\](/docs/ios/troubleshooting-faq#macos-keychain-sharing)
to your target.

#### Why does Firebase require the Keychain Sharing capability on macOS?

Firebase SDKs use keychain to store information like the Firebase
installation ID used for FCM. Without Keychain access, Firebase SDKs may not
function correctly. The macOS keychain behaves differently than the iOS-style
keychain that is used on other platforms (iOS, tvOS, macCatalyst,
and watchOS).

On macOS, apps use a shared keychain that may be modified by other apps and
processes. Unlike iOS, there is no sandboxed keychain that the app has
implicit access to. So, when a Mac app interacts with the keychain, the system
prompts the user for access since the Mac app may be modifying a keychain item
that it did not create. To address this discrepancy, Firebase queries the
keychain with the `kSecUseDataProtectionKeychain` key, which tells
the app to query a keychain item that is part of a keychain access group
(this is default behavior on other platforms). The Keychain Sharing capability
is required because the app needs it to synthesize an access group that can be
shared amongst its targets, thus giving permission for the app to freely
access keychain items in the access group.

For more information, see Apple's
[Keychain documentation](https://developer.apple.com/documentation/security/keychain_services/keychains).

#### In Xcode versions 13 and later, why can my UIKit apps not open some
URLs I've registered
in my Info.plist?

Apple introduced a limit of 50 `LSApplicationQueriesSchemes`
entries in `Info.plist` files. In 2015, Apple introduced
`LSApplicationQueriesSchemes` to limit the number of URL queries
each app could make. With the release of Xcode 13, these limits are enforced,
while in Xcode 12 and earlier there was no effective limit to the number of
schemes.

Some Firebase products, like Firebase Authentication and Firebase Dynamic Links,
require the use of custom URL schemes to redirect to your application. These
URLs conform to a concise and consistent URL scheme that should not count
significantly against the 50 link scheme limit.

Note that for apps that continue to register more than 50
`LSApplicationQueriesSchemes`, some schemes will
be silently ignored. The app may be unable to execute certain deeplinks,
depending on the order in which they are added.

<br />

<br />

<br />

#### What open source notices should I include in my app?

<br />

For Apple platforms, the Firebase SDK is distributed under the Apache 2.0
license.

<br />

<br />