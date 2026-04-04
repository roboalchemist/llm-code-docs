# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference.md.txt

# firebase::database::DatabaseReference Class Reference

# firebase::database::DatabaseReference


`#include <database_reference.h>`

[DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) represents a particular location in your [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) and can be used for reading or writing data to that [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) location.

## Summary

This class is the starting point for all [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) operations. After you've initialized it with a URL, you can use it to read data, write data, and to create new [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances.

### Inheritance

Inherits from: [firebase::database::Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9c00ce11d9d97258d2d5c011c6b7b0fe()` Default constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1ac0ec9372591638c5cc293f904ba0a11e(const https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference & reference)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1aa1eed22badf09b55ed9e3c3a20cb31dd(https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference && reference)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1afb03aa732fde9b5657b414bff832668a()` Required virtual destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a21af95972cbb5cd50c097efa53889d93(const char *path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Gets a reference to a location relative to this one. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9763c7938d6bb3b6da5534a6a3948b18(const std::string & path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Gets a reference to a location relative to this one. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f412bf56be6664bd8a60ebf8f4707b8() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Gets the parent of this location, or get this location again if IsRoot(). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1ad6c842f9121a7f39ba9556ebb501c63d() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Gets the root of the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a0497b9c87998f3f046b46c03e8650689()` | `void` Manually disconnect Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) from the server, and disable automatic reconnection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1ae057efb4208b7fe75984d304b0f17777()` | `void` Manually reestablish connection to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) server and enable automatic reconnection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a66ae8978762c5d1f25b0ec031378e3c7()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/disconnection-handler#classfirebase_1_1database_1_1_disconnection_handler *` Get the disconnect handler, which controls what actions the server will perform to this location's data when this client disconnects. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9cc5ecc48cfebb1a63bd2a1775cedd2a() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Automatically generates a child location, create a reference to it, and returns that reference to it. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a494da77303d99039d40ec21e965dcd5a()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Removes the value at this location from the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a35343205d5d6350728132cc081bf3b72()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a494da77303d99039d40ec21e965dcd5a);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c(https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a2304afa2b9c5965fb7a1f736ab95bf86 transaction_function, void *context, bool trigger_local_events)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot >` Run a user-supplied callback function (passing in a context), possibly multiple times, to perform an atomic transaction on the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a4b12d30ea5e83ad42ac06a304ed1d81a(https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a4d1a08f3c8aa033258bc2c1cd0c2fe3d transaction_function, bool trigger_local_events)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot >` Run a user-supplied callback, possibly multiple times, to perform an atomic transaction on the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1aeeb3fa5bb62174c9a7b54be7237ed5d2(https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1ac43d2f59abc3089c14865eae53a290d6 transaction_function, bool trigger_local_events)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot >` Run a user-supplied callback function, possibly multiple times, to perform an atomic transaction on the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a8d01a050fe13281cab0fc933b05d116c()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot >` Get the result of the most recent call to [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6(https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant priority)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Sets the priority of this field, which controls its sort order relative to its siblings. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a1417333453584e49b835cbfcac6f3937()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e(https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Sets the data at this location to the given value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f(https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant value, https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant priority)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Sets both the data and priority of this location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a1c957e15c6a1cb628a04197f178f416a()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Get the result of the most recent call to [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a27fd6b1e53d21d3e76e7deb985d901aa()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a1c25c006c2a73dfc51ef604e586ad635(https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant values)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Updates the specified child keys to the given values. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1ac5f421a633a5c47aa7ae26f5efc9e3e5(const std::map< std::string, https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant > & values)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Updates the specified child keys to the given values. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af4ee35ff4333e07a3b4ffff082198e4b()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to either version of [UpdateChildren()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a1c25c006c2a73dfc51ef604e586ad635). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1afdcd0bae3501ba5d14a18df2c20a851d() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database *` Gets the database to which we refer. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1ae8ce1e829e6cdc5cd63a4fedcd8765ae() const ` | `bool` Returns true if this reference refers to the root of the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a457a5f7416db0f5b66fa4e2c2486fa8a() const override` | `virtual bool` Returns true if this reference is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1ac9b24b26f34084cc0245150cc728fe84() const ` | `const char *` Gets the string key of this database location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a50a92434fddf5deb35ace7f78bf60986() const ` | `std::string` Gets the string key of this database location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1add11623d85094adf52d81075d37d5cb3(const https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference & reference)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a3037017a0e5714c568e2f9df7e82fac4(https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference && reference)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a58187f6a7ff0c1f2e9ac2bfa12dff349() const ` | `std::string` Get the absolute URL of this reference. |

## Public functions

### Child

```c++
DatabaseReference Child(
  const char *path
) const 
```
Gets a reference to a location relative to this one.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. The pointer only needs to be valid during this call. | |
| **Returns** | Child relative to this location. |

### Child

```c++
DatabaseReference Child(
  const std::string & path
) const 
```
Gets a reference to a location relative to this one.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. | |
| **Returns** | Child relative to this location. |

### DatabaseReference

```c++
 DatabaseReference()
```
Default constructor.

This creates an invalid [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference). Attempting to perform any operations on this reference will fail unless a valid [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) has been assigned to it.

### DatabaseReference

```c++
 DatabaseReference(
  const DatabaseReference & reference
)
```
Copy constructor.

It's totally okay (and efficient) to copy [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances, as they simply point to the same location in the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to copy from. | |

### DatabaseReference

```c++
 DatabaseReference(
  DatabaseReference && reference
)
```
Move constructor.

Moving is an efficient operation for [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to move data from. | |

### GetParent

```c++
DatabaseReference GetParent() const 
```
Gets the parent of this location, or get this location again if IsRoot().

<br />

| Details ||
|---|---|
| **Returns** | Parent of this location in the database, unless this location is the root, in which case it returns this same location again. |

### GetRoot

```c++
DatabaseReference GetRoot() const 
```
Gets the root of the database.

<br />

| Details ||
|---|---|
| **Returns** | Root of the database. |

### GoOffline

```c++
void GoOffline()
```
Manually disconnect Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) from the server, and disable automatic reconnection.

This will affect all other instances of [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) as well.

### GoOnline

```c++
void GoOnline()
```
Manually reestablish connection to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) server and enable automatic reconnection.

This will affect all other instances of [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) as well.

### OnDisconnect

```c++
DisconnectionHandler * OnDisconnect()
```
Get the disconnect handler, which controls what actions the server will perform to this location's data when this client disconnects.

<br />

| Details ||
|---|---|
| **Returns** | Disconnection handler for this location. You can use this to queue up operations on the server to be performed when the client disconnects. |

### PushChild

```c++
DatabaseReference PushChild() const 
```
Automatically generates a child location, create a reference to it, and returns that reference to it.

<br />

| Details ||
|---|---|
| **Returns** | A newly created child, with a unique key. |

### RemoveValue

```c++
Future< void > RemoveValue()
```
Removes the value at this location from the database.

This is an asynchronous operation which takes time to execute, and uses [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) to return its result.


> [!NOTE]
> **Note:** Only one [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a494da77303d99039d40ec21e965dcd5a) should be running on a given database location at the same time. If you need to run multiple operations at once, use [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c).

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### RemoveValueLastResult

```c++
Future< void > RemoveValueLastResult()
```
Gets the result of the most recent call to [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a494da77303d99039d40ec21e965dcd5a);.

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a494da77303d99039d40ec21e965dcd5a). |

