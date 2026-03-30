# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.md.txt

# HarmBlockThreshold

# HarmBlockThreshold


```
public final class HarmBlockThreshold
```

<br />

*** ** * ** ***

Represents the threshold for a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory` to be allowed by `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting`.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion#LOW_AND_ABOVE()` Content with negligible harm is allowed. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion#MEDIUM_AND_ABOVE()` Content with negligible to low harm is allowed. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion#NONE()` All content is allowed regardless of harm. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion#OFF()` All content is allowed regardless of harm. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion#ONLY_HIGH()` Content with negligible to medium harm is allowed. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold#ordinal()` |

## Public fields

### LOW_AND_ABOVE

```
public static final @NonNull HarmBlockThreshold LOW_AND_ABOVE
```

Content with negligible harm is allowed.

### MEDIUM_AND_ABOVE

```
public static final @NonNull HarmBlockThreshold MEDIUM_AND_ABOVE
```

Content with negligible to low harm is allowed.

### NONE

```
public static final @NonNull HarmBlockThreshold NONE
```

All content is allowed regardless of harm.

### OFF

```
public static final @NonNull HarmBlockThreshold OFF
```

All content is allowed regardless of harm.

The same as `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold.Companion#NONE()`, but metadata when the corresponding `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory` occurs will **NOT** be present in the response.

### ONLY_HIGH

```
public static final @NonNull HarmBlockThreshold ONLY_HIGH
```

Content with negligible to medium harm is allowed.

### ordinal

```
public final int ordinal
```