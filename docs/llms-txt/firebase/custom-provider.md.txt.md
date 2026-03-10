# Source: https://firebase.google.com/docs/app-check/android/custom-provider.md.txt

This page shows you how to enable App Check in an Android app, using [your
custom App Check provider](https://firebase.google.com/docs/app-check/android/custom-provider). When you enable App Check,
you help ensure that only your app can access your project's Firebase resources.

If you want to use App Check with the default Play Integrity provider, see
[Enable App Check with Play Integrity on Android](https://firebase.google.com/docs/app-check/android/play-integrity-provider).

## Before you begin

- [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup) if you haven't
  already done so.

- [Implement your custom App Check provider's server-side logic](https://firebase.google.com/docs/app-check/custom-provider).

## 1. Add the App Check library to your app

In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the App Check library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

<br />

```
dependencies {
    // Import the BoM for the Firebase platform
    implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

    // Add the dependency for the App Check library
    // When using the BoM, you don't specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-appcheck")
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
    implementation("com.google.firebase:firebase-appcheck:19.0.2")
}
```

<br />

## 2. Implement the App Check interfaces

First, you need to create classes that implement the `AppCheckProvider` and
`AppCheckProviderFactory` interfaces.

Your `AppCheckProvider` class must have a `getToken()` method, which collects
whatever information your custom App Check provider requires as proof of
authenticity, and sends it to your token acquisition service in exchange for an
App Check token. The App Check SDK handles token caching, so always get
a new token in your implementation of `getToken()`.

### Kotlin

```kotlin
class YourCustomAppCheckToken(
    private val token: String,
    private val expiration: Long,
) : AppCheckToken() {
    override fun getToken(): String = token
    override fun getExpireTimeMillis(): Long = expiration
}

class YourCustomAppCheckProvider(firebaseApp: FirebaseApp) : AppCheckProvider {
    override fun getToken(): Task<AppCheckToken> {
        // Logic to exchange proof of authenticity for an App Check token and
        //   expiration time.
        // ...

        // Refresh the token early to handle clock skew.
        val expMillis = expirationFromServer * 1000L - 60000L

        // Create AppCheckToken object.
        val appCheckToken: AppCheckToken = YourCustomAppCheckToken(tokenFromServer, expMillis)
        return Tasks.forResult(appCheckToken)
    }
}
```

### Java

```java
public class YourCustomAppCheckToken extends AppCheckToken {
    private String token;
    private long expiration;

    YourCustomAppCheckToken(String token, long expiration) {
        this.token = token;
        this.expiration = expiration;
    }

    @NonNull
    @Override
    public String getToken() {
        return token;
    }

    @Override
    public long getExpireTimeMillis() {
        return expiration;
    }
}

public class YourCustomAppCheckProvider implements AppCheckProvider {
    public YourCustomAppCheckProvider(FirebaseApp firebaseApp) {
        // ...
    }

    @NonNull
    @Override
    public Task<AppCheckToken> getToken() {
        // Logic to exchange proof of authenticity for an App Check token and
        //   expiration time.
        // ...

        // Refresh the token early to handle clock skew.
        long expMillis = expirationFromServer * 1000L - 60000L;

        // Create AppCheckToken object.
        AppCheckToken appCheckToken =
                new YourCustomAppCheckToken(tokenFromServer, expMillis);

        return Tasks.forResult(appCheckToken);
    }
}
```

Also, implement a `AppCheckProviderFactory` class that creates instances of your
`AppCheckProvider` implementation:

### Kotlin

```kotlin
class YourCustomAppCheckProviderFactory : AppCheckProviderFactory {
    override fun create(firebaseApp: FirebaseApp): AppCheckProvider {
        // Create and return an AppCheckProvider object.
        return YourCustomAppCheckProvider(firebaseApp)
    }
}
```

### Java

```java
public class YourCustomAppCheckProviderFactory implements AppCheckProviderFactory {
    @NonNull
    @Override
    public AppCheckProvider create(@NonNull FirebaseApp firebaseApp) {
        // Create and return an AppCheckProvider object.
        return new YourCustomAppCheckProvider(firebaseApp);
    }
}
```

## 3. Initialize App Check

Add the following initialization code to your app so that it runs before you use
any other Firebase SDKs:

### Kotlin

```kotlin
Firebase.initialize(context)
Firebase.appCheck.installAppCheckProviderFactory(
    YourCustomAppCheckProviderFactory(),
)
```

### Java

```java
FirebaseApp.initializeApp(/*context=*/ context);
FirebaseAppCheck firebaseAppCheck = FirebaseAppCheck.getInstance();
firebaseAppCheck.installAppCheckProviderFactory(
        new YourCustomAppCheckProviderFactory());
```

## Next steps

Once the App Check library is installed in your app, start distributing the
updated app to your users.

The updated client app will begin sending App Check tokens along with every
request it makes to Firebase, but Firebase products will not require the tokens
to be valid until you enable enforcement in the App Check section of the
Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't
disrupt your existing legitimate users. On the other hand, if you're seeing
suspicious use of your app resources, you might want to enable enforcement
sooner.

To help make this decision, you can look at App Check metrics for the
services you use:

- [Monitor App Check request metrics](https://firebase.google.com/docs/app-check/monitor-metrics) for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [Monitor App Check request metrics for Cloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### Enable App Check enforcement

When you understand how App Check will affect your users and you're ready to
proceed, you can enable App Check enforcement:

- [Enable App Check enforcement](https://firebase.google.com/docs/app-check/enable-enforcement) for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [Enable App Check enforcement for Cloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### Use App Check in debug environments

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as an emulator during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider.

See [Use App Check with the debug provider on Android](https://firebase.google.com/docs/app-check/android/debug-provider).