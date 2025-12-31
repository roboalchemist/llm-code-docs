# Source: https://firebase.google.com/docs/reference/js/firestore_.indexfield.md.txt

# IndexField interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Instead of creating cache indexes manually, consider using `enablePersistentCacheIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

A single field element in an index configuration.

**Signature:**  

    export declare interface IndexField 

## Properties

|                                                  Property                                                   |            Type             |                                                                                                Description                                                                                                 |
|-------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [arrayConfig](https://firebase.google.com/docs/reference/js/firestore_.indexfield.md#indexfieldarrayconfig) | 'CONTAINS'                  | ***(Public Preview)*** What type of array index to create. Set to `CONTAINS` for `array-contains` and `array-contains-any` indexes.Only one of `arrayConfig` or `order` should be set;                     |
| [fieldPath](https://firebase.google.com/docs/reference/js/firestore_.indexfield.md#indexfieldfieldpath)     | string                      | ***(Public Preview)*** The field path to index.                                                                                                                                                            |
| [order](https://firebase.google.com/docs/reference/js/firestore_.indexfield.md#indexfieldorder)             | 'ASCENDING' \| 'DESCENDING' | ***(Public Preview)*** What type of array index to create. Set to `ASCENDING` or 'DESCENDING` for `==`, `!=`, `\<=`, `\<=`, `in` and `not-in\` filters.Only one of `arrayConfig` or `order` should be set. |

## IndexField.arrayConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

What type of array index to create. Set to `CONTAINS` for `array-contains` and `array-contains-any` indexes.

Only one of `arrayConfig` or `order` should be set;

**Signature:**  

    readonly arrayConfig?: 'CONTAINS';

## IndexField.fieldPath

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The field path to index.

**Signature:**  

    readonly fieldPath: string;

## IndexField.order

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

What type of array index to create. Set to `ASCENDING` or 'DESCENDING`for`==`,`!=`,`\<=`,`\<=`,`in`and`not-in\` filters.

Only one of `arrayConfig` or `order` should be set.

**Signature:**  

    readonly order?: 'ASCENDING' | 'DESCENDING';