# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-crash-reporting/crash-reporting-callbacks.md

# Crash Reporting Callbacks

{% hint style="warning" %}

### Avoiding Memory Leaks

These APIs hold the callbacks in a strong reference, so we strongly suggest to avoid registering callbacks without unregistering them when needed, as it may cause a memory leak.
{% endhint %}

### Before Sending a Report

This block is executed in the background before sending each report. You can use it to attach logs and extra data to reports.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Luciq.onReportSubmitHandler{report -> }
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Luciq.onReportSubmitHandler(new Report.OnReportCreatedListener() {
            @Override
            public void onReportCreated(Report report) {
                
            }
        };
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Exporting Crash Metadata

You can use the below API to capture metadata about the crash including:

* **Error Type**: The error type including **ANR** (Foreground ANR), **BG\_ANR** (Background ANR), **Non-fatal** errors and **NDK crashes**.
* **Error Code**: The specific error code associated with the crash.
* **User Attributes**: User attributes associated with the session.
* **Error Description**: The error message associated with the crash

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
CrashReporting.setOnCrashSentCallback
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
CrashReporting.setOnCrashSentCallback
```

{% endcode %}
{% endtab %}
{% endtabs %}
