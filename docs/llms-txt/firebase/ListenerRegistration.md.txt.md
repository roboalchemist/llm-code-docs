# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration.md.txt

# ListenerRegistration

# ListenerRegistration


```
public interface ListenerRegistration
```

<br />

*** ** * ** ***

Represents a listener that can be removed by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration#remove()`.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration#remove()()` Removes the listener being tracked by this `ListenerRegistration`. |

## Public methods

### remove

```
abstract void remove()
```

Removes the listener being tracked by this `ListenerRegistration`. After the initial call, subsequent calls have no effect.