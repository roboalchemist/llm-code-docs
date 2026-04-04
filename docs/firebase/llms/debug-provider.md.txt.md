# Source: https://firebase.google.com/docs/app-check/android/debug-provider.md.txt

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as an emulator during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider.

> [!WARNING]
> **Warning:** The debug provider allows access to your Firebase resources from unverified devices. **Don't** use the debug provider in production builds of your app, and **don't** share your debug builds with untrusted parties.

## Use the debug provider in an emulator

To use the debug provider while running your app in an emulator interactively
(during development, for example), do the following:

1.

   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the App Check library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.


   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependencies for the App Check libraries
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-appcheck-debug")
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
       // Add the dependencies for the App Check libraries
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-appcheck-debug:19.0.2")
   }
   ```

   <br />

2. In your debug build, configure App Check to use the debug provider
   factory:

   ### Kotlin

   ```kotlin
   Firebase.initialize(context = this)
   Firebase.appCheck.installAppCheckProviderFactory(
       DebugAppCheckProviderFactory.getInstance(),
   )
   ```

   ### Java

   ```java
   FirebaseApp.initializeApp(/*context=*/ this);
   FirebaseAppCheck firebaseAppCheck = FirebaseAppCheck.getInstance();
   firebaseAppCheck.installAppCheckProviderFactory(
           DebugAppCheckProviderFactory.getInstance());
   ```
3. Launch the app and trigger a call to a Firebase backend service. A local
   debug token will be logged when the SDK tries to send a request to the
   backend. For example:

   ```
   D DebugAppCheckProvider: Enter this debug secret into the allow list in
   the Firebase Console for your project: 123a4567-b89c-12d3-e456-789012345678
   ```
4. In the [**App Check**](https://console.firebase.google.com/project/_/appcheck) section
   of the Firebase console, choose **Manage debug tokens** from your app's
   overflow menu. Then, register the debug token you logged in the previous
   step.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)

After you register the token, Firebase backend services will accept it as valid.

Because this token allows access to your Firebase resources without a
valid device, it is crucial that you keep it private. Don't commit it to a
public repository, and if a registered token is ever compromised, revoke it
immediately in the Firebase console.

## Use the debug provider for unit testing in a CI environment

To use the debug provider for unit testing in a continuous integration (CI)
environment, do the following:

1. In the [**App Check**](https://console.firebase.google.com/project/_/appcheck) section
   of the Firebase console, choose **Manage debug tokens** from your app's
   overflow menu. Then, create a new debug token. You'll need the token in the
   next step.

   Because this token allows access to your Firebase resources without
   a valid device, it is crucial that you keep it private. Don't commit it to a
   public repository, and if a registered token is ever compromised, revoke it
   immediately in the Firebase console.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)
2. Add the debug token you just created to your CI system's secure key store
   (for example, GitHub Actions' [encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)
   or Travis CI's [encrypted variables](https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml)).

3. If necessary, configure your CI system to make your debug token available
   within the CI environment as an environment variable. Name the variable
   something like `APP_CHECK_DEBUG_TOKEN_FROM_CI`.

4.

   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the App Check library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.

   ### Kotlin


   ```kotlin
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the App Check library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-appcheck-debug")
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
       // Add the dependency for the App Check library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-appcheck-debug:19.0.2")
   }
   ```

   <br />

   ### Java


   ```java
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the App Check library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-appcheck-debug")
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
       // Add the dependency for the App Check library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-appcheck-debug:19.0.2")
   }
   ```

   <br />

5. Add the following to the configuration of your CI build variant:

       testInstrumentationRunnerArguments["firebaseAppCheckDebugSecret"] =
           System.getenv("APP_CHECK_DEBUG_TOKEN_FROM_CI") ?: ""

6. In your test classes, use the `DebugAppCheckTestHelper` to wrap any code
   that needs an App Check token:

   ### Kotlin

       @RunWith(AndroidJunit4::class)
       class MyTests {
           private val debugAppCheckTestHelper =
               DebugAppCheckTestHelper.fromInstrumentationArgs()

           @Test
           fun testWithDefaultApp() {
               debugAppCheckTestHelper.withDebugProvider {
                   // Test code that requires a debug AppCheckToken.
               }
           }

           @Test
           fun testWithNonDefaultApp() {
               debugAppCheckTestHelper.withDebugProvider(
                   FirebaseApp.getInstance("nonDefaultApp")
               ) {
                   // Test code that requires a debug AppCheckToken.
               }
           }
       }

   ### Java

       @RunWith(AndroidJunit4.class)
       public class YourTests {
           private final DebugAppCheckTestHelper debugAppCheckTestHelper =
                   DebugAppCheckTestHelper.fromInstrumentationArgs();

           @Test
           public void testWithDefaultApp() {
               debugAppCheckTestHelper.withDebugProvider(() -> {
                   // Test code that requires a debug AppCheckToken.
               });
           }

           @Test
           public void testWithNonDefaultApp() {
               debugAppCheckTestHelper.withDebugProvider(
                       FirebaseApp.getInstance("nonDefaultApp"),
                       () -> {
                           // Test code that requires a debug AppCheckToken.
                       });
           }
       }

When your app runs in a CI environment, Firebase backend services will accept
the token it sends as valid.