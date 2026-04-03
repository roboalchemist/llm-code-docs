# Source: https://firebase.google.com/docs/reference/js/auth.auth.md.txt

# Auth interface

Interface representing Firebase Auth service.

See [Firebase Authentication](https://firebase.google.com/docs/auth/) for a full guide on how to use the Firebase Auth service.

**Signature:**  

    export interface Auth 

## Properties

|                                            Property                                             |                                                          Type                                                           |                                                                      Description                                                                       |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/auth.auth.md#authapp)                       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)                   | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with the `Auth` service instance. |
| [config](https://firebase.google.com/docs/reference/js/auth.auth.md#authconfig)                 | [Config](https://firebase.google.com/docs/reference/js/auth.config.md#config_interface)                                 | The [Config](https://firebase.google.com/docs/reference/js/auth.config.md#config_interface) used to initialize this instance.                          |
| [currentUser](https://firebase.google.com/docs/reference/js/auth.auth.md#authcurrentuser)       | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) \| null                               | The currently signed-in user (or null).                                                                                                                |
| [emulatorConfig](https://firebase.google.com/docs/reference/js/auth.auth.md#authemulatorconfig) | [EmulatorConfig](https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md#emulatorconfig_interface) \| null | The current emulator configuration (or null).                                                                                                          |
| [languageCode](https://firebase.google.com/docs/reference/js/auth.auth.md#authlanguagecode)     | string \| null                                                                                                          | The [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's language code.                                        |
| [name](https://firebase.google.com/docs/reference/js/auth.auth.md#authname)                     | string                                                                                                                  | The name of the app associated with the `Auth` service instance.                                                                                       |
| [settings](https://firebase.google.com/docs/reference/js/auth.auth.md#authsettings)             | [AuthSettings](https://firebase.google.com/docs/reference/js/auth.authsettings.md#authsettings_interface)               | The [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's settings.                                             |
| [tenantId](https://firebase.google.com/docs/reference/js/auth.auth.md#authtenantid)             | string \| null                                                                                                          | The [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's tenant ID.                                            |

## Methods

|                                                                  Method                                                                   |                                                                                                                Description                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [authStateReady()](https://firebase.google.com/docs/reference/js/auth.auth.md#authauthstateready)                                         | returns a promise that resolves immediately when the initial auth state is settled. When the promise resolves, the current user might be a valid user or `null` if the user signed out.                                                    |
| [beforeAuthStateChanged(callback, onAbort)](https://firebase.google.com/docs/reference/js/auth.auth.md#authbeforeauthstatechanged)        | Adds a blocking callback that runs before an auth state change sets a new user.                                                                                                                                                            |
| [onAuthStateChanged(nextOrObserver, error, completed)](https://firebase.google.com/docs/reference/js/auth.auth.md#authonauthstatechanged) | Adds an observer for changes to the user's sign-in state.                                                                                                                                                                                  |
| [onIdTokenChanged(nextOrObserver, error, completed)](https://firebase.google.com/docs/reference/js/auth.auth.md#authonidtokenchanged)     | Adds an observer for changes to the signed-in user's ID token.                                                                                                                                                                             |
| [setPersistence(persistence)](https://firebase.google.com/docs/reference/js/auth.auth.md#authsetpersistence)                              | Changes the type of persistence on the `Auth` instance.                                                                                                                                                                                    |
| [signOut()](https://firebase.google.com/docs/reference/js/auth.auth.md#authsignout)                                                       | Signs out the current user. This does not automatically revoke the user's ID token.                                                                                                                                                        |
| [updateCurrentUser(user)](https://firebase.google.com/docs/reference/js/auth.auth.md#authupdatecurrentuser)                               | Asynchronously sets the provided user as [Auth.currentUser](https://firebase.google.com/docs/reference/js/auth.auth.md#authcurrentuser) on the [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance. |
| [useDeviceLanguage()](https://firebase.google.com/docs/reference/js/auth.auth.md#authusedevicelanguage)                                   | Sets the current language to the default device/browser preference.                                                                                                                                                                        |

## Auth.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with the `Auth` service instance.

**Signature:**  

    readonly app: FirebaseApp;

## Auth.config

The [Config](https://firebase.google.com/docs/reference/js/auth.config.md#config_interface) used to initialize this instance.

**Signature:**  

    readonly config: Config;

## Auth.currentUser

The currently signed-in user (or null).

**Signature:**  

    readonly currentUser: User | null;

## Auth.emulatorConfig

The current emulator configuration (or null).

**Signature:**  

    readonly emulatorConfig: EmulatorConfig | null;

## Auth.languageCode

The [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's language code.

This is a readable/writable property. When set to null, the default Firebase Console language setting is applied. The language code will propagate to email action templates (password reset, email verification and email change revocation), SMS templates for phone authentication, reCAPTCHA verifier and OAuth popup/redirect operations provided the specified providers support localization with the language code specified.

**Signature:**  

    languageCode: string | null;

## Auth.name

The name of the app associated with the `Auth` service instance.

**Signature:**  

    readonly name: string;

## Auth.settings

The [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's settings.

This is used to edit/read configuration related options such as app verification mode for phone authentication.

**Signature:**  

    readonly settings: AuthSettings;

## Auth.tenantId

The [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's tenant ID.

This is a readable/writable property. When you set the tenant ID of an [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance, all future sign-in/sign-up operations will pass this tenant ID and sign in or sign up users to the specified tenant project. When set to null, users are signed in to the parent project.

**Signature:**  

    tenantId: string | null;

### Example

    // Set the tenant ID on Auth instance.
    auth.tenantId = 'TENANT_PROJECT_ID';

    // All future sign-in request now include tenant ID.
    const result = await signInWithEmailAndPassword(auth, email, password);
    // result.user.tenantId should be 'TENANT_PROJECT_ID'.

## Auth.authStateReady()

returns a promise that resolves immediately when the initial auth state is settled. When the promise resolves, the current user might be a valid user or `null` if the user signed out.

**Signature:**  

    authStateReady(): Promise<void>;

**Returns:**

Promise\<void\>

## Auth.beforeAuthStateChanged()

Adds a blocking callback that runs before an auth state change sets a new user.

**Signature:**  

    beforeAuthStateChanged(callback: (user: User | null) => void | Promise<void>, onAbort?: () => void): Unsubscribe;

#### Parameters

| Parameter |                                                             Type                                                              |                                                   Description                                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| callback  | (user: [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) \| null) =\> void \| Promise\<void\> | callback triggered before new user value is set. If this throws, it blocks the user from being set.              |
| onAbort   | () =\> void                                                                                                                   | callback triggered if a later `beforeAuthStateChanged()` callback throws, allowing you to undo any side effects. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

## Auth.onAuthStateChanged()

Adds an observer for changes to the user's sign-in state.

To keep the old behavior, see [Auth.onIdTokenChanged()](https://firebase.google.com/docs/reference/js/auth.auth.md#authonidtokenchanged).

**Signature:**  

    onAuthStateChanged(nextOrObserver: NextOrObserver<User | null>, error?: ErrorFn, completed?: CompleteFn): Unsubscribe;

#### Parameters

|   Parameter    |                                                                                        Type                                                                                         |                                                                Description                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| nextOrObserver | [NextOrObserver](https://firebase.google.com/docs/reference/js/auth.md#nextorobserver)\<[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) \| null\> | callback triggered on change.                                                                                                              |
| error          | [ErrorFn](https://firebase.google.com/docs/reference/js/util.md#errorfn)                                                                                                            | Deprecated. This callback is never triggered. Errors on signing in/out can be caught in promises returned from sign-in/sign-out functions. |
| completed      | [CompleteFn](https://firebase.google.com/docs/reference/js/util.md#completefn)                                                                                                      | Deprecated. This callback is never triggered.                                                                                              |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

## Auth.onIdTokenChanged()

Adds an observer for changes to the signed-in user's ID token.

This includes sign-in, sign-out, and token refresh events.

**Signature:**  

    onIdTokenChanged(nextOrObserver: NextOrObserver<User | null>, error?: ErrorFn, completed?: CompleteFn): Unsubscribe;

#### Parameters

|   Parameter    |                                                                                        Type                                                                                         |                                                                Description                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| nextOrObserver | [NextOrObserver](https://firebase.google.com/docs/reference/js/auth.md#nextorobserver)\<[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) \| null\> | callback triggered on change.                                                                                                              |
| error          | [ErrorFn](https://firebase.google.com/docs/reference/js/util.md#errorfn)                                                                                                            | Deprecated. This callback is never triggered. Errors on signing in/out can be caught in promises returned from sign-in/sign-out functions. |
| completed      | [CompleteFn](https://firebase.google.com/docs/reference/js/util.md#completefn)                                                                                                      | Deprecated. This callback is never triggered.                                                                                              |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

## Auth.setPersistence()

Changes the type of persistence on the `Auth` instance.

This will affect the currently saved Auth session and applies this type of persistence for future sign-in requests, including sign-in with redirect requests.

This makes it easy for a user signing in to specify whether their session should be remembered or not. It also makes it easier to never persist the Auth state for applications that are shared by other users or have sensitive data.

This method does not work in a Node.js environment.

**Signature:**  

    setPersistence(persistence: Persistence): Promise<void>;

#### Parameters

|  Parameter  |                                                  Type                                                  |                                                    Description                                                     |
|-------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| persistence | [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface) | The [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface) to use. |

**Returns:**

Promise\<void\>

### Example

    auth.setPersistence(browserSessionPersistence);

## Auth.signOut()

Signs out the current user. This does not automatically revoke the user's ID token.

This method is not supported by [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instances created with a [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    signOut(): Promise<void>;

**Returns:**

Promise\<void\>

## Auth.updateCurrentUser()

Asynchronously sets the provided user as [Auth.currentUser](https://firebase.google.com/docs/reference/js/auth.auth.md#authcurrentuser) on the [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance.

A new instance copy of the user provided will be made and set as currentUser.

This will trigger [Auth.onAuthStateChanged()](https://firebase.google.com/docs/reference/js/auth.auth.md#authonauthstatechanged) and [Auth.onIdTokenChanged()](https://firebase.google.com/docs/reference/js/auth.auth.md#authonidtokenchanged) listeners like other sign in methods.

The operation fails with an error if the user to be updated belongs to a different Firebase project.

**Signature:**  

    updateCurrentUser(user: User | null): Promise<void>;

#### Parameters

| Parameter |                                           Type                                            |                                        Description                                         |
|-----------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) \| null | The new [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface). |

**Returns:**

Promise\<void\>

## Auth.useDeviceLanguage()

Sets the current language to the default device/browser preference.

**Signature:**  

    useDeviceLanguage(): void;

**Returns:**

void