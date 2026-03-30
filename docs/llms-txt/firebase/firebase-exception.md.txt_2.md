# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception.md.txt

# Firebase.FirebaseException Class Reference

# Firebase.FirebaseException

Exception thrown for any Task exception.

## Summary

Each API has different error codes, so the error code should be looked up relative to the API that produced the Task.

### Inheritance

Inherits from: Exception

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception_1a133dadb89a50f9d091dbf38f3596efd2()` Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception). ||
| `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception_1aeaae043e5d6a3ac369e9095a2cfc692e(int errorCode)` Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception), with the given error code. ||
| `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception_1a99bb3dbcbc7a1895512df57dd9a83f61(int errorCode, string message)` Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception), with the given error code and message. ||
| `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception_1a126a1e1dec452f4694d3c494134b9d7a(int errorCode, string message, System.Exception inner)` Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception), with the given error code, message, and a reference to the inner exception. ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception_1a2565fe13aaa67e51e13491c7ba14942d` | `int` Returns the API-defined non-zero error code. |

## Properties

### ErrorCode

```c#
int ErrorCode
```
Returns the API-defined non-zero error code.

If the error code is 0, the error is with the Task itself, and not the API. See the exception message for more detail.

## Public functions

### FirebaseException

```c#
 FirebaseException()
```
Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception).

### FirebaseException

```c#
 FirebaseException(
  int errorCode
)
```
Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception), with the given error code.

### FirebaseException

```c#
 FirebaseException(
  int errorCode,
  string message
)
```
Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception), with the given error code and message.

### FirebaseException

```c#
 FirebaseException(
  int errorCode,
  string message,
  System.Exception inner
)
```
Initializes a new [FirebaseException](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception#class_firebase_1_1_firebase_exception), with the given error code, message, and a reference to the inner exception.