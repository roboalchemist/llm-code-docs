# Source: https://firebase.google.com/docs/projects/multiprojects.md.txt

This page describes how to use more than one Firebase project in your app.

Many apps need only a single Firebase project and the default set up described in the*Get Started*guides. Examples of when it can be useful to use multiple Firebase projects include:

- Setting up your development environment to use different Firebase projects based on build type or target.
- Accessing the content from multiple Firebase projects in your app.

## Support different environments

One common use case is to support separate Firebase projects for your development and production environments.

The Web and Admin SDKs are configured by directly passing values to their initialization functions. For these SDK, you can use a runtime check to select development or production configuration variables.

Android and Apple platforms (and their Unity and C++ wrappers) normally load configuration from a configuration file:`GoogleService-Info.plist`on Apple platform and`google-services.json`on Android. These files are read into an options object (`FIROption`or`FirebaseOptions`) that is referenced by the Firebase application object (`FIRApp`or`FirebaseApp`).

For these platforms, switching between environments is usually implemented as a build time decision, through use of different configuration files for each environment.

### Support multiple environments in your Apple application

By default,`FirebaseApp.configure()`will load the`GoogleService-Info.plist`file bundled with the application. If your development and production environments are configured as separate targets in Xcode, you can:

- Download both`GoogleService-Info.plist`files
- Store the two files in different directories
- Add both to your Xcode project
- Associate the different files with the different targets using the Target Membership panel:

