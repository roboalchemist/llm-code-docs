# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md.txt

# firestore.NamespaceBuilder class

**Signature:**  

    export declare class NamespaceBuilder 

## Constructors

|                                                                                        Constructor                                                                                        | Modifiers |                        Description                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------|
| [(constructor)(database, options, namespace)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md#firestorenamespacebuilderconstructor) |           | Constructs a new instance of the `NamespaceBuilder` class |

## Methods

|                                                                          Method                                                                           | Modifiers | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|
| [document(path)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md#firestorenamespacebuilderdocument) |           |             |

## firestore.NamespaceBuilder.(constructor)

Constructs a new instance of the `NamespaceBuilder` class

**Signature:**  

    constructor(database: string, options: DeploymentOptions, namespace?: string);

### Parameters

| Parameter |                                                                     Type                                                                      | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| database  | string                                                                                                                                        |             |
| options   | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |
| namespace | string                                                                                                                                        |             |

## firestore.NamespaceBuilder.document()

**Signature:**  

    document<Path extends string>(path: Path): DocumentBuilder<Path>;

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| path      | Path |             |

**Returns:**

[DocumentBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilder_class)\<Path\>