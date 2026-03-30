# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration.md.txt

# ListenerRegistration

# ListenerRegistration


```
interface ListenerRegistration
```

<br />

*** ** * ** ***

Represents a listener that can be removed by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration#remove()`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration#remove()()` Removes the listener being tracked by this `ListenerRegistration`. |

## Public functions

### remove

```
fun remove(): Unit
```

Removes the listener being tracked by this `ListenerRegistration`. After the initial call, subsequent calls have no effect.