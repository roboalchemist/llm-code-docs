# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot.md.txt

# FirebaseStorage Framework Reference

# StorageTaskSnapshot

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageTaskSnapshot)
    open class StorageTaskSnapshot : NSObject

`StorageTaskSnapshot` represents an immutable view of a task.
A snapshot contains a task, storage reference, metadata (if it exists),
progress, and an error (if one occurred).
- `
  ``
  ``
  `

  ### [task](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)task)

  `
  `  
  The task this snapshot represents.  

  #### Declaration

  Swift  

      @objc
      public let task: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask.html

- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)metadata)

  `
  `  
  Metadata returned by the task, or `nil` if no metadata returned.  

  #### Declaration

  Swift  

      @objc
      public let metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html?

- `
  ``
  ``
  `

  ### [reference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)reference)

  `
  `  
  The [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html) this task operates on.  

  #### Declaration

  Swift  

      @objc
      public let reference: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html

- `
  ``
  ``
  `

  ### [progress](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)progress)

  `
  `  
  An object which tracks the progress of an upload or download.  

  #### Declaration

  Swift  

      @objc
      public let progress: Progress?

- `
  ``
  ``
  `

  ### [error](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)error)

  `
  `  
  An error raised during task execution, or `nil` if no error occurred.  

  #### Declaration

  Swift  

      @objc
      public let error: Error?

- `
  ``
  ``
  `

  ### [status](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)status)

  `
  `  
  The status of the task.  

  #### Declaration

  Swift  

      @objc
      public let status: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageTaskStatus.html

[## NSObject overrides](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/NSObject-overrides)

- `
  ``
  ``
  `

  ### [description](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot#/c:@M@FirebaseStorage@objc(cs)FIRStorageTaskSnapshot(py)description)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override public var description: String { get }