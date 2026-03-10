# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount.md.txt

# ModalityTokenCount

# ModalityTokenCount


```
class ModalityTokenCount
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents token counting info for a single modality.

## Summary

| ### Public functions |
|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ContentModality` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount#component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount#component2()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ContentModality` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount#modality()` The modality associated with this token count. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount#tokenCount()` The number of tokens counted. |

## Public functions

### component1

```
operator fun component1(): ContentModality
```

### component2

```
operator fun component2(): Int
```

## Public properties

### modality

```
val modality: ContentModality
```

The modality associated with this token count.

### tokenCount

```
val tokenCount: Int
```

The number of tokens counted.