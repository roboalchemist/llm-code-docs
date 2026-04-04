# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener.md.txt

# OnProgressListener

# OnProgressListener


```
interface OnProgressListener
```

<br />

*** ** * ** ***

A listener that is called periodically during execution of the [UpdateTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask).

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onProgressUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener#onProgressUpdate(com.google.firebase.appdistribution.UpdateProgress))`(updateState: `[UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress)`)` Called periodically for progress update and state changes of the [UpdateTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask). |

## Public functions

### onProgressUpdate

```
funÂ onProgressUpdate(updateState:Â UpdateProgress):Â Unit
```

Called periodically for progress update and state changes of the [UpdateTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask).