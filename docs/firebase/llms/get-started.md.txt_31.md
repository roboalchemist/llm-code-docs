# Source: https://firebase.google.com/docs/remote-config/android/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/remote-config/ios/get-started) [Android](https://firebase.google.com/docs/remote-config/android/get-started) [Web](https://firebase.google.com/docs/remote-config/web/get-started) [Flutter](https://firebase.google.com/docs/remote-config/flutter/get-started) [Unity](https://firebase.google.com/docs/remote-config/unity/get-started) [C++](https://firebase.google.com/docs/remote-config/cpp/get-started) |

<br />

[Video](https://www.youtube.com/watch?v=pcnnbjAAIkI)

You can use Firebase Remote Config to define parameters in your app and
update their values in the cloud, allowing you to modify the appearance and
behavior of your app without distributing an app update. This guide walks you
through the steps to get started and provides some sample code, all of which is
available to clone or download from the
[firebase/quickstart-android](https://github.com/firebase/quickstart-android/tree/master)
GitHub repository.

## Step 1: Add Firebase and the Remote Config SDK to your app

1. If you haven't already, [add Firebase to your Android
   project](https://firebase.google.com/docs/android/setup).

2. For Remote Config, Google Analytics is required for the
   [conditional targeting of app instances](https://firebase.google.com/docs/remote-config/parameters#conditions_rules_and_conditional_values)
   to user properties and audiences. Make sure that you [enable Google Analytics](https://support.google.com/firebase/answer/9289399#linkga) in your project.

3.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add dependencies for the Remote Config and Analytics libraries for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.

   Also, as part of setting up Analytics, you need to add the Firebase SDK
   for Google Analytics to your app.


   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependencies for the Remote Config and Analytics libraries
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-config")
   implementation("com.google.firebase:firebase-analytics")
   }
   ```

   By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)*
   Add Firebase library dependencies *without* using the BoM

   If you choose not to use the Firebase BoM, you must specify each Firebase library version
   in its dependency line.

   **Note that if you use *multiple* Firebase libraries in your app, we strongly
   recommend using the BoM to manage library versions, which ensures that all versions are
   compatible.**

   ```groovy
   dependencies {
       // Add the dependencies for the Remote Config and Analytics libraries
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-config:23.0.1")
       implementation("com.google.firebase:firebase-analytics:23.0.0")
   }
   ```

   <br />

> [!NOTE]
> **Note:** Because the Android SDK has a dependency on the Remote Config REST API, make sure that you do **not** disable that API, which is enabled by default in a typical project.

## Step 2: Get the Remote Config singleton object

Get a Remote Config object instance and set the minimum fetch interval to
allow for frequent refreshes:

### Kotlin

```kotlin
val remoteConfig: FirebaseRemoteConfig = Firebase.remoteConfig
val configSettings = remoteConfigSettings {
    minimumFetchIntervalInSeconds = 3600
}
remoteConfig.setConfigSettingsAsync(configSettings)
```

### Java

```java
FirebaseRemoteConfig mFirebaseRemoteConfig = FirebaseRemoteConfig.getInstance();
FirebaseRemoteConfigSettings configSettings = new FirebaseRemoteConfigSettings.Builder()
        .setMinimumFetchIntervalInSeconds(3600)
        .build();
mFirebaseRemoteConfig.setConfigSettingsAsync(configSettings);
```

The singleton object is used to store in-app default parameter values, fetch
updated parameter values from the backend, and control when fetched values are
made available to your app.

During development, it's recommended to set a relatively low minimum fetch
interval. See [Throttling](https://firebase.google.com/docs/remote-config/android/get-started#throttling)
for more information.

## Step 3: Set in-app default parameter values

You can set in-app default parameter values in the Remote Config
object, so that your app behaves as intended before it connects to the
Remote Config backend, and so that default values are available if none are
set in the backend.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or values. Remote Config data is encrypted in transit, but end users can access any default or fetched Remote Config parameter that is available to their client app instance.

1. Define a set of parameter names and default parameter values using a
   [Map](http://developer.android.com/reference/java/util/Map.html) object or
   an [XML resource
   file](https://developer.android.com/guide/topics/resources/providing-resources.html)
   stored in your app's `res/xml` folder. The Remote Config quickstart
   sample app uses an [XML
   file](https://github.com/firebase/quickstart-android/blob/master/config/app/src/main/res/xml/remote_config_defaults.xml)
   to define default parameter names and values.

   If you have already configured Remote Config backend parameter values,
   you can download a generated XML file that includes all default values and
   save it to your app's `res/xml` directory:

   ### REST

   ```
   curl --compressed -D headers -H "Authorization: Bearer token" -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig:downloadDefaults?format=XML -o remote_config_defaults.xml
   ```

   You can generate a bearer token by running the following command using
   the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) or
   [Cloud Shell](https://cloud.google.com/shell/docs/run-gcloud-commands):

       gcloud auth print-access-token

   This token is short-lived, so you may need to regenerate it if you get
   an authentication error.

   ### Firebase console

   1. In the [Parameters](https://console.firebase.google.com/project/_/config)
      tab, open the **Menu** ,
      and select **Download default values**.

   2. When prompted, enable **.xml for Android** , then click
      **Download file**.

2. Add these values to the Remote Config object using
   [`setDefaultsAsync(int)`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(int)),
   as shown:

   ### Kotlin

   ```kotlin
   remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)
   ```

   ### Java

   ```java
   mFirebaseRemoteConfig.setDefaultsAsync(R.xml.remote_config_defaults);
   ```

## Step 4: Get parameter values to use in your app

Now you can get parameter values from the Remote Config object. If you set
values in the backend, fetch them, and then activate them, those values are
available to your app. Otherwise, you get the in-app parameter values configured
using
[`setDefaultsAsync(int)`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(int)).
To get these values, call the method listed in the following code that maps to
the data type expected by your app, providing the parameter key as an argument:

- [`getBoolean()`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getBoolean(java.lang.String))
- [`getDouble()`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getDouble(java.lang.String))
- [`getLong()`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getLong(java.lang.String))
- [`getString()`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getString(java.lang.String))

## Step 5: Set parameter values in the Remote Config backend

Using the Firebase console or the [Remote Config backend
APIs](https://firebase.google.com/docs/remote-config/automate-rc), you can create new server-side default
values that override the in-app values according to your desired conditional
logic or user targeting. This section describes the Firebase console steps to
create these values.

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Remote Config** from the menu to view the Remote Config dashboard.
3. Define parameters with the same names as the parameters that you defined in your app. For each parameter, you can set a default value (which will eventually override the corresponding in-app default value), and you can also set conditional values. To learn more, see [Remote Config
   Parameters and Conditions](https://firebase.google.com/docs/remote-config/parameters).
4. If using [custom signal
   conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom_signal_conditions),
   define the attributes and their values. The following examples show how to
   define a custom signal condition.

   ### Kotlin

   ```kotlin
           val customSignals = customSignals {
               put("city", "Tokyo")
               put("preferred_event_category", "sports")
           }

           remoteConfig.setCustomSignals(customSignals)
       
   ```

   ### Java

   ```java
           CustomSignals customSignals = new CustomSignals.Builder()
               .put("city", "Tokyo")
               .put("preferred_event_category", "sports")
               .build();

           mFirebaseRemoteConfig.setCustomSignals(customSignals);

       
   ```

## Step 6: Fetch and activate values

1. To fetch parameter values from the Remote Config backend, call the [`fetch()`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()) method. Any values that you set in the backend are fetched and stored in the Remote Config object.
2. To make fetched parameter values available to your app, call the
   [`activate()`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate())
   method.

   For cases where you want to fetch and activate values in one call, you can
   use a `fetchAndActivate()` request to fetch values from the
   Remote Config backend and make them available to the app:

   ### Kotlin

   ```kotlin
   remoteConfig.fetchAndActivate()
       .addOnCompleteListener(this) { task ->
           if (task.isSuccessful) {
               val updated = task.result
               Log.d(TAG, "Config params updated: $updated")
               Toast.makeText(
                   this,
                   "Fetch and activate succeeded",
                   Toast.LENGTH_SHORT,
               ).show()
           } else {
               Toast.makeText(
                   this,
                   "Fetch failed",
                   Toast.LENGTH_SHORT,
               ).show()
           }
           displayWelcomeMessage()
       }
   ```

   ### Java

   ```java
   mFirebaseRemoteConfig.fetchAndActivate()
           .addOnCompleteListener(this, new OnCompleteListener<Boolean>() {
               @Override
               public void onComplete(@NonNull Task<Boolean> task) {
                   if (task.isSuccessful()) {
                       boolean updated = task.getResult();
                       Log.d(TAG, "Config params updated: " + updated);
                       Toast.makeText(MainActivity.this, "Fetch and activate succeeded",
                               Toast.LENGTH_SHORT).show();

                   } else {
                       Toast.makeText(MainActivity.this, "Fetch failed",
                               Toast.LENGTH_SHORT).show();
                   }
                   displayWelcomeMessage();
               }
           });
   ```

Because these updated parameter values affect the behavior and appearance of
your app, you should activate the fetched values at a time that ensures a smooth
experience for your user, such as the next time that the user opens your app.
See [Remote Config loading strategies](https://firebase.google.com/docs/remote-config/loading) for more
information and examples.

> [!NOTE]
> **Note:** If your app doesn't build with Gradle, you must manually add the correct `google_app_id` string resource to your app so that Remote Config can initialize. The `google-services` Gradle plugin normally adds this automatically, but you can find the appropriate value in the `google-services.json` file that you download from the Firebase console. For more information on getting the `google_app_id` value from the `google-services.json` file, see [Processing the JSON
> file](https://developers.google.com/android/guides/google-services-plugin#processing_the_json_file).

## Step 7: Listen for updates in real time

After you fetch parameter values, you can use real-time Remote Config to
listen for updates from the Remote Config backend. Real-time
Remote Config signals to connected devices when updates are available and
automatically fetches the changes after you publish a new Remote Config
version.

Real-time updates are supported by the Firebase SDK for Android v21.3.0+ (
Firebase BoM v31.2.4+).

> [!NOTE]
> **Important:** Real-time Remote Config also requires the
> Firebase Remote Config
> Realtime API, which should already be enabled for you. To verify, open the
> [Google Cloud console](https://console.developers.google.com/apis/api/firebaseremoteconfigrealtime.googleapis.com/overview),
> select your project, and open the **APIs and Services** page. The API should
> appear as enabled. If it's missing or not enabled, click **Enable APIs \&
> Services** , search for **Firebase Remote Config Realtime API**, and
> enable it.

1. In your app, use `addOnConfigUpdateListener()` to start listening for
   updates and automatically fetch any new parameter values. Implement the
   `onUpdate()` callback to activate the updated config.

   ### Kotlin

   ```kotlin
   remoteConfig.addOnConfigUpdateListener(object : ConfigUpdateListener {
           override fun onUpdate(configUpdate : ConfigUpdate) {
           Log.d(TAG, "Updated keys: " + configUpdate.updatedKeys);

           if (configUpdate.updatedKeys.contains("welcome_message")) {
               remoteConfig.activate().addOnCompleteListener {
                   displayWelcomeMessage()
               }
           }
           }

           override fun onError(error : FirebaseRemoteConfigException) {
               Log.w(TAG, "Config update error with code: " + error.code, error)
           }
       })
       
   ```

   ### Java

   ```java
       mFirebaseRemoteConfig.addOnConfigUpdateListener(new ConfigUpdateListener() {
           @Override
           public void onUpdate(ConfigUpdate configUpdate) {
               Log.d(TAG, "Updated keys: " + configUpdate.getUpdatedKeys());
               mFirebaseRemoteConfig.activate().addOnCompleteListener(new OnCompleteListener<Boolean>() {
                   @Override
                   public void onComplete(@NonNull Task<Boolean> task) {
                       displayWelcomeMessage();
                   }
               });
           }
           @Override
           public void onError(FirebaseRemoteConfigException error) {
               Log.w(TAG, "Config update error with code: " + error.getCode(), error);
           }
       });
       
   ```
2. The next time you publish a new version of your Remote Config, devices
   that are running your app and listening for changes will call the
   `ConfigUpdateListener`.

## Throttling

If an app fetches too many times in a short time period, fetch calls are
throttled and the SDK returns `FirebaseRemoteConfigFetchThrottledException`.
Before SDK version 17.0.0, the limit was 5 fetch requests in a 60 minute window
(newer versions have more permissive limits).

> [!TIP]
> **Tip:** Starting with Android SDK v21.3.0+ (Firebase BoM v31.3.0+), you can use real-time Remote Config to automatically fetch updated parameter values from the Remote Config backend as soon as they're published, bypassing any minimum fetch interval setting. For more information, see [Listen
> for updates in real time](https://firebase.google.com/docs/remote-config/android/get-started#add-real-time-listener).

During app development, you might want to fetch and activate configs very
frequently (many times per hour) to let you rapidly iterate as you develop and
test your app. Real-time Remote Config updates automatically bypass the
cache when the config is updated on the server. To accommodate rapid iteration
on a project with up to 10 developers, you can temporarily set a
`FirebaseRemoteConfigSettings` object with a low minimum fetch interval
(`setMinimumFetchIntervalInSeconds`) in your app.

The default minimum fetch interval for Remote Config is 12 hours, which
means that configs won't be fetched from the backend more than once in a 12 hour
window, regardless of how many fetch calls are actually made. Specifically, the
minimum fetch interval is determined in this following order:

1. The parameter in `fetch(long)`
2. The parameter in `FirebaseRemoteConfigSettings.setMinimumFetchIntervalInSeconds(long)`
3. The default value of 12 hours

To set the minimum fetch interval to a custom value, use
[`FirebaseRemoteConfigSettings.Builder.setMinimumFetchIntervalInSeconds(long)`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#setMinimumFetchIntervalInSeconds(long)).

> [!CAUTION]
> Keep in mind that this setting should be used for development only, not for an app running in production. If you're just testing your app with a small 10-person development team, you are unlikely to hit the hourly service-side quota limits. But if you pushed your app out to thousands of test users with a very low minimum fetch interval, your app would probably hit this quota.