# Source: https://firebase.google.com/docs/reference/node/firebase.auth.multifactorerror.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.multifactorerror.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror.md.txt

# MultiFactorError | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- MultiFactorError

The error thrown when the user needs to provide a second factor to sign in
successfully.
The error code for this error is `auth/multi-factor-auth-required`.
This error provides a [firebase.auth.MultiFactorResolver](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver) object,
which you can use to get the second sign-in factor from the user.

example
:

        firebase.auth().signInWithEmailAndPassword()
            .then(function(result) {
              // User signed in. No 2nd factor challenge is needed.
            })
            .catch(function(error) {
              if (error.code == 'auth/multi-factor-auth-required') {
                var resolver = error.resolver;
                var multiFactorHints = resolver.hints;
              } else {
                // Handle other errors.
              }
            });

        resolver.resolveSignIn(multiFactorAssertion)
            .then(function(userCredential) {
              // User signed in.
            });


## Index

### Properties

- [code](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#code)
- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#credential)
- [email](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#email)
- [message](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#message)
- [phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#phonenumber)
- [resolver](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#resolver)
- [tenantId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorerror#tenantid)

## Properties

### code

code: string
Inherited from [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error).[code](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error#code)  
Unique error code.

### Optional credential

credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)
Inherited from [AuthError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError).[credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#credential)  
The [firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) that can be used to resolve the
error.

### Optional email

email: string
Inherited from [AuthError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError).[email](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#email)  
The email of the user's account used for sign-in/linking.

### message

message: string
Inherited from [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error).[message](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error#message)  
Complete error message.

### Optional phoneNumber

phoneNumber: string
Inherited from [AuthError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError).[phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#phonenumber)  
The phone number of the user's account used for sign-in/linking.

### resolver

resolver: [MultiFactorResolver](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorresolver)  
The multi-factor resolver to complete second factor sign-in.

### Optional tenantId

tenantId: string
Inherited from [AuthError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError).[tenantId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#tenantid)  
The tenant ID being used for sign-in/linking. If you use
{@link firebase.auth.signInWithRedirect} to sign in, you have to
set the tenant ID on Auth instanace again as the tenant ID is not
persisted after redirection.