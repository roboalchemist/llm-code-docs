# Source: https://firebase.google.com/docs/reference/js/storage.listresult.md.txt

# ListResult interface

Result returned by list().

**Signature:**  

    export interface ListResult 

## Properties

|                                                   Property                                                   |                                                             Type                                                             |                                                                                                                       Description                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [items](https://firebase.google.com/docs/reference/js/storage.listresult.md#listresultitems)                 | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface)\[\] | Objects in this directory. You can call getMetadata() and getDownloadUrl() on them.                                                                                                                                                                     |
| [nextPageToken](https://firebase.google.com/docs/reference/js/storage.listresult.md#listresultnextpagetoken) | string                                                                                                                       | If set, there might be more results for this list. Use this token to resume the list.                                                                                                                                                                   |
| [prefixes](https://firebase.google.com/docs/reference/js/storage.listresult.md#listresultprefixes)           | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface)\[\] | References to prefixes (sub-folders). You can call list() on them to get its contents.Folders are implicit based on '/' in the object paths. For example, if a bucket has two objects '/a/b/1' and '/a/b/2', list('/a') will return '/a/b' as a prefix. |

## ListResult.items

Objects in this directory. You can call getMetadata() and getDownloadUrl() on them.

**Signature:**  

    items: StorageReference[];

## ListResult.nextPageToken

If set, there might be more results for this list. Use this token to resume the list.

**Signature:**  

    nextPageToken?: string;

## ListResult.prefixes

References to prefixes (sub-folders). You can call list() on them to get its contents.

Folders are implicit based on '/' in the object paths. For example, if a bucket has two objects '/a/b/1' and '/a/b/2', list('/a') will return '/a/b' as a prefix.

**Signature:**  

    prefixes: StorageReference[];