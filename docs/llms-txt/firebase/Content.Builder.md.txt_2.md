# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder.md.txt

# Content.Builder

# Content.Builder


```
public final class Content.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder class to facilitate constructing complex `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` objects.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()` The mutable list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part`s comprising the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content`. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#role()` The producer of the content. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addFileData(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addImage(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image)` Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addInlineData(kotlin.ByteArray,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bytes, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, which should be interpreted by the model based on the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder` | `<T extends https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addPart(com.google.firebase.vertexai.type.Part)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T data)` Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addText(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TextPart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#build()()` Returns a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` using the defined `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#role()` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`. |

## Public fields

### parts

```
public final @NonNull List<@NonNull Part> parts
```

The mutable list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part`s comprising the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content`.

Prefer using the provided helper methods over modifying this list directly.

### role

```
public final String role
```

The producer of the content. Must be either 'user' or 'model'. By default, it's "user".

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### addFileData

```
public final @NonNull Content.Builder addFileData(@NonNull String uri, @NonNull String mimeType)
```

Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### addImage

```
public final @NonNull Content.Builder addImage(@NonNull Bitmap image)
```

Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### addInlineData

```
public final @NonNull Content.Builder addInlineData(@NonNull byte[] bytes, @NonNull String mimeType)
```

Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, which should be interpreted by the model based on the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)`, to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### addPart

```
public final @NonNull Content.Builder <T extends Part> addPart(@NonNull T data)
```

Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### addText

```
public final @NonNull Content.Builder addText(@NonNull String text)
```

Adds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TextPart` with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`.

### build

```
public final @NonNull Content build()
```

Returns a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` using the defined `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#role()` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()`.