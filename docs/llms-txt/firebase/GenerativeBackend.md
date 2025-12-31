# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend.md.txt

# GenerativeBackend


```
class GenerativeBackend
```

<br />

*** ** * ** ***

Represents a reference to a backend for generative AI.

## Summary

|                                            ### Public companion functions                                            |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GenerativeBackend](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend) | [googleAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend.Companion#googleAI())`()` References the Google Developer API backend.                                                                                                         |
| [GenerativeBackend](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend) | [vertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend.Companion#vertexAI(kotlin.String))`(location: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` References the VertexAI Gemini API backend. |

## Public companion functions

### googleAI

```
funÂ googleAI():Â GenerativeBackend
```

References the Google Developer API backend.  

### vertexAI

```
funÂ vertexAI(location:Â String = "us-central1"):Â GenerativeBackend
```

References the VertexAI Gemini API backend.  

|                                                   Parameters                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `location: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` = "us-central1"` | passes a valid cloud server location, defaults to "us-central1" |