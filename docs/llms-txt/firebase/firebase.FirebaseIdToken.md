# Source: https://firebase.google.com/docs/reference/node/firebase.FirebaseIdToken.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.FirebaseIdToken.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken.md.txt

# FirebaseIdToken | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- FirebaseIdToken

### Indexable

\[claim: string\]: unknown  
Custom claims set by the developer

## Index

### Properties

- [aud](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#aud)
- [auth_time](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#auth_time)
- [email](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#email)
- [email_verified](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#email_verified)
- [exp](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#exp)
- [firebase](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#firebase)
- [iat](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#iat)
- [iss](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#iss)
- [name](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#name)
- [phone_number](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#phone_number)
- [picture](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#picture)
- [provider_id](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#provider_id)
- [sub](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#sub)
- [uid](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#uid)
- [user_id](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken#user_id)

## Properties

### aud

aud: string  
Always set to PROJECT_ID

### auth_time

auth_time: number  
The time the user authenticated, normally 'iat'

### Optional email

email: string  
The user's primary email

### Optional email_verified

email_verified: boolean  
The user's email verification status

### exp

exp: number  
The token expiry time, normally 'iat' + 3600

### firebase

firebase: { identities?: {}; sign_in_provider: [FirebaseSignInProvider](https://firebase.google.com/docs/reference/js/v8/firebase#firebasesigninprovider) }  
Information on all identities linked to this user  

#### Type declaration

-

  ##### Optional identities?: {}

  A map of providers to the user's list of unique identifiers from each provider
-

  ##### sign_in_provider: [FirebaseSignInProvider](https://firebase.google.com/docs/reference/js/v8/firebase#firebasesigninprovider)

  The primary sign-in provider

### iat

iat: number  
The token issue time, in seconds since epoch

### iss

iss: string  
Always set to <https://securetoken.google.com/PROJECT_ID>

### Optional name

name: string  
The user's display name

### Optional phone_number

phone_number: string  
The user's primary phone number

### Optional picture

picture: string  
The user's profile photo URL

### Optional provider_id

provider_id: "anonymous"  
The sign in provider, only set when the provider is 'anonymous'

### sub

sub: string  
The user's unique ID

### Optional uid

uid: never

### user_id

user_id: string  
The user's unique ID. Must be equal to 'sub'