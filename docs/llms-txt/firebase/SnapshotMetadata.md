# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata.md.txt

# SnapshotMetadata

# SnapshotMetadata


```
class SnapshotMetadata
```

<br />

*** ** * ** ***

Metadata about a snapshot, describing the state of the snapshot.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

|                                ### Public functions                                 |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#equals(java.lang.Object))`(obj: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)` |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  | [hasPendingWrites](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#hasPendingWrites())`()`                                                                               |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)          | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#hashCode())`()`                                                                                               |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#toString())`()`                                                                                               |

|                               ### Public properties                                |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isFromCache](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#isFromCache()) |

## Public functions

### equals

```
funÂ equals(obj:Â Any?):Â Boolean
```  

### hasPendingWrites

```
funÂ hasPendingWrites():Â Boolean
```  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if the snapshot contains the result of local writes (for example, `set()` or `update()` calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via [INCLUDE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#INCLUDE)) you will receive another snapshot with `hasPendingWrites()` equal to false once the writes have been committed to the backend. |

### hashCode

```
funÂ hashCode():Â Int
```  

### toString

```
funÂ toString():Â String!
```  

## Public properties

### isFromCache

```
valÂ isFromCache:Â Boolean
```