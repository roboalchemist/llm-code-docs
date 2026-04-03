# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md.txt

# firebase-admin.project-management package

Firebase project management.

## Functions

|                                                                       Function                                                                       |                                                                                                                                                                                                                 Description                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getProjectManagement(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md#getprojectmanagement_8a40afc) | Gets the [ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagement_class) service for the default app or a given app.`getProjectManagement()` can be called with no arguments to access the default app's `ProjectManagement` service, or as `getProjectManagement(app)` to access the `ProjectManagement` service associated with a specific app. |

## Classes

|                                                                                              Class                                                                                               |                                                                                                                              Description                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndroidApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidapp_class)                                                             | A reference to a Firebase Android app.Do not call this constructor directly. Instead, use [ProjectManagement.androidApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementandroidapp). |
| [FirebaseProjectManagementError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.firebaseprojectmanagementerror.md#firebaseprojectmanagementerror_class) | Firebase project management error code structure. This extends PrefixedFirebaseError.                                                                                                                                                                                 |
| [IosApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosapp_class)                                                                         | A reference to a Firebase iOS app.Do not call this constructor directly. Instead, use [ProjectManagement.iosApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementiosapp).             |
| [ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagement_class)                                        | The Firebase ProjectManagement service interface.                                                                                                                                                                                                                     |
| [ShaCertificate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificate_class)                                                 | A SHA-1 or SHA-256 certificate.Do not call this constructor directly. Instead, use \[`projectManagement.shaCertificate()`\](projectManagement.ProjectManagement#shaCertificate).                                                                                      |

## Enumerations

|                                                      Enumeration                                                      |                      Description                       |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [AppPlatform](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md#appplatform) | Platforms with which a Firebase App can be associated. |

## Interfaces

|                                                                            Interface                                                                             |              Description               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidappmetadata.md#androidappmetadata_interface) | Metadata about a Firebase Android App. |
| [AppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadata_interface)                      | Metadata about a Firebase app.         |
| [IosAppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosappmetadata.md#iosappmetadata_interface)             | Metadata about a Firebase iOS App.     |

## Type Aliases

|                                                                     Type Alias                                                                      | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [ProjectManagementErrorCode](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md#projectmanagementerrorcode) |             |

## getProjectManagement(app)

Gets the [ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagement_class) service for the default app or a given app.

`getProjectManagement()` can be called with no arguments to access the default app's `ProjectManagement` service, or as `getProjectManagement(app)` to access the `ProjectManagement` service associated with a specific app.

**Signature:**  

    export declare function getProjectManagement(app?: App): ProjectManagement;

### Parameters

| Parameter | Type |                                                               Description                                                               |
|-----------|------|-----------------------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app whose `ProjectManagement` service to return. If not provided, the default `ProjectManagement` service will be returned. \* |

**Returns:**

[ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagement_class)

The default `ProjectManagement` service if no app is provided or the `ProjectManagement` service associated with the provided app.

### Example 1

    // Get the ProjectManagement service for the default app
    const defaultProjectManagement = getProjectManagement();

### Example 2

    // Get the ProjectManagement service for a given app
    const otherProjectManagement = getProjectManagement(otherApp);

## ProjectManagementErrorCode

**Signature:**  

    export type ProjectManagementErrorCode = 'already-exists' | 'authentication-error' | 'internal-error' | 'invalid-argument' | 'invalid-project-id' | 'invalid-server-response' | 'not-found' | 'service-unavailable' | 'unknown-error';

## AppPlatform

Platforms with which a Firebase App can be associated.

**Signature:**  

    export declare enum AppPlatform 

## Enumeration Members

|      Member      |        Value         |                            Description                            |
|------------------|----------------------|-------------------------------------------------------------------|
| ANDROID          | `"ANDROID"`          | The Firebase App is associated with Android.                      |
| IOS              | `"IOS"`              | The Firebase App is associated with iOS.                          |
| PLATFORM_UNKNOWN | `"PLATFORM_UNKNOWN"` | Unknown state. This is only used for distinguishing unset values. |