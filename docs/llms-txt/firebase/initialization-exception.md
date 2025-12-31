# Source: https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception.md.txt

# Firebase.InitializationException Class Reference

# Firebase.InitializationException

The exception that is thrown when a problem occurs with initialization of a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) module or class.

## Summary

### Inheritance

Inherits from: Exception

| ### Constructors and Destructors ||
|---|---|
| [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception_1affe6e229c08b5c96ac976e5421a341fa)`(`[InitResult](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1a355b61e7544c96415027f22918bd0575)` result)` Initializes a new [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception), with the given result. ||
| [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception_1a40db37d255d1f84a53f0ce0e46755760)`(`[InitResult](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1a355b61e7544c96415027f22918bd0575)` result, string message)` Initializes a new [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception), with the given result and message. ||
| [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception_1af02429ce5e1917a78637f6b2cb1dd168)`(`[InitResult](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1a355b61e7544c96415027f22918bd0575)` result, string message, System.Exception inner)` Initializes a new [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception), with the given result, message, and a reference to the inner exception. ||

|                                                                                                                                                                                   ### Properties                                                                                                                                                                                   ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [InitResult](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception_1a0df06142db69badb0db4149f5ae15abf) | [InitResult](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1a355b61e7544c96415027f22918bd0575) The error code describing the cause of the failure. |

## Properties

### InitResult

```c#
InitResult InitResult
```  
The error code describing the cause of the failure.

## Public functions

### InitializationException

```c#
 InitializationException(
  InitResult result
)
```  
Initializes a new [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception), with the given result.  

### InitializationException

```c#
 InitializationException(
  InitResult result,
  string message
)
```  
Initializes a new [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception), with the given result and message.  

### InitializationException

```c#
 InitializationException(
  InitResult result,
  string message,
  System.Exception inner
)
```  
Initializes a new [InitializationException](https://firebase.google.com/docs/reference/unity/class/firebase/initialization-exception#class_firebase_1_1_initialization_exception), with the given result, message, and a reference to the inner exception.