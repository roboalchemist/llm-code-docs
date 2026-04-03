# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute.md.txt

# Firebase.Firestore.FirestorePropertyAttribute Class Reference

# Firebase.Firestore.FirestorePropertyAttribute

Attribute indicating that a property should be included in [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) conversions.

## Summary

### Inheritance

Inherits from: Attribute

| ### Constructors and Destructors ||
|---|---|
| [FirestorePropertyAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute#class_firebase_1_1_firestore_1_1_firestore_property_attribute_1ab547faec0f9ec373544725e92080ae4e)`()` Creates an instance with no specified name. ||
| [FirestorePropertyAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute#class_firebase_1_1_firestore_1_1_firestore_property_attribute_1a5ddd8053eb2185f203d542acc41a0253)`(string name)` Creates an instance with the specified name. ||

|                                                                                                                                                                                           ### Properties                                                                                                                                                                                            ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ConverterType](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute#class_firebase_1_1_firestore_1_1_firestore_property_attribute_1aad47a5790f604649b51207f76a74857b) | `System.Type` A custom converter type to use for the attributed property.                                                                                                 |
| [Name](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute#class_firebase_1_1_firestore_1_1_firestore_property_attribute_1af5c1e545a500bf952248c6e9e1bc1f90)          | `string` The name to use within the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) document. |

## Properties

### ConverterType

```c#
System.Type ConverterType
```  
A custom converter type to use for the attributed property.  

### Name

```c#
string Name
```  
The name to use within the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) document.

If not set, the name of the property is used directly.

## Public functions

### FirestorePropertyAttribute

```c#
 FirestorePropertyAttribute()
```  
Creates an instance with no specified name.  

### FirestorePropertyAttribute

```c#
 FirestorePropertyAttribute(
  string name
)
```  
Creates an instance with the specified name.

<br />

|                                                                                                                                                                                 Details                                                                                                                                                                                 ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name` | The name to use within the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) document. | |