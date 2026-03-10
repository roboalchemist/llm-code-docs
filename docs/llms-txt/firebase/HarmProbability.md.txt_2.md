# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.md.txt

# HarmProbability

# HarmProbability


```
public final class HarmProbability
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents the probability that some `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory` is applicable in a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating`.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.Companion#HIGH()` Probability for harm is high. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.Companion#LOW()` Probability for harm is low. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.Companion#MEDIUM()` Probability for harm is medium. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.Companion#NEGLIGIBLE()` Probability for harm is negligible. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability.Companion#UNKNOWN()` A new and not yet supported value. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability#ordinal()` |

## Public fields

### HIGH

```
public static final @NonNull HarmProbability HIGH
```

Probability for harm is high.

### LOW

```
public static final @NonNull HarmProbability LOW
```

Probability for harm is low.

### MEDIUM

```
public static final @NonNull HarmProbability MEDIUM
```

Probability for harm is medium.

### NEGLIGIBLE

```
public static final @NonNull HarmProbability NEGLIGIBLE
```

Probability for harm is negligible.

### UNKNOWN

```
public static final @NonNull HarmProbability UNKNOWN
```

A new and not yet supported value.

### ordinal

```
public final int ordinal
```