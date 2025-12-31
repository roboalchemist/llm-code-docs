# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask.md.txt

# FirebaseStorage Framework Reference

# FIRStorageTask


    @interface FIRStorageTask : NSObject

A superclass to all Storage tasks, including `StorageUploadTask`
and `StorageDownloadTask`, to provide state transitions, event raising, and common storage
for metadata and errors.
Callbacks are always fired on the developer-specified callback queue.
If no queue is specified, it defaults to the main queue.
This class is thread-safe.
- `
  ``
  ``
  `

  ### [snapshot](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageTask(py)snapshot)

  `
  `  
  An immutable view of the task and associated metadata, progress, error, etc.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot.html *_Nonnull snapshot;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageTask(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init SWIFT_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageTask(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");