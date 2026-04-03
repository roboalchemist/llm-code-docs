# Source: https://firebase.google.com/docs/app-check/ios/app-attest-provider.md.txt

This page shows you how to enableApp Checkin an Apple app, using the built-in App Attest provider. When you enableApp Check, you help ensure that only your app can access your project's Firebase resources. See an[Overview](https://firebase.google.com/docs/app-check)of this feature.

App Checkuses[App Attest](https://developer.apple.com/documentation/devicecheck/establishing_your_app_s_integrity)to verify that requests to Firebase services are coming from your authentic app.App Checkcurrently does not use App Attest to[analyze fraud risk](https://developer.apple.com/documentation/devicecheck/assessing_fraud_risk).

If you want to useApp Checkwith your own custom provider, see[Implement a customApp Checkprovider](https://firebase.google.com/docs/app-check/ios/custom-provider).
| **Note:** If you are adding App Attest to a production app with a large active user base, Apple recommends[gradually onboarding users](https://developer.apple.com/documentation/devicecheck/preparing-to-use-the-app-attest-service#Onboard-users-gradually)to avoid encountering quota limits.

## 1. Set up your Firebase project

1. You will need Xcode 12.5+ to use App Attest.

2. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup)if you haven't already done so.

3. Register your apps to useApp Checkwith the App Attest provider in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole.

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

   Make sure you're also using the latest version of any other Firebase SDKs you depend on.
2. Run`pod install`and open the created`.xcworkspace`file.

3. In Xcode, add the**App Attest**capability to your app.

4. In your project's`.entitlements`file, set the App Attest environment to`production`.

   | **Note:** TheApp Checkbeta currently doesn't accept tokens generated in the App Attest sandbox environment.

## 3. InitializeApp Check

You will need to initializeApp Checkbefore you use any other Firebase SDKs.

First, write an implementation of`AppCheckProviderFactory`. The specifics of your implementation will depend on your use case.

For example, If you only have users on iOS 14 and later, you can simply always create`AppAttestProvider`objects:  

### Swift

**Note:**This Firebase product is not available on watchOS targets.  

```swift
class YourSimpleAppCheckProviderFactory: NSObject, AppCheckProviderFactory {
  func createProvider(with app: FirebaseApp) -> AppCheckProvider? {
    return AppAttestProvider(app: app)
  }
}
```

<br />

### Objective-C

**Note:**This Firebase product is not available on watchOS targets.  

```objective-c
@interface YourSimpleAppCheckProviderFactory : NSObject <FIRAppCheckProviderFactory>
@end

@implementation YourSimpleAppCheckProviderFactory

- (nullable id<FIRAppCheckProvider>)createProviderWithApp:(nonnull FIRApp *)app {
  return [[FIRAppAttestProvider alloc] initWithApp:app];
}

@end
```

Or, you can create`AppAttestProvider`objects on iOS 14 and later, and fall back to`DeviceCheckProvider`on earlier versions:  

### Swift

**Note:**This Firebase product is not available on watchOS targets.  

```swift
class YourAppCheckProviderFactory: NSObject, AppCheckProviderFactory {
  func createProvider(with app: FirebaseApp) -> AppCheckProvider? {
    if #available(iOS 14.0, *) {
      return AppAttestProvider(app: app)
    } else {
      return DeviceCheckProvider(app: app)
    }
  }
}
```

<br />

### Objective-C

**Note:**This Firebase product is not available on watchOS targets.  

```objective-c
@interface YourAppCheckProviderFactory : NSObject <FIRAppCheckProviderFactory>
@end

@implementation YourAppCheckProviderFactory

- (nullable id<FIRAppCheckProvider>)createProviderWithApp:(nonnull FIRApp *)app {
  if (@available(iOS 14.0, *)) {
    return [[FIRAppAttestProvider alloc] initWithApp:app];
  } else {
    return [[FIRDeviceCheckProvider alloc] initWithApp:app];
  }
}

@end
```

<br />

After you have implemented a`AppCheckProviderFactory`class, configureApp Checkto use it:  

### Swift

**Note:**This Firebase product is not available on watchOS targets.  

```swift
let providerFactory = YourAppCheckProviderFactory()
AppCheck.setAppCheckProviderFactory(providerFactory)

FirebaseApp.configure()
```

<br />

### Objective-C

**Note:**This Firebase product is not available on watchOS targets.  

```objective-c
YourAppCheckProviderFactory *providerFactory =
        [[YourAppCheckProviderFactory alloc] init];
[FIRAppCheck setAppCheckProviderFactory:providerFactory];

[FIRApp configure];
```

<br />

## Next steps

Once theApp Checklibrary is installed in your app, start distributing the updated app to your users.
| **Note:** If you are adding App Attest to a production app with a large active user base, Apple recommends[gradually onboarding users](https://developer.apple.com/documentation/devicecheck/preparing-to-use-the-app-attest-service#Onboard-users-gradually)to avoid encountering quota limits.

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