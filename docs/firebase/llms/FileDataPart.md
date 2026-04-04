# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart.md.txt

# FileDataPart


```
class FileDataPart : Part
```

<br />

*** ** * ** ***

Represents file data stored in Cloud Storage for Firebase, referenced by URI.

## Summary

|                                                                                                                                                            ### Public constructors                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#FileDataPart(kotlin.String,kotlin.String))`(uri: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` |

|                                   ### Public properties                                   |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `open `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isThought](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#isThought()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)          | [mimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#mimeType())   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)          | [uri](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#uri())             |

## Public constructors

### FileDataPart

```
FileDataPart(uri:Â String,Â mimeType:Â String)
```  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uri: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)      | The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"`                                           |
| `mimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |

## Public properties

### isThought

```
openÂ valÂ isThought:Â Boolean
```  

### mimeType

```
valÂ mimeType:Â String
```  

### uri

```
valÂ uri:Â String
```