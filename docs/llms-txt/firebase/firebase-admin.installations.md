# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.md.txt

# firebase-admin.installations package

Firebase Instance ID service.

## Functions

|                                                                Function                                                                 |                                                                                                                                                                                                Description                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getInstallations(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.md#getinstallations_8a40afc) | Gets the [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service for the default app or a given app.`getInstallations()` can be called with no arguments to access the default app's `Installations` service or as `getInstallations(app)` to access the `Installations` service associated with a specific app. |

## Classes

|                                                                                         Class                                                                                         |                                    Description                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [FirebaseInstallationsError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.firebaseinstallationserror.md#firebaseinstallationserror_class)       | Firebase Installations service error code structure. This extends `FirebaseError`. |
| [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class)                                              | The `Installations` service for the current app.                                   |
| [InstallationsClientErrorCode](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installationsclienterrorcode.md#installationsclienterrorcode_class) |                                                                                    |

## getInstallations(app)

Gets the [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service for the default app or a given app.

`getInstallations()` can be called with no arguments to access the default app's `Installations` service or as `getInstallations(app)` to access the `Installations` service associated with a specific app.

**Signature:**  

    export declare function getInstallations(app?: App): Installations;

### Parameters

| Parameter | Type |                                                         Description                                                          |
|-----------|------|------------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app whose `Installations` service to return. If not provided, the default `Installations` service will be returned. |

**Returns:**

[Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class)

The default `Installations` service if no app is provided or the `Installations` service associated with the provided app.

### Example 1

    // Get the Installations service for the default app
    const defaultInstallations = getInstallations();

### Example 2

    // Get the Installations service for a given app
    const otherInstallations = getInstallations(otherApp);