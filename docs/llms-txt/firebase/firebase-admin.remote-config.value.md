# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md.txt

# Value interface

Wraps a parameter value with metadata and type-safe getters.

Type-safe getters insulate application logic from remote changes to parameter names and types.

**Signature:**  

    export interface Value 

## Methods

|                                                          Method                                                           |                                                                               Description                                                                               |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [asBoolean()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#valueasboolean) | Gets the value as a boolean.The following values (case insensitive) are interpreted as true: "1", "true", "t", "yes", "y", "on". Other values are interpreted as false. |
| [asNumber()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#valueasnumber)   | Gets the value as a number. Comparable to calling `Number(value) || 0`.                                                                                                 |
| [asString()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#valueasstring)   | Gets the value as a string.                                                                                                                                             |
| [getSource()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#valuegetsource) | Gets the [ValueSource](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#valuesource) for the given key.                            |

## Value.asBoolean()

Gets the value as a boolean.

The following values (case insensitive) are interpreted as true: "1", "true", "t", "yes", "y", "on". Other values are interpreted as false.

**Signature:**  

    asBoolean(): boolean;

**Returns:**

boolean

## Value.asNumber()

Gets the value as a number. Comparable to calling `Number(value) || 0`.

**Signature:**  

    asNumber(): number;

**Returns:**

number

## Value.asString()

Gets the value as a string.

**Signature:**  

    asString(): string;

**Returns:**

string

## Value.getSource()

Gets the [ValueSource](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#valuesource) for the given key.

**Signature:**  

    getSource(): ValueSource;

**Returns:**

[ValueSource](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#valuesource)