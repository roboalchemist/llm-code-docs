# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask.md.txt

# FirebaseStorage Framework Reference

# StorageObservableTask

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageObservableTask)
    open class StorageObservableTask : https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask.html

An extended [StorageTask](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask.html) providing observable semantics that can be used for responding to changes
in task state.

Observers produce a `StorageHandle`, which is used to keep track of and remove specific
observers at a later date.
- `
  ``
  ``
  `

  ### [observe(_:handler:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)observeStatus:handler:)

  `
  `  
  Observes changes in the upload status: Resume, Pause, Progress, Success, and Failure.  

  #### Declaration

  Swift  

      @discardableResult
      @objc(observeStatus:handler:)
      open func observe(_ status: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageTaskStatus.html,
                        handler: @escaping (https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot.html) -> Void) -> String

  #### Parameters

  |-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*status*` `  | The [StorageTaskStatus](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageTaskStatus.html) change to observe.                                                                              |
  | ` `*handler*` ` | A callback that fires every time the status event occurs, containing a [StorageTaskSnapshot](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot.html) describing task state. |

  #### Return Value

  A task handle that can be used to remove the observer at a later date.
- `
  ``
  ``
  `

  ### [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)removeObserverWithHandle:)

  `
  `  
  Removes the single observer with the provided handle.  

  #### Declaration

  Swift  

      @objc(removeObserverWithHandle:)
      open func removeObserver(withHandle handle: String)

  #### Parameters

  |----------------|-----------------------------------|
  | ` `*handle*` ` | The handle of the task to remove. |

- `
  ``
  ``
  `

  ### [removeAllObservers(for:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)removeAllObserversForStatus:)

  `
  `  
  Removes all observers for a single status.  

  #### Declaration

  Swift  

      @objc(removeAllObserversForStatus:)
      open func removeAllObservers(for status: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageTaskStatus.html)

  #### Parameters

  |----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*status*` ` | A [StorageTaskStatus](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageTaskStatus.html) to remove all listeners for. |

- `
  ``
  ``
  `

  ### [removeAllObservers()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)removeAllObservers)

  `
  `  
  Removes all observers.  

  #### Declaration

  Swift  

      @objc
      open func removeAllObservers()