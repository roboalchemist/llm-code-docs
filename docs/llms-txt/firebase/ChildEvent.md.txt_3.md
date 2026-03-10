# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.md.txt

# ChildEvent

# ChildEvent


```
sealed class ChildEvent
```

<br />

Known direct subclasses [ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added), [ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed), [ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved), [ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added` | Emitted when a new child is added to the location. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed` | Emitted when the data at a child location has changed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved` | Emitted when a child location's priority changes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed` | Emitted when a child is removed from the location. |

*** ** * ** ***

Used to emit events about changes in the child locations of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` when using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).childEvents()` Flow.

## Summary

| ### Nested types |
|---|
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent` Emitted when a new child is added to the location. |
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent` Emitted when the data at a child location has changed. |
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent` Emitted when a child location's priority changes. |
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent` Emitted when a child is removed from the location. |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent#ChildEvent()()` |

## Protected constructors

### ChildEvent

```
protected ChildEvent()
```