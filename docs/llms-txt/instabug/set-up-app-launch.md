# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-app-launch.md

# Set up App Launch

### Cold App Launch

Luciq automatically measures your **cold app launch** latency, which is the time between when your user launches the app from scratch and when it is responsive and accepting touch events.

It starts after Luciq's `ContentProvider` is created and ends when `onActivityResumed()` is called for the first time.

#### Disabling/Enabling App Launch Tracking

If APM is enabled, our SDK starts collecting data about your cold app launch time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.setColdAppLaunchEnabled(true)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.setColdAppLaunchEnabled(true);
```

{% endcode %}
{% endtab %}
{% endtabs %}

***

### Hot App Launch

The Luciq SDK automatically measures the **hot app launch** latency, which is the time between the user launching the app from the background until it's responsive and accepting touch events.

Hot Launch is transitioning the app from the background to the foreground-active state. We capture the Hot Launch event by monitoring the `Application.ActivityLifecycleCallbacks`. It starts with `onActivityStarted()` and ends with `onActivityResumed()` .

#### Disabling/Enabling Hot App Launch Tracking

If APM is enabled, our SDK starts collecting data about your hot app launch time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.setHotAppLaunchEnabled(true)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.setHotAppLaunchEnabled(true);
```

{% endcode %}
{% endtab %}
{% endtabs %}

***

### Warm App Launch

The Luciq SDK automatically measures the **warm app launch** latency, which is somewhere between a cold and hot launch, where some of the operations that take place in a cold launch are still happening.

We capture the Warm Launch event by monitoring the `Application.ActivityLifecycleCallbacks`. It starts with `onActivityCreate()` and ends with `onActivityResumed()`.

#### Disabling/Enabling Warm App Launch Tracking

If APM is enabled, our SDK starts collecting data about your warm app launch time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.setWarmAppLaunchEnabled(true)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.setWarmAppLaunchEnabled(true);
```

{% endcode %}
{% endtab %}
{% endtabs %}

***

### End App Launch

In the event that you'd like to define a specific point in time where the app launch can be considered complete, such as when the app is actually interactable, you can use the end app launch API to set that point. You'll then be able to see this data alongside the automatic cold and hot app launches that were captured.

To use the End App Launch API, you'll just need to call the following method:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.endAppLaunch()
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.endAppLaunch();
```

{% endcode %}
{% endtab %}
{% endtabs %}
