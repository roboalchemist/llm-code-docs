# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter.md.txt

# firebase::firestore::Filter Class Reference

# firebase::firestore::Filter


`#include <filter.h>`

A [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) represents a restriction on one or more field values and can be used to refine the results of a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query).

## Summary

| ### Constructors and Destructors ||
|---|---|
| [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a749f045a229851c7a95ed95fcea6a8a3)`(const `[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` & other)` Copy constructor. ||
| [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1aa89b5699198c1b32c2ea7723a0573203)`(`[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` && other)` Move constructor. ||
| [~Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a928d4cdd3b1c87bce12c022d394b2475)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                ### Public static functions                                                                                                                                                                                                                                                                                                                                                                 ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [And](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a049759e5a9163e1a9e7e95bed3c1f3b9)`(const Filters &... filters)`                                                                                                                                                                                                                                                                                                                           | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter that is a conjunction of the given filters.                                    |
| [And](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a3927cbe95f1e42c13c4277645a5f17cd)`(const std::vector< `[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` > & filters)`                                                                                                                                                                                      | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter that is a conjunction of the given filters.                                    |
| [ArrayContains](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a4110aba92017e62c88e334161802c518)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                                    | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given array field contains the given value.              |
| [ArrayContains](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a583d666b515eb2963a317500059f7800)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                    | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given array field contains the given value.              |
| [ArrayContainsAny](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a91cdc5665676336200629323cc6c51ba)`(const std::string & field, const std::vector< `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` > & values)`                                                                                                                                 | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given array field contains any of the given values.      |
| [ArrayContainsAny](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a8e9def09aabf3dd23a89bdc6353dc890)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const std::vector< `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` > & values)` | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given array field contains any of the given values.      |
| [EqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1ad537dd719a9d1671670e5aaadeb49f1d)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                                          | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is equal to the given value.                 |
| [EqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1aea6e367a6f641d0db952a645334b9997)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                          | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is equal to the given value.                 |
| [GreaterThan](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a5ae74b8e0c2f4b6227f778f4fe657fdf)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                                      | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is greater than the given value.             |
| [GreaterThan](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1ad81b48934ad126ce84b9b74e0a57074a)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                      | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is greater than the given value.             |
| [GreaterThanOrEqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a9b9d5f4ba3f5e597a59fac13fb7809d9)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                             | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is greater than or equal to the given value. |
| [GreaterThanOrEqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a49b40ebc3c84c1a310a3447125a10f4f)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`             | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is greater than or equal to the given value. |
| [In](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a6095aae52da06aaab3310a0e04ba8e78)`(const std::string & field, const std::vector< `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` > & values)`                                                                                                                                               | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field equals any of the given values.              |
| [In](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1aaf1131e1a4481799e90c868774e71e21)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const std::vector< `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` > & values)`               | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field equals any of the given values.              |
| [LessThan](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a4b7d69d07fdc5ccd6222d2aa00b886a4)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                                         | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is less than the given value.                |
| [LessThan](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a68c6605ada4c2273cc02365f79068357)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                         | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is less than the given value.                |
| [LessThanOrEqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a1951bcae8d2af80743f9bb5040fcb9b7)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                                | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is less than or equal to the given value.    |
| [LessThanOrEqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1adc8d2677463c8a6d2b84428d49343518)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is less than or equal to the given value.    |
| [NotEqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1abad32e0497352ba008e5d004a46ce1a3)`(const std::string & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                                                                                                                                                       | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is not equal to the given value.             |
| [NotEqualTo](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1ac8e7ae393a6fa088e318415a3a84ba75)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` & value)`                       | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field is not equal to the given value.             |
| [NotIn](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a175b391e163b438f6d2abb728d851d59)`(const std::string & field, const std::vector< `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` > & values)`                                                                                                                                            | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field does not equal any of the given values.      |
| [NotIn](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1aac9cefb733817e2e31f91042c5a6716c)`(const `[FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field, const std::vector< `[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value)` > & values)`            | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter for checking that the given field does not equal any of the given values.      |
| [Or](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a856a34c167e44487cfba990dc27172ca)`(const Filters &... filters)`                                                                                                                                                                                                                                                                                                                            | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter that is a disjunction of the given filters.                                    |
| [Or](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a86aaad2b14fdcdadee3d92f9371c35d3)`(const std::vector< `[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` > & filters)`                                                                                                                                                                                       | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) Creates a new filter that is a disjunction of the given filters.                                    |

|                                                                                                                                                                                                                                   ### Public functions                                                                                                                                                                                                                                   ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1aa526a16a1a8b578fc99880a1aee8a7e3)`(const `[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` & other)`     | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` &` Copy assignment operator. |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter_1a77e3e7ed9d32baf82352862af90c894e)`(`[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` && other) noexcept` | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter)` &` Move assignment operator. |

## Public static functions

### And

```c++
Filter And(
  const Filters &... filters
)
```  
Creates a new filter that is a conjunction of the given filters.

A conjunction filter includes a document if it satisfies all of the given filters.

If no filter is given, the composite filter is a no-op, and if only one filter is given, the composite filter has the same behavior as the underlying filter.

<br />

|                                                             Details                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-------------------------------------------| | `filters` | The filters to perform a conjunction for. | |
| **Returns** | The newly created filter.                                                                                           |

### And

```c++
Filter And(
  const std::vector< Filter > & filters
)
```  
Creates a new filter that is a conjunction of the given filters.

A conjunction filter includes a document if it satisfies all of the given filters.

If no filter is given, the composite filter is a no-op, and if only one filter is given, the composite filter has the same behavior as the underlying filter.

<br />

|                                                                                Details                                                                                 ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|--------------------------------------------------------------| | `filters` | The list that contains filters to perform a conjunction for. | |
| **Returns** | The newly created filter.                                                                                                                                 |

### ArrayContains

```c++
Filter ArrayContains(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given array field contains the given value.

<br />

|                                                                                                        Details                                                                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------| | `field` | The name of the field containing an array to search. | | `value` | The value that must be contained in the array.       | |
| **Returns** | The newly created filter.                                                                                                                                                                                |

### ArrayContains

```c++
Filter ArrayContains(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given array field contains the given value.

<br />

|                                                                                                        Details                                                                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------| | `field` | The path of the field containing an array to search. | | `value` | The value that must be contained in the array.       | |
| **Returns** | The newly created filter.                                                                                                                                                                                |

### ArrayContainsAny

```c++
Filter ArrayContainsAny(
  const std::string & field,
  const std::vector< FieldValue > & values
)
```  
Creates a new filter for checking that the given array field contains any of the given values.

<br />

|                                                                                                         Details                                                                                                          ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|------------------------------------------------------| | `field`  | The name of the field containing an array to search. | | `values` | The list of values to match.                         | |
| **Returns** | The newly created filter.                                                                                                                                                                                   |

### ArrayContainsAny

```c++
Filter ArrayContainsAny(
  const FieldPath & field,
  const std::vector< FieldValue > & values
)
```  
Creates a new filter for checking that the given array field contains any of the given values.

<br />

|                                                                                                         Details                                                                                                          ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|------------------------------------------------------| | `field`  | The path of the field containing an array to search. | | `values` | The list of values to match.                         | |
| **Returns** | The newly created filter.                                                                                                                                                                                   |

### EqualTo

```c++
Filter EqualTo(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The name of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### EqualTo

```c++
Filter EqualTo(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The path of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### GreaterThan

```c++
Filter GreaterThan(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is greater than the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The name of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### GreaterThan

```c++
Filter GreaterThan(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is greater than the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The path of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### GreaterThanOrEqualTo

```c++
Filter GreaterThanOrEqualTo(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is greater than or equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The name of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### GreaterThanOrEqualTo

```c++
Filter GreaterThanOrEqualTo(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is greater than or equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The path of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### In

```c++
Filter In(
  const std::string & field,
  const std::vector< FieldValue > & values
)
```  
Creates a new filter for checking that the given field equals any of the given values.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|-----------------------------------| | `field`  | The name of the field to compare. | | `values` | The list of values to match.      | |
| **Returns** | The newly created filter.                                                                                                                          |

### In

```c++
Filter In(
  const FieldPath & field,
  const std::vector< FieldValue > & values
)
```  
Creates a new filter for checking that the given field equals any of the given values.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|-----------------------------------| | `field`  | The path of the field to compare. | | `values` | The list of values to match.      | |
| **Returns** | The newly created filter.                                                                                                                          |

### LessThan

```c++
Filter LessThan(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is less than the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The name of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### LessThan

```c++
Filter LessThan(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is less than the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The path of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### LessThanOrEqualTo

```c++
Filter LessThanOrEqualTo(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is less than or equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The name of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### LessThanOrEqualTo

```c++
Filter LessThanOrEqualTo(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is less than or equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The path of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### NotEqualTo

```c++
Filter NotEqualTo(
  const std::string & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is not equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The name of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### NotEqualTo

```c++
Filter NotEqualTo(
  const FieldPath & field,
  const FieldValue & value
)
```  
Creates a new filter for checking that the given field is not equal to the given value.

<br />

|                                                                           Details                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `field` | The path of the field to compare. | | `value` | The value for comparison          | |
| **Returns** | The newly created filter.                                                                                                                       |

### NotIn

```c++
Filter NotIn(
  const std::string & field,
  const std::vector< FieldValue > & values
)
```  
Creates a new filter for checking that the given field does not equal any of the given values.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|-----------------------------------| | `field`  | The name of the field to compare. | | `values` | The list of values to match.      | |
| **Returns** | The newly created filter.                                                                                                                          |

### NotIn

```c++
Filter NotIn(
  const FieldPath & field,
  const std::vector< FieldValue > & values
)
```  
Creates a new filter for checking that the given field does not equal any of the given values.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|-----------------------------------| | `field`  | The path of the field to compare. | | `values` | The list of values to match.      | |
| **Returns** | The newly created filter.                                                                                                                          |

### Or

```c++
Filter Or(
  const Filters &... filters
)
```  
Creates a new filter that is a disjunction of the given filters.

A disjunction filter includes a document if it satisfies *any* of the given filters.

If no filter is given, the composite filter is a no-op, and if only one filter is given, the composite filter has the same behavior as the underlying filter.

<br />

|                                                             Details                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-------------------------------------------| | `filters` | The filters to perform a disjunction for. | |
| **Returns** | The newly created filter.                                                                                           |

### Or

```c++
Filter Or(
  const std::vector< Filter > & filters
)
```  
Creates a new filter that is a disjunction of the given filters.

A disjunction filter includes a document if it satisfies *any* of the given filters.

If no filter is given, the composite filter is a no-op, and if only one filter is given, the composite filter has the same behavior as the underlying filter.

<br />

|                                                                                Details                                                                                 ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|--------------------------------------------------------------| | `filters` | The list that contains filters to perform a disjunction for. | |
| **Returns** | The newly created filter.                                                                                                                                 |

## Public functions

### Filter

```c++
 Filter(
  const Filter & other
)
```  
Copy constructor.

[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) is immutable and can be efficiently copied.

<br />

|                                                                                                                                                              Details                                                                                                                                                              ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) to copy from. | |

### Filter

```c++
 Filter(
  Filter && other
) noexcept
```  
Move constructor.

<br />

|                                                                                                                                                                   Details                                                                                                                                                                   ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) to move data from. | |

### operator=

```c++
Filter & operator=(
  const Filter & other
)
```  
Copy assignment operator.

[Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) is immutable and can be efficiently copied.

<br />

|                                                                                                                                                              Details                                                                                                                                                               ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|----------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) to copy from. | |
| **Returns** | Reference to the destination [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter).                                                                                                                                                          |

### operator=

```c++
Filter & operator=(
  Filter && other
) noexcept
```  
Move assignment operator.

<br />

|                                                                                                                                                                   Details                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter) to move data from. | |
| **Returns** | Reference to the destination [Filter](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter).                                                                                                                                                                    |

### \~Filter

```c++
 ~Filter()
```