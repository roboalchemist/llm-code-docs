# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.md.txt

# FirebaseStorage Framework Reference

# StorageDownloadTask

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageDownloadTask)
    open class StorageDownloadTask : https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask.html, https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement.html

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

  ### [enqueue()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)enqueue)

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

  ### [pause()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)pause)

  `
  `  
  Pauses a task currently in progress. Calling this on a paused task has no effect.  

  #### Declaration

  Swift  

      open func pause()

- `
  ``
  ``
  `

  ### [cancel()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)cancel)

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

  ### [resume()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageDownloadTask(im)resume)

  `
  `  
  Resumes a paused task. Calling this on a running task has no effect.  

  #### Declaration

  Swift  

      open func resume()