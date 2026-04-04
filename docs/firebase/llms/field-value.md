# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value.md.txt

# Firebase.Firestore.FieldValue Class Reference

# Firebase.Firestore.FieldValue

A static class providing properties and methods to represent sentinel values.

## Summary

Sentinel values are special values where the client-side value is not part of the document modification sent to the server. A property decorated with [FirestorePropertyAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute#class_firebase_1_1_firestore_1_1_firestore_property_attribute) can specify an additional attribute to indicate that it's a sentinel value, such as a [ServerTimestampAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/server-timestamp-attribute#class_firebase_1_1_firestore_1_1_server_timestamp_attribute), or the sentinel values returned by the members of this class can be used directly as values to be serialized (for example, in anonymous types), and they will be handled directly by the serialization mechanism.

|                                                                                                                                                                           ### Properties                                                                                                                                                                            ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Delete](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a5a052c06b8e7d76853965d0286d64951)` = FieldValueProxy.ServerTimestamp()` | `static object` Sentinel value indicating that the field should be deleted from the document.                                                |
| [ServerTimestamp](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a6a7acc0716c4387af701ed5b250575a2)                              | `static object` Sentinel value indicating that the field should be set to the timestamp of the commit that creates or modifies the document. |

|                                                                                                                                                                                             ### Public static functions                                                                                                                                                                                             ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArrayRemove](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a4bd53bf887e9f9e1425ccef0eb35026a)`(params object[] elements)` | `object` Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to remove the given elements from any array value that already exists on the server. |
| [ArrayUnion](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1ac05084586564ce5d391bc35d9422d479)`(params object[] elements)`  | `object` Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to union the given elements with any array value that already exists on the server.  |
| [Increment](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a9744159debfe114ea4d21ab2b0a81c19)`(long value)`                 | `object` Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to increment the field's current value by the given value.                           |
| [Increment](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a045b4cb714158b545948e7f4131f76dc)`(double value)`               | `object` Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to increment the field's current value by the given value.                           |

## Properties

### Delete

```c#
static object Delete = FieldValueProxy.ServerTimestamp()
```  
Sentinel value indicating that the field should be deleted from the document.  

### ServerTimestamp

```c#
static object ServerTimestamp
```  
Sentinel value indicating that the field should be set to the timestamp of the commit that creates or modifies the document.

## Public static functions

### ArrayRemove

```c#
object ArrayRemove(
  params object[] elements
)
```  
Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to remove the given elements from any array value that already exists on the server.

All instances of each element specified will be removed from the array. If the field being modified is not already an array, it will be overwritten with an empty array.

<br />

|                                                                                                             Details                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|----------------------------------------| | `elements` | The elements to remove from the array. |                                                                                                     |
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value) sentinel for use in a call to `SetAsync()` or `UpdateAsync()`. |

### ArrayUnion

```c#
object ArrayUnion(
  params object[] elements
)
```  
Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to union the given elements with any array value that already exists on the server.

Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array, it will be overwritten with an array containing exactly the specified elements.

<br />

|                                                                                                             Details                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|---------------------------------------| | `elements` | The elements to union into the array. |                                                                                                       |
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value) sentinel for use in a call to `SetAsync()` or `UpdateAsync()`. |

### Increment

```c#
object Increment(
  long value
)
```  
Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to increment the field's current value by the given value.

If the current field value is an integer, possible integer overflows are resolved to System.Int64.MinValue or System.Int64.MaxValue. If the current field value is a double, both values will be interpreted as doubles and the arithmetic will follow IEEE 754 semantics.

If the current field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value.

<br />

|                                                                                                             Details                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value) sentinel for use in a call to `SetAsync()` or `UpdateAsync()`. |

### Increment

```c#
object Increment(
  double value
)
```  
Returns a special value that can be used with `SetAsync()` or `UpdateAsync()` that tells the server to increment the field's current value by the given value.

If the current value is an integer or a double, both the current and the given value will be interpreted as doubles and all arithmetic will follow IEEE 754 semantics. Otherwise, the transformation will set the field to the given value.

<br />

|                                                                                                             Details                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value) sentinel for use in a call to `SetAsync()` or `UpdateAsync()`. |