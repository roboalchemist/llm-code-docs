# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-data-attribute.md.txt

# Firebase.Firestore.FirestoreDataAttribute Class Reference

# Firebase.Firestore.FirestoreDataAttribute

Attribute indicating that a type is intended to be used with [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore).

## Summary

### Inheritance

Inherits from: Attribute

| ### Constructors and Destructors ||
|---|---|
| [FirestoreDataAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-data-attribute#class_firebase_1_1_firestore_1_1_firestore_data_attribute_1a301302b8726c7d6085243700e7de873e)`()` Constructs a new instance with default values for options. ||
| [FirestoreDataAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-data-attribute#class_firebase_1_1_firestore_1_1_firestore_data_attribute_1a91e0922afbd78f16a14d5c5049eda7ec)`(`[UnknownPropertyHandling](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a894811830fc00e909a8f0df0fa560e25)` unknownPropertyHandling)` Constructs a new instance with the given handling for unknown properties. ||

|                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                         ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ConverterType](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-data-attribute#class_firebase_1_1_firestore_1_1_firestore_data_attribute_1a5dfb4f90735b93918cbff9590af20904)           | `System.Type` A custom converter type to use for serializing and deserializing the attributed type.                                                                                                                                |
| [UnknownPropertyHandling](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-data-attribute#class_firebase_1_1_firestore_1_1_firestore_data_attribute_1a77536a9697dedcfc671762e492e54654) | [UnknownPropertyHandling](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a894811830fc00e909a8f0df0fa560e25) The strategy to use when handling unknown properties. |

## Properties

### ConverterType

```c#
System.Type ConverterType
```  
A custom converter type to use for serializing and deserializing the attributed type.  

### UnknownPropertyHandling

```c#
UnknownPropertyHandling UnknownPropertyHandling
```  
The strategy to use when handling unknown properties.

The default is UnknownPropertyHandling.Warn.

## Public functions

### FirestoreDataAttribute

```c#
 FirestoreDataAttribute()
```  
Constructs a new instance with default values for options.  

### FirestoreDataAttribute

```c#
 FirestoreDataAttribute(
  UnknownPropertyHandling unknownPropertyHandling
)
```  
Constructs a new instance with the given handling for unknown properties.

<br />

|                                                                                  Details                                                                                  ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------------|------------------------------------------------| | `unknownPropertyHandling` | The unknown property handling strategy to use. | |