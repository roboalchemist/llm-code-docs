# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result.md.txt

# Firebase.Database.TransactionResult Class Reference

# Firebase.Database.TransactionResult

Instances of this class represent the desired outcome of a single Run of a transaction.

## Summary

Pass a handler to [DatabaseReference.RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a4b21a7318e923a839b8fcca6ca3e90b0), and in your handler, you can either:

- Set the data to the new value (success) via [TransactionResult.Success(MutableData)](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result_1a6f1f1bf13de9df238709a34fda985ee6)
- abort the transaction via [TransactionResult.Abort()](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result_1a3fb9fa11dcea694892d9ee08950f6184)

<br />

|                                                                                                                 ### Properties                                                                                                                  ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [IsSuccess](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result_1a5be2709b124540980c11f75fc691d0fc) | `bool` Whether or not this result is a success. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Abort](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result_1a3fb9fa11dcea694892d9ee08950f6184)`()`                                                                                                                                                                 | [TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result) Aborts the transaction run with [DatabaseReference.RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a4b21a7318e923a839b8fcca6ca3e90b0) and returns an aborted [TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result) which can be returned from RunTransaction. |
| [Success](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result_1a6f1f1bf13de9df238709a34fda985ee6)`(`[MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data)` resultData)` | [TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result) Builds a successful result to be returned from the handler passed to [DatabaseReference.RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a4b21a7318e923a839b8fcca6ca3e90b0).                                                                                                                                                                                                 |

## Properties

### IsSuccess

```c#
bool IsSuccess
```  
Whether or not this result is a success.

## Public static functions

### Abort

```c#
TransactionResult Abort()
```  
Aborts the transaction run with [DatabaseReference.RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a4b21a7318e923a839b8fcca6ca3e90b0) and returns an aborted [TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result) which can be returned from RunTransaction.  

### Success

```c#
TransactionResult Success(
  MutableData resultData
)
```  
Builds a successful result to be returned from the handler passed to [DatabaseReference.RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a4b21a7318e923a839b8fcca6ca3e90b0).

<br />

|                                                                                                                 Details                                                                                                                  ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|------------------------------------------------| | `resultData` | The desired data to be stored at the location. |                                                                                         |
| **Returns** | A [TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result) indicating the new data to be stored at the location. |