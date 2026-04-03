# Source: https://firebase.google.com/docs/app-check/ios/devicecheck-provider.md.txt

This page shows you how to enableApp Checkin an Apple app, using the built-in DeviceCheck provider. When you enableApp Check, you help ensure that only your app can access your project's Firebase resources. See an[Overview](https://firebase.google.com/docs/app-check)of this feature.

If you want to useApp Checkwith your own custom provider, see[Implement a customApp Checkprovider](https://firebase.google.com/docs/app-check/ios/custom-provider).

## 1. Set up your Firebase project

1. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup)if you haven't already done so.

2. On the Apple developer site,[create a DeviceCheck private key](https://developer.apple.com/help/account/configure-app-capabilities/create-a-devicecheck-private-key/).

3. Register your apps to useApp Checkwith the DeviceCheck provider in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole. You will need to provide the private key you created in the previous step.

   You usually need to register all of your project's apps, because once you enable enforcement for a Firebase product, only registered apps will be able to access the product's backend resources.
4. <br />

   <br />

   **Optional** : In the app registration settings, set a custom time-to-live (TTL) forApp Checktokens issued by the provider. You can set the TTL to any value between 30 minutes and 7 days. When changing this value, be aware of the following tradeoffs:
   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.
   - Quota and cost: Shorter TTLs and frequent re-attestation deplete your quota faster, and for paid services, potentially cost more. See[Quotas \& limits](https://firebase.google.com/docs/app-check#quotas_limits).

   The default TTL of**1 hour** is reasonable for most apps. Note that theApp Checklibrary refreshes tokens at approximately half the TTL duration.

   <br />

   <br />

## 2. Add theApp Checklibrary to your app

1. Add the dependency forApp Checkto your project's`Podfile`:

   ```
   pod 'FirebaseAppCheck'
   ```

   Or, alternatively, you can use[Swift Package Manager](https://firebase.google.com/docs/ios/swift-package-manager)instead.

   Make sure you're also using the latest version of any Firebase service client libraries you depend on.
2. Run`pod install`and open the created`.xcworkspace`file.

## Next steps

Once theApp Checklibrary is installed in your app, start distributing the updated app to your users.

The updated client app will begin sendingApp Checktokens along with every request it makes to Firebase, but Firebase products will not require the tokens to be valid until you enable enforcement in theApp Checksection of the Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't disrupt your existing legitimate users. On the other hand, if you're seeing suspicious use of your app resources, you might want to enable enforcement sooner.

To help make this decision, you can look atApp Checkmetrics for the services you use:

- [MonitorApp Checkrequest metrics](https://firebase.google.com/docs/app-check/monitor-metrics)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [MonitorApp Checkrequest metrics forCloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### EnableApp Checkenforcement

When you understand howApp Checkwill affect your users and you're ready to proceed, you can enableApp Checkenforcement:

- [EnableApp Checkenforcement](https://firebase.google.com/docs/app-check/enable-enforcement)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [EnableApp Checkenforcement forCloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### UseApp Checkin debug environments

If, after you have registered your app forApp Check, you want to run your app in an environment thatApp Checkwould normally not classify as valid, such as a simulator during development, or from a continuous integration (CI) environment, you can create a debug build of your app that uses theApp Checkdebug provider instead of a real attestation provider.

See[UseApp Checkwith the debug provider on Apple platforms](https://firebase.google.com/docs/app-check/ios/debug-provider).