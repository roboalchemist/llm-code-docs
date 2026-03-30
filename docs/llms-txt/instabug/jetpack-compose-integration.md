# Source: https://docs.instabug.com/android/set-up-luciq-for-android/integrate-luciq-on-android/jetpack-compose-integration.md

# Jetpack Compose Integration

This guide provides instructions on how to integrate Luciq's Bug Reporting, Crash Reporting, and App Performance Monitoring features into your Jetpack Compose application. Following these steps, you can capture and report bugs and crashes from your Compose UI.

### Integration Methods

There are two ways to integrate Jetpack Compose with Luciq:

* Automatic Approach - We detect the screens if you are using the Compose Navigation library.
* Manual Approach - You define each screen using an API.

#### Common Integration Steps

For both the manual and automatic approach, you must use these common integration steps:

**For Bug Reporting & Crash Reporting only**

```
implementation "androidx.compose.ui:ui:$compose_version" 
implementation "ai.luciq.library:luciq-compose:x.x.x"
```

**For Bug Reporting, Crash Reporting, & APM**

```
implementation "androidx.compose.ui:ui:$compose_version" 
implementation "androidx.compose.foundation:foundation:$compose_version" 
implementation "ai.luciq.library:luciq-compose-apm:x.x.x"
```

{% hint style="info" %}

### Minimum & Maximum Compose UI and Foundation versions

The minimum supported compose.ui and compose.foundation version is 1.1.0, and the maximum supported version is 1.5.0 for SDKs below 13.0.0. Starting from SDK version 13.0.0 the minimum supported compose.ui and compose foundation versions 1.5.0.
{% endhint %}

{% hint style="danger" %}
All compose.ui and compose.foundation versions below 1.1.0 are not supported and using them may cause your app to crash.
{% endhint %}

{% hint style="warning" %}

### For APM:

The SDK will be responsible for laying out the application’s UI to be able to measure the performance of the composable screen.

LuciqScreen is a UI composable that could be considered a Box UI, as it provides Box scope to its children. It has the below signature:

`fun LuciqScreen(screenName: String, modifier: Modifier = Modifier, content: @Composable BoxScope.() -> Unit)`
{% endhint %}

### Automatic Approach

{% hint style="info" %}

#### For projects using pluginManagement

If your project uses `pluginManagement` in `settings.gradle.kts` (default for new Android projects), configure repositories there:

**settings.gradle.kts:**

```
pluginManagement {
    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
```

Then in your **project-level** `build.gradle.kts`, use the plugins block:

```
plugins {
    id("ai.luciq.library") version "x.x.x" apply false
}
```

{% endhint %}

{% hint style="info" %}

### Please note that the Automatic Approach only works if you are using the Compose Navigation library.

{% endhint %}

If you are using Compose Navigation, you can capture Compose View Names, User Interactions and their performance out-of-the-box without any code change. You will just need to add these configurations to your Gradle - `build.gradle` file:

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
classpath "ai.luciq.library:luciq-plugin:x.x.x"

plugins { 
id 'com.android.application' 
id 'luciq' }

luciq {
setCaptureComposeNavigationDestinations(true)
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

To enrich the data captured in user Interactions (User Steps and Repro steps), please apply Luciq's compiler extension plugin In app build.grade and configure the [compatible extension version to the Kotlin version used:](https://docs.luciq.ai/android/set-up-luciq-for-android/kotlin-compilers-compatibility)

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
plugins {
    ........
    id 'luciq-compiler-extension'
}
luciq {
    compilerExtension {
        version = "x.y.z"
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Configuration Block

You can configure the compiler extension as follows:

{% code overflow="wrap" %}

```
luciq {
    compilerExtension {
        version = "x.y.z" // the compiler extension version to use
        enableComposeAutoTagging = {true/false} // whether to enable or disable Composable(s) auto tagging
        enableDebugLogs = {true/false} // whether to enable debug logs
        suppressCompatibilityCheck = {true/false} // whether to bypass compatibility checkor not
    }
}
```

{% endcode %}

{% hint style="success" %}

### Minimum & Maximum Compose Navigation versions

For SDKs below 13.0.0, the minimum supported Compose Navigation version is 2.4.0, and the maximum supported version is 2.6.0

Starting from SDK version 13.0.0 till 14.2.1, the minimum supported Compose Navigation version is 2.7.1 and the maximum is 2.7.6.

Starting from SDK version 14.2.1, the minimum supported Compose Navigation version is 2.7.x and the maximum is 2.8.x.
{% endhint %}

### Manual Approach

#### Define Screen Names

In order to track and identify screens in your Compose app, you‘ll need to define screen names using the LuciqScreen function. The screen name will correspond to the current view in your app, and Luciq will use the latest UI component to update screens. This wrapper also controls how your composable appears inside APM.

*Example usage of LuciqScreen in a Compose UI:*

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
@Composable
fun HomeScreen() {
    LuciqScreen(screenName = "Home Screen", showAsScreen = false) {
        Box {
           // Your Compose UI code goes here
        }
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

* `screenName`: This represents the name your compose screen will have on the dashboard. Make sure to use unique screen names for each screen in your app.
* `showAsScreen`: **This is an optional configuration** that controls how your composable will appear inside [Screen Loading](https://docs.instabug.com/docs/android-apm-screen-loading) in [APM](https://docs.instabug.com/docs/android-apm).
  * `false`: This composable loading time will be tracked as a **span inside it’s parent activity or composable**. This is the default behavior if the configuration is not used.
  * `true`: This composable will appear **as it’s own screen** and will have all the details associated with screen loading (e.g. Apdex, P50, P90 ,Spans, etc.)

{% hint style="warning" %}

### **Nesting wrappers can cause duplicate data to be recorded**

It is not recommended to nest manual wrappers with `showAsScreen = "true"`&#x20;
{% endhint %}

{% hint style="warning" %}
`showAsScreen` **configuration is only available starting SDK version 14.3.0**
{% endhint %}

## Private Views

You can easily mark any composable view that might contain sensitive information, i.e.; payment details, as private. Any private view will automatically appear with a black overlay covering it in any screenshot.

To mark any composable as private, you just have to add the `luciqPrivate()` `Modifier` extension to the Composable’s list modifier.

**Example**

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Button(
    onClick = {},
    modifier = Modifier
        .fillMaxWidth(fraction = 0.9f)
        .align(Alignment.CenterHorizontally)
        .luciqPrivate()
){
    Text(text = "I'm a private Button")
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

This will mask the content of any composable in screenshot, repro steps, etc …

### Jetpack Compose Support

We currently **support** the following products:

* Bug Reports
* Crashes
* User Steps that happened inside a Compose View
* Repro steps (including interactions) that happened inside a Compose View
* Private views in JPC
* App launches and screen loading Compose view performance
* Network calls that happen on a Compose view
  * Note that you’ll have to [configure the network metric](https://docs.instabug.com/docs/android-apm-network) separately
* [Auto Masking](https://docs.instabug.com/docs/android-repro-steps#auto-masking) for JPC

{% hint style="success" %}

### Minimum SDK Version

Supporting Jetpack Compose requires a minimum Luciq Android SDK version of 12.1.0.
{% endhint %}
