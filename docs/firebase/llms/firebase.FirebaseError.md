# Source: https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.FirebaseError.md.txt

# FirebaseError | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- FirebaseError

`FirebaseError` is a subclass of the standard JavaScript `Error` object. In
addition to a message string and stack trace, it contains a string code.

## Index

### Properties

- [code](https://firebase.google.com/docs/reference/node/firebase.FirebaseError#code)
- [message](https://firebase.google.com/docs/reference/node/firebase.FirebaseError#message)
- [name](https://firebase.google.com/docs/reference/node/firebase.FirebaseError#name)
- [stack](https://firebase.google.com/docs/reference/node/firebase.FirebaseError#stack)

## Properties

### code

code: string  
Error codes are strings using the following format: `"service/string-code"`.
Some examples include `"app/no-app"` and `"auth/user-not-found"`.

While the message for a given error can change, the code will remain the same
between backward-compatible versions of the Firebase SDK.

### message

message: string  
An explanatory message for the error that just occurred.

This message is designed to be helpful to you, the developer. Because
it generally does not convey meaningful information to end users,
this message should not be displayed in your application.

### name

name: "FirebaseError"  
The name of the class of errors, which is `"FirebaseError"`.

### Optional stack

stack: string  
A string value containing the execution backtrace when the error originally
occurred. This may not always be available.

When it is available, this information can be sent to
[Firebase Support](https://firebase.google.com/support/) to help
explain the cause of an error.