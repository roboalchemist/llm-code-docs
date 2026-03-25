# Source: https://docs.logrocket.com/reference/android-sdk-20.md

# Android SDK 2.0

## What's new?

LogRocket Android SDK v2 takes a new approach to view capture in order to improve session replay fidelity. Compared to v1, Android SDK v2 offers **higher-frame-rate** session replays that are **more fluid, responsive, and complete**.

Jetpack Compose support is now available as a separate dependency from the main LogRocket SDK.

## How to upgrade

If your app does not use Jetpack Compose, all that is needed is to update your `app/build.gradle` to use the latest 2.x.x version of LogRocket.

```groovy build.gradle
dependencies {
  implementation "com.logrocket:logrocket:[2.0, 3.0)"
}
```

```kotlin build.gradle.kts
dependencies {
  implementation("com.logrocket:logrocket:[2.0, 3.0)")
}
```

All replay features, including redaction, remain consistent with v1, and no action is needed to adjust them.

### Jetpack Compose

If your app uses Jetpack Compose, support is available via a separate dependency, which can be included in your  `app/build.gradle`.

```groovy build.gradle
dependencies {
  implementation "com.logrocket:logrocket:[2.0, 3.0)"
  implementation "com.logrocket:compose:[2.0, 3.0)"
}
```

```kotlin build.gradle.kts
dependencies {
  implementation("com.logrocket:logrocket:[2.0, 3.0)")
  implementation("com.logrocket:compose:[2.0, 3.0)")
}
```

If you specify a specific version of the LogRocket SDK to use, make sure to use the same version for both dependencies.

```groovy build.gradle
ext {
  logRocketVersion = "2.x.x"
}

dependencies {
  implementation "com.logrocket:logrocket:${logRocketVersion}"
  implementation "com.logrocket:compose:${logRocketVersion}"
}
```

```kotlin build.gradle.kts
dependencies {
  val logRocketVersion = "2.x.x"

  implementation("com.logrocket:logrocket:${logRocketVersion}")
  implementation("com.logrocket:compose:${logRocketVersion}")
}
```

### React Native

If your app uses React Native, then you can take advantage of these new improvements by upgrading to the latest 2.x.x version of the [LogRocket React Native SDK](https://www.npmjs.com/package/@logrocket/react-native) package. This will automatically update the Android native layer of your React Native app to use the new v2 Android SDK.

### Notes on Performance

LogRocket Android SDK v2 achieves higher frame rate by caching more view processing information. Because of these caches, you may see a small increase in memory usage by the LogRocket SDK when upgrading.

As was the case in v1, LogRocket view capture will never use more than 10% of main thread execution time in any given second.

### How to get in touch

Please reach out to `support@logrocket.com` if you have any concerns about LogRocket Android SDK v2. If you would like to disable the new view capture approach after upgrading, you can do so by setting init config option `options.setEnableViewCaptureV2(false)`.

<br />