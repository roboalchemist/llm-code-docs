# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.firestoresettings.md.txt

# FirestoreSettings interface

Settings to pass to the Firestore constructor.

**Signature:**  

    export interface FirestoreSettings 

## Properties

|                                                                   Property                                                                    |  Type   |                                                                                                                                                                                                        Description                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [preferRest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.firestoresettings.md#firestoresettingspreferrest) | boolean | Use HTTP/1.1 REST transport where possible.`preferRest` will force the use of HTTP/1.1 REST transport until a method that requires gRPC is called. When a method requires gRPC, this Firestore client will load dependent gRPC libraries and then use gRPC transport for all communication from that point forward. Currently the only operation that requires gRPC is creating a snapshot listener using `onSnapshot()`. |

## FirestoreSettings.preferRest

Use HTTP/1.1 REST transport where possible.

`preferRest` will force the use of HTTP/1.1 REST transport until a method that requires gRPC is called. When a method requires gRPC, this Firestore client will load dependent gRPC libraries and then use gRPC transport for all communication from that point forward. Currently the only operation that requires gRPC is creating a snapshot listener using `onSnapshot()`.

**Signature:**  

    preferRest?: boolean;