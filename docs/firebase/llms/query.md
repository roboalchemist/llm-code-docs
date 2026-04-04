# Source: https://firebase.google.com/docs/reference/data-connect/gql/query.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/query.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/query.md.txt

# firebase::database::Query Class Reference

# firebase::database::Query


`#include <query.h>`

The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) class is used for reading data.

## Summary

Listeners can be attached, which will be triggered when the data changes.

### Inheritance

Direct Known Subclasses:[firebase::database::DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference)

| ### Constructors and Destructors ||
|---|---|
| [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1ae7cbf62d262d121962d2ae1bb7617522)`()` Default constructor. ||
| [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aaa4356c97c1dbc6bf0f0656dc7a7807b)`(const `[Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query)` & query)` Copy constructor. ||
| [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a66d5c725647e676fd4242ccb801380e2)`(`[Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query)` && query)` Move constructor. ||
| [~Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a0cfac5d5b9d96bfef69aec37f16f98da)`()` Required virtual destructor. ||

|                                                                                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                     ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AddChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750)`(`[ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener)` *listener)`    | `void` Adds a listener that will be called any time a child is added, removed, modified, or reordered.                                                                                                                                                                                                                                                                                                                                                                        |
| [AddValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810)`(`[ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener)` *listener)`    | `void` Adds a listener that will be called immediately and then again any time the data changes.                                                                                                                                                                                                                                                                                                                                                                              |
| [EndAt](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a24504e530c9ba49e3d3ada52ec6e47c1)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` order_value)`                                                      | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or lower.                                                                                                                                                            |
| [EndAt](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a229885e98360bfc52a423d26db4c4a14)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` order_value, const char *child_key)`                               | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or lower, and the given key or lower.                                                                                                                                |
| [EqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1ac07ca967bbec3db1bf8906fc325e0e68)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` order_value)`                                                    | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the exact given sort value.                                                                                                                                                               |
| [EqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a886202008d893180647ff67b670d1019)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` order_value, const char *child_key)`                             | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the exact given sort value, and the exact given key.                                                                                                                                      |
| [GetReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a46b59f642ce2d12d9aa33b9b40eb37e9)`() const `                                                                                                                                                                | [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) Gets a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) corresponding to the given location.                                                                                                   |
| [GetValue](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a562ab39d0575e2c8a8fbe2315ed52fb8)`()`                                                                                                                                                                           | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` >` Gets the value of the query for the given location a single time.                                                                                                                                             |
| [GetValueLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aee8e9012c306553851e32cac66c1b211)`()`                                                                                                                                                                 | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` >` Gets the result of the most recent call to [GetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a562ab39d0575e2c8a8fbe2315ed52fb8). |
| [LimitToFirst](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a825c551e69560f2522db426b3300274c)`(size_t limit)`                                                                                                                                                           | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Gets a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) limited to only the first results.                                                                                                                                                                                 |
| [LimitToLast](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1ac13afd9f657d30e5927c319f5acd6aaf)`(size_t limit)`                                                                                                                                                            | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Gets a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) limited to only the last results.                                                                                                                                                                                  |
| [OrderByChild](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a18250ad084814598c9cbd96df7f3eb30)`(const char *path)`                                                                                                                                                       | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Gets a query in which child nodes are ordered by the values of the specified path.                                                                                                                                                                                                                                                                  |
| [OrderByChild](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a0a6290971237a1d367583f18b5c6a3a0)`(const std::string & path)`                                                                                                                                               | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Gets a query in which child nodes are ordered by the values of the specified path.                                                                                                                                                                                                                                                                  |
| [OrderByKey](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1abc509b58705fc896ef9be808b759a5af)`()`                                                                                                                                                                         | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Gets a query in which child nodes are ordered by their keys.                                                                                                                                                                                                                                                                                        |
| [OrderByPriority](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a4bf0bc99c7133c90277e3d9dde0946d3)`()`                                                                                                                                                                    | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Gets a query in which child nodes are ordered by their priority.                                                                                                                                                                                                                                                                                    |
| [OrderByValue](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1ae9718eb0511153f404e16db1800bfc3f)`()`                                                                                                                                                                       | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Create a query in which nodes are ordered by their value.                                                                                                                                                                                                                                                                                           |
| [RemoveAllChildListeners](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a505c51cb77cefb2fae31d23999d4a56d)`()`                                                                                                                                                            | `void` Removes all child listeners that were added by [AddChildListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750).                                                                                                                                                                                                                                              |
| [RemoveAllValueListeners](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1abf356818e2d12cd09e20b020d9c5b50d)`()`                                                                                                                                                            | `void` Removes all value listeners that were added with [AddValueListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810).                                                                                                                                                                                                                                            |
| [RemoveChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a71862feda6f04f19d45fdae297b024a5)`(`[ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener)` *listener)` | `void` Removes a listener that was previously added with [AddChildListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750).                                                                                                                                                                                                                                           |
| [RemoveValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1addfac4809c61fc91567e033e4edc90f9)`(`[ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener)` *listener)` | `void` Removes a listener that was previously added with [AddValueListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810).                                                                                                                                                                                                                                           |
| [SetKeepSynchronized](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a7e21505d9c247bf03abe564fe08baa56)`(bool keep_sync)`                                                                                                                                                  | `void` Sets whether this location's data should be kept in sync even if there are no active Listeners.                                                                                                                                                                                                                                                                                                                                                                        |
| [StartAt](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a77abcf23c95bf6ad500f2a30b46f9a35)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` order_value)`                                                    | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or higher.                                                                                                                                                           |
| [StartAt](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a8a61996a0ab4e1abfd2e2b4970bafa28)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` order_value, const char *child_key)`                             | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or higher, and the given key or higher.                                                                                                                              |
| [is_valid](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1af1a2fa40d9fbc1abe939d8a9280307cd)`() const `                                                                                                                                                                    | `virtual bool` Returns true if this query is valid, false if it is not valid.                                                                                                                                                                                                                                                                                                                                                                                                 |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a7b6e16816b819d7b9dc030e5282ac5eb)`(const `[Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query)` & query)`                                 | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query)` &` Copy assignment operator.                                                                                                                                                                                                                                                                                                                       |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1af98d7ce987ba005c897aa54a891fda92)`(`[Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query)` && query)`                                      | [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query)` &` Move assignment operator.                                                                                                                                                                                                                                                                                                                       |

