# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart.md.txt

# BlobPart

# BlobPart


```
class BlobPart : Part
```

<br />

*** ** * ** ***

Represents binary data with an associated MIME type sent to and received from requests.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart#BlobPart(kotlin.String,kotlin.ByteArray)(mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, blob: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart#blob()` the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart#mimeType()` an IANA standard MIME type. |

## Public constructors

### BlobPart

```
BlobPart(mimeType: String, blob: ByteArray)
```

| Parameters |
|---|---|
| `mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) . |
| `blob: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |

## Public properties

### blob

```
val blob: ByteArray
```

the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html`

### mimeType

```
val mimeType: String
```

an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) .