# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder.md.txt

# ActionCodeSettings.Builder

# ActionCodeSettings.Builder


```
class ActionCodeSettings.Builder
```

<br />

*** ** * ** ***

A Builder class for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings`. Get an instance of this Builder using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#newBuilder()`.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#build()()` Builds the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` that this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` has constructed. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#getHandleCodeInApp()()` Returns whether the out-of-band (OOB) code should be handled by the app. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#getIOSBundleId()()` Returns the bundle ID of the installed Apple platforms app. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)( androidPackageName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, installIfNotAvailable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, minimumVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Sets the Android package name and returns the current builder instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)(status: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` The default is false. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setIOSBundleId(java.lang.String)(iOSBundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` To be used if the email link that is sent might be opened on an iOS device. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#dynamicLinkDomain()` **This property is deprecated.** Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#linkDomain()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#url()` |

## Public functions

### build

```
fun build(): ActionCodeSettings
```

Builds the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` that this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` has constructed.

### getHandleCodeInApp

```
fun getHandleCodeInApp(): Boolean
```

Returns whether the out-of-band (OOB) code should be handled by the app. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)`.

### getIOSBundleId

```
fun getIOSBundleId(): String?
```

Returns the bundle ID of the installed Apple platforms app. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setIOSBundleId(java.lang.String)`.

### setAndroidPackageName

```
fun setAndroidPackageName(
    androidPackageName: String,
    installIfNotAvailable: Boolean,
    minimumVersion: String?
): ActionCodeSettings.Builder
```

Sets the Android package name and returns the current builder instance. If `
installIfNotAvailable` is set to `true` and the link is opened on an android device, it will try to install the app if not already available. Otherwise the web URL is used.

A minimum version string is also available. If the installed app is an older version, the user is taken to the Play Store to upgrade the app.

### setHandleCodeInApp

```
fun setHandleCodeInApp(status: Boolean): ActionCodeSettings.Builder
```

The default is false. When set to true, the action code link will be sent as a universal link and will be open by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed.

### setIOSBundleId

```
fun setIOSBundleId(iOSBundleId: String?): ActionCodeSettings.Builder
```

To be used if the email link that is sent might be opened on an iOS device.

Sets the iOS bundle Id and returns the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` instance.

## Public properties

### dynamicLinkDomain

```
var dynamicLinkDomain: String!
```

> [!CAUTION]
> **This property is deprecated.**   
>
> Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#linkDomain()` to set a custom domain for mobile links. Learn more in the [Dynamic Links deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq).

### linkDomain

```
var linkDomain: String!
```

### url

```
var url: String!
```