# Source: https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md.txt

A test context that represents a client. Can be used to access emulators for rules unit testing.

<br />

**Signature:**  

    export interface RulesTestContext 

## Methods

|                                                                                Method                                                                                 |                                                                                                                                                                                        Description                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [database(databaseURL)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontextdatabase) | Get a[Database](https://firebase.google.com/docs/reference/js/database.database#database_class)instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).See:[Database](https://firebase.google.com/docs/reference/js/database.database#database_class)                                                 |
| [firestore(settings)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontextfirestore)  | Get a[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore#firestore_class)instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).See:[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore#firestore_class)                                       |
| [storage(bucketUrl)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontextstorage)     | Get a[FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage#firebasestorage_interface)instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).See:[FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage#firebasestorage_interface) |

## RulesTestContext.database()

Get a[Database](https://firebase.google.com/docs/reference/js/database.database#database_class)instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).

See:[Database](https://firebase.google.com/docs/reference/js/database.database#database_class)

**Signature:**  

    database(databaseURL?: string): firebase.database.Database;

### Parameters

|  Parameter  |  Type  |                                                                       Description                                                                        |
|-------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| databaseURL | string | the URL of the Realtime Database instance. If specified, returns an instance for an emulated version of the namespace with parameters extracted from URL |

**Returns:**

firebase.database.Database

a`Database`instance configured to connect to the emulator. It never connects to production even if a production`databaseURL`is specified

## RulesTestContext.firestore()

Get a[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore#firestore_class)instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).

See:[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore#firestore_class)

**Signature:**  

    firestore(settings?: firebase.firestore.Settings): firebase.firestore.Firestore;

### Parameters

| Parameter |            Type             |                                                                Description                                                                |
|-----------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| settings  | firebase.firestore.Settings | a settings object to configure the[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore#firestore_class)instance |

**Returns:**

firebase.firestore.Firestore

a`Firestore`instance configured to connect to the emulator

## RulesTestContext.storage()

Get a[FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage#firebasestorage_interface)instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).

See:[FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage#firebasestorage_interface)

**Signature:**  

    storage(bucketUrl?: string): firebase.storage.Storage;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| bucketUrl | string |             |

**Returns:**

firebase.storage.Storage

a`Storage`instance configured to connect to the emulator