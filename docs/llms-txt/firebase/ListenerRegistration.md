# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration.md.txt

# ListenerRegistration

# ListenerRegistration


```
interface ListenerRegistration
```

<br />

*** ** * ** ***

Represents a listener that can be removed by calling [remove](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration#remove()).

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [remove](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration#remove())`()` Removes the listener being tracked by this `ListenerRegistration`. |

## Public functions

### remove

```
funÂ remove():Â Unit
```

Removes the listener being tracked by this `ListenerRegistration`. After the initial call, subsequent calls have no effect.