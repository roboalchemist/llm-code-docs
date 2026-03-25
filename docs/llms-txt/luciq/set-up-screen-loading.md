# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-screen-loading.md

# Set up Screen Loading

Luciq automatically captures the time it takes for any given screen to load. This covers the time for any Activity between `onCreate` and `onResume` which includes the following lifecycle methods:

* `onCreate`
* `onStart`
* `onResume`

### End Screen Loading

You can also define custom points in each Activity to manually inform the SDK that screen loading has ended.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.endScreenLoading(Class<T> activityClass)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.endScreenLoading(YourActivity.class);
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Jetpack Compose Screen Loading

If you’re using Jetpack Compose and want to measure the loading time of your Composables, you need to complete [Luciq's Jetpack Compose Integration](https://docs.luciq.ai/android/set-up-luciq-for-android/integrate-luciq-on-android/jetpack-compose-integration). Once Integrated, Composable loading times will start appearing in you Screen Loading metric.

#### Composables as Spans

By default, Composables will appear as spans within their parent Activities.

* You can track the loading time of each composable in the spans table of it’s parent screen.
* You can see individual composable occurrences as spans inside the occurrence page of their parent scree, in the spans timeline.

#### Composables as Screens

{% hint style="warning" %}

### Min SDK Version

Configuring Composables to appear as separate screens is supported starting Android SDK version 14.3.0
{% endhint %}

**If you use composables as entire screens** (not just components), you can configure Composables. to appear in the dashboard as their own screens instead of as spans within their parent activities. This is configured through the `showAsSceen` property of the `IBGScreen` wrapper of the Jetpack Compose manual instrumentation approach.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
@Composable
fun HomeScreen() {
    IBGScreen(screenName = "Home Screen", showAsScreen = false) { 
        Box {
           // Your Compose UI code goes here
        }
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

`showAsScreen`: **This is an optional configuration** that controls how your composable will appear inside [Screen Loading](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-screen-loading) in [APM](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring).

* `false`: This composable loading time will be tracked as a **span inside it’s parent activity or composable**. This is the default behavior if the configuration is not used.
* `true`: This composable will appear **as it’s own screen** and will have all the details associated with screen loading (e.g. Apdex, P50, P90 ,Spans, etc.)

{% hint style="warning" %}

### This configuration is only supported through the manual instrumentation wrapper for now

If you are using the automatic instrumentation, adding the manual wrapper to your composables might cause duplicate data to be reported. We’re working to build support for the automatic instrumentation soon.
{% endhint %}

### Disabling/Enabling Screen Loading Tracking

If APM is enabled, our SDK starts collecting data about your screen loading time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.setScreenLoadingEnabled(boolean enabled)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.setScreenLoadingEnabled(boolean enabled);
```

{% endcode %}
{% endtab %}
{% endtabs %}
