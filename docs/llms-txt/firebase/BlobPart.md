# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlobPart.md.txt

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

|                                                                                                                                                              ### Public constructors                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BlobPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart#BlobPart(kotlin.String,kotlin.ByteArray))`(mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, blob: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`)` |

|                                  ### Public properties                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | [blob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart#blob()) the binary data as a [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)        | [mimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlobPart#mimeType()) an IANA standard MIME type.                                                                          |

## Public constructors

### BlobPart

```
BlobPart(mimeType:Â String,Â blob:Â ByteArray)
```  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)    | an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) . |
| `blob: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | the binary data as a [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)                                                                                       |

## Public properties

### blob

```
valÂ blob:Â ByteArray
```

the binary data as a [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)  

### mimeType

```
valÂ mimeType:Â String
```

an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) .