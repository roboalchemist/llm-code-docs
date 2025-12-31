# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GoogleOAuthAccessToken.md.txt

# GoogleOAuthAccessToken

public class **GoogleOAuthAccessToken** extends Object  


**This class was deprecated.**   
Use GoogleCredentials and associated classes.

Represents an OAuth access token, which can be used to access Firebase and other qualified
Google APIs. Encapsulates both the token string, and its expiration time.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [GoogleOAuthAccessToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GoogleOAuthAccessToken#GoogleOAuthAccessToken(java.lang.String, long))(String accessToken, long expiryTime) Create a new GoogleOAuthAccessToken instance |

### Public Method Summary

|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String | [getAccessToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GoogleOAuthAccessToken#getAccessToken())() Returns the JWT access token.                                      |
| long   | [getExpiryTime](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GoogleOAuthAccessToken#getExpiryTime())() Returns the expiration time as a milliseconds since epoch timestamp. |

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

## Public Constructors

#### public
**GoogleOAuthAccessToken**
(String accessToken, long expiryTime)

Create a new GoogleOAuthAccessToken instance  

##### Parameters

| accessToken |                    JWT access token string                     |
| expiryTime  | Time at which the token will expire (milliseconds since epoch) |
|-------------|----------------------------------------------------------------|

##### Throws

| IllegalArgumentException | If the token is null or empty |
|--------------------------|-------------------------------|

## Public Methods

#### public String
**getAccessToken**
()

Returns the JWT access token.  

#### public long
**getExpiryTime**
()

Returns the expiration time as a milliseconds since epoch timestamp.