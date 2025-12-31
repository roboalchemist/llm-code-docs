# Source: https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md.txt

# PhoneAuthProvider class

Provider for generating an [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class).

`PhoneAuthProvider` does not work in a Node.js environment.

**Signature:**  

    export declare class PhoneAuthProvider 

## Constructors

|                                                         Constructor                                                         | Modifiers |                        Description                         |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [(constructor)(auth)](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderconstructor) |           | Constructs a new instance of the `PhoneAuthProvider` class |

## Properties

|                                                               Property                                                                | Modifiers |  Type   |                                               Description                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|-----------|---------|---------------------------------------------------------------------------------------------------------|
| [PHONE_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderphone_sign_in_method) | `static`  | 'phone' | Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).PHONE. |
| [PROVIDER_ID](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderprovider_id)                   | `static`  | 'phone' | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PHONE.     |
| [providerId](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderproviderid)                     |           | "phone" | Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PHONE.     |

## Methods

|                                                                               Method                                                                               | Modifiers |                                                                                                                                 Description                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential(verificationId, verificationCode)](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovidercredential)                | `static`  | Creates a phone auth credential, given the verification ID from [PhoneAuthProvider.verifyPhoneNumber()](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderverifyphonenumber) and the code that was sent to the user's mobile device. |
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovidercredentialfromerror)                         | `static`  | Returns an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) when passed an error.                                                                                                                                |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovidercredentialfromresult)              | `static`  | Generates an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).                            |
| [verifyPhoneNumber(phoneOptions, applicationVerifier)](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderverifyphonenumber) |           | Starts a phone number authentication flow by sending a verification code to the given phone number.                                                                                                                                                                         |

## PhoneAuthProvider.(constructor)

Constructs a new instance of the `PhoneAuthProvider` class

**Signature:**  

    constructor(auth: Auth);

#### Parameters

| Parameter |                                       Type                                        |                                                               Description                                                               |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The Firebase [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance in which sign-ins should occur. |

## PhoneAuthProvider.PHONE_SIGN_IN_METHOD

Always set to [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).PHONE.

**Signature:**  

    static readonly PHONE_SIGN_IN_METHOD: 'phone';

## PhoneAuthProvider.PROVIDER_ID

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PHONE.

**Signature:**  

    static readonly PROVIDER_ID: 'phone';

## PhoneAuthProvider.providerId

Always set to [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PHONE.

**Signature:**  

    readonly providerId: "phone";

## PhoneAuthProvider.credential()

Creates a phone auth credential, given the verification ID from [PhoneAuthProvider.verifyPhoneNumber()](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderverifyphonenumber) and the code that was sent to the user's mobile device.

**Signature:**  

    static credential(verificationId: string, verificationCode: string): PhoneAuthCredential;

#### Parameters

|    Parameter     |  Type  |                                                                                      Description                                                                                       |
|------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| verificationId   | string | The verification ID returned from [PhoneAuthProvider.verifyPhoneNumber()](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthproviderverifyphonenumber). |
| verificationCode | string | The verification code sent to the user's mobile device.                                                                                                                                |

**Returns:**

[PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class)

The auth provider credential.

### Example 1

    const provider = new PhoneAuthProvider(auth);
    const verificationId = provider.verifyPhoneNumber(phoneNumber, applicationVerifier);
    // Obtain verificationCode from the user.
    const authCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const userCredential = signInWithCredential(auth, authCredential);

### Example 2

An alternative flow is provided using the `signInWithPhoneNumber` method.  

    const confirmationResult = await signInWithPhoneNumber(auth, phoneNumber, applicationVerifier);
    // Obtain verificationCode from the user.
    const userCredential = await confirmationResult.confirm(verificationCode);

## PhoneAuthProvider.credentialFromError()

Returns an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) when passed an error.

This method works for errors like `auth/account-exists-with-different-credentials`. This is useful for recovering when attempting to set a user's phone number but the number in question is already tied to another account. For example, the following code tries to update the current user's phone number, and if that fails, links the user with the account associated with that number:  

    const provider = new PhoneAuthProvider(auth);
    const verificationId = await provider.verifyPhoneNumber(number, verifier);
    try {
      const code = ''; // Prompt the user for the verification code
      await updatePhoneNumber(
          auth.currentUser,
          PhoneAuthProvider.credential(verificationId, code));
    } catch (e) {
      if ((e as FirebaseError)?.code === 'auth/account-exists-with-different-credential') {
        const cred = PhoneAuthProvider.credentialFromError(e);
        await linkWithCredential(auth.currentUser, cred);
      }
    }

    // At this point, auth.currentUser.phoneNumber === number.

**Signature:**  

    static credentialFromError(error: FirebaseError): AuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   |               Description                |
|-----------|----------------------------------------------------------------------------------------------------------|------------------------------------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) | The error to generate a credential from. |

**Returns:**

[AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) \| null

## PhoneAuthProvider.credentialFromResult()

Generates an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface).

**Signature:**  

    static credentialFromResult(userCredential: UserCredential): AuthCredential | null;

#### Parameters

|   Parameter    |                                                      Type                                                       |     Description      |
|----------------|-----------------------------------------------------------------------------------------------------------------|----------------------|
| userCredential | [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface) | The user credential. |

**Returns:**

[AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) \| null

## PhoneAuthProvider.verifyPhoneNumber()

Starts a phone number authentication flow by sending a verification code to the given phone number.

**Signature:**  

    verifyPhoneNumber(phoneOptions: PhoneInfoOptions | string, applicationVerifier?: ApplicationVerifier): Promise<string>;

#### Parameters

|      Parameter      |                                                              Type                                                              |                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                            |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| phoneOptions        | [PhoneInfoOptions](https://firebase.google.com/docs/reference/js/auth.md#phoneinfooptions) \| string                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| applicationVerifier | [ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface) | An [ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface), which prevents requests from unauthorized clients. This SDK includes an implementation based on reCAPTCHA v2, [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifier_class). If you've enabled reCAPTCHA Enterprise bot protection in Enforce mode, this parameter is optional; in all other configurations, the parameter is required. |

**Returns:**

Promise\<string\>

A Promise for a verification ID that can be passed to [PhoneAuthProvider.credential()](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovidercredential) to identify this flow.

### Example 1

    const provider = new PhoneAuthProvider(auth);
    const verificationId = await provider.verifyPhoneNumber(phoneNumber, applicationVerifier);
    // Obtain verificationCode from the user.
    const authCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const userCredential = await signInWithCredential(auth, authCredential);

### Example 2

An alternative flow is provided using the `signInWithPhoneNumber` method.  

    const confirmationResult = signInWithPhoneNumber(auth, phoneNumber, applicationVerifier);
    // Obtain verificationCode from the user.
    const userCredential = confirmationResult.confirm(verificationCode);

### Example

    // 'recaptcha-container' is the ID of an element in the DOM.
    const applicationVerifier = new RecaptchaVerifier('recaptcha-container');
    const provider = new PhoneAuthProvider(auth);
    const verificationId = await provider.verifyPhoneNumber('+16505550101', applicationVerifier);
    // Obtain the verificationCode from the user.
    const phoneCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const userCredential = await signInWithCredential(auth, phoneCredential);