# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse.md.txt

# ImagenGenerationResponse


```
class ImagenGenerationResponse<TÂ :Â Any?>
```

<br />

*** ** * ** ***

Represents a response from a call to [ImagenModel.generateImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#generateImages(kotlin.String))

## Summary

|                                     ### Public properties                                     |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`           | [filteredReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse#filteredReason()) if fewer images were generated than were requested, this field will contain the reason they were filtered out. |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<T>` | [images](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse#images()) contains the generated images                                                                                                  |

## Public properties

### filteredReason

```
valÂ filteredReason:Â String?
```

if fewer images were generated than were requested, this field will contain the reason they were filtered out.  

### images

```
valÂ images:Â List<T>
```

contains the generated images