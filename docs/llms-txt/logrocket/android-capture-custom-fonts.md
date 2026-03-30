# Source: https://docs.logrocket.com/reference/android-capture-custom-fonts.md

# Capture Custom Fonts

Android instructions to capture custom font files for display in session replay. Includes React Native on Android.

If you use [custom fonts](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml), and notice missing icons or incorrectly sized text in Session Replay, you may want to follow these instructions to upload your fonts on release builds. This will enable custom fonts to display in Session Replay. Custom font replay requires a minimum SDK version of 1.33.8.

# Install plugin

Include the following in your gradle build file

```kotlin build.gradle.kts
buildscript {
    repositories {
        // Existing repositories
        maven {
            url = uri("https://storage.googleapis.com/logrocket-maven/")
        }
    }
    dependencies {
        // Existing dependencies
        classpath("com.logrocket.gradle:android:0.4.0")
    }
}
```

```groovy build.gradle
buildscript {
  repositories {
    // Existing repositories
    maven { url "https://storage.googleapis.com/logrocket-maven/" }
  }
  dependencies {
    // Existing dependencies
    classpath "com.logrocket.gradle:android:0.3.1"
  }
}
```

## Apply the Plugin

Adding the dependency is not enough to activate the plugin. The following must also be added to your application's gradle build file

```kotlin build.gradle.kts
plugins {
    id("com.android.application") // Should already exist, our plugin must be added after this plugin.
    id("com.logrocket.gradle.android")
}
```

```groovy build.gradle
apply plugin: 'com.android.application' // Should already exist, must add our plugin after this.
apply plugin: 'com.logrocket.gradle.android'
```

# Authorization

Include your API key (found in `General Settings > Development > API key`) in one of two approaches: through an environment variable or directly in your application's gradle file.

## as an environment variable

The API key can be set as an environment variable, such as through your CI system, so you do not need to commit the key to your repository.

```Text .env
LOGROCKET_API_KEY=<org:app:key>
```

## in your application's gradle build file

```kotlin build.gradle.kts
logrocket {
    apiKey = "<org:app:key>"
}
```

```groovy build.gradle
logrocket {
    apiKey = "<org:app:key>"
}
```

# Additional Configuration

By default, the android plugin is only applied for production builds. If you would like to test it on another build variant you may specify a list of variants in your application's gradle build file.

```kotlin build.gradle.kts
logrocket {
    enabledVariants = setOf("debug", "release")
}
```

```groovy build.gradle
logrocket {
    enabledVariants = ["debug", "release"].toSet()
}
```

# Font resource location

[Font Resources](https://developer.android.com/guide/topics/resources/font-resource) are captured if the font exists in `app/src/main/res/fonts` (or a sub-folder).

For React Native we will capture fonts that have been installed into the Android application at `android/app/src/main/assets/fonts`.

If your app has custom fonts stored in any other location (i.e. in a separate project) then you can use the following configuration in your application's gradle build file to specify those directories:

```kotlin build.gradle.kts
logrocket {
    assetDirs = setOf("custom-font/src/main/res/font")
}
```

```groovy build.gradle
logrocket {
    assetDirs = [ "custom-font/src/main/res/font" ].toSet()
}
```