# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.md.txt

## Functions

|                                                          Function                                                          |                                                                                   Description                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [firebaseConfig()](https://firebase.google.com/docs/reference/functions/firebase-functions.md#firebaseconfig)              | Get the fields you need to initialize a Firebase app                                                                                                                            |
| [onInit(callback)](https://firebase.google.com/docs/reference/functions/firebase-functions.md#oninit)                      | Registers a callback that should be run when in a production environment before executing any functions code. Calling this function more than once leads to undefined behavior. |
| [optionsToEndpoint(options)](https://firebase.google.com/docs/reference/functions/firebase-functions.md#optionstoendpoint) |                                                                                                                                                                                 |
| [optionsToTrigger(options)](https://firebase.google.com/docs/reference/functions/firebase-functions.md#optionstotrigger)   |                                                                                                                                                                                 |
| [region(regions)](https://firebase.google.com/docs/reference/functions/firebase-functions.md#region)                       | Configure the regions that the function is deployed to.                                                                                                                         |
| [runWith(runtimeOptions)](https://firebase.google.com/docs/reference/functions/firebase-functions.md#runwith)              | Configure runtime options for the function.                                                                                                                                     |

## Classes

|                                                                Class                                                                |                                                                                                       Description                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)                            | The Cloud Functions interface for events that change state, such as Realtime Database or Cloud Firestore`onWrite`and`onUpdate`events.For more information about the format used to construct`Change`objects, see below. |
| [FunctionBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilder_class) |                                                                                                                                                                                                                         |

## Interfaces

|                                                                         Interface                                                                         |                                                                                                              Description                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BlockingFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction_interface)                | The function type for Auth Blocking triggers.                                                                                                                                                                                          |
| [CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)                         | The function type for all non-HTTPS triggers. This should be exported from your JavaScript file to define a Cloud Function.This type is a special JavaScript function which takes a templated`LegacyEvent`object as its only argument. |
| [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface)             | Configuration options for a function that applies during function deployment.                                                                                                                                                          |
| [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)                            | The context in which an event occurred.                                                                                                                                                                                                |
| [EventContextAuthToken](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtoken_interface) | https://firebase.google.com/docs/reference/security/database#authtoken                                                                                                                                                                 |
| [FailurePolicy](https://firebase.google.com/docs/reference/functions/firebase-functions.failurepolicy.md#failurepolicy_interface)                         | Configuration option for failure policy on background functions.                                                                                                                                                                       |
| [HttpsFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction_interface)                         | The function type for HTTPS triggers. This should be exported from your JavaScript file to define a Cloud Function.                                                                                                                    |
| [LegacyEvent](https://firebase.google.com/docs/reference/functions/firebase-functions.legacyevent.md#legacyevent_interface)                               | Wire format for an event.                                                                                                                                                                                                              |
| [Resource](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resource_interface)                                        | Resource is a standard format for defining a resource (google.rpc.context.AttributeContext.Resource). In Cloud Functions, it is the resource that triggered the function - such as a storage bucket.                                   |
| [Runnable](https://firebase.google.com/docs/reference/functions/firebase-functions.runnable.md#runnable_interface)                                        | A Runnable has a`run`method which directly invokes the user-defined function - useful for unit testing.                                                                                                                                |
| [RuntimeOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptions_interface)                      | Configuration options for a function that applicable at runtime.                                                                                                                                                                       |
| [Schedule](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#schedule_interface)                                        | Configuration options for scheduled functions.                                                                                                                                                                                         |
| [ScheduleRetryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfig_interface)       | Scheduler retry options. Applies only to scheduled functions.                                                                                                                                                                          |

## Namespaces

|                                                           Namespace                                                            | Description |
|--------------------------------------------------------------------------------------------------------------------------------|-------------|
| [analytics](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.md#analytics_namespace)          |             |
| [auth](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#auth_namespace)                         |             |
| [database](https://firebase.google.com/docs/reference/functions/firebase-functions.database.md#database_namespace)             |             |
| [firestore](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestore_namespace)          |             |
| [https](https://firebase.google.com/docs/reference/functions/firebase-functions.https.md#https_namespace)                      |             |
| [logger](https://firebase.google.com/docs/reference/functions/firebase-functions.logger.md#logger_namespace)                   |             |
| [params](https://firebase.google.com/docs/reference/functions/firebase-functions.params.md#params_namespace)                   |             |
| [pubsub](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.md#pubsub_namespace)                   |             |
| [remoteConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.md#remoteconfig_namespace) |             |
| [storage](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.md#storage_namespace)                |             |
| [tasks](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.md#tasks_namespace)                      |             |
| [testLab](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.md#testlab_namespace)                |             |

## Variables

|                                                               Variable                                                                |                               Description                               |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/functions/firebase-functions.md#app)                                                 |                                                                         |
| [config](https://firebase.google.com/docs/reference/functions/firebase-functions.md#config)                                           |                                                                         |
| [DEFAULT_FAILURE_POLICY](https://firebase.google.com/docs/reference/functions/firebase-functions.md#default_failure_policy)           |                                                                         |
| [INGRESS_SETTINGS_OPTIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#ingress_settings_options)       | List of available options for IngressSettings.                          |
| [MAX_NUMBER_USER_LABELS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#max_number_user_labels)           |                                                                         |
| [MAX_TIMEOUT_SECONDS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#max_timeout_seconds)                 | Cloud Functions max timeout value.                                      |
| [MIN_TIMEOUT_SECONDS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#min_timeout_seconds)                 | Cloud Functions min timeout value.                                      |
| [RESET_VALUE](https://firebase.google.com/docs/reference/functions/firebase-functions.md#reset_value)                                 | Special configuration value to reset configuration to platform default. |
| [SUPPORTED_REGIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#supported_regions)                     | List of all regions supported by Cloud Functions.                       |
| [VALID_MEMORY_OPTIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#valid_memory_options)               | List of available memory options supported by Cloud Functions.          |
| [VPC_EGRESS_SETTINGS_OPTIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#vpc_egress_settings_options) | List of available options for VpcConnectorEgressSettings.               |

## firebaseConfig()

Get the fields you need to initialize a Firebase app

**Signature:**  

    export declare function firebaseConfig(): AppOptions | null;

**Returns:**

AppOptions \| null

## onInit()

Registers a callback that should be run when in a production environment before executing any functions code. Calling this function more than once leads to undefined behavior.

**Signature:**  

    export declare function onInit(callback: () => unknown): void;

### Parameters

| Parameter |      Type      |                           Description                           |
|-----------|----------------|-----------------------------------------------------------------|
| callback  | () =\> unknown | initialization callback to be run before any function executes. |

**Returns:**

void

## optionsToEndpoint()

**Signature:**  

    export declare function optionsToEndpoint(options: DeploymentOptions): ManifestEndpoint;

### Parameters

| Parameter |                                                                     Type                                                                      | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| options   | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

**Returns:**

ManifestEndpoint

## optionsToTrigger()

**Signature:**  

    export declare function optionsToTrigger(options: DeploymentOptions): any;

### Parameters

| Parameter |                                                                     Type                                                                      | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| options   | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

**Returns:**

any

## region()

Configure the regions that the function is deployed to.

**Signature:**  

    export declare function region(...regions: Array<(typeof SUPPORTED_REGIONS)[number] | string | Expression<string> | ResetValue>): FunctionBuilder;

### Parameters

| Parameter |                                                                                                                                                        Type                                                                                                                                                        |         Description         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| regions   | Array\<(typeof[SUPPORTED_REGIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#supported_regions))\[number\] \| string \|[Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue\> | One of more region strings. |

**Returns:**

[FunctionBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilder_class)

### Example 1

functions.region('us-east1')

### Example 2

functions.region('us-east1', 'us-central1')

## runWith()

Configure runtime options for the function.

**Signature:**  

    export declare function runWith(runtimeOptions: RuntimeOptions): FunctionBuilder;

### Parameters

|   Parameter    |                                                                 Type                                                                 |                                                                                                                                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| runtimeOptions | [RuntimeOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptions_interface) | Object with optional fields: 1.`memory`: amount of memory to allocate to the function, possible values are: '128MB', '256MB', '512MB', '1GB', '2GB', '4GB', and '8GB'. 2.`timeoutSeconds`: timeout for the function in seconds, possible values are 0 to 540. 3.`failurePolicy`: failure policy of the function, with boolean`true`being equivalent to providing an empty retry object. 4.`vpcConnector`: id of a VPC connector in same project and region. 5.`vpcConnectorEgressSettings`: when a vpcConnector is set, control which egress traffic is sent through the vpcConnector. 6.`serviceAccount`: Specific service account for the function. 7.`ingressSettings`: ingress settings for the function, which control where a HTTPS function can be called from.Value must not be null. |

**Returns:**

[FunctionBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder.md#functionbuilder_class)

## app

**Signature:**  

    app: {
        setEmulatedAdminApp: typeof setEmulatedAdminApp;
    }

## config

> | **Warning:** This API is now obsolete.
>
> `functions.config()`has been removed in firebase-functions v7. Migrate to environment parameters using the`params`module immediately. Migration guide: https://firebase.google.com/docs/functions/config-env#migrate-config

**Signature:**  

    config: never

## DEFAULT_FAILURE_POLICY

**Signature:**  

    DEFAULT_FAILURE_POLICY: FailurePolicy

## INGRESS_SETTINGS_OPTIONS

List of available options for IngressSettings.

**Signature:**  

    INGRESS_SETTINGS_OPTIONS: readonly ["INGRESS_SETTINGS_UNSPECIFIED", "ALLOW_ALL", "ALLOW_INTERNAL_ONLY", "ALLOW_INTERNAL_AND_GCLB"]

## MAX_NUMBER_USER_LABELS

**Signature:**  

    MAX_NUMBER_USER_LABELS = 58

## MAX_TIMEOUT_SECONDS

Cloud Functions max timeout value.

**Signature:**  

    MAX_TIMEOUT_SECONDS = 540

## MIN_TIMEOUT_SECONDS

Cloud Functions min timeout value.

**Signature:**  

    MIN_TIMEOUT_SECONDS = 0

## RESET_VALUE

Special configuration value to reset configuration to platform default.

**Signature:**  

    RESET_VALUE: ResetValue

## SUPPORTED_REGIONS

List of all regions supported by Cloud Functions.

**Signature:**  

    SUPPORTED_REGIONS: readonly ["us-central1", "us-east1", "us-east4", "us-west2", "us-west3", "us-west4", "europe-central2", "europe-west1", "europe-west2", "europe-west3", "europe-west6", "asia-east1", "asia-east2", "asia-northeast1", "asia-northeast2", "asia-northeast3", "asia-south1", "asia-southeast1", "asia-southeast2", "northamerica-northeast1", "southamerica-east1", "australia-southeast1"]

## VALID_MEMORY_OPTIONS

List of available memory options supported by Cloud Functions.

**Signature:**  

    VALID_MEMORY_OPTIONS: readonly ["128MB", "256MB", "512MB", "1GB", "2GB", "4GB", "8GB"]

## VPC_EGRESS_SETTINGS_OPTIONS

List of available options for VpcConnectorEgressSettings.

**Signature:**  

    VPC_EGRESS_SETTINGS_OPTIONS: readonly ["VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED", "PRIVATE_RANGES_ONLY", "ALL_TRAFFIC"]