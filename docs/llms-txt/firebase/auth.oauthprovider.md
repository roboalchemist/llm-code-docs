# Source: https://firebase.google.com/docs/reference/js/auth.oauthprovider.md.txt

# OAuthProvider class

Provider for generating generic [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).

**Signature:**  

    export declare class OAuthProvider extends BaseOAuthProvider 

**Extends:** BaseOAuthProvider

## Methods

|                                                                    Method                                                                     | Modifiers |                                                                                                                                                         Description                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(params)](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovidercredential)                             |           | Creates a [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a generic OAuth provider's access token or ID token.                                                                                                                                          |
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovidercredentialfromerror)            | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation. |
| [credentialFromJSON(json)](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovidercredentialfromjson)               | `static`  | Creates an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a JSON string or a plain object.                                                                                                                                                             |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovidercredentialfromresult) | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).                                                       |

## OAuthProvider.credential()

Creates a [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a generic OAuth provider's access token or ID token.

The raw nonce is required when an ID token with a nonce field is provided. The SHA-256 hash of the raw nonce must match the nonce field in the ID token.

**Signature:**  

    credential(params: OAuthCredentialOptions): OAuthCredential;

#### Parameters

| Parameter |                                                                  Type                                                                   |                                              Description                                              |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| params    | [OAuthCredentialOptions](https://firebase.google.com/docs/reference/js/auth.oauthcredentialoptions.md#oauthcredentialoptions_interface) | Either the options object containing the ID token, access token and raw nonce or the ID token string. |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)

### Example

    // `googleUser` from the onsuccess Google Sign In callback.
    // Initialize a generate OAuth provider with a `google.com` providerId.
    const provider = new OAuthProvider('google.com');
    const credential = provider.credential({
      idToken: googleUser.getAuthResponse().id_token,
    });
    const result = await signInWithCredential(credential);

## OAuthProvider.credentialFromError()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation.

**Signature:**  

    static credentialFromError(error: FirebaseError): OAuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------|-------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) |             |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

## OAuthProvider.credentialFromJSON()

Creates an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a JSON string or a plain object.

**Signature:**  

    static credentialFromJSON(json: object | string): OAuthCredential;

#### Parameters

| Parameter |       Type       |           Description           |
|-----------|------------------|---------------------------------|
| json      | object \| string | A plain object or a JSON string |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)

## OAuthProvider.credentialFromResult()

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
    const provider = new OAuthProvider('google.com');
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
      // This gives you a OAuth Access Token for the provider.
      const credential = provider.credentialFromResult(auth, result);
      const token = credential.accessToken;
    }

### Example 2

    // Sign in using a popup.
    const provider = new OAuthProvider('google.com');
    provider.addScope('profile');
    provider.addScope('email');
    const result = await signInWithPopup(auth, provider);

    // The signed-in user info.
    const user = result.user;
    // This gives you a OAuth Access Token for the provider.
    const credential = provider.credentialFromResult(auth, result);
    const token = credential.accessToken;