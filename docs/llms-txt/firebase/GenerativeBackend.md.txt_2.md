# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend.md.txt

# GenerativeBackend

# GenerativeBackend


```
class GenerativeBackend
```

<br />

*** ** * ** ***

Represents a reference to a backend for generative AI.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend.Companion#googleAI()()` References the Google Developer API backend. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend.Companion#vertexAI(kotlin.String)(location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` References the VertexAI Gemini API backend. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend#hashCode()()` |

## Public companion functions

### googleAI

```
fun googleAI(): GenerativeBackend
```

References the Google Developer API backend.

### vertexAI

```
fun vertexAI(location: String = "us-central1"): GenerativeBackend
```

References the VertexAI Gemini API backend.

| Parameters |
|---|---|
| `location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html = "us-central1"` | passes a valid cloud server location, defaults to "us-central1" |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```