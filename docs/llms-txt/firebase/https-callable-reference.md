# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference.md.txt

# Firebase.Functions.HttpsCallableReference Class Reference

# Firebase.Functions.HttpsCallableReference

Represents a reference to a Google Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions) HTTPS callable function.

## Summary

Represents a reference to a Google Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions) HTTPS callable function. (see [Google Cloud Functions](https://cloud.google.com/functions/))

|                                                                                                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                                                                                                ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Functions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference_1a668f69adbc317d8af76c00ae15c55be7) | [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) service which created this reference. |

|                                                                                                                                                                                                    ### Public functions                                                                                                                                                                                                    ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CallAsync](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference_1a96190a87e3688d4c9909044df490303e)`()`            | `Task< `[HttpsCallableResult](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-result#class_firebase_1_1_functions_1_1_https_callable_result)` >` ... |
| [CallAsync](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference_1a52f9e8fc0c45fe2e0f9c6907fffeb049)`(object data)` | `Task< `[HttpsCallableResult](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-result#class_firebase_1_1_functions_1_1_https_callable_result)` >` ... |

## Properties

### Functions

```c#
FirebaseFunctions Functions
```  
Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) service which created this reference.

<br />

|                                                                                             Details                                                                                             ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) service. |

## Public functions

### CallAsync

```c#
Task< HttpsCallableResult > CallAsync()
```  
...

<br />

|                          Details                          ||
|-------------|----------------------------------------------|
| **Returns** | A Task with the result of the function call. |

### CallAsync

```c#
Task< HttpsCallableResult > CallAsync(
  object data
)
```  
...

<br />

|                                                  Details                                                   ||
|-------------|-----------------------------------------------------------------------------------------------|
| Parameters  | |--------|-----------------------------------| | `data` | The data to pass to the function. | |
| **Returns** | A Task with the result of the function call.                                                  |