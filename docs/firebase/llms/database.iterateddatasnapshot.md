# Source: https://firebase.google.com/docs/reference/js/database.iterateddatasnapshot.md.txt

# IteratedDataSnapshot interface

Represents a child snapshot of a `Reference` that is being iterated over. The key will never be undefined.

**Signature:**  

    export declare interface IteratedDataSnapshot extends DataSnapshot 

**Extends:** [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)

## Properties

|                                                   Property                                                    |  Type  | Description |
|---------------------------------------------------------------------------------------------------------------|--------|-------------|
| [key](https://firebase.google.com/docs/reference/js/database.iterateddatasnapshot.md#iterateddatasnapshotkey) | string |             |

## IteratedDataSnapshot.key

**Signature:**  

    key: string;