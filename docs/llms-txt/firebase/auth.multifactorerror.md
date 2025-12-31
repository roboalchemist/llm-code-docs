# Source: https://firebase.google.com/docs/reference/js/auth.multifactorerror.md.txt

# MultiFactorError interface

The error thrown when the user needs to provide a second factor to sign in successfully.

The error code for this error is `auth/multi-factor-auth-required`.

**Signature:**  

    export interface MultiFactorError extends AuthError 

**Extends:** [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface)

## Properties

|                                                    Property                                                     |                                                                                                                                                                           Type                                                                                                                                                                            |             Description             |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| [customData](https://firebase.google.com/docs/reference/js/auth.multifactorerror.md#multifactorerrorcustomdata) | [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface)\['customData'\] \& { readonly operationType: (typeof [OperationTypeMap](https://firebase.google.com/docs/reference/js/auth.md#operationtype))\[keyof typeof [OperationTypeMap](https://firebase.google.com/docs/reference/js/auth.md#operationtype)\]; } | Details about the MultiFactorError. |

## MultiFactorError.customData

Details about the MultiFactorError.

**Signature:**  

    readonly customData: AuthError['customData'] & {
            readonly operationType: (typeof OperationTypeMap)[keyof typeof OperationTypeMap];
        };

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
            multiFactorHints = resolver.hints;
          } else {
            // Handle other errors.
          }
        });

    // Obtain a multiFactorAssertion by verifying the second factor.

    const userCredential = await resolver.resolveSignIn(multiFactorAssertion);