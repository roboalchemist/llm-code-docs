# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.database.instancebuilder.md.txt

# database.InstanceBuilder class

The Firebase Realtime Database instance builder interface.

Access via \[`database.instance()`\](providers_database_.html#instance).

**Signature:**

    export declare class InstanceBuilder 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(instance, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.instancebuilder.md#databaseinstancebuilderconstructor) |   | Constructs a new instance of the `InstanceBuilder` class |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [ref(path)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.instancebuilder.md#databaseinstancebuilderref) |   |   |

## database.InstanceBuilder.(constructor)

Constructs a new instance of the `InstanceBuilder` class

**Signature:**

    constructor(instance: string, options: DeploymentOptions);

### Parameters

| Parameter | Type | Description |
|---|---|---|
| instance | string |   |
| options | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |   |

## database.InstanceBuilder.ref()

**Signature:**

    ref<Ref extends string>(path: Ref): RefBuilder<Ref>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| path | Ref |   |

**Returns:**

[RefBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilder_class)\<Ref\>

Firebase Realtime Database reference builder interface.