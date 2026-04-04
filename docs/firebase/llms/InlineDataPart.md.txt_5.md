# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart.md.txt

# InlineDataPart

# InlineDataPart


```
class InlineDataPart : Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents binary data with an associated MIME type sent to and received from requests.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart#InlineDataPart(kotlin.ByteArray,kotlin.String)(inlineData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart#inlineData()` the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart#mimeType()` an IANA standard MIME type. |

## Public constructors

### InlineDataPart

```
InlineDataPart(inlineData: ByteArray, mimeType: String)
```

| Parameters |
|---|---|
| `inlineData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) |

## Public properties

### inlineData

```
val inlineData: ByteArray
```

the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html`

### mimeType

```
val mimeType: String
```

an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements)