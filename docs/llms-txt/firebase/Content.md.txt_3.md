# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.md.txt

# Content

# Content


```
class Content
```

<br />

*** ** * ** ***

Represents content sent to and received from the model.

`Content` is composed of a one or more heterogeneous parts that can be represent data in different formats, like text or images.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` Builder class to facilitate constructing complex `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` objects. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content#Content(kotlin.String,kotlin.collections.List)(role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>)` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content#copy(kotlin.String,kotlin.collections.List)(role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>)` Returns a copy of this object, with the provided parameters overwriting the originals. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content#parts()` An ordered list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` that constitute this content. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content#role()` The producer of the content. |

## Public constructors

### Content

```
Content(role: String? = "user", parts: List<Part>)
```

| Parameters |
|---|---|
| `role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = "user"` | The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`. |
| `parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>` | An ordered list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` that constitute this content. |

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

An ordered list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` that constitute this content.

### role

```
val role: String?
```

The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`.