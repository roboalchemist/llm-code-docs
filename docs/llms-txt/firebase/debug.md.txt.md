# Source: https://firebase.google.com/docs/dynamic-links/debug.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

## Preview page flowchart

To help you debug your Dynamic Links, you can preview your Dynamic Links' behavior on
different platforms and configurations with an automatically-generated
flowchart. Generate the flowchart by adding the `d=1` parameter to
any short or long Dynamic Link. For example, `example.page.link/suffix?d=1` for a
short Dynamic Link.

The preview page looks like this:

![A screenshot of the preview page](https://firebase.google.com/static/docs/dynamic-links/images/preview-page.png)

## iOS self-diagnostic tool

If you are having issues with your Dynamic Link integration on iOS, use the self-diagnostic
tool which is built into the Dynamic Links SDK versions 2.1.0 and newer.

The tool can be invoked from anywhere in your code as follows.

### Swift


**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

    DynamicLinks.performDiagnostics(completion: nil)

### Objective-C


**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

    [FIRDynamicLinks performDiagnosticsWithCompletion:nil];

By default, the tool prints debug information, including any detected errors, to
standard output. For example, let's say your iOS app isn't receiving Dynamic Links as
expected. The self-diagnostic tool will output information like:

    --- Firebase Dynamic Links diagnostic output start ---
    Firebase Dynamic Links framework version 2.1.0
    System information: OS iOS, OS version 11.0, model iPhone
    Current date 2017-08-14 22:52:56 +0000
    AutomaticRetrievalEnabled: YES
    ERROR: Specified custom URL scheme is com.google.AppInvitesSample.dev but Info.plist do not contain such scheme in CFBundleURLTypes key.
    AppID Prefix: EQHXZ8M8AV, Team ID: EQHXZ8M8AV, AppId Prefix equal to Team ID: YES
    performDiagnostic detected 1 ERRORS.
    --- Firebase Dynamic Links diagnostic output end ---

In this example, Dynamic Links isn't working because the custom URL scheme isn't
properly configured.

> [!NOTE]
> **Tip**: Copy the self-diagnostic tool's output when you reach out to Firebase support so we can better help you.

## Common errors and warnings

### Android app lacks SHA256. AppLinks is not enabled for the app.

To use [Android App Links](https://developer.android.com/training/app-links/index.html)
with your app, you must [create a SHA256 certificate](https://developer.android.com/training/app-links/index.html).

Once you create the SHA256 certificate, add it to your app in the
[Firebase console](https://console.firebase.google.com/). See [Add a SHA fingerprint](https://support.google.com/firebase/answer/7000104#sha1).

### We could not find Android package name 'com.example' and/or iOS bundle ID 'com.example'

To use Dynamic Links with your Android or iOS app, you must add your app to your
Firebase project. See [Add an app](https://support.google.com/firebase/answer/7000104#apps).

### iOS app lacks Team ID. UniversalLinks is not
enabled for the app.

To use [Universal Links](https://developer.apple.com/ios/universal-links/)
with your app, you must add a Team ID in the [Firebase console](https://console.firebase.google.com/).
See [Add an App Store ID or Team ID](https://support.google.com/firebase/answer/7000104?hl=en&ref_topic=6400762#appid).

You can find your Team ID in the Apple Member Center under the [Membership tab](https://developer.apple.com/account/#/membership).

### iOS store ID does not exist in the given iOS bundle ID. Skipping.

This means that the app listed at `https://itunes.apple.com/us/app/yourapp/idSTOREID`
does not have the given bundle ID.

### Invalid iOS custom scheme

A custom scheme must begin with an alphabetic character (A--Z, a--z) and may be
followed by any number of alphanumeric characters, `+`, `-`, or `.` It also cannot be
any of the following: "javascript", "vbscript", "data", "blob", "http", "https",
"mailto", "livescript", "facetime", "facetime-audio".

### Your project has not configured Dynamic Links

To start using Dynamic Links, you must enable it for your project in
the [Firebase console](https://console.firebase.google.com/).

### Something else?

If you have a different issue, see the [Firebase support page](https://firebase.google.com/support).