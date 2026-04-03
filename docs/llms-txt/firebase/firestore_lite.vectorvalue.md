# Source: https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md.txt

# VectorValue class

Represents a vector type in Firestore documents. Create an instance with [vector()](https://firebase.google.com/docs/reference/js/firestore_.md#vector_0dbdaf2).

VectorValue

**Signature:**  

    export declare class VectorValue 

## Methods

|                                                      Method                                                       | Modifiers |                                                                                   Description                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvaluefromjson) | `static`  | Builds a `VectorValue` instance from a JSON object created by [VectorValue.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvaluetojson). |
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvalueisequal)  |           | Returns `true` if the two `VectorValue` values have the same raw number arrays, returns `false` otherwise.                                                                       |
| [toArray()](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvaluetoarray)       |           | Returns a copy of the raw number array form of the vector.                                                                                                                       |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvaluetojson)         |           | Returns a JSON-serializable representation of this `VectorValue` instance.                                                                                                       |

## VectorValue.fromJSON()

Builds a `VectorValue` instance from a JSON object created by [VectorValue.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvaluetojson).

**Signature:**  

    static fromJSON(json: object): VectorValue;

#### Parameters

| Parameter |  Type  |                       Description                       |
|-----------|--------|---------------------------------------------------------|
| json      | object | a JSON object represention of a `VectorValue` instance. |

**Returns:**

[VectorValue](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvalue_class)

an instance of [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

## VectorValue.isEqual()

Returns `true` if the two `VectorValue` values have the same raw number arrays, returns `false` otherwise.

**Signature:**  

    isEqual(other: VectorValue): boolean;

#### Parameters

| Parameter |                                                     Type                                                     | Description |
|-----------|--------------------------------------------------------------------------------------------------------------|-------------|
| other     | [VectorValue](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvalue_class) |             |

**Returns:**

boolean

## VectorValue.toArray()

Returns a copy of the raw number array form of the vector.

**Signature:**  

    toArray(): number[];

**Returns:**

number\[\]

## VectorValue.toJSON()

Returns a JSON-serializable representation of this `VectorValue` instance.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON representation of this object.