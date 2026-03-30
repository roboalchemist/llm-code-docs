# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlobPart.md.txt

# BlobPart

# BlobPart


```
public final class BlobPart implements Part
```

<br />

*** ** * ** ***

Represents binary data with an associated MIME type sent to and received from requests.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlobPart#blob()` the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlobPart#mimeType()` an IANA standard MIME type. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlobPart#BlobPart(kotlin.String,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] blob)` |

## Public fields

### blob

```
public final @NonNull byte[] blob
```

the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html`

### mimeType

```
public final @NonNull String mimeType
```

an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) .

## Public constructors

### BlobPart

```
public BlobPart(@NonNull String mimeType, @NonNull byte[] blob)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType` | an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) . |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] blob` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |