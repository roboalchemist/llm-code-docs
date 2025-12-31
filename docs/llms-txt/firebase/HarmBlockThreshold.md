# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.md.txt

# HarmBlockThreshold

# HarmBlockThreshold


```
class HarmBlockThreshold
```

<br />

*** ** * ** ***

Represents the threshold for a [HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory) to be allowed by [SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting).

## Summary

|                                            ### Public companion properties                                             |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) | [LOW_AND_ABOVE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#LOW_AND_ABOVE()) Content with negligible harm is allowed.              |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) | [MEDIUM_AND_ABOVE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#MEDIUM_AND_ABOVE()) Content with negligible to low harm is allowed. |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) | [NONE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#NONE()) All content is allowed regardless of harm.                              |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) | [OFF](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#OFF()) All content is allowed regardless of harm.                                |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) | [ONLY_HIGH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#ONLY_HIGH()) Content with negligible to medium harm is allowed.            |

|                           ### Public properties                            |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ordinal](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold#ordinal()) |

## Public companion properties

### LOW_AND_ABOVE

```
valÂ LOW_AND_ABOVE:Â HarmBlockThreshold
```

Content with negligible harm is allowed.  

### MEDIUM_AND_ABOVE

```
valÂ MEDIUM_AND_ABOVE:Â HarmBlockThreshold
```

Content with negligible to low harm is allowed.  

### NONE

```
valÂ NONE:Â HarmBlockThreshold
```

All content is allowed regardless of harm.  

### OFF

```
valÂ OFF:Â HarmBlockThreshold
```

All content is allowed regardless of harm.

The same as [NONE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#NONE()), but metadata when the corresponding [HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory) occurs will **NOT** be present in the response.  

### ONLY_HIGH

```
valÂ ONLY_HIGH:Â HarmBlockThreshold
```

Content with negligible to medium harm is allowed.  

## Public properties

### ordinal

```
valÂ ordinal:Â Int
```