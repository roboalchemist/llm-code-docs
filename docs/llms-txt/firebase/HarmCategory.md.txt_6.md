# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.md.txt

# HarmCategory

# HarmCategory


```
class HarmCategory
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Category for a given harm rating.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.Companion#CIVIC_INTEGRITY()` Content that may be used to harm civic integrity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.Companion#DANGEROUS_CONTENT()` Dangerous content. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.Companion#HARASSMENT()` Harassment content. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.Companion#HATE_SPEECH()` Hate speech and content. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.Companion#SEXUALLY_EXPLICIT()` Sexually explicit content. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory.Companion#UNKNOWN()` A new and not yet supported value. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory#ordinal()` |

## Public companion properties

### CIVIC_INTEGRITY

```
val CIVIC_INTEGRITY: HarmCategory
```

Content that may be used to harm civic integrity.

### DANGEROUS_CONTENT

```
val DANGEROUS_CONTENT: HarmCategory
```

Dangerous content.

### HARASSMENT

```
val HARASSMENT: HarmCategory
```

Harassment content.

### HATE_SPEECH

```
val HATE_SPEECH: HarmCategory
```

Hate speech and content.

### SEXUALLY_EXPLICIT

```
val SEXUALLY_EXPLICIT: HarmCategory
```

Sexually explicit content.

### UNKNOWN

```
val UNKNOWN: HarmCategory
```

A new and not yet supported value.

## Public properties

### ordinal

```
val ordinal: Int
```