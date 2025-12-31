# Source: https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md.txt

# FieldPath class

A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top-level field in the document), or a list of field names (referring to a nested field in the document).

Create a `FieldPath` by providing field names. If more than one field name is provided, the path will point to a nested field in a document.

**Signature:**  

    export declare class FieldPath 

## Constructors

|                                                         Constructor                                                         | Modifiers |                                                                    Description                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [(constructor)(fieldNames)](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpathconstructor) |           | Creates a `FieldPath` from the provided field names. If more than one field name is provided, the path will point to a nested field in a document. |

## Methods

|                                                    Method                                                    | Modifiers |                          Description                           |
|--------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------|
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpathisequal) |           | Returns true if this `FieldPath` is equal to the provided one. |

## FieldPath.(constructor)

Creates a `FieldPath` from the provided field names. If more than one field name is provided, the path will point to a nested field in a document.

**Signature:**  

    constructor(...fieldNames: string[]);

#### Parameters

| Parameter  |    Type    |      Description       |
|------------|------------|------------------------|
| fieldNames | string\[\] | A list of field names. |

## FieldPath.isEqual()

Returns true if this `FieldPath` is equal to the provided one.

**Signature:**  

    isEqual(other: FieldPath): boolean;

#### Parameters

| Parameter |                                                  Type                                                  |             Description             |
|-----------|--------------------------------------------------------------------------------------------------------|-------------------------------------|
| other     | [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class) | The `FieldPath` to compare against. |

**Returns:**

boolean

true if this `FieldPath` is equal to the provided one.