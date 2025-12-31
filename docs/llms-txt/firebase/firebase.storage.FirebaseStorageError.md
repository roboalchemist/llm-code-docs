# Source: https://firebase.google.com/docs/reference/node/firebase.storage.FirebaseStorageError.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.FirebaseStorageError.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError.md.txt

# FirebaseStorageError | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage).
- FirebaseStorageError

An error returned by the Firebase Storage SDK.

## Index

### Properties

- [code](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError#code)
- [customData](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError#customdata)
- [message](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError#message)
- [name](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError#name)
- [stack](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError#stack)

## Properties

### code

code: string
Inherited from [FirebaseError](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError).[code](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError#code)  
Error codes are strings using the following format: `"service/string-code"`.
Some examples include `"app/no-app"` and `"auth/user-not-found"`.

While the message for a given error can change, the code will remain the same
between backward-compatible versions of the Firebase SDK.

### customData

customData: { serverResponse: string \| null }  
Stores custom error data unique to the `StorageError`.  

#### Type declaration

-

  ##### serverResponse: string \| null

### message

message: string
Inherited from [FirebaseError](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError).[message](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError#message)  
An explanatory message for the error that just occurred.

This message is designed to be helpful to you, the developer. Because
it generally does not convey meaningful information to end users,
this message should not be displayed in your application.

### name

name: "FirebaseError"
Inherited from [FirebaseError](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError).[name](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError#name)  
The name of the class of errors, which is `"FirebaseError"`.

### Optional stack

stack: string
Inherited from [FirebaseError](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError).[stack](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError#stack)  
A string value containing the execution backtrace when the error originally
occurred. This may not always be available.

When it is available, this information can be sent to
[Firebase Support](https://firebase.google.com/support/) to help
explain the cause of an error.