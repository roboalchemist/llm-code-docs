# Source: https://firebase.google.com/docs/reference/node/firebase.auth.AuthError.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.AuthError.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError.md.txt

# AuthError | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- AuthError

The account conflict error.
Refer to [firebase.auth.Auth.signInWithPopup](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithpopup) for more information.

#### Common Error Codes

auth/account-exists-with-different-credential
:   Thrown if there already exists an account with the email address
    asserted by the credential. Resolve this by calling
    [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail) with the error.email
    and then asking the user to sign in using one of the returned providers.
    Once the user is signed in, the original credential retrieved from the
    error.credential can be linked to the user with
    [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) to prevent the user from signing
    in again to the original provider via popup or redirect. If you are using
    redirects for sign in, save the credential in session storage and then
    retrieve on redirect and repopulate the credential using for example
    [firebase.auth.GoogleAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#credential) depending on the
    credential provider id and complete the link.

auth/credential-already-in-use
:   Thrown if the account corresponding to the credential already exists
    among your users, or is already linked to a Firebase User.
    For example, this error could be thrown if you are upgrading an anonymous
    user to a Google user by linking a Google credential to it and the Google
    credential used is already associated with an existing Firebase Google
    user.
    The fields `error.email`, `error.phoneNumber`, and
    `error.credential` ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential))
    may be provided, depending on the type of credential. You can recover
    from this error by signing in with `error.credential` directly
    via [firebase.auth.Auth.signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential).

auth/email-already-in-use
:   Thrown if the email corresponding to the credential already exists
    among your users. When thrown while linking a credential to an existing
    user, an `error.email` and `error.credential`
    ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)) fields are also provided.
    You have to link the credential to the existing user with that email if
    you wish to continue signing in with that credential. To do so, call
    [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail), sign in to
    `error.email` via one of the providers returned and then
    [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) the original credential to that
    newly signed in user.

## Index

### Properties

- [code](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#code)
- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#credential)
- [email](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#email)
- [message](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#message)
- [name](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#name)
- [phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#phonenumber)
- [tenantId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError#tenantid)

## Properties

### code

code: string
Inherited from [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error).[code](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error#code)  
Unique error code.

### Optional credential

credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)  
The [firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) that can be used to resolve the
error.

### Optional email

email: string  
The email of the user's account used for sign-in/linking.

### message

message: string
Inherited from [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error).[message](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error#message)  
Complete error message.

### name

name: string
| Inherited from [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error).[name](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error#name)

### Optional phoneNumber

phoneNumber: string  
The phone number of the user's account used for sign-in/linking.

### Optional tenantId

tenantId: string  
The tenant ID being used for sign-in/linking. If you use
[firebase.auth.Auth.signInWithRedirect](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithredirect) to sign in, you have to
set the tenant ID on Auth instanace again as the tenant ID is not
persisted after redirection.