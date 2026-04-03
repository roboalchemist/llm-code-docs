# Source: https://firebase.google.com/docs/reference/js/firestore_.indexconfiguration.md.txt

# IndexConfiguration interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Instead of creating cache indexes manually, consider using `enablePersistentCacheIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

A list of Firestore indexes to speed up local query execution.

See [JSON Format](https://firebase.google.com/docs/reference/firestore/indexes/#json_format) for a description of the format of the index definition.

**Signature:**  

    export declare interface IndexConfiguration 

## Properties

|                                                      Property                                                       |                                              Type                                              |                       Description                       |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [indexes](https://firebase.google.com/docs/reference/js/firestore_.indexconfiguration.md#indexconfigurationindexes) | [Index](https://firebase.google.com/docs/reference/js/firestore_.index.md#index_interface)\[\] | ***(Public Preview)*** A list of all Firestore indexes. |

## IndexConfiguration.indexes

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A list of all Firestore indexes.

**Signature:**  

    readonly indexes?: Index[];