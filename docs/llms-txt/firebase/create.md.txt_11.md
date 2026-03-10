# Source: https://firebase.google.com/docs/dynamic-links/ios/create.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

You can create short or long Dynamic Links with the Firebase Dynamic Links Builder API.
This API accepts either a long Dynamic Link or an object containing Dynamic Link
parameters, and returns URLs like the following examples:

```
https://example.com/link/WXYZ
https://example.page.link/WXYZ
```

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

1. In the Firebase console, open the **Dynamic Links** section.
2. If you have not already accepted the terms of service and set a URI prefix
   for your Dynamic Links, do so when prompted.

   If you already have a Dynamic Links URI prefix, take a note of it. You need to
   provide it when you programmatically create Dynamic Links.

   ![](https://firebase.google.com/static/docs/dynamic-links/images/dynamic-links-domain.png)
3. **Recommended** : Specify the URL patterns allowed in your deep links and fallback links. By doing so, you prevent unauthorized parties from creating Dynamic Links that redirect from your domain to sites you don't control. See [Allow specific URL patterns](https://firebase.google.com/docs/dynamic-links/allow-specific-url-patterns).
4. Ensure that your app's App Store ID and your App ID prefix is
   specified in your app's settings. To view and edit your app's settings, go
   to your Firebase project's
   [Settings page](https://console.firebase.google.com/project/_/settings/general/) and select your iOS app.

   Confirm that your Firebase project is properly configured to use
   Dynamic Links in your iOS app by opening the
   `apple-app-site-association` file that is hosted on your
   Dynamic Links domain. Firebase will serve the
   `apple-app-site-association` file from the root of the
   domain as well as the `.well-known` subdirectory. For
   example:

   ```
       https://example.com/apple-app-site-association
       https://example.com/.well-known/apple-app-site-association
       
   ```

   If your app is connected, the `apple-app-site-association` file contains a reference
   to your app's App ID prefix and bundle ID. For example:

   ```
   {"applinks":{"apps":[],"details":[{"appID":"1234567890.com.example.ios","paths":["/*"]}]}}
   ```

   If the `details` property is empty, double-check that you specified
   your App ID prefix. Note that your App ID prefix may not be the same as your Team ID.

## Add Firebase to your app

1. Import the `FirebaseCore` module in your `UIApplicationDelegate`, as well as any other [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses. For example, to use Cloud Firestore and Authentication:

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
2. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp) shared instance in your app delegate's `application(_:didFinishLaunchingWithOptions:)` method:

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
3. If you're using SwiftUI, you must create an application delegate and attach it to your `App` struct via `UIApplicationDelegateAdaptor` or `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

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

## Use the Firebase console

If you want to generate a single Dynamic Link, either for testing purposes, or for your marketing team
to easily create a link that can be used in something like a social media post, the simplest way would
be to visit the [Firebase console](https://console.firebase.google.com/project/_/durablelinks/links/)
and create one manually following the step-by-step form.

## Use the iOS Builder API

[Video](https://www.youtube.com/watch?v=LqCi-TaUfJs)

You can use the iOS Builder API to build Dynamic Links from parameters, or to
shorten a long Dynamic Link.

### Create a Dynamic Link from parameters

To create a Dynamic Link, create a new `DynamicLinkComponents` object
and specify the Dynamic Link parameters by setting the object's corresponding
properties. Then, get the long link from the object's `url`
property or get the short link by calling `shorten()`.

The following minimal example creates a long Dynamic Link to
`https://www.example.com/my-page` that opens with your iOS app on
iOS and the app `com.example.android` on Android:

#### Swift

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```swift
guard let link = URL(string: "https://www.example.com/my-page") else { return }
let dynamicLinksDomainURIPrefix = "https://example.com/link"
let linkBuilder = DynamicLinkComponents(link: link, domainURIPrefix: dynamicLinksDomainURIPRefix)
linkBuilder.iOSParameters = DynamicLinkIOSParameters(bundleID: "com.example.ios")
linkBuilder.androidParameters = DynamicLinkAndroidParameters(packageName: "com.example.android")

guard let longDynamicLink = linkBuilder.url else { return }
print("The long URL is: \(longDynamicLink)")
```

#### Objective-C

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```objective-c
NSURL *link = [[NSURL alloc] initWithString:@"https://www.example.com/my-page"];
NSString *dynamicLinksDomainURIPrefix = @"https://example.com/link";
FIRDynamicLinkComponents *linkBuilder = [[FIRDynamicLinkComponents alloc]
                                         initWithLink:link
                                               domainURIPrefix:dynamicLinksDomainURIPrefix];
linkBuilder.iOSParameters = [[FIRDynamicLinkIOSParameters alloc]
                             initWithBundleID:@"com.example.ios"];
linkBuilder.androidParameters = [[FIRDynamicLinkAndroidParameters alloc]
                                 initWithPackageName:@"com.example.android"];

NSLog(@"The long URL is: %@", linkBuilder.url);
```

To create a short Dynamic Link, build a `DynamicLinkComponents` the
same way, and then call `shorten()`.

Building a short link requires a network call, so instead of directly
returning the link, `shorten()` accepts a completion handler, which
is called when the request completes. For example:

#### Swift

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```swift
linkBuilder.shorten() { url, warnings, error in
  guard let url = url, error != nil else { return }
  print("The short URL is: \(url)")
}
```

#### Objective-C

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```objective-c
[linkBuilder shortenWithCompletion:^(NSURL * _Nullable shortURL,
                                     NSArray<NSString *> * _Nullable warnings,
                                     NSError * _Nullable error) {
  if (error || shortURL == nil) { return; }
  NSLog(@"The short URL is: %@", shortURL);
}];
      
```

By default, short Dynamic Links are generated with 17-character link suffixes that
make it extremely unlikely that someone can guess a valid Dynamic Link. If, for
your use case, there's no harm in someone successfully guessing a short link,
you might prefer to generate suffixes that are only as long as necessary to be
unique, which you can do by setting the
`dynamicLinkComponentsOptions` property:

#### Swift

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```swift
linkBuilder.options = DynamicLinkComponentsOptions()
linkBuilder.options.pathLength = .short
linkBuilder.shorten() { url, warnings, error in
  guard let url = url, error != nil else { return }
  print("The short URL is: \(url)")
}
```

#### Objective-C

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```objective-c
linkBuilder.dynamicLinkComponentsOptions = [[FIRDynamicLinkComponentsOptions alloc] init];
linkBuilder.dynamicLinkComponentsOptions.pathLength = FIRShortDynamicLinkPathLengthShort;
[linkBuilder shortenWithCompletion:^(NSURL * _Nullable shortURL,
                                     NSArray<NSString *> * _Nullable warnings,
                                     NSError * _Nullable error) {
  if (error || shortURL == nil) { return; }
  NSLog(@"The short URL is: %@", shortURL);
}];
      
```

#### Dynamic Link parameters

You can use the Dynamic Link Builder API to create Dynamic Links with any of the
supported parameters. See the
[API reference](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink) for details.

The following example creates a Dynamic Link with several common parameters
set:

#### Swift

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```swift
guard let link = URL(string: "https://www.example.com/my-page") else { return }
let dynamicLinksDomainURIPrefix = "https://example.com/link"
let linkBuilder = DynamicLinkComponents(link: link, domainURIPRefix: dynamicLinksDomainURIPrefix)

linkBuilder.iOSParameters = DynamicLinkIOSParameters(bundleID: "com.example.ios")
linkBuilder.iOSParameters.appStoreID = "123456789"
linkBuilder.iOSParameters.minimumAppVersion = "1.2.3"

linkBuilder.androidParameters = DynamicLinkAndroidParameters(packageName: "com.example.android")
linkBuilder.androidParameters.minimumVersion = 123

linkBuilder.analyticsParameters = DynamicLinkGoogleAnalyticsParameters(source: "orkut",
                                                                       medium: "social",
                                                                       campaign: "example-promo")

linkBuilder.iTunesConnectParameters = DynamicLinkItunesConnectAnalyticsParameters()
linkBuilder.iTunesConnectParameters.providerToken = "123456"
linkBuilder.iTunesConnectParameters.campaignToken = "example-promo"

linkBuilder.socialMetaTagParameters = DynamicLinkSocialMetaTagParameters()
linkBuilder.socialMetaTagParameters.title = "Example of a Dynamic Link"
linkBuilder.socialMetaTagParameters.descriptionText = "This link works whether the app is installed or not!"
linkBuilder.socialMetaTagParameters.imageURL = "https://www.example.com/my-image.jpg"

guard let longDynamicLink = linkBuilder.url else { return }
print("The long URL is: \(longDynamicLink)")
```

#### Objective-C

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```objective-c
NSURL *link = [[NSURL alloc] initWithString:@"https://www.example.com/my-page"];
NSString *dynamicLinksDomainURIPrefix = @"https://example.com/link";
FIRDynamicLinkComponents *linkBuilder = [[FIRDynamicLinkComponents alloc]
                                         initWithLink:link
                                         domainURIPrefix:dynamicLinksDomainURIPrefix];

linkBuilder.iOSParameters = [[FIRDynamicLinkIOSParameters alloc]
                             initWithBundleID:@"com.example.ios"];
linkBuilder.iOSParameters.appStoreID = @"123456789";
linkBuilder.iOSParameters.minimumAppVersion = @"1.2.3";

linkBuilder.androidParameters = [[FIRDynamicLinkAndroidParameters alloc]
                                 initWithPackageName:@"com.example.android"];
linkBuilder.androidParameters.minimumVersion = 123;

linkBuilder.analyticsParameters = [[FIRDynamicLinkGoogleAnalyticsParameters alloc]
                                   initWithSource:@"orkut"
                                           medium:@"social"
                                         campaign:@"example-promo"];

linkBuilder.iTunesConnectParameters = [[FIRDynamicLinkItunesConnectAnalyticsParameters alloc] init];
linkBuilder.iTunesConnectParameters.providerToken = @"123456";
linkBuilder.iTunesConnectParameters.campaignToken = @"example-promo";

linkBuilder.socialMetaTagParameters = [[FIRDynamicLinkSocialMetaTagParameters alloc] init];
linkBuilder.socialMetaTagParameters.title = @"Example of a Dynamic Link";
linkBuilder.socialMetaTagParameters.descriptionText = @"This link works whether the app is installed or not!";
linkBuilder.socialMetaTagParameters.imageURL = @"https://www.example.com/my-image.jpg";

NSLog(@"The long URL is: %@", linkBuilder.url);
```

You can set Dynamic Link parameters with the following objects and properties:

| DynamicLinkComponents ||
|---|---|
| link | The link your app will open. Specify a URL that your app can handle, typically the app's content or payload, which initiates app-specific logic (such as crediting the user with a coupon or displaying a welcome screen). This link must be a well-formatted URL, be properly URL-encoded, use either HTTP or HTTPS, and cannot be another Dynamic Link. > [!NOTE] > When users open a Dynamic Link on a desktop web browser, they will load this URL (unless the `ofl` parameter is specified). If you don't have a web equivalent to the linked content, the URL doesn't need to point to a valid web resource. In this situation, you should set up a redirect from this URL to, for example, your home page. |
| domainURIPrefix | Your Dynamic Link URL prefix, which you can find in the Firebase console. A Dynamic Link domain looks like the following examples: ``` https://example.com/link https://example.page.link ``` |

| DynamicLinkAndroidParameters ||
|---|---|
| fallbackURL | The link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app. |
| minimumVersion | The [`versionCode`](http://developer.android.com/tools/publishing/versioning.html#appversioning) of the minimum version of your app that can open the link. If the installed app is an older version, the user is taken to the Play Store to upgrade the app. |

| DynamicLinkIOSParameters ||
|---|---|
| appStoreID | Your app's App Store ID, used to send users to the App Store when the app isn't installed |
| fallbackURL | The link to open when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app. |
| customScheme | Your app's custom URL scheme, if defined to be something other than your app's bundle ID |
| iPadFallbackURL | The link to open on iPads when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the web version of the content, or display a promotional page for your app. |
| iPadBundleID | The bundle ID of the iOS app to use on iPads to open the link. The app must be connected to your project from the Overview page of the Firebase console. |
| minimumAppVersion | The [version number](https://developer.apple.com/library/content/technotes/tn2420/_index.html) of the minimum version of your app that can open the link. This flag is passed to your app when it is opened, and your app must decide what to do with it. |

| DynamicLinkNavigationInfoParameters ||
|---|---|
| forcedRedirectEnabled | If set to '1', skip the app preview page when the Dynamic Link is opened, and instead redirect to the app or store. The app preview page (enabled by default) can more reliably send users to the most appropriate destination when they open Dynamic Links in apps; however, if you expect a Dynamic Link to be opened only in apps that can open Dynamic Links reliably without this page, you can disable it with this parameter. This parameter will affect the behavior of the Dynamic Link only on iOS. |

| DynamicLinkSocialMetaTagParameters ||
|---|---|
| title | The title to use when the Dynamic Link is shared in a social post. |
| descriptionText | The description to use when the Dynamic Link is shared in a social post. |
| imageURL | The URL to an image related to this link. The image should be at least 300x200 px, and less than 300 KB. |

| DynamicLinkGoogleAnalyticsParameters ||
|---|---|
| source medium campaign term content | Google Play analytics parameters. These parameters (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) are passed on to the Play Store as well as appended to the link payload. |

| DynamicLinkItunesConnectAnalyticsParameters ||
|---|---|
| providerToken affiliateToken campaignToken | iTunes Connect analytics parameters. These parameters (`pt`, `at`, `ct`) are passed to the App Store. |

### Shorten a long Dynamic Link

To shorten a long Dynamic Link, pass the long Dynamic Link to
`shortenURL(url:options:)` along with a
`DynamicLinkComponentsOptions` object if you want to generate a
link with a short suffix:

#### Swift

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```swift
DynamicLinkComponents.shortenURL(url: longLinkUrl, options: nil) { url, warnings, error in
  guard let url = url, error != nil else { return }
  print("The short URL is: \(url)")
}
```

#### Objective-C

**Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

```objective-c
[FIRDynamicLinkComponents shortenURL:longLinkUrl
                             options:nil
                          completion:^(NSURL * _Nullable shortURL,
                                       NSArray<NSString *> * _Nullable warnings,
                                       NSError * _Nullable error) {
  if (error || shortURL == nil) { return; }
  NSLog(@"The short URL is: %@", shortURL);
}];
```

## Specifying a custom URL scheme for Dynamic Links

By default, Dynamic Links uses your app's bundle identifier as the URL scheme needed to open up your
application. We recommend staying with this default value to keep your implementation simple.

However, developers who are already using a custom URL scheme for other purposes may wish to use
this same custom URL scheme for their Dynamic Links as well. If you are in this situation, you can specify
a different URL scheme for your Firebase Dynamic Links by following these steps:

1. When setting up your app, make sure you specify the default URL scheme to be used by your application before configuring your `FirebaseApp` shared instance:

   #### Swift

   **Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

   ```swift
   func application(_ application: UIApplication,
                    didFinishLaunchingWithOptions launchOptions: [UIApplication
                      .LaunchOptionsKey: Any]?) -> Bool {
     // Set deepLinkURLScheme to the custom URL scheme you defined in your
     // Xcode project.
     FirebaseOptions.defaultOptions()?.deepLinkURLScheme = customURLScheme
     FirebaseApp.configure()

     return true
   }
   ```

   #### Objective-C

   **Note:** This Firebase product is not available on macOS, Mac Catalyst, tvOS, or watchOS targets.

   ```objective-c
   - (BOOL)application:(UIApplication *)application
       didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
     // Set deepLinkURLScheme to the custom URL scheme you defined in your
     // Xcode project.
     [FIROptions defaultOptions].deepLinkURLScheme = CUSTOM_URL_SCHEME;
     [FIRApp configure];

     return YES;
   }
   ```
2. Whenever you create any Dynamic Link, you will need to specify the custom URL scheme that your app uses. You can do this through the Firebase console, setting the `customScheme` in the Builder API, specifying the `ius` parameter in your URL, or sending the `iosCustomScheme` parameter to the REST API

## Next steps

Now that you've created Dynamic Links, you need to set up your app to receive
Dynamic Links and send users to the right place in your app after a user opens them.

To receive Dynamic Links in your app, see the documentation for
[iOS](https://firebase.google.com/docs/dynamic-links/ios/receive),
[Android](https://firebase.google.com/docs/dynamic-links/android/receive),
[C++](https://firebase.google.com/docs/dynamic-links/cpp/receive), and
[Unity](https://firebase.google.com/docs/dynamic-links/unity/receive).