### RunTransaction

```c++
Future< DataSnapshot > RunTransaction(
  DoTransactionWithContext transaction_function,
  void *context,
  bool trigger_local_events
)
```
Run a user-supplied callback function (passing in a context), possibly multiple times, to perform an atomic transaction on the database.

**See also:** [firebase::database::DoTransactionWithContext](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a2304afa2b9c5965fb7a1f736ab95bf86) for more information.

> [!NOTE]
> **Note:** Only one [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c) should be running on a given database location at the same time.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `transaction_function` | The user-supplied function that will be called, possibly multiple times, to perform the database transaction. | | `context` | User-supplied context that will be passed to the transaction function. | | `trigger_local_events` | If true, events will be triggered for intermediate state changes during the transaction. If false, only the final state will cause events to be triggered. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the transaction either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded and the transaction was committed, and the new value of the data will be returned in the [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) result. If the Error is kErrorTransactionAbortedByUser, the transaction was aborted because the transaction function returned kTransactionResultAbort, and the old value will be returned in [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot). Otherwise, if some other error occurred, Error and ErrorMessage will be set and [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) will be invalid. |

### RunTransaction

```c++
Future< DataSnapshot > RunTransaction(
  DoTransactionFunction transaction_function,
  bool trigger_local_events
)
```
Run a user-supplied callback, possibly multiple times, to perform an atomic transaction on the database.

