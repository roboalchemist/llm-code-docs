# Source: https://firebase.google.com/docs/remote-config/ios/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/remote-config/ios/get-started) [Android](https://firebase.google.com/docs/remote-config/android/get-started) [Web](https://firebase.google.com/docs/remote-config/web/get-started) [Flutter](https://firebase.google.com/docs/remote-config/flutter/get-started) [Unity](https://firebase.google.com/docs/remote-config/unity/get-started) [C++](https://firebase.google.com/docs/remote-config/cpp/get-started) |

<br />

[Video](https://www.youtube.com/watch?v=8K9stpPhTYI)

You can use Firebase Remote Config to define parameters in your app and
update their values in the cloud, allowing you to modify the appearance and
behavior of your app without distributing an app update. This guide walks you
through the steps to get started and provides some sample code, all of which is
available to clone or download from the
[firebase/quickstart-ios](https://github.com/firebase/quickstart-ios/tree/master)
GitHub repository.

## Step 1: Add Remote Config to your app

1. If you haven't already, [add Firebase to your Apple
   project](https://firebase.google.com/docs/ios/setup).

2. For Remote Config, Google Analytics is required for the
   [conditional targeting of app instances](https://firebase.google.com/docs/remote-config/parameters#conditions_rules_and_conditional_values)
   to user properties and audiences. Make sure that you [enable
   Google Analytics](https://firebase.google.com/docs/analytics/get-started?platform=ios) in your
   project.

3. Create the singleton Remote Config object, as shown in the following
   example:

   ### Swift

   ```swift
   let remoteConfig = RemoteConfig.remoteConfig()
   let settings = RemoteConfigSettings()
   settings.minimumFetchInterval = 0
   RemoteConfig.remoteConfig().configSettings = settingshttps://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/MigratedSnippets.swift#L240-L242
   ```

   ### Objective-C

   ```objective-c
   FIRRemoteConfig *remoteConfig = [FIRRemoteConfig remoteConfig];
   FIRRemoteConfigSettings *remoteConfigSettings = [[FIRRemoteConfigSettings alloc] init];
   remoteConfigSettings.minimumFetchInterval = 0;
   remoteConfig.configSettings = remoteConfigSettings;
   ```

This object is used to store in-app default parameter values, fetch updated
parameter values from the Remote Config backend, and control when fetched
values are made available to your app.

During development, it's recommended to set a relatively low minimum fetch
interval. See
[Throttling](https://firebase.google.com/docs/remote-config/ios/get-started#throttling) for more
information.

## Step 2: Set in-app default parameter values

You can set in-app default parameter values in the Remote Config
object, so that your app behaves as intended before it connects to the
Remote Config backend, and so that default values are available if none are
set in the backend.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or values. Remote Config data is encrypted in transit, but end users can access any default or fetched Remote Config parameter that is available to their client app instance.

1. Define a set of parameter names, and default parameter values using an
   [`NSDictionary`](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSDictionary_Class/)
   object or a [plist
   file](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html).

   If you have already configured Remote Config backend parameter values,
   you can download a generated `plist` file that includes all default values
   and save it to your Xcode project.

   ### REST

   ```
   curl --compressed -D headers -H "Authorization: Bearer token -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig:downloadDefaults?format=PLIST -o RemoteConfigDefaults.plist
   ```

   You can generate a bearer token by running the following command using the
   [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) or [Cloud
   Shell](https://cloud.google.com/shell/docs/run-gcloud-commands):

       gcloud auth print-access-token

   This token is short-lived, so you may need to regenerate it if you get an
   authentication error.

   ### Firebase console

   1. In the [Parameters](https://console.firebase.google.com/project/_/config)
      tab, open the **Menu** ,
      and select **Download default values**.

   2. When prompted, enable **.plist for iOS** , then click **Download file**.

2. Add these values to the Remote Config object using
   [`setDefaults:`](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/interface_f_i_r_remote_config#a5a2fd04d83373458be28b53134468626).
   The following example sets in-app default values from a plist file:

   ### Swift

   ```swift
   RemoteConfig.remoteConfig().setDefaults(fromPlist: "RemoteConfigDefaults")
   ```

   ### Objective-C

   ```objective-c
   [remoteConfig setDefaultsFromPlistFileName:@"RemoteConfigDefaults"];
   ```

> [!NOTE]
> **Note:** These code snippets refer to the file `RemoteConfigDefaults.plist` from the sample [`quickstart-ios`](https://github.com/firebase/quickstart-ios/tree/master/config) project. If you use the downloaded defaults file, use `remote_config_defaults`.

## Step 3: Get parameter values to use in your app

Now you can get parameter values from the Remote Config object. If you later
set values in the Remote Config backend, fetch them, and then activate them,
those values are available to your app. Otherwise, you get the in-app parameter
values configured using
[`setDefaults:`](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/interface_f_i_r_remote_config#a5a2fd04d83373458be28b53134468626).
To get these values, call the
[`configValueForKey:`](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/interface_f_i_r_remote_config#a3219d5ac3411efb16b429019fa05be29)
method, providing the parameter key as an argument.

    let remoteConfig = RemoteConfig.remoteConfig()

    // Retrieve a parameter value using configValueForKey
    let welcomeMessageValue = remoteConfig.configValue(forKey: "welcome_message")
    let welcomeMessage = welcomeMessageValue.stringValue

    let featureFlagValue = remoteConfig.configValue(forKey: "new_feature_flag")
    let isFeatureEnabled = featureFlagValue.boolValue

A more readable and convenient way to access these values in Swift is through
Swift's subscript notation:

    let remoteConfig = RemoteConfig.remoteConfig()

    // Retrieve a string parameter value
    let welcomeMessage = remoteConfig["welcome_message"].stringValue

    // Retrieve a boolean parameter value
    let isFeatureEnabled = remoteConfig["new_feature_flag"].boolValue

    // Retrieve a number parameter value
    let maxItemCount = remoteConfig["max_items"].numberValue.intValue

### Use Codable for type-safe configuration

For more complex configurations, you can use Swift's `Codable` protocol to
decode structured data from Remote Config. This provides type-safe
configuration management and simplifies working with complex objects.

    // Define a Codable struct for your configuration
    struct AppFeatureConfig: Codable {
      let isNewFeatureEnabled: Bool
      let maxUploadSize: Int
      let themeColors: [String: String]
    }

    // Fetch and decode the configuration
    func configureAppFeatures() {
      let remoteConfig = RemoteConfig.remoteConfig()
      remoteConfig.fetchAndActivate { status, error in
        guard error == nil else { return }

        do {
          let featureConfig = try remoteConfig["app_feature_config"].decoded(asType: AppFeatureConfig.self)
          configureApp(with: featureConfig)
        } catch {
          // Handle decoding errors
          print("Failed to decode configuration: \(error)")
        }
      }
    }

This method lets you:

- Define complex configuration structures.
- Automatically parse JSON configurations.
- Ensure type safety when accessing Remote Config values.
- Provide clean, readable code for handling structured Remote Config templates.

### Use Property Wrappers for declarative configuration in SwiftUI

Property wrappers are a powerful Swift feature that lets you add custom behavior
to property declarations. In SwiftUI, property wrappers are used to manage
state, bindings, and other property behaviors. For more information, see the
[Swift Language
Guide](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties/#Property-Wrappers).

    struct ContentView: View {
      @RemoteConfigProperty(key: "cardColor", fallback: "#f05138")
      var cardColor

      var body: some View {
        VStack {
          Text("Dynamic Configuration")
            .background(Color(hex: cardColor))
        }
        .onAppear {
          RemoteConfig.remoteConfig().fetchAndActivate()
        }
      }
    }

Use the `@RemoteConfigProperty` property wrapper when you want a declarative way
to access Remote Config values in SwiftUI, with built-in support for default
values and simplified configuration management.

## Step 4: Set parameter values

Using the Firebase console or the [Remote Config backend
APIs](https://firebase.google.com/docs/remote-config/automate-rc), you can create new backend default
values that override the in-app values according to your desired conditional
logic or user targeting. This section walks you through the Firebase console
steps to create these values.

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Remote Config** from the menu to view the Remote Config dashboard.
3. Define parameters with the same names as the parameters that you defined in your app. For each parameter, you can set a default value (which will eventually override the in-app default value) and you can also set conditional values. To learn more, see [Remote Config Parameters and
   Conditions](https://firebase.google.com/docs/remote-config/ios/parameters).
4. If using [custom signal
   conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom_signal_conditions),
   define the attributes and their values. The following examples show how to
   define a custom signal condition.

   ### Swift

   ```swift
       Task {
           let customSignals: [String: CustomSignalValue?] = [
           "city": .string("Tokyo"),
           "preferred_event_category": .string("sports")
         ]

         do {
           try await remoteConfig.setCustomSignals(customSignals)
           print("Custom signals set successfully!")
           } catch {
               print("Error setting custom signals: \(error)")
           }
     }
   ```

   ### Objective-C

   ```objective-c
       dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
         NSDictionary *customSignals = @{
           @"city": @"Tokyo",
           @"preferred_event_category": @"sports"
         };

         [self.remoteConfig setCustomSignals:customSignals withCompletion:^(NSError * _Nullable error) {
             if (error) {
                 NSLog(@"Error setting custom signals: %@", error);
             } else {
                 NSLog(@"Custom signals set successfully!");
             }
       }];
   });
   ```

## Step 5: Fetch and activate values

To fetch parameter values from Remote Config, call the
[`fetchWithCompletionHandler:`](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/interface_f_i_r_remote_config#ab41c9bf417ffff17fb473b6d6d92ffc0)
or [`fetchWithExpirationDuration:completionHandler:`](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/interface_f_i_r_remote_config#a14b69977b64a6cbca7e65fc5fcd06379)
method. Any values that you set on the backend are fetched and cached in the
Remote Config object.

For cases where you want to fetch and activate values in one call, use
`fetchAndActivateWithCompletionHandler:`.

This example fetches values from the Remote Config backend (not cached
values) and calls`activateWithCompletionHandler:` to make them available to the
app:

### Swift

```swift
remoteConfig.fetch { (status, error) -> Void in
  if status == .success {
    print("Config fetched!")
    remoteConfig.activate { changed, error in
      // ...
    }
  } else {
    print("Config not fetched")
    print("Error: \(error?.localizedDescription ?? "No error available.")")
  }
}
```

### Objective-C

```objective-c
[remoteConfig fetchWithCompletionHandler:^(FIRRemoteConfigFetchStatus status, NSError *error) {
  if (status == FIRRemoteConfigFetchStatusSuccess) {
    NSLog(@"Config fetched!");
    [remoteConfig activateWithCompletion:^(BOOL changed, NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Activate error: %@", error.localizedDescription);
      } else {
        dispatch_async(dispatch_get_main_queue(), ^{
          // update UI
        });
      }
    }];
  } else {
    NSLog(@"Config not fetched");
    NSLog(@"Error %@", error.localizedDescription);
  }
}];
```

Because these updated parameter values affect the behavior and appearance of
your app, you should activate the fetched values at a time that ensures a smooth
experience for your user, such as the next time that the user opens your app.
See [Remote Config loading strategies](https://firebase.google.com/docs/remote-config/loading) for more
information and examples.

## Step 6: Listen for updates in real time

After you fetch parameter values, you can use real-time Remote Config to
listen for updates from the Remote Config backend. Real-time
Remote Config signals to connected devices when updates are available and
automatically fetches the changes after you publish a new Remote Config
version.

Real-time updates are supported by the Firebase SDK for Apple platforms v10.7.0+ and higher.

> [!NOTE]
> **Important:** Real-time Remote Config also requires the
> Firebase Remote Config
> Realtime API, which should already be enabled for you. To verify, open the
> [Google Cloud console](https://console.developers.google.com/apis/api/firebaseremoteconfigrealtime.googleapis.com/overview),
> select your project, and open the **APIs and Services** page. The API
> should appear as enabled. If it's missing or not enabled, click
> **Enable APIs \& Services** , search for
> **Firebase Remote Config Realtime API**, and then enable it.

1. In your app, call `addOnConfigUpdateListener` to start listening for updates
   and automatically fetch any new or updated parameter values. The following
   example listens for updates and when `activateWithCompletionHandler` is
   called, uses the newly fetched values to display an updated welcome message.

   ### Swift

   ```swift
   remoteConfig.addOnConfigUpdateListener { configUpdate, error in
       guard let configUpdate, error == nil else {
         print("Error listening for config updates: \(error)")
       }

       print("Updated keys: \(configUpdate.updatedKeys)")

       self.remoteConfig.activate { changed, error in
         guard error == nil else { return self.displayError(error) }
         DispatchQueue.main.async {
           self.displayWelcome()
         }
       }
     }
     
   ```

   ### Objective-C

   ```objective-c
   __weak __typeof__(self) weakSelf = self;
     [self.remoteConfig addOnConfigUpdateListener:^(FIRRemoteConfigUpdate * _Nonnull configUpdate, NSError * _Nullable error) {
       if (error != nil) {
         NSLog(@"Error listening for config updates %@", error.localizedDescription);
       } else {
         NSLog(@"Updated keys: %@", configUpdate.updatedKeys);

         __typeof__(self) strongSelf = weakSelf;
         [strongSelf.remoteConfig activateWithCompletion:^(BOOL changed, NSError * _Nullable error) {
           if (error != nil) {
             NSLog(@"Activate error %@", error.localizedDescription);
           }

           dispatch_async(dispatch_get_main_queue(), ^{
             [strongSelf displayWelcome];
           });
         }];
       }
     }];
     
   ```
2. The next time you publish a new version of your Remote Config, devices
   that are running your app and listening for changes will call the completion
   handler.

## Throttling

If an app fetches too many times in a short time period, fetch calls are
throttled and the SDK returns
[`FIRRemoteConfigFetchStatusThrottled`](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchStatus#firremoteconfigfetchstatusthrottled).
Before SDK version 6.3.0, the limit was 5 fetch requests in a 60 minute window
(newer versions have more permissive limits).

> [!TIP]
> **Tip:** Starting with Apple platforms SDK v10.7.0+, you can use real-time Remote Config to automatically fetch updated parameter values from the Remote Config backend as soon as they're published, bypassing any minimum fetch interval setting. You can use real-time updates rather than fetching frequently to refresh the cache. For more information, see [Listen
> for updates in real time](https://firebase.google.com/docs/remote-config/ios//get-started#add-real-time-listener).

During app development,you might want to fetch more often to refresh the cache
very frequently (many times per hour) to let you rapidly iterate as you develop
and test your app. Real-time Remote Config updates automatically bypass the
cache when the config is updated on the server. To accommodate rapid iteration
on a project with numerous developers, you can temporarily add a
`FIRRemoteConfigSettings` property with a low minimum fetch interval
(`MinimumFetchInterval`) in your app.

The default and recommended production fetch interval for Remote Config
is 12 hours, which means that configs won't be fetched from the backend more
than once in a 12 hour window, regardless of how many fetch calls are actually
made. Specifically, the minimum fetch interval is determined in this following
order:

1. The parameter in `fetch(long)`
2. The parameter in `FIRRemoteConfigSettings.MinimumFetchInterval`
3. The default value of 12 hours

> [!CAUTION]
> Keep in mind that this setting should be used for development only, not for an app running in production. If you're just testing your app with a small 10-person development team, you are unlikely to hit the hourly service-side quota limits. But if you pushed your app out to thousands of test users with a very low minimum fetch interval, your app would probably hit this quota.