# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/installations.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/installations/installations.md.txt

# Source: https://firebase.google.com/docs/reference/js/installations.md.txt

# installations package

The Firebase Installations Web SDK. This SDK does not work in a Node.js environment.

## Functions

|                                                             Function                                                             |                                                                                                                                      Description                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                           |                                                                                                                                                                                                                                                                                        |
| [getInstallations(app)](https://firebase.google.com/docs/reference/js/installations.md#getinstallations_cf608e1)                 | Returns an instance of [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance. |
| **function(installations, ...)**                                                                                                 |                                                                                                                                                                                                                                                                                        |
| [deleteInstallations(installations)](https://firebase.google.com/docs/reference/js/installations.md#deleteinstallations_606c567) | Deletes the Firebase Installation and all associated data.                                                                                                                                                                                                                             |
| [getId(installations)](https://firebase.google.com/docs/reference/js/installations.md#getid_606c567)                             | Creates a Firebase Installation if there isn't one for the app and returns the Installation ID.                                                                                                                                                                                        |
| [getToken(installations, forceRefresh)](https://firebase.google.com/docs/reference/js/installations.md#gettoken_cf009a7)         | Returns a Firebase Installations auth token, identifying the current Firebase Installation.                                                                                                                                                                                            |
| [onIdChange(installations, callback)](https://firebase.google.com/docs/reference/js/installations.md#onidchange_b579e0e)         | Sets a new callback that will get called when Installation ID changes. Returns an unsubscribe function that will remove the callback when called.                                                                                                                                      |

## Interfaces

|                                                       Interface                                                       |                     Description                     |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) | Public interface of the Firebase Installations SDK. |

## Type Aliases

|                                                  Type Alias                                                   |                                                                          Description                                                                          |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IdChangeCallbackFn](https://firebase.google.com/docs/reference/js/installations.md#idchangecallbackfn)       | An user defined callback function that gets called when Installations ID changes.                                                                             |
| [IdChangeUnsubscribeFn](https://firebase.google.com/docs/reference/js/installations.md#idchangeunsubscribefn) | Unsubscribe a callback function previously added via [IdChangeCallbackFn](https://firebase.google.com/docs/reference/js/installations.md#idchangecallbackfn). |

## function(app, ...)

### getInstallations(app)

Returns an instance of [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance.

**Signature:**  

    export declare function getInstallations(app?: FirebaseApp): Installations;

#### Parameters

| Parameter |                                                 Type                                                  |                                                     Description                                                     |
|-----------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance. |

**Returns:**

[Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface)

## function(installations, ...)

### deleteInstallations(installations)

Deletes the Firebase Installation and all associated data.

**Signature:**  

    export declare function deleteInstallations(installations: Installations): Promise<void>;

#### Parameters

|   Parameter   |                                                         Type                                                          |          Description          |
|---------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------|
| installations | [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) | The `Installations` instance. |

**Returns:**

Promise\<void\>

### getId(installations)

Creates a Firebase Installation if there isn't one for the app and returns the Installation ID.

**Signature:**  

    export declare function getId(installations: Installations): Promise<string>;

#### Parameters

|   Parameter   |                                                         Type                                                          |          Description          |
|---------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------|
| installations | [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) | The `Installations` instance. |

**Returns:**

Promise\<string\>

### getToken(installations, forceRefresh)

Returns a Firebase Installations auth token, identifying the current Firebase Installation.

**Signature:**  

    export declare function getToken(installations: Installations, forceRefresh?: boolean): Promise<string>;

#### Parameters

|   Parameter   |                                                         Type                                                          |                  Description                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| installations | [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) | The `Installations` instance.                 |
| forceRefresh  | boolean                                                                                                               | Force refresh regardless of token expiration. |

**Returns:**

Promise\<string\>

### onIdChange(installations, callback)

Sets a new callback that will get called when Installation ID changes. Returns an unsubscribe function that will remove the callback when called.

**Signature:**  

    export declare function onIdChange(installations: Installations, callback: IdChangeCallbackFn): IdChangeUnsubscribeFn;

#### Parameters

|   Parameter   |                                                         Type                                                          |                       Description                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| installations | [Installations](https://firebase.google.com/docs/reference/js/installations.installations.md#installations_interface) | The `Installations` instance.                           |
| callback      | [IdChangeCallbackFn](https://firebase.google.com/docs/reference/js/installations.md#idchangecallbackfn)               | The callback function that is invoked when FID changes. |

**Returns:**

[IdChangeUnsubscribeFn](https://firebase.google.com/docs/reference/js/installations.md#idchangeunsubscribefn)

A function that can be called to unsubscribe.

## IdChangeCallbackFn

An user defined callback function that gets called when Installations ID changes.

**Signature:**  

    export type IdChangeCallbackFn = (installationId: string) => void;

## IdChangeUnsubscribeFn

Unsubscribe a callback function previously added via [IdChangeCallbackFn](https://firebase.google.com/docs/reference/js/installations.md#idchangecallbackfn).

**Signature:**  

    export type IdChangeUnsubscribeFn = () => void;