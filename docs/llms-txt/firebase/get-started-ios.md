# Source: https://firebase.google.com/docs/perf-mon/get-started-ios.md.txt

<br />

## Before you begin

If you haven't already,[add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).
| **Note:** Firebase supports both CocoaPods and Swift Package Manager. If you choose to install Firebase using[Swift Package Manager](https://firebase.google.com/docs/ios/swift-package-manager), you can skip CocoaPods-related steps, like modifying Podfiles and running the`pod`command.

## **Step 1** : AddPerformance Monitoringto your app

After you've added thePerformance MonitoringSDK, Firebase automatically starts collecting data for your app's[screen rendering](https://firebase.google.com/docs/perf-mon/screen-traces), data related to your app's lifecycle (like[app start time](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces)), and data for[HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces?platform=ios).

Use Swift Package Manager to install and manage Firebase dependencies.
| Visit[our installation guide](https://firebase.google.com/docs/ios/installation-methods)to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.

1. In Xcode, with your app project open, navigate to**File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:  

```text
  https://github.com/firebase/firebase-ios-sdk.git
```
| **Note:**New projects should use the default (latest) SDK version, but you can choose an older version if needed.
3. Choose thePerformance Monitoringlibrary.
4. Add the`-ObjC`flag to the*Other Linker Flags*section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

Next, configure the Firebase module:

1. Import the`FirebaseCore`module in your`UIApplicationDelegate`, as well as any other[Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods)your app delegate uses. For example, to useCloud FirestoreandAuthentication:  

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
2. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:  

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
3. If you're using SwiftUI, you must create an application delegate and attach it to your`App`struct via`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).  

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
4. Recompile your app.

| **Note:** When you addPerformance Monitoringto your app, theRemote ConfigSDK is included as a dependency. If you already useRemote Config, you won't see any difference. However, if you're new toRemote Config, explore the[Remote Configdocumentation](https://firebase.google.com/docs/remote-config/ios)to learn more about the various features you'll be able to access in your app.

## **Step 2**: Generate performance events for initial data display

Firebase starts processing the events when you successfully add the SDK to your app. If you're still developing locally, interact with your app to generate events for initial data collection and processing.
| **Note:** ThePerformance MonitoringSDK batches events locally then sends them to Firebase periodically (every 30 seconds) or when the app comes back to foreground. So, there's a delay between an app interaction and when Firebase receives the event information from your app.

1. Continue to develop your app using a simulator or test device.

2. Generate events by switching your app between background and foreground several times, interacting with your app by navigating across screens, and/or triggering network requests.

3. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole. You should see your initial data display within a few minutes.

   If you don't see a display of your initial data, review the[troubleshooting tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios#sdk-detected-no-data).

## **Step 3** :*(Optional)*View log messages for performance events

1. Enable debug logging, as follows:

   1. In Xcode (minimum v16.2), select**Product** \>**Scheme** \>**Edit scheme**.
   2. Select**Run** from the left menu, then select the**Arguments**tab.
   3. In the*Arguments Passed on Launch* section, add`-FIRDebugEnabled`.
2. Check your log messages for any error messages.

3. Performance Monitoringtags its log messages with`Firebase/Performance`so that you can filter your log messages.

4. Check for the following types of logs which indicate thatPerformance Monitoringis logging performance events:

   - `Logging trace metric: `<var translate="no">TRACE_NAME</var>`, `<var translate="no">FIREBASE_PERFORMANCE_CONSOLE_URL</var>
   - `Logging network request trace: `<var translate="no">URL</var>
5. Click on the URL to view your data in the Firebase console. It may take a few moments for the data to update in the dashboard.

If your app isn't logging performance events, review the[troubleshooting tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios#app-not-logging-events).

## **Step 4** :*(Optional)*Add custom monitoring for specific code

To monitor performance data associated with specific code in your app, you can instrument[**custom code traces**](https://firebase.google.com/docs/perf-mon/custom-code-traces).

With a custom code trace, you can measure how long it takes your app to complete a specific task or set of tasks, such as loading a set of images or querying your database. The default metric for a custom code trace is its duration, but you can also add custom metrics, such as cache hits and memory warnings.

In your code, you define the beginning and the end of a custom code trace (and add any desired custom metrics) using the API provided by thePerformance MonitoringSDK.

Visit[Add monitoring for specific code](https://firebase.google.com/docs/perf-mon/custom-code-traces)to learn more about these features and how to add them to your app.

## **Step 5**: Deploy your app then review results

After you've validatedPerformance Monitoringusing the Xcode simulator and one or more test devices, you can deploy the updated version of your app to your users.

You can monitor performance data in the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole.

## Known issues

- Performance Monitoringhas known compatibility issues with GTMSQLite. We recommend not usingPerformance Monitoringwith apps that use GTMSQLite.
- Method swizzling after calling`FirebaseApp.configure()`might interfere with thePerformance MonitoringSDK.
- Known issues with the iOS 8.0-8.2 Simulator preventPerformance Monitoringfrom capturing performance events. These issues are fixed in the iOS 8.3 Simulator and later versions.
- Connections established using NSURLSession's`backgroundSessionConfiguration`will exhibit longer than expected connection times. These connections are executed out-of-process and the timings reflect in-process callback events.

## Next steps

- Review and run the[Performance MonitoringiOS code sample on GitHub](https://github.com/firebase/quickstart-ios/tree/master/performance).

- Learn more about data automatically collected byPerformance Monitoring:

  - Data related to your app's lifecycle, like[app start time](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces?platform=ios)
  - Data for[screen rendering](https://firebase.google.com/docs/perf-mon/screen-traces?platform=ios)in your app
  - Data for[HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces?platform=ios)issued by your app
- [View, track, and filter](https://firebase.google.com/docs/perf-mon/console?platform=ios)your performance data in theFirebaseconsole.

- Add monitoring for specific tasks or workflows in your app by[instrumenting custom code traces](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=ios).

- [Use attributes to filter performance data](https://firebase.google.com/docs/perf-mon/attributes?platform=ios).