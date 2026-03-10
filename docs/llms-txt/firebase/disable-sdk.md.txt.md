# Source: https://firebase.google.com/docs/perf-mon/disable-sdk.md.txt

<button value="ios" default="">iOS+</button> <button value="android">Android</button> <button value="web">Web</button> <button value="flutter">Flutter</button>

<br />

To let your users opt-in or opt-out of using Firebase Performance Monitoring, you might
want to configure your app so that you can enable and disable Performance Monitoring. You
might also find this capability to be useful during app development and testing.

The following are some options to consider:

- You can disable the Performance Monitoring SDK when building your app, with the option to
  re-enable it at runtime.

- You can build your app with the Performance Monitoring SDK enabled but have the option to
  disable it at runtime using Firebase Remote Config.

- You can completely deactivate the Performance Monitoring SDK, with no option to enable it
  at runtime.

## Disable Performance Monitoring during your app build process

One situation where disabling Performance Monitoring during your app build process could be
useful is to avoid reporting performance data from a pre-release version of your
app during app development and testing.

To disable or deactivate Performance Monitoring, you can add one of two keys to the
property list file (`Info.plist`) for your Apple app:

- To disable Performance Monitoring, but allow your app to enable it at runtime, set
  `firebase_performance_collection_enabled` to `false` in your app's
  `Info.plist` file.

- To completely deactivate Performance Monitoring, with no option to enable it at runtime,
  set `firebase_performance_collection_deactivated` to `true` in your app's
  `Info.plist` file.

  > [!NOTE]
  > **Note:** This setting overrides the `firebase_performance_collection_enabled` setting and must be removed from your app's `Info.plist` file to re-enable Performance Monitoring.

## Disable your app at runtime using Remote Config

Firebase Remote Config lets you make changes to the behavior and appearance
of your app, so it provides an ideal way to let you disable Performance Monitoring in
deployed instances of your app.

