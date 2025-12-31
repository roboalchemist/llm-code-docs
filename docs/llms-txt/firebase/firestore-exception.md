# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception.md.txt

# Firebase.Firestore.FirestoreException Class Reference

# Firebase.Firestore.FirestoreException

A class of exceptions thrown by Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore).

## Summary

### Inheritance

Inherits from: Exception

| ### Constructors and Destructors ||
|---|---|
| [FirestoreException](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception_1a7e3a48f6ffddf9446c500b15c366500c)`(`[FirestoreError](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a24804fae11b868e5f88ba5d44d1500a8)` errorCode)` Initializes a new [FirestoreException](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception), with the given error code. ||
| [FirestoreException](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception_1adaf2c9e7bc40e87d24c64f4a055f1912)`(`[FirestoreError](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a24804fae11b868e5f88ba5d44d1500a8)` errorCode, string message)` Initializes a new [FirestoreException](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception), with the given error code and message. ||

|                                                                                                                                                                                                ### Properties                                                                                                                                                                                                ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ErrorCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception_1a3f4fa5a9755454ec7630d196e5b59995) | [FirestoreError](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a24804fae11b868e5f88ba5d44d1500a8) The error code describing the error. |

## Properties

### ErrorCode

```c#
FirestoreError ErrorCode
```  
The error code describing the error.

## Public functions

### FirestoreException

```c#
 FirestoreException(
  FirestoreError errorCode
)
```  
Initializes a new [FirestoreException](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception), with the given error code.  

### FirestoreException

```c#
 FirestoreException(
  FirestoreError errorCode,
  string message
)
```  
Initializes a new [FirestoreException](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-exception#class_firebase_1_1_firestore_1_1_firestore_exception), with the given error code and message.