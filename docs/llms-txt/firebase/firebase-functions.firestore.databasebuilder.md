# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md.txt

# firestore.DatabaseBuilder class

**Signature:**  

    export declare class DatabaseBuilder 

## Constructors

|                                                                                 Constructor                                                                                  | Modifiers |                       Description                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(database, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md#firestoredatabasebuilderconstructor) |           | Constructs a new instance of the `DatabaseBuilder` class |

## Methods

|                                                                             Method                                                                             | Modifiers | Description |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|
| [document(path)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md#firestoredatabasebuilderdocument)        |           |             |
| [namespace(namespace)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md#firestoredatabasebuildernamespace) |           |             |

## firestore.DatabaseBuilder.(constructor)

Constructs a new instance of the `DatabaseBuilder` class

**Signature:**  

    constructor(database: string, options: DeploymentOptions);

### Parameters

| Parameter |                                                                     Type                                                                      | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| database  | string                                                                                                                                        |             |
| options   | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## firestore.DatabaseBuilder.document()

**Signature:**  

    document<Path extends string>(path: Path): DocumentBuilder<Path>;

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| path      | Path |             |

**Returns:**

[DocumentBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilder_class)\<Path\>

## firestore.DatabaseBuilder.namespace()

**Signature:**  

    namespace(namespace: string): NamespaceBuilder;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| namespace | string |             |

**Returns:**

[NamespaceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md#firestorenamespacebuilder_class)