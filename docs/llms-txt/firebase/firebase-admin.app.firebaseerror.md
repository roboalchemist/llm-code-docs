# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseerror.md.txt

# FirebaseError interface

`FirebaseError` is a subclass of the standard JavaScript `Error` object. In addition to a message string and stack trace, it contains a string code.

**Signature:**  

    export interface FirebaseError 

## Properties

|                                                         Property                                                          |  Type  |                                                                                                                                             Description                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [code](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseerror.md#firebaseerrorcode)       | string | Error codes are strings using the following format: `"service/string-code"`. Some examples include `"auth/invalid-uid"` and `"messaging/invalid-recipient"`.While the message for a given error can change, the code will remain the same between backward-compatible versions of the Firebase SDK. |
| [message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseerror.md#firebaseerrormessage) | string | An explanatory message for the error that just occurred.This message is designed to be helpful to you, the developer. Because it generally does not convey meaningful information to end users, this message should not be displayed in your application.                                           |
| [stack](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseerror.md#firebaseerrorstack)     | string | A string value containing the execution backtrace when the error originally occurred.This information can be useful for troubleshooting the cause of the error with [Firebase Support](https://firebase.google.com/support).                                                                        |

## Methods

|                                                          Method                                                           |                           Description                            |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseerror.md#firebaseerrortojson) | Returns a JSON-serializable object representation of this error. |

## FirebaseError.code

Error codes are strings using the following format: `"service/string-code"`. Some examples include `"auth/invalid-uid"` and `"messaging/invalid-recipient"`.

While the message for a given error can change, the code will remain the same between backward-compatible versions of the Firebase SDK.

**Signature:**  

    code: string;

## FirebaseError.message

An explanatory message for the error that just occurred.

This message is designed to be helpful to you, the developer. Because it generally does not convey meaningful information to end users, this message should not be displayed in your application.

**Signature:**  

    message: string;

## FirebaseError.stack

A string value containing the execution backtrace when the error originally occurred.

This information can be useful for troubleshooting the cause of the error with [Firebase Support](https://firebase.google.com/support).

**Signature:**  

    stack?: string;

## FirebaseError.toJSON()

Returns a JSON-serializable object representation of this error.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.