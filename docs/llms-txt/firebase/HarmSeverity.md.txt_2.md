# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.md.txt

# HarmSeverity

# HarmSeverity


```
public final class HarmSeverity
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents the severity of a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory` being applicable in a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating`.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.Companion#HIGH()` High level of harm severity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.Companion#LOW()` Low level of harm severity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.Companion#MEDIUM()` Medium level of harm severity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.Companion#NEGLIGIBLE()` Severity for harm is negligible. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.Companion#UNKNOWN()` A new and not yet supported value. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity#ordinal()` |

## Public fields

### HIGH

```
public static final @NonNull HarmSeverity HIGH
```

High level of harm severity.

### LOW

```
public static final @NonNull HarmSeverity LOW
```

Low level of harm severity.

### MEDIUM

```
public static final @NonNull HarmSeverity MEDIUM
```

Medium level of harm severity.

### NEGLIGIBLE

```
public static final @NonNull HarmSeverity NEGLIGIBLE
```

Severity for harm is negligible.

### UNKNOWN

```
public static final @NonNull HarmSeverity UNKNOWN
```

A new and not yet supported value.

### ordinal

```
public final int ordinal
```