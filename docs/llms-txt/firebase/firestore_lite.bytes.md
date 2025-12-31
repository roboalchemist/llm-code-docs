# Source: https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md.txt

# Bytes class

An immutable object representing an array of bytes.

**Signature:**  

    export declare class Bytes 

## Methods

|                                                         Method                                                          | Modifiers |                                                                       Description                                                                        |
|-------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromBase64String(base64)](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytesfrombase64string) | `static`  | Creates a new `Bytes` object from the given Base64 string, converting it to bytes.                                                                       |
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytesfromjson)                   | `static`  | Builds a `Bytes` instance from a JSON object created by [Bytes.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytestojson). |
| [fromUint8Array(array)](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytesfromuint8array)      | `static`  | Creates a new `Bytes` object from the given Uint8Array.                                                                                                  |
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytesisequal)                    |           | Returns true if this `Bytes` object is equal to the provided one.                                                                                        |
| [toBase64()](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytestobase64)                       |           | Returns the underlying bytes as a Base64-encoded string.                                                                                                 |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytestojson)                           |           | Returns a JSON-serializable representation of this `Bytes` instance.                                                                                     |
| [toString()](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytestostring)                       |           | Returns a string representation of the `Bytes` object.                                                                                                   |
| [toUint8Array()](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytestouint8array)               |           | Returns the underlying bytes in a new `Uint8Array`.                                                                                                      |

## Bytes.fromBase64String()

Creates a new `Bytes` object from the given Base64 string, converting it to bytes.

**Signature:**  

    static fromBase64String(base64: string): Bytes;

#### Parameters

| Parameter |  Type  |                     Description                      |
|-----------|--------|------------------------------------------------------|
| base64    | string | The Base64 string used to create the `Bytes` object. |

**Returns:**

[Bytes](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytes_class)

## Bytes.fromJSON()

Builds a `Bytes` instance from a JSON object created by [Bytes.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytestojson).

**Signature:**  

    static fromJSON(json: object): Bytes;

#### Parameters

| Parameter |  Type  |                   Description                    |
|-----------|--------|--------------------------------------------------|
| json      | object | a JSON object represention of a `Bytes` instance |

**Returns:**

[Bytes](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytes_class)

an instance of [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

## Bytes.fromUint8Array()

Creates a new `Bytes` object from the given Uint8Array.

**Signature:**  

    static fromUint8Array(array: Uint8Array): Bytes;

#### Parameters

| Parameter |    Type    |                    Description                    |
|-----------|------------|---------------------------------------------------|
| array     | Uint8Array | The Uint8Array used to create the `Bytes` object. |

**Returns:**

[Bytes](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytes_class)

## Bytes.isEqual()

Returns true if this `Bytes` object is equal to the provided one.

**Signature:**  

    isEqual(other: Bytes): boolean;

#### Parameters

| Parameter |                                            Type                                            |              Description               |
|-----------|--------------------------------------------------------------------------------------------|----------------------------------------|
| other     | [Bytes](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytes_class) | The `Bytes` object to compare against. |

**Returns:**

boolean

true if this `Bytes` object is equal to the provided one.

## Bytes.toBase64()

Returns the underlying bytes as a Base64-encoded string.

**Signature:**  

    toBase64(): string;

**Returns:**

string

The Base64-encoded string created from the `Bytes` object.

## Bytes.toJSON()

Returns a JSON-serializable representation of this `Bytes` instance.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON representation of this object.

## Bytes.toString()

Returns a string representation of the `Bytes` object.

**Signature:**  

    toString(): string;

**Returns:**

string

A string representation of the `Bytes` object.

## Bytes.toUint8Array()

Returns the underlying bytes in a new `Uint8Array`.

**Signature:**  

    toUint8Array(): Uint8Array;

**Returns:**

Uint8Array

The Uint8Array created from the `Bytes` object.