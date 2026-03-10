# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating.md.txt

# SafetyRating

# SafetyRating


```
class SafetyRating
```

<br />

*** ** * ** ***

An assessment of the potential harm of some generated content.

The rating will be restricted to a particular `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#category()`.

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#blocked()` Indicates whether the content was blocked due to safety concerns. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#category()` The category of harm being assessed (for example, Hate speech). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmProbability` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#probability()` The likelihood of the content causing harm. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#probabilityScore()` A numerical score representing the probability of harm, between `0` and `1`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#severity()` The severity of the potential harm. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#severityScore()` A numerical score representing the severity of harm. |

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

The category of harm being assessed (for example, Hate speech).

### probability

```
val probability: HarmProbability
```

The likelihood of the content causing harm.

### probabilityScore

```
val probabilityScore: Float
```

A numerical score representing the probability of harm, between `0` and `1`.

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