To disable Performance Monitoring data collection the next time that your Apple app starts,
use the example code shown below. For more information about using
Remote Config in an Apple app, see
[Use Firebase Remote Config on Apple platforms](https://firebase.google.com/docs/remote-config/get-started?platform=ios).

1. Ensure that Remote Config is used in your `Podfile`:

       pod 'Firebase/RemoteConfig'

2. Add the following to the top of your app's `AppDelegate` file:

   ### Swift


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       import FirebaseRemoteConfig

   ### Objective-C


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       @import FirebaseRemoteConfig;

3. In your `AppDelegate` file, add the following code to the `launchOptions`
   statements in the `application:didFinishLaunchingWithOptions:` instance
   method:

   ### Swift


   **Note:** This product is not available on macOS, Mac Catalyst, watchOS targets.

       remoteConfig = RemoteConfig.remoteConfig()
       // You can change the "false" below to "true" to permit more fetches when validating
       // your app, but you should change it back to "false" or remove this statement before
       // distributing your app in production.
       let remoteConfigSettings = RemoteConfigSettings(developerModeEnabled: false)
       remoteConfig.configSettings = remoteConfigSettings!
       // Load in-app defaults from a plist file that sets perf_disable to false until
       // you update values in the Firebase console.
       remoteConfig.setDefaultsFromPlistFileName("RemoteConfigDefaults")
       // Important! This needs to be applied before FirebaseApp.configure()
       if !remoteConfig["perf_disable"].boolValue {
           // The following line disables all automatic (out-of-the-box) monitoring
           Performance.sharedInstance().isInstrumentationEnabled = false
           // The following line disables all custom monitoring
           Performance.sharedInstance().isDataCollectionEnabled = false
       }
       else {
           Performance.sharedInstance().isInstrumentationEnabled = true
           Performance.sharedInstance().isDataCollectionEnabled = true
       }
       // Use Firebase library to configure APIs
       FirebaseApp.configure()

   ### Objective-C


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       self.remoteConfig = [FIRRemoteConfig remoteConfig];
       // You can change the NO below to YES to permit more fetches when validating
       // your app, but you should change it back to NO or remove this statement before
       // distributing your app in production.
       FIRRemoteConfigSettings *remoteConfigSettings =
           [[FIRRemoteConfigSettings alloc] initWithDeveloperModeEnabled:NO];
       self.remoteConfig.configSettings = remoteConfigSettings;
       // Load in-app defaults from a plist file that sets perf_disable to false until
       // you update values in the Firebase console.
       [self.remoteConfig setDefaultsFromPlistFileName:@"RemoteConfigDefaults"];
       // Important! This needs to be applied before [FIRApp configure]
       if (!self.remoteConfig[@"perf_disable"].numberValue.boolValue) {
           // The following line disables all automatic (out-of-the-box) monitoring
           [FIRPerformance sharedInstance].instrumentationEnabled = NO;
           // The following line disables all custom monitoring
           [FIRPerformance sharedInstance].dataCollectionEnabled = NO;
       }
       else {
           [FIRPerformance sharedInstance].instrumentationEnabled = YES;
           [FIRPerformance sharedInstance].dataCollectionEnabled = YES;
       }
       // Use Firebase library to configure APIs
       [FIRApp configure];

4. In `ViewController.m`, or another implementation file used by your app, add
   the following code to fetch and activate Remote Config values:

   ### Swift


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       //RemoteConfig fetch and activation in your app, shortly after startup
       remoteConfig.fetch(withExpirationDuration: TimeInterval(30.0)) { (status, error) -> Void in
         if status == .success {
           print("Config fetched!")
           self.remoteConfig.activateFetched()
         } else {
           print("Config not fetched")
           print("Error \(error!.localizedDescription)")
         }
       }

   ### Objective-C


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       //RemoteConfig fetch and activation in your app, shortly after startup
       [self.remoteConfig fetchWithExpirationDuration:30.0 completionHandler:^(FIRRemoteConfigFetchStatus status, NSError *error) {
         if (status == FIRRemoteConfigFetchStatusSuccess) {
           NSLog(@"Config fetched!");
           [self.remoteConfig activateFetched];
         } else {
           NSLog(@"Config not fetched");
           NSLog(@"Error %@", error.localizedDescription);
         }
       }];

5. To disable Performance Monitoring in the Firebase console, create a **perf_disable**
   parameter in your app's project, then set its value to `true`.

   If you set the value of **perf_disable** to `false`, Performance Monitoring remains
   enabled.

### Disable automatic or custom data collection separately

You can make some changes to the code shown above and in the Firebase console
to let you disable all automatic (out-of-the-box) monitoring separately from
custom monitoring.

1. Add the following code to the `launchOptions` statements in the
   `application:didFinishLaunchingWithOptions:` instance method (instead of
   what's shown above for the same instance method):

   ### Swift


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       remoteConfig = FIRRemoteConfig.remoteConfig()
       let remoteConfigSettings = FIRRemoteConfigSettings(developerModeEnabled: true)
       remoteConfig.configSettings = remoteConfigSettings!
       // Important! This needs to be applied before FirebaseApp.configure()
       if remoteConfig["perf_disable_auto"].boolValue {
           // The following line disables all automatic (out-of-the-box) monitoring
           Performance.sharedInstance().isInstrumentationEnabled = false
       }
       else {
           Performance.sharedInstance().isInstrumentationEnabled = true
       }
       if remoteConfig["perf_disable_manual"].boolValue {
           // The following line disables all custom monitoring
           Performance.sharedInstance().isDataCollectionEnabled = false
       }
       else {
           Performance.sharedInstance().isDataCollectionEnabled = true
       }
       // Use Firebase library to configure APIs
       FirebaseApp.configure()

   ### Objective-C


   **Note:** This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.

       self.remoteConfig = [FIRRemoteConfig remoteConfig];
       FIRRemoteConfigSettings *remoteConfigSettings =
           [[FIRRemoteConfigSettings alloc] initWithDeveloperModeEnabled:YES];
       self.remoteConfig.configSettings = remoteConfigSettings;
       // Important! This needs to be applied before [FirebaseApp configure]
       if (self.remoteConfig[@"perf_disable_auto"].numberValue.boolValue) {
           // The following line disables all automatic (out-of-the-box) monitoring
           [FIRPerformance sharedInstance].instrumentationEnabled = NO;
       }
       else {
           [FIRPerformance sharedInstance].instrumentationEnabled = YES;
       }
       if (self.remoteConfig[@"perf_disable_manual"].numberValue.boolValue) {
           // The following line disables all custom monitoring
           [FIRPerformance sharedInstance].dataCollectionEnabled = NO;
       }
       else {
           [FIRPerformance sharedInstance].dataCollectionEnabled = YES;
       }
       // Use Firebase library to configure APIs
       [FirebaseApp configure];

2. Complete the following in the Firebase console:

   - To disable all automatic (out-of-the-box) monitoring, create a **perf_disable_auto** parameter in your app's project, then set its value to `true`.
   - To disable all custom monitoring, create a **perf_disable_manual** parameter in your app's project, then set its value to `true`.

   > [!NOTE]
   > **Note:** To enable either of these aspects of Performance Monitoring in your app, set the value of the corresponding parameter to `false` in the Firebase console.