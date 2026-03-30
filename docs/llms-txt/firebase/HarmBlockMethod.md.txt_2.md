# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod.md.txt

# HarmBlockMethod

# HarmBlockMethod


```
public final class HarmBlockMethod
```

<br />

*** ** * ** ***

Specifies how the block method computes the score that will be compared against the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` in `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting`.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod.Companion#PROBABILITY()` The harm block method uses the probability score. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod.Companion#SEVERITY()` The harm block method uses both probability and severity scores. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod#ordinal()` |

## Public fields

### PROBABILITY

```
public static final @NonNull HarmBlockMethod PROBABILITY
```

The harm block method uses the probability score. See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmProbability`.

### SEVERITY

```
public static final @NonNull HarmBlockMethod SEVERITY
```

The harm block method uses both probability and severity scores. See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmSeverity` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmProbability`.

### ordinal

```
public final int ordinal
```