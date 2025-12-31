# Source: https://firebase.google.com/docs/reference/unity/class/firebase/functions/functions-exception.md.txt

# Firebase.Functions.FunctionsException Class Reference

# Firebase.Functions.FunctionsException

Represents an Exception resulting from an operation on a FunctionsReference

## Summary

### Inheritance

Inherits from: Exception

|                                                                                                                       ### Properties                                                                                                                       ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [ErrorCode](https://firebase.google.com/docs/reference/unity/class/firebase/functions/functions-exception#class_firebase_1_1_functions_1_1_functions_exception_1a619f98df0495dc859c4547bb7258e2cd) | `FunctionsErrorCode`                                   |
| **Returns**                                                                                                                                                                                        | A code that indicates the type of error that occurred. |

## Properties

### ErrorCode

```c#
FunctionsErrorCode ErrorCode
```  
<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | A code that indicates the type of error that occurred. |

This value will be one of the set of constants defined on [FunctionsException](https://firebase.google.com/docs/reference/unity/class/firebase/functions/functions-exception#class_firebase_1_1_functions_1_1_functions_exception).