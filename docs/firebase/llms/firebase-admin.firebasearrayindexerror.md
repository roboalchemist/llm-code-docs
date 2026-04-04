# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.firebasearrayindexerror.md.txt

# FirebaseArrayIndexError interface

Composite type which includes both a `FirebaseError` object and an index which can be used to get the errored item.

**Signature:**  

    export interface FirebaseArrayIndexError 

## Properties

|                                                               Property                                                                |                                                              Type                                                              |                                           Description                                            |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [error](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firebasearrayindexerror.md#firebasearrayindexerrorerror) | [FirebaseError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firebaseerror.md#firebaseerror_interface) | The error object.                                                                                |
| [index](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firebasearrayindexerror.md#firebasearrayindexerrorindex) | number                                                                                                                         | The index of the errored item within the original array passed as part of the called API method. |

## FirebaseArrayIndexError.error

The error object.

**Signature:**  

    error: FirebaseError;

## FirebaseArrayIndexError.index

The index of the errored item within the original array passed as part of the called API method.

**Signature:**  

    index: number;

### Example

    var registrationTokens = [token1, token2, token3];
    admin.messaging().subscribeToTopic(registrationTokens, 'topic-name')
      .then(function(response) {
        if (response.failureCount > 0) {
          console.log("Following devices unsucessfully subscribed to topic:");
          response.errors.forEach(function(error) {
            var invalidToken = registrationTokens[error.index];
            console.log(invalidToken, error.error);
          });
        } else {
          console.log("All devices successfully subscribed to topic:", response);
        }
      })
      .catch(function(error) {
        console.log("Error subscribing to topic:", error);
      });