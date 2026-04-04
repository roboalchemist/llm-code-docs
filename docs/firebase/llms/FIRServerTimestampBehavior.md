# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior.md.txt

# FirebaseFirestore Framework Reference

# FIRServerTimestampBehavior

    enum FIRServerTimestampBehavior : NSInteger {}

Controls the return value for server timestamps that have not yet been set to
their final value.
- `
  ``
  ``
  `

  ### [FIRServerTimestampBehaviorNone](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior#/c:@E@FIRServerTimestampBehavior@FIRServerTimestampBehaviorNone)

  `
  `  
  Return `NSNull` for `FieldValue.serverTimestamp()` fields that have not yet
  been set to their final value.  

  #### Declaration

  Objective-C  

      FIRServerTimestampBehaviorNone

- `
  ``
  ``
  `

  ### [FIRServerTimestampBehaviorEstimate](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior#/c:@E@FIRServerTimestampBehavior@FIRServerTimestampBehaviorEstimate)

  `
  `  
  Return a local estimates for `FieldValue.serverTimestamp()`
  fields that have not yet been set to their final value. This estimate will
  likely differ from the final value and may cause these pending values to
  change once the server result becomes available.  

  #### Declaration

  Objective-C  

      FIRServerTimestampBehaviorEstimate

- `
  ``
  ``
  `

  ### [FIRServerTimestampBehaviorPrevious](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior#/c:@E@FIRServerTimestampBehavior@FIRServerTimestampBehaviorPrevious)

  `
  `  
  Return the previous value for `FieldValue.serverTimestamp()` fields that
  have not yet been set to their final value.  

  #### Declaration

  Objective-C  

      FIRServerTimestampBehaviorPrevious