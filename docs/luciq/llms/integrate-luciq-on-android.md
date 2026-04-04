# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/integrate-luciq-on-android.md

# Integrate Luciq on Android

{% hint style="warning" %}

### Compile SDK Version

Please note that the `compileSDKVersion` should be v29 or above, otherwise you may run into build errors.
{% endhint %}

## Installation

This installation process will install the Luciq SDK that supports [Bug Reporting](https://www.luciq.ai/product/bug-reporting), [Crash Reporting](https://www.luciq.ai/product/crash-reporting) and [App Performance Monitoring](https://www.luciq.ai/product/app-performance-monitoring).

### Gradle

Add this line to your `build.gradle` file.

{% tabs %}
{% tab title="Gradle" %}

```gradle
implementation 'ai.luciq.library:luciq:18.0.0' 
```

{% endtab %}
{% endtabs %}

### Maven

{% tabs %}
{% tab title="Maven" %}

```gradle
<dependency>
      <groupId>ai.luciq.library</groupId>
      <artifactId>luciq</artifactId>
      <version>18.0.0</version>
</dependency>
```

{% endtab %}
{% endtabs %}

## Using Luciq

In your `Application` class add this line to your `onCreate` method. This initializes Luciq with the default invocation event, *Shake*.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Luciq.Builder(this, "APP_TOKEN").build()
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
new Luciq.Builder(this, "APP_TOKEN").build();
```

{% endcode %}
{% endtab %}
{% endtabs %}

Initializing [Luciq](https://luciq.ai/platforms/android) in your application can also be done using one or multiple invocation events. All possible invocation events are explained in the [invocation](https://docs.luciq.ai/docs/android-invocation) section.

{% tabs %}
{% tab title="Kotlin" %}

```kotlin
Luciq.Builder(this, "APP_TOKEN")
            .setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.FLOATING_BUTTON)
            .build()
```

{% endtab %}

{% tab title="Java" %}

```java
new Luciq.Builder(this, "APP_TOKEN")
	.setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.SCREENSHOT)
	.build();
```

{% endtab %}
{% endtabs %}

You can find your app token by selecting **SDK Integration** in the **Settings** menu of your [Luciq dashboard](https://dashboard.luciq.ai/dashboard).

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FyyVtl3ILP3Gb2hMpNk01%2Fimage.png?alt=media&#x26;token=1da87cd0-951b-49f3-8925-7a045eb7a308" alt=""><figcaption></figcaption></figure>

#### Permissions

Permissions are automatically added to your `AndroidManifest.xml` file. Some of them are required to be able to fetch information like network and WiFi connection. Others are used to allow your users to attach images, videos, and audio recordings. In general, permission requests don't appear unless your user attempts to use a feature requiring a permission.

The only exception is if you set the [invocation event](https://docs.luciq.ai/docs/android-invocation) to be a *Screenshot*. In that case, the storage permission will be requested when your application launches. The screenshot invocation is a special case because there is no native event that tells the SDK that a screenshot has been captured. The only way to know is to monitor the screenshots directory. The SDK is invoked when a screenshot is added to the directory while your application is active.

{% tabs %}
{% tab title="XML" %}
{% code overflow="wrap" %}

```xml
<uses-permission android:name=“android.permission.ACCESS_NETWORK_STATE” />
<uses-permission android:name=“android.permission.WRITE_EXTERNAL_STORAGE” />
<uses-permission android:name=“android.permission.READ_EXTERNAL_STORAGE” />
<uses-permission android:name=“android.permission.ACCESS_WIFI_STATE” />
<uses-permission android:name=“android.permission.RECORD_AUDIO” />
<uses-permission android:name=“android.permission.MODIFY_AUDIO_SETTINGS” />
<uses-permission android:name=“android.permission.INTERNET” />
<uses-permission android:name=“android.permission.WAKE_LOCK” />
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can remove any of the permissions if you will not be using the feature associated with it, as in the following example.

{% tabs %}
{% tab title="XML" %}
{% code overflow="wrap" %}

```xml
<uses-permission android:name=“android.permission.WRITE_EXTERNAL_STORAGE” tools:node=“remove”/>
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="warning" %}

### Required Permissions

There are a few permissions that are always required and cannot be removed. These permissions are:\
`<uses-permission android:name=“android.permission.WAKE_LOCK”/>`\
`<uses-permission android:name=“android.permission.INTERNET”/>`
{% endhint %}

{% hint style="info" %}

### **16KB Compatibility**

From Android 15 (API 35), native (.so) libraries must support 16KB page sizes. Luciq supports this starting from version **13.4.0**. Please upgrade if your app targets Android 15+ to avoid crashes. [Learn more](https://developer.android.com/guide/practices/page-sizes?hl=en).
{% endhint %}
