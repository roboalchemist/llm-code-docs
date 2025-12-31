# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot.md.txt

# FirebaseStorage Framework Reference

# FIRStorageTaskSnapshot


    @interface FIRStorageTaskSnapshot : NSObject

`StorageTaskSnapshot` represents an immutable view of a task.
A snapshot contains a task, storage reference, metadata (if it exists),
progress, and an error (if one occurred).
- `
  ``
  ``
  `

  ### [task](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)task)

  `
  `  
  The task this snapshot represents.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask.html *_Nonnull task;

- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)metadata)

  `
  `  
  Metadata returned by the task, or `nil` if no metadata returned.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable metadata;

- `
  ``
  ``
  `

  ### [reference](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)reference)

  `
  `  
  The `StorageReference` this task operates on.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *_Nonnull reference;

- `
  ``
  ``
  `

  ### [progress](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)progress)

  `
  `  
  An object which tracks the progress of an upload or download.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSProgress *_Nullable progress;

- `
  ``
  ``
  `

  ### [error](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)error)

  `
  `  
  An error raised during task execution, or `nil` if no error occurred.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSError *_Nullable error;

- `
  ``
  ``
  `

  ### [status](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)status)

  `
  `  
  The status of the task.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) enum https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Enums/FIRStorageTaskStatus.html status;

- `
  ``
  ``
  `

  ### [description](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)description)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, copy) NSString * _Nonnull description

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(im)init)

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

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");