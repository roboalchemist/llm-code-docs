# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.md.txt

# PendingDynamicLinkData

# PendingDynamicLinkData


```
class PendingDynamicLinkData
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Provides accessor methods to dynamic links data.

## Summary

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#PendingDynamicLinkData(java.lang.String,int,long,android.net.Uri)( deepLink: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, clickTimestamp: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, redirectUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html? )` Create a PendingDynamicLinkData which can be used for testing. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `[getClickTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getClickTimestamp())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `[getLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `[getMinimumAppVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getMinimumAppVersion())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/content/Intent.html?` | `[getUpdateAppIntent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context))(context: https://developer.android.com/reference/kotlin/android/content/Context.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/os/Bundle.html` | `[getUtmParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUtmParameters())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Extension functions |
|---|---|
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide link. |
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide minimumAppVersion. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide clickTimestamp. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Protected constructors

### PendingDynamicLinkData

```
protected PendingDynamicLinkData(
    deepLink: String?,
    minVersion: Int,
    clickTimestamp: Long,
    redirectUrl: Uri?
)
```

Create a PendingDynamicLinkData which can be used for testing.

| Parameters |
|---|---|
| `deepLink: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | dynamic link deep link, can be null. |
| `minVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | app minimum version. 0 if no minimum version required. |
| `clickTimestamp: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | timestamp of when the dynamic link was clicked. If zero, will be current time. |

## Public functions

### getClickTimestamp

```
fun [getClickTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getClickTimestamp())(): Long
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the time that the user clicked on the Firebase Dynamic Link. This can be used to determine the amount of time that has passed since the user selected the link until the app is launched.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The number of milliseconds that have elapsed since January 1, 1970. |

### getLink

```
fun [getLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getLink())(): Uri?
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link parameter of the Firebase Dynamic Link.

This link will be set as data in the launch Intent, see `https://developer.android.com/reference/kotlin/android/content/Intent.html#setData-android.net.Uri-`, which will match `https://developer.android.com/reference/kotlin/android/content/IntentFilter.html` to deep link into the app.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | The deep link if it exists, null otherwise. |

### getMinimumAppVersion

```
fun [getMinimumAppVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getMinimumAppVersion())(): Int
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the minimum app version requested to process the Firebase Dynamic Link that can be compared directly with `https://developer.android.com/reference/kotlin/android/content/pm/PackageInfo.html#versionCode--`. If the minimum version code is higher than the installed app version code, the app can upgrade using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context)`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | minimum version code set on the dynamic link, or 0 if not specified. |

### getUpdateAppIntent

```
fun [getUpdateAppIntent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context))(context: Context): Intent?
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the intent to update the app to the version in the Play Store.

An intent is returned to be used as a parameter to startActivity to launch the Play Store update flow for the app. After update, if the user re-launches the app from the Play Store by selecting the displayed Continue button then the deep link will be set as the data in the re-launch intent and will launch any Activity with an `https://developer.android.com/reference/kotlin/android/content/IntentFilter.html` that matches the deeplink. This is the same as the new install flow. The dynamic link returned during initial launch will not be available from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)` during the update re-launch.

If the minimum version required by the dynamic link is not greater than the currently installed version, then null is returned.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/content/Intent.html?` | - An `https://developer.android.com/reference/kotlin/android/content/Intent.html` that will launch the Play Store to update the app, or null if the dynamic link minimum version code is not greater than the installed version. |

### getUtmParameters

```
fun [getUtmParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUtmParameters())(): Bundle
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the `https://developer.android.com/reference/kotlin/android/os/Bundle.html` which contains utm parameters associated with the Firebase Dynamic Link.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/os/Bundle.html` | Bundle of utm parameters associated with firebase dynamic link. |

## Extension functions

### component1

```
operator fun PendingDynamicLinkData.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())(): Uri?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide link.

### component1

```
operator fun PendingDynamicLinkData.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())(): Uri?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide link.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### component2

```
operator fun PendingDynamicLinkData.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())(): Int
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide minimumAppVersion.

### component2

```
operator fun PendingDynamicLinkData.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())(): Int
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide minimumAppVersion.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### component3

```
operator fun PendingDynamicLinkData.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide clickTimestamp.

### component3

```
operator fun PendingDynamicLinkData.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())(): Long
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide clickTimestamp.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)