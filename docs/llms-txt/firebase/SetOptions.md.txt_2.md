# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions.md.txt

# SetOptions

# SetOptions


```
class SetOptions
```

<br />

*** ** * ** ***

An options object that configures the behavior of `set()` calls. By providing one of the SetOptions objects returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#merge()`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFields(java.util.List<java.lang.String>)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFieldPaths(java.util.List<com.google.firebase.firestore.FieldPath>)`, the `set()` calls in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` can be configured to perform granular merges instead of overwriting the target documents in their entirety.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#merge()()` Changes the behavior of `set()` calls to only replace the values specified in its data argument. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFieldPaths(java.util.List<com.google.firebase.firestore.FieldPath>)(fields: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath!>)` Changes the behavior of `set()` calls to only replace the given fields. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFields(java.lang.String...)(fields: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!)` Changes the behavior of `set()` calls to only replace the given fields. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#mergeFields(java.util.List<java.lang.String>)(fields: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>)` Changes the behavior of `set()` calls to only replace the given fields. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/model/mutation/FieldMask?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions#fieldMask()` |

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### merge

```
java-static fun merge(): SetOptions
```

Changes the behavior of `set()` calls to only replace the values specified in its data argument. Fields omitted from the `set()` call will remain untouched. If your input sets any field to an empty map, all nested fields are overwritten.

### mergeFieldPaths

```
java-static fun mergeFieldPaths(fields: (Mutable)List<FieldPath!>): SetOptions
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here in its to data argument.

| Parameters |
|---|---|
| `fields: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath!>` | The list of fields to merge. |

### mergeFields

```
java-static fun mergeFields(fields: Array<String!>!): SetOptions
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here.

| Parameters |
|---|---|
| `fields: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. |

### mergeFields

```
java-static fun mergeFields(fields: (Mutable)List<String!>): SetOptions
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched. If your input sets any field to an empty map, all nested fields are overwritten.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here.

| Parameters |
|---|---|
| `fields: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. |

## Public properties

### fieldMask

```
val fieldMask: FieldMask?
```