## Public functions

### AddChildListener

```c++
void AddChildListener(
  ChildListener *listener
)
```  
Adds a listener that will be called any time a child is added, removed, modified, or reordered.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                                                                                  ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `listener` | A [ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener) instance, which must remain in memory until you remove the listener from the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query). | |

### AddValueListener

```c++
void AddValueListener(
  ValueListener *listener
)
```  
Adds a listener that will be called immediately and then again any time the data changes.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                                                                                  ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `listener` | A [ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener) instance, which must remain in memory until you remove the listener from the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query). | |

### EndAt

```c++
Query EndAt(
  Variant order_value
)
```  
Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or lower.

This method is used to generate a reference to a limited view of the data at this location. The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) returned will only refer to child nodes with a value less than or equal to the given value, using the given OrderBy directive (or priority as default).

<br />

|                                                                                                                                                                                             Details                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `order_value` | The highest sort value the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should refer to. | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, filtering out child nodes that have a higher sort value or key than the sort value or key specified.                                                                                                                             |

### EndAt

```c++
Query EndAt(
  Variant order_value,
  const char *child_key
)
```  
Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or lower, and the given key or lower.

This method is used to generate a reference to a limited view of the data at this location. The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) returned will only refer to child nodes with a value less than or equal to the given value, using the given OrderBy directive (or priority as default), and additionally only child nodes with a key less than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [EndAt(Variant order_value)](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a24504e530c9ba49e3d3ada52ec6e47c1) instead.

<br />

|                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                         ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `order_value` | The highest sort value the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include. | | `child_key`   | The highest key the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include.        | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, filtering out child nodes that have a higher sort value than the sort value specified, or a higher key than the key specified.                                                                                                                                                                                                                                                                                          |

### EqualTo

```c++
Query EqualTo(
  Variant order_value
)
```  
Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the exact given sort value.

This method is used to create a query constrained to only return child nodes with the given value, using the given OrderBy directive (or priority as default).

<br />

|                                                                                                                                                                                          Details                                                                                                                                                                                           ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `order_value` | The exact sort value the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include. | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, filtering out child nodes that have a different sort value than the sort value specified.                                                                                                                                  |

### EqualTo

