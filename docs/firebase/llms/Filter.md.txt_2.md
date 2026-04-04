# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter.md.txt

# Firebase.Firestore.Filter Class Reference

# Firebase.Firestore.Filter

A [Filter](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter) represents a restriction on one or more field values and can be used to refine the results of a [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query).

## Summary

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1afa30b6d929b8a20bb18bce5370434bdd(params https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter[] filters)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter that is a conjunction of the given filters. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a3a542576a782081d84b6197f2a345afe(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given array field contains the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a49b470300282a731cf389db2a1eadd7e(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given array field contains the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a572fd91823ae1683737e1b78a55336d0(string fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given array field contains any of the given values. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a59bb3e982db4e0dd5fcec231b289a116(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given array field contains any of the given values. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a01cbf5d04e26977b8716319aae11cac9(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1ad4b46c890112aadd9709b6c34fd8d85d(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1ad243f8ee2ac2e982ae0a8612770817c2(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is greater than the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a19e498159459eccd40af98a8c2a5bab0(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is greater than the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a354ee5e124c55aa80b8d248ecea05cf4(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is greater than or equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1aa573fe5820925d64167ba256d43189ae(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is greater than or equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1ad33e1bf3ae4106da69ae71a174c72fb6(string fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field equals any of the given values. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a3375514c09a923ec4f314a3495a59326(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field equals any of the given values. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a581f5329c1896c8e6a728e0a9267bbad(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is less than the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a9b91ffcbaa29ae6e787717af20dccdab(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is less than the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a1354c418df041d6f52e4394a04481a25(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is less than or equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1aa98b7fef1b0238b10bcdacf6b721068e(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is less than or equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a30b861ec46fca779939cc2d7e7b4eed3(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is not equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a03bb8c70602d52e52e31cd97a4a00a19(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field is not equal to the given value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a7d8e32080606666f6c5c32ef87156f38(string fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field does not equal any of the given values. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a7ce20c6b64cd0e5eadb17d4f687899bd(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter for checking that the given field does not equal any of the given values. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter_1a50d082de185cdeeb2c32af986f27b5d3(params https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter[] filters)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter` Creates a new filter that is a disjunction of the given filters. |

## Public static functions

### And

```c#
Filter And(
  params Filter[] filters
)
```
Creates a new filter that is a conjunction of the given filters.

A conjunction filter includes a document if it satisfies all of the given filters.

If no filter is given, the composite filter is a no-op, and if only one filter is given, the composite filter has the same behavior as the underlying filter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `filters` | The filters to perform a conjunction for. | |
| **Returns** | The newly created filter. |

### ArrayContains

```c#
Filter ArrayContains(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given array field contains the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field containing an array to search. | | `value` | The value that must be contained in the array. | |
| **Returns** |   |

### ArrayContains

```c#
Filter ArrayContains(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given array field contains the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field containing an array to search. | | `value` | The value that must be contained in the array. | |
| **Returns** | The newly created filter. |

### ArrayContainsAny

```c#
Filter ArrayContainsAny(
  string fieldPath,
  IEnumerable< object > values
)
```
Creates a new filter for checking that the given array field contains any of the given values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field containing an array to search. | | `values` | The list of values to match. | |
| **Returns** | The newly created filter. |

### ArrayContainsAny

```c#
Filter ArrayContainsAny(
  FieldPath fieldPath,
  IEnumerable< object > values
)
```
Creates a new filter for checking that the given array field contains any of the given values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field containing an array to search. | | `values` | The list of values to match. | |
| **Returns** | The newly created filter. |

### EqualTo

```c#
Filter EqualTo(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### EqualTo

```c#
Filter EqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field containing an array to search. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### GreaterThan

```c#
Filter GreaterThan(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is greater than the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### GreaterThan

```c#
Filter GreaterThan(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is greater than the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### GreaterThanOrEqualTo

```c#
Filter GreaterThanOrEqualTo(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is greater than or equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### GreaterThanOrEqualTo

```c#
Filter GreaterThanOrEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is greater than or equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### In

```c#
Filter In(
  string fieldPath,
  IEnumerable< object > values
)
```
Creates a new filter for checking that the given field equals any of the given values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `values` | The list of values to match. | |
| **Returns** |   |

### In

```c#
Filter In(
  FieldPath fieldPath,
  IEnumerable< object > values
)
```
Creates a new filter for checking that the given field equals any of the given values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `values` | The list of values to match. | |
| **Returns** | The newly created filter. |

### LessThan

```c#
Filter LessThan(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is less than the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### LessThan

```c#
Filter LessThan(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is less than the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### LessThanOrEqualTo

```c#
Filter LessThanOrEqualTo(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is less than or equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### LessThanOrEqualTo

```c#
Filter LessThanOrEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is less than or equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### NotEqualTo

```c#
Filter NotEqualTo(
  string fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is not equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### NotEqualTo

```c#
Filter NotEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates a new filter for checking that the given field is not equal to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The newly created filter. |

### NotIn

```c#
Filter NotIn(
  string fieldPath,
  IEnumerable< object > values
)
```
Creates a new filter for checking that the given field does not equal any of the given values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the field to compare. | | `values` | The list of values to match. | |
| **Returns** | The newly created filter. |

### NotIn

```c#
Filter NotIn(
  FieldPath fieldPath,
  IEnumerable< object > values
)
```
Creates a new filter for checking that the given field does not equal any of the given values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The path of the field to compare. | | `values` | The list of values to match. | |
| **Returns** | The newly created filter. |

### Or

```c#
Filter Or(
  params Filter[] filters
)
```
Creates a new filter that is a disjunction of the given filters.

A disjunction filter includes a document if it satisfies any of the given filters.

If no filter is given, the composite filter is a no-op, and if only one filter is given, the composite filter has the same behavior as the underlying filter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `filters` | The filters to perform a disjunction for. | |
| **Returns** | The newly created filter. |