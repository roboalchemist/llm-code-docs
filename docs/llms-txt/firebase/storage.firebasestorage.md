# Source: https://firebase.google.com/docs/reference/js/storage.firebasestorage.md.txt

# FirebaseStorage interface

A Firebase Storage instance.

**Signature:**  

    export interface FirebaseStorage extends _FirebaseService 

**Extends:** _FirebaseService

## Properties

|                                                                Property                                                                |                                                 Type                                                  |                                                                        Description                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorageapp)                                     | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with this `FirebaseStorage` instance. |
| [maxOperationRetryTime](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestoragemaxoperationretrytime) | number                                                                                                | The maximum time to retry operations other than uploads or downloads in milliseconds.                                                                      |
| [maxUploadRetryTime](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestoragemaxuploadretrytime)       | number                                                                                                | The maximum time to retry uploads in milliseconds.                                                                                                         |

## FirebaseStorage.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with this `FirebaseStorage` instance.

**Signature:**  

    readonly app: FirebaseApp;

## FirebaseStorage.maxOperationRetryTime

The maximum time to retry operations other than uploads or downloads in milliseconds.

**Signature:**  

    maxOperationRetryTime: number;

## FirebaseStorage.maxUploadRetryTime

The maximum time to retry uploads in milliseconds.

**Signature:**  

    maxUploadRetryTime: number;