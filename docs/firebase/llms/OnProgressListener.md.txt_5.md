# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener.md.txt

# OnProgressListener

# OnProgressListener


```
interface OnProgressListener
```

<br />

*** ** * ** ***

A listener that is called periodically during execution of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener#onProgressUpdate(com.google.firebase.appdistribution.UpdateProgress)(updateState: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress)` Called periodically for progress update and state changes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask`. |

## Public functions

### onProgressUpdate

```
fun onProgressUpdate(updateState: UpdateProgress): Unit
```

Called periodically for progress update and state changes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask`.