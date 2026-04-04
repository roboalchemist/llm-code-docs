# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.md.txt

# FirebaseStorage Framework Reference

# FIRStorageUploadTask


    @interface FIRStorageUploadTask
        : https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask.html <https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement.html>

`StorageUploadTask` implements resumable uploads to a file in Firebase Storage.
Uploads can be returned on completion with a completion callback, and can be monitored
by attaching observers, or controlled by calling `pause()`, `resume()`,
or `cancel()`.
Uploads can be initialized from `Data` in memory, or a URL to a file on disk.
Uploads are performed on a background queue, and callbacks are raised on the developer
specified `callbackQueue` in Storage, or the main queue if unspecified.
- `
  ``
  ``
  `

  ### [-enqueue](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)enqueue)

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

  ### [-pause](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)pause)

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

  ### [-cancel](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)cancel)

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

  ### [-resume](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)resume)

  `
  `  
  Resumes a paused task.  

  #### Declaration

  Objective-C  

      - (void)resume;