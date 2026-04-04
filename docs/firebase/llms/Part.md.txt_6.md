# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.md.txt

# Part

# Part


```
interface Part
```

<br />

Known direct subclasses [CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart), [ExecutableCodePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart), [FileDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart), [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart), [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart), [ImagePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart), [InlineDataPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart), [TextPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/TextPart)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart` | Represents the code execution result from the model. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart` | Represents the code that was executed by the model. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart` | Represents file data stored in Cloud Storage for Firebase, referenced by URI. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart` | Represents function call name and params received from requests. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` | Represents function call output to be returned to the model when it requests a function call. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart` | Represents image data sent to and received from requests. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart` | Represents binary data with an associated MIME type sent to and received from requests. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/TextPart` | Represents text or string based data sent to and received from requests. |

*** ** * ** ***

Interface representing data sent to and received from requests.

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#isThought()` |

| ### Extension functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asFileDataOrNull()()` Returns the part as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart` if it represents a file, and null otherwise |
| `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asImageOrNull()()` Returns the part as a `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` if it represents an image, and null otherwise |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asInlineDataPartOrNull()()` Returns the part as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart` if it represents inline data, and null otherwise |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part#(com.google.firebase.ai.type.Part).asTextOrNull()()` Returns the part as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` if it represents text, and null otherwise |

## Public properties

### isThought

```
val isThought: Boolean
```

## Extension functions

### asFileDataOrNull

```
fun Part.asFileDataOrNull(): FileDataPart?
```

Returns the part as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart` if it represents a file, and null otherwise

### asImageOrNull

```
fun Part.asImageOrNull(): Bitmap?
```

Returns the part as a `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` if it represents an image, and null otherwise

### asInlineDataPartOrNull

```
fun Part.asInlineDataPartOrNull(): InlineDataPart?
```

Returns the part as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart` if it represents inline data, and null otherwise

### asTextOrNull

```
fun Part.asTextOrNull(): String?
```

Returns the part as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` if it represents text, and null otherwise