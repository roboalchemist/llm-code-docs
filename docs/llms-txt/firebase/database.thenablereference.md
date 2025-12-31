# Source: https://firebase.google.com/docs/reference/js/database.thenablereference.md.txt

# ThenableReference interface

A `Promise` that can also act as a `DatabaseReference` when returned by [push()](https://firebase.google.com/docs/reference/js/database.md#push_c74661c). The reference is available immediately and the `Promise` resolves as the write to the backend completes.

**Signature:**  

    export declare interface ThenableReference extends DatabaseReference, Pick<Promise<DatabaseReference>, 'then' | 'catch'> 

**Extends:** [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface), Pick\<Promise\<[DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface)\>, 'then' \| 'catch'\>

## Properties

|                                                   Property                                                    |                                                             Type                                                             | Description |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------|
| [key](https://firebase.google.com/docs/reference/js/database.thenablereference.md#thenablereferencekey)       | string                                                                                                                       |             |
| [parent](https://firebase.google.com/docs/reference/js/database.thenablereference.md#thenablereferenceparent) | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) |             |

## ThenableReference.key

**Signature:**  

    key: string;

## ThenableReference.parent

**Signature:**  

    parent: DatabaseReference;