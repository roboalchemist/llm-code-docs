# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-bug-reporting/extended-bug-report-for-android.md

# Extended Bug Report for Android

### What is an Extended Bug Report?

Free-form comments from reporters can be time-consuming to read through when triaging bugs. The Extended Bug Report standardizes all of your bug reports with additional fields that are commonly used by QA and technical beta testers: steps to reproduce the bug, actual results, and expected results.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FpEMHsclvGe6gQxsrsIxT%2Fimage.png?alt=media&#x26;token=9ab5bfb8-ff8e-40c7-b39f-929a2b69a2f6" alt=""><figcaption></figcaption></figure>

If enabled, the Extended Bug Report adds a second step to the bug reporting flow that your testers experience in your app.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FtdhJ6uuSQussYBRbJ1q0%2Fimage.png?alt=media&#x26;token=8a5ba88e-71d7-4f04-b892-e10787d52569" alt=""><figcaption><p><br><em>The Extended Bug Report includes additional fields for your testers to complete when sending reports.</em></p></figcaption></figure>

### Enabling the Extended Bug Report

By default, the Extended Bug Report mode is disabled. When enabling the Extended Bug Report, you can set whether the additional fields are required or optional.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
BugReporting.setExtendedBugReportState(ExtendedBugReport.State.ENABLED_WITH_REQUIRED_FIELDS)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
BugReporting.setExtendedBugReportState(ExtendedBugReport.State.ENABLED_WITH_REQUIRED_FIELDS);
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here are the possible modes you can set for Extended Bug Reports.

{% tabs %}
{% tab title="Android" %}
{% code overflow="wrap" %}

```java
//Disable extended bug report mode
ExtendedBugReport.State.DISABLED
//Enable extended bug report mode and make all additional fields required 
ExtendedBugReport.State.ENABLED_WITH_REQUIRED_FIELDS
//Enable extended bug report mode and make all additional fields optional
ExtendedBugReport.State.ENABLED_WITH_OPTIONAL_FIELDS
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Override Placeholder Values

You can also override each placeholder within the Extended Bug Reports using the following method.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Luciq.setExtendedBugReportHints("Hint1", "Hint2", "Hint3")
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Luciq.setExtendedBugReportHints("Hint1", "Hint2", "Hint3");
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Passing `null` as one of the parameters will not affect in modifying the original placeholder.
{% endhint %}
