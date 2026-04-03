# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.md.txt

# FirebaseStorage Framework Reference

# StorageUploadTask

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageUploadTask)
    open class StorageUploadTask: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask.html,
      https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement.html

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

  ### [enqueue()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)enqueue)

  `
  `  
  Prepares a task and begins execution.  

  #### Declaration

  Swift  

      open func enqueue()

- `
  ``
  ``
  `

  ### [pause()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)pause)

  `
  `  
  Pauses a task currently in progress.  

  #### Declaration

  Swift  

      open func pause()

- `
  ``
  ``
  `

  ### [cancel()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)cancel)

  `
  `  
  Cancels a task.  

  #### Declaration

  Swift  

      open func cancel()

- `
  ``
  ``
  `

  ### [resume()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageUploadTask(im)resume)

  `
  `  
  Resumes a paused task.  

  #### Declaration

  Swift  

      open func resume()