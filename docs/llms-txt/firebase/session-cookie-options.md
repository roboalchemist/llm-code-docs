# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/session-cookie-options.md.txt

# FirebaseAdmin.Auth.SessionCookieOptions Class Reference

# FirebaseAdmin.Auth.SessionCookieOptions

Options for the [FirebaseAuth.CreateSessionCookieAsync(string, SessionCookieOptions)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1adc3b86778805979f1936b726940159fb) API.

## Summary

|                                                                                                                                    ### Properties                                                                                                                                    ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [ExpiresIn](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/session-cookie-options#class_firebase_admin_1_1_auth_1_1_session_cookie_options_1aefa156e6092acaba6d1694569d803943) | `TimeSpan` Gets or sets the duration until the cookie is expired. |

## Properties

### ExpiresIn

```text
TimeSpan ExpiresIn
```  
Gets or sets the duration until the cookie is expired.

Must be between 5 minutes and 14 days. The backend service uses seconds precision for this parameter.