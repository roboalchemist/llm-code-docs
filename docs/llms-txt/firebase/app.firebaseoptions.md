# Source: https://firebase.google.com/docs/reference/js/app.firebaseoptions.md.txt

# FirebaseOptions interface

Firebase configuration object. Contains a set of parameters required by services in order to successfully communicate with Firebase server APIs and to associate client data with your Firebase project and Firebase application. Typically this object is populated by the Firebase console at project setup. See also: [Learn about the Firebase config object](https://firebase.google.com/docs/web/setup#config-object).

**Signature:**  

    export interface FirebaseOptions 

## Properties

|                                                          Property                                                          |  Type  |                                                                            Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [apiKey](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsapikey)                       | string | An encrypted string used when calling certain APIs that don't need to access private user data (example value: `AIzaSyDOCAbC123dEf456GhI789jKl012-MnO`).          |
| [appId](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsappid)                         | string | Unique identifier for the app.                                                                                                                                    |
| [authDomain](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsauthdomain)               | string | Auth domain for the project ID.                                                                                                                                   |
| [databaseURL](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsdatabaseurl)             | string | Default Realtime Database URL.                                                                                                                                    |
| [measurementId](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsmeasurementid)         | string | An ID automatically created when you enable Analytics in your Firebase project and register a web app. In versions 7.20.0 and higher, this parameter is optional. |
| [messagingSenderId](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsmessagingsenderid) | string | Unique numerical value used to identify each sender that can send Firebase Cloud Messaging messages to client apps.                                               |
| [projectId](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsprojectid)                 | string | The unique identifier for the project across all of Firebase and Google Cloud.                                                                                    |
| [storageBucket](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptionsstoragebucket)         | string | The default Cloud Storage bucket name.                                                                                                                            |

## FirebaseOptions.apiKey

An encrypted string used when calling certain APIs that don't need to access private user data (example value: `AIzaSyDOCAbC123dEf456GhI789jKl012-MnO`).

**Signature:**  

    apiKey?: string;

## FirebaseOptions.appId

Unique identifier for the app.

**Signature:**  

    appId?: string;

## FirebaseOptions.authDomain

Auth domain for the project ID.

**Signature:**  

    authDomain?: string;

## FirebaseOptions.databaseURL

Default Realtime Database URL.

**Signature:**  

    databaseURL?: string;

## FirebaseOptions.measurementId

An ID automatically created when you enable Analytics in your Firebase project and register a web app. In versions 7.20.0 and higher, this parameter is optional.

**Signature:**  

    measurementId?: string;

## FirebaseOptions.messagingSenderId

Unique numerical value used to identify each sender that can send Firebase Cloud Messaging messages to client apps.

**Signature:**  

    messagingSenderId?: string;

## FirebaseOptions.projectId

The unique identifier for the project across all of Firebase and Google Cloud.

**Signature:**  

    projectId?: string;

## FirebaseOptions.storageBucket

The default Cloud Storage bucket name.

**Signature:**  

    storageBucket?: string;