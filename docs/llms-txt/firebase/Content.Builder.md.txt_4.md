# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder.md.txt

# Content.Builder

# Content.Builder


```
class Content.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder class to facilitate constructing complex `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` objects.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#build()()` Returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` using the defined `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#role()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)(uri: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)(image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagePart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, which should be interpreted by the model based on the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder` | `<T : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#part(com.google.firebase.vertexai.type.Part)(data: T)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TextPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()` The mutable list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part`s comprising the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#role()` The producer of the content. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): Content
```

Returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` using the defined `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#role()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### fileData

```
fun fileData(uri: String, mimeType: String): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### image

```
fun image(image: Bitmap): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagePart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### inlineData

```
fun inlineData(bytes: ByteArray, mimeType: String): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, which should be interpreted by the model based on the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### part

```
fun <T : Part> part(data: T): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### text

```
fun text(text: String): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TextPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder#parts()`.

## Public properties

### parts

```
var parts: MutableList<Part>
```

The mutable list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part`s comprising the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content`.

Prefer using the provided helper methods over modifying this list directly.

### role

```
var role: String?
```

The producer of the content. Must be either 'user' or 'model'. By default, it's "user".