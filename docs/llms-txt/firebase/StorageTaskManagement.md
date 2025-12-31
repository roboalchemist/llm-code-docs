# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement.md.txt

# FirebaseStorage Framework Reference

# StorageTaskManagement

    @objc(FIRStorageTaskManagement)
    public protocol StorageTaskManagement : NSObjectProtocol

Defines task operations such as pause, resume, cancel, and enqueue for all tasks.

All tasks are required to implement enqueue, which begins the task, and may optionally
implement pause, resume, and cancel, which operate on the task to pause, resume, and cancel
operations.
- `
  ``
  ``
  `

  ### [enqueue()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)enqueue)

  `
  `  
  Prepares a task and begins execution.  

  #### Declaration

  Swift  

      @objc
      func enqueue()

- `
  ``
  ``
  `

  ### [pause()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)pause)

  `
  `  
  Pauses a task currently in progress.  

  #### Declaration

  Swift  

      @objc
      optional func pause()

- `
  ``
  ``
  `

  ### [cancel()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)cancel)

  `
  `  
  Cancels a task.  

  #### Declaration

  Swift  

      @objc
      optional func cancel()

- `
  ``
  ``
  `

  ### [resume()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)resume)

  `
  `  
  Resumes a paused task.  

  #### Declaration

  Swift  

      @objc
      optional func resume()