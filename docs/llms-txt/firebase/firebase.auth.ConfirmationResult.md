# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.ConfirmationResult.md.txt

# ConfirmationResult | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [auth](https://firebase.google.com/docs/reference/node/firebase.auth).
- ConfirmationResult

A result from a phone number sign-in, link, or reauthenticate call.

## Index

### Properties

- [verificationId](https://firebase.google.com/docs/reference/node/firebase.auth.ConfirmationResult#verificationid)

### Methods

- [confirm](https://firebase.google.com/docs/reference/node/firebase.auth.ConfirmationResult#confirm)

## Properties

### verificationId

verificationId: string  
The phone number authentication operation's verification ID. This can be used
along with the verification code to initialize a phone auth credential.

## Methods

### confirm

- confirm ( verificationCode : string ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/node/firebase.auth#usercredential) \>
- Finishes a phone number sign-in, link, or reauthentication, given the code
  that was sent to the user's mobile device.

  #### Error Codes

  auth/invalid-verification-code
  :   Thrown if the verification code is not valid.

  auth/missing-verification-code
  :   Thrown if the verification code is missing.

  #### Parameters

  -

    ##### verificationCode: string

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/node/firebase.auth#usercredential)\>