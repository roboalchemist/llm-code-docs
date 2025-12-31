# Source: https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorgenerator.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator.md.txt

# PhoneMultiFactorGenerator | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- PhoneMultiFactorGenerator

The class used to initialize [firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorassertion).

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator#constructor)

### Properties

- [FACTOR_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator#factor_id)

### Methods

- [assertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator#assertion)

## Constructors

### Private constructor

- new PhoneMultiFactorGenerator ( ) : [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator)
-

  #### Returns [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator)

## Properties

### Static FACTOR_ID

FACTOR_ID: string  
The identifier of the phone second factor: `phone`.

## Methods

### Static assertion

- assertion ( phoneAuthCredential : [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential) ) : [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorassertion)
- Initializes the [firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorassertion) to confirm ownership
  of the phone second factor.

  #### Parameters

  -

    ##### phoneAuthCredential: [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential)

  #### Returns [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorassertion)