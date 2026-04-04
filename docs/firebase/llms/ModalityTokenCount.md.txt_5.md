# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount.md.txt

# ModalityTokenCount

# ModalityTokenCount


```
class ModalityTokenCount
```

<br />

*** ** * ** ***

Represents token counting info for a single modality.

## Summary

| ### Public functions |
|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ContentModality` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount#component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount#component2()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ContentModality` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount#modality()` The modality associated with this token count. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount#tokenCount()` The number of tokens counted. |

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