# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.md.txt

# HarmSeverity

# HarmSeverity


```
class HarmSeverity
```

<br />

*** ** * ** ***

Represents the severity of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory` being applicable in a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating`.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.Companion#HIGH()` High level of harm severity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.Companion#LOW()` Low level of harm severity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.Companion#MEDIUM()` Medium level of harm severity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.Companion#NEGLIGIBLE()` Severity for harm is negligible. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.Companion#UNKNOWN()` A new and not yet supported value. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity#ordinal()` |

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