# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-crash-reporting/reporting-crashes-for-android.md

# Reporting Crashes For Android

## Automatic Crash Reporting

If you enable Crash Reporting, crashes will automatically be reported to and viewable from the crashes page of your Luciq dashboard.

You'll also see the trends covering the previous 7 days, including:

* Crash-free sessions: the percentage of sessions that ran and concluded without any fatal errors.
* Crash-free users: the percentage of users that haven't encountered any fatal errors.
* Crashing sessions: the number of sessions that ran and concluded with a fatal error.
* Affected users: the number of unique users who had one or more sessions that ended with a fatal error.
* Total number of occurrences: by hovering on it, you’ll get a breakdown of the number of fatal sessions, the number of OOM sessions, the number of ANR sessions, and the number of non-fatal sessions.

If there is a sharp decline in the crash-free sessions rate, an email will be sent to notify you.

![](https://content.gitbook.com/content/zyyZGn3dXyNyX4fbdQmV/blobs/Ai6bVGXzgJXkKtlu63SM/91e23716c4a2bef146bbf59f1daf8504b8ef92f974703e3565af0a9241a286a1%20android%20reporting%20crashes%201.png)

### ANR Crashes

By default, if Crash Reporting is enabled, Luciq captures any ANR that occurs within your app, along with the stack trace of the crash.

You can disable/enable ANR reporting using the following API:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
CrashReporting.setAnrState(Feature.State.DISABLED)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
CrashReporting.setAnrState(Feature.State.DISABLED);
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Force Restarts

Starting from SDK version `11.1.0`, Luciq automatically reports Force Restarts. A Force Restart is when a user force terminates your application and re-launches it within 5 seconds, which could indicate performance issues.

Please note that Force Restarts reports *will not contain a stack trace*.

For Force Restarts to be detected on devices running Android KitKat (API 20) and below, the following security permission needs to be added:

{% code title="Android" %}

```xml
<uses-permission android:name="android.permission.GET_TASKS"/>
```

{% endcode %}

### App Hangs

Starting SDK version `11.5.0`, Luciq automatically reports App Hangs. An App Hang is captured when the main thread is blocked for more than 3 seconds. App Hangs that last more than 3 seconds are considered severe and are likely to cause user frustration. They are reported along with a stack trace for debugging.

## Manual Crash Reporting

You can use the following method and API to manually report any error or exception that you handle in your code and assign it a severity level.

### Report Exception

To report exceptions manually, use the following method; Both errors and exceptions can be passed to this method:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
val exception = LuciqNonFatalException.Builder(NullPointerException("Test Exception"))
.setUserAttributes(mapOf("height" to "tall"))
.setFingerprint("My Custom Fingerprint")
.setLevel(LuciqNonFatalException.Level.CRITICAL)
.build()
CrashReporting.report(exception)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
LCQNonFatalException exception = new LCQNonFatalException.Builder(new NullPointerException("Test Exception"))
.setUserAttributes(new HashMap<>())
.setFingerprint("My Custom Fingerprint")
.setLevel(LCQNonFatalException.Level.CRITICAL)
.build();
CrashReporting.report(exception);
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here is another example:

{% code title="Kotlin" %}

```kotlin
LuciqNonFatalException.Builder(NullPointerException("Test Exception"))
.setUserAttributes(mapOf("height" to "tall"))
.setFingerprint("My Custom Fingerprint")
.setLevel(LuciqNonFatalException.Level.CRITICAL)
.build().let { exception -> CrashReporting.report(exception) }
```

{% endcode %}

#### Add Level to Exception

You can set different severity levels for manually reported exceptions using the following API:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
val exception = LuciqNonFatalException.Builder(NullPointerException("Test Exception"))
.setLevel(LuciqNonFatalException.Level.CRITICAL)
.build()
CrashReporting.report(exception)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
LCQNonFatalException exception = new LCQNonFatalException.Builder(new NullPointerException("Test Exception"))
.setLevel(LCQNonFatalException.Level.CRITICAL)
.build();
CrashReporting.report(exception);
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here are the different severity levels available. *In case no level is indicated, the default level would be `ERROR`*

{% code title="Java" %}

```java
LuciqNonFatalException.Level.WARNING
LuciqNonFatalException.Level.ERROR
LuciqNonFatalException.Level.CRITICAL
LuciqNonFatalException.Level.INFO
```

{% endcode %}

### NDK Crashes

In the events that you're using a C++/NDK library or have code that runs at C++ level, the Luciq SDK will automatically detect and capture these low level crashes.

#### Adding the NDK Crashes Dependency

In order to start capturing NDK crashes, you'll need to add the below dependency to your app level gradle. Once it's added and the gradle is synced, NDK crashes will automatically be captured after the SDK is initialized and NDK crash reporting is enabled.

{% code title="Groovy" %}

```groovy
implementation 'ai.luciq.library:luciq-ndk-crash:18.0.0'
```

{% endcode %}

#### Enabling and Disabling

NDK crash reporting is disabled by default if the NDK dependency is added, however it can be enabled using the below method.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
CrashReporting.setNDKCrashesState(Feature.State.ENABLED)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
CrashReporting.setNDKCrashesState(Feature.State.ENABLED);
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Deobfuscation

Since native code is always obfuscated, you'll need to follow the instructions mentioned in the [deobfuscation page](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-crash-reporting/deobfuscation-for-android) in order to make the stack traces more readable.

### Grouping

When an already existing crash occurs once more for any user, that crash is reported as an occurrence in the original entry. However, in order to calculate whether a crash already exists and needs to be grouped, Luciq generates a fingerprint based on attributes used in the grouping logic.

The default Luciq grouping algorithm uses a mix of the exception and stack trace information. In some cases, you might want to change how the issues are grouped together using custom grouping or fingerprints.

#### Crash-to-Screen Assignment Logic

When a crash occurs, the Luciq SDK evaluates the in-memory view hierarchy at that moment. The crash is then assigned to the screen name (Activity, Fragment, or Composable) that is determined to be at the top of the hierarchy at the time of the crash.

#### Custom Grouping

{% hint style="warning" %}

#### Required Mapping Files

Please note that in order for custom grouping to be applied, mapping files are required to be uploaded first, otherwise, default grouping will be applied. For more information on uploading mapping files, please visit the [deobfuscation page](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-crash-reporting/deobfuscation-for-android).
{% endhint %}

One way to customize how crashes are grouped together is by providing Luciq with packages that you would like to ignore from our default grouping logic. If you define a package to be ignored, the frame with that package will be skipped and then we'll move on to find the next one that is not on your ignored list. This is done on an application level by going to your Application → Settings → Custom Crash Grouping. A few examples of this can be found below with an expected input.

Expected Input:

* Package
* Packages will be matched on a "starts with" basis:
  * Adding `com.thirdParty` will ignore any package we find in the stack trace that start with `com.thirdParty`
    * Examples: `com.thirdParty.start`, `com.thirdParty.start.user`, `com.thirdParty.end` etc.

Example 1

Sample Stack Trace:

```
com.thirdParty.login
com.app.page
com.android.error
com.app.user
com.app.homepageloading
```

* Without custom grouping, Luciq would group the crash based on `com.thirdParty.login` since it's the first non-system frame
* With custom grouping, having `com.thirdParty.login` on your list of package to ignore, we will skip the first frame `com.thirdParty.login` and the crash will be grouped based on `com.app.page`

Example 2

Sample Stack Trace:

```
com.thirdParty.login
com.thirdParty.userlogged
com.app.page
com.android.error
com.app.user
com.app.homepageloading
```

* Without custom grouping, Luciq would group the crash based on `com.thirdParty.login` since it's the first non-system frame
* With custom grouping, having `com.thirdParty` on your list of package to ignore, we will skip the first two frames \[`com.thirdParty.login` and `com.thirdParty.userlogged`] and the crash will be grouped based on `com.app.page`

#### Custom Fingerprinting

{% hint style="warning" %}

#### Overriding the default grouping

Please note that using custom fingerprinting will override Luciq's default grouping by sending a fingerprint string.
{% endhint %}

In the event that you'd like to report the exception manually with a custom grouping fingerprint in mind, you can use the below APIs to do just that.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
CrashReporting.reportException(throwable, "exception identifier", userAttrsMap, "grouping fingerprint");
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
CrashReporting.reportException(throwable, "exception identifier", userAttrsMap, "grouping fingerprint")
```

{% endcode %}
{% endtab %}
{% endtabs %}