**See also:** [firebase::database::DoTransactionFunction](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1a4d1a08f3c8aa033258bc2c1cd0c2fe3d) for more information.

> [!NOTE]
> **Note:** Only one [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c) should be running on a given database location at the same time.

> [!NOTE]
> **Note:** This version (that accepts an std::function) is not available when using stlport on Android. If you don't wish to use std::function, use the overloaded method that accepts a simple function pointer with a context.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `transaction_function` | The user-supplied function or lambda that will be called, possibly multiple times, to perform the database transaction. | | `trigger_local_events` | If true, events will be triggered for intermediate state changes during the transaction. If false, only the final state will cause events to be triggered. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the transaction either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded and the transaction was committed, and the new value of the data will be returned in the [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) result. If the Error is kErrorTransactionAbortedByUser, the transaction was aborted because the transaction function returned kTransactionResultAbort, and the old value will be returned in [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot). Otherwise, if some other error occurred, Error and ErrorMessage will be set and [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) will be invalid. |

### RunTransaction

```c++
Future< DataSnapshot > RunTransaction(
  DoTransaction transaction_function,
  bool trigger_local_events
)
```
Run a user-supplied callback function, possibly multiple times, to perform an atomic transaction on the database.

**See also:** [firebase::database::DoTransaction](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1ac43d2f59abc3089c14865eae53a290d6) for more information.

> [!NOTE]
> **Note:** Only one [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c) should be running on a given database location at the same time.

> [!NOTE]
> **Note:** This version (that accepts a simple function pointer) is only available when using stlport and std::function is not available.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `transaction_function` | The user-supplied function that will be called, possibly multiple times, to perform the database transaction. | | `trigger_local_events` | If true, events will be triggered for intermediate state changes during the transaction. If false, only the final state will cause events to be triggered. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the transaction either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded and the transaction was committed, and the new value of the data will be returned in the [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) result. If the Error is kErrorTransactionAbortedByUser, the transaction was aborted because the transaction function returned kTransactionResultAbort, and the old value will be returned in [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot). Otherwise, if some other error occurred, Error and ErrorMessage will be set and [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) will be invalid. |

### RunTransactionLastResult

```c++
Future< DataSnapshot > RunTransactionLastResult()
```
Get the result of the most recent call to [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c).

<br />

| Details ||
|---|---|
| **Returns** | Results of the most recent call to [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c). |

### SetPriority

```c++
Future< void > SetPriority(
  Variant priority
)
```
Sets the priority of this field, which controls its sort order relative to its siblings.

In Firebase, children are sorted in the following order:

1. First, children with no priority.
2. Then, children with numerical priority, sorted numerically in ascending order.
3. Then, remaining children, sorted lexicographically in ascending order of their text priority.

<br />

Children with the same priority (including no priority) are sorted by key: A. First, children with keys that can be parsed as 32-bit integers, sorted in ascending numerical order of their keys. B. Then, remaining children, sorted in ascending lexicographical order of their keys.

This is an asynchronous operation which takes time to execute, and uses [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) to return its result.


> [!NOTE]
> **Note:** Only one [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6) should be running on a given database location at the same time. If you need to run multiple operations at once, use [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `priority` | Sort priority for this child relative to its siblings. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types accepted are Null, Int64, Double, and String. Other types will return kErrorInvalidVariantType. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### SetPriorityLastResult

```c++
Future< void > SetPriorityLastResult()
```
Gets the result of the most recent call to [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6).

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6). |

### SetValue

```c++
Future< void > SetValue(
  Variant value
)
```
Sets the data at this location to the given value.

This is an asynchronous operation which takes time to execute, and uses [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) to return its result.


