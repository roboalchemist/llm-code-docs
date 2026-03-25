# Source: https://docs.logrocket.com/reference/android.md

# Initialize SDK

Call `init()` with your appID to configure and start LogRocket. You can find your appID on [https://app.logrocket.com](https://app.logrocket.com) under Settings > Project Setup.

##

### Configure Gradle

The LogRocket Android SDK is distributed through Maven. To include the SDK in your application add our Maven repository in your `settings.gradle` or `app/build.gradle` file. Then, declare the logrocket dependency in your `app/build.gradle` file. New releases of the LogRocket Native SDKs are catalogued on our [Mobile SDK Changelog](https://docs.logrocket.com/docs/mobile-sdk-changelog).

```groovy
repositories {
    // Add this declaration to any existing repositories block.
    maven { url "https://storage.googleapis.com/logrocket-maven/" }
}

dependencies {
    // Add this declaration to any existing dependencies block.
    implementation "com.logrocket:logrocket:[1.0, 2.0)"
}
```

```kotlin
repositories {
    // Add this declaration to any existing repositories block.
    maven { url = uri("https://storage.googleapis.com/logrocket-maven/") }
}

dependencies {
    // Add this declaration to any existing dependencies block.
    implementation("com.logrocket:logrocket:[1.0, 2.0)")
}
```

### Initializing the SDK

The LogRocket Android SDK must be initialized with an `Application` instance and a fully attached `Context` for the application. The simplest way to initialize the SDK is from a custom `Application` class in the `attachBaseContext` method.

Replace `<APP_SLUG>` with your LogRocket application slug, located in our [dashboard's quick start guides](https://app.logrocket.com/r/settings/setup).

```java
import android.app.Application;
import com.logrocket.core.SDK;

public class App extends Application {
  @Override
  protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);

    SDK.init(
      this,
      base,
      options -> {
        options.setAppID("<APP_SLUG>");
      }
    );
  }
}
```

If you did not already have an existing custom Application class, add the name of the class as the `android:name` property for the `<application>` node in `AndroidManifest.xml`:

```xml
<application
  android:name=".App"
  ..>
```

### Supported Android Versions

The LogRocket Android SDK supports Android API 25 (Nougat) through Android API 35 (Vanilla Ice Cream).