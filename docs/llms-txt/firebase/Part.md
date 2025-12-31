# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.md.txt

# Part


```
interface Part
```

<br />

Known direct subclasses  
[CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart), [ExecutableCodePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart), [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart), [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart), [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart), [ImagePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart), [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart), [TextPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/TextPart)  

|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart) | Represents the code execution result from the model.                                          |
| [ExecutableCodePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart)           | Represents the code that was executed by the model.                                           |
| [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart)                       | Represents file data stored in Cloud Storage for Firebase, referenced by URI.                 |
| [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)               | Represents function call name and params received from requests.                              |
| [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)       | Represents function call output to be returned to the model when it requests a function call. |
| [ImagePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart)                             | Represents image data sent to and received from requests.                                     |
| [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart)                   | Represents binary data with an associated MIME type sent to and received from requests.       |
| [TextPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/TextPart)                               | Represents text or string based data sent to and received from requests.                      |

*** ** * ** ***

Interface representing data sent to and received from requests.

## Summary

|                               ### Public properties                                |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isThought](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#isThought()) |

|                                              ### Extension functions                                              |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart)`?`     | [Part](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part)`.`[asFileDataOrNull](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asFileDataOrNull())`()` Returns the part as a [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart) if it represents a file, and null otherwise                      |
| [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)`?`                          | [Part](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part)`.`[asImageOrNull](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asImageOrNull())`()` Returns the part as a [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html) if it represents an image, and null otherwise                                               |
| [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart)`?` | [Part](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part)`.`[asInlineDataPartOrNull](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asInlineDataPartOrNull())`()` Returns the part as a [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart) if it represents inline data, and null otherwise |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                               | [Part](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part)`.`[asTextOrNull](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asTextOrNull())`()` Returns the part as a [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) if it represents text, and null otherwise                                                          |

## Public properties

### isThought

```
valÂ isThought:Â Boolean
```  

## Extension functions

### asFileDataOrNull

```
funÂ Part.asFileDataOrNull():Â FileDataPart?
```

Returns the part as a [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart) if it represents a file, and null otherwise  

### asImageOrNull

```
funÂ Part.asImageOrNull():Â Bitmap?
```

Returns the part as a [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html) if it represents an image, and null otherwise  

### asInlineDataPartOrNull

```
funÂ Part.asInlineDataPartOrNull():Â InlineDataPart?
```

Returns the part as a [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart) if it represents inline data, and null otherwise  

### asTextOrNull

```
funÂ Part.asTextOrNull():Â String?
```

Returns the part as a [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) if it represents text, and null otherwise