![Target Membership panel](https://firebase.google.com/static/images/targetmembership.png)

If the builds are part of a single target, the best option is to give both configuration files unique names (e.g.`GoogleService-Info-Free.plist`and`GoogleService-Info-Paid.plist`). Then choose at runtime which plist to load. This is shown in the following example:  

```gdscript
// Load a named file.
guard 
  let filePath = Bundle.main.path(forResource: "MyGoogleService", ofType: "plist"),
  let fileOptions = FirebaseOptions(contentsOfFile: filePath)
else { fatalError("Couldn't load config file.") }
FirebaseApp.configure(options: fileOptions)
```
| **Warning:** This approach can impactAnalyticscollection in some circumstances, see the[reliable analytics](https://firebase.google.com/docs/projects/multiprojects#reliable-analytics)section.

### Support multiple environments in your Android application

In Android, the`google-services.json`file is processed into Android string resources by the Google Services gradle plugin. You can see which resources are created in the Google Services Plugin documentation on[Processing the JSON file](https://developers.google.com/android/guides/google-services-plugin#processing_the_json_file).

You can have multiple`google-services.json`files for different[build variants](https://developer.android.com/studio/build/build-variants.html)by placing`google-services.json`files in dedicated directories named for each variant under the app module root. For example, if you have "development" and "release" build flavors, your configuration could be organized like this:  

    app/
        google-services.json
        src/development/google-services.json
        src/release/google-services.json
        ...

To learn more, see the Google Services Plugin documentation on[Adding the JSON file](https://developers.google.com/android/guides/google-services-plugin#adding_the_json_file).

These resources are then loaded by the[FirebaseInitProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider), which runs before your application code and initializes Firebase APIs using those values.

Because this provider is just reading resources with known names, another option is to add the string resources directly to your app instead of using the Google Services gradle plugin. You can do this by:

- Removing the`google-services`plugin from your root`build.gradle`
- Deleting the`google-services.json`from your project
- Adding the string resources directly
- Deleting`apply plugin: 'com.google.gms.google-services'`from your app`build.gradle`

## Use multiple projects in your application

Sometimes you need to access different projects using the same APIs - for example, accessing multiple database instances. In most cases there is a central Firebase application object that manages the configuration for all the Firebase APIs. This object is initialized as part of your normal setup. However, when you want to access multiple projects from a single application, you'll need a distinct Firebase application object to reference each one individually. It's up to you to initialize these other instances.

In both cases, you need to first create a Firebase options object to hold the configuration data for the Firebase application. Full documentation for the options can be found in the API reference documentation for the following classes:

- Swift:[`FirebaseOptions(googleAppID:gcmSenderID:)`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseOptions#/c:objc(cs)FIROptions(im)initWithGoogleAppID:GCMSenderID:)
- Android:[`FirebaseOptions.Builder`](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder)
- Web:[`initializeApp()`](https://firebase.google.com/docs/reference/js/app#initializeapp)
- C++:[`firebase::App::Create`](https://firebase.google.com/docs/reference/cpp/class/firebase/app#create)
- Unity:[`FirebaseApp.Create`](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#create)
- Node.js:[`initializeApp`](https://firebase.google.com/docs/reference/admin/node/firebase-admin#initializeapp)
- Java:[`FirebaseOptions.Builder`](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)

The use of these classes to support multiple projects in an application is shown in the following examples:  

### Swift

```swift
// Configure with manual options. Note that projectID and apiKey, though not
// required by the initializer, are mandatory.
let secondaryOptions = FirebaseOptions(googleAppID: "1:27992087142:ios:2a4732a34787067a",
                                       gcmSenderID: "27992087142")
secondaryOptions.apiKey = "AIzaSyBicqfAZPvMgC7NZkjayUEsrepxuXzZDsk"
secondaryOptions.projectID = "projectid-12345"

// The other options are not mandatory, but may be required
// for specific Firebase products.
secondaryOptions.bundleID = "com.google.firebase.devrel.FiroptionConfiguration"
secondaryOptions.clientID = "27992087142-ola6qe637ulk8780vl8mo5vogegkm23n.apps.googleusercontent.com"
secondaryOptions.databaseURL = "https://myproject.firebaseio.com"
secondaryOptions.storageBucket = "myproject.appspot.com"
secondaryOptions.deepLinkURLScheme = "myapp://"
secondaryOptions.storageBucket = "projectid-12345.appspot.com"
secondaryOptions.appGroupID = nil  
https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AppDelegate.swift#L48-L63
```

### Kotlin

```kotlin
// Manually configure Firebase Options. The following fields are REQUIRED:
//   - Project ID
//   - App ID
//   - API Key
val options = FirebaseOptions.Builder()
    .setProjectId("my-firebase-project")
    .setApplicationId("1:27992087142:android:ce3b6448250083d1")
    .setApiKey("AIzaSyADUe90ULnQDuGShD9W23RDP0xmeDc6Mvw")
    // .setDatabaseUrl(...)
    // .setStorageBucket(...)
    .build()https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firebaseoptions/app/src/main/java/devrel/firebase/google/com/firebaseoptions/kotlin/MainActivity.kt#L19-L29
```

### Java

```java
// Manually configure Firebase Options. The following fields are REQUIRED:
//   - Project ID
//   - App ID
//   - API Key
FirebaseOptions options = new FirebaseOptions.Builder()
        .setProjectId("my-firebase-project")
        .setApplicationId("1:27992087142:android:ce3b6448250083d1")
        .setApiKey("AIzaSyADUe90ULnQDuGShD9W23RDP0xmeDc6Mvw")
        // setDatabaseURL(...)
        // setStorageBucket(...)
        .build();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firebaseoptions/app/src/main/java/devrel/firebase/google/com/firebaseoptions/MainActivity.java#L32-L42
```

### Web

```javascript
// The following fields are REQUIRED:
//  - Project ID
//  - App ID
//  - API Key
const secondaryAppConfig = {
    projectId: "<PROJECT_ID>",
    appId: "<APP_ID>",
    apiKey: "<API_KEY>",
    // databaseURL: "...",
    // storageBucket: "...",
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firebaseapp/firebaseapp.js#L5-L15
```

### C++

    firebase::AppOptions secondary_app_options;

    // API key, app ID, and project ID are always required.
    secondary_app_options.set_api_key("<API_KEY>");
    secondary_app_options.set_app_id("<GOOGLE_APP_ID>");
    secondary_app_options.set_project_id("<PROJECT_ID>");

    // The following options are specific to individual Firebase products
    // and may not always be required.
    secondary_app_options.set_database_url("<DATABASE_URL>");
    secondary_app_options.set_messaging_sender_id("<SENDER_ID>");
    secondary_app_options.set_storage_bucket("<STORAGE_BUCKET>");

### Unity

    Firebase.AppOptions secondaryAppOptions = new Firebase.AppOptions {
      ApiKey = "<API_KEY>",
      AppId = "<GOOGLE_APP_ID>",
      ProjectId = "<PROJECT_ID>"
    };

### Node.js

```javascript
const secondaryServiceAccount = require('./path/to/serviceAccountKey.json');

// All required options are specified by the service account,
// add service-specific configuration like databaseURL as needed.
const secondaryAppConfig = {
    credential: cert(secondaryServiceAccount),
    // databaseURL: 'https://<DATABASE_NAME>.firebaseio.com'
};https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firebaseapp/index.js#L76-L83
```

### Java

    FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccountKey.json");

    FirebaseOptions secondaryAppConfig = new FirebaseOptions.Builder()
      .setCredential(FirebaseCredentials.fromCertificate(serviceAccount))
      .setDatabaseUrl("https://<DATABASE_NAME>.firebaseio.com/")
      .build();

After you have initialized this options object, you can use it to configure an additional Firebase application instance. Note that in all the examples shown below we use the string*secondary* . This name is used to retrieve the application instance, and to distinguish it from other instances, including the default instance (named*\[DEFAULT\]*). You should pick a string appropriate to the intended use of the other Firebase project.

The following snippets demonstrate connecting to an alternativeRealtime Database(the APIs for other Firebase features follow the same pattern).  

### Swift

```swift
// Configure an alternative FIRApp.
FirebaseApp.configure(name: "secondary", options: secondaryOptions)

// Retrieve a previous created named app.
guard let secondary = FirebaseApp.app(name: "secondary")
  else { fatalError("Could not retrieve secondary app") }


// Retrieve a Real Time Database client configured against a specific app.
let secondaryDb = Database.database(app: secondary)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AppDelegate.swift#L68-L77
```

### Kotlin

```kotlin
// Initialize secondary FirebaseApp.
Firebase.initialize(context = this, options, "secondary")

// Retrieve secondary FirebaseApp.
val secondary = Firebase.app("secondary")
// Get the database for the other app.
val secondaryDatabase = Firebase.database(secondary)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firebaseoptions/app/src/main/java/devrel/firebase/google/com/firebaseoptions/kotlin/MainActivity.kt#L33-L39
```

### Java

```java
// Initialize with secondary app
FirebaseApp.initializeApp(this /* Context */, options, "secondary");

// Retrieve secondary FirebaseApp
FirebaseApp secondary = FirebaseApp.getInstance("secondary");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firebaseoptions/app/src/main/java/devrel/firebase/google/com/firebaseoptions/MainActivity.java#L46-L50
```

### Web

```javascript
// Initialize another app with a different config
const secondaryApp = firebase.initializeApp(secondaryAppConfig, "secondary");
// Access services, such as the Realtime Database
// secondaryApp.database();  
https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firebaseapp/firebaseapp.js#L19-L22
```

### C++

    firebase::App* secondary_app = firebase::App::Create(secondary_app_options, "Secondary");
    firebase::database::Database* secondary_database = firebase::database::Database::GetInstance(secondary_app);

### Unity

    var secondaryApp = Firebase.FirebaseApp.Create(secondaryAppOptions, "Secondary"));
    var secondaryDatabase = Firebase.Database.FirebaseDatabase.getInstance(secondaryApp);

### Node.js

```javascript
// Initialize another app with a different config
const secondary = initializeApp(secondaryAppConfig, 'secondary');
// Access services, such as the Realtime Database
// const secondaryDatabase = secondary.database();  
https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firebaseapp/index.js#L87-L90
```

### Java

    // Initialize another app with a different config
    FirebaseApp secondaryApp = FirebaseApp.initializeApp(secondaryAppConfig, "secondary");

    // Retrieve the database.
    FirebaseDatabase secondaryDatabase = FirebaseDatabase.getInstance(secondaryApp);

| **Note:** On Android and Apple platforms,Analyticsare only logged for the default app.

## Ensure reliable reporting forAnalytics

Google Analyticscollects events very early in the app start up flow, in some occasions before the primary Firebase app instance has been configured. In these cases, Firebase refers to the Android resource or`GoogleService-Info.plist`on Apple platforms to look up the correct Google app ID to store events. For this reason, we recommend using the default configuration methods wherever possible.

If runtime configuration is required, please note the following caveats:

1. If you're usingAdMoband request ads at startup as recommended, you may miss some Analytics data to related to mobile ads when not using the resource based configuration approach.
2. Only ever supply a single Google app ID in each distributed variant of your app. For example, if you ship version 1 of your app with a certain`GOOGLE_APP_ID`in the configuration then upload version 2 with a different ID, it may cause analytics data to be dropped.
3. On Apple platforms, do not add GoogleService-Info.plist to your project if you are supplying different configuration at run time, as this can result in an apparent change of`GOOGLE_APP_ID`and result in lost Analytics.