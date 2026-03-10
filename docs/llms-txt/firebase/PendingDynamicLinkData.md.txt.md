# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData.md.txt

# PendingDynamicLinkData

# PendingDynamicLinkData


```
public class PendingDynamicLinkData
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
| `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#PendingDynamicLinkData(java.lang.String,int,long,android.net.Uri)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html deepLink, int minVersion, long clickTimestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html redirectUrl )` Create a PendingDynamicLinkData which can be used for testing. |

| ### Public methods |
|---|---|
| `long` | `[getClickTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getClickTimestamp())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getLink](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getLink())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `int` | `[getMinimumAppVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getMinimumAppVersion())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/content/Intent.html` | `[getUpdateAppIntent](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context)` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/os/Bundle.html` | `[getUtmParameters](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUtmParameters())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Extension functions |
|---|---|
| `final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide link. |
| `final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData receiver )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide minimumAppVersion. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData receiver )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide clickTimestamp. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData receiver )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Protected constructors

### PendingDynamicLinkData

```
protected PendingDynamicLinkData(
    @Nullable String deepLink,
    int minVersion,
    long clickTimestamp,
    @Nullable Uri redirectUrl
)
```

Create a PendingDynamicLinkData which can be used for testing.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html deepLink` | dynamic link deep link, can be null. |
| `int minVersion` | app minimum version. 0 if no minimum version required. |
| `long clickTimestamp` | timestamp of when the dynamic link was clicked. If zero, will be current time. |

## Public methods

### getClickTimestamp

```
public long [getClickTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getClickTimestamp())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the time that the user clicked on the Firebase Dynamic Link. This can be used to determine the amount of time that has passed since the user selected the link until the app is launched.

| Returns |
|---|---|
| `long` | The number of milliseconds that have elapsed since January 1, 1970. |

### getLink

```
public @Nullable Uri [getLink](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getLink())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link parameter of the Firebase Dynamic Link.

This link will be set as data in the launch Intent, see `https://developer.android.com/reference/kotlin/android/content/Intent.html#setData-android.net.Uri-`, which will match `https://developer.android.com/reference/kotlin/android/content/IntentFilter.html` to deep link into the app.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | The deep link if it exists, null otherwise. |

### getMinimumAppVersion

```
public int [getMinimumAppVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getMinimumAppVersion())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the minimum app version requested to process the Firebase Dynamic Link that can be compared directly with `https://developer.android.com/reference/kotlin/android/content/pm/PackageInfo.html#versionCode--`. If the minimum version code is higher than the installed app version code, the app can upgrade using `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context)`.

| Returns |
|---|---|
| `int` | minimum version code set on the dynamic link, or 0 if not specified. |

### getUpdateAppIntent

```
public @Nullable Intent [getUpdateAppIntent](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context))(@NonNull Context context)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the intent to update the app to the version in the Play Store.

An intent is returned to be used as a parameter to startActivity to launch the Play Store update flow for the app. After update, if the user re-launches the app from the Play Store by selecting the displayed Continue button then the deep link will be set as the data in the re-launch intent and will launch any Activity with an `https://developer.android.com/reference/kotlin/android/content/IntentFilter.html` that matches the deeplink. This is the same as the new install flow. The dynamic link returned during initial launch will not be available from `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)` during the update re-launch.

If the minimum version required by the dynamic link is not greater than the currently installed version, then null is returned.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/content/Intent.html` | - An `https://developer.android.com/reference/kotlin/android/content/Intent.html` that will launch the Play Store to update the app, or null if the dynamic link minimum version code is not greater than the installed version. |

### getUtmParameters

```
public @NonNull Bundle [getUtmParameters](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUtmParameters())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the `https://developer.android.com/reference/kotlin/android/os/Bundle.html` which contains utm parameters associated with the Firebase Dynamic Link.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/os/Bundle.html` | Bundle of utm parameters associated with firebase dynamic link. |

## Extension functions

### FirebaseDynamicLinksKt.component1

```
public final Uri FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())(
    @NonNull PendingDynamicLinkData receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide link.

### FirebaseDynamicLinksKt.component1

```
public final Uri FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())(
    @NonNull PendingDynamicLinkData receiver
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide link.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseDynamicLinksKt.component2

```
public final int FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())(
    @NonNull PendingDynamicLinkData receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide minimumAppVersion.

### FirebaseDynamicLinksKt.component2

```
public final int FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())(
    @NonNull PendingDynamicLinkData receiver
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide minimumAppVersion.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseDynamicLinksKt.component3

```
public final long FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())(
    @NonNull PendingDynamicLinkData receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide clickTimestamp.

### FirebaseDynamicLinksKt.component3

```
public final long FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())(
    @NonNull PendingDynamicLinkData receiver
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData` to provide clickTimestamp.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)