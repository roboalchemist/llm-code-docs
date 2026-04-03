# Source: https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md.txt

# FieldValue class

Sentinel values that can be used when writing document fields with `set()` or `update()`.

**Signature:**  

    export declare abstract class FieldValue 

## Methods

|                                                   Method                                                   | Modifiers |             Description              |
|------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------|
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalueisequal) |           | Compares `FieldValue`s for equality. |

## FieldValue.isEqual()

Compares `FieldValue`s for equality.

**Signature:**  

    abstract isEqual(other: FieldValue): boolean;

#### Parameters

| Parameter |                                                 Type                                                  | Description |
|-----------|-------------------------------------------------------------------------------------------------------|-------------|
| other     | [FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class) |             |

**Returns:**

boolean