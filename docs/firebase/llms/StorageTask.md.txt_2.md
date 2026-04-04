# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask.md.txt

# FirebaseStorage Framework Reference

# StorageTask

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageTask)
    open class StorageTask : NSObject

A superclass to all Storage tasks, including `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`
and `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html`, to provide state transitions, event raising, and common storage
for metadata and errors.

Callbacks are always fired on the developer-specified callback queue.
If no queue is specified, it defaults to the main queue.
This class is thread-safe.
- `


  ### [snapshot](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageTask(py)snapshot)


  ` An immutable view of the task and associated metadata, progress, error, etc.

  #### Declaration

  Swift

      @objc
      public var snapshot: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot.html { get }