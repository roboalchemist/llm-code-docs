# Source: https://firebase.google.com/docs/app-check/ios/devicecheck-provider.md.txt

This page shows you how to enable App Check in an Apple app, using the
built-in DeviceCheck provider. When you enable App Check, you help ensure
that only your app can access your project's Firebase resources. See an
[Overview](https://firebase.google.com/docs/app-check) of this feature.

If you want to use App Check with your own custom provider, see
[Implement a custom App Check provider](https://firebase.google.com/docs/app-check/ios/custom-provider).

## 1. Set up your Firebase project

1. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup) if you haven't already
   done so.

2. On the Apple developer site, [create a DeviceCheck private key](https://developer.apple.com/help/account/configure-app-capabilities/create-a-devicecheck-private-key/).

3. Register your apps to use App Check with the DeviceCheck provider in the
   [**App Check**](https://console.firebase.google.com/project/_/appcheck) section of the
   Firebase console. You will need to provide the private key you created in
   the previous step.

   You usually need to register all of your project's apps, because once you
   enable enforcement for a Firebase product, only registered apps will be able
   to access the product's backend resources.
4. <br />

   <br />

   **Optional** : In the app registration settings, set a custom time-to-live
   (TTL) for App Check tokens issued by the provider. You can set the TTL
   to any value between 30 minutes and 7 days. When changing this value, be
   aware of the following tradeoffs:
   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.
   - Quota and cost: Shorter TTLs and frequent re-attestation deplete your quota faster, and for paid services, potentially cost more. See [Quotas \& limits](https://firebase.google.com/docs/app-check#quotas_limits).

   The default TTL of
   **1 hour**
   is reasonable for most apps. Note that the App Check library refreshes
   tokens at approximately half the TTL duration.

   <br />

   <br />

## 2. Add the App Check library to your app

1. Use [Swift Package Manager](https://firebase.google.com/docs/ios/swift-package-manager) to install and
   manage Firebase dependencies.

   In Xcode, with your app project open, navigate to **File \> Add Packages** ,
   add the Firebase Apple platforms SDK repository
   (`https://github.com/firebase/firebase-ios-sdk`), and choose the
   **FirebaseAppCheck** library.

   > [!NOTE]
   > **Note:** If you've already added the Firebase Apple platforms SDK to your project, you can add **FirebaseAppCheck** to your app target using the **Frameworks, Libraries, and Embedded Content** section of your target's settings.

## Next steps

Once the App Check library is installed in your app, start distributing the
updated app to your users.

The updated client app will begin sending App Check tokens along with every
request it makes to Firebase, but Firebase products will not require the tokens
to be valid until you enable enforcement in the App Check section of the
Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't
disrupt your existing legitimate users. On the other hand, if you're seeing
suspicious use of your app resources, you might want to enable enforcement
sooner.

To help make this decision, you can look at App Check metrics for the
services you use:

- [Monitor App Check request metrics](https://firebase.google.com/docs/app-check/monitor-metrics) for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [Monitor App Check request metrics for Cloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### Enable App Check enforcement

When you understand how App Check will affect your users and you're ready to
proceed, you can enable App Check enforcement:

- [Enable App Check enforcement](https://firebase.google.com/docs/app-check/enable-enforcement) for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [Enable App Check enforcement for Cloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### Use App Check in debug environments

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as a simulator during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider.

See [Use App Check with the debug provider on Apple platforms](https://firebase.google.com/docs/app-check/ios/debug-provider).