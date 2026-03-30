# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.md.txt

# HarmBlockMethod

# HarmBlockMethod


```
class HarmBlockMethod
```

<br />

*** ** * ** ***

Specifies how the block method computes the score that will be compared against the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting`.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.Companion#PROBABILITY()` The harm block method uses the probability score. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.Companion#SEVERITY()` The harm block method uses both probability and severity scores. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod#ordinal()` |

## Public companion properties

### PROBABILITY

```
val PROBABILITY: HarmBlockMethod
```

The harm block method uses the probability score. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmProbability`.

### SEVERITY

```
val SEVERITY: HarmBlockMethod
```

The harm block method uses both probability and severity scores. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmProbability`.

## Public properties

### ordinal

```
val ordinal: Int
```