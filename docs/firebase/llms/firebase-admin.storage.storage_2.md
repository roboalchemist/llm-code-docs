# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.storage_2.md.txt

# Storage_2 class

The default `Storage` service if no app is provided or the `Storage` service associated with the provided app.

**Signature:**  

    export declare class Storage 

## Properties

|                                                   Property                                                    | Modifiers | Type |                                                   Description                                                    |
|---------------------------------------------------------------------------------------------------------------|-----------|------|------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.storage_2.md#storage_2app) |           | App  | Optional app whose `Storage` service to return. If not provided, the default `Storage` service will be returned. |

## Methods

|                                                          Method                                                           | Modifiers |                 Description                 |
|---------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------|
| [bucket(name)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.storage_2.md#storage_2bucket) |           | Gets a reference to a Cloud Storage bucket. |

## Storage_2.app

Optional app whose `Storage` service to return. If not provided, the default `Storage` service will be returned.

**Signature:**  

    get app(): App;

## Storage_2.bucket()

Gets a reference to a Cloud Storage bucket.

**Signature:**  

    bucket(name?: string): Bucket;

### Parameters

| Parameter |  Type  |                                                     Description                                                     |
|-----------|--------|---------------------------------------------------------------------------------------------------------------------|
| name      | string | Optional name of the bucket to be retrieved. If name is not specified, retrieves a reference to the default bucket. |

**Returns:**

Bucket

A [Bucket](https://cloud.google.com/nodejs/docs/reference/storage/latest/Bucket) instance as defined in the `@google-cloud/storage` package.