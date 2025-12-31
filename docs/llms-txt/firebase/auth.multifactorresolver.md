# Source: https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md.txt

# MultiFactorResolver interface

The class used to facilitate recovery from [MultiFactorError](https://firebase.google.com/docs/reference/js/auth.multifactorerror.md#multifactorerror_interface) when a user needs to provide a second factor to sign in.

**Signature:**  

    export interface MultiFactorResolver 

## Properties

|                                                    Property                                                     |                                                            Type                                                             |                                                  Description                                                  |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [hints](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolverhints)     | [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)\[\]      | The list of hints for the second factors needed to complete the sign-in for the current session.              |
| [session](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolversession) | [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) | The session identifier for the current sign-in flow, which can be used to complete the second factor sign-in. |

## Methods

|                                                                 Method                                                                 |                                                                                                                                       Description                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [resolveSignIn(assertion)](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolverresolvesignin) | A helper function to help users complete sign in with a second factor using an [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface) confirming the user successfully completed the second factor challenge. |

## MultiFactorResolver.hints

The list of hints for the second factors needed to complete the sign-in for the current session.

**Signature:**  

    readonly hints: MultiFactorInfo[];

## MultiFactorResolver.session

The session identifier for the current sign-in flow, which can be used to complete the second factor sign-in.

**Signature:**  

    readonly session: MultiFactorSession;

## MultiFactorResolver.resolveSignIn()

A helper function to help users complete sign in with a second factor using an [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface) confirming the user successfully completed the second factor challenge.

**Signature:**  

    resolveSignIn(assertion: MultiFactorAssertion): Promise<UserCredential>;

#### Parameters

| Parameter |                                                               Type                                                                |                     Description                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| assertion | [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface) | The multi-factor assertion to resolve sign-in with. |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

The promise that resolves with the user credential object.

### Example

    const phoneAuthCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(phoneAuthCredential);
    const userCredential = await resolver.resolveSignIn(multiFactorAssertion);

### Example

    let resolver;
    let multiFactorHints;

    signInWithEmailAndPassword(auth, email, password)
        .then((result) => {
          // User signed in. No 2nd factor challenge is needed.
        })
        .catch((error) => {
          if (error.code == 'auth/multi-factor-auth-required') {
            resolver = getMultiFactorResolver(auth, error);
            // Show UI to let user select second factor.
            multiFactorHints = resolver.hints;
          } else {
            // Handle other errors.
          }
        });

    // The enrolled second factors that can be used to complete
    // sign-in are returned in the `MultiFactorResolver.hints` list.
    // UI needs to be presented to allow the user to select a second factor
    // from that list.

    const selectedHint = // ; selected from multiFactorHints
    const phoneAuthProvider = new PhoneAuthProvider(auth);
    const phoneInfoOptions = {
      multiFactorHint: selectedHint,
      session: resolver.session
    };
    const verificationId = phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, appVerifier);
    // Store `verificationId` and show UI to let user enter verification code.

    // UI to enter verification code and continue.
    // Continue button click handler
    const phoneAuthCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(phoneAuthCredential);
    const userCredential = await resolver.resolveSignIn(multiFactorAssertion);