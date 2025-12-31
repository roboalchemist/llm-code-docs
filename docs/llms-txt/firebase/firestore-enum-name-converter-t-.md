# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-enum-name-converter-t-.md.txt

# Firebase.Firestore.FirestoreEnumNameConverter Class Reference

# Firebase.Firestore.FirestoreEnumNameConverter\< T \>

Custom converter which uses enum value names instead of integer values as the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) representation.

## Summary

This converter is not used by default; it must be configured in the same way as any other custom converter.

Currently this is always case-sensitive, with no customization of the names used. In future releases we may introduce further ways to configure this converter, but the default behavior will remain the same.

When the same enum value has multiple names, no guarantee is made about which one is returned, although both are accepted for conversion back to enum values. You are strongly encouraged not to use multiple names for the same value.

<br />

|                                          Details                                           ||
|---------------------|-----------------------------------------------------------------------|
| Template Parameters | |-----|--------------------------| | `T` | The enum type to convert | |

### Inheritance

Inherits from: FirestoreConverter\< T \>

|                                                                                                                                               ### Public functions                                                                                                                                               ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [FromFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-enum-name-converter-t-#class_firebase_1_1_firestore_1_1_firestore_enum_name_converter_3_01_t_01_4_1ab9cf43597380685027005325fed3ffeb)`(object value)` | `override T`                                          |
| [ToFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-enum-name-converter-t-#class_firebase_1_1_firestore_1_1_firestore_enum_name_converter_3_01_t_01_4_1af4efa3dadd02aeac4199e873fe9be714)`(T value)`        | `override object` Converts an enum value to its name. |

## Public functions

### FromFirestore

```c#
override T FromFirestore(
  object value
)
```  

### ToFirestore

```c#
override object ToFirestore(
  T value
)
```  
Converts an enum value to its name.

If multiple values in the enum map to the same integer, it is undefined which will be returned. If the value is not a named enum element, an exception is thrown, even if the enum is decorated with FlagsAttribute.

<br />

|                                                                                   Details                                                                                    ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------| | `value` | The value to convert. |                                                                                         |
| Exceptions  | |---------------------|-------------------------------------------------------| | `ArgumentException` | The given value is not a named value within the enum. | |
| **Returns** | The name of the value.                                                                                                                                          |