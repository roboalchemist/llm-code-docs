# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState.md.txt

# LoadBundleTaskProgress.TaskState

# LoadBundleTaskProgress.TaskState


```
public enum LoadBundleTaskProgress.TaskState
```

<br />

*** ** * ** ***

Represents the state of bundle loading tasks.

Both [SUCCESS](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#SUCCESS) and [ERROR](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#ERROR) are final states: task will abort or complete and there will be no more updates after they are reported.

## Summary

|                                                           ### Enum Values                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------|---|
| [ERROR](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#ERROR)     |   |
| [RUNNING](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#RUNNING) |   |
| [SUCCESS](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#SUCCESS) |   |

|                                                                       ### Public methods                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[LoadBundleTaskProgress.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static LoadBundleTaskProgress.TaskState[]`                                                                                                                    | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                            |

## Enum Values

### ERROR

```
LoadBundleTaskProgress.TaskStateÂ LoadBundleTaskProgress.TaskState.ERROR
```  

### RUNNING

```
LoadBundleTaskProgress.TaskStateÂ LoadBundleTaskProgress.TaskState.RUNNING
```  

### SUCCESS

```
LoadBundleTaskProgress.TaskStateÂ LoadBundleTaskProgress.TaskState.SUCCESS
```  

## Public methods

### valueOf

```
publicÂ staticÂ LoadBundleTaskProgress.TaskStateÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                        Returns                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [LoadBundleTaskProgress.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState) | the enum constant with the specified name |

|                                                                              Throws                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ LoadBundleTaskProgress.TaskState[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|               Returns                |
|--------------------------------------|------------------------------------------------------------------------------------|
| `LoadBundleTaskProgress.TaskState[]` | an array containing the constants of this enum type, in the order they're declared |