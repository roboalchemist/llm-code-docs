# Source: https://firebase.google.com/docs/reference/js/database.database.md.txt

# Database class

Class representing a Firebase Realtime Database.

**Signature:**  

    export declare class Database 

## Properties

|                                        Property                                         | Modifiers |                                                 Type                                                  |                                                                        Description                                                                         |
|-----------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/database.database.md#databaseapp)   |           | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with this Realtime Database instance. |
| [type](https://firebase.google.com/docs/reference/js/database.database.md#databasetype) |           | (not declared)                                                                                        | Represents a `Database` instance.                                                                                                                          |

## Database.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with this Realtime Database instance.

**Signature:**  

    readonly app: FirebaseApp;

## Database.type

Represents a `Database` instance.

**Signature:**  

    readonly 'type' = "database";