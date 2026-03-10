# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols.md.txt

# FirebaseStorage Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [FIRStorageTaskManagement](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement)


  ` Defines task operations such as pause, resume, cancel, and enqueue for all tasks.
  All tasks are required to implement enqueue, which begins the task, and may optionally
  implement pause, resume, and cancel, which operate on the task to pause, resume, and cancel
  operations.

  #### Declaration

  Objective-C

      @protocol FIRStorageTaskManagement <NSObject>