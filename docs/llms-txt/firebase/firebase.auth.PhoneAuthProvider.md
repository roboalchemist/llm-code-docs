# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider.md.txt

# PhoneAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [auth](https://firebase.google.com/docs/reference/node/firebase.auth).
- PhoneAuthProvider

Phone number auth provider.

example
:

        // 'recaptcha-container' is the ID of an element in the DOM.
        var applicationVerifier = new firebase.auth.RecaptchaVerifier(
            'recaptcha-container');
        var provider = new firebase.auth.PhoneAuthProvider();
        provider.verifyPhoneNumber('+16505550101', applicationVerifier)
            .then(function(verificationId) {
              var verificationCode = window.prompt('Please enter the verification ' +
                  'code that was sent to your mobile device.');
              return firebase.auth.PhoneAuthProvider.credential(verificationId,
                  verificationCode);
            })
            .then(function(phoneCredential) {
              return firebase.auth().signInWithCredential(phoneCredential);
            });


param

:   The Firebase Auth instance in which
    sign-ins should occur. Uses the default Auth instance if unspecified.

### Implements

- [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#constructor)

### Properties

- [providerId](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#providerid)
- [PHONE_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#phone_sign_in_method)
- [PROVIDER_ID](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#provider_id)

### Methods

- [verifyPhoneNumber](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#verifyphonenumber)
- [credential](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#credential)

## Constructors

### constructor

- new PhoneAuthProvider ( auth ? : [Auth](https://firebase.google.com/docs/reference/node/firebase.auth.Auth) \| null ) : [PhoneAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider)
-
  | Inherited from [PhoneAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider).[constructor](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#constructor)

  #### Parameters

  -

    ##### Optional auth: [Auth](https://firebase.google.com/docs/reference/node/firebase.auth.Auth) \| null

  #### Returns [PhoneAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider#providerid)
| Inherited from [PhoneAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider).[providerId](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#providerid)

### Static PHONE_SIGN_IN_METHOD

PHONE_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/node/firebase.auth.Auth#fetchsigninmethodsforemail).

### Static PROVIDER_ID

PROVIDER_ID: string

## Methods

### verifyPhoneNumber

- verifyPhoneNumber ( phoneInfoOptions : [PhoneInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth#phoneinfooptions) \| string , applicationVerifier : [ApplicationVerifier](https://firebase.google.com/docs/reference/node/firebase.auth.ApplicationVerifier) ) : Promise \< string \>
-
  Inherited from [PhoneAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider).[verifyPhoneNumber](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#verifyphonenumber)  
  Starts a phone number authentication flow by sending a verification code to
  the given phone number. Returns an ID that can be passed to
  [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#credential) to identify this flow.

  For abuse prevention, this method also requires a
  [firebase.auth.ApplicationVerifier](https://firebase.google.com/docs/reference/node/firebase.auth.ApplicationVerifier). The Firebase Auth SDK includes
  a reCAPTCHA-based implementation, firebase.auth.RecaptchaVerifier.

  #### Error Codes

  auth/captcha-check-failed
  :   Thrown if the reCAPTCHA response token was invalid, expired, or if
      this method was called from a non-whitelisted domain.

  auth/invalid-phone-number
  :   Thrown if the phone number has an invalid format.

  auth/missing-phone-number
  :   Thrown if the phone number is missing.

  auth/quota-exceeded
  :   Thrown if the SMS quota for the Firebase project has been exceeded.

  auth/user-disabled
  :   Thrown if the user corresponding to the given phone number has been
      disabled.

  auth/maximum-second-factor-count-exceeded
  :   Thrown if The maximum allowed number of second factors on a user
      has been exceeded.

  auth/second-factor-already-in-use
  :   Thrown if the second factor is already enrolled on this account.

  auth/unsupported-first-factor
  :   Thrown if the first factor being used to sign in is not supported.

  auth/unverified-email
  :   Thrown if the email of the account is not verified.

  #### Parameters

  -

    ##### phoneInfoOptions: [PhoneInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth#phoneinfooptions) \| string

    The user's [firebase.auth.PhoneInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth#phoneinfooptions).
    The phone number should be in E.164 format (e.g. +16505550101).
  -

    ##### applicationVerifier: [ApplicationVerifier](https://firebase.google.com/docs/reference/node/firebase.auth.ApplicationVerifier)

  #### Returns Promise\<string\>

  A Promise for the verification ID.

### Static credential

- credential ( verificationId : string , verificationCode : string ) : [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential)
- Creates a phone auth credential, given the verification ID from
  [firebase.auth.PhoneAuthProvider.verifyPhoneNumber](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#verifyphonenumber) and the code
  that was sent to the user's mobile device.

  #### Error Codes

  auth/missing-verification-code
  :   Thrown if the verification code is missing.

  auth/missing-verification-id
  :   Thrown if the verification ID is missing.

  #### Parameters

  -

    ##### verificationId: string

    The verification ID returned from
    [firebase.auth.PhoneAuthProvider.verifyPhoneNumber](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider#verifyphonenumber).
  -

    ##### verificationCode: string

    The verification code sent to the user's
    mobile device.

  #### Returns [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential)

The auth provider credential.