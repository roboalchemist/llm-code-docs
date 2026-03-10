# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.md.txt

# BlockReason

# BlockReason


```
class BlockReason
```

<br />

*** ** * ** ***

Describes why content was blocked.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.Companion#BLOCKLIST()` Content was blocked for another reason. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.Companion#OTHER()` Content was blocked for another reason. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.Companion#PROHIBITED_CONTENT()` Candidates blocked due to the terms which are included from the terminology blocklist. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.Companion#SAFETY()` Content was blocked for violating provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.Companion#UNKNOWN()` A new and not yet supported value. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason#name()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason#ordinal()` |

## Public companion properties

### BLOCKLIST

```
val BLOCKLIST: BlockReason
```

Content was blocked for another reason.

### OTHER

```
val OTHER: BlockReason
```

Content was blocked for another reason.

### PROHIBITED_CONTENT

```
val PROHIBITED_CONTENT: BlockReason
```

Candidates blocked due to the terms which are included from the terminology blocklist.

### SAFETY

```
val SAFETY: BlockReason
```

Content was blocked for violating provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting`.

### UNKNOWN

```
val UNKNOWN: BlockReason
```

A new and not yet supported value.

## Public properties

### name

```
val name: String
```

### ordinal

```
val ordinal: Int
```