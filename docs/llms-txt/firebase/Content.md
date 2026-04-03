# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.md.txt

# Content

# Content


```
public final class Content
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents content sent to and received from the model.

`Content` is composed of a one or more heterogeneous parts that can be represent data in different formats, like text or images.

## Summary

|                                                                                                                                                                     ### Nested types                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public final class `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder) **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |

|                                                                                                                                                                                   ### Public fields                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)`>` | [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content#parts()) An ordered list of [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part) that constitute this content. |
| `final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                                                                                                                                                                                | [role](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content#role()) The producer of the content.                                                                                                                         |

|                                                                                                                                                                                                                                                                                                       ### Public constructors                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content#Content(kotlin.String,kotlin.collections.List))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` role, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)`> parts)` |

|                                                                                              ### Public methods                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) | [copy](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content#copy(kotlin.String,kotlin.collections.List))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` role, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)`> parts)` Returns a copy of this object, with the provided parameters overwriting the originals. |

## Public fields

### parts

```
publicÂ finalÂ @NonNull List<@NonNull Part>Â parts
```

An ordered list of [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part) that constitute this content.  

### role

```
publicÂ finalÂ StringÂ role
```

The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`.  

## Public constructors

### Content

```
publicÂ Content(StringÂ role,Â @NonNull List<@NonNull Part>Â parts)
```  

|                                                                                                                                                                                      Parameters                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` role`                                                                                                                                                                                                                                                                                                 | The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`.                                                      |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)`> parts` | An ordered list of [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part) that constitute this content. |

## Public methods

### copy

```
publicÂ finalÂ @NonNull ContentÂ copy(StringÂ role,Â @NonNull List<@NonNull Part>Â parts)
```

Returns a copy of this object, with the provided parameters overwriting the originals.