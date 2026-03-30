# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.md.txt

# ShortDynamicLink

# ShortDynamicLink


```
interface ShortDynamicLink
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This interface is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Response from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink()` that returns the shortened Dynamic Link, link flow chart, and warnings from the requested Dynamic Link.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) @https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = [Suffix.UNGUESSABLE, Suffix.SHORT]) annotation https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix` Path generation option for short Dynamic Link length |
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning` **This interface is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public functions |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `[getPreviewLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getPreviewLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `[getShortLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getShortLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning!>` | `[getWarnings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getWarnings())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Extension functions |
|---|---|
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide shortLink. |
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide previewLink. |
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide warnings. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public functions

### getPreviewLink

```
fun [getPreviewLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getPreviewLink())(): Uri?
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the preview link to show the link flow chart.

### getShortLink

```
fun [getShortLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getShortLink())(): Uri?
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the short Dynamic Link value.

### getWarnings

```
fun [getWarnings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getWarnings())(): (Mutable)List<ShortDynamicLink.Warning!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets information about potential warnings on link creation.

## Extension functions

### component1

```
operator fun ShortDynamicLink.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())(): Uri?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide shortLink.

### component1

```
operator fun ShortDynamicLink.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())(): Uri?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide shortLink.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### component2

```
operator fun ShortDynamicLink.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())(): Uri?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide previewLink.

### component2

```
operator fun ShortDynamicLink.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())(): Uri?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide previewLink.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### component3

```
operator fun ShortDynamicLink.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())(): List<ShortDynamicLink.Warning>
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide warnings.

### component3

```
operator fun ShortDynamicLink.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())(): List<ShortDynamicLink.Warning>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink` to provide warnings.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)