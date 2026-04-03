# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Added.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added.md.txt

# ChildEvent.Added

# ChildEvent.Added


```
public final data class ChildEvent.Added extends ChildEvent
```

<br />

|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                |||
| â³ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent)                ||
|   | â³ | [com.google.firebase.database.ChildEvent.Added](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added) |

*** ** * ** ***

Emitted when a new child is added to the location.

## Summary

|                                                                                                 ### Public fields                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                             | [previousChildName](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added#previousChildName()) The key name of sibling location ordered before the new child. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DataSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot) | [snapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added#snapshot()) An immutable snapshot of the data at the new child location                      |

|                                                                                                                                                                                                                                        ### Public constructors                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Added](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added#Added(com.google.firebase.database.DataSnapshot,kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DataSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot)` snapshot, `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` previousChildName)` |

## Public fields

### previousChildName

```
publicÂ finalÂ StringÂ previousChildName
```

The key name of sibling location ordered before the new child. This  

```text
    will be null for the first child node of a location.
```  

### snapshot

```
publicÂ finalÂ @NonNull DataSnapshotÂ snapshot
```

An immutable snapshot of the data at the new child location  

## Public constructors

### Added

```
publicÂ Added(@NonNull DataSnapshotÂ snapshot,Â StringÂ previousChildName)
```  

|                                                                                                       Parameters                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DataSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot)` snapshot` | An immutable snapshot of the data at the new child location                                                                          |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` previousChildName`                                                                                                                      | The key name of sibling location ordered before the new child. This ```text will be null for the first child node of a location. ``` |