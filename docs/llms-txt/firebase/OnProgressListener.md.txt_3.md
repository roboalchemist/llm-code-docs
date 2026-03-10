# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/OnProgressListener.md.txt

# OnProgressListener

# OnProgressListener


```
public interface OnProgressListener
```

<br />

*** ** * ** ***

A listener that is called periodically during execution of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask`.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/OnProgressListener#onProgressUpdate(com.google.firebase.appdistribution.UpdateProgress)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress updateState)` Called periodically for progress update and state changes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask`. |

## Public methods

### onProgressUpdate

```
abstract void onProgressUpdate(@NonNull UpdateProgress updateState)
```

Called periodically for progress update and state changes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask`.