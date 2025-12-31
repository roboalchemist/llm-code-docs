# Source: https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md.txt

# TwitterAuthProvider class

Provider for generating an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) for [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).TWITTER.

**Signature:**  

    export declare class TwitterAuthProvider extends BaseOAuthProvider 

**Extends:** BaseOAuthProvider

## Constructors

|                                                         Constructor                                                         | Modifiers |                         Description                          |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthproviderconstructor) |           | Constructs a new instance of the `TwitterAuthProvider` class |

## Properties

|                                                                   Property                                                                    | Modifiers |     Type      |                                                Description                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------|-----------------------------------------------------------------------------------------------------------|
| [PROVIDER_ID](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthproviderprovider_id)                       | `static`  | 'twitter.com' | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).TWITTER.     |
| [TWITTER_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthprovidertwitter_sign_in_method) | `static`  | 'twitter.com' | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).TWITTER. |

## Methods

|                                                                          Method                                                                           | Modifiers |                                                                                                                                                         Description                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(token, secret)](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthprovidercredential)                      | `static`  | Creates a credential for Twitter.                                                                                                                                                                                                                                                                                           |
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthprovidercredentialfromerror)            | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation. |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthprovidercredentialfromresult) | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).                                                       |

## TwitterAuthProvider.(constructor)

Constructs a new instance of the `TwitterAuthProvider` class

**Signature:**  

    constructor();

## TwitterAuthProvider.PROVIDER_ID

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).TWITTER.

**Signature:**  

    static readonly PROVIDER_ID: 'twitter.com';

## TwitterAuthProvider.TWITTER_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).TWITTER.

**Signature:**  

    static readonly TWITTER_SIGN_IN_METHOD: 'twitter.com';

## TwitterAuthProvider.credential()

Creates a credential for Twitter.

**Signature:**  

    static credential(token: string, secret: string): OAuthCredential;

#### Parameters

| Parameter |  Type  |      Description      |
|-----------|--------|-----------------------|
| token     | string | Twitter access token. |
| secret    | string | Twitter secret.       |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)

## TwitterAuthProvider.credentialFromError()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation.

**Signature:**  

    static credentialFromError(error: FirebaseError): OAuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------|-------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) |             |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

## TwitterAuthProvider.credentialFromResult()

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
    const provider = new TwitterAuthProvider();
    // Start a sign in process for an unauthenticated user.
    await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    if (result) {
      // This is the signed-in user
      const user = result.user;
      // This gives you a Twitter Access Token and Secret.
      const credential = TwitterAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      const secret = credential.secret;
    }

### Example 2

    // Sign in using a popup.
    const provider = new TwitterAuthProvider();
    const result = await signInWithPopup(auth, provider);

    // The signed-in user info.
    const user = result.user;
    // This gives you a Twitter Access Token and Secret.
    const credential = TwitterAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    const secret = credential.secret;