```c++
Query EqualTo(
  Variant order_value,
  const char *child_key
)
```  
Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the exact given sort value, and the exact given key.

This method is used to create a query constrained to only return the child node with the given value, using the given OrderBy directive (or priority as default), and the given key. Note that there is at most one such child as child key names are unique.

**Known issue** This currently does not work properly on iOS, tvOS and desktop. Please use [EqualTo(Variant order_value)](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1ac07ca967bbec3db1bf8906fc325e0e68) instead.

<br />

|                                                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                                                      ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `order_value` | The exact sort value the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include. | | `child_key`   | The exact key the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include.        | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, filtering out child nodes that have a different sort value than the sort value specified, and containing at most one child with the exact key specified.                                                                                                                                                                                                                                                          |

### GetReference

```c++
DatabaseReference GetReference() const 
```  
Gets a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) corresponding to the given location.

<br />

|                                                                                                                                                                                                   Details                                                                                                                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) corresponding to the same location as the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query), but without any of the ordering or filtering parameters. |

### GetValue

```c++
Future< DataSnapshot > GetValue()
```  
Gets the value of the query for the given location a single time.

This is an asynchronous operation which takes time to execute, and uses [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) to return its result.

<br />

|                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                     ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. On this [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)'s completion, if its Error is kErrorNone, the operation succeeded, and the [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) contains the data in this location. |

### GetValueLastResult

```c++
Future< DataSnapshot > GetValueLastResult()
```  
Gets the result of the most recent call to [GetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a562ab39d0575e2c8a8fbe2315ed52fb8).

<br />

|                                                                                                      Details                                                                                                      ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Result of the most recent call to [GetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a562ab39d0575e2c8a8fbe2315ed52fb8). |

### LimitToFirst

```c++
Query LimitToFirst(
  size_t limit
)
```  
Gets a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) limited to only the first results.

Limits the query to reference only the first N child nodes, using the given OrderBy directive (or priority as default).

<br />

|                                                                                                                                                                               Details                                                                                                                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------| | `limit` | Number of children to limit the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) to. | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, limited to the specified number of children (taken from the beginning of the sorted list).                                                                                                           |

### LimitToLast

```c++
Query LimitToLast(
  size_t limit
)
```  
Gets a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) limited to only the last results.

<br />

|                                                                                                                                                                               Details                                                                                                                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------| | `limit` | Number of children to limit the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) to. | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, limited to the specified number of children (taken from the end of the sorted list).                                                                                                                 |

### OrderByChild

```c++
Query OrderByChild(
  const char *path
)
```  
Gets a query in which child nodes are ordered by the values of the specified path.

Any previous OrderBy directive will be replaced in the returned [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query).

<br />

|                                                                                                                                                                          Details                                                                                                                                                                           ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------| | `path` | Path to a child node. The value of this node will be used for sorting this query. The pointer you pass in need not remain valid after the call completes. | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, with the children are sorted by the value of their own child specified here.                                                                                                               |

### OrderByChild

```c++
Query OrderByChild(
  const std::string & path
)
```  
Gets a query in which child nodes are ordered by the values of the specified path.

Any previous OrderBy directive will be replaced in the returned [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query).

<br />

|                                                                                                                   Details                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-----------------------------------------------------------------------------------| | `path` | Path to a child node. The value of this node will be used for sorting this query. |                                   |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, with the children are sorted by the value of their own child specified here. |

### OrderByKey

```c++
Query OrderByKey()
```  
Gets a query in which child nodes are ordered by their keys.

Any previous OrderBy directive will be replaced in the returned [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query).

<br />

|                                                                                                  Details                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, with the children are sorted by their key. |

### OrderByPriority

```c++
Query OrderByPriority()
```  
Gets a query in which child nodes are ordered by their priority.

Any previous OrderBy directive will be replaced in the returned [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query).

<br />

|                                                                                                     Details                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, with the children are sorted by their priority. |

### OrderByValue

```c++
Query OrderByValue()
```  
Create a query in which nodes are ordered by their value.

<br />

|                                                                                                   Details                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, with the children are sorted by their value. |

### Query

```c++
 Query()
```  
Default constructor.

This creates an invalid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query). Attempting to perform any operations on this reference will fail unless a valid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) has been assigned to it.  

### Query

```c++
 Query(
  const Query & query
)
```  
Copy constructor.

