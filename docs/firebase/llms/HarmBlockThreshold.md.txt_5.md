# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.md.txt

# HarmBlockThreshold

# HarmBlockThreshold


```
class HarmBlockThreshold
```

<br />

*** ** * ** ***

Represents the threshold for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory` to be allowed by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting`.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#LOW_AND_ABOVE()` Content with negligible harm is allowed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#MEDIUM_AND_ABOVE()` Content with negligible to low harm is allowed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#NONE()` All content is allowed regardless of harm. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#OFF()` All content is allowed regardless of harm. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#ONLY_HIGH()` Content with negligible to medium harm is allowed. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold#ordinal()` |

## Public companion properties

### LOW_AND_ABOVE

```
val LOW_AND_ABOVE: HarmBlockThreshold
```

Content with negligible harm is allowed.

### MEDIUM_AND_ABOVE

```
val MEDIUM_AND_ABOVE: HarmBlockThreshold
```

Content with negligible to low harm is allowed.

### NONE

```
val NONE: HarmBlockThreshold
```

All content is allowed regardless of harm.

### OFF

```
val OFF: HarmBlockThreshold
```

All content is allowed regardless of harm.

The same as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold.Companion#NONE()`, but metadata when the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory` occurs will **NOT** be present in the response.

### ONLY_HIGH

```
val ONLY_HIGH: HarmBlockThreshold
```

Content with negligible to medium harm is allowed.

## Public properties

### ordinal

```
val ordinal: Int
```