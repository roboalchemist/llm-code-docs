# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRTransactionResult.md.txt

# FirebaseDatabase Framework Reference

# FIRTransactionResult


    @interface FIRTransactionResult : NSObject

Used for `runTransactionBlock(_:)`. A `TransactionResult` instance is a
container for the results of the transaction.
- `
  ``
  ``
  `

  ### [+successWithValue:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRTransactionResult#/c:objc(cs)FIRTransactionResult(cm)successWithValue:)

  `
  `  
  Used for `runTransactionBlock(_:)`. Indicates that the new value should be
  saved at this location.  

  #### Declaration

  Objective-C  

      + (nonnull FIRTransactionResult *)successWithValue:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData.html *)value;

  #### Parameters

  |---------------|-------------------------------------------------------------|
  | ` `*value*` ` | A `MutableData` instance containing the new value to be set |

  #### Return Value

  A `TransactionResult` instance that can be used as a return value
  from the block given to `runTransactionBlock(_:)`.
- `
  ``
  ``
  `

  ### [+abort](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRTransactionResult#/c:objc(cs)FIRTransactionResult(cm)abort)

  `
  `  
  Used for `runTransactionBlock(_:)`. Indicates that the current transaction
  should no longer proceed.  

  #### Declaration

  Objective-C  

      + (nonnull FIRTransactionResult *)abort;

  #### Return Value

  A `TransactionResult` instance that can be used as a return value
  from the block given to `runTransactionBlock(_:)`