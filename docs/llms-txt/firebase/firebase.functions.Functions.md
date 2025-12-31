# Source: https://firebase.google.com/docs/reference/js/v8/firebase.functions.Functions.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.functions.Functions.md.txt

# Functions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [functions](https://firebase.google.com/docs/reference/node/firebase.functions).
- Functions

The Cloud Functions for Firebase service interface.

Do not call this constructor directly. Instead, use
[`firebase.functions()`](https://firebase.google.com/docs/reference/node/firebase.functions).

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.functions.Functions#constructor)

### Methods

- [httpsCallable](https://firebase.google.com/docs/reference/node/firebase.functions.Functions#httpscallable)
- [useEmulator](https://firebase.google.com/docs/reference/node/firebase.functions.Functions#useemulator)
- [useFunctionsEmulator](https://firebase.google.com/docs/reference/node/firebase.functions.Functions#usefunctionsemulator)

## Constructors

### Private constructor

- new Functions ( ) : [Functions](https://firebase.google.com/docs/reference/node/firebase.functions.Functions)
-

  #### Returns [Functions](https://firebase.google.com/docs/reference/node/firebase.functions.Functions)

## Methods

### httpsCallable

- httpsCallable ( name : string , options ? : [HttpsCallableOptions](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsCallableOptions) ) : [HttpsCallable](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsCallable)
- Gets an `HttpsCallable` instance that refers to the function with the given
  name.

  #### Parameters

  -

    ##### name: string

    The name of the https callable function.
  -

    ##### Optional options: [HttpsCallableOptions](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsCallableOptions)

    The options for this HttpsCallable instance.

  #### Returns [HttpsCallable](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsCallable)

  The `HttpsCallable` instance.

### useEmulator

- useEmulator ( host : string , port : number ) : void
- Modify this instance to communicate with the Cloud Functions emulator.

  Note: this must be called before this instance has been used to do any operations.

  #### Parameters

  -

    ##### host: string

    The emulator host (ex: localhost)
  -

    ##### port: number

    The emulator port (ex: 5001)

  #### Returns void

### useFunctionsEmulator

- useFunctionsEmulator ( url : string ) : void
-

  deprecated

  :   Prefer the useEmulator(host, port) method.

  Changes this instance to point to a Cloud Functions emulator running
  locally. See <https://firebase.google.com/docs/functions/local-emulator>

  #### Parameters

  -

    ##### url: string

  #### Returns void