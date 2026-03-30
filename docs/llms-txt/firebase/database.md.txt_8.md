# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/database.md.txt

# firebase::database Namespace

# firebase::database

Namespace for the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) C++ SDK.

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231a4589f1a305b7bf25951b8b345ca2ea53 = 0, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231a449ec7d89f1ea10b60d8c482705a7d80, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231ae4107651eb03b3a5578c1d269e3e1584, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231abf25851e1999cd0468de8a94834306d8, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231a1489f3c18bc92ddcef64fd025b6fbcad, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231aac353a1e53bcfc6cc2d60adb32bf6e4d, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231a51ccc4696f0f8ad24aad214af174fe7e, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231af91a63a16e4bbe859d70273dc9214599, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231ac562f511e335597e9ee888e931ab2987, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231af0fc64bd2fa60402e9973bc8f6f444e4, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231aafb67f0652362c7f68a16adc99f08595, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231ac821e79bdf06f7e3acaa440da5a1a801, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231a2b46764d2c7479b6859e129ab7385536, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231a0c9d49d794f752622fa5dcd8813ae302, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231ae64c6ce35e43893af8d2470f451b25d0 }` | enumError code returned by Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) C++ functions. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9809aaddcfabafdeedee53895914704b{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9809aaddcfabafdeedee53895914704baf36b83b017bf6d1e33470b73ea9b1cd4, https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9809aaddcfabafdeedee53895914704ba1cb82f507416604bbca91980b0fd4c69 }` | enumSpecifies whether the transaction succeeded or not. |

| ### Typedefs ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1ac43d2f59abc3089c14865eae53a290d6)(MutableData *data)` | typedef `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9809aaddcfabafdeedee53895914704b(*` Your own transaction handler, which the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library may call multiple times to apply changes to the data, and should return success or failure depending on whether it succeeds. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a4d1a08f3c8aa033258bc2c1cd0c2fe3d` | typedef `std::function< https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9809aaddcfabafdeedee53895914704b(https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data *data)>` Your own transaction handler function or lambda, which the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library may call multiple times to apply changes to the data, and should return success or failure depending on whether it succeeds. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a2304afa2b9c5965fb7a1f736ab95bf86)(MutableData *data, void *context)` | typedef `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9809aaddcfabafdeedee53895914704b(*` Your own transaction handler, which the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library may call multiple times to apply changes to the data, and should return success or failure depending on whether it succeeds. |

| ### Functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aa1d847bf984cc1717185a59930d97877(https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231 error)` | `const char *` Get the human-readable error message corresponding to an error code. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a77f136a633fb85b06e5b3f56400fa21a()` | `const https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant &` Get a server-populated value corresponding to the current timestamp. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aceba02421311a4797694a38b2f1b2b74(const https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query & rhs)` | `bool` Compares two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a9bd2c0dd411d5ddbbd0e0d457c9ea65c(const https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference & rhs)` | `bool` Compares two [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances. |

| ### Classes ||
|---|---|
| [firebase::database::ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener) | Child listener interface. |
| [firebase::database::DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot) | A [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) instance contains data from a Firebase [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) location. |
| [firebase::database::Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database) | Entry point for the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) C++ SDK. |
| [firebase::database::DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference) | [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) represents a particular location in your [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) and can be used for reading or writing data to that [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) location. |
| [firebase::database::DisconnectionHandler](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler) | Allows you to register server-side actions to occur when the client disconnects. |
| [firebase::database::MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data) | Instances of this class encapsulate the data and priority at a location. |
| [firebase::database::Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query) | The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) class is used for reading data. |
| [firebase::database::ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener) | Value listener interface. |

## Enumerations

### Error

```c++
 Error
```
Error code returned by Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) C++ functions.

| Properties ||
|---|---|
| `kErrorConflictingOperationInProgress` | An operation that conflicts with this one is already in progress. For example, calling SetValue and SetValueAndPriority on a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) is not allowed. |
| `kErrorDisconnected` | The operation had to be aborted due to a network disconnect. |
| `kErrorExpiredToken` | The supplied auth token has expired. |
| `kErrorInvalidToken` | The specified authentication token is invalid. |
| `kErrorInvalidVariantType` | You specified an invalid [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type for a field. For example, a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference)'s Priority and the keys of a Map must be of scalar type (MutableString, StaticString, Int64, Double). |
| `kErrorMaxRetries` | The transaction had too many retries. |
| `kErrorNetworkError` | The operation could not be performed due to a network error. |
| `kErrorNone` | The operation was a success, no error occurred. |
| `kErrorOperationFailed` | The server indicated that this operation failed. |
| `kErrorOverriddenBySet` | The transaction was overridden by a subsequent set. |
| `kErrorPermissionDenied` | This client does not have permission to perform this operation. |
| `kErrorTransactionAbortedByUser` | The transaction was aborted, because the user's DoTransaction function returned kTransactionResultAbort instead of kTransactionResultSuccess. |
| `kErrorUnavailable` | The service is unavailable. |
| `kErrorUnknownError` | An unknown error occurred. |
| `kErrorWriteCanceled` | The write was canceled locally. |

