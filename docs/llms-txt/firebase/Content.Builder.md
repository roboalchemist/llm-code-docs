# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder.md.txt

# Content.Builder

# Content.Builder


```
public final class Content.Builder
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder class to facilitate constructing complex [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) objects.

## Summary

|                                                                                                                                                                                   ### Public fields                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)`>` | [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()) The mutable list of [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)s comprising the [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content). |
| `final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                                                                                                                                                                                | [role](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#role()) The producer of the content.                                                                                                                                                                                                                     |

|                                                    ### Public constructors                                                    |
|-------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#Builder())`()` |

|                                                                                                      ### Public methods                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder) | [addFileData](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addFileData(kotlin.String,kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` uri, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` mimeType)` Adds a new [FileDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart) with the provided [uri](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)) and [mimeType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).    |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder) | [addImage](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addImage(android.graphics.Bitmap))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` image)` Adds a new [ImagePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart) with the provided [image](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).                                                                                                                                                                                                                                                                                                                                                                    |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder) | [addInlineData](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addInlineData(kotlin.ByteArray,kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` byte[] bytes, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` mimeType)` Adds a new [InlineDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart) with the provided [bytes](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)), which should be interpreted by the model based on the [mimeType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)), to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()). |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder) | `<T extends `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)`> `[addPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addPart(com.google.firebase.vertexai.type.Part))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T data)` Adds a new [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder) | [addText](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#addText(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` text)` Adds a new [TextPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TextPart) with the provided [text](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).                                                                                                                                                                                                                                                                                                                                                                                                      |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#build())`()` Returns a new [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) using the defined [role](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#role()) and [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Public fields

### parts

```
publicÂ finalÂ @NonNull List<@NonNull Part>Â parts
```

The mutable list of [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)s comprising the [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content).

Prefer using the provided helper methods over modifying this list directly.  

### role

```
publicÂ finalÂ StringÂ role
```

The producer of the content. Must be either 'user' or 'model'. By default, it's "user".  

## Public constructors

### Builder

```
publicÂ Builder()
```  

## Public methods

### addFileData

```
publicÂ finalÂ @NonNull Content.BuilderÂ addFileData(@NonNull StringÂ uri,Â @NonNull StringÂ mimeType)
```

Adds a new [FileDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart) with the provided [uri](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)) and [mimeType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#fileData(kotlin.String,kotlin.String)) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).  

### addImage

```
publicÂ finalÂ @NonNull Content.BuilderÂ addImage(@NonNull BitmapÂ image)
```

Adds a new [ImagePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart) with the provided [image](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#image(android.graphics.Bitmap)) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).  

### addInlineData

```
publicÂ finalÂ @NonNull Content.BuilderÂ addInlineData(@NonNull byte[]Â bytes,Â @NonNull StringÂ mimeType)
```

Adds a new [InlineDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart) with the provided [bytes](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)), which should be interpreted by the model based on the [mimeType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#inlineData(kotlin.ByteArray,kotlin.String)), to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).  

### addPart

```
publicÂ finalÂ @NonNull Content.BuilderÂ <TÂ extendsÂ Part> addPart(@NonNull TÂ data)
```

Adds a new [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).  

### addText

```
publicÂ finalÂ @NonNull Content.BuilderÂ addText(@NonNull StringÂ text)
```

Adds a new [TextPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TextPart) with the provided [text](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#text(kotlin.String)) to [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).  

### build

```
publicÂ finalÂ @NonNull ContentÂ build()
```

Returns a new [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) using the defined [role](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#role()) and [parts](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content.Builder#parts()).