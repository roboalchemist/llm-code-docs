# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.md.txt

# Content

# Content


```
class Content
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents content sent to and received from the model.

`Content` is composed of a one or more heterogeneous parts that can be represent data in different formats, like text or images.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder` **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content#Content(kotlin.String,kotlin.collections.List)(role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part>)` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content#copy(kotlin.String,kotlin.collections.List)(role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part>)` Returns a copy of this object, with the provided parameters overwriting the originals. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content#parts()` An ordered list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` that constitute this content. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content#role()` The producer of the content. |

## Public constructors

### Content

```
Content(role: String? = "user", parts: List<Part>)
```

| Parameters |
|---|---|
| `role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = "user"` | The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`. |
| `parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part>` | An ordered list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` that constitute this content. |

## Public functions

### copy

```
fun copy(role: String? = this.role, parts: List<Part> = this.parts): Content
```

Returns a copy of this object, with the provided parameters overwriting the originals.

## Public properties

### parts

```
val parts: List<Part>
```

An ordered list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` that constitute this content.

### role

```
val role: String?
```

The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`.