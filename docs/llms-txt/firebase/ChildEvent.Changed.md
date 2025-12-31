# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Changed.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Changed.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Changed.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed.md.txt

# ChildEvent.Changed

# ChildEvent.Changed


```
data class ChildEvent.Changed : ChildEvent
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                          |||
| â³ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent)                    ||
|   | â³ | [com.google.firebase.database.ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed) |

*** ** * ** ***

Emitted when the data at a child location has changed.

## Summary

|                                                                                                                                                                                             ### Public constructors                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed#Changed(com.google.firebase.database.DataSnapshot,kotlin.String))`(snapshot: `[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)`, previousChildName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` |

|                                            ### Public properties                                            |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                         | [previousChildName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed#previousChildName()) The key name of sibling location ordered before the child. |
| [DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot) | [snapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed#snapshot()) An immutable snapshot of the data at the new data at the child location      |

## Public constructors

### Changed

```
Changed(snapshot:Â DataSnapshot,Â previousChildName:Â String?)
```  

|                                                       Parameters                                                        |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `snapshot: `[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot) | An immutable snapshot of the data at the new data at the child location                                                            |
| `previousChildName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                | The key name of sibling location ordered before the child. This will ```kotlin be null for the first child node of a location. ``` |

## Public properties

### previousChildName

```
valÂ previousChildName:Â String?
```

The key name of sibling location ordered before the child. This will  

```kotlin
    be null for the first child node of a location.
```  

### snapshot

```
valÂ snapshot:Â DataSnapshot
```

An immutable snapshot of the data at the new data at the child location