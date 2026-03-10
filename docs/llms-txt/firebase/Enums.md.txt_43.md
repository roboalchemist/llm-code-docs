# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums.md.txt

# FirebaseStorage Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [StorageTaskStatus](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageTaskStatus)


  ` Undocumented

  #### Declaration

  Swift

      @objc(FIRStorageTaskStatus)
      public enum StorageTaskStatus : Int

- `


  ### [StorageErrorCode](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode)


  ` Adds wrappers for common Firebase Storage errors (including creating errors from GCS errors).
  For more information on unwrapping GCS errors, see the GCS errors docs:
  <https://cloud.google.com/storage/docs/json_api/v1/status-codes>
  This is never publicly exposed to end developers (as they will simply see an NSError).

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageErrorCode)
      public enum StorageErrorCode : Int, Swift.Error

- `


  ### [StorageError](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError)


  ` Firebase Storage errors

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      public enum StorageError : Error, CustomNSError