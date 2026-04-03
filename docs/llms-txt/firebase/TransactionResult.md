# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/TransactionResult.md.txt

# FirebaseDatabase Framework Reference

# TransactionResult

    class TransactionResult : NSObject

Used for `runTransactionBlock(_:)`. A `TransactionResult` instance is a
container for the results of the transaction.
- `
  ``
  ``
  `

  ### [success(withValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/TransactionResult#/c:objc(cs)FIRTransactionResult(cm)successWithValue:)

  `
  `  
  Used for `runTransactionBlock(_:)`. Indicates that the new value should be
  saved at this location.  

  #### Declaration

  Swift  

      class func success(withValue value: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData.html) -> TransactionResult

  #### Parameters

  |---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` ` | A [MutableData](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData.html) instance containing the new value to be set |

  #### Return Value

  A `TransactionResult` instance that can be used as a return value
  from the block given to `runTransactionBlock(_:)`.
- `
  ``
  ``
  `

  ### [abort()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/TransactionResult#/c:objc(cs)FIRTransactionResult(cm)abort)

  `
  `  
  Used for `runTransactionBlock(_:)`. Indicates that the current transaction
  should no longer proceed.  

  #### Declaration

  Swift  

      class func abort() -> TransactionResult

  #### Return Value

  A `TransactionResult` instance that can be used as a return value
  from the block given to `runTransactionBlock(_:)`