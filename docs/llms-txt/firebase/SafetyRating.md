# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating.md.txt

# SafetyRating

<br />

```
class SafetyRating
```

<br />

*** ** * ** ***

An assessment of the potential harm of some generated content.

The rating will be restricted to a particular[category](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#category()).

## Summary

|                                              ### Public properties                                               |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?`                            | [blocked](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#blocked()) Indicates whether the content was blocked due to safety concerns.                           |
| [HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory)       | [category](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#category()) The category of harm being assessed (for example, Hate speech).                           |
| [HarmProbability](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmProbability) | [probability](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#probability()) The likelihood of the content causing harm.                                         |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)                                   | [probabilityScore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#probabilityScore()) A numerical score representing the probability of harm, between`0`and`1`. |
| [HarmSeverity](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity)`?`    | [severity](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#severity()) The severity of the potential harm.                                                       |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                | [severityScore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating#severityScore()) A numerical score representing the severity of harm.                            |

## Public properties

### blocked

```
valÂ blocked:Â Boolean?
```

Indicates whether the content was blocked due to safety concerns.  

### category

```
valÂ category:Â HarmCategory
```

The category of harm being assessed (for example, Hate speech).  

### probability

```
valÂ probability:Â HarmProbability
```

The likelihood of the content causing harm.  

### probabilityScore

```
valÂ probabilityScore:Â Float
```

A numerical score representing the probability of harm, between`0`and`1`.  

### severity

```
valÂ severity:Â HarmSeverity?
```

The severity of the potential harm.  

### severityScore

```
valÂ severityScore:Â Float?
```

A numerical score representing the severity of harm.