# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions.md.txt

# SetOptions

# SetOptions


```
public final class SetOptions
```

<br />

*** ** * ** ***

An options object that configures the behavior of `set()` calls. By providing one of the SetOptions objects returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#merge()`, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#mergeFields(java.util.List<java.lang.String>)` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#mergeFieldPaths(java.util.List<com.google.firebase.firestore.FieldPath>)`, the `set()` calls in `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference`, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction` can be configured to perform granular merges instead of overwriting the target documents in their entirety.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/model/mutation/FieldMask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#fieldMask()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#hashCode()()` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#merge()()` Changes the behavior of `set()` calls to only replace the values specified in its data argument. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#mergeFieldPaths(java.util.List<com.google.firebase.firestore.FieldPath>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath> fields)` Changes the behavior of `set()` calls to only replace the given fields. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#mergeFields(java.lang.String...)(String[] fields)` Changes the behavior of `set()` calls to only replace the given fields. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions#mergeFields(java.util.List<java.lang.String>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://developer.android.com/reference/kotlin/java/lang/String.html> fields)` Changes the behavior of `set()` calls to only replace the given fields. |

## Public fields

### fieldMask

```
public final @Nullable FieldMask fieldMask
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### hashCode

```
public int hashCode()
```

### merge

```
public static @NonNull SetOptions merge()
```

Changes the behavior of `set()` calls to only replace the values specified in its data argument. Fields omitted from the `set()` call will remain untouched. If your input sets any field to an empty map, all nested fields are overwritten.

### mergeFieldPaths

```
public static @NonNull SetOptions mergeFieldPaths(@NonNull List<FieldPath> fields)
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here in its to data argument.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath> fields` | The list of fields to merge. |

### mergeFields

```
public static @NonNull SetOptions mergeFields(String[] fields)
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here.

| Parameters |
|---|---|
| `String[] fields` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. |

### mergeFields

```
public static @NonNull SetOptions mergeFields(@NonNull List<String> fields)
```

Changes the behavior of `set()` calls to only replace the given fields. Any field that is not specified in `fields` is ignored and remains untouched. If your input sets any field to an empty map, all nested fields are overwritten.

It is an error to pass a `SetOptions` object to a `set()` call that is missing a value for any of the fields specified here.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://developer.android.com/reference/kotlin/java/lang/String.html> fields` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. |