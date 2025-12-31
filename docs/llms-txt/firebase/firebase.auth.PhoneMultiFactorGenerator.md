# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator.md.txt

# PhoneMultiFactorGenerator | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- PhoneMultiFactorGenerator

The class used to initialize [firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorAssertion).

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator#constructor)

### Properties

- [FACTOR_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator#factor_id)

### Methods

- [assertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator#assertion)

## Constructors

### Private constructor

- new PhoneMultiFactorGenerator ( ) : [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator)
-

  #### Returns [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator)

## Properties

### Static FACTOR_ID

FACTOR_ID: string  
The identifier of the phone second factor: `phone`.

## Methods

### Static assertion

- assertion ( phoneAuthCredential : [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthCredential) ) : [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorAssertion)
- Initializes the [firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorAssertion) to confirm ownership
  of the phone second factor.

  #### Parameters

  -

    ##### phoneAuthCredential: [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthCredential)

  #### Returns [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorAssertion)