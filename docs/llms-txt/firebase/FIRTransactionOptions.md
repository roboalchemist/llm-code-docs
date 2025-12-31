# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransactionOptions.md.txt

# FirebaseFirestore Framework Reference

# FIRTransactionOptions


    @interface FIRTransactionOptions : NSObject <NSCopying>

Options to customize the behavior of `Firestore.runTransactionWithOptions()`.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransactionOptions#/c:objc(cs)FIRTransactionOptions(im)init)

  `
  `  
  Creates and returns a new `TransactionOptions` object with all properties initialized to their
  default values.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  The created `TransactionOptions` object.
- `
  ``
  ``
  `

  ### [maxAttempts](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransactionOptions#/c:objc(cs)FIRTransactionOptions(py)maxAttempts)

  `
  `  
  The maximum number of attempts to commit, after which transaction fails. Default is 5.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSInteger maxAttempts;