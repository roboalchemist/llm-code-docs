# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.md.txt

# BlockReason

# BlockReason


```
public final class BlockReason
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Describes why content was blocked.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.Companion#BLOCKLIST()` Content was blocked for another reason. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.Companion#OTHER()` Content was blocked for another reason. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.Companion#PROHIBITED_CONTENT()` Candidates blocked due to the terms which are included from the terminology blocklist. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.Companion#SAFETY()` Content was blocked for violating provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.Companion#UNKNOWN()` A new and not yet supported value. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason#name()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason#ordinal()` |

## Public fields

### BLOCKLIST

```
public static final @NonNull BlockReason BLOCKLIST
```

Content was blocked for another reason.

### OTHER

```
public static final @NonNull BlockReason OTHER
```

Content was blocked for another reason.

### PROHIBITED_CONTENT

```
public static final @NonNull BlockReason PROHIBITED_CONTENT
```

Candidates blocked due to the terms which are included from the terminology blocklist.

### SAFETY

```
public static final @NonNull BlockReason SAFETY
```

Content was blocked for violating provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting`.

### UNKNOWN

```
public static final @NonNull BlockReason UNKNOWN
```

A new and not yet supported value.

### name

```
public final @NonNull String name
```

### ordinal

```
public final int ordinal
```