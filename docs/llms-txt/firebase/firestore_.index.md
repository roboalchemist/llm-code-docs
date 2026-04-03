# Source: https://firebase.google.com/docs/reference/js/firestore_.index.md.txt

# Index interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Instead of creating cache indexes manually, consider using `enablePersistentCacheIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

The SDK definition of a Firestore index.

**Signature:**  

    export declare interface Index 

## Properties

|                                                 Property                                                  |                                                     Type                                                      |                        Description                        |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [collectionGroup](https://firebase.google.com/docs/reference/js/firestore_.index.md#indexcollectiongroup) | string                                                                                                        | ***(Public Preview)*** The ID of the collection to index. |
| [fields](https://firebase.google.com/docs/reference/js/firestore_.index.md#indexfields)                   | [IndexField](https://firebase.google.com/docs/reference/js/firestore_.indexfield.md#indexfield_interface)\[\] | ***(Public Preview)*** A list of fields to index.         |

## Index.collectionGroup

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The ID of the collection to index.

**Signature:**  

    readonly collectionGroup: string;

## Index.fields

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A list of fields to index.

**Signature:**  

    readonly fields?: IndexField[];