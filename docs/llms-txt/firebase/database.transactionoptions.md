# Source: https://firebase.google.com/docs/reference/js/database.transactionoptions.md.txt

# TransactionOptions interface

An options object to configure transactions.

**Signature:**  

    export declare interface TransactionOptions 

## Properties

|                                                          Property                                                           |  Type   |                                                                                                                                          Description                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [applyLocally](https://firebase.google.com/docs/reference/js/database.transactionoptions.md#transactionoptionsapplylocally) | boolean | By default, events are raised each time the transaction update function runs. So if it is run multiple times, you may see intermediate states. You can set this to false to suppress these intermediate states and instead wait until the transaction has completed before events are raised. |

## TransactionOptions.applyLocally

By default, events are raised each time the transaction update function runs. So if it is run multiple times, you may see intermediate states. You can set this to false to suppress these intermediate states and instead wait until the transaction has completed before events are raised.

**Signature:**  

    readonly applyLocally?: boolean;