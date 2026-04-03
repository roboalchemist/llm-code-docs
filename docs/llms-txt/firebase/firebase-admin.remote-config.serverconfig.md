# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md.txt

# ServerConfig interface

Represents the configuration produced by evaluating a server template.

**Signature:**  

    export interface ServerConfig 

## Methods

|                                                                    Method                                                                    |                                                                                                                         Description                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getAll()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfiggetall)            | Returns all config values.                                                                                                                                                                                                                                   |
| [getBoolean(key)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfiggetboolean) | Gets the value for the given key as a boolean.Convenience method for calling `serverConfig.getValue(key).asBoolean()`.                                                                                                                                       |
| [getNumber(key)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfiggetnumber)   | Gets the value for the given key as a number.Convenience method for calling `serverConfig.getValue(key).asNumber()`.                                                                                                                                         |
| [getString(key)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfiggetstring)   | Gets the value for the given key as a string. Convenience method for calling `serverConfig.getValue(key).asString()`.                                                                                                                                        |
| [getValue(key)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfiggetvalue)     | Gets the [Value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#value_interface) for the given key.Ensures application logic will always have a type-safe reference, even if the parameter is removed remotely. |

## ServerConfig.getAll()

Returns all config values.

**Signature:**  

    getAll(): {
            [key: string]: Value;
        };

**Returns:**

{ \[key: string\]: [Value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#value_interface); }

A map of all config keys to their values.

## ServerConfig.getBoolean()

Gets the value for the given key as a boolean.

Convenience method for calling `serverConfig.getValue(key).asBoolean()`.

**Signature:**  

    getBoolean(key: string): boolean;

### Parameters

| Parameter |  Type  |        Description         |
|-----------|--------|----------------------------|
| key       | string | The name of the parameter. |

**Returns:**

boolean

The value for the given key as a boolean.

## ServerConfig.getNumber()

Gets the value for the given key as a number.

Convenience method for calling `serverConfig.getValue(key).asNumber()`.

**Signature:**  

    getNumber(key: string): number;

### Parameters

| Parameter |  Type  |        Description         |
|-----------|--------|----------------------------|
| key       | string | The name of the parameter. |

**Returns:**

number

The value for the given key as a number.

## ServerConfig.getString()

Gets the value for the given key as a string. Convenience method for calling `serverConfig.getValue(key).asString()`.

**Signature:**  

    getString(key: string): string;

### Parameters

| Parameter |  Type  |        Description         |
|-----------|--------|----------------------------|
| key       | string | The name of the parameter. |

**Returns:**

string

The value for the given key as a string.

## ServerConfig.getValue()

Gets the [Value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#value_interface) for the given key.

Ensures application logic will always have a type-safe reference, even if the parameter is removed remotely.

**Signature:**  

    getValue(key: string): Value;

### Parameters

| Parameter |  Type  |        Description         |
|-----------|--------|----------------------------|
| key       | string | The name of the parameter. |

**Returns:**

[Value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#value_interface)

The value for the given key.