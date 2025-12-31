# Source: https://firebase.google.com/docs/reference/js/firestore_.transactionoptions.md.txt

# TransactionOptions interface

Options to customize transaction behavior.

**Signature:**  

    export declare interface TransactionOptions 

## Properties

|                                                          Property                                                           |  Type  |                                    Description                                     |
|-----------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------|
| [maxAttempts](https://firebase.google.com/docs/reference/js/firestore_.transactionoptions.md#transactionoptionsmaxattempts) | number | Maximum number of attempts to commit, after which transaction fails. Default is 5. |

## TransactionOptions.maxAttempts

Maximum number of attempts to commit, after which transaction fails. Default is 5.

**Signature:**  

    readonly maxAttempts?: number;