# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod.md.txt

# HarmBlockMethod

# HarmBlockMethod


```
class HarmBlockMethod
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Specifies how the block method computes the score that will be compared against the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockThreshold` in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting`.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod.Companion#PROBABILITY()` The harm block method uses the probability score. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod.Companion#SEVERITY()` The harm block method uses both probability and severity scores. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod#ordinal()` |

## Public companion properties

### PROBABILITY

```
val PROBABILITY: HarmBlockMethod
```

The harm block method uses the probability score. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability`.

### SEVERITY

```
val SEVERITY: HarmBlockMethod
```

The harm block method uses both probability and severity scores. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability`.

## Public properties

### ordinal

```
val ordinal: Int
```