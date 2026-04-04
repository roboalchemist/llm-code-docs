# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/query.md.txt

# Firebase.Database.Query Class Reference

# Firebase.Database.Query

The [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) class (and its subclass, [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) ) are used for reading data.

## Summary

Listeners are attached, and they will be triggered when the corresponding data changes.   


Instances of [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) are obtained by calling [StartAt()](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a579f39425905e1301d3cef7e6259abf2), [EndAt()](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ab96f9fe9354febf20403276c27b1be71), or Limit() on a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference).

### Inheritance

Direct Known Subclasses:[Firebase.Database.DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a6c892241cfe3d3cfa77540d6341a0016` | `EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args >` Event raised when children nodes are added relative to this location. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a71e2af7868312246b5da3024bb13204c` | `EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args >` Event raised when children nodes are changed relative to this location. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ade5832ad58d0b31fd5a649019bb8f2c9` | `EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args >` Event raised when children nodes are moved relative to this location. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1af4ef267bfef07b1969bd1394eb45c428` | `EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args >` Event raised when children nodes are removed relative to this location. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a6168285deb501f7c842b26947102e403` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference` A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to this location |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a80a78f3505955b9ed2583dc2f14cf739` | `EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/database/value-changed-event-args#class_firebase_1_1_database_1_1_value_changed_event_args >` Event for changes in the data at this location. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ab96f9fe9354febf20403276c27b1be71(string value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ad16b26fc15b2fd9f761d19fbfda22d53(double value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a2b99446acd04ee76abdd4d2979f2a9ae(bool value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ad7995dab5d4ca352b1687f0362d684fc(string value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key key less than or equal to the given key. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ab65b706c24b371a2e43f0e9733b0fe1d(double value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a79e82265c59c65d6559194db9fb78df1(bool value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a201d4cf96cd0608d9c954a50df8019f0(string value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with the given value |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a2a492212cba7ab028c36aa2c65791ff7(double value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with the given value |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1aeba6c847b1de73a1add49d184eeebaf9(bool value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a0cc7d801187ef4b1bf894ddfdbf70b94(string value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return the child node with the given key and value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1aa9a76c9d51827f0898d13467649530f6(double value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return the child node with the given key and value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a6df9b6af34ed5f108cc950a579667353(bool value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return the child node with the given key and value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a42a42204ed15f65fa54e8e21c6c92474()` | `Task< https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot >` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a541ff2958034fe1348ee9e6970218446(bool keepSynced)` | `void` By calling `keepSynced(true)` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a5d94502e61cf238e6a2c86459dfff806(int limit)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query with limit and anchor it to the start of the window |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a680c58d366ee8d62e407f62777fefdf0(int limit)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query with limit and anchor it to the end of the window |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a63006db86c9c79e84f92fe27d743b8ce(string path)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query in which child nodes are ordered by the values of the specified path. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a582a675a9195b75aa5023bd8307fedf9()` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query in which child nodes are ordered by their keys. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a36ebaad867acad713a0242b856fd4391()` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query in which child nodes are ordered by their priorities. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a446fab2545676895fa54954c555d081f()` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query in which nodes are ordered by their value |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a579f39425905e1301d3cef7e6259abf2(string value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1afb9a47a397b7eace4ed5e0379057be8f(double value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1af7fb01d52153f3acc63fe6372588b3b0(bool value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a4b895014176a47b413a0841b638ed92f(string value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a49c1bb730b4f8addf549987d4ba519fa(double value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1af2bc8e079372fd00786591538b09921f(bool value, string key)` | `https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query` Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |

## Properties

### ChildAdded

```c#
EventHandler< ChildChangedEventArgs > ChildAdded
```
Event raised when children nodes are added relative to this location.

Register a handler to observe when children are added relative to this [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) object. Each time time children nodes are added, your handler will be called with an immutable snapshot of the data.

### ChildChanged

```c#
EventHandler< ChildChangedEventArgs > ChildChanged
```
Event raised when children nodes are changed relative to this location.

Register a handler to observe changes to children relative to this [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) object. Each time time children nodes are changed, your handler will be called with an immutable snapshot of the data.

### ChildMoved

```c#
EventHandler< ChildChangedEventArgs > ChildMoved
```
Event raised when children nodes are moved relative to this location.

Register a handler to observe when children are moved relative to this [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) object. Each time time children nodes are moved, your handler will be called with an immutable snapshot of the data.

### ChildRemoved

```c#
EventHandler< ChildChangedEventArgs > ChildRemoved
```
Event raised when children nodes are removed relative to this location.

Register a handler to observe when children are removed relative to this [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) object. Each time time children nodes are removed, your handler will be called with an immutable snapshot of the data.

### Reference

```c#
DatabaseReference Reference
```
A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to this location

### ValueChanged

```c#
EventHandler< ValueChangedEventArgs > ValueChanged
```
Event for changes in the data at this location.

Register a handler to observe changes at the location of this [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) object. Each time time the data changes, your handler will be called with an immutable snapshot of the data.

## Public functions

### EndAt

```c#
Query EndAt(
  string value
)
```
Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to end at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### EndAt

```c#
Query EndAt(
  double value
)
```
Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to end at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### EndAt

```c#
Query EndAt(
  bool value
)
```
Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to end at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### EndAt

```c#
Query EndAt(
  string value,
  string key
)
```
Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key key less than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [EndAt(string value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ab96f9fe9354febf20403276c27b1be71) instead.

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to end at, inclusive | | `key` | The key to end at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### EndAt

```c#
Query EndAt(
  double value,
  string key
)
```
Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [EndAt(double value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ad16b26fc15b2fd9f761d19fbfda22d53) instead.

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to end at, inclusive | | `key` | The key to end at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### EndAt

```c#
Query EndAt(
  bool value,
  string key
)
```
Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [EndAt(bool value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a2b99446acd04ee76abdd4d2979f2a9ae) instead.

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to end at, inclusive | | `key` | The key to end at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### EqualTo

```c#
Query EqualTo(
  string value
)
```
Create a query constrained to only return child nodes with the given value

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to query for | |
| **Returns** | A query with the new constraint |

### EqualTo

```c#
Query EqualTo(
  double value
)
```
Create a query constrained to only return child nodes with the given value

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to query for | |
| **Returns** | A query with the new constraint |

### EqualTo

```c#
Query EqualTo(
  bool value
)
```
Create a query constrained to only return child nodes with the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to query for | |
| **Returns** | A query with the new constraint |

### EqualTo

```c#
Query EqualTo(
  string value,
  string key
)
```
Create a query constrained to only return the child node with the given key and value.

Create a query constrained to only return the child node with the given key and value. Note that there is at most one such child as names are unique.   

**Known issue** This currently does not work properly on iOS and tvOS. Please use [EqualTo(string value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a201d4cf96cd0608d9c954a50df8019f0) instead.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to query for | | `key` | The key of the child | |
| **Returns** | A query with the new constraint |

### EqualTo

```c#
Query EqualTo(
  double value,
  string key
)
```
Create a query constrained to only return the child node with the given key and value.

Create a query constrained to only return the child node with the given key and value. Note that there is at most one such child as keys are unique.   

**Known issue** This currently does not work properly on iOS and tvOS. Please use [EqualTo(double value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a2a492212cba7ab028c36aa2c65791ff7) instead.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to query for | | `key` | The key of the child | |
| **Returns** | A query with the new constraint |

### EqualTo

```c#
Query EqualTo(
  bool value,
  string key
)
```
Create a query constrained to only return the child node with the given key and value.

Create a query constrained to only return the child node with the given key and value. Note that there is at most one such child as keys are unique.   

**Known issue** This currently does not work properly on iOS and tvOS. Please use [EqualTo(bool value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1aeba6c847b1de73a1add49d184eeebaf9) instead.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to query for | | `key` | The name of the child | |
| **Returns** | A query with the new constraint |

### GetValueAsync

```c#
Task< DataSnapshot > GetValueAsync()
```

### KeepSynced

```c#
void KeepSynced(
  bool keepSynced
)
```
By calling `keepSynced(true)` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location.

By calling `keepSynced(true)` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `keepSynced` | Pass `true` to keep this location synchronized, pass `false` to stop synchronization. | |

### LimitToFirst

```c#
Query LimitToFirst(
  int limit
)
```
Create a query with limit and anchor it to the start of the window

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `limit` | The maximum number of child nodes to return | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### LimitToLast

```c#
Query LimitToLast(
  int limit
)
```
Create a query with limit and anchor it to the end of the window

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `limit` | The maximum number of child nodes to return | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### OrderByChild

```c#
Query OrderByChild(
  string path
)
```
Create a query in which child nodes are ordered by the values of the specified path.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | The path to the child node to use for sorting | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### OrderByKey

```c#
Query OrderByKey()
```
Create a query in which child nodes are ordered by their keys.

<br />

| Details ||
|---|---|
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### OrderByPriority

```c#
Query OrderByPriority()
```
Create a query in which child nodes are ordered by their priorities.

<br />

| Details ||
|---|---|
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### OrderByValue

```c#
Query OrderByValue()
```
Create a query in which nodes are ordered by their value

<br />

| Details ||
|---|---|
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### StartAt

```c#
Query StartAt(
  string value
)
```
Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to start at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### StartAt

```c#
Query StartAt(
  double value
)
```
Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to start at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### StartAt

```c#
Query StartAt(
  bool value
)
```
Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to start at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### StartAt

```c#
Query StartAt(
  string value,
  string key
)
```
Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [StartAt(string value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a579f39425905e1301d3cef7e6259abf2) instead.

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The priority to start at, inclusive | | `key` | The key to start at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### StartAt

```c#
Query StartAt(
  double value,
  string key
)
```
Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [StartAt(double value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1afb9a47a397b7eace4ed5e0379057be8f) instead.

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The priority to start at, inclusive | | `key` | The key name to start at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |

### StartAt

```c#
Query StartAt(
  bool value,
  string key
)
```
Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [StartAt(bool value)](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1af7fb01d52153f3acc63fe6372588b3b0) instead.

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The priority to start at, inclusive | | `key` | The key to start at, inclusive | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query) with the new constraint |