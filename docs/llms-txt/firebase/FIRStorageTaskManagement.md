# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement.md.txt

# FirebaseStorage Framework Reference

# FIRStorageTaskManagement

    @protocol FIRStorageTaskManagement <NSObject>

Defines task operations such as pause, resume, cancel, and enqueue for all tasks.
All tasks are required to implement enqueue, which begins the task, and may optionally
implement pause, resume, and cancel, which operate on the task to pause, resume, and cancel
operations.
- `
  ``
  ``
  `

  ### [-enqueue](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)enqueue)

  `
  `  
  Prepares a task and begins execution.  

  #### Declaration

  Objective-C  

      - (void)enqueue;

- `
  ``
  ``
  `

  ### [-pause](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)pause)

  `
  `  
  Pauses a task currently in progress.  

  #### Declaration

  Objective-C  

      - (void)pause;

- `
  ``
  ``
  `

  ### [-cancel](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)cancel)

  `
  `  
  Cancels a task.  

  #### Declaration

  Objective-C  

      - (void)cancel;

- `
  ``
  ``
  `

  ### [-resume](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement#/c:@M@FirebaseStorage@objc(pl)FIRStorageTaskManagement(im)resume)

  `
  `  
  Resumes a paused task.  

  #### Declaration

  Objective-C  

      - (void)resume;