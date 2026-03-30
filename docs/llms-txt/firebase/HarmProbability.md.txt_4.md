# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability.md.txt

# HarmProbability

# HarmProbability


```
class HarmProbability
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents the probability that some `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` is applicable in a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating`.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability.Companion#HIGH()` Probability for harm is high. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability.Companion#LOW()` Probability for harm is low. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability.Companion#MEDIUM()` Probability for harm is medium. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability.Companion#NEGLIGIBLE()` Probability for harm is negligible. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability.Companion#UNKNOWN()` A new and not yet supported value. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability#ordinal()` |

## Public companion properties

### HIGH

```
val HIGH: HarmProbability
```

Probability for harm is high.

### LOW

```
val LOW: HarmProbability
```

Probability for harm is low.

### MEDIUM

```
val MEDIUM: HarmProbability
```

Probability for harm is medium.

### NEGLIGIBLE

```
val NEGLIGIBLE: HarmProbability
```

Probability for harm is negligible.

### UNKNOWN

```
val UNKNOWN: HarmProbability
```

A new and not yet supported value.

## Public properties

### ordinal

```
val ordinal: Int
```