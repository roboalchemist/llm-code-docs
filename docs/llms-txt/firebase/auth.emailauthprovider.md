# Source: https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md.txt

# EmailAuthProvider class

Provider for generating [EmailAuthCredential](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredential_class).

**Signature:**  

    export declare class EmailAuthProvider implements AuthProvider 

**Implements:** [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)

## Properties

|                                                                        Property                                                                         | Modifiers |    Type     |                                                         Description                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| [EMAIL_LINK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovideremail_link_sign_in_method)         | `static`  | 'emailLink' | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_LINK.                |
| [EMAIL_PASSWORD_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovideremail_password_sign_in_method) | `static`  | 'password'  | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_PASSWORD.            |
| [PROVIDER_ID](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthproviderprovider_id)                                     | `static`  | 'password'  | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PASSWORD, even for email link. |
| [providerId](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthproviderproviderid)                                       |           | "password"  | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PASSWORD, even for email link. |

## Methods

|                                                                       Method                                                                        | Modifiers |                                                                                              Description                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(email, password)](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovidercredential)                  | `static`  | Initialize an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) using an email and password.                                                |
| [credentialWithLink(email, emailLink)](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovidercredentialwithlink) | `static`  | Initialize an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) using an email and an email link after a sign in with email link operation. |

## EmailAuthProvider.EMAIL_LINK_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_LINK.

**Signature:**  

    static readonly EMAIL_LINK_SIGN_IN_METHOD: 'emailLink';

## EmailAuthProvider.EMAIL_PASSWORD_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_PASSWORD.

**Signature:**  

    static readonly EMAIL_PASSWORD_SIGN_IN_METHOD: 'password';

## EmailAuthProvider.PROVIDER_ID

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PASSWORD, even for email link.

**Signature:**  

    static readonly PROVIDER_ID: 'password';

## EmailAuthProvider.providerId

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PASSWORD, even for email link.

**Signature:**  

    readonly providerId: "password";

## EmailAuthProvider.credential()

Initialize an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) using an email and password.

**Signature:**  

    static credential(email: string, password: string): EmailAuthCredential;

#### Parameters

| Parameter |  Type  |      Description       |
|-----------|--------|------------------------|
| email     | string | Email address.         |
| password  | string | User account password. |

**Returns:**

[EmailAuthCredential](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredential_class)

The auth provider credential.

### Example 1

    const authCredential = EmailAuthProvider.credential(email, password);
    const userCredential = await signInWithCredential(auth, authCredential);

### Example 2

    const userCredential = await signInWithEmailAndPassword(auth, email, password);

## EmailAuthProvider.credentialWithLink()

Initialize an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) using an email and an email link after a sign in with email link operation.

**Signature:**  

    static credentialWithLink(email: string, emailLink: string): EmailAuthCredential;

#### Parameters

| Parameter |  Type  |     Description     |
|-----------|--------|---------------------|
| email     | string | Email address.      |
| emailLink | string | Sign-in email link. |

**Returns:**

[EmailAuthCredential](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredential_class)

- The auth provider credential.

### Example 1

    const authCredential = EmailAuthProvider.credentialWithLink(auth, email, emailLink);
    const userCredential = await signInWithCredential(auth, authCredential);

### Example 2

    await sendSignInLinkToEmail(auth, email);
    // Obtain emailLink from user.
    const userCredential = await signInWithEmailLink(auth, email, emailLink);