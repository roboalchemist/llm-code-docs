# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/email-auth-provider.md.txt

# firebase::auth::EmailAuthProvider Class Reference

# firebase::auth::EmailAuthProvider


`#include <credential.h>`

Use email and password to authenticate.

## Summary

Allows developers to use the email and password credentials as they could other auth providers. For example, this can be used to change passwords, log in, etc.

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/email-auth-provider#classfirebase_1_1auth_1_1_email_auth_provider_1ae0e30d0da0a4bf9059e6d3c277574f41` | `const char *const` The string used to identify this provider. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/email-auth-provider#classfirebase_1_1auth_1_1_email_auth_provider_1a7d86709d38b24e4923024e243d112aaa(const char *email, const char *password)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential from the given email and password. |

## Public static attributes

### kProviderId

```c++
const char *const kProviderId
```
The string used to identify this provider.

## Public static functions

### GetCredential

```c++
Credential GetCredential(
  const char *email,
  const char *password
)
```
Generate a credential from the given email and password.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `email` | E-mail to generate the credential from. | | `password` | Password to use for the new credential. | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |