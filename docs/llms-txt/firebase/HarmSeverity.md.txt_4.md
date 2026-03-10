# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.md.txt

# HarmSeverity

# HarmSeverity


```
class HarmSeverity
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents the severity of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` being applicable in a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating`.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.Companion#HIGH()` High level of harm severity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.Companion#LOW()` Low level of harm severity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.Companion#MEDIUM()` Medium level of harm severity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.Companion#NEGLIGIBLE()` Severity for harm is negligible. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.Companion#UNKNOWN()` A new and not yet supported value. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity#ordinal()` |

## Public companion properties

### HIGH

```
val HIGH: HarmSeverity
```

High level of harm severity.

### LOW

```
val LOW: HarmSeverity
```

Low level of harm severity.

### MEDIUM

```
val MEDIUM: HarmSeverity
```

Medium level of harm severity.

### NEGLIGIBLE

```
val NEGLIGIBLE: HarmSeverity
```

Severity for harm is negligible.

### UNKNOWN

```
val UNKNOWN: HarmSeverity
```

A new and not yet supported value.

## Public properties

### ordinal

```
val ordinal: Int
```