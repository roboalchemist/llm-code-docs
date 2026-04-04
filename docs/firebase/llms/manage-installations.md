# Source: https://firebase.google.com/docs/projects/manage-installations.md.txt

TheFirebaseinstallations service (FIS) provides aFirebaseinstallation ID (FID) for each installed instance of a Firebase app. TheFirebaseinstallation ID is used internally by these Firebase services:

|          Firebase service          |                                                                                                                                           Firebaseinstallations functionality                                                                                                                                           |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase Cloud Messaging           | Firebase Cloud MessagingusesFirebaseinstallation IDs to target devices for message delivery.                                                                                                                                                                                                                            |
| Firebase Crashlytics               | Firebase Crashlyticsrotates theCrashlyticsinstallation UUID based on changes to the app instance's Firebase installation ID. In the future, the installation ID may be used to enable features that enhance crash reporting and crash management services.                                                              |
| Firebase In-App Messaging          | Firebase In-App MessagingusesFirebaseinstallation IDs to target devices for message delivery.                                                                                                                                                                                                                           |
| Firebase Performance Monitoring    | Performance MonitoringusesFirebaseinstallation IDs to calculate the number of unique Firebase installations that access network resources, to ensure that access patterns are sufficiently anonymous. It also usesFirebaseinstallation IDs withFirebase Remote Configto manage the rate of performance event reporting. |
| Firebase Remote Config             | Remote ConfigusesFirebaseinstallation IDs to select configuration values to return to end-user devices.                                                                                                                                                                                                                 |
| Firebase ML                        | Credentials called[installation auth tokens](https://firebase.google.com/docs/projects/manage-installations#retrieve-fis-token)are used byFirebase MLfor device authentication when interacting with app instances, for example, to distribute developer models to app instances.                                       |
| Firebase User Segmentation Storage | Firebase User Segmentation Storage storesFirebaseinstallation IDs and related attributes and segments to provide targeting information to other Firebase services that use them.                                                                                                                                        |

| **Note:** Additional Firebase services use different types of credentials for similar purposes of identifying or targeting app instances. See[Privacy and security in Firebase](https://firebase.google.com/support/privacy#data_processing_information)for complete details.
|
| If you link your Firebase project to a Google Analytics property, then Google Analytics may useFirebaseinstallation IDs to provide analytics and attribution information. The precise information collected can vary by the device and environment.

Typically, Firebase services use theFirebaseinstallations service without requiring developers to interact directly with the FIS API. However, there are cases where app developers might want to directly call the FIS API, such as:

- To delete a Firebase installation and data tied to the installation.
- To retrieve identifiers (Firebaseinstallation IDs) in order to target specific app installations.
- To retrieve installation auth tokens to authenticate Firebase installations.

To get started with directly calling the FIS API, add the SDK to your app.

## Add theFirebaseinstallations SDK to your app

### iOS+

<br />

1. Add the dependency forFirebaseinstallations to your Podfile:  

   ```
   pod 'FirebaseInstallations'
   ```
2. Run`pod install`and open the created`.xcworkspace`file.
3. Import the`FirebaseCore`module in your`UIApplicationDelegate`, as well as any other[Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods)your app delegate uses. For example, to useCloud FirestoreandAuthentication:  

   #### SwiftUI

   ```python
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
4. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:  

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
5. If you're using SwiftUI, you must create an application delegate and attach it to your`App`struct via`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).  

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

<br />

### Android

Add the dependency for theFirebaseinstallations Android SDK to your module (app-level) Gradle file (usually`app/build.gradle`):  

    implementation 'com.google.firebase:firebase-installations:19.0.1'

### JavaScript

Depending on how your web application is hosted, your configuration may be handled automatically or you may need to update your[Firebase configuration object](https://firebase.google.com/docs/projects/learn-more#config-files-objects).

For example, if your dependencies are added in index.html, add the dependency in the \<head\> element:

<br />

```javascript
<script src="/__/firebase/12.7.0/firebase-installations.js"></script>
```

<br />

### Flutter

1. From the root directory of your Flutter project, run the following command to install theFirebaseinstallations plugin:

       flutter pub add firebase_app_installations

2. Rebuild your project:

       flutter run

3. Import theFirebaseinstallations plugin:

       import 'package:firebase_app_installations/firebase_app_installations.dart';

## Delete aFirebaseinstallation

Data tied to aFirebaseinstallation is generally*not*personally identifying. Still, it can be helpful to give users an option to manage and delete this data.

Firebaseinstallation IDs are different for every installation of every application; different applications on the same device have differentFirebaseinstallation IDs.Firebaseinstallation IDs identify app installations and data tied to those app installations.

When you delete an installation ID, the data tied to that installation ID is removed from live and backup systems of all Firebase services that useFirebaseinstallation IDs to identify installations within 180 days. This process is described at a high level in Google's[statement on deletion and retention](https://policies.google.com/technologies/retention).

Unless you disable all FID-generating services in your app, FIS creates a new ID within a few days. Firebase considers the newly-created ID to be a newFirebaseinstallation, and doesn't associate it with the previous ID or data in any way.
| **Note:** Google Analytics for Firebase uses its own form of ID to keep track of analytics data. Deleting aFirebaseinstallation ID does*not* delete Analytics data. Learn how to[delete Analytics data associated with end users](https://support.google.com/firebase/answer/9019185#delete_analytics_data).

### Delete an FID with a client API call

To delete FIDs generated by Firebase services, call the appropriate method from theFirebaseinstallations SDK:  

### Swift

```swift
do {
  try await Installations.installations().delete()
  print("Installation deleted");
} catch {
  print("Error deleting installation: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/AppDelegate.swift#L84-L89
```

### Objective-C

```objective-c
[[FIRInstallations installations] deleteWithCompletion:^(NSError *error) {
   if (error != nil) {
     NSLog(@"Error deleting Installation %@", error);
     return;
   }
   NSLog(@"Installation deleted");
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/ObjCSnippets.m#L68-L74
```

### Java

```java
FirebaseInstallations.getInstance().delete()
        .addOnCompleteListener(new OnCompleteListener<Void>() {
    @Override
    public void onComplete(@NonNull Task<Void> task) {
        if (task.isSuccessful()) {
            Log.d("Installations", "Installation deleted");
        } else {
            Log.e("Installations", "Unable to delete Installation");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/MainActivity.java#L54-L64
```

### Kotlin

```kotlin
FirebaseInstallations.getInstance().delete().addOnCompleteListener { task ->
    if (task.isComplete) {
        Log.d("Installations", "Installation deleted")
    } else {
        Log.e("Installations", "Unable to delete Installation")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/kotlin/MainActivity.kt#L45-L51
```

### JavaScript

```javascript
await firebase.installations().delete();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/installations/index.js#L7-L7
```

### Dart

    await FirebaseInstallations.instance.delete();

### Delete an FID with a server API call

To delete an FID with a server API call,[add the Firebase Admin SDK to your server](https://firebase.google.com/docs/admin/setup), if you haven't already.

Once the SDK is added, delete FIDs through a call to the deletion function in your language of choice (note: Except for Node.js, these methods reflect Instance ID naming. However, they all actually delete the FID when called with any current Firebase SDK).  

### Node.js

    // An FIDsent from a client service SDK
    const idToDelete = 'eyJhbGciOiJFUzI1N_iIs5';

    admin.installations().deleteInstallation(idToDelete);

### Java

    // An FID sent from a client service SDK
    String idToDelete = "eyJhbGciOiJFUzI1N_iIs5";

    FirebaseInstanceId.getInstance().deleteInstanceIdAsync(idToDelete).get();

### Python

      from firebase_admin import instance_id

      # An FID sent from a client service SDK
      id_to_delete = 'eyJhbGciOiJFUzI1N_iIs5'

      instance_id.delete_instance_id(id_to_delete)

### Go

    client, err := app.InstanceId(ctx)
    if err != nil {
      log.Fatalln("error initializing client", err)
    }

    iidToDelete := "eyJhbGciOiJFUzI1N_iIs5"
    if err := client.DeleteInstanceId(ctx, iidToDelete); err != nil {
      log.Fatalln("error deleting FID", err)
    }

When you delete anFirebaseinstallation ID with a server API call, Firebase services start the process to delete the data tied to that installation ID, stop accepting new data for that ID over the course of 1-2 days, and then notify the client app that the ID was deleted. Until Firebase notifies the client app, some of the app's services might still target the ID---for example, a Firebase installation might continue to receiveFCMnotifications for a few hours.

If you want to delete the currentFirebaseinstallation ID and immediately use Firebase services with a new, unrelated ID, use the client API to handle the deletion.

## Retrieve client identifiers

If you have a requirement to identify particular installations of your app, you can do so by retrieving theFirebaseinstallation ID. For example, to create segments of app installs for BiqQuery import, or to perform testing duringFirebase In-App Messagingdevelopment, you can identify and target the correct devices using the correspondingFirebaseinstallation IDs.

To retrieve aFirebaseinstallation ID:  

### Swift

```swift
do {
  let id = try await Installations.installations().installationID()
  print("Installation ID: \(id)")
} catch {
  print("Error fetching id: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/AppDelegate.swift#L61-L66
```

### Objective-C

```objective-c
[[FIRInstallations installations] installationIDWithCompletion:^(NSString *identifier, NSError *error) {
  if (error != nil) {
    NSLog(@"Error fetching Installation ID %@", error);
    return;
  }
  NSLog(@"Installation ID: %@", identifier);
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/ObjCSnippets.m#L43-L49
```

### Java

```java
FirebaseInstallations.getInstance().getId()
        .addOnCompleteListener(new OnCompleteListener<String>() {
    @Override
    public void onComplete(@NonNull Task<String> task) {
        if (task.isSuccessful()) {
            Log.d("Installations", "Installation ID: " + task.getResult());
        } else {
            Log.e("Installations", "Unable to get Installation ID");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/MainActivity.java#L38-L48
```

### Kotlin

```kotlin
FirebaseInstallations.getInstance().id.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        Log.d("Installations", "Installation ID: " + task.result)
    } else {
        Log.e("Installations", "Unable to get Installation ID")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/kotlin/MainActivity.kt#L33-L39
```

### JavaScript

```javascript
const installationId = await firebase.installations().getId();
console.log(installationId);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/installations/index.js#L17-L18
```

### Dart

    String id = await FirebaseInstallations.instance.getId();

## Retrieve installation auth tokens

Firebase services can authenticate Firebase installations with auth tokens retrieved from FIS. For example, when designing A/B tests forRemote Config, you can authenticate a targeted test device using an installation auth token.
| **Important:** Do not confuse installation auth tokens with[tokens used byFirebase Authentication](https://firebase.google.com/docs/auth/users#auth_tokens). These different types of tokens differ in usage, and are*not*interchangeable.

An installation auth token is a short-lived bearer token in JSON web token (JWT) format containing the following information for an installation:

- TheFirebaseinstallation ID
- The associated project (`projectNumber`)
- The associated Firebase application ID (`appId`)
- The token's expiration date

An installation auth token cannot be revoked, and remains valid until its expiration date. The default token lifetime is one week.

To retrieve an installation auth token:  

### Swift

```swift
do {
  let result = try await Installations.installations()
    .authTokenForcingRefresh(true)
  print("Installation auth token: \(result.authToken)")
} catch {
  print("Error fetching token: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/AppDelegate.swift#L72-L78
```

### Objective-C

```objective-c
[[FIRInstallations installations] authTokenForcingRefresh:true
                                               completion:^(FIRInstallationsAuthTokenResult *result, NSError *error) {
  if (error != nil) {
    NSLog(@"Error fetching Installation token %@", error);
    return;
  }
  NSLog(@"Installation auth token: %@", [result authToken]);
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/ObjCSnippets.m#L55-L62
```

### Java

```java
FirebaseInstallations.getInstance().getToken(/* forceRefresh */true)
        .addOnCompleteListener(new OnCompleteListener<InstallationTokenResult>() {
    @Override
    public void onComplete(@NonNull Task<InstallationTokenResult> task) {
        if (task.isSuccessful() && task.getResult() != null) {
            Log.d("Installations", "Installation auth token: " + task.getResult().getToken());
        } else {
            Log.e("Installations", "Unable to get Installation auth token");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/MainActivity.java#L22-L32
```

### Kotlin

```kotlin
val forceRefresh = true
FirebaseInstallations.getInstance().getToken(forceRefresh)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d("Installations", "Installation auth token: " + task.result?.token)
        } else {
            Log.e("Installations", "Unable to get Installation auth token")
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/kotlin/MainActivity.kt#L19-L27
```

### JavaScript

```javascript
const installationToken = await firebase.installations()
    .getToken(/* forceRefresh */ true);
console.log(installationToken);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/installations/index.js#L28-L30
```

### Dart

    String token = await FirebaseInstallations.instance.getToken();

## Monitor theFirebaseinstallation ID lifecycle

During the normal operation of an app,Firebaseinstallation IDs (FIDs) don't require special monitoring. However, apps that explicitly retrieve and use FIDs should add logic to monitor the potential deletion or rotation of the FID. Here are some cases where FIDs could be deleted or rotated:

- Uninstallation or reinstallation of the app, for instance when an end user installs on a new device.
- The end user clears the cache of the app or the device.
- FID deletion is triggered in the backend due to app inactivity (currently the threshold for this is 270 days of inactivity).

When apps experience FID rotation or deletion in these kinds of cases, they are assigned a new FID. Also, the installation auth token associated with a deleted FID is deleted, regardless of its own maturity, and is replaced with a new installation auth token.

Apps can monitor these changes and respond accordingly.

To monitor FID rotation:  

### Swift

```swift
installationIDObserver = NotificationCenter.default.addObserver(
        forName: .InstallationIDDidChange,
        object: nil,
        queue: nil
) { (notification) in
  // Fetch new Installation ID
  Task {
    await self.fetchInstallationToken()
  }
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/AppDelegate.swift#L46-L55
```

### Objective-C

```objective-c
__weak __auto_type weakSelf = self;
self.installationIDObserver = [[NSNotificationCenter defaultCenter]
        addObserverForName: FIRInstallationIDDidChangeNotification
                    object:nil
                     queue:nil
                usingBlock:^(NSNotification * _Nonnull notification) {
    // Fetch new Installation ID
    [weakSelf fetchInstallationsID];
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/ObjCSnippets.m#L29-L37
```

An NSNotification named`NSNotificationName.InstallationIDDidChange`is posted to the default NSNotificationCenter whenever a new FID is assigned.

### Android

Kotlin and Java clients should add retry logic to respond on failed calls to retrieve the new FID.

### JavaScript

Web apps can subscribe to the`onIdChange`hook.

Whenever a new FID is created, the subscribed callback is triggered:  

```javascript
await firebase.installations().onIdChange((newId) => {
  console.log(newId);
  // TODO: Handle new installation ID.
});
```

### Dart

    FirebaseInstallations.instance.onIdChange.listen((token) {
      print('FID token: $token');
    });

## Migrate from Instance ID toFirebaseinstallations

Prior to the introduction ofFirebaseinstallations, Firebase relied on the Instance ID SDK for identifiers of app installs.Firebaseinstallations provides significant advantages over Instance ID in reliability, performance, and security. Firebase apps that depend on the Instance ID SDK should migrate toFirebaseinstallations.

The migration process is different based on your app:

- Apps that don't directly call Instance ID APIs can migrate by[updating their SDK versions](https://firebase.google.com/docs/projects/manage-installations#version-update). Most Firebase apps fall into this category.

- Apps that explicitly make API calls to Instance ID must update SDK versions**and** [make code changes](https://firebase.google.com/docs/projects/manage-installations#explicit-update)to replace Instance ID methods with theirFirebaseinstallations orFCMequivalents. If your app uses Instance ID to retrieveFCMregistration tokens or explicitly uses Instance ID to target app instances or for any other purpose, you'll need to update your application code.

Currently, FIS is backward-compatible with the legacy identifier Firebase Instance ID.[Deleting an IID](https://firebase.google.com/support/privacy/manage-iids#delete_an_instance_id)is an alternative method of requesting data deletion with these Firebase SDKs:

- iOS 6.14.0 and lower
- Android SDKs earlier than February 27, 2020

This means that apps are not*required* to migrate toFirebaseinstallations; however, doing so is highly recommended.

### Upgrading to minimum SDK versions forFirebaseinstallations

To migrate from Instance ID toFirebaseinstallations, make sure that your applications use at least the listed minimum version numbers of the following Firebase SDKs:

|----------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Firebase SDK**                                   | **Minimum Android version**                                                                 | **Minimum iOS version**                                                                       |
| Firebase Cloud Messaging                           | [v20.3.0](https://firebase.google.com/support/release-notes/android#messaging_v20-3-0)      | [v6.34.0](https://firebase.google.com/support/release-notes/ios#fcm_2)                        |
| Remote Config                                      | [v19.2.0](https://firebase.google.com/support/release-notes/android#remote-config_v19-2-0)  | [v6.24.0](https://firebase.google.com/support/release-notes/ios#remote-config_9)              |
| Google Analytics for Firebase \\ (Measurement SDK) | [v17.4.4](https://firebase.google.com/support/release-notes/android#analytics_v17-4-4)      | [v6.18.0](https://firebase.google.com/support/release-notes/ios#analytics_17)                 |
| In-App Messaging                                   | [v19.0.7](https://firebase.google.com/support/release-notes/android#inappmessaging_v19-0-7) | [v6.24.0](https://firebase.google.com/support/release-notes/ios#version_6240_-_may_5_2020)    |
| Performance Monitoring                             | [v19.0.8](https://firebase.google.com/support/release-notes/android#performance_v19-0-8)    | [v6.21.0](https://firebase.google.com/support/release-notes/ios#performance-monitoring_7)     |
| Crashlytics                                        | [v17.2.1](https://firebase.google.com/support/release-notes/android#crashlytics_v17-2-1)    | [v6.23.0](https://firebase.google.com/support/release-notes/ios#version_6230_-_april_21_2020) |
| ML Kit                                             | [v22.1.2](https://firebase.google.com/support/release-notes/android#mlkit-common_v22-1-2)   | [v6.28.0](https://firebase.google.com/support/release-notes/ios#ml_kit_for_firebase)          |

### Updating code that explicitly calls Instance ID APIs

If your Android or Apple app directly uses Instance ID SDK methods, you can replace that usage with identical alternatives in theFirebaseinstallations SDK or theFCMSDK.

#### Retrieving an identifier

Methods to get Instance IDs are replaced with methods to get an installations ID. For example:

**Before**  

#### Swift

```swift
Messaging.messaging().token { token, error in
  if let error = error {
    print("Error fetching remote FCM registration token: \(error)")
  } else if let token = token {
    print("Remote instance ID token: \(token)")
  }
}
```

#### Objective-C

```objective-c
[[FIRMessaging messaging] tokenWithCompletion:^(NSString * _Nullable token, NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error fetching the remote FCM registration token: %@", error);
  } else {
    NSLog(@"Remote FCM registration token: %@", token);
    NSString* message =
      [NSString stringWithFormat:@"FCM registration token: %@", token];
    // display message
    NSLog(@"%@", message);
  }
}];
```

### Java

```java
FirebaseInstanceId.getInstance().getInstanceId()
        .addOnCompleteListener(new OnCompleteListener<InstanceIdResult>() {
            @Override
            public void onComplete(@NonNull Task<InstanceIdResult> task) {
                Log.d("IID_TOKEN", task.getResult().getToken());
            }
        });
```

### Kotlin

```kotlin
FirebaseInstanceId.getInstance().instanceId
        .addOnSuccessListener { result ->
            Log.d("IID_TOKEN", result.token)
        }
```

**After**  

### Swift

```swift
do {
  let id = try await Installations.installations().installationID()
  print("Installation ID: \(id)")
} catch {
  print("Error fetching id: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/AppDelegate.swift#L61-L66
```

### Objective-C

```objective-c
[[FIRInstallations installations] installationIDWithCompletion:^(NSString *identifier, NSError *error) {
  if (error != nil) {
    NSLog(@"Error fetching Installation ID %@", error);
    return;
  }
  NSLog(@"Installation ID: %@", identifier);
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/installations/InstallationsSnippets/ObjCSnippets.m#L43-L49
```

### Java

```java
FirebaseInstallations.getInstance().getId()
        .addOnCompleteListener(new OnCompleteListener<String>() {
    @Override
    public void onComplete(@NonNull Task<String> task) {
        if (task.isSuccessful()) {
            Log.d("Installations", "Installation ID: " + task.getResult());
        } else {
            Log.e("Installations", "Unable to get Installation ID");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/MainActivity.java#L38-L48
```

### Kotlin

```kotlin
FirebaseInstallations.getInstance().id.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        Log.d("Installations", "Installation ID: " + task.result)
    } else {
        Log.e("Installations", "Unable to get Installation ID")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/kotlin/MainActivity.kt#L33-L39
```

#### Deleting an identifier

Methods to delete Instance IDs are replaced with methods to deleteFirebaseinstallation IDs. For example:

**Before**  

### Swift

    InstanceID.instanceID().deleteID { error in
      if let error = error {
        print("Error deleting instance ID: \(error)")
      }
    }

### Objective-C

    [FIRInstanceID instanceID] deleteIDWithHandler:^(NSError *error) {
      if error != nil {
        NSLog(@"Error deleting instance ID: %@", error);
      }
    }];

### Android

    FirebaseInstanceId.deleteInstanceId();

**After**  

### Swift

    func delete(completion: @escaping (Error?) -> Void)

### Objective-C

    - (void)deleteWithCompletion:(nonnull void (^)(NSError *_Nullable))completion;

### Java

```java
FirebaseInstallations.getInstance().delete()
        .addOnCompleteListener(new OnCompleteListener<Void>() {
    @Override
    public void onComplete(@NonNull Task<Void> task) {
        if (task.isSuccessful()) {
            Log.d("Installations", "Installation deleted");
        } else {
            Log.e("Installations", "Unable to delete Installation");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/MainActivity.java#L54-L64
```

### Kotlin

```kotlin
FirebaseInstallations.getInstance().delete().addOnCompleteListener { task ->
    if (task.isComplete) {
        Log.d("Installations", "Installation deleted")
    } else {
        Log.e("Installations", "Unable to delete Installation")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/kotlin/MainActivity.kt#L45-L51
```

#### Retrieving anFCMregistration token

Prior to the introduction of Firebase Installations,FCMclients retrieved registration tokens from Instance ID. Now, theFCMSDK provides methods to retrieve the registration token.

**Before**  

### Java

```java
FirebaseInstanceId.getInstance().getInstanceId()
        .addOnCompleteListener(new OnCompleteListener<InstanceIdResult>() {
            @Override
            public void onComplete(@NonNull Task<InstanceIdResult> task) {
                if (!task.isSuccessful()) {
                    Log.w(TAG, "getInstanceId failed", task.getException());
                    return;
                }

                // Get new Instance ID token
                String token = task.getResult().getToken();

                // Log and toast
                String msg = getString(R.string.msg_token_fmt, token);
                Log.d(TAG, msg);
                Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
            }
        });
```

### Kotlin

```kotlin
FirebaseInstanceId.getInstance().instanceId
        .addOnCompleteListener(OnCompleteListener { task ->
            if (!task.isSuccessful) {
                Log.w(TAG, "getInstanceId failed", task.exception)
                return@OnCompleteListener
            }

            // Get new Instance ID token
            val token = task.result?.token

            // Log and toast
            val msg = getString(R.string.msg_token_fmt, token)
            Log.d(TAG, msg)
            Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
        })
```

#### Swift

```swift
InstanceID.instanceID().instanceID { result, error in
  if let error = error {
    print("Error fetching instance ID: \(error)")
  } else if let result = result {
    print("Instance ID token: \(result.token)")
  }
}
```

#### Objective-C

```objective-c
[[FIRInstanceID instanceID] instanceIDWithHandler:^(FIRInstanceIDResult * _Nullable result,
                                                    NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error fetching instance ID: %@", error);
  } else {
    NSLog(@"Instance ID token: %@", result.token);
  }
}];
```

**After**  

### Java

```java
FirebaseMessaging.getInstance().getToken()
    .addOnCompleteListener(new OnCompleteListener<String>() {
        @Override
        public void onComplete(@NonNull Task<String> task) {
          if (!task.isSuccessful()) {
            Log.w(TAG, "Fetching FCM registration token failed", task.getException());
            return;
          }

          // Get new FCM registration token
          String token = task.getResult();

          // Log and toast
          String msg = getString(R.string.msg_token_fmt, token);
          Log.d(TAG, msg);
          Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
        }
    });
```

### Kotlin

```kotlin
FirebaseMessaging.getInstance().token.addOnCompleteListener(OnCompleteListener { task ->
    if (!task.isSuccessful) {
        Log.w(TAG, "Fetching FCM registration token failed", task.exception)
        return@OnCompleteListener
    }

    // Get new FCM registration token
    val token = task.result

    // Log and toast
    val msg = getString(R.string.msg_token_fmt, token)
    Log.d(TAG, msg)
    Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
})
```

#### Swift

```swift
Messaging.messaging().token { token, error in
  if let error = error {
    print("Error fetching remote FCM registration token: \(error)")
  } else if let token = token {
    print("Remote instance ID token: \(token)")
  }
}
```

#### Objective-C

```objective-c
[[FIRMessaging messaging] tokenWithCompletion:^(NSString * _Nullable token, NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error fetching the remote FCM registration token: %@", error);
  } else {
    NSLog(@"Remote FCM registration token: %@", token);
    NSString* message =
      [NSString stringWithFormat:@"FCM registration token: %@", token];
    // display message
    NSLog(@"%@", message);
  }
}];
```