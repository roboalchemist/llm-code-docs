# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md.txt

# Database interface

The Firebase Database service interface. Extends the [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database) interface provided by the `@firebase/database-compat` package.

**Signature:**  

    export interface Database extends FirebaseDatabase 

**Extends:** FirebaseDatabase

## Methods

|                                                              Method                                                              |                                                                       Description                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getRules()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#databasegetrules)         | Gets the currently applied security rules as a string. The return value consists of the rules source including comments.                                |
| [getRulesJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#databasegetrulesjson) | Gets the currently applied security rules as a parsed JSON object. Any comments in the original source are stripped away.                               |
| [setRules(source)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#databasesetrules)   | Sets the specified rules on the Firebase Realtime Database instance. If the rules source is specified as a string or a Buffer, it may include comments. |

## Database.getRules()

Gets the currently applied security rules as a string. The return value consists of the rules source including comments.

**Signature:**  

    getRules(): Promise<string>;

**Returns:**

Promise\<string\>

A promise fulfilled with the rules as a raw string.

## Database.getRulesJSON()

Gets the currently applied security rules as a parsed JSON object. Any comments in the original source are stripped away.

**Signature:**  

    getRulesJSON(): Promise<object>;

**Returns:**

Promise\<object\>

A promise fulfilled with the parsed rules object.

## Database.setRules()

Sets the specified rules on the Firebase Realtime Database instance. If the rules source is specified as a string or a Buffer, it may include comments.

**Signature:**  

    setRules(source: string | Buffer | object): Promise<void>;

### Parameters

| Parameter |            Type            |                        Description                         |
|-----------|----------------------------|------------------------------------------------------------|
| source    | string \| Buffer \| object | Source of the rules to apply. Must not be `null` or empty. |

**Returns:**

Promise\<void\>

Resolves when the rules are set on the Realtime Database.