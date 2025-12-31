# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting/HarmBlockMethod.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.md.txt

# HarmBlockMethod

# HarmBlockMethod


```
class HarmBlockMethod
```

<br />

*** ** * ** ***

Specifies how the block method computes the score that will be compared against the [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) in [SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting).

## Summary

|                                         ### Public companion properties                                          |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HarmBlockMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod) | [PROBABILITY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.Companion#PROBABILITY()) The harm block method uses the probability score.          |
| [HarmBlockMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod) | [SEVERITY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.Companion#SEVERITY()) The harm block method uses both probability and severity scores. |

|                           ### Public properties                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ordinal](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod#ordinal()) |

## Public companion properties

### PROBABILITY

```
valÂ PROBABILITY:Â HarmBlockMethod
```

The harm block method uses the probability score. See [HarmProbability](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmProbability).  

### SEVERITY

```
valÂ SEVERITY:Â HarmBlockMethod
```

The harm block method uses both probability and severity scores. See [HarmSeverity](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity) and [HarmProbability](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmProbability).  

## Public properties

### ordinal

```
valÂ ordinal:Â Int
```