# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md.txt

# Extensions class

The Firebase `Extensions` service interface.

**Signature:**  

    export declare class Extensions 

## Properties

|                                                      Property                                                      | Modifiers | Type | Description |
|--------------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md#extensionsapp) |           | App  |             |

## Methods

|                                                            Method                                                            | Modifiers |                                                    Description                                                     |
|------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------|
| [runtime()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md#extensionsruntime) |           | The runtime() method returns a new Runtime, which provides methods to modify an extension instance's runtime data. |

## Extensions.app

**Signature:**  

    readonly app: App;

## Extensions.runtime()

The runtime() method returns a new Runtime, which provides methods to modify an extension instance's runtime data.

This method will throw an error if called outside an Extensions environment.

**Signature:**  

    runtime(): Runtime;

**Returns:**

[Runtime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtime_class)

A new [Runtime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtime_class) object.