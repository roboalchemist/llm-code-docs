# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion.md.txt

# FirebaseFunctionsException.Code.Companion

# FirebaseFunctionsException.Code.Companion


```
public static class FirebaseFunctionsException.Code.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                        ### Public methods                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code) | [fromHttpStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromHttpStatus(kotlin.Int))`(int status)` Takes an HTTP status code and returns the corresponding [Code](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code) error code. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code) | [fromValue](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromValue(kotlin.Int))`(int value)`                                                                                                                                                                                                         |

## Public methods

### fromHttpStatus

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsException.CodeÂ fromHttpStatus(intÂ status)
```

Takes an HTTP status code and returns the corresponding [Code](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code) error code. This is the standard HTTP status code -\> error mapping defined in: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto  

|  Parameters  |
|--------------|----------------------|
| `int status` | An HTTP status code. |

|                                                                                                                       Returns                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code) | The corresponding `Code`, or `Code.UNKNOWN` if none. |

### fromValue

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsException.CodeÂ fromValue(intÂ value)
```