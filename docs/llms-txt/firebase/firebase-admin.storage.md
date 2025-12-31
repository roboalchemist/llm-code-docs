# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.md.txt

# firebase-admin.storage package

Cloud Storage for Firebase.

## Functions

|                                                            Function                                                            |                                                                                                               Description                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getDownloadURL(file)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.md#getdownloadurl_bc488a6) | Gets the download URL for the given [File](https://cloud.google.com/nodejs/docs/reference/storage/latest/storage/file).                                                                                                                  |
| [getStorage(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.md#getstorage_8a40afc)          | Gets the service for the default app or a given app.`getStorage()` can be called with no arguments to access the default app's `Storage` service or as `getStorage(app)` to access the `Storage` service associated with a specific app. |

## Classes

|                                                         Class                                                          |                                                  Description                                                   |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [Storage_2](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.storage_2.md#storage_2_class) | The default `Storage` service if no app is provided or the `Storage` service associated with the provided app. |

## getDownloadURL(file)

Gets the download URL for the given [File](https://cloud.google.com/nodejs/docs/reference/storage/latest/storage/file).

**Signature:**  

    export declare function getDownloadURL(file: File): Promise<string>;

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| file      | File |             |

**Returns:**

Promise\<string\>

### Example

    // Get the downloadUrl for a given file ref
    const storage = getStorage();
    const myRef = ref(storage, 'images/mountains.jpg');
    const downloadUrl = await getDownloadURL(myRef);

## getStorage(app)

Gets the service for the default app or a given app.

`getStorage()` can be called with no arguments to access the default app's `Storage` service or as `getStorage(app)` to access the `Storage` service associated with a specific app.

**Signature:**  

    export declare function getStorage(app?: App): Storage;

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| app       | App  |             |

**Returns:**

[Storage](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage.storage_2.md#storage_2_class)

### Example 1

    // Get the Storage service for the default app
    const defaultStorage = getStorage();

### Example 2

    // Get the Storage service for a given app
    const otherStorage = getStorage(otherApp);