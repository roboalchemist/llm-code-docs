# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState.md.txt

# LoadBundleTaskProgress.TaskState

# LoadBundleTaskProgress.TaskState


```
enum LoadBundleTaskProgress.TaskState
```

<br />

*** ** * ** ***

Represents the state of bundle loading tasks.

Both `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#SUCCESS` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#ERROR` are final states: task will abort or complete and there will be no more updates after they are reported.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#ERROR` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#RUNNING` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#SUCCESS` |   |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ERROR

```
val LoadBundleTaskProgress.TaskState.ERROR: LoadBundleTaskProgress.TaskState
```

### RUNNING

```
val LoadBundleTaskProgress.TaskState.RUNNING: LoadBundleTaskProgress.TaskState
```

### SUCCESS

```
val LoadBundleTaskProgress.TaskState.SUCCESS: LoadBundleTaskProgress.TaskState
```

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): LoadBundleTaskProgress.TaskState!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<LoadBundleTaskProgress.TaskState!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState!>!` | an array containing the constants of this enum type, in the order they're declared |