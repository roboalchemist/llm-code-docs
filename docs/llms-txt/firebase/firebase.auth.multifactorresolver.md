# Source: https://firebase.google.com/docs/reference/node/firebase.auth.multifactorresolver.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.multifactorresolver.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver.md.txt

# MultiFactorResolver | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- MultiFactorResolver

The class used to facilitate recovery from
[firebase.auth.MultiFactorError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror) when a user needs to provide a second
factor to sign in.

example
:

        firebase.auth().signInWithEmailAndPassword()
            .then(function(result) {
              // User signed in. No 2nd factor challenge is needed.
            })
            .catch(function(error) {
              if (error.code == 'auth/multi-factor-auth-required') {
                var resolver = error.resolver;
                // Show UI to let user select second factor.
                var multiFactorHints = resolver.hints;
              } else {
                // Handle other errors.
              }
            });

        // The enrolled second factors that can be used to complete
        // sign-in are returned in the `MultiFactorResolver.hints` list.
        // UI needs to be presented to allow the user to select a second factor
        // from that list.

        var selectedHint = // ; selected from multiFactorHints
        var phoneAuthProvider = new firebase.auth.PhoneAuthProvider();
        var phoneInfoOptions = {
          multiFactorHint: selectedHint,
          session: resolver.session
        };
        phoneAuthProvider.verifyPhoneNumber(
          phoneInfoOptions,
          appVerifier
        ).then(function(verificationId) {
          // store verificationID and show UI to let user enter verification code.
        });

        // UI to enter verification code and continue.
        // Continue button click handler
        var phoneAuthCredential =
            firebase.auth.PhoneAuthProvider.credential(verificationId, verificationCode);
        var multiFactorAssertion =
            firebase.auth.PhoneMultiFactorGenerator.assertion(phoneAuthCredential);
        resolver.resolveSignIn(multiFactorAssertion)
            .then(function(userCredential) {
              // User signed in.
            });


## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver#constructor)

### Properties

- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver#auth)
- [hints](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver#hints)
- [session](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver#session)

### Methods

- [resolveSignIn](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver#resolvesignin)

## Constructors

### Private constructor

- new MultiFactorResolver ( ) : [MultiFactorResolver](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver)
-

  #### Returns [MultiFactorResolver](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver)

## Properties

### auth

auth: [Auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth)  
The Auth instance used to sign in with the first factor.

### hints

hints: [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo)\[\]  
The list of hints for the second factors needed to complete the sign-in
for the current session.

### session

session: [MultiFactorSession](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorsession)  
The session identifier for the current sign-in flow, which can be used
to complete the second factor sign-in.

## Methods

### resolveSignIn

- resolveSignIn ( assertion : [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorassertion) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- A helper function to help users complete sign in with a second factor
  using an [firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorassertion) confirming the user
  successfully completed the second factor challenge.

  #### Error Codes

  auth/invalid-verification-code
  :   Thrown if the verification code is not valid.

  auth/missing-verification-code
  :   Thrown if the verification code is missing.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  auth/missing-verification-id
  :   Thrown if the verification ID is missing.

  auth/code-expired
  :   Thrown if the verification code has expired.

  auth/invalid-multi-factor-session
  :   Thrown if the request does not contain a valid proof of first factor
      successful sign-in.

  auth/missing-multi-factor-session
  :   Thrown if The request is missing proof of first factor successful
      sign-in.

  #### Parameters

  -

    ##### assertion: [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorassertion)

    The multi-factor assertion to resolve sign-in with.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

The promise that resolves with the user credential object.