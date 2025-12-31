# Source: https://firebase.google.com/docs/perf-mon/get-started-android.md.txt

<br />

## Before you begin

If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

## **Step 1** : Add thePerformance MonitoringSDK to your app

After you've added thePerformance MonitoringSDK, Firebase automatically starts collecting data for your app's[screen rendering](https://firebase.google.com/docs/perf-mon/screen-traces)and data related to your app's lifecycle (like[app start time](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces)). To enable Firebase to monitor network requests, you must*also* add thePerformance MonitoringGradle plugin (next step).

1. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for thePerformance Monitoringlibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

   <br />

   ```carbon
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Performance Monitoring library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-perf")
   }
   ```

   By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)* Add Firebase library dependencies*without* using theBoM

   If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

   **Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

   ```groovy
   dependencies {
       // Add the dependency for the Performance Monitoring library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-perf:22.0.4")
   }
   ```

   <br />

2. Recompile your app.

| **Note:** When you add thePerformance MonitoringSDK to your app, theRemote ConfigSDK is included as a dependency. If you already useRemote Config, you won't see any difference. However, if you're new toRemote Config, explore the[Remote Configdocumentation](https://firebase.google.com/docs/remote-config/android)to learn more about the various features you'll be able to access in your app.

## **Step 2** : Add thePerformance MonitoringGradle plugin to your app

After you've added thePerformance MonitoringGradle plugin, Firebase automatically starts collecting data for[HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces?platform=android). The plugin also enables you to instrument custom code traces using[@AddTrace annotation](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=android#add-trace-annotation).
How thePerformance Monitoringplugin works

Before your code is converted to DEX files, thePerformance Monitoringplugin uses the[Transform API](https://developer.android.com/reference/tools/gradle-api/current/com/android/build/api/transform/Transform)and the[ASM bytecode instrumentation framework](https://asm.ow2.io/)to visit your app's compiled class files and to instrument the code (to measure performance). The time it takes to instrument your code largely depends on the number and size of your classes.

If your app takes more time to compile than you'd like, consider the following options:

- [Disable thePerformance Monitoringplugin](https://firebase.google.com/docs/perf-mon/disable-sdk?platform=android#disable-during-build)for your debug builds at compile time
- [Modularize your code](https://developer.android.com/studio/build/optimize-your-build#create_libraries)to optimize your build speed

1. In your**root-level (project-level)** Gradle file (`<project>/build.gradle.kts`or`<project>/build.gradle`), add thePerformance MonitoringGradle plugin:

   ### Kotlin

   Are you still using the`buildscript`syntax? Learn how to[add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax)using that syntax.  

   ```kotlin
   plugins {
       // To benefit from the latest Performance Monitoring plugin features,
       // update your Android Gradle plugin dependency to at least v3.4.0
       id("com.android.application") version "7.3.0" apply false

       // Make sure that you have the Google services Gradle plugin dependency
       id("com.google.gms.google-services") version "4.4.4" apply false

       // Add the dependency for the Performance Monitoring Gradle plugin
       id("com.google.firebase.firebase-perf") version "2.0.2" apply false
   }
   ```

   ### Groovy

   Are you still using the`buildscript`syntax? Learn how to[add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax)using that syntax.  

   ```groovy
   plugins {
       // To benefit from the latest Performance Monitoring plugin features,
       // update your Android Gradle plugin dependency to at least v3.4.0
       id 'com.android.application' version '7.3.0' apply false

       // Make sure that you have the Google services Gradle plugin dependency
       id 'com.google.gms.google-services' version '4.4.4' apply false

       // Add the dependency for the Performance Monitoring Gradle plugin
       id 'com.google.firebase.firebase-perf' version '2.0.2' apply false
   }
   ```
2. In your**module (app-level)** Gradle file (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add thePerformance MonitoringGradle plugin:

   ### Kotlin

   ```kotlin
   plugins {
       id("com.android.application")

       // Make sure that you have the Google services Gradle plugin
       id("com.google.gms.google-services")

       // Add the Performance Monitoring Gradle plugin
       id("com.google.firebase.firebase-perf")
       ...
   }
   ```

   ### Groovy

   ```groovy
   plugins {
       id 'com.android.application'

       // Make sure that you have the Google services Gradle plugin
       id 'com.google.gms.google-services'

       // Add the Performance Monitoring Gradle plugin
       id 'com.google.firebase.firebase-perf'
       ...
   }
   ```
3. Recompile your app.

## **Step 3**: Generate performance events for initial data display

Firebase starts processing the events when you successfully add the SDK to your app. If you're still developing locally, interact with your app to generate events for initial data collection and processing.
| **Note:** ThePerformance MonitoringSDK batches events locally then sends them to Firebase periodically (every 30 seconds). So, there's a delay between an app interaction and when Firebase receives the event information from your app.

1. Generate events by switching your app between background and foreground several times, interacting with your app by navigating across screens, and/or triggering network requests.

2. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole. You should see your initial data display within a few minutes.

   If you don't see a display of your initial data, review the[troubleshooting tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=android#sdk-detected-no-data).

## **Step 4** :*(Optional)*View log messages for performance events

1. Enable debug logging forPerformance Monitoringat build time by adding a`<meta-data>`element to your app's`AndroidManifest.xml`file, like so:

   ```scdoc
   <application>
       <meta-data
         android:name="firebase_performance_logcat_enabled"
         android:value="true" />
   </application>
   ```
2. Check your log messages for any error messages.

3. Performance Monitoringtags its log messages with`FirebasePerformance`. Using logcat filtering, you can specifically view duration trace and HTTP/S network request logging by running the following command:

   ```
   adb logcat -s FirebasePerformance
   ```
4. Check for the following types of logs which indicate thatPerformance Monitoringis logging performance events:

   - `Logging trace metric: `<var translate="no">TRACE_NAME</var>`, `<var translate="no">FIREBASE_PERFORMANCE_CONSOLE_URL</var>
   - `Logging network request trace: `<var translate="no">URL</var>
5. Click on the URL to view your data in the Firebase console. It may take a few moments for the data to update in the dashboard.

If your app isn't logging performance events, review the[troubleshooting tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=android#app-not-logging-events).

## **Step 5** :*(Optional)*Add custom monitoring for specific code

To monitor performance data associated with specific code in your app, you can instrument[**custom code traces**](https://firebase.google.com/docs/perf-mon/custom-code-traces).

With a custom code trace, you can measure how long it takes your app to complete a specific task or set of tasks, such as loading a set of images or querying your database. The default metric for a custom code trace is its duration, but you can also add custom metrics, such as cache hits and memory warnings.

In your code, you define the beginning and the end of a custom code trace (and add any desired custom metrics) using the API provided by thePerformance MonitoringSDK. For Android apps, you can also monitor the duration of specific methods using[@AddTrace annotation](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=android#add-trace-annotation).

Visit[Add monitoring for specific code](https://firebase.google.com/docs/perf-mon/custom-code-traces)to learn more about these features and how to add them to your app.

## **Step 6**: Deploy your app then review results

After you've validatedPerformance Monitoringusing one or more test devices, you can deploy the updated version of your app to your users.

You can monitor performance data in the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole.

## Known issues

- ThePerformance MonitoringGradle plugin v1.1.0 can cause a mismatch in Guava dependencies, resulting in the following error:

  ```
  Error:Execution failed for task ':app:packageInstantRunResourcesDebug'.
  > com.google.common.util.concurrent.MoreExecutors.directExecutor()Ljava/util/concurrent/Executor;
  ```

  If you see this error, you can either:
  - Upgrade thePerformance Monitoringplugin to v1.1.1 or later (the most recent is v2.0.2).

  - Replace thePerformance Monitoringplugin dependency line in your**root-level (project-level)** Gradle file (`<project>/build.gradle.kts`or`<project>/build.gradle`), as follows:

    ### Kotlin

    ```kotlin
    buildscript {
      // ...

      dependencies {
        // ...

        // Replace the standard Performance Monitoring plugin dependency line, as follows:
        classpath("com.google.firebase:perf-plugin:1.1.0") {
            exclude(group = "com.google.guava", module = "guava-jdk5")
        }
      }
    }
    ```

    ### Groovy

    ```groovy
    buildscript {
      // ...

      dependencies {
        // ...

        // Replace the standard Performance Monitoring plugin dependency line, as follows:
        classpath('com.google.firebase:perf-plugin:1.1.0') {
            exclude group: 'com.google.guava', module: 'guava-jdk5'
        }
      }
    }
    ```
- Performance Monitoringreports the total payload size for HTTP network requests based on the value set in the HTTP content-length header. This value might not always be accurate.

- Performance Monitoringonly supports the main process in multi-process Android apps.

## Next steps

- Review and run the[Performance MonitoringAndroid code sample on GitHub](https://github.com/firebase/quickstart-android/tree/master/perf).

- Learn more about data automatically collected byPerformance Monitoring:

  - Data related to your app's lifecycle, like[app start time](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces?platform=android)
  - Data for[screen rendering](https://firebase.google.com/docs/perf-mon/screen-traces?platform=android)in your app
  - Data for[HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces?platform=android)issued by your app
- [View, track, and filter](https://firebase.google.com/docs/perf-mon/console?platform=android)your performance data in theFirebaseconsole.

- Add monitoring for specific tasks or workflows in your app by[instrumenting custom code traces](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=android).

- [Use attributes to filter performance data](https://firebase.google.com/docs/perf-mon/attributes?platform=android).