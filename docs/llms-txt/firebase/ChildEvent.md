# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.md.txt

# ChildEvent

# ChildEvent


```
sealed class ChildEvent
```

<br />

Known direct subclasses  
[ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added), [ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed), [ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved), [ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed)  

|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added)     | Emitted when a new child is added to the location.     |
| [ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed) | Emitted when the data at a child location has changed. |
| [ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved)     | Emitted when a child location's priority changes.      |
| [ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed) | Emitted when a child is removed from the location.     |

*** ** * ** ***

Used to emit events about changes in the child locations of a given [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) when using the [childEvents](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).childEvents()) Flow.

## Summary

|                                                                                                                                            ### Nested types                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data class `[ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added)` : `[ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) Emitted when a new child is added to the location.         |
| `data class `[ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed)` : `[ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) Emitted when the data at a child location has changed. |
| `data class `[ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved)` : `[ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) Emitted when a child location's priority changes.          |
| `data class `[ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed)` : `[ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) Emitted when a child is removed from the location.     |

|                                                ### Protected constructors                                                |
|--------------------------------------------------------------------------------------------------------------------------|
| [ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent#ChildEvent())`()` |

## Protected constructors

### ChildEvent

```
protectedÂ ChildEvent()
```