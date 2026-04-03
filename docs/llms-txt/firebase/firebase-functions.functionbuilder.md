# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md.txt

# FunctionBuilder class

**Signature:**  

    export declare class FunctionBuilder 

## Constructors

|                                                                   Constructor                                                                   | Modifiers |                       Description                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(options)](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderconstructor) |           | Constructs a new instance of the `FunctionBuilder` class |

## Properties

|                                                                Property                                                                | Modifiers |                                                                                                                                                                                                                                                                                                                                                                                                             Type                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [analytics](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderanalytics)       |           | { event: (analyticsEventType: string) =\> [analytics.AnalyticsEventBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder.md#analyticsanalyticseventbuilder_class); }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| [auth](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderauth)                 |           | { user: (userOptions?: [auth.UserOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.useroptions.md#authuseroptions_interface)) =\> [auth.UserBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilder_class); }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| [database](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderdatabase)         |           | { instance: (instance: string) =\> [database.InstanceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.instancebuilder.md#databaseinstancebuilder_class); ref: \<Ref extends string\>(path: Ref) =\> [database.RefBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilder_class)\<Ref\>; }                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
| [firestore](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderfirestore)       |           | { document: \<Path extends string\>(path: Path) =\> [firestore.DocumentBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilder_class)\<Path\>; namespace: (namespace: string) =\> [firestore.NamespaceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md#firestorenamespacebuilder_class); database: (database: string) =\> [firestore.DatabaseBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md#firestoredatabasebuilder_class); }                                                                                                                                                                                    |             |
| [https](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderhttps)               |           | { onRequest: (handler: (req: https.Request, resp: express.Response) =\> void \| Promise\<void\>) =\> import("./cloud-functions").[HttpsFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction_interface); onCall: (handler: (data: any, context: [https.CallableContext](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontext_interface)) =\> any \| Promise\<any\>) =\> import("./cloud-functions").[HttpsFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction_interface) \& import("./cloud-functions").[Runnable](https://firebase.google.com/docs/reference/functions/firebase-functions.runnable.md#runnable_interface)\<any\>; } |             |
| [pubsub](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderpubsub)             |           | { topic: (topic: string) =\> [pubsub.TopicBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder.md#pubsubtopicbuilder_class); schedule: (schedule: string) =\> [pubsub.ScheduleBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilder_class); }                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| [remoteConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderremoteconfig) |           | { onUpdate: (handler: (version: [remoteConfig.TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any) =\> import("./cloud-functions").[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[remoteConfig.TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface)\>; }                                                                                  |             |
| [storage](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderstorage)           |           | { bucket: (bucket?: string) =\> [storage.BucketBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.bucketbuilder.md#storagebucketbuilder_class); object: () =\> [storage.ObjectBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilder_class); }                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             |
| [tasks](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuildertasks)               |           | { taskQueue: (options?: [tasks.TaskQueueOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptions_interface)) =\> [tasks.TaskQueueBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuebuilder.md#taskstaskqueuebuilder_class); }                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |             |
| [testLab](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuildertestlab)           |           | { testMatrix: () =\> [testLab.TestMatrixBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrixbuilder.md#testlabtestmatrixbuilder_class); }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |

## Methods

|                                                                    Method                                                                    | Modifiers |                       Description                       |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------|
| [region(regions)](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderregion)          |           | Configure the regions that the function is deployed to. |
| [runWith(runtimeOptions)](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilderrunwith) |           | Configure runtime options for the function.             |

## FunctionBuilder.(constructor)

Constructs a new instance of the `FunctionBuilder` class

**Signature:**  

    constructor(options: DeploymentOptions);

### Parameters

| Parameter |                                                                     Type                                                                      | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| options   | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## FunctionBuilder.analytics

**Signature:**  

    get analytics(): {
            event: (analyticsEventType: string) => analytics.AnalyticsEventBuilder;
        };

## FunctionBuilder.auth

**Signature:**  

    get auth(): {
            user: (userOptions?: auth.UserOptions) => auth.UserBuilder;
        };

## FunctionBuilder.database

**Signature:**  

    get database(): {
            instance: (instance: string) => database.InstanceBuilder;
            ref: <Ref extends string>(path: Ref) => database.RefBuilder<Ref>;
        };

## FunctionBuilder.firestore

**Signature:**  

    get firestore(): {
            document: <Path extends string>(path: Path) => firestore.DocumentBuilder<Path>;
            namespace: (namespace: string) => firestore.NamespaceBuilder;
            database: (database: string) => firestore.DatabaseBuilder;
        };

## FunctionBuilder.https

**Signature:**  

    get https(): {
            onRequest: (handler: (req: https.Request, resp: express.Response) => void | Promise<void>) => import("./cloud-functions").HttpsFunction;
            onCall: (handler: (data: any, context: https.CallableContext) => any | Promise<any>) => import("./cloud-functions").HttpsFunction & import("./cloud-functions").Runnable<any>;
        };

## FunctionBuilder.pubsub

**Signature:**  

    get pubsub(): {
            topic: (topic: string) => pubsub.TopicBuilder;
            schedule: (schedule: string) => pubsub.ScheduleBuilder;
        };

## FunctionBuilder.remoteConfig

**Signature:**  

    get remoteConfig(): {
            onUpdate: (handler: (version: remoteConfig.TemplateVersion, context: EventContext) => PromiseLike<any> | any) => import("./cloud-functions").CloudFunction<remoteConfig.TemplateVersion>;
        };

## FunctionBuilder.storage

**Signature:**  

    get storage(): {
            bucket: (bucket?: string) => storage.BucketBuilder;
            object: () => storage.ObjectBuilder;
        };

## FunctionBuilder.tasks

**Signature:**  

    get tasks(): {
            taskQueue: (options?: tasks.TaskQueueOptions) => tasks.TaskQueueBuilder;
        };

## FunctionBuilder.testLab

**Signature:**  

    get testLab(): {
            testMatrix: () => testLab.TestMatrixBuilder;
        };

## FunctionBuilder.region()

Configure the regions that the function is deployed to.

**Signature:**  

    region(...regions: Array<(typeof SUPPORTED_REGIONS)[number] | string | Expression<string> | ResetValue>): FunctionBuilder;

### Parameters

| Parameter |                                                                                                                                                         Type                                                                                                                                                         |         Description         |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| regions   | Array\<(typeof [SUPPORTED_REGIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#supported_regions))\[number\] \| string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue\> | One or more region strings. |

**Returns:**

[FunctionBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilder_class)

### Example 1

functions.region('us-east1')

### Example 2

functions.region('us-east1', 'us-central1')

## FunctionBuilder.runWith()

Configure runtime options for the function.

**Signature:**  

    runWith(runtimeOptions: RuntimeOptions): FunctionBuilder;

### Parameters

|   Parameter    |                                                                 Type                                                                 |                                                                                                                                                                                                                                                                                                         Description                                                                                                                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| runtimeOptions | [RuntimeOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptions_interface) | Object with optional fields: 1. `memory`: amount of memory to allocate to the function, possible values are: '128MB', '256MB', '512MB', '1GB', '2GB', '4GB', and '8GB'. 2. `timeoutSeconds`: timeout for the function in seconds, possible values are 0 to 540. 3. `failurePolicy`: failure policy of the function, with boolean `true` being equivalent to providing an empty retry object. 4. `vpcConnector`: id of a VPC connector in the same project and region 5. `vpcConnectorEgressSettings`: when a `vpcConnector` is set, control which egress traffic is sent through the `vpcConnector`.Value must not be null. |

**Returns:**

[FunctionBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilder_class)