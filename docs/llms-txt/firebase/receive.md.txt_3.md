# Source: https://firebase.google.com/docs/dynamic-links/ios/receive.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

To receive the Firebase Dynamic Links that [you created](https://firebase.google.com/docs/dynamic-links/create-links), you must include the Dynamic Links SDK in your app and call the
`handleUniversalLink:` and `dynamicLinkFromCustomSchemeURL:`
methods when your app loads to get the data passed in the Dynamic Link.

## Prerequisites

Before you begin, make sure to [add Firebase to your iOS
project](https://firebase.google.com/docs/ios/setup).

## Set up Firebase and the Dynamic Links SDK

Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```

> [!NOTE]
> **Note:** New projects should use the default (latest) SDK version, but you can choose an older version if needed.

3. Choose the Dynamic Links library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. For an optimal experience with Dynamic Links, we recommend [enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga) in your Firebase project and adding the Firebase SDK for Google Analytics to your app. You can select either the library without IDFA collection or with IDFA collection. See our FAQ on the [latest organization of modules in the Google Analytics for Firebase SDK](https://firebase.google.com/support/faq#analytics-odm2-sdk-refactor-ios).
6. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

Now, perform some configuration steps:

1. In the [Firebase console](https://console.firebase.google.com/), open the **Dynamic Links** section. Accept the terms of service if you are prompted to do so.
2. Ensure that your app's App Store ID and your App ID prefix is
   specified in your app's settings. To view and edit your app's settings, go
   to your Firebase project's
   [Settings page](https://console.firebase.google.com/project/_/settings/general/) and select your iOS app.

   You can confirm that your Firebase project is properly configured to use
   Dynamic Links in your iOS app by opening the following URL:

   ```
   https://your_dynamic_links_domain/apple-app-site-association
   ```

   If your app is connected, the `apple-app-site-association` file contains a reference
   to your app's App ID prefix and bundle ID. For example:

   ```
   {"applinks":{"apps":[],"details":[{"appID":"1234567890.com.example.ios","paths":["NOT /_/*","/*"]}]}}
   ```

   If the `details` field is empty, double-check that you specified
   your App ID prefix. Note that your App ID prefix may not be the same as your Team ID.
3. **Optional** : Disable the Dynamic Links SDK's use of the iOS
   pasteboard.

   By default, the Dynamic Links SDK uses the pasteboard to improve the
   reliability of post-install deep links. By using the pasteboard, Dynamic Links
   can make sure that when a user opens a Dynamic Link but needs to install your
   app first, the user can go immediately to the original linked content when
   opening the app for the first time after installation.

   The downside of this is that use of the pasteboard triggers a
   notification on iOS 14 and later. So, the first time users open your app,
   if the pasteboard contains a URL, they will see a notification that your
   app accessed the pasteboard, which can cause confusion.

   To disable this behavior, edit your Xcode project's
   `Info.plist` file and set the
   `FirebaseDeepLinkPasteboardRetrievalEnabled` key to
   `NO`.

   > [!CAUTION]
   > When you disable this feature, the Dynamic Links you receive will have a `https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink#matchtype` of `weak` at best. Adjust your app's logic accordingly.

## Open Dynamic Links in your app

1. In the **Info** tab of your app's Xcode project, create a new URL type to be used for Dynamic Links. Set the **Identifier** field to a unique value and the **URL scheme** field to be your bundle identifier, which is the default URL scheme used by Dynamic Links.
2. In the **Capabilities** tab of your app's Xcode project, enable Associated Domains and add the following to the **Associated
   Domains** list:

   ```
   applinks:your_dynamic_links_domain
   ```
3. If you want to receive Dynamic Links with a [fully-custom domain](https://firebase.google.com/docs/dynamic-links/custom-domains), in your Xcode project's `Info.plist` file, create a key called `FirebaseDynamicLinksCustomDomains` and set it to your app's Dynamic Links URL prefixes. For example:

   ```
   FirebaseDynamicLinksCustomDomains

     https://example.com/promos
     https://example.com/links/share
   ```
4. Import the `FirebaseCore` module in your `UIApplicationDelegate`, as well as any other [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses. For example, to use Cloud Firestore and Authentication:

   #### SwiftUI

   ```swift
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Swift

   ```swift
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
         
   ```
5. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp) shared instance in your app delegate's `application(_:didFinishLaunchingWithOptions:)` method:

   #### SwiftUI

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```objective-c
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
6. If you're using SwiftUI, you must create an application delegate and attach it to your `App` struct via `UIApplicationDelegateAdaptor` or `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

   #### SwiftUI

   ```swift
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
     @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

     var body: some Scene {
       WindowGroup {
         NavigationView {
           ContentView()
         }
       }
     }
   }
         
   ```
7. Next, in the `application:continueUserActivity:restorationHandler:
   ` method, handle links received as [Universal Links](https://developer.apple.com/library/ios/documentation/General/Conceptual/AppSearch/UniversalLinks.html) when the app is already installed:

   #### Swift

   **Note:** This product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

   ```swift
   func application(_ application: UIApplication, continue userActivity: NSUserActivity,
                    restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
     let handled = DynamicLinks.dynamicLinks()
       .handleUniversalLink(userActivity.webpageURL!) { dynamiclink, error in
         // ...
       }

     return handled
   }
   ```

   #### Objective-C

   **Note:** This product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

   ```objective-c
   - (BOOL)application:(UIApplication *)application
   continueUserActivity:(nonnull NSUserActivity *)userActivity
    restorationHandler:
   #if defined(__IPHONE_12_0) && (__IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_12_0)
   (nonnull void (^)(NSArray<id> *_Nullable))restorationHandler {
   #else
       (nonnull void (^)(NSArray *_Nullable))restorationHandler {
   #endif  // __IPHONE_12_0
     BOOL handled = [[FIRDynamicLinks dynamicLinks] handleUniversalLink:userActivity.webpageURL
                                                             completion:^(FIRDynamicLink * _Nullable dynamicLink,
                                                                          NSError * _Nullable error) {
                                                               // ...
                                                             }];
     return handled;
   }
   ```
8. Finally, in `application:openURL:options:` handle links received through your app's custom URL scheme. This method is called when your app is opened for the first time after installation.

   If the Dynamic Link isn't found on your app's first launch, this method will be called with the
   `DynamicLink`'s `url` set to `nil`, indicating that the SDK
   failed to find a matching pending Dynamic Link.

   #### Swift

   **Note:** This product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

   ```swift
   @available(iOS 9.0, *)
   func application(_ app: UIApplication, open url: URL,
                    options: [UIApplication.OpenURLOptionsKey: Any]) -> Bool {
     return application(app, open: url,
                        sourceApplication: options[UIApplication.OpenURLOptionsKey
                          .sourceApplication] as? String,
                        annotation: "")
   }

   func application(_ application: UIApplication, open url: URL, sourceApplication: String?,
                    annotation: Any) -> Bool {
     if let dynamicLink = DynamicLinks.dynamicLinks().dynamicLink(fromCustomSchemeURL: url) {
       // Handle the deep link. For example, show the deep-linked content or
       // apply a promotional offer to the user's account.
       // ...
       return true
     }
     return false
   }
   ```

   #### Objective-C

   **Note:** This product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

   ```objective-c
   - (BOOL)application:(UIApplication *)app
               openURL:(NSURL *)url
               options:(NSDictionary *)options {
     return [self application:app
                      openURL:url
            sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey]
                   annotation:options[UIApplicationOpenURLOptionsAnnotationKey]];
   }

   - (BOOL)application:(UIApplication *)application
               openURL:(NSURL *)url
     sourceApplication:(NSString *)sourceApplication
            annotation:(id)annotation {
     FIRDynamicLink *dynamicLink = [[FIRDynamicLinks dynamicLinks] dynamicLinkFromCustomSchemeURL:url];

     if (dynamicLink) {
       if (dynamicLink.url) {
         // Handle the deep link. For example, show the deep-linked content,
         // apply a promotional offer to the user's account or show customized onboarding view.
         // ...
       } else {
         // Dynamic link has empty deep link. This situation will happens if
         // Firebase Dynamic Links iOS SDK tried to retrieve pending dynamic link,
         // but pending link is not available for this device/App combination.
         // At this point you may display default onboarding view.
       }
       return YES;
     }
     return NO;
   }
   ```
   This step is particularly important when you've configured the Dynamic Links SDK to use the pasteboard for more reliable link matching. If you skip this step, users will see a pasteboard access notification every time they open your app, rather than only the first open.