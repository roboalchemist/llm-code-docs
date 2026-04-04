# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.md.txt

# ChildEvent

# ChildEvent


```
public class ChildEvent
```

<br />

Known direct subclasses [ChildEvent.Added](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added), [ChildEvent.Changed](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed), [ChildEvent.Moved](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved), [ChildEvent.Removed](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added` | Emitted when a new child is added to the location. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed` | Emitted when the data at a child location has changed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved` | Emitted when a child location's priority changes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed` | Emitted when a child is removed from the location. |

*** ** * ** ***

Used to emit events about changes in the child locations of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` when using the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).childEvents()` Flow.

## Summary

| ### Nested types |
|---|
| `public final data class https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added extends https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent` Emitted when a new child is added to the location. |
| `public final data class https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed extends https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent` Emitted when the data at a child location has changed. |
| `public final data class https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved extends https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent` Emitted when a child location's priority changes. |
| `public final data class https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed extends https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent` Emitted when a child is removed from the location. |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent#ChildEvent()()` |

## Protected constructors

### ChildEvent

```
protected ChildEvent()
```