# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md.txt

# firebase-functions package

The 2nd gen API for Cloud Functions for Firebase. This SDK supports deep imports. For example, the namespace `pubsub` is available at `firebase-functions/v2` or is directly importable from `firebase-functions/v2/pubsub`.

## Functions

| Function | Description |
|---|---|
| [onInit(callback)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#oninit) | Registers a callback that should be run when in a production environment before executing any functions code. Calling this function more than once leads to undefined behavior. |
| [setGlobalOptions(options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#setglobaloptions) | Sets default options for all functions written using the 2nd gen SDK. |

## Classes

| Class | Description |
|---|---|
| [Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class) | The Cloud Functions interface for events that change state, such as Realtime Database or Cloud Firestore `onWrite` and `onUpdate` events.For more information about the format used to construct `Change` objects, see below. |

## Interfaces

| Interface | Description |
|---|---|
| [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface) | ***(BETA)*** A `CloudEventBase` is the base of a cross-platform format for encoding a serverless event. For more information, see https://github.com/cloudevents/spec. |
| [CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface) | ***(BETA)*** A handler for CloudEvents. |
| [EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface) | Additional fields that can be set on any event-handling function. |
| [GlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptions_interface) | `GlobalOptions` are options that can be set across an entire project. These options are common to HTTPS and event handling functions. |

## Namespaces

| Namespace | Description |
|---|---|
| [alerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md#alerts_namespace) |   |
| [database](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#database_namespace) |   |
| [dataconnect](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnect_namespace) |   |
| [eventarc](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.md#eventarc_namespace) |   |
| [firestore](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestore_namespace) |   |
| [https](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#https_namespace) |   |
| [identity](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identity_namespace) |   |
| [params](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#params_namespace) |   |
| [pubsub](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.md#pubsub_namespace) |   |
| [remoteConfig](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfig_namespace) |   |
| [scheduler](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.md#scheduler_namespace) |   |
| [storage](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storage_namespace) |   |
| [tasks](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.md#tasks_namespace) |   |
| [testLab](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlab_namespace) |   |

## Variables

| Variable | Description |
|---|---|
| [app](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#app) |   |
| [config](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#config) |   |
| [logger](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#logger) | Logger object containing all logging methods.Mockable for testing purposes. |
| [traceContext](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#tracecontext) |   |

## Type Aliases

| Type Alias | Description |
|---|---|
| [IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) | List of available options for `IngressSettings`. |
| [MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) | List of available memory options supported by Cloud Functions. |
| [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof) | A type that maps all parameter capture groups into keys of a record. For example, ParamsOf\<"users/{uid}"\> is { uid: string } ParamsOf\<"users/{uid}/logs/{log}"\> is { uid: string; log: string } ParamsOf\<"some/static/data"\> is {}For flexibility reasons, ParamsOf is Record\<string, string\> |
| [SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) | List of all regions supported by Cloud Functions (2nd gen). |
| [VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) | List of available options for `VpcConnectorEgressSettings`. |

## onInit()

Registers a callback that should be run when in a production environment before executing any functions code. Calling this function more than once leads to undefined behavior.

**Signature:**

    export declare function onInit(callback: () => unknown): void;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| callback | () =\> unknown | initialization callback to be run before any function executes. |

**Returns:**

void

## setGlobalOptions()

Sets default options for all functions written using the 2nd gen SDK.

**Signature:**

    export declare function setGlobalOptions(options: GlobalOptions): void;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [GlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptions_interface) | Options to set as default |

**Returns:**

void

## app

**Signature:**

    app: {
        setEmulatedAdminApp: typeof setEmulatedAdminApp;
    }

## config

> > [!WARNING]
> > **Warning:** This API is now obsolete.
>
> `functions.config()` has been removed in firebase-functions v7. Migrate to environment parameters using the `params` module immediately. Migration guide: https://firebase.google.com/docs/functions/config-env#migrate-config

**Signature:**

    config: never

## logger

Logger object containing all logging methods.

Mockable for testing purposes.

**Signature:**

    logger: {
        write: typeof write;
        debug: typeof debug;
        log: typeof log;
        info: typeof info;
        warn: typeof warn;
        error: typeof error;
    }

## traceContext

**Signature:**

    traceContext: AsyncLocalStorage<TraceContext>

## IngressSetting

List of available options for `IngressSettings`.

**Signature:**

    export type IngressSetting = "ALLOW_ALL" | "ALLOW_INTERNAL_ONLY" | "ALLOW_INTERNAL_AND_GCLB";

## MemoryOption

List of available memory options supported by Cloud Functions.

**Signature:**

    export type MemoryOption = "128MiB" | "256MiB" | "512MiB" | "1GiB" | "2GiB" | "4GiB" | "8GiB" | "16GiB" | "32GiB";

## ParamsOf

A type that maps all parameter capture groups into keys of a record. For example, ParamsOf\<"users/{uid}"\> is { uid: string } ParamsOf\<"users/{uid}/logs/{log}"\> is { uid: string; log: string } ParamsOf\<"some/static/data"\> is {}

For flexibility reasons, ParamsOf is Record\<string, string\>

**Signature:**

    export type ParamsOf<PathPattern extends string | Expression<string>> = PathPattern extends Expression<string> ? Record<string, string> : string extends PathPattern ? Record<string, string> : {
        [Key in VarName<Split<NullSafe<Exclude<PathPattern, Expression<string>>>, "/">[number]>]: string;
    };

## SupportedRegion

List of all regions supported by Cloud Functions (2nd gen).

**Signature:**

    export type SupportedRegion = "asia-east1" | "asia-northeast1" | "asia-northeast2" | "europe-north1" | "europe-west1" | "europe-west4" | "us-central1" | "us-east1" | "us-east4" | "us-west1" | "asia-east2" | "asia-northeast3" | "asia-southeast1" | "asia-southeast2" | "asia-south1" | "australia-southeast1" | "europe-central2" | "europe-west2" | "europe-west3" | "europe-west6" | "northamerica-northeast1" | "southamerica-east1" | "us-west2" | "us-west3" | "us-west4";

## VpcEgressSetting

List of available options for `VpcConnectorEgressSettings`.

**Signature:**

    export type VpcEgressSetting = "PRIVATE_RANGES_ONLY" | "ALL_TRAFFIC";