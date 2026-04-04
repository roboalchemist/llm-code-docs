# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode.md.txt

# AuthErrorCode

public final enum **AuthErrorCode** extends Enum\<E extends Enum\<E\>\>  
Error codes that can be raised by the Firebase Auth APIs.

### Inherited Method Summary

From class java.lang.Enum

|---|---|
| final Object | clone() |
| final int | compareTo(E arg0) |
| int | compareTo(Object arg0) |
| final boolean | equals(Object arg0) |
| final void | finalize() |
| final Class\<E\> | getDeclaringClass() |
| final int | hashCode() |
| final String | name() |
| final int | ordinal() |
| String | toString() |
| static \<T extends Enum\<T\>\> T | valueOf(Class\<T\> arg0, String arg1) |

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

From interface java.lang.Comparable

|---|---|
| abstract int | compareTo(T arg0) |

## Enum Values

#### public static final AuthErrorCode
**CERTIFICATE_FETCH_FAILED**

Failed to retrieve public key certificates required to verify JWTs.

#### public static final AuthErrorCode
**CONFIGURATION_NOT_FOUND**

No IdP configuration found for the given identifier.

#### public static final AuthErrorCode
**EMAIL_ALREADY_EXISTS**

A user already exists with the provided email.

#### public static final AuthErrorCode
**EMAIL_NOT_FOUND**

No user record found for the given email, typically raised when
generating a password reset link using an email for a user that
is not already registered.

#### public static final AuthErrorCode
**EXPIRED_ID_TOKEN**

The specified ID token is expired.

#### public static final AuthErrorCode
**EXPIRED_SESSION_COOKIE**

The specified session cookie is expired.

#### public static final AuthErrorCode
**INVALID_DYNAMIC_LINK_DOMAIN**

The provided dynamic link domain is not configured or authorized for the current project.

#### public static final AuthErrorCode
**INVALID_HOSTING_LINK_DOMAIN**

The provided hosting link domain is not configured or authorized for the current project.

#### public static final AuthErrorCode
**INVALID_ID_TOKEN**

The specified ID token is invalid.

#### public static final AuthErrorCode
**INVALID_SESSION_COOKIE**

The specified session cookie is invalid.

#### public static final AuthErrorCode
**PHONE_NUMBER_ALREADY_EXISTS**

A user already exists with the provided phone number.

#### public static final AuthErrorCode
**REVOKED_ID_TOKEN**

The specified ID token has been revoked.

#### public static final AuthErrorCode
**REVOKED_SESSION_COOKIE**

The specified session cookie has been revoked.

#### public static final AuthErrorCode
**TENANT_ID_MISMATCH**

Tenant ID in the JWT does not match.

#### public static final AuthErrorCode
**TENANT_NOT_FOUND**

No tenant found for the given identifier.

#### public static final AuthErrorCode
**UID_ALREADY_EXISTS**

A user already exists with the provided UID.

#### public static final AuthErrorCode
**UNAUTHORIZED_CONTINUE_URL**

The domain of the continue URL is not whitelisted. Whitelist the domain in the Firebase
console.

#### public static final AuthErrorCode
**USER_DISABLED**

The user record is disabled.

#### public static final AuthErrorCode
**USER_NOT_FOUND**

No user record found for the given identifier.