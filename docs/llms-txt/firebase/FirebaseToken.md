# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken.md.txt

# FirebaseToken

public final class **FirebaseToken** extends Object  
A decoded and verified Firebase token. Can be used to get the uid and other user attributes
available in the token. See [verifyIdToken(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String)) and
[verifySessionCookie(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String)) for details on how to obtain an instance of
this class.  

### Public Method Summary

|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map\<String, Object\> | [getClaims](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getClaims())() Returns a map of all of the claims on this token.                                                                                                                                                                 |
| String                | [getEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getEmail())() Returns the e-mail address for this user, or `null` if it's unavailable.                                                                                                                                            |
| String                | [getIssuer](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getIssuer())() Returns the Issuer for this token.                                                                                                                                                                                |
| String                | [getName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getName())() Returns the user's display name.                                                                                                                                                                                      |
| String                | [getPicture](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getPicture())() Returns the Uri string of the user's profile photo.                                                                                                                                                             |
| String                | [getTenantId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getTenantId())() Returns the tenant ID for this token.                                                                                                                                                                         |
| String                | [getUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getUid())() Returns the Uid for this token.                                                                                                                                                                                         |
| boolean               | [isEmailVerified](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#isEmailVerified())() Indicates if the email address returned by [getEmail()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getEmail()) has been verified as good. |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public Map\<String, Object\>
**getClaims**
()

Returns a map of all of the claims on this token.  

#### public String
**getEmail**
()

Returns the e-mail address for this user, or `null` if it's unavailable.  

#### public String
**getIssuer**
()

Returns the Issuer for this token.  

#### public String
**getName**
()

Returns the user's display name.  

#### public String
**getPicture**
()

Returns the Uri string of the user's profile photo.  

#### public String
**getTenantId**
()

Returns the tenant ID for this token.  

#### public String
**getUid**
()

Returns the Uid for this token.  

#### public boolean
**isEmailVerified**
()

Indicates if the email address returned by [getEmail()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken#getEmail()) has been verified as good.