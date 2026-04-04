# Source: https://firebase.google.com/docs/reference/js/auth.dependencies.md.txt

# Dependencies interface

The dependencies that can be used to initialize an [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance.

The modular SDK enables tree shaking by allowing explicit declarations of dependencies. For example, a web app does not need to include code that enables Cordova redirect sign in. That functionality is therefore split into [browserPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#browserpopupredirectresolver) and [cordovaPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#cordovapopupredirectresolver). The dependencies object is how Auth is configured to reduce bundle sizes.

There are two ways to initialize an [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance: [getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1) and [initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b). `getAuth` initializes everything using platform-specific configurations, while `initializeAuth` takes a `Dependencies` object directly, giving you more control over what is used.

**Signature:**  

    export interface Dependencies 

## Properties

|                                                           Property                                                            |                                                                                                         Type                                                                                                         |                                                                                                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [errorMap](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependencieserrormap)                           | [AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface)                                                                                                            | Which [AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface) to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [persistence](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependenciespersistence)                     | [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface) \| [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)\[\] | Which [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface) to use. If this is an array, the first `Persistence` that the device supports is used. The SDK searches for an existing account in order and, if one is found in a secondary `Persistence`, the account is moved to the primary `Persistence`.If no persistence is provided, the SDK falls back on [inMemoryPersistence](https://firebase.google.com/docs/reference/js/auth.md#inmemorypersistence).                                                                                                                                                                                            |
| [popupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependenciespopupredirectresolver) | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface)                                                                                 | The [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) to use. This value depends on the platform. Options are [browserPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#browserpopupredirectresolver) and [cordovaPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#cordovapopupredirectresolver). This field is optional if neither [signInWithPopup()](https://firebase.google.com/docs/reference/js/auth.md#signinwithpopup_770f816) or [signInWithRedirect()](https://firebase.google.com/docs/reference/js/auth.md#signinwithredirect_770f816) are being used. |

## Dependencies.errorMap

Which [AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface) to use.

**Signature:**  

    errorMap?: AuthErrorMap;

## Dependencies.persistence

Which [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface) to use. If this is an array, the first `Persistence` that the device supports is used. The SDK searches for an existing account in order and, if one is found in a secondary `Persistence`, the account is moved to the primary `Persistence`.

If no persistence is provided, the SDK falls back on [inMemoryPersistence](https://firebase.google.com/docs/reference/js/auth.md#inmemorypersistence).

**Signature:**  

    persistence?: Persistence | Persistence[];

## Dependencies.popupRedirectResolver

The [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) to use. This value depends on the platform. Options are [browserPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#browserpopupredirectresolver) and [cordovaPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#cordovapopupredirectresolver). This field is optional if neither [signInWithPopup()](https://firebase.google.com/docs/reference/js/auth.md#signinwithpopup_770f816) or [signInWithRedirect()](https://firebase.google.com/docs/reference/js/auth.md#signinwithredirect_770f816) are being used.

**Signature:**  

    popupRedirectResolver?: PopupRedirectResolver;