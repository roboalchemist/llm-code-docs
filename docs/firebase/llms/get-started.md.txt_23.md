# Source: https://firebase.google.com/docs/crashlytics/ios/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-started) [Android](https://firebase.google.com/docs/crashlytics/android/get-started) [Android NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-started) [Unity](https://firebase.google.com/docs/crashlytics/unity/get-started) |

<br />

This guide describes how to get started with Firebase Crashlytics in
your Apple platforms app (for example, an iOS app).

After you've set up the Firebase Crashlytics SDK in your app, you can
get comprehensive crash reports in the Firebase console. With Crashlytics
for Apple platforms, you get reports for crashes and non-fatal errors.

Setting up Crashlytics requires tasks both in the Firebase console and
your IDE (like adding a Firebase configuration file and the Crashlytics
SDK). To finish setup, you'll need to force a test crash to send your first
crash report to Firebase.

## Before you begin

1. If you haven't already, [add Firebase](https://firebase.google.com/docs/ios/setup) to your Apple
   project. If you don't have an Apple app, you can download a
   [sample app](https://firebase.google.com/docs/samples).

2. **Recommended** : To automatically get
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#get-breadcrumb-logs)
   to understand user actions leading up to a crash or non-fatal event
   you need to enable Google Analytics in your Firebase project.

   - If your existing Firebase project doesn't have Google Analytics
     enabled, you can enable Google Analytics from the
     [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations/analytics) of your
     \> *Project settings*
     in the Firebase console.

   - If you're creating a new Firebase project, enable Google Analytics
     during the project creation workflow.

   Note that breadcrumb logs are available for all Apple platforms supported by
   Crashlytics except watchOS.

## **Step 1** : Add the Crashlytics SDK to your app

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

3. Choose the Crashlytics library.
4. To take advantage of [breadcrumb logs](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#get-breadcrumb-logs), also add the Firebase SDK for Google Analytics to your app. Make sure that [Google Analytics is enabled](https://support.google.com/firebase/answer/9289399#linkga) in your Firebase project.
5. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
6. *(macOS only)* In your `Info.plist`, add the key `NSApplicationCrashOnExceptions` and set it to `YES`.
7. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

Next, configure the Firebase module:

1. Import the Firebase module in your `App` struct or `UIApplicationDelegate`:

   ### Swift

   ```swift
   import Firebase
   ```

   ### Objective-C

   ```objective-c
   @import Firebase;
   ```
2. Configure a `FirebaseApp` shared instance, typically in your app delegate's
   `application(_:didFinishLaunchingWithOptions:)` method:

   ### Swift

   ```swift
   // Use the Firebase library to configure APIs.
   FirebaseApp.configure()
   ```

   ### Objective-C

   ```objective-c
   // Use the Firebase library to configure APIs.
   [FIRApp configure];
   ```

## **Step 2**: Set up Xcode to automatically upload dSYM files

To generate human readable crash reports, Crashlytics needs your project's
debug symbol (dSYM) files. The following steps describe how to configure Xcode
to automatically produce your dSYMs, process them, and upload the files whenever
you build your app.

1. Open your project's Xcode workspace, then select its project file in the
   left navigator.

2. From the **TARGETS** list, select your main build target.

3. Click the **Build Settings** tab, then complete the following steps so that
   Xcode produces dSYMs for your builds.

   1. Click **All** , then search for `debug information format`.

   2. Set **Debug Information Format** to `DWARF with dSYM File` for all your
      build types.

4. Click the **Build Phases** tab, then complete the following steps so that
   Xcode can process your dSYMs and upload the files.

   1. Click \>
      **New Run Script Phase**.

      Make sure this new *Run Script* phase is your project's last build
      phase; otherwise, Crashlytics can't properly process dSYMs.
   2. Expand the new *Run Script* section.

      > [!NOTE]
      > **Note:** For the remaining substeps, copy-and-paste the paths exactly as specified, and Xcode will resolve them. However, if you have issues with Xcode resolving these paths or a unique project structure, you can manually specify the paths instead.

   3. In the script field (located under the *Shell* label), add the
      following run script.

      This script processes your project's dSYM files and uploads the files to
      Crashlytics.

      ```
      "${BUILD_DIR%/Build/*}/SourcePackages/checkouts/firebase-ios-sdk/Crashlytics/run"
      ```
   4. In the *Input Files* section, add the paths for the locations of the
      following files:

      ```
      ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}
      ```

      ```
      ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}/Contents/Resources/DWARF/${PRODUCT_NAME}
      ```

      ```
      ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}/Contents/Info.plist
      ```

      ```
      $(TARGET_BUILD_DIR)/$(UNLOCALIZED_RESOURCES_FOLDER_PATH)/GoogleService-Info.plist
      ```

      ```
      $(TARGET_BUILD_DIR)/$(EXECUTABLE_PATH)
      ```
      If you have `ENABLE_USER_SCRIPT_SANDBOXING=YES` and `ENABLE_DEBUG_DYLIB=YES` in your project build settings, then include the following:

      ```
      ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}/Contents/Resources/DWARF/${PRODUCT_NAME}.debug.dylib
      ```
      **Understand why the locations of these files are
      needed**

      Xcode looks in the specified locations for these input files to ensure
      that the build files are available for the run script. Also, if
      *User Script Sandboxing* is enabled, Xcode only allows the run
      script to access files specified in the *Input Files*.
      - Providing the location of your project's dSYM files enables Crashlytics to process dSYMs.
      - Providing the location of your app's built `GoogleService-Info.plist` file enables Crashlytics to associate the dSYMs with your Firebase app.
      - Providing the location of your app's executable allows the run script to prevent duplicate uploads of the same dSYM. Note that app binaries are *not uploaded*.

For more detailed information about dSYM files and Crashlytics (including
how to manually upload dSYM files), visit
[Get deobfuscated crash reports](https://firebase.google.com/docs/crashlytics/ios/get-deobfuscated-reports).

## **Step 3**: Force a test crash to finish setup

To finish setting up Crashlytics and see initial data in the
Crashlytics dashboard of the Firebase console, you need to force a test
crash.

1. Add code to your app that you can use to force a test crash.

   You can use the following code to add a button to your app that, when
   pressed, causes a crash. The button is labeled "Test Crash".

   <br />

   ### SwiftUI

   ```swift
   Button("Crash") {
     fatalError("Crash was triggered")
   }
   ```

   ### UIKit

   ### Swift

   ```
   import UIKit

   class ViewController: UIViewController {
     override func viewDidLoad() {
         super.viewDidLoad()

         // Do any additional setup after loading the view, typically from a nib.

         let button = UIButton(type: .roundedRect)
         button.frame = CGRect(x: 20, y: 50, width: 100, height: 30)
         button.setTitle("Test Crash", for: [])
         button.addTarget(self, action: #selector(self.crashButtonTapped(_:)), for: .touchUpInside)
         view.addSubview(button)
     }

     @IBAction func crashButtonTapped(_ sender: AnyObject) {
         let numbers = [0]
         let _ = numbers[1]
     }
   }
   ```

   ### Objective-C

   ```objective-c
   #import "ViewController.h"

   @implementation ViewController
   ‐ (void)viewDidLoad {
       [super viewDidLoad];

       // Do any additional setup after loading the view, typically from a nib.

       UIButton* button = [UIButton buttonWithType:UIButtonTypeRoundedRect];
       button.frame = CGRectMake(20, 50, 100, 30);
       [button setTitle:@"Test Crash" forState:UIControlStateNormal];
       [button addTarget:self action:@selector(crashButtonTapped:)
           forControlEvents:UIControlEventTouchUpInside];
       [self.view addSubview:button];
   }

   ‐ (IBAction)crashButtonTapped:(id)sender {
       @[][1];
   }

   @end
   ```
2. Build and run your app in Xcode with the Xcode debugger disconnected.

   > [!CAUTION]
   > **The Xcode debugger prevents crash reports
   > from being sent to Crashlytics.** Complete the following steps to disconnect your test device or simulator from the Xcode debugger ***before*** forcing a crash.

   1. Click **Build and then
      run the current scheme** to build your app on a test device or
      simulator.

   2. Wait until your app is running, then click
      **Stop running the scheme or
      action** to close the initial instance of your app. This initial
      instance included the debugger that interferes with Crashlytics.

3. Force the test crash in order to send your app's first crash report:

   1. Open your app from the home screen of your test device or simulator.

   2. In your app, press the "Test Crash" button that you added using the code
      above.

   3. After your app crashes, run it again from Xcode so that your app can
      send the crash report to Firebase.

4. Go to the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
   Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes,
   [enable debug logging](https://firebase.google.com/docs/crashlytics/ios/test-implementation#enable-debug-logging)
   to see if your app is sending crash reports.

<br />

And that's it! Crashlytics is now monitoring your app for crashes.
Visit the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) to view and investigate
all your reports and statistics.

## Next steps

-
  [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports)
  by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.

-
  [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud)
  for advanced analysis and features, like
  querying your data, building custom dashboards, and setting up custom alerts.