# Source: https://firebase.google.com/docs/reference/node/firebase.auth.ApplicationVerifier.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier.md.txt

# ApplicationVerifier | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- ApplicationVerifier

A verifier for domain verification and abuse prevention. Currently, the
only implementation is [firebase.auth.RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).

### Implemented by

- [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier)

## Index

### Properties

- [type](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier#type)

### Methods

- [verify](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier#verify)

## Properties

### type

type: string  
Identifies the type of application verifier (e.g. "recaptcha").

## Methods

### verify

- verify ( ) : Promise \< string \>
- Executes the verification process.

  #### Returns Promise\<string\>

  A Promise for a token that can be used to
assert the validity of a request.