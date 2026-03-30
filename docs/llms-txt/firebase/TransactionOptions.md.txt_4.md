# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/TransactionOptions.md.txt

# FirebaseFirestore Framework Reference

# TransactionOptions

    class TransactionOptions : NSObject, NSCopying

Options to customize the behavior of `Firestore.runTransactionWithOptions()`.
- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/TransactionOptions#/c:objc(cs)FIRTransactionOptions(im)init)


  ` Creates and returns a new `TransactionOptions` object with all properties initialized to their
  default values.

  #### Declaration

  Swift

      init()

  #### Return Value

  The created `TransactionOptions` object.
- `


  ### [maxAttempts](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/TransactionOptions#/c:objc(cs)FIRTransactionOptions(py)maxAttempts)


  ` The maximum number of attempts to commit, after which transaction fails. Default is 5.

  #### Declaration

  Swift

      var maxAttempts: Int { get set }