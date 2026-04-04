# Source: https://firebase.google.com/docs/reference/js/firestore_lite.settings.md.txt

# Settings interface

Specifies custom configurations for your Cloud Firestore instance. You must set these before invoking any other methods.

**Signature:**  

    export declare interface Settings 

## Properties

|                                                                Property                                                                 |  Type   |                                                                                                                                     Description                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [host](https://firebase.google.com/docs/reference/js/firestore_lite.settings.md#settingshost)                                           | string  | The hostname to connect to.                                                                                                                                                                                                                                                          |
| [ignoreUndefinedProperties](https://firebase.google.com/docs/reference/js/firestore_lite.settings.md#settingsignoreundefinedproperties) | boolean | Whether to skip nested properties that are set to `undefined` during object serialization. If set to `true`, these properties are skipped and not written to Firestore. If set to `false` or omitted, the SDK throws an exception when it encounters properties of type `undefined`. |
| [ssl](https://firebase.google.com/docs/reference/js/firestore_lite.settings.md#settingsssl)                                             | boolean | Whether to use SSL when connecting.                                                                                                                                                                                                                                                  |

## Settings.host

The hostname to connect to.

**Signature:**  

    host?: string;

## Settings.ignoreUndefinedProperties

Whether to skip nested properties that are set to `undefined` during object serialization. If set to `true`, these properties are skipped and not written to Firestore. If set to `false` or omitted, the SDK throws an exception when it encounters properties of type `undefined`.

**Signature:**  

    ignoreUndefinedProperties?: boolean;

## Settings.ssl

Whether to use SSL when connecting.

**Signature:**  

    ssl?: boolean;