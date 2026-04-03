# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.md.txt

# ShortDynamicLink

# ShortDynamicLink


```
interface ShortDynamicLink
```

<br />

*** ** * ** ***

| **This interface is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Response from [buildShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink()) that returns the shortened Dynamic Link, link flow chart, and warnings from the requested Dynamic Link.

## Summary

|                                                                                                                                                                                                                                    ### Nested types                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[Retention](https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html)`(value = RetentionPolicy.SOURCE)` `@`[IntDef](https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html)`(value = [Suffix.UNGUESSABLE, Suffix.SHORT])` `annotation `[ShortDynamicLink.Suffix](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix) Path generation option for short Dynamic Link length |
| `interface `[ShortDynamicLink.Warning](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning) **This interface is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                                                                                                              |

|                                                                                                                                                              ### Public functions                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                                                                                                                                                                                                   | ~~[getPreviewLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getPreviewLink())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                                                                                                                                                                                                   | ~~[getShortLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getShortLink())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />     |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ShortDynamicLink.Warning](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning)`!>` | ~~[getWarnings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getWarnings())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />       |

|                                                                                                             ### Extension functions                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                                                                                         | [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`.`~~[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())~~`()` Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide shortLink.   |
| `operator `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                                                                                         | [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`.`~~[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())~~`()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                  |
| `operator `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                                                                                         | [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`.`~~[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())~~`()` Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide previewLink. |
| `operator `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                                                                                         | [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`.`~~[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())~~`()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                  |
| `operator `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ShortDynamicLink.Warning](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning)`>` | [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`.`~~[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())~~`()` Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide warnings.    |
| `operator `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ShortDynamicLink.Warning](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning)`>` | [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`.`~~[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())~~`()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                  |

## Public functions

### getPreviewLink

```
funÂ [getPreviewLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getPreviewLink())():Â Uri?
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the preview link to show the link flow chart.  

### getShortLink

```
funÂ [getShortLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getShortLink())():Â Uri?
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the short Dynamic Link value.  

### getWarnings

```
funÂ [getWarnings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#getWarnings())():Â (Mutable)List<ShortDynamicLink.Warning!>
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets information about potential warnings on link creation.  

## Extension functions

### component1

```
operatorÂ funÂ ShortDynamicLink.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())():Â Uri?
```

Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide shortLink.  

### component1

```
operatorÂ funÂ ShortDynamicLink.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component1())():Â Uri?
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide shortLink.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### component2

```
operatorÂ funÂ ShortDynamicLink.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())():Â Uri?
```

Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide previewLink.  

### component2

```
operatorÂ funÂ ShortDynamicLink.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component2())():Â Uri?
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide previewLink.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### component3

```
operatorÂ funÂ ShortDynamicLink.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())():Â List<ShortDynamicLink.Warning>
```

Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide warnings.  

### component3

```
operatorÂ funÂ ShortDynamicLink.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink#(com.google.firebase.dynamiclinks.ShortDynamicLink).component3())():Â List<ShortDynamicLink.Warning>
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) to provide warnings.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)