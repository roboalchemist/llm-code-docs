# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part.md.txt

# Part

# Part


```
public interface Part
```

<br />

Known direct subclasses [FileDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart), [FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart), [FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart), [ImagePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart), [InlineDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart), [TextPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TextPart)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart` | **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart` | **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart` | **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart` | **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart` | **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TextPart` | **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |

*** ** * ** ***

> [!CAUTION]
> **This interface is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Interface representing data sent to and received from requests.

## Summary

| ### Extension functions |
|---|---|
| `default final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part#(com.google.firebase.vertexai.type.Part).asFileDataOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part receiver)` Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart` if it represents a file, and null otherwise |
| `default final https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part#(com.google.firebase.vertexai.type.Part).asImageOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part receiver)` Returns the part as a `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` if it represents an image, and null otherwise |
| `default final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part#(com.google.firebase.vertexai.type.Part).asInlineDataPartOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part receiver)` Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart` if it represents inline data, and null otherwise |
| `default final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part#(com.google.firebase.vertexai.type.Part).asTextOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part receiver)` Returns the part as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` if it represents text, and null otherwise |

## Extension functions

### PartKt.asFileDataOrNull

```
default final FileDataPart PartKt.asFileDataOrNull(@NonNull Part receiver)
```

Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart` if it represents a file, and null otherwise

### PartKt.asImageOrNull

```
default final Bitmap PartKt.asImageOrNull(@NonNull Part receiver)
```

Returns the part as a `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` if it represents an image, and null otherwise

### PartKt.asInlineDataPartOrNull

```
default final InlineDataPart PartKt.asInlineDataPartOrNull(@NonNull Part receiver)
```

Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart` if it represents inline data, and null otherwise

### PartKt.asTextOrNull

```
default final String PartKt.asTextOrNull(@NonNull Part receiver)
```

Returns the part as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` if it represents text, and null otherwise