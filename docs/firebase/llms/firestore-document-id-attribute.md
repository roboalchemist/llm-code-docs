# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-document-id-attribute.md.txt

# Firebase.Firestore.FirestoreDocumentIdAttribute Class Reference

# Firebase.Firestore.FirestoreDocumentIdAttribute

Attribute indicating that a property should be populated with the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) document ID.

## Summary

This attribute must only be applied to properties of string or [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference). This attribute is ignored when serializing a document to [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore). This attribute must not be applied on a property which also has [FirestorePropertyAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-property-attribute#class_firebase_1_1_firestore_1_1_firestore_property_attribute).

### Inheritance

Inherits from: Attribute

| ### Constructors and Destructors ||
|---|---|
| [FirestoreDocumentIdAttribute](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firestore-document-id-attribute#class_firebase_1_1_firestore_1_1_firestore_document_id_attribute_1a26e83ee2eaf04e582b562f3420424b9c)`()` Creates an instance of the attribute. ||

## Public functions

### FirestoreDocumentIdAttribute

```c#
 FirestoreDocumentIdAttribute()
```  
Creates an instance of the attribute.