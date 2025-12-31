# Source: https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md.txt

# GoogleAuthProvider class

Provider for generating an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) for [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GOOGLE.

**Signature:**  

    export declare class GoogleAuthProvider extends BaseOAuthProvider 

**Extends:** BaseOAuthProvider

## Constructors

|                                                        Constructor                                                        | Modifiers |                         Description                         |
|---------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthproviderconstructor) |           | Constructs a new instance of the `GoogleAuthProvider` class |

## Properties

|                                                                 Property                                                                  | Modifiers |     Type     |                                               Description                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------|----------------------------------------------------------------------------------------------------------|
| [GOOGLE_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthprovidergoogle_sign_in_method) | `static`  | 'google.com' | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).GOOGLE. |
| [PROVIDER_ID](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthproviderprovider_id)                     | `static`  | 'google.com' | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GOOGLE.     |

## Methods

|                                                                         Method                                                                          | Modifiers |                                                                                                                                                         Description                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(idToken, accessToken)](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthprovidercredential)               | `static`  | Creates a credential for Google. At least one of ID token and access token is required.                                                                                                                                                                                                                                     |
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthprovidercredentialfromerror)            | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation. |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthprovidercredentialfromresult) | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).                                                       |

## GoogleAuthProvider.(constructor)

Constructs a new instance of the `GoogleAuthProvider` class

**Signature:**  

    constructor();

## GoogleAuthProvider.GOOGLE_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).GOOGLE.

**Signature:**  

    static readonly GOOGLE_SIGN_IN_METHOD: 'google.com';

## GoogleAuthProvider.PROVIDER_ID

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GOOGLE.

**Signature:**  

    static readonly PROVIDER_ID: 'google.com';

## GoogleAuthProvider.credential()

Creates a credential for Google. At least one of ID token and access token is required.

**Signature:**  

    static credential(idToken?: string | null, accessToken?: string | null): OAuthCredential;

#### Parameters

|  Parameter  |      Type      |     Description      |
|-------------|----------------|----------------------|
| idToken     | string \| null | Google ID token.     |
| accessToken | string \| null | Google access token. |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)

### Example

    // \`googleUser\` from the onsuccess Google Sign In callback.
    const credential = GoogleAuthProvider.credential(googleUser.getAuthResponse().id_token);
    const result = await signInWithCredential(credential);

## GoogleAuthProvider.credentialFromError()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation.

**Signature:**  

    static credentialFromError(error: FirebaseError): OAuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------|-------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) |             |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

## GoogleAuthProvider.credentialFromResult()

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
    const provider = new GoogleAuthProvider();
    // Start a sign in process for an unauthenticated user.
    provider.addScope('profile');
    provider.addScope('email');
    await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    if (result) {
      // This is the signed-in user
      const user = result.user;
      // This gives you a Google Access Token.
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
    }

### Example 2

    // Sign in using a popup.
    const provider = new GoogleAuthProvider();
    provider.addScope('profile');
    provider.addScope('email');
    const result = await signInWithPopup(auth, provider);

    // The signed-in user info.
    const user = result.user;
    // This gives you a Google Access Token.
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;