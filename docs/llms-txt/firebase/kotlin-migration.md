# Source: https://firebase.google.com/docs/android/kotlin-migration.md.txt

<br />

Firebase is increasing its commitment to Kotlin, and we're working to modernize our Android ecosystem to make Kotlin more accessible and easy-to-use with Firebase.

To accomplish this modernization, we're making a few changes to our Firebase SDKs for Android. This page describes important information about this change, including:

- [What's changing](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-whats-changing)
- [The reason we're making this change](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-why-making-change)
- [Important dates for this change](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-important-dates)
- [How to migrate to use KTX APIs from the main module](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-how-to-migrate)

<br />

[Learn how to migrate your app](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-how-to-migrate)
| In[July 2025](https://firebase.google.com/support/release-notes/android#2025-07-21), we stopped releasing new versions of the KTX modules and removed the KTX libraries from theFirebase Android BoM(v34.0.0).

## What's changing?

The Kotlin extensions (KTX) APIs have been added to their respective main modules. For example, all the APIs from`firebase-perf-ktx`have been added to`firebase-perf`under the`com.google.firebase.perf`package.

**This change means that Kotlin developers can now depend on the main modules instead of the KTX modules** (when using[Firebase BoMv32.5.0+](https://firebase.google.com/support/release-notes/android#bom_v32-5-0)or main module versions listed inBoMv32.5.0+).

In July 2025, we stopped releasing new versions of the KTX modules and removed the KTX libraries from theFirebase Android BoM(v34.0.0).
| **Note:** Any currently or previously released versions of the KTX modules orBoMwill still function.  
| However, we recommend that you[migrate your app to use KTX APIs from the main module](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-how-to-migrate)to ensure that you continue to get fixes and can take advantage of changes and new features now that new versions of the KTX modules are no longer released.

## Why are we making this change?

Firebase is committed to a[Kotlin-first](https://developer.android.com/kotlin/first)ecosystem for Android developers. This packaging modernization provides the following advantages:

- **Simplified dependency management:**You now only need to depend on a single module, eliminating the need to switch between the main module and the Kotlin extensions or to depend on both.

- **Enhanced Kotlin support:**All of our Firebase SDKs for Android will now provide better support for Kotlin. We'll include all the new Kotlin-friendly features directly in our main modules.

## Important dates for this change

| We recommend that you[migrate your app to use KTX APIs from the main module](https://firebase.google.com/docs/android/kotlin-migration#ktx-apis-to-main-how-to-migrate)to ensure that you continue to get fixes and can take advantage of changes and new features now that the KTX modules are no longer released.

#### **In October 2023**

In October 2023, the Kotlin extensions (KTX) APIs were added to their respective main modules, which means that you can now use the KTX APIs directly from the main modules when using[Firebase BoMv32.5.0+](https://firebase.google.com/support/release-notes/android#bom_v32-5-0)or main module versions listed inBoMv32.5.0+.

In parallel, the Kotlin extension (KTX) APIs*in the KTX modules* were deprecated (see the[release notes](https://firebase.google.com/support/release-notes/android#2023-10-30)describing this change). During the[deprecated phase](https://firebase.google.com/policies/changes-to-firebase/introducing-and-communicating-changes#deprecated-phase), the deprecated APIs in the KTX modules will continue to function and be maintained.

#### **In July 2025**

In July 2025, we stopped releasing new versions of the KTX modules, and we removed the KTX modules from theFirebase BoM(starting with[BoMv34.0.0](https://firebase.google.com/support/release-notes/android#bom_v34-0-0)).

Any previously released version of a KTX module or theBoMwill continue to function, but they're now[end-of-maintenance](https://firebase.google.com/policies/changes-to-firebase/introducing-and-communicating-changes#end-of-maintenance). This means that we won't add bug fixes, backwards-compatible changes, or new features to the KTX modules. Instead, all future development for Firebase on Android will only be done in the*main modules*(for both Java and Kotlin).

## How to migrate to use KTX APIs from the main modules

If you use Kotlin extensions (KTX) APIs, make the following updates in your app to start using the APIs from the main modules instead of the KTX modules.

1. Revise your Gradle dependencies to rely on the main module rather than the KTX module. For example, if you use theFirebase Android BoM*(recommended)*:

   **BEFORE**  

   ```kotlin
   dependencies {
     // ...

     // Import the Firebase BoM
     implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

     // Using KTX libraries for Authentication and Cloud Firestore
     implementation("com.google.firebase:firebase-auth-ktx")
     implementation("com.google.firebase:firebase-firestore-ktx")
   }
   ```

   **AFTER**  

   ```kotlin
   dependencies {
     // ...

     // Import the Firebase BoM as usual
     // Make sure to use https://firebase.google.com/support/release-notes/android#bom_v32-5-0 or higher
     implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

     // No need to use the KTX libraries; everything is now in the main module
     implementation("com.google.firebase:firebase-auth")
     implementation("com.google.firebase:firebase-firestore")
   }
   ```

   <br />

   **If you don't use theFirebase Android BoM**

   <br />

   **BEFORE**  

   ```kotlin
   dependencies {
     // ...

     // Using KTX libraries for Authentication and Cloud Firestore
     implementation("com.google.firebase:firebase-auth-ktx:23.2.1")
     implementation("com.google.firebase:firebase-firestore-ktx:25.1.4")
   }
   ```

   **AFTER**  

   ```kotlin
   dependencies {
     // ...

     // No need to use the KTX libraries, everything is now in the main module
     // Make sure to use a version listed in https://firebase.google.com/support/release-notes/android#bom_v32-5-0 or higher
     implementation("com.google.firebase:firebase-auth:24.0.1")
     implementation("com.google.firebase:firebase-firestore:26.0.2")
   }
   ```

   <br />

   <br />

   <br />

2. Update your code to replace all occurrences of the KTX APIs with the relocated APIs in the main module under the`com.google.firebase`package.

   **BEFORE**  

   ```kotlin
   import com.google.firebase.auth.ktx.auth
   import com.google.firebase.firestore.ktx.firestore
   import com.google.firebase.firestore.ktx.toObject
   import com.google.firebase.ktx.Firebase
   ```

   **AFTER**  

   ```kotlin
   import com.google.firebase.auth.auth
   import com.google.firebase.firestore.firestore
   import com.google.firebase.firestore.toObject
   import com.google.firebase.Firebase
   ```