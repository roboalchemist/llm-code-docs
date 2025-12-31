# Source: https://firebase.google.com/docs/app-check/unity/default-providers.md.txt

# Source: https://firebase.google.com/docs/app-check/flutter/default-providers.md.txt

# Source: https://firebase.google.com/docs/app-check/cpp/default-providers.md.txt

# Source: https://firebase.google.com/docs/app-check/unity/default-providers.md.txt

# Source: https://firebase.google.com/docs/app-check/flutter/default-providers.md.txt

# Source: https://firebase.google.com/docs/app-check/cpp/default-providers.md.txt

<br />

This page shows you how to enable App Check in a C++ app, using the default providers: Play Integrity on Android, and Device Check or App Attest on Apple platforms. When you enable App Check, you help ensure that only your app can access your project's Firebase resources. See an[Overview](https://firebase.google.com/docs/app-check)of this feature.

## 1. Set up your Firebase project

1. [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup)if you haven't already done so.

2. Register your apps to use App Check with the Play Integrity, Device Check, or App Attest providers in the[**Project Settings \> App Check**](https://console.firebase.google.com/project/_/appcheck)section of the Firebase console.

   You usually need to register all of your project's apps, because once you enable enforcement for a Firebase product, only registered apps will be able to access the product's backend resources.

   For detailed instructions on how to register with each provider, refer to the Android and iOS specific documentation.
3. **Optional**: In the app registration settings, set a custom time-to-live (TTL) for App Check tokens issued by the provider. You can set the TTL to any value between 30 minutes and 7 days. When changing this value, be aware of the following tradeoffs:

   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.
   - Quota and cost: Shorter TTLs and frequent re-attestation deplete your quota faster, and for paid services, potentially cost more. See[Quotas \& limits](https://firebase.google.com/docs/app-check#quotas_limits).

   The default TTL is reasonable for most apps. Note that the App Check library refreshes tokens at approximately half the TTL duration.

## 2. Add the App Check library to your app

Include the App Check library in your set of dependencies, following[the setup instructions](https://firebase.google.com/docs/cpp/setup#add-sdks)for App Check.

## 3. Initialize App Check

Add the following initialization code to your app so that it runs before you use any Firebase services including any creation of Firebase Apps.  

### Android

1. Include the header file for`firebase::app_check`:

   ```c++
   #include "firebase/app_check.h"
   ```
2. Initialize the App Check library with the Play Integrity provider:

       firebase::app_check::AppCheck::SetAppCheckProviderFactory(
         firebase::app_check::PlayIntegrityProviderFactory::GetInstance());

### iOS+

1. Include the header file for`firebase::app_check`:

   ```c++
   #include "firebase/app_check.h"
   ```
2. Initialize the App Check library with the Device Check or App Attest provider:

       firebase::app_check::AppCheck::SetAppCheckProviderFactory(
         firebase::app_check::DeviceCheckProviderFactory::GetInstance());

## Next steps

Once the App Check library is installed in your app, start distributing the updated app to your users.

The updated client app will begin sending App Check tokens along with every request it makes to Firebase, but Firebase products will not require the tokens to be valid until you enable enforcement in the App Check section of the Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't disrupt your existing legitimate users. On the other hand, if you're seeing suspicious use of your app resources, you might want to enable enforcement sooner.

To help make this decision, you can look at App Check metrics for the services you use:

- [Monitor App Check request metrics](https://firebase.google.com/docs/app-check/monitor-metrics)for Realtime Database, Cloud Firestore, and Cloud Storage.
- [Monitor App Check request metrics for Cloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### Enable App Check enforcement

When you understand how App Check will affect your users and you're ready to proceed, you can enable App Check enforcement:

- [Enable App Check enforcement](https://firebase.google.com/docs/app-check/enable-enforcement)for Realtime Database, Cloud Firestore, and Cloud Storage.
- [Enable App Check enforcement for Cloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### Use App Check in debug environments

If, after you have registered your app for App Check, you want to run your app in an environment that App Check would normally not classify as valid, such as on desktop, an emulator during development, or from a continuous integration (CI) environment, you can create a debug build of your app that uses the App Check debug provider instead of a real attestation provider.

See[Use App Check with the debug provider in C++ apps](https://firebase.google.com/docs/app-check/cpp/debug-provider).