# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Removed.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Removed.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed.md.txt

# ChildEvent.Removed

# ChildEvent.Removed


```
data class ChildEvent.Removed : ChildEvent
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                          |||
| â³ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent)                    ||
|   | â³ | [com.google.firebase.database.ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed) |

*** ** * ** ***

Emitted when a child is removed from the location.

## Summary

|                                                                                                                                  ### Public constructors                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed#Removed(com.google.firebase.database.DataSnapshot))`(snapshot: `[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)`)` |

|                                            ### Public properties                                            |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot) | [snapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed#snapshot()) An immutable snapshot of the data at the child that was removed. |

## Public constructors

### Removed

```
Removed(snapshot:Â DataSnapshot)
```  

|                                                       Parameters                                                        |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `snapshot: `[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot) | An immutable snapshot of the data at the child that was removed. |

## Public properties

### snapshot

```
valÂ snapshot:Â DataSnapshot
```

An immutable snapshot of the data at the child that was removed.