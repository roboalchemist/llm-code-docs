# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.md.txt

# FirebaseDynamicLinks

# FirebaseDynamicLinks


```
abstract class FirebaseDynamicLinks
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Provides access to dynamic links that are received by an app at launch.

When a dynamic link is clicked, the app is launched, or if the app is not yet installed, the user is directed to the Play Store to install and launch the app. In both cases the dynamic link made available to the app using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)`. An `https://developer.android.com/reference/kotlin/android/content/IntentFilter.html` for the deeplink can also be used to launch the app directly into a targeted `https://developer.android.com/reference/kotlin/android/app/Activity.html` or otherwise will start in the main launch Activity.

Dynamic link data returned from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)` can be accessed using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` class.

[Android App Links](https://developer.android.com/training/app-links/index.html) can also be used to launch the app with dynamic links by registering to handle your Dynamic Links in your app. The guide for setting up your app to receive Firebase Dynamic Links as an App Link can be found on the Android [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/android/receive#app_links) site.

Dynamic link data is available from the app launch intent. This data may include data for dynamic link extensions such as app invites.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#FirebaseDynamicLinks()()` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[createDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#createDynamicLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData!>` | `[getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.net.Uri))(dynamicLinkUri: https://developer.android.com/reference/kotlin/android/net/Uri.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData!>` | `[getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent))(intent: https://developer.android.com/reference/kotlin/android/content/Intent.html?)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `synchronized java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks` | `[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `synchronized java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks` | `[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance(com.google.firebase.FirebaseApp))(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Extension functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1)` function. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1)` function. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))(suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1)` function. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))(suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public constructors

### FirebaseDynamicLinks

```
FirebaseDynamicLinks()
```

## Public functions

### createDynamicLink

```
abstract fun [createDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#createDynamicLink())(): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create a long or short Dynamic Link.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | Builder to create the Dynamic Link. |

### getDynamicLink

```
abstract fun [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.net.Uri))(dynamicLinkUri: Uri): Task<PendingDynamicLinkData!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Determine if the app has a pending dynamic link and provide access to the dynamic link parameters. A pending dynamic link may have been previously captured when a user clicked on a dynamic link, or may be present in the dynamicLinkUri parameter. If both are present, the previously captured dynamic link will take precedence. The captured data will be removed after first access.

This method provides the same functionality as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)` except the Uri is provided in place of the `https://developer.android.com/reference/kotlin/android/content/Intent.html`.

| Parameters |
|---|---|
| `dynamicLinkUri: https://developer.android.com/reference/kotlin/android/net/Uri.html` | - A uri that may be a dynamic link. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData!>` | Task where `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--` is true when processing is completed successfully and either a dynamic link is returned, or null if a dynamic link is not previously captured or is in the Uri. `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--` will only be false when a processing error occurs. |

### getDynamicLink

```
abstract fun [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent))(intent: Intent?): Task<PendingDynamicLinkData!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Determine if the app has a pending dynamic link and provide access to the dynamic link parameters. A pending dynamic link may have been previously captured when a user clicked on a dynamic link, or may be present in the intent.

When a dynamic link is clicked by the user, in most cases it is captured when clicked and stored until accessed by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)` and returned as the of the `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html`. If the dynamic link was not captured, as is the case when App Links launches the app, then the dynamic link is provided in the `https://developer.android.com/reference/kotlin/android/content/Intent.html#getData--`. The intent data is then processed to retrieve the dynamic link data. If the dynamic links is both captured and is present in the intent, then the captured data will take precedence. The captured data will be removed after first access.

The intent parameter should be the intent that launched the application, or can be null if the intent does not include the dynamic link. A non-null intent is necessary only when the app is launched directly using the dynamic link, such as when using [App Links](https://developer.android.com/training/app-links/index.html). The app must configure an `https://developer.android.com/reference/kotlin/android/content/IntentFilter.html` to override the default capture processing when the link is clicked.

In the callback the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` is returned in `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnSuccessListener-com.google.android.gms.tasks.OnSuccessListener&lt;? super TResult&gt;-` or `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCompleteListener-android.app.Activity-com.google.android.gms.tasks.OnCompleteListener&lt;TResult&gt;-` which returns the most recently clicked dynamic link, or null if a dynamic link was not pending as captured data or in the intent.

If processing could not be completed due to an error, then `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html` will be called. Notice that in the case a pending dynamic link is not present, then `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--` will be true and the returned `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData` will be null as this is normal processing and not an error condition.

If a dynamic link, the call will also send FirebaseAnalytics dynamic link event.

### getInstance

```
synchronized java-static fun [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance())(): FirebaseDynamicLinks
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks`.

The default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance must have been initialized before this function is called. See [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).

### getInstance

```
synchronized java-static fun [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance(com.google.firebase.FirebaseApp))(firebaseApp: FirebaseApp): FirebaseDynamicLinks
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks` for the provided firebaseApp.

## Extension functions

### dynamicLink

```
fun FirebaseDynamicLinks.[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))(init: DynamicLink.Builder.() -> Unit): DynamicLink
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1)` function.

### dynamicLink

```
fun FirebaseDynamicLinks.[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))(init: DynamicLink.Builder.() -> Unit): DynamicLink
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1)` function.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### shortLinkAsync

```
fun FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))(init: DynamicLink.Builder.() -> Unit): Task<ShortDynamicLink>
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1)` function.

### shortLinkAsync

```
fun FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))(suffix: Int, init: DynamicLink.Builder.() -> Unit): Task<ShortDynamicLink>
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1)` function.

### shortLinkAsync

```
fun FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))(init: DynamicLink.Builder.() -> Unit): Task<ShortDynamicLink>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1)` function.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### shortLinkAsync

```
fun FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))(suffix: Int, init: DynamicLink.Builder.() -> Unit): Task<ShortDynamicLink>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1)` function.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)