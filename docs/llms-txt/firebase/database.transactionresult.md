# Source: https://firebase.google.com/docs/reference/js/database.transactionresult.md.txt

# TransactionResult class

A type for the resolve value of [runTransaction()](https://firebase.google.com/docs/reference/js/database.md#runtransaction_a3641e5).

**Signature:**  

    export declare class TransactionResult 

## Properties

|                                                      Property                                                       | Modifiers |                                                   Type                                                    |                     Description                     |
|---------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [committed](https://firebase.google.com/docs/reference/js/database.transactionresult.md#transactionresultcommitted) |           | boolean                                                                                                   | Whether the transaction was successfully committed. |
| [snapshot](https://firebase.google.com/docs/reference/js/database.transactionresult.md#transactionresultsnapshot)   |           | [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class) | The resulting data snapshot.                        |

## Methods

|                                                     Method                                                      | Modifiers |                        Description                         |
|-----------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/js/database.transactionresult.md#transactionresulttojson) |           | Returns a JSON-serializable representation of this object. |

## TransactionResult.committed

Whether the transaction was successfully committed.

**Signature:**  

    readonly committed: boolean;

## TransactionResult.snapshot

The resulting data snapshot.

**Signature:**  

    readonly snapshot: DataSnapshot;

## TransactionResult.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object