> [!NOTE]
> **Note:** Only one [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e) should be running on a given database location at the same time. If you need to run multiple operations at once, use [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to set this location to. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type corresponds to the types accepted by the database JSON: Null: Deletes this location from the database. Int64: Inserts an integer value into this location. Double: Inserts a floating point value into this location. String: Inserts a string into this location. (Accepts both Mutable and Static strings) Vector: Inserts a JSON array into this location. The elements can be any [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type, including Vector and Map. Map: Inserts a JSON associative array into this location. The keys must be of type String (or Int64/Double which are converted to String). The values can be any [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type, including Vector and Map. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### SetValueAndPriority

```c++
Future< void > SetValueAndPriority(
  Variant value,
  Variant priority
)
```
Sets both the data and priority of this location.

See [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e) and [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6) for context on the parameters.

This is an asynchronous operation which takes time to execute, and uses [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) to return its result.


> [!NOTE]
> **Note:** Only one [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f) should be running on a given database location at the same time. [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f) can't be used on the same location at the same time as either [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e) or [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6), and will return kErrorConflictingOperationInProgress if you try. If you need to run multiple operations at once, use [RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to set this location to. See [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e) for information on the types accepted. | | `priority` | The priority to set this location to. See [SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6) for information on the types accepted. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### SetValueAndPriorityLastResult

```c++
Future< void > SetValueAndPriorityLastResult()
```
Get the result of the most recent call to [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f).

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f). |

### SetValueLastResult

```c++
Future< void > SetValueLastResult()
```
Gets the result of the most recent call to [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e).

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e). |

### UpdateChildren

```c++
Future< void > UpdateChildren(
  Variant values
)
```
Updates the specified child keys to the given values.


> [!NOTE]
> **Note:** This method will return kErrorConflictingOperationInProgress if it is run at the same time as [SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e), [SetValueAndPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1af1006cfdea6474cc86e0930c871f248f), or [RemoveValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a494da77303d99039d40ec21e965dcd5a) in the same location.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `values` | A variant of type Map. The keys are the paths to update and must be of type String (or Int64/Double which are converted to String). The values can be any [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type. A value of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type Null will delete the child. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### UpdateChildren

```c++
Future< void > UpdateChildren(
  const std::map< std::string, Variant > & values
)
```
Updates the specified child keys to the given values.

This is an asynchronous operation which takes time to execute, and uses [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) to return its result.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `values` | The paths to update, and their new child values. A value of type Null will delete that particular child. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### UpdateChildrenLastResult

```c++
Future< void > UpdateChildrenLastResult()
```
Gets the result of the most recent call to either version of [UpdateChildren()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a1c25c006c2a73dfc51ef604e586ad635).

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [UpdateChildren()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a1c25c006c2a73dfc51ef604e586ad635). |

### database

```c++
Database * database() const 
```
Gets the database to which we refer.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | Firebase [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) instance that this [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) refers to. |

### is_root

```c++
bool is_root() const 
```
Returns true if this reference refers to the root of the database.

<br />

| Details ||
|---|---|
| **Returns** | true if this reference refers to the root of the database, false otherwise. |

### is_valid

```c++
virtual bool is_valid() const override
```
Returns true if this reference is valid, false if it is not valid.

DatabaseReferences constructed with the default constructor are considered invalid. An invalid reference could be returned by [Database::GetReference()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1adc2324f618f325e72f9e4b924519d6bd) or [Database::GetReferenceFromUrl()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a91b0d75a4241d5a30d50c1c8682c76fb) if you specify an incorrect location, or calling [Query::GetReference()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a46b59f642ce2d12d9aa33b9b40eb37e9) on an invalid query.

<br />

| Details ||
|---|---|
| **Returns** | true if this reference is valid, false if this reference is invalid. |

### key

```c++
const char * key() const 
```
Gets the string key of this database location.

The pointer is only valid while the [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) remains in memory.

<br />

| Details ||
|---|---|
| **Returns** | String key of this database location, which will remain valid in memory until the [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) itself goes away. |

### key_string

```c++
std::string key_string() const 
```
Gets the string key of this database location.

<br />

| Details ||
|---|---|
| **Returns** | String key of this database location. |

### operator=

```c++
DatabaseReference & operator=(
  const DatabaseReference & reference
)
```
Copy assignment operator.

It's totally okay (and efficient) to copy [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances, as they simply point to the same location in the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to copy from. | |
| **Returns** | Reference to the destination [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference). |

### operator=

```c++
DatabaseReference & operator=(
  DatabaseReference && reference
)
```
Move assignment operator.

Moving is an efficient operation for [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to move data from. | |
| **Returns** | Reference to the destination [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference). |

### url

```c++
std::string url() const 
```
Get the absolute URL of this reference.

<br />

| Details ||
|---|---|
| **Returns** | The absolute URL of the location this reference refers to. |

### \~DatabaseReference

```c++
virtual  ~DatabaseReference()
```
Required virtual destructor.