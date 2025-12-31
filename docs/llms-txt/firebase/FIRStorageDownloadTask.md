# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask.md.txt

# FirebaseStorage Framework Reference

# FIRStorageDownloadTask


    @interface FIRStorageDownloadTask
        : https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask.html <https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement.html>

`StorageDownloadTask` implements resumable downloads from an object in Firebase Storage.
Downloads can be returned on completion with a completion handler, and can be monitored
by attaching observers, or controlled by calling `pause()`, `resume()`,
or `cancel()`.
Downloads can currently be returned as `Data` in memory, or as a `URL` to a file on disk.
Downloads are performed on a background queue, and callbacks are raised on the developer
specified `callbackQueue` in Storage, or the main queue if left unspecified.
- `
  ``
  ``
  `

  ### [-enqueue](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)enqueue)

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

  ### [-pause](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)pause)

  `
  `  
  Pauses a task currently in progress. Calling this on a paused task has no effect.  

  #### Declaration

  Objective-C  

      - (void)pause;

- `
  ``
  ``
  `

  ### [-cancel](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)cancel)

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

  ### [-resume](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)resume)

  `
  `  
  Resumes a paused task. Calling this on a running task has no effect.  

  #### Declaration

  Objective-C  

      - (void)resume;