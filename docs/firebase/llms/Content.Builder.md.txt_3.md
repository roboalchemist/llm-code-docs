# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder.md.txt

# Content.Builder

# Content.Builder


```
class Content.Builder
```

<br />

*** ** * ** ***

Builder class to facilitate constructing complex `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` objects.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#build()()` Returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` using the defined `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#role()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#fileData(kotlin.String,kotlin.String)(uri: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#image(android.graphics.Bitmap)(image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#image(android.graphics.Bitmap)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, which should be interpreted by the model based on the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `<T : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#part(com.google.firebase.ai.type.Part)(data: T)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#setParts(kotlin.collections.MutableList)(parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#setRole(kotlin.String)(role: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#text(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/TextPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#text(kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()` The mutable list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part`s comprising the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#role()` The producer of the content. |

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

Returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` using the defined `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#role()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`.

### fileData

```
fun fileData(uri: String, mimeType: String): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`.

### image

```
fun image(image: Bitmap): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#image(android.graphics.Bitmap)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`.

### inlineData

```
fun inlineData(bytes: ByteArray, mimeType: String): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, which should be interpreted by the model based on the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`.

### part

```
fun <T : Part> part(data: T): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`.

### setParts

```
fun setParts(parts: MutableList<Part>): Content.Builder
```

### setRole

```
fun setRole(role: String?): Content.Builder
```

### text

```
fun text(text: String): Content.Builder
```

Adds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/TextPart` with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#text(kotlin.String)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder#parts()`.

## Public properties

### parts

```
var parts: MutableList<Part>
```

The mutable list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part`s comprising the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content`.

Prefer using the provided helper methods over modifying this list directly.

### role

```
var role: String?
```

The producer of the content. Must be either 'user' or 'model'. By default, it's "user".