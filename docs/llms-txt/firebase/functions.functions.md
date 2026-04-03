# Source: https://firebase.google.com/docs/reference/js/functions.functions.md.txt

# Functions interface

A `Functions` instance.

**Signature:**  

    export interface Functions 

## Properties

|                                                  Property                                                  |                                                 Type                                                  |                                                                       Description                                                                       |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/functions.functions.md#functionsapp)                   | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this `Functions` instance is associated with. |
| [customDomain](https://firebase.google.com/docs/reference/js/functions.functions.md#functionscustomdomain) | string \| null                                                                                        | A custom domain hosting the callable Cloud Functions. ex: https://mydomain.com                                                                          |
| [region](https://firebase.google.com/docs/reference/js/functions.functions.md#functionsregion)             | string                                                                                                | The region the callable Cloud Functions are located in. Default is `us-central-1`.                                                                      |

## Functions.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this `Functions` instance is associated with.

**Signature:**  

    app: FirebaseApp;

## Functions.customDomain

A custom domain hosting the callable Cloud Functions. ex: https://mydomain.com

**Signature:**  

    customDomain: string | null;

## Functions.region

The region the callable Cloud Functions are located in. Default is `us-central-1`.

**Signature:**  

    region: string;