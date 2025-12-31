# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/InlineDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart.md.txt

# InlineDataPart

# InlineDataPart


```
class InlineDataPart : Part
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents binary data with an associated MIME type sent to and received from requests.

## Summary

|                                                                                                                                                                          ### Public constructors                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart#InlineDataPart(kotlin.ByteArray,kotlin.String))`(inlineData: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`, mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` |

|                                  ### Public properties                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | [inlineData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart#inlineData()) the binary data as a [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)        | [mimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InlineDataPart#mimeType()) an IANA standard MIME type.                                                                                      |

## Public constructors

### InlineDataPart

```
InlineDataPart(inlineData:Â ByteArray,Â mimeType:Â String)
```  

|                                              Parameters                                               |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inlineData: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | the binary data as a [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)                                                                                     |
| `mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)          | an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements) |

## Public properties

### inlineData

```
valÂ inlineData:Â ByteArray
```

the binary data as a [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)  

### mimeType

```
valÂ mimeType:Â String
```

an IANA standard MIME type. For supported values, see the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements)