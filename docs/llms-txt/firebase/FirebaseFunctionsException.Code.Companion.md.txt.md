# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion.md.txt

# FirebaseFunctionsException.Code.Companion

# FirebaseFunctionsException.Code.Companion


```
public static class FirebaseFunctionsException.Code.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromHttpStatus(kotlin.Int)(int status)` Takes an HTTP status code and returns the corresponding `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` error code. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromValue(kotlin.Int)(int value)` |

## Public methods

### fromHttpStatus

```
public static final @NonNull FirebaseFunctionsException.Code fromHttpStatus(int status)
```

Takes an HTTP status code and returns the corresponding `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` error code. This is the standard HTTP status code -\> error mapping defined in: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto

| Parameters |
|---|---|
| `int status` | An HTTP status code. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` | The corresponding `Code`, or `Code.UNKNOWN` if none. |

### fromValue

```
public static final @NonNull FirebaseFunctionsException.Code fromValue(int value)
```