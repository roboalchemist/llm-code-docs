# Source: https://firebase.google.com/docs/app-distribution/set-up-alerts.md.txt

<br />

iOS+Android  

<br />

| TheFirebase App DistributioniOS and Android SDKs are**beta releases**. This means that the functionality might change in backward-incompatible ways. A beta release is not subject to any SLA or deprecation policy and may receive limited or no support.

The optionalFirebase App DistributioniOS and Android SDKs let you display in-app alerts to your testers when new builds of your app are available to install. This guide explains how to use theApp DistributioniOS and Android SDKs to create and customize new build alerts for your testers.

## Before you begin

If you haven't already,[add Firebase to your iOS project](https://firebase.google.com/docs/ios/setup).
| **Note:** If you have multiple apps in your Firebase project, make sure the app you want to distribute withApp Distributionhas its own`GoogleServices-info.plist`config file. For more information, see[Support multiple environments](https://firebase.google.com/docs/projects/multiprojects#support_multiple_environments_in_your_ios_application).

## **Step 1** : Enable theApp DistributionTester API

1. Select your project in the[Google Cloudconsole](https://console.cloud.google.com/apis/library/firebaseapptesters.googleapis.com).

2. Under**Firebase App Testers API** , click**Enable**.

## **Step 2** : AddApp Distributionto your app

| **Note:** Firebase supports both CocoaPods and Swift Package Manager. If you choose to install Firebase using[Swift Package Manager](https://firebase.google.com/docs/ios/swift-package-manager), you can skip CocoaPods-related steps, like modifying Podfiles and running the`pod`command.

1. Open the Podfile you created for the project (or run`pod init`to create one), then add the following line inside the target section:

   ```
   pod 'FirebaseAppDistribution'
   ```
2. In the directory of your podfile, run`pod install`, then open the created`.xcworkspace`file.

3. Import the Firebase module in your`App`struct or`UIApplicationDelegate`:

   ### Swift

       import FirebaseCore
       import FirebaseAppDistribution

   ### Objective-C

       @import FirebaseCore;
       @import FirebaseAppDistribution;

4. Configure a`FirebaseApp`shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:

   ### Swift

       // Use Firebase library to configure APIs
       FirebaseApp.configure()

   ### Objective-C

       // Use Firebase library to configure APIs
       [FIRApp configure];

5. If swizzling is disabled, pass any opened URLs to theApp DistributionSDK in your implementation of`application(_:open:options:)`:

   ### Swift

       func application(_ app: UIApplication, 
                        open url: URL,
                        options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
          if AppDistribution.appDistribution().application(application, open: url, options: options) {
             return true
          }

          // Handle other non-Firebase URLs here.

          return false
       }

   ### Objective-C

       - (BOOL)application:(UIApplication *)app 
                   openURL:(NSURL *)url 
                   options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
          if ([[FIRAppDistribution appDistribution] application:app openURL:url options:options]) {
             return YES;
          }

          // Handle other non-Firebase URLs here.

          return NO;
       }

6. Finally, recompile your app.

## **Step 3**: Configure in-app alerts

TheApp DistributionSDK provides two ways of setting up in-app build alerts for your testers: a basic alert configuration, which comes with pre-built app update and sign-in dialogues to display to testers, and an advanced alert configuration, which allows you to customize your own user interface. We recommend first using the basic alert configuration if you're new to theApp DistributionSDK.

### **Basic configuration**

Use`checkForUpdate`to display a pre-built enable alerts dialogue to testers who haven't yet enabled alerts, and then check if a new build is available. When called, the method enacts the following sequence:

1. Checks if a tester has enabled alerts by prompting them to sign intoApp Distributionwith their Google account.

2. If the tester has not yet enabled alerts, displays a pre-built dialogue.

   Enabling alerts is a one-time process on the test device and persists across updates of your app. Alerts remain enabled on the test device until either the app is uninstalled, or until the`signOutTester`method is called. See the method's reference documentation ([Swift](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes)or[Objective-C](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes)) for more information.
3. Checks for newly available builds for the tester to install.

You can invoke`checkForUpdate()`at any point in your app. For example, you can prompt your testers to install newly available builds at startup by including`checkForUpdate()`in the`onAppear(perform:)`of your app's root view.

The following example checks whether or not the tester has enabled alerts and has access to a new build, and if so, displays a dialogue when the build is available to install:  

### Swift

<br />

**Note:**This product is not available on macOS, Mac Catalyst, tvOS or watchOS targets.  

    AppDistribution.appDistribution().checkForUpdate(completion: { release, error in
      if error != nil {
          // Handle error
          return
      }

      guard let release = release else {
        return
      }

      // Customize your alerts here.
      let title = "New Version Available"
      let message = "Version \(release.displayVersion)(\(release.buildVersion)) is available."
      let uialert = UIAlertController(title: title,message: message, preferredStyle: .alert)

      uialert.addAction(UIAlertAction(title: "Update", style: UIAlertAction.Style.default) {
        _ in
        UIApplication.shared.open(release.downloadURL)
      })
      uialert.addAction(UIAlertAction(title: "Cancel", style: UIAlertAction.Style.cancel) {
        _ in
      })

      // self should be a UIViewController.
      self.present(uialert, animated: true, completion: nil)
    })

### Objective-C

<br />

**Note:**This product is not available on macOS, Mac Catalyst, tvOS or watchOS targets.  

    [[FIRAppDistribution appDistribution]
      checkForUpdateWithCompletion:^(FIRAppDistributionRelease *_Nullable release,
                                     NSError *_Nullable error) {
      if (error) {
        // Handle error
        return;
      }

      if (release) {
        UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"New Version Available"
    message:[NSString stringWithFormat:@"Version %@ (%@) is available.", release.displayVersion,
    release.buildVersion] preferredStyle:UIAlertControllerStyleAlert];

        UIAlertAction *updateAction = [UIAlertAction actionWithTitle:@"Update"
    style:UIAlertActionStyleDefault handler:^(UIAlertAction *action) {
          [[UIApplication sharedApplication] openURL:release.downloadURL options:@{}
    completionHandler:nil];
        }];
        UIAlertAction *cancelAction = [UIAlertAction actionWithTitle:@"Cancel"
    style:UIAlertActionStyleCancel handler:^(UIAlertAction *action) {}];
        [alert addAction:updateAction];
        [alert addAction:cancelAction];
        [self presentViewController:alert animated:YES completion:nil];
      }
    }];

### **Advanced configuration**

The methods`signInTester()`and`isTesterSignedIn`give you more flexibility customizing your tester's sign-in experience, so it can better match your app's look and feel.

The following example checks whether the tester has already signed into theirFirebase App Distributiontester account, so you can choose to display your sign-in UI only for testers who haven't yet signed in. After the tester has signed in, you can then call`checkForUpdate()`to check whether the tester has access to a new build.  

### Swift

<br />

**Note:**This product is not available on macOS, Mac Catalyst, tvOS or watchOS targets.  

    // Sign in a tester without automatically checking for update
    if (!AppDistribution.appDistribution().isTesterSignedIn) {
      AppDistribution.appDistribution().signInTester (completion: { error in
        // completion block for signInTester
         if (error != nil) {
           // handle failed sign in
          return
         }
        // handle successful sign in
      })
    }

    // Only check for update if tester is already signed in - do not prompt
    if (AppDistribution.appDistribution().isTesterSignedIn) {
      AppDistribution.appDistribution().checkForUpdate(completion: { release, error in
          // completion block for check for update
      })
    }

### Objective-C

<br />

**Note:**This product is not available on macOS, Mac Catalyst, tvOS or watchOS targets.  

    // Sign in a tester without automatically checking for update
    if(![[FIRAppDistribution appDistribution] isTesterSignedIn]) {
      [[FIRAppDistribution appDistribution]
        signInTesterWithCompletion:^(NSError *_Nullable error) {
          // completion block for signInTester
         if (error) {
           // handle failed sign in
           return;
         }
          // handle successful sign in
      }];
    }

    // only check for update if tester is already signed in - do not prompt
    if([[FIRAppDistribution appDistribution] isTesterSignedIn]) {
      [[FIRAppDistribution appDistribution]
            checkForUpdateWithCompletion:^(FIRAppDistributionRelease *_Nullable release,
                                           NSError *_Nullable error) {
         // completion block for check for update
      }];
    }

For information on additional methods, including`signOutTester()`, see theApp Distributionreference documentation for[Swift](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes)and[Objective-C](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes).

## **Step 4**: Build and test your implementation

Finally, build your app and test your implementation by[distributing the build](https://firebase.google.com/docs/app-distribution/ios/distribute-console)to testers using theFirebaseconsole.
| **Note:** In-app alerts cannot be tested on a simulator. To test your implementation, use a real test device and make sure it's enabled to install builds fromApp Distribution(for instructions on setting up your test device, see[Set up for testing](https://firebase.google.com/docs/app-distribution/ios/set-up-for-testing)).

Visit the[App DistributionTroubleshooting guide](https://firebase.google.com/docs/app-distribution/troubleshooting?platform=ios#enable-alerts)for help with common issues, such as:

- Tester not receiving in-app alerts
- Tester being prompted to sign in to Google more than once