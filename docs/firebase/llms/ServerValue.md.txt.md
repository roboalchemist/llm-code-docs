# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ServerValue.md.txt

# ServerValue

# ServerValue


```
public class ServerValue
```

<br />

*** ** * ** ***

Contains placeholder values to use when writing data to the Firebase Database.

## Summary

| ### Constants |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ServerValue#TIMESTAMP()` A placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) by the Firebase Database servers. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ServerValue#ServerValue()()` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ServerValue#increment(long)(long delta)` Returns a placeholder value that can be used to atomically increment the current database value by the provided delta. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ServerValue#increment(double)(double delta)` Returns a placeholder value that can be used to atomically increment the current database value by the provided delta. |

## Constants

### TIMESTAMP

```
public static final @NonNull Map<String, String> TIMESTAMP
```

A placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) by the Firebase Database servers.

## Public constructors

### ServerValue

```
public ServerValue()
```

## Public methods

### increment

```
public static final @NonNull Object increment(long delta)
```

Returns a placeholder value that can be used to atomically increment the current database value by the provided delta.

The delta must be an long or a double value. If the current value is not a number, or if the database value does not yet exist, the transformation will set the database value to the delta value. If either the delta value or the existing value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the sum is calculated as a double.

| Parameters |
|---|---|
| `long delta` | the amount to modify the current value atomically. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | a placeholder value for modifying data atomically server-side. |

### increment

```
public static final @NonNull Object increment(double delta)
```

Returns a placeholder value that can be used to atomically increment the current database value by the provided delta.

The delta must be an long or a double value. If the current value is not an integer or double, or if the data does not yet exist, the transformation will set the data to the delta value. If either of the delta value or the existing data are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the sum is calculated as a a double.

| Parameters |
|---|---|
| `double delta` | the amount to modify the current value atomically. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | a placeholder value for modifying data atomically server-side. |