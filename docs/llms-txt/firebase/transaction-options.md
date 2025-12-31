# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options.md.txt

# Firebase.Firestore.TransactionOptions Class Reference

# Firebase.Firestore.TransactionOptions

Options to customize transaction behavior for [FirebaseFirestore.RunTransactionAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a5dd9d4668863426fefa06221068f3d6e).

## Summary

| ### Constructors and Destructors ||
|---|---|
| [TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options_1a4aa0a048ae3b228c57e7bf58d00bf0ba)`()` Creates the default [TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options). ||

|                                                                                                                                       ### Properties                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [MaxAttempts](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options_1aa950db727e8199208aee6a812f8327b7) | `Int32` The maximum number of attempts to commit, after which the transaction fails. |

|                                                                                                   ### Public functions                                                                                                   ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options_1aafe10d9eb76ab3d225f9c0fe7be16d66)`()` | `override string` |

## Properties

### MaxAttempts

```c#
Int32 MaxAttempts
```  
The maximum number of attempts to commit, after which the transaction fails.

The default value is 5, and must be greater than zero.

## Public functions

### ToString

```c#
override string ToString()
```  

### TransactionOptions

```c#
 TransactionOptions()
```  
Creates the default [TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options).