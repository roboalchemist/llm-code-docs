# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler.md.txt

# firebase::database::DisconnectionHandler Class Reference

# firebase::database::DisconnectionHandler


`#include <disconnection.h>`

Allows you to register server-side actions to occur when the client disconnects.

## Summary

Each method you call (with the exception of Cancel) will queue up an action on the data that will be performed by the server in the event the client disconnects. To reset this queue, call [Cancel()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a508350a5ed484cde44c4f0d795a7f728).

A [DisconnectionHandler](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler) is associated with a specific location in the database, as they are obtained by calling [DatabaseReference::OnDisconnect()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a66ae8978762c5d1f25b0ec031378e3c7).

| ### Constructors and Destructors ||
|---|---|
| [~DisconnectionHandler](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a8dace64e40303704d2b804c9f00c7530)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                                                               ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                               ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cancel](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a508350a5ed484cde44c4f0d795a7f728)`()`                                                                                                                                                                                                                                                       | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Cancel any Disconnection operations that are queued up by this handler.                                                                                                                                                                                               |
| [CancelLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a74f3e575c606d82db966653fbc5d39ff)`()`                                                                                                                                                                                                                                             | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the result of the most recent call to [Cancel()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a508350a5ed484cde44c4f0d795a7f728).                            |
| [RemoveValue](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a1defd566393a63c37fa9b1e5b309b1af)`()`                                                                                                                                                                                                                                                  | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Remove the value at the current location when the client disconnects.                                                                                                                                                                                                 |
| [RemoveValueLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1ae93d6e0953961e3b1a8c1adcbfe84d3a)`()`                                                                                                                                                                                                                                        | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the result of the most recent call to [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a1defd566393a63c37fa9b1e5b309b1af).                       |
| [SetValue](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a7659bb5cb9b8e87b6ab8ed0c9c3147dd)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` value)`                                                                                                                                   | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Set the value of the data at the current location when the client disconnects.                                                                                                                                                                                        |
| [SetValueAndPriority](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1add9a029b5ceac773f0987ce6e5e4f64b)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` value, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` priority)` | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Set the value and priority of the data at the current location when the client disconnects.                                                                                                                                                                           |
| [SetValueAndPriorityLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1ae9a96ba1d7786576ee00e6b401f234ab)`()`                                                                                                                                                                                                                                | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the result of the most recent call to [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1add9a029b5ceac773f0987ce6e5e4f64b).               |
| [SetValueLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a756928b3aa6411a2995c3d0ba3d466f8)`()`                                                                                                                                                                                                                                           | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the result of the most recent call to [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a7659bb5cb9b8e87b6ab8ed0c9c3147dd).                          |
| [UpdateChildren](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1acdb1ca3203b838f0b53ac918013d55a9)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` values)`                                                                                                                            | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Updates the specified child keys to the given values when the client disconnects.                                                                                                                                                                                     |
| [UpdateChildren](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a49441e14a3142301b9006ff90aa75101)`(const std::map< std::string, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > & values)`                                                                                           | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Updates the specified child keys to the given values when the client disconnects.                                                                                                                                                                                     |
| [UpdateChildrenLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1ac5dcf10412c74a02917eefdb56691ec8)`()`                                                                                                                                                                                                                                     | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Gets the result of the most recent call to either version of [UpdateChildren()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1acdb1ca3203b838f0b53ac918013d55a9). |

## Public functions

### Cancel

```c++
Future< void > Cancel()
```  
Cancel any Disconnection operations that are queued up by this handler.

When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) returns, if its Error is kErrorNone, the queue has been cleared on the server.

<br />

|                                                                                                                                                                                       Details                                                                                                                                                                                       ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### CancelLastResult

```c++
Future< void > CancelLastResult()
```  
Get the result of the most recent call to [Cancel()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a508350a5ed484cde44c4f0d795a7f728).

<br />

|                                                                                                                     Details                                                                                                                     ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Result of the most recent call to [Cancel()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a508350a5ed484cde44c4f0d795a7f728). |

### RemoveValue

```c++
Future< void > RemoveValue()
```  
Remove the value at the current location when the client disconnects.

When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) returns, if its Error is kErrorNone, the RemoveValue operation has been successfully queued up on the server.

<br />

|                                                                                                                                                                                       Details                                                                                                                                                                                       ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### RemoveValueLastResult

```c++
Future< void > RemoveValueLastResult()
```  
Get the result of the most recent call to [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a1defd566393a63c37fa9b1e5b309b1af).

<br />

|                                                                                                                       Details                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Result of the most recent call to [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a1defd566393a63c37fa9b1e5b309b1af). |

### SetValue

```c++
Future< void > SetValue(
  Variant value
)
```  
Set the value of the data at the current location when the client disconnects.

When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) returns, if its Error is kErrorNone, the SetValue operation has been successfully queued up on the server.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The value to set this location to when the client disconnects. For information on how the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types are used, see [firebase::database::DatabaseReference::SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e). | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### SetValueAndPriority

```c++
Future< void > SetValueAndPriority(
  Variant value,
  Variant priority
)
```  
Set the value and priority of the data at the current location when the client disconnects.

When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) returns, if its Error is kErrorNone, the SetValue operation has been successfully queued up on the server.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value`    | The value to set this location to when the client disconnects. For information on how the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types are used, see [firebase::database::DatabaseReference::SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e).                                                                | | `priority` | The priority to set this location to when the client disconnects. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types accepted are Null, Int64, Double, and String. For information about how priority is used, see [firebase::database::DatabaseReference::SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6). | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### SetValueAndPriorityLastResult

```c++
Future< void > SetValueAndPriorityLastResult()
```  
Get the result of the most recent call to [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1add9a029b5ceac773f0987ce6e5e4f64b).

<br />

|                                                                                                                           Details                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Result of the most recent call to [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1add9a029b5ceac773f0987ce6e5e4f64b). |

### SetValueLastResult

```c++
Future< void > SetValueLastResult()
```  
Get the result of the most recent call to [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a7659bb5cb9b8e87b6ab8ed0c9c3147dd).

<br />

|                                                                                                                      Details                                                                                                                      ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Result of the most recent call to [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1a7659bb5cb9b8e87b6ab8ed0c9c3147dd). |

### UpdateChildren

```c++
Future< void > UpdateChildren(
  Variant values
)
```  
Updates the specified child keys to the given values when the client disconnects.

When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) returns, if its Error is kErrorNone, the UpdateChildren operation has been successfully queued up by the server.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `values` | A variant of type Map. The keys are the paths to update and must be of type String (or Int64/Double which are converted to String). The values can be any [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type. A value of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type Null will delete the child. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### UpdateChildren

```c++
Future< void > UpdateChildren(
  const std::map< std::string, Variant > & values
)
```  
Updates the specified child keys to the given values when the client disconnects.

When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) returns, if its Error is kErrorNone, the UpdateChildren operation has been successfully queued up by the server.

<br />

|                                                                                                                                                                                       Details                                                                                                                                                                                       ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|----------------------------------------------------------------------------------------------------------| | `values` | The paths to update, and their new child values. A value of type Null will delete that particular child. |                                                                                                                        |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### UpdateChildrenLastResult

```c++
Future< void > UpdateChildrenLastResult()
```  
Gets the result of the most recent call to either version of [UpdateChildren()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1acdb1ca3203b838f0b53ac918013d55a9).

<br />

|                                                                                                                         Details                                                                                                                         ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Result of the most recent call to [UpdateChildren()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler_1acdb1ca3203b838f0b53ac918013d55a9). |

### \~DisconnectionHandler

```c++
 ~DisconnectionHandler()
```