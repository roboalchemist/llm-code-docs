# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md.txt

# CloudFunction interface

The function type for all non-HTTPS triggers. This should be exported from your JavaScript file to define a Cloud Function.

This type is a special JavaScript function which takes a templated `LegacyEvent` object as its only argument.

**Signature:**

    export interface CloudFunction<T> extends Runnable<T> 

**Extends:** [Runnable](https://firebase.google.com/docs/reference/functions/firebase-functions.runnable.md#runnable_interface)\<T\>

## Properties

| Property | Type | Description |
|---|---|---|
| [__endpoint](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction__endpoint) | ManifestEndpoint |   |
| [__requiredAPIs](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction__requiredapis) | ManifestRequiredAPI\[\] |   |
| [__trigger](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction__trigger) | TriggerAnnotation |   |

## CloudFunction.__endpoint

**Signature:**

    __endpoint: ManifestEndpoint;

## CloudFunction.__requiredAPIs

**Signature:**

    __requiredAPIs?: ManifestRequiredAPI[];

## CloudFunction.__trigger

**Signature:**

    __trigger: TriggerAnnotation;