Queries can be copied. Copies exist independently of each other.  

### Query

```c++
 Query(
  Query && query
)
```  
Move constructor.  

### RemoveAllChildListeners

```c++
void RemoveAllChildListeners()
```  
Removes all child listeners that were added by [AddChildListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750).


| **Note:** You can remove ChildListeners from a different [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) than you added them to, as long as the two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances are equivalent.

<br />

### RemoveAllValueListeners

```c++
void RemoveAllValueListeners()
```  
Removes all value listeners that were added with [AddValueListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810).


| **Note:** You can remove ValueListeners from a different [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) than you added them to, as long as the two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances are equivalent.

<br />

### RemoveChildListener

```c++
void RemoveChildListener(
  ChildListener *listener
)
```  
Removes a listener that was previously added with [AddChildListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750).


| **Note:** You can remove a [ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener) from a different [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) than you added it to, as long as the two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances are equivalent.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                        Details                                                                                                                                                                                                                                                                                                                                                                                                        ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `listener` | A [ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener) instance to remove from the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query). After it is removed, you can delete it or attach it to a new location. | |

### RemoveValueListener

```c++
void RemoveValueListener(
  ValueListener *listener
)
```  
Removes a listener that was previously added with [AddValueListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810).


| **Note:** You can remove a [ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener) from a different [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) than you added it to, as long as the two [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) instances are equivalent.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                        Details                                                                                                                                                                                                                                                                                                                                                                                                        ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `listener` | A [ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener) instance to remove from the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query). After it is removed, you can delete it or attach it to a new location. | |

### SetKeepSynchronized

```c++
void SetKeepSynchronized(
  bool keep_sync
)
```  
Sets whether this location's data should be kept in sync even if there are no active Listeners.

By calling SetKeepSynchronized(true) on a given database location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location. Additionally, while a location is kept synced, it will not be evicted from the persistent disk cache.

<br />

|                                                                                                             Details                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|-----------------------------------------------------------------------------------------| | `keep_sync` | If true, set this location to be synchronized. If false, set it to not be synchronized. | |

### StartAt

```c++
Query StartAt(
  Variant order_value
)
```  
Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or higher.

This method is used to generate a reference to a limited view of the data at this location. The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) returned will only refer to child nodes with a value greater than or equal to the given value, using the given OrderBy directive (or priority as the default).

<br />

|                                                                                                                                                                                           Details                                                                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `order_value` | The lowest sort value the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include. | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, filtering out child nodes that have a lower sort value than the sort value specified.                                                                                                                                        |

### StartAt

```c++
Query StartAt(
  Variant order_value,
  const char *child_key
)
```  
Get a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) constrained to nodes with the given sort value or higher, and the given key or higher.

This method is used to generate a reference to a limited view of the data at this location. The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) returned will only refer to child nodes with a value greater than or equal to the given value, using the given OrderBy directive (or priority as default), and additionally only child nodes with a key greater than or equal to the given key.

**Known issue** This currently does not work properly on all platforms. Please use [StartAt(Variant order_value)](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a77abcf23c95bf6ad500f2a30b46f9a35) instead.

<br />

|                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                        ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `order_value` | The lowest sort value the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include. | | `child_key`   | The lowest key the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) should include.        | |
| **Returns** | A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) in this same location, filtering out child nodes that have a lower sort value than the sort value specified, or a lower key than the key specified.                                                                                                                                                                                                                                                                                         |

### is_valid

```c++
virtual bool is_valid() const 
```  
Returns true if this query is valid, false if it is not valid.

An invalid query could be returned by, say, attempting to OrderBy two different items, or calling [OrderByChild()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a18250ad084814598c9cbd96df7f3eb30) with an empty path, or by constructing a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) with the default constructor. If a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) is invalid, attempting to add more constraints will also result in an invalid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query).

<br />

|                                  Details                                  ||
|-------------|--------------------------------------------------------------|
| **Returns** | true if this query is valid, false if this query is invalid. |

### operator=

```c++
Query & operator=(
  const Query & query
)
```  
Copy assignment operator.

Queries can be copied. Copies exist independently of each other.  

### operator=

```c++
Query & operator=(
  Query && query
)
```  
Move assignment operator.  

### \~Query

```c++
virtual  ~Query()
```  
Required virtual destructor.