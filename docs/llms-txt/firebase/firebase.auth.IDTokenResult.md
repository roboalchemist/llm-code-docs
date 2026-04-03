# Source: https://firebase.google.com/docs/reference/node/firebase.auth.IDTokenResult.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult.md.txt

# IdTokenResult | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- IdTokenResult

Interface representing ID token result obtained from
[firebase.User.getIdTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.User#getidtokenresult). It contains the ID token JWT string
and other helper properties for getting different data associated with the
token as well as all the decoded payload claims.

Note that these claims are not to be trusted as they are parsed client side.
Only server side verification can guarantee the integrity of the token
claims.

## Index

### Properties

- [authTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#authtime)
- [claims](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#claims)
- [expirationTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#expirationtime)
- [issuedAtTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#issuedattime)
- [signInProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#signinprovider)
- [signInSecondFactor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#signinsecondfactor)
- [token](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult#token)

## Properties

### authTime

authTime: string  
The authentication time formatted as a UTC string. This is the time the
user authenticated (signed in) and not the time the token was refreshed.

### claims

claims: {}  
The entire payload claims of the ID token including the standard reserved
claims as well as the custom claims.  

#### Type declaration

-

  ##### \[key: string\]: any

### expirationTime

expirationTime: string  
The ID token expiration time formatted as a UTC string.

### issuedAtTime

issuedAtTime: string  
The ID token issued at time formatted as a UTC string.

### signInProvider

signInProvider: string \| null  
The sign-in provider through which the ID token was obtained (anonymous,
custom, phone, password, etc). Note, this does not map to provider IDs.

### signInSecondFactor

signInSecondFactor: string \| null  
The type of second factor associated with this session, provided the user
was multi-factor authenticated (eg. phone, etc).

### token

token: string  
The Firebase Auth ID token JWT string.