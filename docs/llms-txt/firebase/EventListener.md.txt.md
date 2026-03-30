# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener.md.txt

# EventListener

# EventListener


```
public interface EventListener<T>
```

<br />

*** ** * ** ***

An interface for event listeners.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener#onEvent(T,com.google.firebase.firestore.FirebaseFirestoreException)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException error)` `onEvent` will be called with the new value or the error if an error occurred. |

## Public methods

### onEvent

```
abstract void onEvent(@Nullable T value, @Nullable FirebaseFirestoreException error)
```

`onEvent` will be called with the new value or the error if an error occurred. It's guaranteed that exactly one of value or error will be non-`null`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T value` | The value of the event. `null` if there was an error. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException error` | The error if there was error. `null` otherwise. |