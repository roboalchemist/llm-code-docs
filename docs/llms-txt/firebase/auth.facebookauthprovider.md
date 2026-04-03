# Source: https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md.txt

# FacebookAuthProvider class

Provider for generating an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) for [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).FACEBOOK.

**Signature:**  

    export declare class FacebookAuthProvider extends BaseOAuthProvider 

**Extends:** BaseOAuthProvider

## Constructors

|                                                          Constructor                                                          | Modifiers |                          Description                          |
|-------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthproviderconstructor) |           | Constructs a new instance of the `FacebookAuthProvider` class |

## Properties

|                                                                     Property                                                                      | Modifiers |      Type      |                                                Description                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------|------------------------------------------------------------------------------------------------------------|
| [FACEBOOK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthproviderfacebook_sign_in_method) | `static`  | 'facebook.com' | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).FACEBOOK. |
| [PROVIDER_ID](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthproviderprovider_id)                         | `static`  | 'facebook.com' | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).FACEBOOK.     |

## Methods

|                                                                           Method                                                                            | Modifiers |                                                                                                                                                         Description                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(accessToken)](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthprovidercredential)                        | `static`  | Creates a credential for Facebook.                                                                                                                                                                                                                                                                                          |
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthprovidercredentialfromerror)            | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation. |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthprovidercredentialfromresult) | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).                                                       |

## FacebookAuthProvider.(constructor)

Constructs a new instance of the `FacebookAuthProvider` class

**Signature:**  

    constructor();

## FacebookAuthProvider.FACEBOOK_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).FACEBOOK.

**Signature:**  

    static readonly FACEBOOK_SIGN_IN_METHOD: 'facebook.com';

## FacebookAuthProvider.PROVIDER_ID

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).FACEBOOK.

**Signature:**  

    static readonly PROVIDER_ID: 'facebook.com';

## FacebookAuthProvider.credential()

Creates a credential for Facebook.

**Signature:**  

    static credential(accessToken: string): OAuthCredential;

#### Parameters

|  Parameter  |  Type  |      Description       |
|-------------|--------|------------------------|
| accessToken | string | Facebook access token. |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)

### Example

    // `event` from the Facebook auth.authResponseChange callback.
    const credential = FacebookAuthProvider.credential(event.authResponse.accessToken);
    const result = await signInWithCredential(credential);

## FacebookAuthProvider.credentialFromError()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation.

**Signature:**  

    static credentialFromError(error: FirebaseError): OAuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------|-------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) |             |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

## FacebookAuthProvider.credentialFromResult()

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
    const provider = new FacebookAuthProvider();
    // Start a sign in process for an unauthenticated user.
    provider.addScope('user_birthday');
    await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    if (result) {
      // This is the signed-in user
      const user = result.user;
      // This gives you a Facebook Access Token.
      const credential = FacebookAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
    }

### Example 2

    // Sign in using a popup.
    const provider = new FacebookAuthProvider();
    provider.addScope('user_birthday');
    const result = await signInWithPopup(auth, provider);

    // The signed-in user info.
    const user = result.user;
    // This gives you a Facebook Access Token.
    const credential = FacebookAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;