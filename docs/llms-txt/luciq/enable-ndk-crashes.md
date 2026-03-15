# Source: https://docs.luciq.ai/references/crash-reporting/enable-or-disable-crash-reporting/enable-ndk-crashes.md

# Enable NDK Crashes

In order to start capturing NDK crashes, you'll need to add the below dependency to your app-level gradle.

{% tabs fullWidth="true" %}
{% tab title="Gradle" %}

```java
implementation 'com.luciq.library:luciq-ndk-crash:11.8.0'
```

{% endtab %}
{% endtabs %}

```groovy
implementation 'com.luciq.library:luciq-ndk-crash:11.8.0'
```

NDK crash reporting is disabled by default if the NDK dependency is added; however, it can be enabled using the below method.

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
CrashReporting.setNDKCrashesState(Feature.State.ENABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
CrashReporting.setNDKCrashesState(Feature.State.ENABLED)

```

{% endtab %}
{% endtabs %}

> 📘 **16KB Compatibility**
>
> From Android 15 (API 35), native (.so) libraries must support 16KB page sizes. Luciq supports this starting from version **13.4.0**. Please upgrade if your app targets Android 15+ to avoid crashes. [Learn more](https://developer.android.com/guide/practices/page-sizes?hl=en).
