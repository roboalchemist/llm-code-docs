# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.md.txt

# ShortDynamicLink

# ShortDynamicLink


```
public interface ShortDynamicLink
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This interface is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Response from `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink()` that returns the shortened Dynamic Link, link flow chart, and warnings from the requested Dynamic Link.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) @https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = [Suffix.UNGUESSABLE, Suffix.SHORT]) public annotation https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix` Path generation option for short Dynamic Link length |
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning` **This interface is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getPreviewLink](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#getPreviewLink())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getShortLink](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#getShortLink())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning>` | `[getWarnings](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#getWarnings())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Extension functions |
|---|---|
| `default final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide shortLink. |
| `default final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `default final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide previewLink. |
| `default final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `default final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide warnings. |
| `default final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public methods

### getPreviewLink

```
abstract @Nullable Uri [getPreviewLink](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#getPreviewLink())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the preview link to show the link flow chart.

### getShortLink

```
abstract @Nullable Uri [getShortLink](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#getShortLink())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the short Dynamic Link value.

### getWarnings

```
abstract @NonNull List<ShortDynamicLink.Warning> [getWarnings](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#getWarnings())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets information about potential warnings on link creation.

## Extension functions

### FirebaseDynamicLinksKt.component1

```
default final Uri FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())(@NonNull ShortDynamicLink receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide shortLink.

### FirebaseDynamicLinksKt.component1

```
default final Uri FirebaseDynamicLinksKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())(@NonNull ShortDynamicLink receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide shortLink.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseDynamicLinksKt.component2

```
default final Uri FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())(@NonNull ShortDynamicLink receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide previewLink.

### FirebaseDynamicLinksKt.component2

```
default final Uri FirebaseDynamicLinksKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())(@NonNull ShortDynamicLink receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide previewLink.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseDynamicLinksKt.component3

```
default final @NonNull List<@NonNull ShortDynamicLink.Warning> FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())(@NonNull ShortDynamicLink receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide warnings.

### FirebaseDynamicLinksKt.component3

```
default final @NonNull List<@NonNull ShortDynamicLink.Warning> FirebaseDynamicLinksKt.[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())(@NonNull ShortDynamicLink receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide warnings.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)