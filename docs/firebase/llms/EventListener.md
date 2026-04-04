# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener.md.txt

# EventListener

# EventListener


```
interface EventListener<T>
```

<br />

*** ** * ** ***

An interface for event listeners.

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener#onEvent(T,com.google.firebase.firestore.FirebaseFirestoreException))`(value: T?, error: `[FirebaseFirestoreException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException)`?)` `onEvent` will be called with the new value or the error if an error occurred. |

## Public functions

### onEvent

```
funÂ onEvent(value:Â T?,Â error:Â FirebaseFirestoreException?):Â Unit
```

`onEvent` will be called with the new value or the error if an error occurred. It's guaranteed that exactly one of value or error will be non-`null`.  

|                                                                      Parameters                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `value: T?`                                                                                                                                          | The value of the event. `null` if there was an error. |
| `error: `[FirebaseFirestoreException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException)`?` | The error if there was error. `null` otherwise.       |