# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeURL.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL.md.txt

# ActionCodeURL | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [auth](https://firebase.google.com/docs/reference/node/firebase.auth).
- ActionCodeURL

A utility class to parse email action URLs.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#constructor)

### Properties

- [apiKey](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#apikey)
- [code](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#code)
- [continueUrl](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#continueurl)
- [languageCode](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#languagecode)
- [operation](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#operation)
- [tenantId](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#tenantid)

### Methods

- [parseLink](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL#parselink)

## Constructors

### Private constructor

- new ActionCodeURL ( ) : [ActionCodeURL](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL)
-

  #### Returns [ActionCodeURL](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL)

## Properties

### apiKey

apiKey: string  
The API key of the email action link.

### code

code: string  
The action code of the email action link.

### continueUrl

continueUrl: string \| null  
The continue URL of the email action link. Null if not provided.

### languageCode

languageCode: string \| null  
The language code of the email action link. Null if not provided.

### operation

operation: [Operation](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeInfo#operation)  
The action performed by the email action link. It returns from one
of the types from [firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeInfo).

### tenantId

tenantId: string \| null  
The tenant ID of the email action link. Null if the email action
is from the parent project.

## Methods

### Static parseLink

- parseLink ( link : string ) : [ActionCodeURL](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL) \| null
- Parses the email action link string and returns an ActionCodeURL object
  if the link is valid, otherwise returns null.

  #### Parameters

  -

    ##### link: string

    The email action link string.

  #### Returns [ActionCodeURL](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL) \| null

The ActionCodeURL object, or null if the link is invalid.