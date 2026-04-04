# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Enums.md.txt

# FirebaseStorage Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRStorageErrorCode](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Enums/FIRStorageErrorCode)


  ` Adds wrappers for common Firebase Storage errors (including creating errors from GCS errors).
  For more information on unwrapping GCS errors, see the GCS errors docs:
  <https://cloud.google.com/storage/docs/json_api/v1/status-codes>
  This is never publicly exposed to end developers (as they will simply see an NSError).

  #### Declaration

  Objective-C

      enum FIRStorageErrorCode : NSInteger {}

- `


  ### [FIRStorageTaskStatus](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Enums/FIRStorageTaskStatus)


  ` Undocumented

  #### Declaration

  Objective-C

      SWIFT_ENUM_NAMED(NSInteger, FIRStorageTaskStatus, "StorageTaskStatus", open) {
        FIRStorageTaskStatusUnknown = 0,
        FIRStorageTaskStatusResume = 1,
        FIRStorageTaskStatusProgress = 2,
        FIRStorageTaskStatusPause = 3,
        FIRStorageTaskStatusSuccess = 4,
        FIRStorageTaskStatusFailure = 5,
      }