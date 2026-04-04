# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Moved.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved.md.txt

# ChildEvent.Moved

# ChildEvent.Moved


```
data class ChildEvent.Moved : ChildEvent
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                      |||
| â³ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent)                ||
|   | â³ | [com.google.firebase.database.ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved) |

*** ** * ** ***

Emitted when a child location's priority changes.

## Summary

|                                                                                                                                                                                          ### Public constructors                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved#Moved(com.google.firebase.database.DataSnapshot,kotlin.String))`(snapshot: `[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)`, previousChildName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` |

|                                            ### Public properties                                            |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                         | [previousChildName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved#previousChildName()) The key name of the sibling location ordered before the child |
| [DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot) | [snapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved#snapshot()) An immutable snapshot of the data at the location that moved.                   |

## Public constructors

### Moved

```
Moved(snapshot:Â DataSnapshot,Â previousChildName:Â String?)
```  

|                                                       Parameters                                                        |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `snapshot: `[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot) | An immutable snapshot of the data at the location that moved.                                                                              |
| `previousChildName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                | The key name of the sibling location ordered before the child ```kotlin location. This will be null if this location is ordered first. ``` |

## Public properties

### previousChildName

```
valÂ previousChildName:Â String?
```

The key name of the sibling location ordered before the child  

```kotlin
    location. This will be null if this location is ordered first.
```  

### snapshot

```
valÂ snapshot:Â DataSnapshot
```

An immutable snapshot of the data at the location that moved.