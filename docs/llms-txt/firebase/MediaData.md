# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData.md.txt

# MediaData

<br />

```
@PublicPreviewAPI
class MediaData
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| Use \`InlineData\` instead

Represents the media data to be sent to the server

## Summary

|                                                                                                                                                             ### Public constructors                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MediaData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData#MediaData(kotlin.ByteArray,kotlin.String))`(data: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`, mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` |

|                                  ### Public properties                                  |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | [data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData#data()) Byte array representing the data to be sent. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)        | [mimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData#mimeType()) an IANA standard MIME type.          |

## Public constructors

### MediaData

```
MediaData(data:Â ByteArray,Â mimeType:Â String)
```  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | Byte array representing the data to be sent.                                                                                                                    |
| `mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)    | an IANA standard MIME type. For supported MIME type values see the[Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |

## Public properties

### data

```
valÂ data:Â ByteArray
```

Byte array representing the data to be sent.  

### mimeType

```
valÂ mimeType:Â String
```

an IANA standard MIME type. For supported MIME type values see the[Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements).