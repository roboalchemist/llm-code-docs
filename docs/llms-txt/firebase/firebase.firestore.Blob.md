# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Blob.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob.md.txt

# Blob | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- Blob

An immutable object representing an array of bytes.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob#constructor)

### Methods

- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob#isequal)
- [toBase64](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob#tobase64)
- [toUint8Array](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob#touint8array)
- [fromBase64String](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob#frombase64string)
- [fromUint8Array](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob#fromuint8array)

## Constructors

### Private constructor

- new Blob ( ) : [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)
-

  #### Returns [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)

## Methods

### isEqual

- isEqual ( other : [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob) ) : boolean
- Returns true if this `Blob` is equal to the provided one.

  #### Parameters

  -

    ##### other: [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)

    The `Blob` to compare against.

  #### Returns boolean

  true if this `Blob` is equal to the provided one.

### toBase64

- toBase64 ( ) : string
- Returns the bytes of a Blob as a Base64-encoded string.

  #### Returns string

  The Base64-encoded string created from the Blob object.

### toUint8Array

- toUint8Array ( ) : Uint8Array
- Returns the bytes of a Blob in a new Uint8Array.

  #### Returns Uint8Array

  The Uint8Array created from the Blob object.

### Static fromBase64String

- fromBase64String ( base64 : string ) : [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)
- Creates a new Blob from the given Base64 string, converting it to
  bytes.

  #### Parameters

  -

    ##### base64: string

    The Base64 string used to create the Blob object.

  #### Returns [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)

### Static fromUint8Array

- fromUint8Array ( array : Uint8Array ) : [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)
- Creates a new Blob from the given Uint8Array.

  #### Parameters

  -

    ##### array: Uint8Array

    The Uint8Array used to create the Blob object.

  #### Returns [Blob](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Blob)