### TransactionResult

```c++
 TransactionResult
```
Specifies whether the transaction succeeded or not.

| Properties ||
|---|---|
| `kTransactionResultAbort` | The transaction did not succeed. Any changes to the [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) will be discarded. |
| `kTransactionResultSuccess` | The transaction was successful, the [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) was updated. |

## Typedefs

### DoTransaction

```c++
TransactionResult(* DoTransaction)(MutableData *data)
```
Your own transaction handler, which the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library may call multiple times to apply changes to the data, and should return success or failure depending on whether it succeeds.

<br />

> [!NOTE]
> **Note:** This version of the callback is no longer supported (unless you are building for Android with stlport). You should use either one of DoTransactionWithContext (a simple function pointer that accepts context data) or DoTransactionFunction (based on std::function).

**See also:** [DoTransactionWithContext](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a2304afa2b9c5965fb7a1f736ab95bf86) for more information.

<br />

### DoTransactionFunction

```c++
std::function< TransactionResult(MutableData *data)> DoTransactionFunction
```
Your own transaction handler function or lambda, which the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library may call multiple times to apply changes to the data, and should return success or failure depending on whether it succeeds.

**See also:** [DoTransactionWithContext](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a2304afa2b9c5965fb7a1f736ab95bf86) for more information.

### DoTransactionWithContext

```c++
TransactionResult(* DoTransactionWithContext)(MutableData *data, void *context)
```
Your own transaction handler, which the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library may call multiple times to apply changes to the data, and should return success or failure depending on whether it succeeds.

The context you specified to RunTransaction will be passed into this call.

This function will be called, *possibly multiple times*, with the current data at this location. The function is responsible for inspecting that data and modifying it as desired, then returning a TransactionResult specifying either that the [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) was modified to a desired new state, or that the transaction should be aborted. Whenever this function is called, the [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) passed in must be modified from scratch.

Since this function may be called repeatedly for the same transaction, be extremely careful of any side effects that may be triggered by this function. In addition, this function is called from within the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) library's run loop, so care is also required when accessing data that may be in use by other threads in your application.

Best practices for this function are to ONLY rely on the data passed in.

<br />

> [!NOTE]
> **Note:** If you want a callback to be triggered when the transaction is finished, you can use the Future value returned by the method running the transaction, and call [Future::OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a334de3fc89aefc4704c89f3fb7ba1c08) to register a callback to be called when the transaction either succeeds or fails.

**See also:** [DoTransaction](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1ac43d2f59abc3089c14865eae53a290d6) for more information.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `data` | Mutable data, which the callback can edit. | | `context` | Context pointer, passed verbatim to the callback. | |
| **Returns** | The callback should return kTransactionResultSuccess if the data was modified, or kTransactionResultAbort if it was unable to modify the data. If the callback returns kTransactionResultAbort, the RunTransaction() call will return the kErrorTransactionAbortedByUser error code. |

## Functions

### GetErrorMessage

```c++
const char * GetErrorMessage(
  Error error
)
```
Get the human-readable error message corresponding to an error code.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `error` | Error code to get the error message for. | |
| **Returns** | Statically-allocated string describing the error. |

### ServerTimestamp

```c++
const Variant & ServerTimestamp()
```
Get a server-populated value corresponding to the current timestamp.

When inserting values into the database, you can use the special value [firebase::database::ServerTimestamp()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a77f136a633fb85b06e5b3f56400fa21a) to have the server auto-populate the current timestamp, which is represented as millieconds since the Unix epoch, into the field.

<br />

| Details ||
|---|---|
| **Returns** | A special value that tells the server to use the current timestamp. |

### operator==

```c++
bool operator==(
  const Query & lhs,
  const Query & rhs
)
```
Compares two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances.

Two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances on the same database, in the same location, with the same parameters (OrderBy\*, StartAt, EndAt, EqualTo, Limit\*) are considered equivalent.

Equivalent Queries have a shared pool of ValueListeners and ChildListeners. When listeners are added or removed from one [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instance, it affects all equivalent [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `lhs` | The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) to compare against. | | `rhs` | The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) to compare against. | |
| **Returns** | True if the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances have the same database, the same path, and the same parameters, determined by StartAt(), EndAt(), EqualTo(), and the OrderBy and LimitTo methods. False otherwise. |

### operator==

```c++
bool operator==(
  const DatabaseReference & lhs,
  const DatabaseReference & rhs
)
```
Compares two [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `lhs` | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference). | | `rhs` | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to compare against. | |
| **Returns** | True if the [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances have the same URL. False otherwise. |