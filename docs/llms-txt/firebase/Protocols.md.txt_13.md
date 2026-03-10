# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols.md.txt

# FirebaseStorage Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [StorageTaskManagement](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement)


  ` Defines task operations such as pause, resume, cancel, and enqueue for all tasks.

  All tasks are required to implement enqueue, which begins the task, and may optionally
  implement pause, resume, and cancel, which operate on the task to pause, resume, and cancel
  operations.

  #### Declaration

  Swift

      @objc(FIRStorageTaskManagement)
      public protocol StorageTaskManagement : NSObjectProtocol