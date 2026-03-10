# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating.md.txt

# SafetyRating

# SafetyRating


```
class SafetyRating
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

An assessment of the potential harm of some generated content.

The rating will be restricted to a particular `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#category()`.

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#blocked()` Indicates whether the content was blocked due to safety concerns. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#category()` The category of harm being assessed (e.g., Hate speech). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#probability()` The likelihood of the content causing harm. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#probabilityScore()` A numerical score representing the probability of harm, between 0 and |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#severity()` The severity of the potential harm. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating#severityScore()` A numerical score representing the severity of harm. |

## Public properties

### blocked

```
val blocked: Boolean?
```

Indicates whether the content was blocked due to safety concerns.

### category

```
val category: HarmCategory
```

The category of harm being assessed (e.g., Hate speech).

### probability

```
val probability: HarmProbability
```

The likelihood of the content causing harm.

### probabilityScore

```
val probabilityScore: Float
```

A numerical score representing the probability of harm, between 0 and

1. 

### severity

```
val severity: HarmSeverity?
```

The severity of the potential harm.

### severityScore

```
val severityScore: Float?
```

A numerical score representing the severity of harm.