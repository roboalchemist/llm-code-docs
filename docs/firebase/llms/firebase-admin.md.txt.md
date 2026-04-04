# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.md.txt

# firebase-admin package

Firebase namespaced API (legacy).

## Functions

| Function | Description |
|---|---|
| [app(name)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#app_1eaaff4) |   |
| [appCheck(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#appcheck_8a40afc) | Gets the [AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheck_class) service for the default app or a given app.`admin.appCheck()` can be called with no arguments to access the default app's `AppCheck` service or as `admin.appCheck(app)` to access the `AppCheck` service associated with a specific app. |
| [auth(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#auth_8a40afc) | Gets the [Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#auth_class) service for the default app or a given app.`admin.auth()` can be called with no arguments to access the default app's [Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#auth_class) service or as `admin.auth(app)` to access the [Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#auth_class) service associated with a specific app. |
| [database(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#database_8a40afc) | Gets the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service for the default app or a given app.`admin.database()` can be called with no arguments to access the default app's `Database` service or as `admin.database(app)` to access the `Database` service associated with a specific app.`admin.database` is also a namespace that can be used to access global constants and methods associated with the `Database` service. |
| [firestore(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#firestore_8a40afc) |   |
| [initializeApp(options, name)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#initializeapp_279660b) |   |
| [installations(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#installations_8a40afc) | Gets the [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service for the default app or a given app.`admin.installations()` can be called with no arguments to access the default app's [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service or as `admin.installations(app)` to access the [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service associated with a specific app. |
| [instanceId(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#instanceid_8a40afc) | Gets the [InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceid_class) service for the default app or a given app.`admin.instanceId()` can be called with no arguments to access the default app's `InstanceId` service or as `admin.instanceId(app)` to access the `InstanceId` service associated with a specific app. |
| [machineLearning(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#machinelearning_8a40afc) | Gets the [MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearning_class) service for the default app or a given app.`admin.machineLearning()` can be called with no arguments to access the default app's `MachineLearning` service or as `admin.machineLearning(app)` to access the `MachineLearning` service associated with a specific app. |
| [messaging(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#messaging_8a40afc) | Gets the [Messaging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messaging_class) service for the default app or a given app.`admin.messaging()` can be called with no arguments to access the default app's `Messaging` service or as `admin.messaging(app)` to access the `Messaging` service associated with a specific app. |
| [projectManagement(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#projectmanagement_8a40afc) | Gets the [ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagement_class) service for the default app or a given app.`admin.projectManagement()` can be called with no arguments to access the default app's `ProjectManagement` service, or as `admin.projectManagement(app)` to access the `ProjectManagement` service associated with a specific app. |
| [remoteConfig(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#remoteconfig_8a40afc) | Gets the [RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfig_class) service for the default app or a given app.`admin.remoteConfig()` can be called with no arguments to access the default app's `RemoteConfig` service or as `admin.remoteConfig(app)` to access the `RemoteConfig` service associated with a specific app. |
| [securityRules(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#securityrules_8a40afc) | Gets the [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service for the default app or a given app.`admin.securityRules()` can be called with no arguments to access the default app's [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service, or as `admin.securityRules(app)` to access the [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service associated with a specific app. |
| [storage(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#storage_8a40afc) | Gets the service for the default app or a given app.`admin.storage()` can be called with no arguments to access the default app's `Storage` service or as `admin.storage(app)` to access the `Storage` service associated with a specific app. |

## Interfaces

| Interface | Description |
|---|---|
| [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.appoptions.md#appoptions_interface) | Available options to pass to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd). |
| [FirebaseArrayIndexError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firebasearrayindexerror.md#firebasearrayindexerror_interface) | Composite type which includes both a `FirebaseError` object and an index which can be used to get the errored item. |
| [FirebaseError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firebaseerror.md#firebaseerror_interface) | `FirebaseError` is a subclass of the standard JavaScript `Error` object. In addition to a message string and stack trace, it contains a string code. |
| [GoogleOAuthAccessToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.googleoauthaccesstoken.md#googleoauthaccesstoken_interface) | Interface for Google OAuth 2.0 access tokens. |
| [ServiceAccount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.serviceaccount.md#serviceaccount_interface) |   |

## Namespaces

| Namespace | Description |
|---|---|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.md#app_namespace) |   |
| [appCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.appcheck_n.md#appcheck_namespace) |   |
| [auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth_n.md#auth_namespace) |   |
| [credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.credential_n.md#credential_namespace) |   |
| [database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#database_namespace) |   |
| [firestore](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore_n.md#firestore_namespace) |   |
| [installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations_n.md#installations_namespace) |   |
| [instanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instanceid_n.md#instanceid_namespace) |   |
| [machineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machinelearning_n.md#machinelearning_namespace) |   |
| [messaging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging_n.md#messaging_namespace) |   |
| [projectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.projectmanagement_n.md#projectmanagement_namespace) |   |
| [remoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remoteconfig_n.md#remoteconfig_namespace) |   |
| [securityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.securityrules_n.md#securityrules_namespace) |   |
| [storage](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage_n.md#storage_namespace) |   |

## Variables

| Variable | Description |
|---|---|
| [apps](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#apps) |   |
| [SDK_VERSION](https://firebase.google.com/docs/reference/admin/node/firebase-admin.md#sdk_version) |   |

## app(name)

**Signature:**

    export declare function app(name?: string): app.App;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |

**Returns:**

[app.App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appapp_interface)

## appCheck(app)

Gets the [AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheck_class) service for the default app or a given app.

`admin.appCheck()` can be called with no arguments to access the default app's `AppCheck` service or as `admin.appCheck(app)` to access the `AppCheck` service associated with a specific app.

**Signature:**

    export declare function appCheck(app?: App): appCheck.AppCheck;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app for which to return the `AppCheck` service. If not provided, the default `AppCheck` service is returned. |

**Returns:**

[appCheck.AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.appcheck_n.md#appcheckappcheck)

The default `AppCheck` service if no app is provided, or the `AppCheck` service associated with the provided app.

### Example 1

    // Get the `AppCheck` service for the default app
    var defaultAppCheck = admin.appCheck();

### Example 2

    // Get the `AppCheck` service for a given app
    var otherAppCheck = admin.appCheck(otherApp);

## auth(app)

Gets the [Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#auth_class) service for the default app or a given app.

`admin.auth()` can be called with no arguments to access the default app's [Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#auth_class) service or as `admin.auth(app)` to access the [Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#auth_class) service associated with a specific app.

**Signature:**

    export declare function auth(app?: App): auth.Auth;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App |   |

**Returns:**

[auth.Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth_n.md#authauth)

### Example 1

    // Get the Auth service for the default app
    var defaultAuth = admin.auth();

### Example 2

    // Get the Auth service for a given app
    var otherAuth = admin.auth(otherApp);

## database(app)

Gets the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service for the default app or a given app.

`admin.database()` can be called with no arguments to access the default app's `Database` service or as `admin.database(app)` to access the `Database` service associated with a specific app.

`admin.database` is also a namespace that can be used to access global constants and methods associated with the `Database` service.

**Signature:**

    export declare function database(app?: App): database.Database;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App |   |

**Returns:**

[database.Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasedatabase)

The default `Database` service if no app is provided or the `Database` service associated with the provided app.

### Example 1

    // Get the Database service for the default app
    var defaultDatabase = admin.database();

### Example 2

    // Get the Database service for a specific app
    var otherDatabase = admin.database(app);

## firestore(app)

**Signature:**

    export declare function firestore(app?: App): _firestore.Firestore;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App |   |

**Returns:**

_firestore.Firestore

## initializeApp(options, name)

**Signature:**

    export declare function initializeApp(options?: AppOptions, name?: string): app.App;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.appoptions.md#appoptions_interface) |   |
| name | string |   |

**Returns:**

[app.App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appapp_interface)

## installations(app)

Gets the [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service for the default app or a given app.

`admin.installations()` can be called with no arguments to access the default app's [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service or as `admin.installations(app)` to access the [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) service associated with a specific app.

**Signature:**

    export declare function installations(app?: App): installations.Installations;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app whose `Installations` service to return. If not provided, the default `Installations` service is returned. |

**Returns:**

[installations.Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations_n.md#installationsinstallations)

The default `Installations` service if no app is provided or the `Installations` service associated with the provided app.

### Example 1

    // Get the Installations service for the default app
    var defaultInstallations = admin.installations();

### Example 2

    // Get the Installations service for a given app
    var otherInstallations = admin.installations(otherApp);

## instanceId(app)

Gets the [InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceid_class) service for the default app or a given app.

`admin.instanceId()` can be called with no arguments to access the default app's `InstanceId` service or as `admin.instanceId(app)` to access the `InstanceId` service associated with a specific app.

**Signature:**

    export declare function instanceId(app?: App): instanceId.InstanceId;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app whose `InstanceId` service to return. If not provided, the default `InstanceId` service will be returned. |

**Returns:**

[instanceId.InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instanceid_n.md#instanceidinstanceid)

The default `InstanceId` service if no app is provided or the `InstanceId` service associated with the provided app.

### Example 1

    // Get the Instance ID service for the default app
    var defaultInstanceId = admin.instanceId();

### Example 2

    // Get the Instance ID service for a given app
    var otherInstanceId = admin.instanceId(otherApp);

## machineLearning(app)

Gets the [MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearning_class) service for the default app or a given app.

`admin.machineLearning()` can be called with no arguments to access the default app's `MachineLearning` service or as `admin.machineLearning(app)` to access the `MachineLearning` service associated with a specific app.

**Signature:**

    export declare function machineLearning(app?: App): machineLearning.MachineLearning;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app whose `MachineLearning` service to return. If not provided, the default `MachineLearning` service will be returned. |

**Returns:**

[machineLearning.MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machinelearning_n.md#machinelearningmachinelearning)

The default `MachineLearning` service if no app is provided or the `MachineLearning` service associated with the provided app.

### Example 1

    // Get the MachineLearning service for the default app
    var defaultMachineLearning = admin.machineLearning();

### Example 2

    // Get the MachineLearning service for a given app
    var otherMachineLearning = admin.machineLearning(otherApp);

## messaging(app)

Gets the [Messaging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messaging_class) service for the default app or a given app.

`admin.messaging()` can be called with no arguments to access the default app's `Messaging` service or as `admin.messaging(app)` to access the `Messaging` service associated with a specific app.

**Signature:**

    export declare function messaging(app?: App): messaging.Messaging;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app whose `Messaging` service to return. If not provided, the default `Messaging` service will be returned. |

**Returns:**

[messaging.Messaging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging_n.md#messagingmessaging)

The default `Messaging` service if no app is provided or the `Messaging` service associated with the provided app.

### Example 1

    // Get the Messaging service for the default app
    var defaultMessaging = admin.messaging();

### Example 2

    // Get the Messaging service for a given app
    var otherMessaging = admin.messaging(otherApp);

## projectManagement(app)

Gets the [ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagement_class) service for the default app or a given app.

`admin.projectManagement()` can be called with no arguments to access the default app's `ProjectManagement` service, or as `admin.projectManagement(app)` to access the `ProjectManagement` service associated with a specific app.

**Signature:**

    export declare function projectManagement(app?: App): projectManagement.ProjectManagement;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app whose `ProjectManagement` service to return. If not provided, the default `ProjectManagement` service will be returned. \* |

**Returns:**

[projectManagement.ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.projectmanagement_n.md#projectmanagementprojectmanagement)

The default `ProjectManagement` service if no app is provided or the `ProjectManagement` service associated with the provided app.

### Example 1

    // Get the ProjectManagement service for the default app
    var defaultProjectManagement = admin.projectManagement();

### Example 2

    // Get the ProjectManagement service for a given app
    var otherProjectManagement = admin.projectManagement(otherApp);

## remoteConfig(app)

Gets the [RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfig_class) service for the default app or a given app.

`admin.remoteConfig()` can be called with no arguments to access the default app's `RemoteConfig` service or as `admin.remoteConfig(app)` to access the `RemoteConfig` service associated with a specific app.

**Signature:**

    export declare function remoteConfig(app?: App): remoteConfig.RemoteConfig;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app for which to return the `RemoteConfig` service. If not provided, the default `RemoteConfig` service is returned. |

**Returns:**

[remoteConfig.RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remoteconfig_n.md#remoteconfigremoteconfig)

The default `RemoteConfig` service if no app is provided, or the `RemoteConfig` service associated with the provided app.

### Example 1

    // Get the `RemoteConfig` service for the default app
    var defaultRemoteConfig = admin.remoteConfig();

### Example 2

    // Get the `RemoteConfig` service for a given app
    var otherRemoteConfig = admin.remoteConfig(otherApp);

## securityRules(app)

Gets the [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service for the default app or a given app.

`admin.securityRules()` can be called with no arguments to access the default app's [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service, or as `admin.securityRules(app)` to access the [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service associated with a specific app.

**Signature:**

    export declare function securityRules(app?: App): securityRules.SecurityRules;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App | Optional app to return the `SecurityRules` service for. If not provided, the default `SecurityRules` service is returned. |

**Returns:**

[securityRules.SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.securityrules_n.md#securityrulessecurityrules)

The default `SecurityRules` service if no app is provided, or the `SecurityRules` service associated with the provided app.

### Example 1

    // Get the SecurityRules service for the default app
    var defaultSecurityRules = admin.securityRules();

### Example 2

    // Get the SecurityRules service for a given app
    var otherSecurityRules = admin.securityRules(otherApp);

## storage(app)

Gets the service for the default app or a given app.

`admin.storage()` can be called with no arguments to access the default app's `Storage` service or as `admin.storage(app)` to access the `Storage` service associated with a specific app.

**Signature:**

    export declare function storage(app?: App): storage.Storage;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | App |   |

**Returns:**

[storage.Storage](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage_n.md#storagestorage)

### Example 1

    // Get the Storage service for the default app
    var defaultStorage = admin.storage();

### Example 2

    // Get the Storage service for a given app
    var otherStorage = admin.storage(otherApp);

## apps

**Signature:**

    apps: (app.App | null)[]

## SDK_VERSION

**Signature:**

    SDK_VERSION: string