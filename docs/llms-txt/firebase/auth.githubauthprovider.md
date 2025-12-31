# Source: https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md.txt

# GithubAuthProvider class

Provider for generating an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) for [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GITHUB.

GitHub requires an OAuth 2.0 redirect, so you can either handle the redirect directly, or use the [signInWithPopup()](https://firebase.google.com/docs/reference/js/auth.md#signinwithpopup_770f816) handler:

**Signature:**  

    export declare class GithubAuthProvider extends BaseOAuthProvider 

**Extends:** BaseOAuthProvider

## Constructors

|                                                        Constructor                                                        | Modifiers |                         Description                         |
|---------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthproviderconstructor) |           | Constructs a new instance of the `GithubAuthProvider` class |

## Properties

|                                                                 Property                                                                  | Modifiers |     Type     |                                               Description                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------|----------------------------------------------------------------------------------------------------------|
| [GITHUB_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthprovidergithub_sign_in_method) | `static`  | 'github.com' | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).GITHUB. |
| [PROVIDER_ID](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthproviderprovider_id)                     | `static`  | 'github.com' | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GITHUB.     |

## Methods

|                                                                         Method                                                                          | Modifiers |                                                                                                                                                         Description                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(accessToken)](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthprovidercredential)                        | `static`  | Creates a credential for GitHub.                                                                                                                                                                                                                                                                                            |
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthprovidercredentialfromerror)            | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation. |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthprovidercredentialfromresult) | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).                                                       |

## GithubAuthProvider.(constructor)

Constructs a new instance of the `GithubAuthProvider` class

**Signature:**  

    constructor();

## GithubAuthProvider.GITHUB_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).GITHUB.

**Signature:**  

    static readonly GITHUB_SIGN_IN_METHOD: 'github.com';

## GithubAuthProvider.PROVIDER_ID

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GITHUB.

**Signature:**  

    static readonly PROVIDER_ID: 'github.com';

## GithubAuthProvider.credential()

Creates a credential for GitHub.

**Signature:**  

    static credential(accessToken: string): OAuthCredential;

#### Parameters

|  Parameter  |  Type  |     Description      |
|-------------|--------|----------------------|
| accessToken | string | GitHub access token. |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)

## GithubAuthProvider.credentialFromError()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation.

**Signature:**  

    static credentialFromError(error: FirebaseError): OAuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------|-------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) |             |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

## GithubAuthProvider.credentialFromResult()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).

**Signature:**  

    static credentialFromResult(userCredential: UserCredential): OAuthCredential | null;

#### Parameters

|   Parameter    |                                                      Type                                                       |     Description      |
|----------------|-----------------------------------------------------------------------------------------------------------------|----------------------|
| userCredential | [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface) | The user credential. |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

### Example 1

    // Sign in using a redirect.
    const provider = new GithubAuthProvider();
    // Start a sign in process for an unauthenticated user.
    provider.addScope('repo');
    await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    if (result) {
      // This is the signed-in user
      const user = result.user;
      // This gives you a GitHub Access Token.
      const credential = GithubAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
    }

### Example 2

    // Sign in using a popup.
    const provider = new GithubAuthProvider();
    provider.addScope('repo');
    const result = await signInWithPopup(auth, provider);

    // The signed-in user info.
    const user = result.user;
    // This gives you a GitHub Access Token.
    const credential = GithubAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;