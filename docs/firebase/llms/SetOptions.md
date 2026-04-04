# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions.md.txt

# SetOptions

# SetOptions


```
class SetOptions
```

<br />

*** ** * ** ***

An options object that configures the behavior of `set()` calls. By providing one of the SetOptions objects returned by [merge](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#merge()), [mergeFields](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFields(java.util.List<java.lang.String>)) and [mergeFieldPaths](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFieldPaths(java.util.List<com.google.firebase.firestore.FieldPath>)), the `set()` calls in [DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference), [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) and [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) can be configured to perform granular merges instead of overwriting the target documents in their entirety.

## Summary

|                                                  ### Public functions                                                  |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                                                                                                                                                                                                                                                                      |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                             | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#hashCode())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `java-static `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions) | [merge](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#merge())`()` Changes the behavior of `set()` calls to only replace the values specified in its data argument.                                                                                                                                                                                                                                                                                                                                                                       |
| `java-static `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions) | [mergeFieldPaths](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFieldPaths(java.util.List<com.google.firebase.firestore.FieldPath>))`(fields: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`!>)` Changes the behavior of `set()` calls to only replace the given fields. |
| `java-static `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions) | [mergeFields](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFields(java.lang.String...))`(fields: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>!)` Changes the behavior of `set()` calls to only replace the given fields.                                                                                                                                                                                   |
| `java-static `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions) | [mergeFields](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFields(java.util.List<java.lang.String>))`(fields: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>)` Changes the behavior of `set()` calls to only replace the given fields.                                                      |

|                                                  ### Public properties                                                   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [FieldMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/model/mutation/FieldMask)`?` | [fieldMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#fieldMask()) |

## Public functions

### equals

```
funÂ equals(o:Â Any!):Â Boolean
```  

### hashCode

```
funÂ hashCode():Â Int
```  

### merge

```
java-staticÂ funÂ merge():Â SetOptions
```

Changes the behavior of `set()` calls to only replace the values specified in its data argument. Fields omitted from the `set()` call will remain untouched. If your input sets any field to an empty map, all nested fields are overwritten.  

### mergeFieldPaths

```
java-staticÂ funÂ mergeFieldPaths(fields:Â (Mutable)List<FieldPath!>):Â SetOptions
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here in its to data argument.  

|                                                                                                                                                       Parameters                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| `fields: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`!>` | The list of fields to merge. |

### mergeFields

```
java-staticÂ funÂ mergeFields(fields:Â Array<String!>!):Â SetOptions
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here.  

|                                                                                    Parameters                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `fields: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>!` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. |

### mergeFields

```
java-staticÂ funÂ mergeFields(fields:Â (Mutable)List<String!>):Â SetOptions
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched. If your input sets any field to an empty map, all nested fields are overwritten.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here.  

|                                                                                                                                            Parameters                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `fields: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. |

## Public properties

### fieldMask

```
valÂ fieldMask:Â FieldMask?
```